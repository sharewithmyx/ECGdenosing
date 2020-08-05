import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy.signal import filtfilt, iirnotch, freqz, butter
import matplotlib.pyplot as plt
import xlrd
import xlwt
import numpy as np
"""
Created on Wed Aug 5 16:57 2020
@author: Meng yuxuan, Sichuan University

This file uses 50Hz notch filter to filter ECG signal, 
so as to remove power frequency interference
"""
#Design of 50 Hz notch filter
def filter_50(signal):   
    fs = 500.0           # Sample frequency (Hz)
    f0 = 50              # Frequency to be removed from signal (Hz)
    w0 = f0 / (fs / 2)   # Normalized Frequency
    Q= 30
    b, a = iirnotch(w0, Q)
    signal = filtfilt(b, a, signal)
    return(signal)

#Open excel file, and get the original ECG data
workbook = xlrd.open_workbook('Heart1.xlsx') #Data storage path
print(workbook.sheet_names()) 
sheet2=workbook.sheet_by_name('Sheet1')  
nrows=sheet2.nrows               #Number of rows in sheet
N=nrows
t=[i/500.0 for i in range(nrows)]#Calculate the time series of data points, and 500 is the sampling frequency
ncols=sheet2.ncols          #Column number of sheet
print(nrows,ncols)          #Output number of rows and columns
clou=sheet2.col_values(0)   #Read the contents of the first column
data=clou                   #Data represents the ECG signal used in this example
#Draw the time domain waveform diagram of ECG signal
plt.subplot(221)
plt.plot(t, data, 'b-', label='data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
#Draw the spectrogram of ECG signal
fs=500                #sampling frequency
dataFreqs = np.linspace(0,fs/2,int(N/2)+1) 
dataFFT = np.abs(np.fft.rfft(data)/N)      #fast fourier transform
plt.subplot(222)      #Conventionally, the spectrum of half the sampling frequency is displayed
plt.plot(dataFreqs,dataFFT, label='dataFFT')
plt.xlabel("Freq/Hz")
plt.legend()
plt.grid()

dataFiltered=filter_50(data)   #Using 50Hz filter to remove power frequency interference of ECG signal
np.save('heart1_filtered.npy',dataFiltered) #Write the filtered ECG signal into excel table

#Draw the filtered ECG signal waveform in time domain
plt.subplot(223)
plt.plot(t, dataFiltered, 'b-', label='dataFiltered')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
#spectrogram of filtered ECG signal
dataFilteredFFT = np.abs(np.fft.rfft(dataFiltered)/N)      #fast fourier transform
plt.subplot(224)           
plt.plot(dataFreqs,dataFilteredFFT, label='dataFilteredFFT')
plt.xlabel("Freq/Hz")
plt.legend()
plt.grid()

plt.show()
