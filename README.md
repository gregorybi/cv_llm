# Large Language Model analyzing CV

This project is an application using an LLM to handle a canditate's CV data.
The model summarizes the CV and produces output regarding canditate's tech and soft skills.
The model also provides suggestions for CV optimization.

## Table of Contents

- Intro
- Prerequisites
- Setup
- Execute
- Algorithm

## Intro
- The model used is facebook/bart-large-cnn
- Task: Text Summarization
- BART is a transformer model pre-trained for language understanding and generation.
- The language of developement is Python

## Prerequisites
- Python 3.8+
- pip
- Install Dependencies
- Has to be execute in linux based environment

## Setup
1. Clone the repository:

```bash
git clone https://github.com/gregorybi/cv_llm.git
cd cv_llm
```

2. Dowload the Model (Install Dependencies)
```bash
pip install transformers torch nltk
```
You’ll download the model the first time you run it.

## Execute
1. Edit the resume_text variable inside resume_analyzer.py with your resume content (or load a resume from a file).
   
2. Execute the Python script in the terminal

```bash
python3 resume_analyzer.py
```
3. The analyzer will print the resume summary, skill extraction and improvement suggestions in the terminal.

## Algorithm
The model reads CV and produces a brief summary.\
It also finds keywords asocciated with technical and soft skills of the canditate and displays them seperately.\
Furthermore it also produces CV improvement suggestions based on the data provided.
