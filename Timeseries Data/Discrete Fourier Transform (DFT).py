## decompose a given timeseries into a linear combination of sinusoids.
import numpy as np
# numpy implementation of FFT
Xfft = np.fft.fft(x)

x_invfft = np.fft.ifft(Xfft)
# convert the above representation over frequency back to the original representation over time
