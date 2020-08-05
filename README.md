# ECGdenosing
baselineRemoval.py : This file removes the baseline drift of ECG signals;/n
notchFilter.py     : This file uses 50Hz notch filter to filter ECG signal, so as to remove power frequency interference/n
heart1.xlsx        : This file saves the ECG data of a group of normal people in MIT-BIH database, which is used as the input of notchFilter.py file/n
heart1_filtered.npy: This file is the output of notchFilter.py file, which represents the ECG signal filtered by 50Hz notch filter and is used as the/n
                     input of baselineRemoval.py file/n
@Created on Wed Aug 5 2020/n
@author: Meng yuxuan, Sichuan University/n
