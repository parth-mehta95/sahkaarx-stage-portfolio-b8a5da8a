# SahkaarX Learning Portfolio

[![Repository Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a)
[![Branch](https://img.shields.io/badge/branch-feature%2Finitial--repo--setup-blue.svg)](https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a/tree/feature/initial-repo-setup)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A clean, modular, and collaborative team portfolio repository establishing clean structure and professional Git practices from Day 1.

---

## 📌 Repository Overview

This repository serves as the shared engineering workspace for the **SahkaarX** program. It is configured to follow industry-standard software engineering workflows, including:
- Modular directory architecture separating source code, tests, documentation, and exercises.
- Professional Git branching workflow (`feature/*`, `fix/*`, `docs/*`) targeting protected `main`.
- Conventional Commit conventions for traceable version control.
- Pull request templates and code review standards.

---

## 📂 Project Structure

```text
sahkaarx-stage-portfolio-b8a5da8a/
├── .github/
│   └── pull_request_template.md        # Pull request template for peer reviews
├── docs/
│   └── git-workflow.md                 # Team branching, commit & PR guidelines
├── practice/
│   └── week-01-initialize-portfolio-repository-on-github/
│       └── README.md                   # Week 01 task brief and guidelines
├── src/
│   ├── __init__.py                     # Package initialization
│   └── main.py                         # Application entry point
├── tests/
│   ├── __init__.py                     # Test suite initialization
│   └── test_basic.py                   # Initial smoke test
├── .gitignore                          # Standard git ignore definitions
└── README.md                           # Main repository documentation
```

---

## 🚀 Getting Started

### Prerequisites
- [Git](https://git-scm.com/) (version 2.30+ recommended)
- [Python](https://www.python.org/) (version 3.9+ recommended)

### Clone the Repository
```bash
git clone https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a.git
cd sahkaarx-stage-portfolio-b8a5da8a
```

### Running the Application
```bash
python -m src.main
```

### Running Tests
```bash
pytest tests/
```

---

## 🌿 Git & Collaboration Workflow

We strictly follow a feature-branch workflow to maintain stability on the `main` branch.

1. **Create a Feature Branch:**
   ```bash
   git checkout -b feature/<descriptive-name>
   ```

2. **Make Atomic Commits:**
   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat: implement modular project structure"
   ```

3. **Push to Remote & Open Pull Request:**
   ```bash
   git push -u origin feature/<descriptive-name>
   ```

Refer to [`docs/git-workflow.md`](docs/git-workflow.md) for full details on commit formats and PR checklist.

---

## 🔗 Submission Details

- **Repository URL:** [https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a](https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a)
- **Feature Branch:** [`feature/initial-repo-setup`](https://github.com/parth-mehta95/sahkaarx-stage-portfolio-b8a5da8a/tree/feature/initial-repo-setup)
- **Status:** Initialized structure and feature branch with 2+ commits ready for Pull Request.
