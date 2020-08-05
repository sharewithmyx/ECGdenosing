# ECGdenosing
# baselineRemoval.py : This file removes the baseline drift of ECG signals;
# notchFilter.py     : This file uses 50Hz notch filter to filter ECG signal, so as to remove power frequency interference;
# heart1.xlsx        : This file saves the ECG data of a group of normal people in MIT-BIH database, which is used as the input of notchFilter.py file;
# heart1_filtered.npy: This file is the output of notchFilter.py file, which represents the ECG signal filtered by 50Hz notch filter and is used as the
#                      input of baselineRemoval.py file;
# @Created on Wed Aug 5 2020;
# @author: Meng yuxuan, Sichuan University;
