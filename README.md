```markdown
# 🛡️ Hate Speech Classifier — NLP Project

A machine learning system to automatically detect hate speech in YouTube comments, built for scalability and production readiness.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Development Workflow](#development-workflow)
- [Team](#team)

---

## 🔍 Overview

YouTube faces a growing problem with hate speech in video comments. This project builds an automated solution to detect and flag hate speech messages, allowing moderators to take action at scale.

### Objectives
- Analyze and preprocess a YouTube comments dataset
- Implement classical NLP techniques
- Train and evaluate ML classification models
- Deploy a user-facing interface for real-time detection

---

## 📁 Project Structure
```
project-ai-nlp/
├── data/
│   ├── raw/              → original unmodified data
│   ├── processed/        → cleaned and ready data
│   └── external/         → data from APIs or scraping
│
├── notebooks/
│   ├── exploration/      → free EDA and analysis
│   ├── experiments/      → model experiments
│   └── reports/          → final clean results
│
├── src/
│   ├── data/             → data loading and validation
│   ├── features/         → preprocessing and vectorization
│   ├── models/           → training, evaluation, prediction
│   ├── visualization/    → reusable plots
│   └── api/              → FastAPI / Streamlit app
│
├── tests/
│   ├── unit/             → unit tests
│   └── integration/      → pipeline tests
│
├── configs/              → parameters and configuration
├── docker/               → Dockerfile and docker-compose
├── docs/                 → technical documentation
├── scripts/              → executable pipelines
├── models/
│   ├── saved/            → trained models
│   └── metrics/          → results and metrics
│
├── Makefile
├── pyproject.toml
└── README.md
```

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11+ |
| Package Manager | uv |
| NLP | NLTK, SpaCy |
| ML | Scikit-learn, Optuna |
| Deep Learning | TensorFlow / PyTorch |
| Transformers | HuggingFace |
| Interface | Streamlit / FastAPI |
| Experiment Tracking | MLFlow |
| Testing | Pytest |
| Containerization | Docker |
| Version Control | Git / GitHub |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- uv installed → https://docs.astral.sh/uv/

### Installation

```bash
# Clone the repository
git clone https://github.com/Factoria-F5-madrid/project-ai-nlp.git
cd project-ai-nlp

# Install dependencies
make install

# Set up environment variables
cp .env.example .env
```

### Register Jupyter kernel

```bash
uv run python -m ipykernel install --user --name=project-ai-nlp --display-name "Python (project-ai-nlp)"
```

---

## 💻 Usage

### Run the app
```bash
make run
```

### Train the model
```bash
make train
```

### Run tests
```bash
make test
```

---

## 🔀 Development Workflow
feature/branch → develop → main

1. Create your feature branch from develop  
2. Work on your feature  
3. Open a Pull Request to develop  
4. After review, merge to develop  
5. When stable, merge develop to main  

### Branch naming convention
- feature/setup  
- feature/eda  
- feature/preprocessing  
- feature/ml-model  
- feature/interface  

### Commit convention
- feat: add preprocessing pipeline  
- fix: correct tokenization bug  
- docs: update README  
- test: add unit tests for model  
- refactor: clean preprocessing functions  

---

## 👥 Team

| Name | GitHub |
|---|---|
| Andres Torrez | @Andres-Torrez |

---

## 📄 License

MIT License
```

---