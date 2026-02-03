import streamlit as st

st.title("數字金字塔")
height = st.number_input(
    "輸入一個整數 (1 ~ 9)", min_value=1, max_value=9, value=5, step=1
)
st.write("數字金字塔:")
for i in range(1, height + 1):
    st.write(str(i) * i)

st.title("箭頭金字塔")
arrow_height = st.number_input("請輸入箭頭的層數", min_value=1, value=5, step=1)
st.write("箭頭金字塔:")
a = ""
for i in range(1, arrow_height + 1):
    a = a + (" " * (arrow_height - i) + "*" * (i * 2 - 1) + "\n")

for i in range(arrow_height):
    a = a + (" " * (arrow_height - 1) + "*" + "\n")
st.write(f"```\n\n{a}```")
