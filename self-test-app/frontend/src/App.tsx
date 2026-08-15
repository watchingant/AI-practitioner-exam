import { useState, useEffect, useCallback } from 'react'
import { Timer, CheckCircle2, XCircle, ArrowRight, ArrowLeft, RefreshCw, AlertCircle } from 'lucide-react'

interface Question {
  id: number;
  domain: string;
  type: 'mcq' | 'true-false' | 'multi-select';
  text: string;
  options: string[];
}

interface ResultQuestion extends Question {
  answer: string | string[];
  explanation: string;
  userAnswer: string | string[];
  isCorrect: boolean;
}

interface ExamResults {
  score: number;
  passed: boolean;
  correctCount: number;
  totalCount: number;
  results: ResultQuestion[];
}

function App() {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, any>>({});
  const [timeLeft, setTimeLeft] = useState(90 * 60); // 90 minutes
  const [examStarted, setExamStarted] = useState(false);
  const [examFinished, setExamFinished] = useState(false);
  const [results, setResults] = useState<ExamResults | null>(null);
  const [loading, setLoading] = useState(false);

  const startExam = async () => {
    setLoading(true);
    try {
      const startRes = await fetch('/api/start', { method: 'POST' });
      const { sessionId } = await startRes.json();
      setSessionId(sessionId);
      
      const questRes = await fetch(`/api/questions/${sessionId}`);
      const questData = await questRes.json();
      setQuestions(questData);
      setExamStarted(true);
      setTimeLeft(90 * 60);
    } catch (error) {
      console.error('Failed to start exam:', error);
    }
    setLoading(false);
  };

  const finishExam = useCallback(async () => {
    if (!sessionId) return;
    setLoading(true);
    try {
      const res = await fetch(`/api/results/${sessionId}`);
      const resultData = await res.json();
      setResults(resultData);
      setExamFinished(true);
      setExamStarted(false);
    } catch (error) {
      console.error('Failed to finish exam:', error);
    }
    setLoading(false);
  }, [sessionId]);

  useEffect(() => {
    let timer: any;
    if (examStarted && timeLeft > 0) {
      timer = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            finishExam();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [examStarted, timeLeft, finishExam]);

  const handleAnswerChange = async (questionId: number, answer: any) => {
    setAnswers(prev => ({ ...prev, [questionId]: answer }));
    if (sessionId) {
      await fetch(`/api/submit/${sessionId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ questionId, answer })
      });
    }
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  if (!examStarted && !examFinished) {
    return (
      <div className="card" style={{ maxWidth: '600px', margin: '0 auto' }}>
        <h2>AWS AI Practitioner Practice Exam</h2>
        <p style={{ color: 'var(--text-secondary)' }}>
          This practice exam consists of 65 questions randomly selected from a pool of 200.
          You have 90 minutes to complete the exam.
        </p>
        <div style={{ padding: '1rem', borderLeft: '4px solid var(--primary-color)', backgroundColor: '#1e293b', marginBottom: '1.5rem' }}>
          <p style={{ margin: 0, fontSize: '0.9rem' }}>
            <AlertCircle size={16} style={{ verticalAlign: 'middle', marginRight: '8px' }} />
            Note: The passing score for this practice exam is <strong>80%</strong>, which is purposely higher than the real test to ensure you are fully prepared.
          </p>
        </div>
        <button onClick={startExam} disabled={loading} style={{ width: '100%' }}>
          {loading ? 'Generating Exam...' : 'Start Practice Exam'}
        </button>
      </div>
    );
  }

  if (examStarted && questions.length > 0) {
    const q = questions[currentIndex];
    const userAnswer = answers[q.id];

    return (
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <span style={{ color: 'var(--text-secondary)' }}>Question {currentIndex + 1} of 65</span>
          <div style={{ display: 'flex', alignItems: 'center', color: timeLeft < 300 ? 'var(--error-color)' : 'var(--text-primary)' }}>
            <Timer size={20} style={{ marginRight: '8px' }} />
            <span style={{ fontWeight: 'bold', fontSize: '1.2rem' }}>{formatTime(timeLeft)}</span>
          </div>
        </div>

        <div className="card">
          <p style={{ fontSize: '0.9rem', color: 'var(--primary-color)', marginBottom: '0.5rem', fontWeight: 'bold', textTransform: 'uppercase' }}>{q.domain}</p>
          <h3 style={{ marginTop: 0, lineHeight: 1.4 }}>{q.text}</h3>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginTop: '1.5rem' }}>
            {q.options.map((opt, i) => (
              <label 
                key={i} 
                style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  padding: '1rem', 
                  backgroundColor: '#262626', 
                  borderRadius: '8px', 
                  cursor: 'pointer',
                  border: '1px solid var(--border-color)',
                  transition: 'background-color 0.2s'
                }}
              >
                <input 
                  type={q.type === 'multi-select' ? 'checkbox' : 'radio'}
                  name={`question-${q.id}`}
                  checked={q.type === 'multi-select' ? (userAnswer || []).includes(opt) : userAnswer === opt}
                  onChange={(e) => {
                    if (q.type === 'multi-select') {
                      const current = userAnswer || [];
                      const next = e.target.checked 
                        ? [...current, opt]
                        : current.filter((a: string) => a !== opt);
                      handleAnswerChange(q.id, next);
                    } else {
                      handleAnswerChange(q.id, opt);
                    }
                  }}
                  style={{ marginRight: '12px' }}
                />
                {opt}
              </label>
            ))}
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '2rem' }}>
          <button 
            onClick={() => setCurrentIndex(prev => prev - 1)} 
            disabled={currentIndex === 0}
            style={{ backgroundColor: 'var(--secondary-color)', display: 'flex', alignItems: 'center' }}
          >
            <ArrowLeft size={18} style={{ marginRight: '8px' }} /> Previous
          </button>
          
          {currentIndex === 64 ? (
            <button onClick={finishExam} style={{ backgroundColor: 'var(--success-color)' }}>
              Submit Exam
            </button>
          ) : (
            <button 
              onClick={() => setCurrentIndex(prev => prev + 1)}
              style={{ display: 'flex', alignItems: 'center' }}
            >
              Next <ArrowRight size={18} style={{ marginLeft: '8px' }} />
            </button>
          )}
        </div>
      </div>
    );
  }

  if (examFinished && results) {
    return (
      <div style={{ maxWidth: '900px', margin: '0 auto', textAlign: 'left' }}>
        <div className="card" style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h2 style={{ color: results.passed ? 'var(--success-color)' : 'var(--error-color)', fontSize: '2.5rem', marginBottom: '0.5rem' }}>
            {results.passed ? 'PASSED' : 'FAILED'}
          </h2>
          <p style={{ fontSize: '1.2rem', marginBottom: '1.5rem' }}>
            Your Score: <strong>{results.score.toFixed(1)}%</strong>
          </p>
          <p style={{ color: 'var(--text-secondary)' }}>
            Correct: {results.correctCount} | Total: {results.totalCount} | Required: 80%
          </p>
          <button onClick={() => window.location.reload()} style={{ display: 'inline-flex', alignItems: 'center', marginTop: '1rem' }}>
            <RefreshCw size={18} style={{ marginRight: '8px' }} /> Retake Exam
          </button>
        </div>

        <h3 style={{ marginBottom: '1.5rem' }}>Detailed Review</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {results.results.map((r, i) => (
            <div key={i} className="card" style={{ borderLeft: `6px solid ${r.isCorrect ? 'var(--success-color)' : 'var(--error-color)'}` }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>{r.domain}</span>
                {r.isCorrect ? <CheckCircle2 color="var(--success-color)" /> : <XCircle color="var(--error-color)" />}
              </div>
              <h4 style={{ margin: '0.5rem 0 1rem 0' }}>{i + 1}. {r.text}</h4>
              
              <div style={{ fontSize: '0.95rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                <p><strong>Your Answer:</strong> <span style={{ color: r.isCorrect ? 'var(--success-color)' : 'var(--error-color)' }}>
                  {Array.isArray(r.userAnswer) ? r.userAnswer.join(', ') : (r.userAnswer || 'No answer')}
                </span></p>
                {!r.isCorrect && (
                  <p><strong>Correct Answer:</strong> <span style={{ color: 'var(--success-color)' }}>
                    {Array.isArray(r.answer) ? r.answer.join(', ') : r.answer}
                  </span></p>
                )}
                <div style={{ marginTop: '1rem', padding: '1rem', backgroundColor: '#262626', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
                  <strong>Explanation:</strong>
                  <p style={{ margin: '0.5rem 0 0 0', color: 'var(--text-secondary)' }}>{r.explanation}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return <div>Loading...</div>;
}

export default App
