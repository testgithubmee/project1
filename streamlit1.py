import streamlit as st
#image
st.image("images.png")

import time as t

#titles
st.title("welcome to intellipath page")

#header
st.header("language courses")

#subheader
st.subheader(["python","udemy","django","vbs","vfx"])

#information
st.info("hurry up!,first come first serve")

#error message
st.error("time is out!!")

#success message
st.success("get upto 50% discount on early joining")

#markdown
st.markdown(":sunglasses:")
st.markdown(":moon:")

#text
st.text("limited seats available!!")

#color
st.color_picker("color")


#for mathematical operations
st.latex(r'''a^2+b^2+2ab''')

#balloons
st.balloons()

#widget
st.checkbox("click")

#button
st.button("")

#radio widget
st.radio("choose your courses",["python","udemy","django","vbs","vfx"])

#slider
st.slider("select the number",1,100)


#selectbox
st.selectbox("course fees",[10000,20000,30000,16000,26000])

#multiselect
st.multiselect("choose your course",["python","udemy","django","vbs","vfx"])

#select slider
st.select_slider("rating",["average","good","execellent","o/s"])
st.select_slider("rating",[30,50,70,85,100])


#number input
st.number_input("number1",40)
st.number_input("range(10,100)")
st.number_input("number2,(27,40)")
st.number_input("number3,(27)")

#text input
st.text_input("feedback")

#date input
st.date_input("batch starts from")

#time input
st.time_input("timing starts from")

#spinner
with st.spinner("wait"):
  t.sleep(5)

#imports
import pandas as pd
import numpy as np
import seaborn as sns

#for uploading file
data=st.file_uploader("any format")
if data is not None:
  h1=pd.read_csv(data)


#show dataset
if data is not None:
  if st.checkbox("preview dataset"):
    if st.button("Head"):
        st.write(h1.head())
    if st.button("Tail"):
        st.write(h1.tail())  


#to check datatype of each column?


if data is not None:
   if st.checkbox("Datatypes"):
      st.text("Datatypes")
      st.write(h1.dtypes)

#to show whether dataset has null values or not?

if data is not None:
   h2=h1.isnull().values.any()
   if h2==True:
    if st.checkbox("null values in dataset"):
      sns.heatmap(h1.isnull())
      st.pyplot()

else:
    st.success("ok,no problem!!")


#to show shape of dataset?

if data is not None:
   h3=st.radio("which dimension want to check?",["rows","columns"])
   if h3=='rows':
      st.text("number of rows")
      st.write(h1.shape[0])
   if h3=='columns':
      st.text("number of columns")
      st.write(h1.shape[1])
      

#find duplicates value in dataset?


if data is not None:
   h4=h1.duplicated().any()
   if h4==True:
      st.warning("data has some duplicate values")
      h5=st.selectbox("DO YOU want to remove duplicate values?",\
               ("Select one","Yes","No"))
      if h5=="Yes":
         h5=h1.drop_duplicates() 
         st.text("duplicates values are removed")        
else:
         st.text("no duplicates")



#overall statistics?

if data is not None:
   if st.checkbox("summary of dataset"):
    st.write(h1.describe(include="all"))

#about app

if st.button("about app"):
   st.text("webpage make in python using streamlit")
   st.text("thanx to streamlit")


#by
if st.checkbox("bye"):
  st.success("meenu aggarwal")
   
  







