import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

st.title("🎧 Real-Time Audio Noise Reduction")

# Recording settings
duration = st.slider("Recording Duration (seconds)", 1, 10, 3)
sample_rate = 44100

if st.button("🎤 Record Audio"):
    st.write("Recording...")

    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    st.success("Recording Complete!")

    audio = audio.flatten()

    st.subheader("Original Signal")
    st.line_chart(audio)

    # FFT
    fft = np.fft.fft(audio)
    freq = np.fft.fftfreq(len(audio), 1/sample_rate)

    # Noise filtering
    cutoff = 4000
    fft[np.abs(freq) > cutoff] = 0
    filtered = np.fft.ifft(fft)

    filtered = np.real(filtered)

    st.subheader("Filtered Signal")
    st.line_chart(filtered)

    sf.write("output.wav", filtered, sample_rate)

    st.success("Noise Reduction Complete! Check output.wav")
