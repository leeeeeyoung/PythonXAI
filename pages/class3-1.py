import streamlit as st

st.title("點餐機")

ss = st.session_state

if "orders" not in ss:
    ss.orders = []

col1, col2 = st.columns([9, 1])
foodInput = col1.text_input("請輸入餐點")
if col2.button("加入"):
    ss.orders.append(foodInput)
    st.rerun()

st.write("### 購物籃")
for i in range(len(ss.orders)):
    col3, col4 = st.columns([9, 1])
    col3.write(ss.orders[i])
    if col4.button("刪除", key=f"delete_{i}"):
        ss.orders.pop(i)
        st.rerun()
