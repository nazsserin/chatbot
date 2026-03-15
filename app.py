import streamlit as st
import os

# Nika'nın hafıza dosyası
HAFIZA_DOSYASI = "hafiza.txt"

# Dosya yoksa oluştur
if not os.path.exists(HAFIZA_DOSYASI):
    with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f:
        f.write("merhaba:Selam ben Nika\n")

def hafizayi_oku():
    sozluk = {}
    with open(HAFIZA_DOSYASI, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, val = line.strip().split(":", 1)
                sozluk[key] = val
    return sozluk

def hafizaya_kaydet(soru, cevap):
    with open(HAFIZA_DOSYASI, "a", encoding="utf-8") as f:
        f.write(f"{soru}:{cevap}\n")

st.title("Nika'nın Hafızası")
sozluk = hafizayi_oku()

soru = st.text_input("Nika'ya bir şey öğret veya sor:").lower()

if st.button("Gönder"):
    if soru in sozluk:
        st.write(f"Nika: {sozluk[soru]}")
    else:
        st.write("Nika: Bunu bilmiyorum. Ne cevap vermeliyim?")
        cevap = st.text_input("Cevabı buraya yaz:")
        if st.button("Öğret"):
            hafizaya_kaydet(soru, cevap)
            st.success("Nika bunu artık unutmayacak!")
    
