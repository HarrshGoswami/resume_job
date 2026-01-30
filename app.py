import streamlit as st

from src.resume_parser import extract_text
from src.text_cleaner import clean_text
from src.skill_extractor import load_skills, extract_skills
from src.matcher import calculate_match_score
from src.ats_scorer import ats_score


st.set_page_config(page_title="AI Resume–Job Match Analyzer", layout="centered")

st.title("AI-Powered Resume & Job Match Analyzer")

st.write(
    "Upload your resume and paste a job description to get a match score, "
    "ATS score, and skill gap analysis."
)

# -----------------------------
# Inputs
# -----------------------------
resume_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# -----------------------------
# Processing
# -----------------------------
if resume_file and job_description:

    # 1️⃣ Extract & clean text
    resume_text = extract_text(resume_file)
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_description)

    # 2️⃣ Load skills & extract
    skills_list = load_skills()
    resume_skills = extract_skills(resume_clean, skills_list)
    jd_skills = extract_skills(jd_clean, skills_list)

    # 3️⃣ Match score
    match_score = calculate_match_score(resume_clean, jd_clean)

    # 4️⃣ ATS score
    ats = ats_score(
        resume_text=resume_text,
        resume_skills=resume_skills,
        jd_skills=jd_skills,
        cleaned_resume_text=resume_clean,
        cleaned_jd_text=jd_clean
    )

    # 5️⃣ Missing skills
    missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))

    # -----------------------------
    # Output
    # -----------------------------
    st.subheader("📊 Match Results")

    st.metric(label="Resume–JD Match Score", value=f"{match_score}%")
    st.metric(label="ATS Resume Score", value=f"{ats} / 100")

    st.subheader("✅ Skills Found in Resume")
    if resume_skills:
        st.write(resume_skills)
    else:
        st.warning("No relevant skills detected in resume.")

    st.subheader("📋 Skills Required by Job Description")
    if jd_skills:
        st.write(jd_skills)
    else:
        st.warning("No relevant skills detected in job description.")

    st.subheader("❌ Missing Skills")
    if missing_skills:
        st.warning(missing_skills)
    else:
        st.success("No major skill gaps found 🎉")

else:
    st.info("Please upload a resume and paste a job description to continue.")
