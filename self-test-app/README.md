# AWS AI Practitioner Practice Exam App

A professional, dark-themed practice exam application for the AWS AI Practitioner certification.

## Features
- **Question Pool:** 200 high-quality questions covering all 5 exam domains.
- **Exam Format:** 65 randomly selected questions per session.
- **Timer:** 90-minute countdown.
- **Question Types:** True/False, Multiple Choice, and Multi-select.
- **Scoring:** Automated scoring with an 80% passing threshold.
- **Review:** Detailed explanations for every answer.
- **Tech Stack:** React (TypeScript), Express (Node.js), Vanilla CSS.

## Getting Started

Follow these steps in order to set up and run the application locally.

### 1. Prerequisites
- Node.js (v18 or higher recommended)
- npm

### 2. Backend Setup
The backend handles question serving and session state.

```bash
cd self-test-app/backend
npm config set fund false
npm install
npm run build
npm start
```
The backend server will run on `http://localhost:3001`.

### 3. Frontend Setup
The frontend provides the interactive exam interface. **Note:** Ensure the backend is running first so the frontend proxy can connect.

```bash
cd self-test-app/frontend
npm config set fund false)
# Use --legacy-peer-deps to handle minor version conflicts in the scaffold
npm install --legacy-peer-deps
npm run dev
```
The frontend will typically run on `http://localhost:5173`. Open this URL in your browser to start the exam.

## Order of Operations
1. **Start the Backend:** Navigate to `backend/` and run `npm start`.
2. **Start the Frontend:** Navigate to `frontend/` and run `npm run dev`.
3. **Take the Exam:** Access the app via the Vite development URL.

## Notes
- The passing score is set to **80%**, which is intentionally higher than the real exam to ensure thorough preparation.
- Session data is stored temporarily in `backend/sessions/` as JSON files. No database is required.
