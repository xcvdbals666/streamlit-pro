# -*- coding: utf-8 -*-
# 파일명 : 04_data_display_dataframe.py

import streamlit as st 
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')

    iris = load_data()
    st.dataframe(iris, use_container_width = True)

    # pandas style
    st.dataframe(iris.iloc[140:145, 0:4].style.highlight_max(axis=1))


if __name__ == "__main__":
    main()
