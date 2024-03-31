import streamlit as st
def foo(a,b):
    return a+b
st.title("add")
a=st.number_input("input a")
b=st.number_input("input b")




answer =foo(a,b)
st.write(answer)
