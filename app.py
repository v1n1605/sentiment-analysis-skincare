import streamlit as st
import joblib
import re

# Load model
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")
le = joblib.load("label_encoder.pkl")


# Preprocessing
def preprocess_text(text):

    text = str(text).lower()

    text = re.sub(r'http\S+|www\S+', '', text)

    text = re.sub(r'[^\w\s]', ' ', text)

    text = re.sub(r'\d+', '', text)

    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Prediksi
def predict_sentiment(text):

    text_clean = preprocess_text(text)

    text_tfidf = tfidf.transform([text_clean])

    prediction = model.predict(text_tfidf)[0]

    label = le.inverse_transform([prediction])[0]

    return label


# Tampilan Website
st.title("🧴 Analisis Sentimen Produk Skincare")

st.write("Masukkan ulasan produk skincare untuk mengetahui sentimennya.")

review = st.text_area(
    "Masukkan ulasan"
)

if st.button("Prediksi"):

    hasil = predict_sentiment(review)

    if str(hasil).lower() == "positif":
        st.success(f"😊 Sentimen : {hasil}")

    elif str(hasil).lower() == "negatif":
        st.error(f"😞 Sentimen : {hasil}")

    else:
        st.info(f"😐 Sentimen : {hasil}")