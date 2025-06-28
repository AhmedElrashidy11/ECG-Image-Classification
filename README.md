
# 🫀 ECG Image Classification using Deep Learning

This project classifies ECG images into different clinical categories using a Convolutional Neural Network (CNN).

---

## 📁 Project Structure

```
ECG-Image-Classification/
│
├── Deployment/
│   ├── app.py               # Streamlit web application
│   └── ecg_model.h5         # 🔺 Not included (download below)
│
├── dataset/                 # (Optional) ECG training data
├── models/                  # Model checkpoints or saved logs
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## 📦 Download Assets

### 🔹 Dataset Source:
The ECG image dataset was obtained from Kaggle:  
📂 [ECG Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/evilspirit05/ecg-analysis)

### 🔹 Trained Model:
Due to GitHub's file size limits, the trained model is hosted externally.  
📥 **[Download `ecg_model.h5` (Google Drive)](https://drive.google.com/file/d/1RKHBI8iKVx28_VsnTBHcaw6lkdtvdtjv/view?usp=sharing)**

After downloading, place it in:
```
Deployment/ecg_model.h5
```

---

## 🚀 How to Run the App

1. **Clone the repository:**
```bash
git clone https://github.com/AhmedElrashidy11/ECG-Image-Classification.git
cd ECG-Image-Classification
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv .venv
.\.venv\Scriptsctivate    # For Windows
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit web app:**
```bash
cd Deployment
streamlit run app.py
```

---

## 📊 Model Evaluation

The model was evaluated on a test set of 928 ECG images across 4 classes:

| Class                                                                 | Precision | Recall | F1-score | Support |
|-----------------------------------------------------------------------|-----------|--------|----------|---------|
| ECG Images of Myocardial Infarction Patients (240x12 = 2880)         | 1.00      | 1.00   | 1.00     | 239     |
| ECG Images of Patients with History of MI (172x12 = 2064)            | 0.96      | 1.00   | 0.98     | 172     |
| ECG Images of Patients with Abnormal Heartbeat (233x12 = 2796)       | 0.99      | 1.00   | 1.00     | 233     |
| Normal Person ECG Images (284x12 = 3408)                             | 1.00      | 0.96   | 0.98     | 284     |

**Overall Accuracy:** `0.99` (on 928 test samples)  
**Macro Avg:** Precision = `0.99`, Recall = `0.99`, F1-score = `0.99`  
**Weighted Avg:** Precision = `0.99`, Recall = `0.99`, F1-score = `0.99`

---

## 🛠️ Technologies Used

- Python 3.9+
- TensorFlow / Keras
- OpenCV
- NumPy, Pandas
- Streamlit
- Scikit-learn
- Matplotlib

---

## 👨‍💻 Author

**Ahmed Elrashidy**  
Data Science & AI Engineer – Zewail City  
[GitHub](https://github.com/AhmedElrashidy11) • [LinkedIn](https://www.linkedin.com/in/ahmedelrashidy)

**Mariam Mohamed**
Data Science & AI Engineer – Zewail City
[LinkedIn](https://www.linkedin.com/in/mariamgoda)

---

## 📄 License

This project is for educational and academic use only.
