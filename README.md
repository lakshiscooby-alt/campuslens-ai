# CampusLens AI

> A multimodal AI assistant that uses Gemma 4 to understand college notices and documents, extract important information, and answer student questions.

---

## 👥 Team — Synap Tech

| Member | Contribution |
|---|---|
| **Lakshithaa V** | AI/backend development, Gemma 4 integration, multimodal document processing, information extraction, Q&A, Git/GitHub |
| **Pavitraa Surendran** | Streamlit UI, frontend development, upload/results/Q&A interface, frontend testing |
| **Shivamihit G** | Documentation and presentation |
| **Rithvik Kumar** | Prompt engineering, AI testing, edge cases |

---

# 🎯 The Problem

College students regularly receive important information through:

- College notices
- Posters
- Circulars
- Assignment sheets
- Event announcements
- Other visual documents

These documents often contain important details such as:

- Dates
- Times
- Venues
- Deadlines
- Requirements
- Event information

Finding this information manually can be time-consuming, especially when students need a quick answer.

## Why We Chose This Problem

Students deal with college information every day, but this information is often presented in visually dense documents.

We wanted to build a simple AI assistant that can turn these documents into information students can actually use.

---

# 💡 Our Solution

**CampusLens AI** is a multimodal AI assistant designed for understanding college documents.

A student can upload a notice or document, and **Gemma 4** analyzes the visual content to understand the information.

CampusLens then:

1. Extracts important information.
2. Presents the information in a structured format.
3. Allows students to ask questions about the uploaded document.

### Core Workflow

**Upload Document → Gemma 4 → Understand → Extract Information → Ask Questions**

---

# ✨ Key Features

## 📄 Multimodal Document Understanding

CampusLens uses Gemma 4 to understand visual college notices and documents.

## 🔎 Structured Information Extraction

The application extracts:

- Event
- Date
- Time
- Venue
- Deadline
- Requirements
- Summary
- Important Details

## 💬 Ask Questions

Students can ask natural-language questions about the uploaded document.

Examples:

> "What do I need to bring?"

> "When is the event?"

> "Where is it happening?"

> "What time does the event start?"

## 🛡️ No Guessing

Our prompt instructs Gemma 4 not to invent information.

If a detail is not present in the document, CampusLens reports:

> "Not mentioned"

This helps reduce misleading answers.

## 🎓 Student-Focused Interface

The application is designed around a simple workflow:

**Upload → Analyze → Understand → Ask**

---

# 🤖 Why Gemma 4?

Gemma 4 is the core intelligence behind CampusLens AI.

We use the multimodal capabilities of Gemma 4 to understand visual content from college notices instead of relying only on traditional text extraction.

This allows CampusLens to reason about information contained inside an image and answer questions about the document.

### Model Used

`gemma-4-26b-a4b-it`

We selected this Gemma 4 model because it provided reliable performance in our hackathon development environment.

---

# 💡 Innovation and Differentiation

CampusLens is designed specifically around a common student problem: **understanding information hidden inside college documents quickly.**

Instead of simply extracting text from an image, CampusLens combines:

- Multimodal document understanding
- Structured information extraction
- Natural-language question answering
- A student-focused interface

This creates a simple workflow where students can go from a visual notice to actionable information without manually reading through the entire document.

---

# 🏗️ Technical Implementation

## Architecture

```text
                College Notice / Document
                         │
                         ▼
                  Streamlit Upload
                         │
                         ▼
                    Gemma 4
                Multimodal Analysis
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
     Structured Extraction       Q&A Context
             │                       │
             ▼                       ▼
       Student-Friendly        Student Questions
           Results                    │
                                     ▼
                              Gemma 4 Answer
```

## Technology Stack

- **Python**
- **Streamlit**
- **Google GenAI SDK**
- **Gemma 4**
- **Git**
- **GitHub**

---

# ⚙️ How It Works

### 1. Upload

The student uploads a college notice or document.

### 2. Multimodal Understanding

The uploaded image is sent to Gemma 4 for visual understanding.

### 3. Information Extraction

Gemma 4 identifies important information such as:

- Event
- Date
- Time
- Venue
- Deadline
- Requirements

### 4. Results

CampusLens presents the extracted information in a structured, easy-to-read format.

### 5. Ask Questions

The student can ask additional questions about the uploaded document.

Gemma 4 generates an answer based on the document.

---

# 🧪 Example

For a college event notice, CampusLens can produce:

```text
EVENT:
Ugadi 25 Celebration

DATE:
March 29 & 30, 2025

TIME:
March 29: 4:30 PM – 7:30 PM
March 30: 12:15 PM – 5:30 PM

VENUE:
New Auditorium
Amriteswari Hall

DEADLINE:
Not mentioned
```

Example question:

> "Where is the movie screening?"

CampusLens can answer based on the information contained in the uploaded notice.

---

# 🚀 Implementation During the Hackathon

During the hackathon, our team focused on building a working end-to-end MVP rather than adding unnecessary features.

The main implementation stages were:

1. Set up the Gemma 4 development environment.
2. Integrated the Google GenAI SDK.
3. Tested Gemma 4 text generation.
4. Tested multimodal document understanding.
5. Designed prompts for structured information extraction.
6. Built the Streamlit frontend.
7. Added document upload and image preview.
8. Added structured analysis results.
9. Added document-based Q&A.
10. Tested the application using a real college notice.
11. Collaborated through GitHub.
12. Recorded a working demonstration.

Our final MVP focuses on the core workflow:

**Upload → Analyze → Extract → Ask**

---

# 🧠 Challenges & Learnings

## Challenges

### Model Availability and Stability

During development, we initially tested another Gemma 4 model configuration that returned HTTP 500 errors in one development environment.

We tested the available Gemma 4 models and selected:

`gemma-4-26b-a4b-it`

because it provided reliable results for our working application.

### Multimodal Integration

Connecting image uploads with Gemma 4 and getting useful structured responses required testing both the API integration and prompts.

### Prompt Engineering

We needed to design prompts that:

- Extract the correct information.
- Return consistent fields.
- Avoid inventing missing information.
- Support follow-up questions.

### Git Collaboration

Since multiple team members were developing different parts of the project simultaneously, we encountered Git synchronization issues.

We learned to use collaborative workflows such as:

```bash
git pull --rebase origin main
git push origin main
```

instead of force-pushing changes.

### Hackathon Time Constraints

With limited hackathon time, we prioritized a reliable core MVP instead of attempting too many additional features.

---

# 📚 What We Learned

Through this project, we gained practical experience with:

- Gemma 4 multimodal AI
- Prompt engineering
- Structured information extraction
- AI-powered question answering
- Streamlit application development
- Google GenAI SDK
- Git and GitHub collaboration
- Rapid MVP development
- Testing AI applications with real-world documents

---

# 🔮 Future Scope

CampusLens can be extended with:

- 📅 Calendar integration
- 🔔 Smart reminders for deadlines
- ✅ Automatic action-item generation
- 📚 Support for more document types
- 🌐 Multilingual document understanding
- 🔍 Search across multiple uploaded campus documents
- 📱 Improved mobile experience
- 🏫 Integration with college information systems

These features are potential future improvements beyond the current hackathon MVP.

---

# 🖥️ Working Application

CampusLens currently runs as a Streamlit application.

## Demo Video

▶️ [**Watch the CampusLens AI Demo**](https://youtu.be/EYpPQo6tEKM)

The demo shows the core workflow:

**Upload → Gemma 4 Analysis → Information Extraction → Q&A**

## GitHub Repository

https://github.com/lakshiscooby-alt/campuslens-ai

---

# 📸 Demo

![CampusLens AI Demo](demo.png)

---

# 🔧 Setup & Usage

## 1. Clone the Repository

```bash
git clone https://github.com/lakshiscooby-alt/campuslens-ai.git
cd campuslens-ai
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure the Gemini API Key

Set the `GEMINI_API_KEY` environment variable.

For Git Bash:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

For Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

**Do not commit or share your API key.**

## 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

# 🔐 Open Source & AI Usage

CampusLens AI was developed as an open-source hackathon project.

### AI Model

**Gemma 4** is the core multimodal AI model used for:

- Understanding uploaded documents
- Extracting structured information
- Answering student questions

### SDK

The project uses the **Google GenAI SDK** to interact with the model.

### Open Source

The source code is available in this repository for others to explore and build upon.

---

# 🏆 Hackathon Submission

**Hackathon:** MLH Hacktoberfest Hack Day Coimbatore

**Team:** Synap Tech

**Challenge Focus:** Best Use of Gemma 4

**Demo Video:**  
https://youtu.be/EYpPQo6tEKM

**Repository:**  
https://github.com/lakshiscooby-alt/campuslens-ai

---

# 📝 Devpost Submission

The final Devpost submission will include:

- Project description
- Problem statement
- Solution
- Key features
- Technical implementation
- Team contributions
- GitHub repository
- Demo video
- Gemma 4 usage
- Hackathon challenge category
### DEV.to Project Post

[Read our DEV.to project post](https://dev.to/lakshiscoobyalt/campuslens-ai-a-gemma-4-multimodal-assistant-for-college-notices-3iip)

---

# 📜 Credits and License

Built by **Synap Tech** during the MLH Hacktoberfest Hack Day Coimbatore.

## Team

- Lakshithaa V
- Pavitraa Surendran
- Shivamihit G
- Rithvik Kumar

## License

This project is released under the **MIT License**.

See [LICENSE](LICENSE) for details.

---

# ✅ Submission Checklist

- [x] Working Streamlit application
- [x] Gemma 4 integration
- [x] Multimodal document understanding
- [x] Structured information extraction
- [x] Question answering
- [x] GitHub repository
- [x] `requirements.txt`
- [x] Demo screenshot
- [x] Demo video
- [x] Team contributions documented
- [x] Challenges and learnings documented
- [x] Setup instructions
- [x] Open-source information
- [x] Final Devpost submission
- [x] Final hackathon submission
