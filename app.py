
import streamlit as st

st.title("Kalkulator Keuangan UMKM")
st.write("Hitung omzet, biaya, dan laba usahamu.")

st.header("Masukkan Data Bisnis")

jumlah_produk = st.number_input(
    "Jumlah produk terjual",
    min_value=0,
    value=10
)

harga_jual = st.number_input(
    "Harga jual per produk (Rp)",
    min_value=0,
    value=15000,
    step=1000
)

biaya = st.number_input(
    "Total biaya usaha (Rp)",
    min_value=0,
    value=80000,
    step=5000
)

omzet = jumlah_produk * harga_jual
laba = omzet - biaya

st.subheader("Hasil Perhitungan")

st.metric("Total Omzet", f"Rp{omzet:,.0f}")
st.metric("Total Biaya", f"Rp{biaya:,.0f}")
st.metric("Laba / Rugi", f"Rp{laba:,.0f}")

if laba > 0:
    st.success("Usaha memperoleh laba.")
elif laba < 0:
    st.error("Usaha mengalami kerugian.")
else:
    st.info("Pendapatan sama dengan biaya.")
