
# 🫀 ECG Image Classification using Deep Learning

This project classifies ECG images into different clinical categories using a Convolutional Neural Network (CNN). It was developed as part of the **DSAI 308** course at Zewail City – Year 3, Semester 2.

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

| Class                                                            | Precision | Recall | F1-score |
|------------------------------------------------------------------|-----------|--------|----------|
| ECG Images of Myocardial Infarction Patients (240x12=2880)       | 1.00      | 1.00   | 1.00     |
| ECG Images of Patients with History of MI (172x12=2064)          | 0.96      | 1.00   | 0.98     |

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
