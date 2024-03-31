import streamlit as st
def foo(a):
    #return a+b
    return ("hello  ",a)
st.title("Hello")
a=st.text_input("input your name")
#b=st.number_input("input b")



answer =foo(a)
#answer =foo(a,b)
st.write(answer)
