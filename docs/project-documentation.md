# Project Documentation for PastAI

## 1. Product Vision
PastAI is an AI-powered language-learning and memory-assist SaaS application for university students and individuals with memory challenges. Users record daily voice journals in Turkish or English. These are processed to enable AI-driven personalized, context-aware conversations and reminders.

## 2. Use Cases & Personas
### Persona 1: Ayşe (21, university student)
- **Goal:** Practice daily English speaking
- **Use Case:** Ayşe logs in, records her thoughts, and receives personalized responses.

### Persona 2: Mehmet (65, Alzheimer’s patient)
- **Goal:** Memory support through journaling
- **Use Case:** Mehmet speaks a journal entry, and the AI reminds him of names, events, and routines.

### General Use Case Flow:
1. Login
2. Record journal (voice)
3. Transcription & context storage
4. Memory injection
5. Chat or reminders using past context

## 3. System Architecture
- **Frontend:** Next.js (React)
- **Backend:** FastAPI or ASP.NET Core
- **LLM:** OpenAI GPT-4
- **STT:** Whisper or Deepgram
- **Context:** Redis/PostgreSQL
- **Hosting:** Render or Railway
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus + Grafana

## 4. Database Design
### Tables:
- **Users:** id, email, name, created_at
- **Journals:** id, user_id, text, date
- **Context:** id, user_id, data (JSON), updated_at
- **Reminders:** id, user_id, text, datetime

## 5. API Endpoints
- **POST /api/v1/journal** → Record a journal
- **GET /api/v1/context** → Retrieve user context
- **POST /api/v1/chat** → Send input + get response
- **GET /api/v1/reminders** → List reminders
- **POST /api/v1/reminders** → Create reminder

## 6. Prompting Strategy
- **System Prompt:** “You are a friendly AI assistant who remembers what the user has said before.”
- **Context:** “Yesterday, the user talked about a family visit...”
- **User Prompt:** “I want to continue talking about my family.”

## 7. Testing Plan
- **Unit Testing:** Prompt builder, context storage
- **Integration Testing:** End-to-end journaling
- **Load Testing:** Whisper & GPT API throughput
- **Manual QA:** UI, reminder accuracy
- **Tools:** Pytest, Selenium, Postman

## 8. CI/CD and Monitoring
- **CI/CD with GitHub Actions**
- **Dockerized deployment**
- **Prometheus + Grafana for health**
- **Logging via ELK stack**
- **Alerts for failed jobs**

## 9. Legal & Privacy
- **GDPR & KVKK compliant**
- **Encrypted storage of sensitive voice/text data**
- **Export/delete data options**
- **Explicit consent required for training model on user data**