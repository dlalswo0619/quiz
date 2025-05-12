import streamlit as st

st.title("간단한 퀴즈풀기!!")

q1 = st.radio("Q1. 광운대학교가 세워진 연도는 몇년도일까요?",
              ("1. 1934", "2. 2010", "3. 1999", "4. 430"))

if st.button("Q1 정답 확인"):
    if q1 == "1. 1934":
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다. 정답은 1934년입니다.")

q2 = st.text_input("Q2. 오픈소스 소프트웨어 수업을 진행하시는 교수님의 성함은 무엇일까요?")

if st.button("Q2 정답 확인"):
    if q2 == "박규동":
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다. 정답은 '박규동'교수님 입니다.")