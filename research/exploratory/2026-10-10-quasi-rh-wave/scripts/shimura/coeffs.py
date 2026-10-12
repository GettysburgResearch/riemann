"""Compute r_3(N) for N<=R3MAX (FFT convolution) and Hurwitz H(N) for N<=HMAX
(direct enumeration of reduced forms, weighted 1/|Aut|*2). Cross-check the
classical relations r_3(N)=12H(4N) (N=1,2 mod 4), r_3(N)=24H(N) (N=3 mod 8)."""
import numpy as np, time, sys, os
from scipy.fft import rfft, irfft, next_fast_len
OUT = os.path.dirname(os.path.abspath(__file__))
R3MAX = 10**7
HMAX  = 10**6

t0=time.time()
# ---- r_3 via convolution of theta with itself twice ----
L = next_fast_len(2*R3MAX+1, real=True)
theta = np.zeros(L); 
m = np.arange(0, int(np.sqrt(R3MAX))+1)
theta[m*m] = 1.0; theta[m[1:]**2] = 2.0   # theta coefficient: 1 for n=0, 2 for n=k^2>0
T = rfft(theta)
r2 = irfft(T*T, L)[:R3MAX+1]; r2 = np.rint(r2)
r2f = np.zeros(L); r2f[:R3MAX+1]=r2
r3 = irfft(rfft(r2f)*T, L)[:R3MAX+1]
r3err = np.max(np.abs(r3-np.rint(r3))); r3 = np.rint(r3).astype(np.int64)
print("r3 computed up to",R3MAX,"max rounding error",r3err,"time",time.time()-t0)
assert r3[:8].tolist()==[1,6,12,8,6,24,24,0], r3[:8]
np.save(os.path.join(OUT,"r3.npy"), r3)

# ---- Hurwitz class numbers by counting reduced forms (a,b,c), b^2-4ac=-N ----
t0=time.time()
H = np.zeros(HMAX+1)
amax = int(np.sqrt(HMAX/3.0))+1
for a in range(1, amax+1):
    b = np.arange(-a+1, a+1)
    cmax = (HMAX + b*b)//(4*a)
    cnt = np.maximum(cmax - a + 1, 0)
    if cnt.sum()==0: continue
    bb = np.repeat(b, cnt)
    # c runs a..cmax for each b
    starts = np.repeat(cmax - cnt + 1, cnt)   # = a where cnt>0
    idx = np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt)-cnt, cnt)
    cc = starts + idx
    N = 4*a*cc - bb*bb
    w = np.ones(len(N))
    eq = (cc==a)
    w[eq & (bb<0)] = 0.0          # (a,b,a) with b<0 not reduced
    w[eq & (bb==0)] = 0.5         # a(x^2+y^2): |Aut|=4
    w[eq & (bb==a)] = 1.0/3.0     # a(x^2+xy+y^2): |Aut|=6
    # also (a,a,c) with c>a: reduced requires b>=0, i.e. b=-a excluded already (b starts at -a+1). OK
    H += np.bincount(N, weights=w, minlength=HMAX+1)[:HMAX+1]
print("H computed up to",HMAX,"time",time.time()-t0)
print("H(3),H(4),H(7),H(8),H(11),H(12),H(15),H(16),H(19),H(20),H(23),H(24):",
      [round(H[k],4) for k in [3,4,7,8,11,12,15,16,19,20,23,24]])
# expected: 1/3, 1/2, 1, 1, 1, 4/3, 2, 3/2, 1, 2, 3, 2
np.save(os.path.join(OUT,"H.npy"), H)

# ---- cross-checks ----
N = np.arange(1, HMAX//4+1)
m12 = (N%4==1)|(N%4==2)
d1 = np.max(np.abs(r3[N[m12]] - 12*H[4*N[m12]]))
N2 = np.arange(1, HMAX+1); m3 = (N2%8==3)
d2 = np.max(np.abs(r3[N2[m3]] - 24*H[N2[m3]]))
N4 = np.arange(1, R3MAX//4+1)
d3 = np.max(np.abs(r3[4*N4]-r3[N4]))
d4 = np.max(np.abs(r3[N2[N2%8==7]]))
print("max|r3(N)-12H(4N)| (N=1,2 mod 4):",d1)
print("max|r3(N)-24H(N)| (N=3 mod 8):",d2)
print("max|r3(4N)-r3(N)|:",d3, "  max r3(N), N=7 mod 8:",d4)
# H(4N)=(3-chi_D(2))H(N) for N odd = 3 mod 4 -> H(4N)=4H(N) (N=3 mod 8), 2H(N) (N=7 mod 8)
m7 = (N%8==7); m3b=(N%8==3)
print("max|H(4N)-2H(N)| N=7 mod 8:", np.max(np.abs(H[4*N[m7]]-2*H[N[m7]])),
      " max|H(4N)-4H(N)| N=3 mod 8:", np.max(np.abs(H[4*N[m3b]]-4*H[N[m3b]])))
