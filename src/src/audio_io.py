import sounddevice as sd
import soundfile as sf

def record_audio(duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording complete")
    return audio.flatten(), fs

def save_audio(file_path, data, samplerate):
    sf.write(file_path, data, samplerate)
