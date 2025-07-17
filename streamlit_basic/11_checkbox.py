# -*- coding: utf-8 -*-
# 파일명 : 11_checkbox.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Check Box Control")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox("시각화 보여주기")

    fig, ax = plt.subplots()
    ax.plot(x, y)

    if show_plot: # 체크박스 클릭이 된 상태에서는 시각화 보여주기
        st.pyplot(fig)

if __name__ == '__main__':
    main()