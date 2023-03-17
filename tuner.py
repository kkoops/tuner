import pyaudio
import numpy as np

p = pyaudio.PyAudio()

RATE = 44100  
CHUNK = int(RATE * 0.25 / 4)

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("start!!")

while True:
    data = stream.read(CHUNK)
    x = np.frombuffer(data, dtype="int16") / 32768.0
    freq_list = np.fft.fftfreq(len(x), d=1.0/RATE)
    y = np.fft.fft(x)
    amplitude = np.abs(y)
    index = np.argmax(amplitude)
    freq = freq_list[index]
    print("Frequency: {:.2f} Hz".format(freq))

stream.stop_stream()
stream.close()
p.terminate()
