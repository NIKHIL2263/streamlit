import streamlit as st
def foo(a,b,c):
    #return a+b
    a=max(a,b,c)
    return ("Max is  "+a)
st.title("MaxOfThree")
#a=st.text_input("input your name")

b1=st.number_input("input b")
b2=st.number_input("input b")
b3=st.number_input("input b")



#answer =foo(a)
#answer =foo(a,b)
st.write(foo(b1,b2,b3))
