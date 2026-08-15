#!/usr/bin/env python3
"""
Generate per-domain HTML quiz pages from both practice exam Markdown files.
Combines all 240 questions, classifies each into one of 5 AWS AI Practitioner
exam domains, then emits one self-contained HTML file per domain.

Usage: python generate_domains.py
"""

import re, json, html, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXAM_DIR   = os.path.dirname(SCRIPT_DIR)

MD_FILES = [
    os.path.join(EXAM_DIR, "practice-exam.md"),
    os.path.join(EXAM_DIR, "practice-exam-2.md"),
]

DOMAINS = [
    {
        "id": "domain1",
        "num": 1,
        "title": "Domain 1: Fundamentals of AI and ML",
        "short": "AI & ML Fundamentals",
        "color": "#1565C0",
        "filename": "domain1-ai-ml-fundamentals.html",
    },
    {
        "id": "domain2",
        "num": 2,
        "title": "Domain 2: Fundamentals of Generative AI",
        "short": "Generative AI Fundamentals",
        "color": "#6A1B9A",
        "filename": "domain2-generative-ai.html",
    },
    {
        "id": "domain3",
        "num": 3,
        "title": "Domain 3: Applications of Foundation Models",
        "short": "Foundation Model Applications",
        "color": "#00695C",
        "filename": "domain3-foundation-models.html",
    },
    {
        "id": "domain4",
        "num": 4,
        "title": "Domain 4: Guidelines for Responsible AI",
        "short": "Responsible AI",
        "color": "#E65100",
        "filename": "domain4-responsible-ai.html",
    },
    {
        "id": "domain5",
        "num": 5,
        "title": "Domain 5: Security, Compliance, and Governance",
        "short": "Security & Governance",
        "color": "#B71C1C",
        "filename": "domain5-security-governance.html",
    },
]

# ---------------------------------------------------------------------------
# Domain classifier
# ---------------------------------------------------------------------------
# Each rule is (domain_num, pattern) — first match wins.
# Patterns are matched case-insensitively against the full question text + options + explanation.

RULES = [
    # ---- Domain 5: Security, Compliance, Governance ----
    (5, r"\bIAM\b|\bKMS\b|\bVPC\b|\bprivate subnet|\bencrypt|\bTLS\b|\bSSL\b|\bShared Responsibility|\bGDPR\b|\bHIPAA\b|\bdata governance|\bdata residency|\bcompliance|\bsecurity group|\bpolicy.*access|\baccess.*policy|\baudit.*trail|\bCloudTrail\b|\bcloudtrail\b|\bMacie\b|\bGuardDuty|\bSecurity Hub|\bdata provenance|\bprivacy.*regulation|\bpersonal.*data.*regulat"),

    # ---- Domain 4: Responsible AI ----
    (4, r"\bresponsible AI|\bfairness|\bbias(?! variance|\b.*model complexity)|\bexplainab|\binterpretab|\btransparency|\baccountability|\brobustness|\bhuman.?in.?the.?loop|\bhuman oversight|\bethic|\bSageMaker Clarify|\bClarify\b|\bmodel card|\bdiscriminator|\bequit|\bPII\b|\bprivacy(?!.*regulation)|\bwatermark|\bcontent disclosure|\bcontestab|\bharm|\bmisuse|\bunintended|\bsafety.*AI|\bAI.*safety|\btoxic|\bsentinelAI|\bgoverned|\bdisparat"),

    # ---- Domain 3: Applications of Foundation Models ----
    (3, r"\bRAG\b|\bretrieval.?augmented|\bKnowledge Base|\bvector database|\bvector store|\bchunking|\bembedding(?!s.*Word2Vec)|\bBedrock Agent|\bAgent.*Bedrock|\bfine.?tun|\bprompt engineering|\bfew.?shot|\bzero.?shot|\bone.?shot|\bchain.?of.?thought|\bsystem prompt|\binstruction.*tun|\bRLHF|\breinforcement.*human feedback|\bfoundation model.*deploy|\bdeploy.*foundation|\bevaluation.*LLM|\bmodel.*evaluat|\bBedrock.*Guardrail|\bGuardrail.*Bedrock|\bPartyRock|\bBedrock.*playground|\bcontext window|\bmap.?reduce.*summar|\bhierarchical.*summar|\btool use\b|\bfunction call|\bAgents for Bedrock|\bProduction Variant|\bSageMaker.*endpoint.*model"),

    # ---- Domain 2: Generative AI Fundamentals ----
    (2, r"\bfoundation model\b|\bLLM\b|\blarge language model|\bgenerative AI|\bGenerative AI|\bgenAI\b|\bBedrock\b|\btransformer\b|\battention mechanism|\bself.?attention|\bencoder.?decoder|\btoken(?:izer|ization|s\b)|\btemperature\b.*generat|\bTop.?[pPk]\b|\bnucleus sampling|\bhallucinat|\bword embedding|\bWord2Vec|\bGloVe|\bGPT\b|\bClaude\b|\bTitan\b|\bLlama\b|\bdiffusion model|\bimage generat|\bAmazon Q\b|\bSageMaker JumpStart|\bJumpStart\b"),

    # ---- Domain 1: AI & ML Fundamentals (catch-all) ----
    (1, r".*"),
]


def classify(q: dict) -> int:
    """Return domain number 1-5 for a question."""
    corpus = " ".join([
        q["text"],
        " ".join(o["text"] for o in q["options"]),
        q["explanation"],
    ])
    for domain_num, pattern in RULES:
        if re.search(pattern, corpus, re.IGNORECASE):
            return domain_num
    return 1  # fallback


# ---------------------------------------------------------------------------
# Markdown parser (reused from generate.py)
# ---------------------------------------------------------------------------

def parse_correct_answers(answer_line: str) -> list:
    line = re.sub(r"^Correct Answers?:\s*", "", answer_line, flags=re.IGNORECASE).strip()
    letters = re.findall(r"\b([A-E])\)", line)
    return list(dict.fromkeys(letters))


def parse_md(path: str, source_label: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    raw_blocks = re.split(r"\n---\n", content)
    questions = []

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        q_match = re.match(
            r"\*\*Question\s+(\d+)\*\*\s*\n+(.*?)(?=\n[A-E]\)|\n<details)",
            block, re.DOTALL
        )
        if not q_match:
            continue

        q_num  = int(q_match.group(1))
        q_text = q_match.group(2).strip()

        options_raw = re.findall(r"^([A-E])\)\s+(.+)$", block, re.MULTILINE)
        options = [{"letter": l, "text": t.strip()} for l, t in options_raw]

        details_match = re.search(r"<details>(.*?)</details>", block, re.DOTALL)
        if not details_match:
            continue
        details_content = details_match.group(1).strip()
        details_content = re.sub(r"<summary>.*?</summary>", "", details_content, flags=re.DOTALL).strip()

        lines = [l for l in details_content.split("\n") if l.strip()]
        answer_line = ""
        explanation_lines = []
        for i, line in enumerate(lines):
            if re.match(r"Correct Answers?:", line, re.IGNORECASE):
                answer_line = line
                explanation_lines = lines[i + 1:]
                break

        if not answer_line:
            answer_line = lines[0] if lines else ""
            explanation_lines = lines[1:] if len(lines) > 1 else []

        correct_letters = parse_correct_answers(answer_line)

        explanation = "\n".join(explanation_lines).strip()
        explanation = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", explanation)

        multi_select = bool(
            re.search(r"Select TWO|Choose two|select two|choose two", q_text, re.IGNORECASE)
        )

        if multi_select and len(correct_letters) < 2 and explanation:
            for opt in options:
                if opt["letter"] not in correct_letters:
                    core = re.split(r"\(", opt["text"])[0].strip()
                    if len(core) >= 8 and re.search(re.escape(core), explanation, re.IGNORECASE):
                        correct_letters.append(opt["letter"])
                    elif re.search(r"\b" + re.escape(opt["letter"]) + r"\)", explanation):
                        correct_letters.append(opt["letter"])
                if len(correct_letters) >= 2:
                    break

        questions.append({
            "num": q_num,
            "source": source_label,
            "text": q_text,
            "options": options,
            "correct": correct_letters,
            "explanation": explanation,
            "multi": multi_select,
        })

    questions.sort(key=lambda q: q["num"])
    return questions


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<style>
  :root {{
    --accent:  {color};
    --navy:    #232F3E;
    --correct-bg: #d4edda; --correct-border: #28a745;
    --wrong-bg:   #f8d7da; --wrong-border:   #dc3545;
    --neutral-bg: #f4f6f8; --card-bg: #ffffff;
    --radius: 10px; --shadow: 0 2px 8px rgba(0,0,0,0.08);
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          background: var(--neutral-bg); color: #222; line-height: 1.6; }}

  header {{
    background: var(--navy); color: #fff; padding: 16px 24px;
    position: sticky; top: 0; z-index: 100;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
  }}
  header h1 {{ font-size: 1rem; font-weight: 700; }}
  header h1 span {{ color: {color}; }}
  .header-meta {{ display: flex; justify-content: space-between; align-items: center; margin-top: 6px; flex-wrap: wrap; gap: 8px; }}
  #progress-bar-wrap {{ flex: 1; background: rgba(255,255,255,0.2); border-radius: 4px; height: 6px; min-width: 120px; }}
  #progress-bar {{ height: 6px; border-radius: 4px; background: {color}; transition: width 0.3s; width: 0%; }}
  #progress-text {{ font-size: 0.8rem; color: #ccc; white-space: nowrap; }}
  .back-link {{ font-size: 0.8rem; color: #aaa; text-decoration: none; margin-right: 12px; }}
  .back-link:hover {{ color: #fff; }}

  main {{ max-width: 860px; margin: 28px auto; padding: 0 16px 60px; }}

  .domain-badge {{
    display: inline-block; background: {color}; color: #fff;
    border-radius: 6px; padding: 6px 16px; font-size: 0.85rem;
    font-weight: 700; margin-bottom: 24px;
  }}

  .question-card {{
    background: var(--card-bg); border-radius: var(--radius);
    box-shadow: var(--shadow); padding: 24px; margin-bottom: 28px;
    border-left: 5px solid #ddd; transition: border-color 0.3s;
  }}
  .question-card.answered-correct {{ border-left-color: var(--correct-border); }}
  .question-card.answered-wrong   {{ border-left-color: var(--wrong-border); }}
  .question-card.answered-partial {{ border-left-color: {color}; }}

  .q-header {{ display: flex; gap: 12px; align-items: baseline; margin-bottom: 14px; flex-wrap: wrap; }}
  .q-num {{
    font-size: 0.72rem; font-weight: 700; background: var(--navy);
    color: #fff; padding: 2px 8px; border-radius: 20px; white-space: nowrap; flex-shrink: 0;
  }}
  .q-source {{
    font-size: 0.68rem; color: #888; background: #eee;
    padding: 1px 7px; border-radius: 10px; white-space: nowrap; flex-shrink: 0;
  }}
  .q-text {{ font-size: 0.97rem; font-weight: 600; line-height: 1.5; }}
  .multi-badge {{
    font-size: 0.7rem; background: {color}; color: #fff;
    border-radius: 4px; padding: 1px 6px; margin-left: 6px;
    font-weight: 600; white-space: nowrap;
  }}

  .options {{ display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px; }}
  .option-label {{
    display: flex; align-items: flex-start; gap: 10px;
    padding: 10px 14px; border: 2px solid #e0e0e0; border-radius: 8px;
    cursor: pointer; transition: border-color 0.15s, background 0.15s; font-size: 0.92rem;
  }}
  .option-label:hover {{ border-color: {color}; background: #f5f5ff; }}
  .option-label input {{ flex-shrink: 0; margin-top: 3px; accent-color: {color}; }}
  .option-label .letter {{ font-weight: 700; color: var(--navy); flex-shrink: 0; min-width: 22px; }}
  .option-label.correct {{ border-color: var(--correct-border); background: var(--correct-bg); }}
  .option-label.wrong   {{ border-color: var(--wrong-border);   background: var(--wrong-bg); }}
  .option-label.disabled {{ cursor: default; pointer-events: none; }}
  .option-label.correct::after {{ content: " \u2713"; color: var(--correct-border); font-weight: 700; }}
  .option-label.wrong::after   {{ content: " \u2717"; color: var(--wrong-border);   font-weight: 700; }}

  .submit-btn {{
    display: inline-block; padding: 9px 22px; background: var(--navy);
    color: #fff; border: none; border-radius: 6px; font-size: 0.9rem;
    font-weight: 600; cursor: pointer; transition: background 0.2s;
  }}
  .submit-btn:hover {{ background: {color}; }}
  .submit-btn:disabled {{ background: #aaa; cursor: default; }}

  .result-badge {{
    display: inline-block; font-size: 0.8rem; font-weight: 700;
    padding: 2px 10px; border-radius: 12px; margin-bottom: 12px;
  }}
  .result-badge.correct {{ background: var(--correct-bg); color: var(--correct-border); border: 1px solid var(--correct-border); }}
  .result-badge.wrong   {{ background: var(--wrong-bg);   color: var(--wrong-border);   border: 1px solid var(--wrong-border); }}
  .result-badge.partial {{ background: #fff3cd; color: #856404; border: 1px solid #ffc107; }}

  .explanation {{ margin-top: 16px; border-radius: 8px; border: 1px solid #d0d0d0; overflow: hidden; }}
  .explanation summary {{
    list-style: none; padding: 10px 16px; background: #f0f0f0;
    cursor: pointer; font-size: 0.88rem; font-weight: 600;
    display: flex; align-items: center; gap: 8px; user-select: none;
  }}
  .explanation summary::-webkit-details-marker {{ display: none; }}
  .explanation summary::before {{ content: "\u25b6"; font-size: 0.7rem; transition: transform 0.2s; }}
  .explanation[open] summary::before {{ transform: rotate(90deg); }}
  .explanation-body {{
    padding: 14px 16px; font-size: 0.9rem; line-height: 1.65;
    background: #fafafa; border-top: 1px solid #d0d0d0;
  }}

  #score-panel {{
    display: none; background: var(--navy); color: #fff;
    border-radius: var(--radius); padding: 32px; text-align: center;
    margin-bottom: 40px; box-shadow: var(--shadow);
  }}
  #score-panel h2 {{ font-size: 1.4rem; margin-bottom: 8px; }}
  .score-num {{ font-size: 3rem; font-weight: 900; color: {color}; }}
  .score-pct {{ font-size: 1rem; color: #ccc; margin-bottom: 16px; }}
  .score-grade {{ font-size: 1rem; }}

  @media (max-width: 600px) {{
    header {{ padding: 12px 14px; }}
    .question-card {{ padding: 16px; }}
  }}
</style>
</head>
<body>
<header>
  <div>
    <h1><span>{short_title}</span></h1>
    <div class="header-meta">
      <div id="progress-bar-wrap"><div id="progress-bar"></div></div>
      <span id="progress-text">0 / {total} answered</span>
    </div>
  </div>
</header>
<main>
  <div id="score-panel">
    <h2>Domain Complete!</h2>
    <div class="score-num" id="score-correct">0</div>
    <div class="score-pct" id="score-pct">out of {total} questions</div>
    <div class="score-grade" id="score-grade"></div>
  </div>
  <div id="questions"></div>
</main>
<script>
const QUESTIONS = {questions_json};
const TOTAL = QUESTIONS.length;
let answeredCount = 0;
let correctCount  = 0;

function escHtml(s) {{
  return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}}

function buildQuiz() {{
  const container = document.getElementById("questions");
  QUESTIONS.forEach((q, idx) => {{
    const card = document.createElement("div");
    card.className = "question-card";
    card.id = "q" + idx;
    const multiBadge = q.multi ? "<span class=\\"multi-badge\\">Select 2</span>" : "";
    const srcBadge   = "<span class=\\"q-source\\">" + escHtml(q.source) + "</span>";
    card.innerHTML = `
      <div class="q-header">
        <span class="q-num">Q${{q.num}}</span>
        ${{srcBadge}}
        <span class="q-text">${{escHtml(q.text)}}${{multiBadge}}</span>
      </div>
      <div class="options" id="opts_${{idx}}">
        ${{q.options.map(o =>
          "<label class=\\"option-label\\" id=\\"lbl_" + idx + "_" + o.letter + "\\">" +
          "<input type=\\"" + (q.multi ? "checkbox" : "radio") + "\\" name=\\"q" + idx + "\\" value=\\"" + o.letter + "\\" />" +
          "<span class=\\"letter\\">" + o.letter + ")</span>" +
          "<span>" + escHtml(o.text) + "</span>" +
          "</label>"
        ).join("")}}
      </div>
      <button class="submit-btn" onclick="submitAnswer(${{idx}})">Check Answer</button>
      <div id="badge_${{idx}}" style="margin-top:12px;"></div>
      <details class="explanation" id="exp_${{idx}}">
        <summary>&#x1F4A1; Explanation</summary>
        <div class="explanation-body">${{q.explanation}}</div>
      </details>
    `;
    container.appendChild(card);
  }});
}}

function getSelected(idx) {{
  return Array.from(document.querySelectorAll("[name=\\"q" + idx + "\\"]:checked")).map(i => i.value);
}}

function submitAnswer(idx) {{
  const q = QUESTIONS[idx];
  const selected = getSelected(idx);
  if (!selected.length) return;

  document.querySelectorAll("[name=\\"q" + idx + "\\"]").forEach(i => i.disabled = true);
  document.querySelector("#q" + idx + " .submit-btn").disabled = true;

  q.options.forEach(o => {{
    const lbl = document.getElementById("lbl_" + idx + "_" + o.letter);
    lbl.classList.add("disabled");
    if (q.correct.includes(o.letter)) lbl.classList.add("correct");
    else if (selected.includes(o.letter)) lbl.classList.add("wrong");
  }});

  const correctSet  = new Set(q.correct);
  const selectedSet = new Set(selected);
  let result;
  if (q.multi) {{
    const allCorrect = q.correct.every(l => selectedSet.has(l)) && selected.every(l => correctSet.has(l));
    result = allCorrect ? "correct" : (q.correct.some(l => selectedSet.has(l)) ? "partial" : "wrong");
  }} else {{
    result = (selected.length === 1 && selected[0] === q.correct[0]) ? "correct" : "wrong";
  }}

  const badge = document.getElementById("badge_" + idx);
  const corrStr = q.correct.join(", ");
  if (result === "correct") {{
    badge.innerHTML = "<span class=\\"result-badge correct\\">&#x2713; Correct!</span>";
    document.getElementById("q" + idx).classList.add("answered-correct");
    correctCount++;
  }} else if (result === "partial") {{
    badge.innerHTML = "<span class=\\"result-badge partial\\">Partially Correct \u2014 full answer: " + corrStr + "</span>";
    document.getElementById("q" + idx).classList.add("answered-partial");
  }} else {{
    badge.innerHTML = "<span class=\\"result-badge wrong\\">&#x2717; Incorrect \u2014 correct: " + corrStr + "</span>";
    document.getElementById("q" + idx).classList.add("answered-wrong");
  }}

  document.getElementById("exp_" + idx).setAttribute("open", "");
  answeredCount++;
  updateProgress();
  if (answeredCount === TOTAL) showScore();
}}

function updateProgress() {{
  document.getElementById("progress-bar").style.width = (answeredCount / TOTAL * 100) + "%";
  document.getElementById("progress-text").textContent = answeredCount + " / " + TOTAL + " answered";
}}

function showScore() {{
  const panel = document.getElementById("score-panel");
  panel.style.display = "block";
  document.getElementById("score-correct").textContent = correctCount;
  const pct = Math.round(correctCount / TOTAL * 100);
  document.getElementById("score-pct").textContent = "out of " + TOTAL + " questions (" + pct + "%)";
  let grade;
  if (pct >= 90)      grade = "Excellent \u2014 strong domain mastery!";
  else if (pct >= 75) grade = "Good \u2014 review your misses and try again.";
  else if (pct >= 60) grade = "Needs work \u2014 spend more time on this domain.";
  else                grade = "Focus here \u2014 this domain needs significant study.";
  document.getElementById("score-grade").textContent = grade;
  panel.scrollIntoView({{ behavior: "smooth" }});
}}

buildQuiz();
updateProgress();
</script>
</body>
</html>
"""


def questions_to_json(questions: list) -> str:
    raw = json.dumps(questions, ensure_ascii=False)
    return raw.replace("</script>", "<\\/script>")


def generate_html(domain: dict, questions: list) -> str:
    return HTML_TEMPLATE.format(
        title=html.escape(domain["title"]),
        short_title=html.escape(domain["title"]),
        color=domain["color"],
        total=len(questions),
        questions_json=questions_to_json(questions),
    )


def main():
    # Parse all questions from both exams
    all_questions = []
    labels = ["Exam 1", "Exam 2"]
    for path, label in zip(MD_FILES, labels):
        print(f"Parsing {os.path.basename(path)} ...", end=" ", flush=True)
        qs = parse_md(path, label)
        print(f"{len(qs)} questions")
        all_questions.extend(qs)

    print(f"\nTotal questions: {len(all_questions)}")

    # Classify
    by_domain = {d["num"]: [] for d in DOMAINS}
    for q in all_questions:
        d = classify(q)
        q["domain"] = d
        by_domain[d].append(q)

    print("\nClassification results:")
    for domain in DOMAINS:
        n = len(by_domain[domain["num"]])
        print(f"  {domain['title']}: {n} questions")

    # Generate HTML files
    print()
    for domain in DOMAINS:
        questions = by_domain[domain["num"]]
        out_path  = os.path.join(SCRIPT_DIR, domain["filename"])
        html_content = generate_html(domain, questions)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  Written: {domain['filename']}  ({len(questions)} questions)")

    print("\nDone.")


if __name__ == "__main__":
    main()
