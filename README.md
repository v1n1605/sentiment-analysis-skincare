# 🧴 Sentiment Analysis Produk Skincare

Aplikasi berbasis Machine Learning untuk melakukan klasifikasi sentimen terhadap ulasan produk skincare menggunakan algoritma:

- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

Aplikasi ini dibangun menggunakan **Python**, **Scikit-Learn**, dan **Streamlit** sehingga dapat digunakan secara online melalui web.

---

## 📌 Fitur

- Prediksi sentimen ulasan skincare
- Preprocessing teks otomatis
- Klasifikasi sentimen Positif, Negatif, dan Netral
- Menampilkan confidence score
- Antarmuka web menggunakan Streamlit
- Model terbaik dipilih berdasarkan akurasi pengujian

---

## 📂 Struktur Project

```text
.
├── app.py
├── model.pkl
├── tfidf.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
```

---

## ⚙️ Library yang Digunakan

- streamlit
- scikit-learn
- pandas
- numpy
- nltk
- scipy
- joblib

---

## 🚀 Menjalankan Program Secara Lokal

Install seluruh library:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
streamlit run app.py
```

Kemudian buka:

```text
http://localhost:8501
```

---

## 🧠 Metode yang Digunakan

### Text Preprocessing

- Case Folding
- Cleansing
- Tokenizing
- Stopword Removal
- Stemming

### Feature Extraction

- TF-IDF Vectorization

### Algoritma Klasifikasi

1. Random Forest
2. Support Vector Machine (LinearSVC)
3. Naive Bayes

Model terbaik dipilih berdasarkan nilai akurasi pada data testing.

---

## 📊 Evaluasi Model

Parameter evaluasi yang digunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

---

## 🌐 Deployment

Aplikasi dideploy menggunakan:

- Streamlit Community Cloud

---

## 👨‍💻 Author

Nama : Abdullah Kevin  
Universitas : Universitas Islam Negeri Maulana Malik Ibrahim Malang
