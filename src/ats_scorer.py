def ats_score(
    resume_text,
    resume_skills,
    jd_skills,
    cleaned_resume_text,
    cleaned_jd_text
):
    score = 0

    # 1️⃣ Skill Match Coverage (40 points)
    if jd_skills:
        skill_match_ratio = len(set(resume_skills) & set(jd_skills)) / len(jd_skills)
        score += skill_match_ratio * 40

    # 2️⃣ Keyword Match (30 points)
    resume_words = set(cleaned_resume_text.split())
    jd_words = set(cleaned_jd_text.split())

    if jd_words:
        keyword_ratio = len(resume_words & jd_words) / len(jd_words)
        score += keyword_ratio * 30

    # 3️⃣ Resume Length Score (15 points)
    word_count = len(resume_text.split())

    if 300 <= word_count <= 900:
        score += 15
    elif 200 <= word_count < 300 or 900 < word_count <= 1100:
        score += 8
    else:
        score += 4

    # 4️⃣ Formatting / Cleanliness (15 points)
    special_char_ratio = sum(
        not c.isalnum() and not c.isspace() for c in resume_text
    ) / max(len(resume_text), 1)

    if special_char_ratio < 0.05:
        score += 15
    elif special_char_ratio < 0.1:
        score += 8
    else:
        score += 4

    return round(score, 2)
