from transformers import pipeline
import nltk
import re

# Sentence tokenization
nltk.download('punkt')

# CV text
resume_text = """
George Athanasiou is a junior machine learning engineer with a background in SVM-based classification models.
He gratuated recently and completed his research thesis using support vector machines for text classification.
Skilled in Python, Scikit-learn, K-means clustering, data preprocessing, and model evaluation.
He is a team player, fast learner and problem solver 
with strong communication skills and keen atention to detail. 
Currently studying large language models.
"""

# Quick review
print("Loading summarizer ...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_resume(text):
    
    summary = summarizer(text, max_length=100, min_length=60, do_sample=False)
    return summary[0]['summary_text']

# Find skills
tech_keywords = ["Python", "Scikit-learn", "PyTorch", "TensorFlow", "data preprocessing",
                 "SVM", "transformer", "BERT", "NLP", "machine learning", "model evaluation"
                 , "large language models"]

soft_keywords = ["team", "communication", "problem solver", "adapt", "fast learner", "collaborate", 
                 "attention to detail"]


# return first 5 skills from the resume
def extract_skills(text, keywords):
    found = [word for word in keywords if re.search(rf"\b{word}\b", text, re.IGNORECASE)]
    return found[:5]
    

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
    print (*extract_skills(resume_text, tech_keywords), sep=', ')
    

    print("\n Soft Skills Found:")
    print (*extract_skills(resume_text, soft_keywords), sep=', ')
    

    print("\n Suggestions:")
    for suggestion in suggest_improvements(resume_text):
        print(suggestion)
