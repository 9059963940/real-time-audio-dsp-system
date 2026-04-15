import numpy as np

def spectral_subtraction(signal, fs=44100):
    fft = np.fft.fft(signal)
    magnitude = np.abs(fft)
    phase = np.angle(fft)

    noise_estimate = np.mean(magnitude[:100])
    cleaned_magnitude = magnitude - noise_estimate
    cleaned_magnitude = np.maximum(cleaned_magnitude, 0)

    cleaned_fft = cleaned_magnitude * np.exp(1j * phase)
    cleaned_signal = np.fft.ifft(cleaned_fft)

    return np.real(cleaned_signal)
