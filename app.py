import streamlit as st
def foo(a):
    #return a+b
    a=max(a)
    return ("Max is  "+a)
st.title("MaxOfThree")
#a=st.text_input("input your name")

l=st.number_input("input 3 comma seperated numbers")
#b2=st.number_input("input b")
#b3=st.number_input("input b")



#answer =foo(a)
#answer =foo(a,b)
st.write(foo(l))
