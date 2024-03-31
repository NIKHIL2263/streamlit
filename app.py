import streamlit as st
def foo(a,b):
    return a+b
st.title("add")
a=st.number_input()
b=st.number_input()

st.write(foo(a,b))
