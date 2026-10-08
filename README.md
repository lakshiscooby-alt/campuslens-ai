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
