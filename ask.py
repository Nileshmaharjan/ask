import matplotlib.pyplot as plt
import numpy as np
from math import pi
import gen_binary as gb

# Carrier information
Fs = 1000 # sampling frequency
fc = 100 # carrier frequency
T = 1 # simulation time
t = np.arange(0, T, 1/Fs)

# Carrier wave
x = np.sin(2*pi*fc*t);

# Generate random binary signal
Td = 0.1 # Bit duration
samples =  int(Td * Fs)
sym = int(np.floor(np.size(t)/samples))

sig = gb.binary(sym, samples)

# plot
plt.subplot(3,1,1)
plt.plot(t, sig)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid()


# Generate ASK
ask = x * sig;

plt.subplot(3,1,2)
plt.plot(t, ask)
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.plot(t, sig)
plt.grid()
plt.tight_layout()


# Noise

noise = np.random.normal(0, 0.1, [1000]);

channel = noise + ask

plt.subplot(3,1,3)
plt.plot(t, channel)
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.plot(t, sig)
plt.grid()
plt.tight_layout()
plt.show()