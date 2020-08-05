import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import xlrd
import xlwt
import numpy as np
from scipy.signal import medfilt
"""
Created on Wed Aug 5 17:12 2020
@author: Meng yuxuan, Sichuan University

This file removes the baseline drift of ECG signals
"""
def fix_baseline_wander(data, fs=500):
    """BaselineWanderRemovalMedian.m from ecg-kit.  Given a list of amplitude values
    (data) and sample rate (sr), it applies two median filters to data to
    compute the baseline.  The returned result is the original data minus this
    computed baseline.
    """
    #source : https://pypi.python.org/pypi/BaselineWanderRemoval/2017.10.25

    data = np.array(data)
    winsize = int(round(0.2*fs))
    # delayBLR = round((winsize-1)/2)
    if winsize % 2 == 0:
        winsize += 1
    baseline_estimate = medfilt(data, kernel_size=winsize)
    winsize = int(round(0.6*fs))
    # delayBLR = delayBLR + round((winsize-1)/2)
    if winsize % 2 == 0:
        winsize += 1
    baseline_estimate = medfilt(baseline_estimate, kernel_size=winsize)
    ecg_blr = data - baseline_estimate
    return ecg_blr.tolist()

data=np.load('heart1_filtered.npy')
N=data.shape[0]
t=[i/500.0 for i in range(N)]#Calculate the time series of data points, and 500 is the sampling frequency
#Draw the time domain waveform diagram of ECG signal
plt.subplot(221)
plt.plot(t, data, 'b-', label='data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

#Draw the spectrogram of ECG signal
fs=500                    #sampling frequency
dataFreqs = np.linspace(0,fs/2,int(N/2)+1) 
dataFFT = np.abs(np.fft.rfft(data)/N)      #fast fourier transform
plt.subplot(222)          #Conventionally, the spectrum of half the sampling frequency is displayed
plt.plot(dataFreqs,dataFFT, label='dataFFT')
plt.xlabel("Freq/Hz")
plt.legend()
plt.grid()

# Remove baseline drift
dataFiltered=fix_baseline_wander(data, fs=500)
#Draw the filtered ECG signal waveform in time domain
plt.subplot(223)
plt.plot(t, dataFiltered, 'b-', label='dataFiltered')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
#spectrogram of filtered ECG signal
dataFilteredFFT = np.abs(np.fft.rfft(dataFiltered)/N)   #fast fourier transform
plt.subplot(224)   
plt.plot(dataFreqs,dataFilteredFFT, label='dataFilteredFFT')
plt.xlabel("Freq/Hz")
plt.legend()
plt.grid()

plt.show()