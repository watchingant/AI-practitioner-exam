import express from 'express';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import { v4 as uuidv4 } from 'uuid';

const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

const DATA_DIR = path.join(__dirname, '../data');
const SESSIONS_DIR = path.join(__dirname, '../sessions');
const QUESTIONS_PATH = path.join(DATA_DIR, 'questions.json');

if (!fs.existsSync(SESSIONS_DIR)) {
  fs.mkdirSync(SESSIONS_DIR, { recursive: true });
}

interface Question {
  id: number;
  domain: string;
  type: 'mcq' | 'multi-select';
  text: string;
  options: string[];
  answer: string | string[];
  explanation: string;
}

interface Session {
  id: string;
  startTime: number;
  questionIds: number[];
  answers: Record<number, string | string[]>;
}

const loadQuestions = (): Question[] => {
  const data = fs.readFileSync(QUESTIONS_PATH, 'utf-8');
  return JSON.parse(data);
};

const saveSession = (session: Session) => {
  fs.writeFileSync(path.join(SESSIONS_DIR, `${session.id}.json`), JSON.stringify(session));
};

const getSession = (id: string): Session | null => {
  const sessionPath = path.join(SESSIONS_DIR, `${id}.json`);
  if (!fs.existsSync(sessionPath)) return null;
  return JSON.parse(fs.readFileSync(sessionPath, 'utf-8'));
};

app.post('/api/start', (req, res) => {
  const allQuestions = loadQuestions();
  const shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
  const selected = shuffled.slice(0, 65);
  
  const sessionId = uuidv4();
  const session: Session = {
    id: sessionId,
    startTime: Date.now(),
    questionIds: selected.map(q => q.id),
    answers: {}
  };
  
  saveSession(session);
  res.json({ sessionId, startTime: session.startTime, questionIds: session.questionIds });
});

app.get('/api/questions/:sessionId', (req, res) => {
  const session = getSession(req.params.sessionId);
  if (!session) return res.status(404).send('Session not found');
  
  const allQuestions = loadQuestions();
  const sessionQuestions = session.questionIds.map(id => {
    const q = allQuestions.find(q => q.id === id);
    if (!q) return null;
    const { answer, explanation, ...rest } = q;
    return rest;
  }).filter(Boolean);
  
  res.json(sessionQuestions);
});

app.post('/api/submit/:sessionId', (req, res) => {
  const session = getSession(req.params.sessionId);
  if (!session) return res.status(404).send('Session not found');
  
  const { questionId, answer } = req.body;
  session.answers[questionId] = answer;
  saveSession(session);
  res.json({ success: true });
});

app.get('/api/results/:sessionId', (req, res) => {
  const session = getSession(req.params.sessionId);
  if (!session) return res.status(404).send('Session not found');
  
  const allQuestions = loadQuestions();
  let correctCount = 0;
  
  const results = session.questionIds.map(id => {
    const question = allQuestions.find(q => q.id === id)!;
    const userAnswer = session.answers[id];
    
    let isCorrect = false;
    if (question.type === 'multi-select') {
      const qAnswer = question.answer as string[];
      const uAnswer = (userAnswer as string[]) || [];
      isCorrect = qAnswer.length === uAnswer.length && qAnswer.every(a => uAnswer.includes(a));
    } else {
      isCorrect = question.answer === userAnswer;
    }
    
    if (isCorrect) correctCount++;
    
    return {
      ...question,
      userAnswer,
      isCorrect
    };
  });
  
  const score = (correctCount / session.questionIds.length) * 100;
  const passed = score >= 80;
  
  res.json({
    score,
    passed,
    correctCount,
    totalCount: session.questionIds.length,
    results
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
