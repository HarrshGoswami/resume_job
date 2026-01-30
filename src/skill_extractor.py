import pandas as pd

def load_skills(path="data/skills.csv"):
    df = pd.read_csv(path)
    return [skill.lower() for skill in df["skill"].tolist()]

def extract_skills(text, skills_list):
    extracted = []
    for skill in skills_list:
        if skill in text:
            extracted.append(skill)
    return list(set(extracted))

