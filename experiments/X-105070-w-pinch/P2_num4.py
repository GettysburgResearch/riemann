import numpy as np
from math import log, pi
Vg = np.load('Vg.npy'); xg = np.load('xg.npy'); dx = xg[1]-xg[0]
g13 = 14.134725141734695/3
for h in (0.05, 0.02, 0.01):
    ph = Vg*np.exp(-h*xg)
    NP = 2**24
    F = np.fft.fft(ph, NP)*dx
    freq = np.fft.fftfreq(NP, d=dx)*2*pi
    band = (freq>3.5)&(freq<6.0)
    fb, ab = freq[band], np.abs(F[band])**2
    pk = fb[np.argmax(ab)]
    # compare profile with saturated-pole model |c|^2/((h+1/lnXc)^2+(t-t0)^2)? report peak+widths
    print(f"h={h}: peak |G|^2 at t={pk:.4f} (pred {g13:.4f}), peak val={ab.max():.5f}")
    for w in (0.05,0.1,0.2,0.4,0.8):
        m = (np.abs(fb-g13)<=w)
        print(f"   mass in +-{w}: {np.sum(ab[m])*(fb[1]-fb[0]):.5f}")
# also unweighted (no sqrt log) comparison: raw half-singularity should be WEAKER
import math
Vg0 = Vg/np.sqrt((2/3)*xg)  # divide out sqrt((2/3)logX)
for h in (0.01,):
    for (nm,vv) in (("weighted",Vg),("raw",Vg0)):
        ph = vv*np.exp(-h*xg); F = np.fft.fft(ph, 2**24)*dx
        freq = np.fft.fftfreq(2**24, d=dx)*2*pi
        band=(np.abs(freq-g13)<=0.15); m2=np.sum(np.abs(F[band])**2)*(freq[1]-freq[0])
        ctrl=(freq>=7)&(freq<=8); c2=np.sum(np.abs(F[ctrl])**2)*(freq[1]-freq[0])
        print(f"h={h} {nm}: win(+-0.15)={m2:.5f} ctrl[7,8]={c2:.5f} ratio={m2/ c2:.2f}")
