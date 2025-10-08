import spacy
import re
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "Python", "C++", "Java", "TensorFlow", "Keras", "React", "Node.js",
    "SQL", "Machine Learning", "Data Analysis", "FastAPI", "AWS", "HTML", "CSS"
]

def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text):
            found.append(skill)
    return list(set(found))

def parse_resume(file):
    text = extract_text_from_pdf(file)
    doc = nlp(text)
    skills = extract_skills(text)
    summary = " ".join([sent.text for sent in list(doc.sents)[:5]])
    return {"text": text, "skills": skills, "summary": summary}
