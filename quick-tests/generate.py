#!/usr/bin/env python3
"""
Generate self-contained HTML quiz pages from AWS AI Practitioner practice exam Markdown files.
Usage: python generate.py
Outputs: practice-exam.html, practice-exam-2.html in the same directory.
"""

import re
import json
import html
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXAM_DIR = os.path.dirname(SCRIPT_DIR)

EXAMS = [
    {
        "md": os.path.join(EXAM_DIR, "practice-exam.md"),
        "html": os.path.join(SCRIPT_DIR, "practice-exam.html"),
        "title": "AWS AI Practitioner — Practice Test 1",
    },
    {
        "md": os.path.join(EXAM_DIR, "practice-exam-2.md"),
        "html": os.path.join(SCRIPT_DIR, "practice-exam-2.html"),
        "title": "AWS AI Practitioner — Practice Test 2",
    },
]


def parse_correct_answers(answer_line: str) -> list[str]:
    """Extract the letter(s) from a 'Correct Answer(s): ...' line."""
    # Remove prefix
    line = re.sub(r"^Correct Answers?:\s*", "", answer_line, flags=re.IGNORECASE).strip()
    # Find all capital letter option markers like "A)", "B)", "D)"
    letters = re.findall(r"\b([A-E])\)", line)
    return list(dict.fromkeys(letters))  # deduplicate while preserving order


def parse_md(path: str) -> list[dict]:
    """Parse a practice exam markdown file into a list of question dicts."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split on horizontal rules.  We need to be careful: the separator is "---"
    # on its own line.  Use a positive-lookahead to keep blocks together.
    raw_blocks = re.split(r"\n---\n", content)

    questions = []

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        # Must contain a question marker
        q_match = re.match(r"\*\*Question\s+(\d+)\*\*\s*\n+(.*?)(?=\n[A-E]\)|\n<details)", block, re.DOTALL)
        if not q_match:
            continue

        q_num = int(q_match.group(1))
        q_text = q_match.group(2).strip()

        # Extract options  (lines starting with A) B) C) D) E))
        options_raw = re.findall(r"^([A-E])\)\s+(.+)$", block, re.MULTILINE)
        options = [{"letter": l, "text": t.strip()} for l, t in options_raw]

        # Extract the <details> block
        details_match = re.search(r"<details>(.*?)</details>", block, re.DOTALL)
        if not details_match:
            continue
        details_content = details_match.group(1).strip()

        # Remove <summary>…</summary>
        details_content = re.sub(r"<summary>.*?</summary>", "", details_content, flags=re.DOTALL).strip()

        # First non-empty line should be the correct answer line
        lines = [l for l in details_content.split("\n") if l.strip()]
        answer_line = ""
        explanation_lines = []
        for i, line in enumerate(lines):
            if re.match(r"Correct Answers?:", line, re.IGNORECASE):
                answer_line = line
                explanation_lines = lines[i + 1:]
                break

        if not answer_line:
            # Fallback: treat first line as answer line
            answer_line = lines[0] if lines else ""
            explanation_lines = lines[1:] if len(lines) > 1 else []

        correct_letters = parse_correct_answers(answer_line)

        # Clean up explanation: strip markdown bold markers, leading/trailing blank lines
        explanation = "\n".join(explanation_lines).strip()
        # Convert **text** to <strong>text</strong>
        explanation = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", explanation)

        # Detect multi-select
        multi_select = bool(
            re.search(r"Select TWO|Choose two|select two|choose two", q_text, re.IGNORECASE)
        )

        # If multi-select but only one answer was found, try to recover the second
        # answer from the explanation by matching key words from option text.
        if multi_select and len(correct_letters) < 2 and explanation:
            for opt in options:
                if opt["letter"] not in correct_letters:
                    # Use the core service name (up to first '(' or end) for matching
                    core = re.split(r'\(', opt["text"])[0].strip()
                    # Try matching core name in explanation (at least 8 chars to avoid false positives)
                    if len(core) >= 8 and re.search(re.escape(core), explanation, re.IGNORECASE):
                        correct_letters.append(opt["letter"])
                    elif re.search(r'\b' + re.escape(opt["letter"]) + r'\)', explanation):
                        correct_letters.append(opt["letter"])
                if len(correct_letters) >= 2:
                    break

        questions.append(
            {
                "num": q_num,
                "text": q_text,
                "options": options,
                "correct": correct_letters,
                "explanation": explanation,
                "multi": multi_select,
            }
        )

    # Sort by question number
    questions.sort(key=lambda q: q["num"])
    return questions


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<style>
  :root {{
    --aws-orange: #FF9900;
    --aws-navy:   #232F3E;
    --aws-blue:   #1A73E8;
    --correct-bg: #d4edda;
    --correct-border: #28a745;
    --wrong-bg:   #f8d7da;
    --wrong-border: #dc3545;
    --neutral-bg: #f4f6f8;
    --card-bg:    #ffffff;
    --radius:     10px;
    --shadow:     0 2px 8px rgba(0,0,0,0.08);
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: var(--neutral-bg);
    color: #222;
    line-height: 1.6;
  }}
  header {{
    background: var(--aws-navy);
    color: #fff;
    padding: 20px 24px;
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
  }}
  header h1 {{
    font-size: 1.1rem;
    font-weight: 700;
    flex: 1;
  }}
  header h1 span {{
    color: var(--aws-orange);
  }}
  #progress-bar-wrap {{
    width: 100%;
    background: rgba(255,255,255,0.2);
    border-radius: 4px;
    height: 6px;
    margin-top: 8px;
  }}
  #progress-bar {{
    height: 6px;
    border-radius: 4px;
    background: var(--aws-orange);
    transition: width 0.3s;
    width: 0%;
  }}
  #progress-text {{
    font-size: 0.82rem;
    color: #ccc;
    white-space: nowrap;
  }}
  main {{
    max-width: 860px;
    margin: 28px auto;
    padding: 0 16px 60px;
  }}
  .question-card {{
    background: var(--card-bg);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 24px;
    margin-bottom: 28px;
    border-left: 5px solid #ddd;
    transition: border-color 0.3s;
  }}
  .question-card.answered-correct  {{ border-left-color: var(--correct-border); }}
  .question-card.answered-wrong    {{ border-left-color: var(--wrong-border); }}
  .question-card.answered-partial  {{ border-left-color: var(--aws-orange); }}
  .q-header {{
    display: flex;
    gap: 12px;
    align-items: baseline;
    margin-bottom: 14px;
  }}
  .q-num {{
    font-size: 0.75rem;
    font-weight: 700;
    background: var(--aws-navy);
    color: #fff;
    padding: 2px 8px;
    border-radius: 20px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .q-text {{
    font-size: 0.97rem;
    font-weight: 600;
    line-height: 1.5;
  }}
  .multi-badge {{
    font-size: 0.72rem;
    background: var(--aws-orange);
    color: #fff;
    border-radius: 4px;
    padding: 1px 6px;
    margin-left: 8px;
    font-weight: 600;
    vertical-align: middle;
    white-space: nowrap;
  }}
  .options {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 16px;
  }}
  .option-label {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 14px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: border-color 0.15s, background 0.15s;
    font-size: 0.92rem;
  }}
  .option-label:hover {{ border-color: var(--aws-orange); background: #fff8ec; }}
  .option-label input {{ flex-shrink: 0; margin-top: 3px; accent-color: var(--aws-orange); }}
  .option-label .letter {{
    font-weight: 700;
    color: var(--aws-navy);
    flex-shrink: 0;
    min-width: 22px;
  }}
  /* Feedback states applied after submit */
  .option-label.correct {{
    border-color: var(--correct-border);
    background: var(--correct-bg);
  }}
  .option-label.wrong {{
    border-color: var(--wrong-border);
    background: var(--wrong-bg);
  }}
  .option-label.disabled {{ cursor: default; pointer-events: none; }}
  .option-label.correct::after {{ content: " ✓"; color: var(--correct-border); font-weight: 700; }}
  .option-label.wrong::after   {{ content: " ✗"; color: var(--wrong-border); font-weight: 700; }}
  .submit-btn {{
    display: inline-block;
    padding: 9px 22px;
    background: var(--aws-navy);
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }}
  .submit-btn:hover {{ background: var(--aws-orange); }}
  .submit-btn:disabled {{ background: #aaa; cursor: default; }}
  /* Explanation details */
  .explanation {{
    margin-top: 16px;
    border-radius: 8px;
    border: 1px solid #d0d0d0;
    overflow: hidden;
  }}
  .explanation summary {{
    list-style: none;
    padding: 10px 16px;
    background: #f0f0f0;
    cursor: pointer;
    font-size: 0.88rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    user-select: none;
  }}
  .explanation summary::-webkit-details-marker {{ display: none; }}
  .explanation summary::before {{
    content: "▶";
    font-size: 0.7rem;
    transition: transform 0.2s;
  }}
  .explanation[open] summary::before {{ transform: rotate(90deg); }}
  .explanation-body {{
    padding: 14px 16px;
    font-size: 0.9rem;
    line-height: 1.65;
    background: #fafafa;
    border-top: 1px solid #d0d0d0;
  }}
  .result-badge {{
    display: inline-block;
    font-size: 0.8rem;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 12px;
    margin-bottom: 12px;
  }}
  .result-badge.correct {{ background: var(--correct-bg); color: var(--correct-border); border: 1px solid var(--correct-border); }}
  .result-badge.wrong   {{ background: var(--wrong-bg); color: var(--wrong-border); border: 1px solid var(--wrong-border); }}
  .result-badge.partial {{ background: #fff3cd; color: #856404; border: 1px solid #ffc107; }}
  /* Score panel */
  #score-panel {{
    display: none;
    background: var(--aws-navy);
    color: #fff;
    border-radius: var(--radius);
    padding: 32px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: var(--shadow);
  }}
  #score-panel h2 {{ font-size: 1.5rem; margin-bottom: 8px; }}
  #score-panel .score-num {{ font-size: 3rem; font-weight: 900; color: var(--aws-orange); }}
  #score-panel .score-pct {{ font-size: 1.1rem; color: #ccc; margin-bottom: 16px; }}
  #score-panel .score-grade {{ font-size: 1rem; }}
  @media (max-width: 600px) {{
    header {{ padding: 14px 16px; }}
    .question-card {{ padding: 16px; }}
  }}
</style>
</head>
<body>
<header>
  <div style="flex:1">
    <h1>☁️ <span>{title_short}</span></h1>
    <div id="progress-bar-wrap"><div id="progress-bar"></div></div>
  </div>
  <div id="progress-text">0 / {total} answered</div>
</header>
<main>
  <div id="score-panel">
    <h2>Quiz Complete!</h2>
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
let correctCount = 0;

function escHtml(s) {{
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}

function buildQuiz() {{
  const container = document.getElementById('questions');
  QUESTIONS.forEach((q, idx) => {{
    const card = document.createElement('div');
    card.className = 'question-card';
    card.id = `q${{idx}}`;

    const multiBadge = q.multi ? `<span class="multi-badge">Select 2</span>` : '';
    card.innerHTML = `
      <div class="q-header">
        <span class="q-num">Q${{q.num}}</span>
        <span class="q-text">${{escHtml(q.text)}}${{multiBadge}}</span>
      </div>
      <div class="options" id="opts_${{idx}}">
        ${{q.options.map(o => `
          <label class="option-label" id="lbl_${{idx}}_${{o.letter}}">
            <input type="${{q.multi ? 'checkbox' : 'radio'}}" name="q${{idx}}" value="${{o.letter}}" />
            <span class="letter">${{o.letter}})</span>
            <span>${{escHtml(o.text)}}</span>
          </label>`).join('')}}
      </div>
      <button class="submit-btn" onclick="submitAnswer(${{idx}})">Check Answer</button>
      <div id="badge_${{idx}}" style="margin-top:12px;"></div>
      <details class="explanation" id="exp_${{idx}}">
        <summary>💡 Explanation</summary>
        <div class="explanation-body">${{q.explanation}}</div>
      </details>
    `;
    container.appendChild(card);
  }});
}}

function getSelected(idx) {{
  const inputs = document.querySelectorAll(`[name="q${{idx}}"]:checked`);
  return Array.from(inputs).map(i => i.value);
}}

function submitAnswer(idx) {{
  const q = QUESTIONS[idx];
  const selected = getSelected(idx);
  if (selected.length === 0) return;

  // Disable all inputs
  document.querySelectorAll(`[name="q${{idx}}"]`).forEach(inp => inp.disabled = true);
  document.querySelector(`#q${{idx}} .submit-btn`).disabled = true;

  // Apply visual feedback
  q.options.forEach(o => {{
    const lbl = document.getElementById(`lbl_${{idx}}_${{o.letter}}`);
    lbl.classList.add('disabled');
    const isCorrect = q.correct.includes(o.letter);
    const isSelected = selected.includes(o.letter);
    if (isCorrect) lbl.classList.add('correct');
    else if (isSelected && !isCorrect) lbl.classList.add('wrong');
  }});

  // Determine result
  const correctSet = new Set(q.correct);
  const selectedSet = new Set(selected);
  let result;
  if (q.multi) {{
    const allCorrect = q.correct.every(l => selectedSet.has(l)) && selected.every(l => correctSet.has(l));
    const partialCorrect = q.correct.some(l => selectedSet.has(l));
    result = allCorrect ? 'correct' : (partialCorrect ? 'partial' : 'wrong');
  }} else {{
    result = (selected.length === 1 && selected[0] === q.correct[0]) ? 'correct' : 'wrong';
  }}

  const badge = document.getElementById(`badge_${{idx}}`);
  if (result === 'correct') {{
    badge.innerHTML = `<span class="result-badge correct">✓ Correct!</span>`;
    document.getElementById(`q${{idx}}`).classList.add('answered-correct');
    correctCount++;
  }} else if (result === 'partial') {{
    const corrStr = q.correct.join(', ');
    badge.innerHTML = `<span class="result-badge partial">Partially Correct — full answer: ${{corrStr}}</span>`;
    document.getElementById(`q${{idx}}`).classList.add('answered-partial');
  }} else {{
    const corrStr = q.correct.join(', ');
    badge.innerHTML = `<span class="result-badge wrong">✗ Incorrect — correct answer: ${{corrStr}}</span>`;
    document.getElementById(`q${{idx}}`).classList.add('answered-wrong');
  }}

  // Auto-open explanation
  document.getElementById(`exp_${{idx}}`).setAttribute('open', '');

  answeredCount++;
  updateProgress();

  if (answeredCount === TOTAL) showScore();
}}

function updateProgress() {{
  const pct = (answeredCount / TOTAL) * 100;
  document.getElementById('progress-bar').style.width = pct + '%';
  document.getElementById('progress-text').textContent = `${{answeredCount}} / ${{TOTAL}} answered`;
}}

function showScore() {{
  const panel = document.getElementById('score-panel');
  panel.style.display = 'block';
  document.getElementById('score-correct').textContent = correctCount;
  document.getElementById('score-pct').textContent = `out of ${{TOTAL}} questions (${{Math.round(correctCount/TOTAL*100)}}%)`;
  const pct = correctCount / TOTAL * 100;
  let grade;
  if (pct >= 90) grade = "Excellent \u2014 you\'re exam-ready!";
  else if (pct >= 75) grade = "Good \u2014 review your misses and try again.";
  else if (pct >= 60) grade = "Needs more study \u2014 keep going!";
  else grade = "Keep practicing \u2014 you\'ll get there!";
  document.getElementById('score-grade').textContent = grade;
  panel.scrollIntoView({{ behavior: 'smooth' }});
}}

buildQuiz();
updateProgress();
</script>
</body>
</html>
"""


def questions_to_json(questions: list[dict]) -> str:
    """Serialize questions to a JSON string safe for embedding in a <script> tag."""
    # We need to escape </script> to avoid breaking the tag
    raw = json.dumps(questions, ensure_ascii=False, indent=None)
    return raw.replace("</script>", "<\\/script>")


def generate_html(title: str, questions: list[dict]) -> str:
    title_short = title.split("—")[-1].strip() if "—" in title else title
    questions_json = questions_to_json(questions)
    return HTML_TEMPLATE.format(
        title=html.escape(title),
        title_short=html.escape(title_short),
        total=len(questions),
        questions_json=questions_json,
    )


def main():
    for exam in EXAMS:
        print(f"Parsing {exam['md']} ...", end=" ", flush=True)
        questions = parse_md(exam["md"])
        print(f"{len(questions)} questions found.")

        html_content = generate_html(exam["title"], questions)

        with open(exam["html"], "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  → Written to {exam['html']}")


if __name__ == "__main__":
    main()
