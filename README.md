ForensicsDetective: PDF Provenance Classification📘 Project OverviewForensicsDetective is a specialized machine learning system built to identify the digital "fingerprints" left by document creation software. By analyzing structural artifacts, font embedding patterns, and pixel-level rendering differences, this pipeline classifies the origin of PDF documents across four major sources: Microsoft Word, Google Docs, ReportLab (Python), and LibreOffice.🎯 Key AchievementsHigh-Fidelity Classification: Achieved a peak accuracy of 99.96% using a Multi-Layer Perceptron (MLP) model.Large-Scale Synthetic Data: Generated a balanced dataset of 40,000+ PDFs to ensure robust model generalization.Statistical Rigor: Validated model performance using McNemar’s Test to confirm significant improvements over baseline SVM architectures.⚙️ Technical Architecture1. Data Generation & PreprocessingDiverse Sourcing: Integrated LibreOffice as a fourth source to capture unique open-source rendering signatures.Pixel-Level Analysis: Converted PDFs to high-resolution .png images via Pillow to extract visual forensic cues.Feature Engineering: Resized and flattened images into $200 \times 200$ grayscale feature vectors, normalized using StandardScaler.2. Model ZooThe pipeline evaluates four distinct algorithmic families to ensure the most robust classification:CategoryModelJustificationNeural NetworkMLP ClassifierModels complex, non-linear feature interactions (Best Performer).Optimization-BasedSGD ClassifierHigh-efficiency approximation for rapid real-time inference.Ensemble MethodRandom ForestCaptures non-linear relationships via tree aggregation.Margin-BasedSVMProvides strong linear decision boundaries for high-dimensional data.📊 Experimental ResultsPerformance MetricsModelAccuracyTraining TimeMLP99.96%210sSGD99.84%39sSVM99.73%1744sRandom Forest99.73%11sStatistical Validation (McNemar’s Test)To ensure results were statistically significant ($p < 0.05$):SVM vs. MLP: $p = 0.0002$ (Highly Significant ✅)SVM vs. SGD: $p = 0.031$ (Significant ✅)🚀 Getting StartedPrerequisitesPython 3.14+Virtual Environment (Recommended)InstallationBashgit clone https://github.com/yourusername/pdf-provenance-classifier.git
cd pdf-provenance-classifier
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
ExecutionTrain & Evaluate: python src/classification.pyGenerate Visuals: python src/analysis.pyStatistical Test: python src/statistical_analysis.py📂 Project StructurePlaintext├── src/
│   ├── classification.py       # Core training & evaluation logic
│   ├── analysis.py             # Visualization & metric generation
│   └── statistical_analysis.py  # McNemar significance testing
├── results/
│   ├── confusion_matrices/     # Visual performance breakdowns
│   └── performance_metrics.csv  # Raw data output
├── reports/
│   └── final_research_report.pdf # Formal 3-page academic report
└── requirements.txt            # Project dependencies
🤝 ContributingDeveloped by Dilip Nallamasa as part of advanced AI coursework. Contributions to expand the source library (e.g., Adobe Acrobat, LaTeX) are welcome!
