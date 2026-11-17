# Meeting Action Taker

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![CI](https://img.shields.io/github/actions/workflow/status/daily-project-factory/meeting-action-taker/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)

**Meeting Action Taker** is an intelligent utility designed to bridge the gap between spoken conversation and project execution. By leveraging LLM-driven extraction, it transforms raw meeting transcripts into structured, actionable data, ensuring that no task, decision, or owner assignment is ever lost in the noise of a long conference call.

---

## 🎯 Problem Statement & Target Audience
**The Problem:** Teams frequently lose track of follow-up items and accountability after long meetings. Manual note-taking is inconsistent, prone to human error, and often results in "action item drift," where tasks are forgotten or misassigned.

**Target Audience:** Engineering managers, project leads, and remote-first teams who rely on video conferencing and need a reliable, automated way to maintain project momentum without the overhead of manual documentation.

---

## 🚀 Key Features
*   **Transcript Ingestion:** Seamlessly process raw meeting transcripts via JSON or plain text file uploads.
*   **LLM-Powered Extraction:** Utilizes advanced prompting to identify discrete tasks, strict due dates, and specific assignees.
*   **Structured Integration:** Provides a FastAPI endpoint to push validated action items directly to external issue trackers.
*   **Validation Workflow:** Generates a summary validation report, allowing users to review and refine extracted data before final export.

---

## 🏗️ Architecture & System Design
The system follows a modular design pattern to ensure separation of concerns and maintainability:

*   `src/models.py`: Defines Pydantic domain schemas and request/response models for strict data validation.
*   `src/core.py`: Contains the core business logic, LangChain orchestration, and algorithmic processing engine.
*   `src/api.py`: FastAPI HTTP routes, middleware, and endpoint definitions.
*   `src/main.py`: The application entry point, providing both a CLI interface and the FastAPI server.

---

## 🛠️ Technology Stack
*   **Language:** Python 3.10+
*   **API Framework:** FastAPI
*   **AI/LLM Orchestration:** LangChain
*   **Data Validation:** Pydantic
*   **Vector Storage:** ChromaDB
*   **Testing:** pytest

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/daily-project-factory/meeting-action-taker.git
   cd meeting-action-taker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Variables
Copy the `.env.example` file to `.env` and configure the following:

```env
OPENAI_API_KEY=your_api_key_here
CHROMA_DB_PATH=./data/chroma
API_ENV=development
```

---

## ⚡ Usage

### CLI Interface
Process a transcript file directly from your terminal:
```bash
python src/main.py process --file path/to/transcript.txt
```

### API Endpoints
Start the server:
```bash
uvicorn src.main:app --reload
```
*   `POST /extract`: Upload a transcript for processing.
*   `GET /report/{id}`: Retrieve the validation report for a specific meeting.
*   `POST /export`: Push validated tasks to your project management tool.

---

## 🧪 Automated Testing
Run the full test suite using `pytest`:

```bash
# Run all tests
pytest tests/

# Run specific module tests
pytest tests/test_core.py
```

---

## 📂 Project Structure
```text
.
├── src/
│   ├── __init__.py
│   ├── api.py          # FastAPI routes
│   ├── core.py         # Business logic
│   ├── main.py         # Entry point
│   └── models.py       # Pydantic schemas
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_core.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Roadmap
- [ ] Add support for Zoom/Google Meet native API webhooks.
- [ ] Implement OAuth2 for direct Jira/Linear integration.
- [ ] Add support for multi-language transcript processing.
- [ ] Enhance the validation UI for manual overrides.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.