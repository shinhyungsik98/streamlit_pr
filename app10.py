#스트림릿의 내장 차트 함수와 유명한 라이브러리인 plotly 차트

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main() :
    #스트림릿에서 제공해주는 차트
    #line_chart, area_chart

    df1 = pd.read_csv('./data/lang_data.csv')
    print(df1)

    print(df1.columns[1:])

    columns_list = df1.columns[1:]

    choice_list = st.multiselect('언어를 선택하세요.', columns_list)

    print(choice_list)

    if len(choice_list) !=0 :
        df_choice=df1[choice_list]

        st.dataframe(df_choice)

        st.line_chart(df_choice)
        st.area_chart(df_choice)

    df3 = pd.read_csv('./data/location.csv', index_col=0)
    print(df3)

    st.map(df3)

    df4=pd.read_csv('./data/prog_languages_data.csv')
    print(df4) 

if __name__== '__main__':
    main()
