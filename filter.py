import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# fs_Hz = 128

# # create the 50 Hz filter
# bp_stop_50_hz = np.array([45.0, 55.0]) # 49.0, 51.0
# b50, a50 = signal.butter(2, bp_stop_50_hz / (fs_Hz / 2.0), 'bandstop')

# print("50Hz b: " , b50)
# print("50Hz a: " , a50)

# # create the 60 Hz filter
# bp_stop_60_hz = np.array([59.0, 61.0])
# b60, a60 = signal.butter(2, bp_stop_60_hz / (fs_Hz / 2.0), 'bandstop')

# print("60Hz b: " , b60)
# print("60Hz a: " , a60)

# # create the 1-50Hz
# bp_50_hz = np.array([1, 50])
# b_50_bp = signal.butter(2, bp_50_hz / (fs_Hz / 2.0), 'band')

# # compute the frequency response
# w50, h50 = signal.freqz(b50, a50, 1000)
# w60, h60 = signal.freqz(b60, a60, 1000)

# # convert from rad/sample to hz
# f = w60 * fs_Hz / (2 * np.pi) 

# # 60 Hz Notch for fs 128 Hz

def butter_bandpass_normal(lowcut, highcut, fs, order=2):
    # b,a]=butter(2,[15 50]/(250/2)); %matlab command
    b, a = signal.butter(order, np.array([lowcut, highcut]) / (fs / 2.0), btype='band')
    print("Normal BandPass {0}-{1}Hz b: {2}".format(lowcut, highcut, b))
    print("Normal BandPass {0}-{1}Hz a: {2}".format(lowcut, highcut, a))

def butter_bandpass(lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    print("BandPass {0}-{1}Hz b: {2}".format(lowcut, highcut, b))
    print("BandPass {0}-{1}Hz a: {2}".format(lowcut, highcut, a))
    #return b, a

def butter_bandstop_normal(lowcut, highcut, fs, order=2):
    #  b, a = signal.butter(2,[49.0 51.0]/(fs_Hz / 2.0), 'bandstop')
    b, a = signal.butter(order, np.array([lowcut, highcut]) / (fs / 2.0), 'bandstop')
    print("Normal BandStop {0}-{1}Hz b: {2}".format(lowcut, highcut, b))
    print("Normal BandStop {0}-{1}Hz a: {2}".format(lowcut, highcut, a))

def butter_bandstop(lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = signal.butter(order, [low, high], btype='bandstop')
    #y = lfilter(i, u, data)
    #return b, a
    print("BandStop {0}-{1}Hz b: {2}".format(lowcut, highcut, b))
    print("BandStop {0}-{1}Hz a: {2}".format(lowcut, highcut, a))

def notch(fs, lowcut, highcut, f0):
    Q = (highcut - lowcut) / f0
    b, a = signal.iirnotch(f0, Q, fs)
    print("Notch {0}-{1}Hz b: {2}".format(lowcut, highcut, b))
    print("Notch {0}-{1}Hz a: {2}".format(lowcut, highcut, a))

def butter_highpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high')
    print("HighPass {0}Hz b: {1}".format(cutoff, b))
    print("HighPass {0}Hz a: {1}".format(cutoff, a))

if __name__ == "__main__":
    fs_Hz = 128

    butter_bandstop_normal(49.0, 51.0, fs_Hz, 2) # 50 Hz
    butter_bandstop_normal(48.0, 52.0, fs_Hz, 2)
    butter_bandstop_normal(47.0, 53.0, fs_Hz, 2)
    butter_bandstop_normal(46.0, 54.0, fs_Hz, 2)
    butter_bandstop_normal(59.0, 61.0, fs_Hz, 2) # 60 Hz

    butter_bandstop(49.0, 51.0, fs_Hz, 2)
    butter_bandstop(48.0, 52.0, fs_Hz, 2)
    butter_bandstop(47.0, 53.0, fs_Hz, 2)
    butter_bandstop(46.0, 54.0, fs_Hz, 2)
    butter_bandstop(59.0, 61.0, fs_Hz, 2)

    notch(fs_Hz, 49.0, 51.0, 50.0)
    notch(fs_Hz, 48.0, 52.0, 50.0)
    notch(fs_Hz, 47.0, 53.0, 50.0)
    notch(fs_Hz, 46.0, 54.0, 50.0)
    notch(fs_Hz, 59.0, 61.0, 60.0)

    butter_bandpass_normal(5.0, 50, fs_Hz, 2)
    butter_bandpass_normal(7.0, 13.0, fs_Hz, 2)
    butter_bandpass_normal(15.0, 50.0, fs_Hz, 2)
    butter_bandpass_normal(1.0, 50.0, fs_Hz, 2)
    #butter_bandpass_normal(1.0, 100.0, fs_Hz, 2)

    butter_bandpass(5.0, 50, fs_Hz, 2)
    butter_bandpass(7.0, 13.0, fs_Hz, 2)
    butter_bandpass(15.0, 50.0, fs_Hz, 2)
    butter_bandpass(1.0, 50.0, fs_Hz, 2)
    #butter_bandpass(1.0, 100.0, fs_Hz, 2)

    butter_highpass(50, fs_Hz, 2)