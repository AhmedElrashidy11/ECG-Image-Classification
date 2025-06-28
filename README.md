ممتاز يا أحمد 👌 شكرًا لمشاركة الروابط!

الآن أدرجتها في ملف `README.md` لك بشكل منسّق واحترافي.

---

### 📄 ملف `README.md` النهائي (جاهز للنسخ والاستخدام):

```markdown
# ECG Image Classification using Deep Learning 🫀📊

This project classifies ECG images into multiple clinical categories using a Convolutional Neural Network (CNN).  
It was developed as part of the **DSAI 308** course at Zewail City.

---

## 📁 Project Structure

```

Project/
│
├── Deployment/              # Streamlit app interface
│   ├── app.py               # Web app for ECG image upload and prediction
│   └── ecg\_model.h5         # (Not included - download below)
│
├── dataset/                 # (Optional) ECG images used in training
├── models/                  # Saved models, logs, or checkpoints
├── README.md                # Documentation
└── requirements.txt         # Python dependencies

```

---

## 📥 Downloads

### 🔹 Dataset:
This project uses ECG images from Kaggle:  
📂 **[ECG Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/evilspirit05/ecg-analysis)**

### 🔹 Trained Model:
Due to GitHub's 100MB file limit, the trained model `ecg_model.h5` is hosted externally:  
📦 **[Download ecg_model.h5 from Google Drive](https://drive.google.com/file/d/1RKHBI8iKVx28_VsnTBHcaw6lkdtvdtjv/view?usp=sharing)**

➡️ After downloading, place the file in:
```

Deployment/ecg\_model.h5

````

---

## 🚀 How to Run

1. **Clone the repo:**
```bash
git clone https://github.com/AhmedElrashidy11/ECG-Image-Classification.git
cd ECG-Image-Classification
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add model file:**
   Place `ecg_model.h5` inside the `Deployment/` folder.

4. **Run the Streamlit app:**

```bash
cd Deployment
streamlit run app.py
```

---

## 📊 Model Evaluation

| Class                                                      | Precision | Recall | F1-score |
| ---------------------------------------------------------- | --------- | ------ | -------- |
| ECG Images of Myocardial Infarction Patients (240x12=2880) | 1.00      | 1.00   | 1.00     |
| ECG Images of Patients with History of MI (172x12=2064)    | 0.96      | 1.00   | 0.98     |

---

## 📚 Technologies Used

* Python 3.9+
* TensorFlow / Keras
* Streamlit
* NumPy, OpenCV
* Scikit-learn

---

## 👨‍💻 Author

**Ahmed Elrashidy**
Data Science & AI Engineer – Zewail City
[GitHub](https://github.com/AhmedElrashidy11) • [LinkedIn](https://www.linkedin.com/in/ahmedelrashidy)

---

## 🧠 License

This project is for academic and educational purposes only.

````
