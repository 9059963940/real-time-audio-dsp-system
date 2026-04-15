from audio_io import record_audio
from noise_filter import spectral_subtraction

def process_realtime():
    signal, fs = record_audio()
    filtered = spectral_subtraction(signal, fs)
    return signal, filtered, fs
