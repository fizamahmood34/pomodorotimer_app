import streamlit as st
import time

st.title("Streamlit Pomodoro Timer")

work_timer=st.slider("Work Time (minutes)", 5, 90, 25)
break_timer=st.slider("Break Time", 1, 30, 5)

def pomodoro_timer(work_time, break_time):
    work_seconds= work_time*60
    break_seconds= break_time*60 

    work_placeholder= st.empty()
    break_placeholder= st.empty()

    work_placeholder.write("Work!")
    for i in range(work_seconds):
        work_placeholder.write(f"{work_seconds- i} seconds left")
        
        break_placeholder.write("break!")
        for i in range(break_seconds):
            time.sleep(1)
            break_placeholder.write(f"{break_seconds-i} seconds left")

if st.button("Start Timer"):
 pomodoro_timer(work_timer, break_timer)
