# Resume Job Matching & ATS Scoring System

This project is a Python-based Resume–Job Description matching system that simulates how an Applicant Tracking System (ATS) evaluates resumes against job descriptions.

It parses resumes, extracts skills, compares them with job requirements, and generates an ATS-style score to indicate how well a resume matches a given role.

---

## Features

- Resume text parsing
- Skill extraction from resume and job description
- Text cleaning and normalization
- ATS-style scoring logic
- Skill match coverage calculation
- Modular and extensible code structure

---

## Project Structure

resume_job_aai/
│
├── app.py # Main entry point
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files (venv, cache, etc.)
│
├── data/
│ └── skills.csv # Skill dataset
│
└── src/
├── ats_scorer.py # ATS scoring logic
├── matcher.py # Resume–JD matching logic
├── resume_parser.py # Resume text parsing
├── skill_extractor.py # Skill extraction logic
└── text_cleaner.py # Text preprocessing utilities

