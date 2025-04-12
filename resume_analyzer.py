from transformers import pipeline
import nltk
import re

nltk.download('punkt')  # For sentence tokenization

# CV text
resume_text = """
John Doe is a junior machine learning engineer with a background in SVM-based classification models.
He completed a research thesis using support vector machines for text classification.
Skilled in Python, Scikit-learn, data preprocessing, and model evaluation.
Currently studying large language models and transformer architectures.
"""

# Quick review
print("⏳ Loading summarizer model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_resume(text):
    
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Find skills
tech_keywords = ["Python", "Scikit-learn", "PyTorch", "TensorFlow", "data preprocessing",
                 "SVM", "transformer", "BERT", "NLP", "machine learning", "model evaluation"]

soft_keywords = ["team", "communication", "problem", "adapt", "fast learner", "collaborate"]

def extract_skills(text, keywords):
    found = [word for word in keywords if re.search(rf"\b{word}\b", text, re.IGNORECASE)]
    return list(set(found))[:5]

# Improvement suggestions
def suggest_improvements(text):
    suggestions = []
    if "project" not in text.lower():
        suggestions.append("- Add at least one personal or academic project.")
    if "github" not in text.lower():
        suggestions.append("- Include a link to your GitHub or portfolio.")
    if "metrics" not in text.lower():
        suggestions.append("- Quantify achievements with metrics (e.g., 95% accuracy).")
    return suggestions if suggestions else ["- Looks good! Just tailor it to specific job roles."]

# Execution
if __name__ == "__main__":
    print("\n Summary:")
    print(summarize_resume(resume_text))

    print("\n Technical Skills Found:")
    print(", ".join(extract_skills(resume_text, tech_keywords)))

    print("\n Soft Skills Found:")
    print(", ".join(extract_skills(resume_text, soft_keywords)))

    print("\n Suggestions:")
    for s in suggest_improvements(resume_text):
        print(s)
