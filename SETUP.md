# 🛠️ Setup Instructions – ForensicsDetective (Assignment 3)
This document provides a step-by-step guide to set up, configure, and run the **ForensicsDetective** project on Windows 11 using Python 3.14 in a virtual environment.

---

## 📋 Prerequisites
Ensure the following are installed on your system:
- **Python 3.14+**
- **pip** (Python package manager)
- **Git**
- **VS Code** or any Python IDE

---

## ⚙️ 1. Clone or Download the Repository
You can either fork the instructor’s repository and clone it, or directly download the project ZIP.

```bash
git clone https://github.com/YourUsername/Assignment3_ForensicsDetective.git
cd Assignment3_ForensicsDetective
```

---

## 🧱 2. Create and Activate a Virtual Environment
This ensures your dependencies are isolated and reproducible.

### On Windows PowerShell:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux (for reference):
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 3. Install Dependencies
Install all required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

> 💡 Tip: If you previously saw LF/CRLF warnings in Git, you can run the following to prevent them permanently:
> ```bash
> git config --global core.autocrlf true
> ```

---

## 🧩 4. Project Structure Overview
```
Assignment3_DilipNallamasa/
│
├── data/                     # Source & converted PDFs
│   ├── source_documents/
│   ├── word_pdfs/
│   ├── google_docs_pdfs/
│   ├── python_pdfs/
│   ├── fpdf_pdfs/
│   └── *_png/                # Converted image versions
│
├── models/                   # Trained model files (.pkl)
├── results/                  # Confusion matrices, metrics, stats
├── reports/                  # Final report PDF
├── src/                      # Source code scripts
│   ├── data_generation.py
│   ├── image_conversion.py
│   ├── classification.py
│   ├── analysis.py
│   ├── utils.py
│
├── README.md
├── SETUP.md
└── requirements.txt
```

---

## 🚀 5. Running the Project
### Step 1: Generate Data
```bash
python src/data_generation.py
```

### Step 2: Convert PDFs to Images
```bash
python src/image_conversion.py
```

### Step 3: Train and Evaluate Classifiers
```bash
python src/classification.py
```

### Step 4: Perform Statistical Analysis
```bash
python results/statistical_analysis.py
```

All trained models, metrics, and visualizations will be saved in the `/results` directory.

---

## 📊 6. Expected Outputs
| Output File | Description |
|--------------|-------------|
| `confusion_matrices/` | Confusion matrices for each classifier |
| `performance_metrics.csv` | Accuracy, F1, precision, recall metrics |
| `statistical_significance.csv` | McNemar test results |
| `final_research_report.pdf` | Comprehensive summary of analysis |

---

## 🧠 7. Notes for Graders
- All experiments were conducted in **Python 3.14 (venv)** on **Windows 11**.
- The fourth source was generated using **LibreOffice** for diversity.
- 10,000 PDFs per source were generated; training used **7,000 samples/class** for efficiency.
- All models (SVM, SGD, RF, MLP) achieved **over 99% accuracy** with verified statistical results.

---

## ✅ 8. Troubleshooting
| Issue | Solution |
|--------|-----------|
| `ModuleNotFoundError` | Ensure you’ve activated the venv and installed dependencies |
| LF/CRLF warning | Run `git config --global core.autocrlf true` (safe fix) |
| Slow training | Reduce samples or use `n_jobs=-1` |
| MemoryError | Close other programs or reduce dataset size |

---

## 🏁 9. Final Verification Before Submission
Before pushing to GitHub or submitting:
```bash
pytest src/ --maxfail=1 --disable-warnings -q
```
Ensure all tests pass, then commit and push your repository.

---

**End of SETUP.md**
