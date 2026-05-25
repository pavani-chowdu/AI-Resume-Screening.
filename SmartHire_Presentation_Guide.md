# SmartHire AI Project Handbook

This document is your "cheat sheet" for explaining your project in interviews, presentations, or documentation. It contains the architecture, the problem it solves, and how it works under the hood.

## 1. The Core Problem It Solves

**The Problem (Real-world Context):** 
HR departments receive hundreds or thousands of resumes for a single job posting. Manually reading each resume is extremely slow, prone to human bias, and highly inefficient. Recruiters often miss top talent because they are overwhelmed by volume.

**The Solution (Your Application):**
You built an **AI-powered Resume Screening Platform** that automates the first round of hiring. It ingests thousands of resumes, uses Natural Language Processing (NLP) to "read" them like a human would, and instantly ranks candidates based on how well their skills match the specific job description.

## 2. Technical Stack (What to tell interviewers)

You built a modern, full-stack application using microservices-like architecture:
* **Frontend:** React.js paired with Vite. It provides a lightning-fast, reactive single-page application (SPA).
* **Backend:** Python using **FastAPI**. It's modern, asynchronous, and incredibly fast for API routing.
* **Database:** SQLite (managed via SQLAlchemy ORM). Used to safely store structured candidate and user data.
* **AI/Machine Learning:** 
  * `PyPDF2` (for parsing raw text from PDF resumes)
  * `Spacy` (Advanced Natural Language Processing for named-entity recognition, finding names, emails, etc.)
  * `Sentence-Transformers (BERT)` (Used for deeply understanding the semantic meaning of skills, not just keyword matching).

## 3. How the AI Actually Works (The "Secret Sauce")

When asked *how* it screens resumes, explain this three-step pipeline:

1. **Extraction Pipeline:** When a PDF is uploaded, the backend rips the raw text out of it. It uses NLP patterns to identify the person's contact info, education, and bullet points.
2. **Skill Extraction Engine:** Using your `skills.csv` dataset and Spacy NLP, the system cross-references the text to isolate exact technical skills mentioned in the resume.
3. **Semantic Matching (The AI part):** Instead of simple `CTRL+F` keyword matching (which is flawed if someone writes "Machine Learning" instead of "AI"), your system uses deep-learning Transformer models. It converts the candidate's skills and the Job Description into mathematical vectors, then calculates the **Cosine Similarity Score**. This ranks how closely the candidate matches the job contextually.

---

# Proposing "Real-Time" Advanced Features

To take this from a great academic project to a **highly competitive, enterprise-grade application**, here are three features we could add right now. 

### Feature Option 1: LLM-Generated Interview Questions (Most Impressive)
* **What it does:** Once a candidate gets a high matching score, we integrate an LLM API (like Grok or OpenAI). It looks at the job description, looks at the candidate's resume, and automatically generates **5 custom technical interview questions** specifically tailored to grill *that specific candidate*. 
* **Real-world value:** It prepares the HR manager instantly for the interview stage.

### Feature Option 2: Automated Email Dispatch (Very Practical)
* **What it does:** We add a Python background task system. When an HR manager drops 50 resumes into the system, the system ranks them. Automatically, all candidates who score above 75% receive an email inviting them to a technical interview. Candidates below 40% receive a polite, automated rejection email.
* **Real-world value:** Solves the massive "ghosting" problem in the hiring industry by automating candidate communication.

### Feature Option 3: Real-Time Notifications via WebSocket
* **What it does:** Scanning heavy PDFs can take time. We can implement a WebSocket pipeline so the user sees a real-time progress bar (e.g., "Extracting text... 20%", "Running AI model... 80%") instead of just a spinning loader.
* **Real-world value:** Massively improves User Experience (UX) and system reliability perception. 
