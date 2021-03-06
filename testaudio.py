import pyaudio
import wave
import speech_recognition as sr
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test2.wav")
r = sr.Recognizer()

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 48000 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 2 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test2.wav' # name of .wav file


audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

# use the audio file as the audio source

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    print("Sphinx thinks you said " + r.recognize_google(audio, key="API-KEY"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
