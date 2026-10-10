# Illustration for Theorem A2 (note D): the Robin excess Delta(N) = sigma(N)/N - e^gamma log log N on colossally
# abundant numbers, compared with the RH scale (log N)^{-1/2} and the new unconditional envelope (log N)^{-1/8}(loglog N)^2.
# Ordinary floating point (mpmath, 30 digits); not a certificate.
import mpmath as mp
mp.mp.dps = 30
from sympy import primerange
def ca_number_data(x):
    # CA number with largest prime x: epsilon just below log(1+1/x)/log x; exponents a_p = max k with p^eps <= 1 + 1/(p+...+p^k)
    eps = mp.log(1 + mp.mpf(1)/x)/mp.log(x) * (1 - mp.mpf(10)**-12)
    logN = mp.mpf(0); logI = mp.mpf(0)
    for p in primerange(2, x+1):
        p = mp.mpf(p); k = 0; s = mp.mpf(0)
        while True:
            s += p**(k+1)              # p + p^2 + ... + p^{k+1}
            if p**eps <= 1 + 1/s: k += 1
            else: break
        a = k
        logN += a*mp.log(p)
        logI += mp.log((p**(a+1) - 1)/(p**a*(p-1)))
    return logN, logI
print("x(largest prime)   log N        Delta           Delta*sqrt(logN)   Delta*(logN)^{1/8}/(loglogN)^2")
for x in [97, 997, 9973, 99991, 999983]:
    logN, logI = ca_number_data(x)
    I = mp.e**logI
    Delta = I - mp.e**mp.euler*mp.log(logN)
    print(f"{x:>8}  {mp.nstr(logN,8):>12}  {mp.nstr(Delta,8):>14}  {mp.nstr(Delta*mp.sqrt(logN),8):>16}  {mp.nstr(Delta*logN**(mp.mpf(1)/8)/mp.log(logN)**2,8):>14}")
