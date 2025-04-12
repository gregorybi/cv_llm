# Large Language Model analyzing CV

In this project an LLM has been developed that handles candiatates CV data.
The model summarizes the CV and produces output regarding canditates tech and soft skills.
The model also provides suggestions for CV optimization.


## Table of Contents

- [Intro] (#intro)
- [Prerequisites] (#prerequisites)
- [Setup] (#setup)
- [Execute] (#execute)

## Table of Contents

- [Intro] (#intro)
- [Prerequisites] (#prerequisites)
- [Setup] (#setup)
- [Execute] (#execute)
- [Algorithm] (#algorithm)

## Intro
- The model used is BART (Bidirectional and Auto-Regressive Transformer)
- The language of developement is Python

## Prerequisites
- Install [Python 3]
- Install [Dependencies]
- Has to be execute in linux based environment

## Setup
1. Clone the repository:

```bash
git clone https://github.com/gregorybi/cv_llm.git
cd cv_llm
```

## Execute
1. Execute the Python script in the terminal

```bash
python3 resume_analyzer.py
```

## Algorithm
The model reads CV and produces a brief summary.
It also finds keywords asocciated with technical and soft skills of the canditate and displays them seperately.
Furthermore it also produces CV improvement suggestions based on the data provided.