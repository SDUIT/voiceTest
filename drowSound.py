import sys
import wave
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

def format_time(x, pos=None):
    global duration, nframes, k
    progress = int(x / float(nframes) * duration * k)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out

def format_db(x, pos=None):
    if pos == 0:
        return ""
    if x == 0:
        return "-inf"

    db = 20 * math.log10(abs(x) / float(peak))
    return int(db)

def drow(x, y):
    soundAddr = x
    imageAddr = y

    global wav, nchannels, sampwidth, framerate, nframes, comptype, compname, duration, w, h, k, DPI, peak

    wav = wave.open(soundAddr, mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

    if nframes == 0 :
        return False

    else :
        
        duration = nframes / framerate
        w, h = 1500, 400
        k = nframes/w/32
        DPI = 72
        peak = 256 ** sampwidth / 2

        content = wav.readframes(nframes)
        samples = np.fromstring(content, dtype=types[sampwidth])

        plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)
        plt.subplots_adjust(wspace=5, hspace=0)
        
        for n in range(nchannels):
            channel = samples[n::nchannels]

            channel = channel[0::k]
            if nchannels == 1:
                channel = channel - peak   

            #axes = plt.subplot(1, 1, n+1, axisbg="k")
            try :
                axes = plt.subplot(1, 1, n+1, axisbg="k" )    
                axes.plot(channel, "g")
                axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
                plt.grid(True, color="w")
                axes.xaxis.set_major_formatter(ticker.NullFormatter())
            except :
                try :
                    axes = plt.subplot(2, 1, n+1, axisbg="k" )    
                    axes.plot(channel, "g")
                    axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
                    plt.grid(True, color="w")
                    axes.xaxis.set_major_formatter(ticker.NullFormatter())
                except :            
                    return False
        axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
        plt.savefig(imageAddr, dpi=DPI)

        return True
        
wav=None,
nchannels=None,
sampwidth=None,
framerate=None,
nframes=None,
comptype=None,
compname=None,
duration=None,
w=None,
h=None,
k=None,
DPI=None,
peak=None

