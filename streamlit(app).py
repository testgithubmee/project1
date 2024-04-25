import streamlit as st
import time as t

#title- it is used to add the title of an app
st.title("Welcome to intellipath")
#header
st.header("Machine Learning")
#sub header
st.subheader("lINEAR REGRESSION")

#information
st.info("information details of a user")

#warning message

st.warning("Come on time")

#error mesage
st.error("wrong")


#success message
st.success("congratulations!")


#write
st.write("Employee name")
st.write(range(50))

#markdown
st.markdown("# intellipath")
st.markdown("## intellipath")
st.markdown("### intellipath")
st.markdown("intellipath")
st.markdown(":moon:")
st.markdown(":sun:")

#text
st.text("intellipath learners")

#caption
st.caption("here")

#o display mathematical function
st.latex(r'''a+b x^2+c''')
st.latex(r'''a^2+b^2+2ab''')

#widget
#checkbox
st.checkbox("login")

#button
st.button("click")

#radio widget

st.radio("pick your gender",["Male","Female","Others"])

#select box
st.selectbox("pick your course",["Al","Ml","cyber security"])

#multiselect
st.multiselect("choose the dept",["hr","sales","marketing","software","electronics"])

#selectslider
st.select_slider("rating",["bad","good","o/s"])

#slider
st.slider("enter ur number",0,30)
st.slider("enter ur number",0,100)

#number_input
st.number_input("enter your number",0,100)

#text_input
st.text_input("enter gmail address")

#date input
st.date_input("openeing ceremony")

#time input
st.time_input("what is the timing")

#text area
st.text_area("welcome to intellipath")


#for uploading file
st.file_uploader("upload your file")

#for choosing color
st.color_picker("color")

st.progress(90)

#spinner 
with st.spinner("just wait"):
    t.sleep(10)

#balloon
st.balloons()

#sidebar
st.sidebar.title("wlcome to intellipath")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio("professional expert",["Student","working","others"])



#data visalization

#import
import pandas as pd
import seaborn as sns
import numpy as np
st.title("Bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["X","Y"])
st.bar_chart(data)


st.title("line chart")
st.line_chart(data)


st.title("area chart")
st.area_chart(data)

import pandas as pd
import seaborn as sns
import numpy as np

#loading dataset

uploading=st.file_uploader("upload file in csv format")
if uploading is not None:
    data=pd.read_csv(uploading)

#show dataset

if uploading is not None:
    if st.checkbox("preview dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())


#check datatype of each column

if uploading is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Datatypes")
        st.write(data.dtypes)



#find shape of dataset

if uploading is not None:
    data_shape=st.radio("what dimenson do you want to check?",('rows','columns'))

    if data_shape=='rows':
        st.text("Number of rows")
        st.write(data.shape[0])
    if data_shape=='columns':
        st.text("Number of columns")
        st.write(data.shape[1])


#find null values in dataset

if uploading is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("congrats,no missing values")


#find duplicatews values in dataset
if uploading is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("this dataset contains some duplicate values")
        dup=st.selectbox("do u want to remove duplicate values?",\
                         ("Select one","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("duplicate values are removed")
        if dup=="No":
            st.text("ok,no problem")   

#overall statistics
if uploading is not None:
    if st.checkbox("summary of dataset"):
        st.write(data.describe(include="all"))

#about section
if st.button("ABOUT APP"):
    st.text("built with streamlit")
    st.text("thanks to streamlit")

#by
if st.checkbox("by"):
    st.success("meenu aggarwal")