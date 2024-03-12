import pygame, random
import pyaudio
import numpy as np
import scipy.fftpack
import time


def get_microphone_frequency():
    CHUNK = 1024  # Number of audio frames per buffer
    RATE = 44100  # Sampling rate (samples per second)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    while True:
        data = stream.read(CHUNK)
        audio_array = np.frombuffer(data, dtype=np.int16)
        frequencies = scipy.fftpack.fftfreq(len(audio_array))
        freq_amplitudes = scipy.fftpack.fft(audio_array)
        dominant_frequency = abs(frequencies[np.argmax(np.abs(freq_amplitudes))])
        time.sleep(0.01)
        return dominant_frequency
        
    stream.stop_stream()
    stream.close()
    p.terminate()
