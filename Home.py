import streamlit as st
import pandas as pd


df = pd.read_csv("data.csv", sep=";")


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=300)

with col2:
    st.title("Xinan (Ian) Yang")
    content = """
    Hi, I am Ian, a computing msc graduate and a junior software developer.
    """
    st.info(content)

content2 = """
I have included below some apps I built so far in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


with col3:
    even = df.index[df.index % 2 == 0]
    for index in even:
        row = df.loc[index]
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[View]({row['url1']})")
        st.write(f"[Source Code]({row['url2']})")

with col4:
    odd = df.index[df.index % 2 != 0]
    for index in odd:
        row = df.loc[index]
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[View]({row['url1']})")
        st.write(f"[Source Code]({row['url2']})")
