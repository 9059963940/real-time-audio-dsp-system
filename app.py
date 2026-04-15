import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

st.title("🎧 Real-Time Audio Noise Reduction")

uploaded_file = st.file_uploader("Upload Audio File (.wav)", type=["wav"])

if uploaded_file is not None:
    data, sr = sf.read(uploaded_file)

    st.subheader("Original Signal")
    st.line_chart(data)

    # FFT
    fft = np.fft.fft(data)
    freq = np.fft.fftfreq(len(data), 1/sr)

    # Noise filtering
    cutoff = 4000
    fft[np.abs(freq) > cutoff] = 0
    filtered = np.fft.ifft(fft)

    st.subheader("Filtered Signal")
    st.line_chart(np.real(filtered))

    sf.write("output.wav", np.real(filtered), sr)

    st.success("Noise Reduction Complete! Check output.wav")
