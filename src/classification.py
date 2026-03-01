import os
import sys
import numpy as np
from PIL import Image
import time
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# Add local src folder to sys.path to avoid import errors
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import save_confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# ---------------- DATA LOADING ---------------- #
def load_4class_dataset(max_samples_per_class=7000, target_size=(200,200)):
    """Load 4-class grayscale flattened images."""
    print(f"Loading dataset ({max_samples_per_class} per class) with image size {target_size}...")
    X, y = [], []

    def load_images_from_dir(folder, label, limit):
        files = [f for f in os.listdir(folder) if f.endswith('.png')]
        files = files[:limit]
        print(f" -> Loading {len(files)} images from {folder}")
        for filename in files:
            path = os.path.join(folder, filename)
            try:
                img = Image.open(path).convert('L')
                img = img.resize(target_size, Image.LANCZOS)
                X.append(np.array(img).flatten())
                y.append(label)
            except Exception as e:
                print(f"   Skipped {filename}: {e}")

    load_images_from_dir('data/word_pdfs_png', 0, max_samples_per_class)
    load_images_from_dir('data/google_docs_pdfs_png', 1, max_samples_per_class)
    load_images_from_dir('data/python_pdfs_png', 2, max_samples_per_class)
    load_images_from_dir('data/fpdf_pdfs_png', 3, max_samples_per_class)

    X = np.array(X)
    y = np.array(y)
    print(f"Dataset loaded: {len(X)} samples, {X.shape[1]} features each")
    return X, y

# ---------------- TRAIN & EVALUATE ---------------- #
def train_and_evaluate(model, X_train, y_train, X_test, y_test, name):
    print(f"\n=== Training {name} ===")
    start = time.time()
    model.fit(X_train, y_train)
    elapsed = time.time() - start

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f} (trained in {elapsed:.2f}s)")
    print(classification_report(y_test, y_pred, target_names=['Word','Google','Python','FPDF']))

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

    os.makedirs("results/confusion_matrices", exist_ok=True)
    save_confusion_matrix(cm, classes=['Word','Google','Python','FPDF'],
                          title=name, filename=f"results/confusion_matrices/{name}_cm.png")
    return model, acc

# ---------------- MAIN ---------------- #
def main():
    X, y = load_4class_dataset(max_samples_per_class=7000, target_size=(200,200))

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

    # ---------- CLASSIFIERS ----------
    svm_model, svm_acc = train_and_evaluate(
        LinearSVC(C=1, max_iter=5000, dual=False, random_state=42),
        X_train, y_train, X_test, y_test, "SVM"
    )

    sgd_model, sgd_acc = train_and_evaluate(
        SGDClassifier(loss='hinge', max_iter=1000, tol=1e-3, random_state=42),
        X_train, y_train, X_test, y_test, "SGD"
    )

    rf_model, rf_acc = train_and_evaluate(
        RandomForestClassifier(n_estimators=50, max_depth=20, n_jobs=-1, random_state=42),
        X_train, y_train, X_test, y_test, "Random Forest"
    )

    mlp_model, mlp_acc = train_and_evaluate(
        MLPClassifier(hidden_layer_sizes=(100,50), max_iter=300, early_stopping=True, random_state=42),
        X_train, y_train, X_test, y_test, "MLP"
    )

    # ---------- SAVE MODELS ----------
    os.makedirs("results", exist_ok=True)
    for model_name, model_obj in zip(["svm","sgd","rf","mlp"], [svm_model, sgd_model, rf_model, mlp_model]):
        with open(f"results/{model_name}_model.pkl", "wb") as f:
            pickle.dump(model_obj, f)

    with open("results/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    # ---------- SAVE TEST DATA FOR STATISTICAL ANALYSIS ----------
    with open("results/X_test.pkl", "wb") as f:
        pickle.dump(X_test, f)
    with open("results/y_test.pkl", "wb") as f:
        pickle.dump(y_test, f)

    # ---------- SAVE PERFORMANCE METRICS ----------
    metrics = pd.DataFrame({
        "Classifier": ["SVM","SGD","Random Forest","MLP"],
        "Accuracy": [svm_acc, sgd_acc, rf_acc, mlp_acc]
    })
    metrics.to_csv("results/performance_metrics.csv", index=False)

if __name__ == "__main__":
    main()
