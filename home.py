import streamlit as st
import pandas as pd
import plotly

st.set_page_config(page_title = 'home')
st.title("비만 분류 데이터 분석 방법")
st.header("데이터 개요", divider = 'blue')

st.markdown('''
    BMI(체질량지수) 기반의 비만 분류 데이터셋을 분석합니다.
    이 데이터셋은 다양한 특성을 바탕으로 비만 여부를 예측하며, 주요 항목은 아래와 같습니다
    <ul style = "list-style-type: circle; padding-left: 20px;">
        <li><strong>Age</strong>: 나이</li>
        <li><strong>Gender</strong>: 성별(Male, Female)</li>
        <li><strong>Height</strong>: 키(cm)</li>
        <li><strong>Weight</strong>: 몸무게(Male, Female)</li>
        <li><strong>BMI</strong>: 체질량지수(Male, Female)</li>
        <li><strong>Label</strong>: 비만 여부(Normal Weight, Over Weight, Obese, Under Weight)</li>
    </ul>
''', unsafe_allow_html=True)