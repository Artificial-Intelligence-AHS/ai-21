import matplotlib.pyplot as plt
from scipy.io import wavfile

# import the libraries
local_file_path = './PROJECTS/voice_recognition/audioFiles/3.wav'

# Read the wav file (mono)
samplingFrequency, signalData = wavfile.read(local_file_path)
print(samplingFrequency)

signalDataNormalized = []
for i in signalData:
    if abs(i) > 2000:
        signalDataNormalized.append(i)
    else:
        signalDataNormalized.append(0) 


# Plot only spectogram

plt.plot(signalData)
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.axvline(x=29700, color='r', linestyle='--')

plt.axhline(y=2000, color='r', linestyle='-')
plt.axhline(y=-2000, color='r', linestyle='-')

plt.show()

#print(signalData)

plt.plot(signalDataNormalized)
plt.xlabel('Sample')
plt.ylabel('Amplitude')

thresholdLine = 2000

plt.axhline(y=thresholdLine, color='r', linestyle='-')
plt.axhline(y=-1*thresholdLine, color='r', linestyle='-')

speakingPos = [[3494, 6046], [10790, 13040], [18411, 20846], [26346, 28459], [33049, 37083], [43194, 45725], [52712, 55070], [61311, 62899], [69324, 71930], [77853, 80284], [101162, 102992], [108013, 110760], [112084, 113405], [114663, 127054]]
for i in speakingPos:
    plt.axvline(x=i[0], color='blue', linestyle='-.')
    plt.axvline(x=i[1], color='green', linestyle='-.')
plt.show()



plt.show()

#print(signalData)



# OTHER CODE
"""
sample_rate, samples = wavfile.read(local_file_path)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
"""
"""
import librosa
import librosa.display
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
local_file_path = '/Users/kunal/Documents/AI-21/ai-21/PROJECTS/voice_recognition/audioFiles/3.mp3'

def plot_mp3_matplot(filename):
    
    plot_mp3_matplot -- using matplotlib to simply plot time vs amplitude waveplot
    
    Arguments:
    filename -- filepath to the file that you want to see the waveplot for
    
    Returns -- None
    
    
    # sr is for 'sampling rate'
    # Feel free to adjust it
    x, sr = librosa.load(filename, sr=44100)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)

def convert_audio_to_spectogram(filename):
    
    convert_audio_to_spectogram -- using librosa to simply plot a spectogram
    
    Arguments:
    filename -- filepath to the file that you want to see the waveplot for
    
    Returns -- None
    
    
    # sr == sampling rate 
    x, sr = librosa.load(filename, sr=44100)
    
    # stft is short time fourier transform
    X = librosa.stft(x)
    
    # convert the slices to amplitude
    Xdb = librosa.amplitude_to_db(abs(X))
    
    # ... and plot, magic!
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
    plt.colorbar()
    
# same as above, just changed the y_axis from hz to log in the display func    
def convert_audio_to_spectogram_log(filename):
    x, sr = librosa.load(filename, sr=44100)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'log')
    plt.colorbar()   

plot_mp3_matplot(local_file_path)
"""
