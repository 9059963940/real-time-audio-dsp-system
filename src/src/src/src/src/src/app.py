import streamlit as st
from realtime import process_realtime

st.title("🎧 Real-Time Audio DSP System")

if st.button("Start Recording"):
    original, filtered, fs = process_realtime()
    
    st.write("Processing complete")
    st.line_chart(original)
    st.line_chart(filtered)
