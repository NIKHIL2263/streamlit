import streamlit as st
def foo(a,b,c):
    #return a+b
    x=max(a,b,c)
    return ("Max is  ",x)
st.title("MaxOfThree")
#a=st.text_input("input your name")

l1=st.number_input("input first number")
l2=st.number_input("input second number")
l3=st.number_input("input third number")
#b2=st.number_input("input b")
#b3=st.number_input("input b")
print(l1,l2,l3)



#answer =foo(a)
#answer =foo(a,b)
st.write(foo(l1,l2,l3))
