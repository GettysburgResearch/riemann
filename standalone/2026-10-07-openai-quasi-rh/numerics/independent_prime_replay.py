# Independent check: for primary split primes pi=a+b*omega (a≡1,b≡0 mod 3), N(pi)=p≡1 mod 3,
# Independent second implementation (written separately from eisenstein.py) of the prime case of Lemma lem:arithmetic.
# gamma_j(pi) = p^{-1/2} sum_{x mod p} chi(x)^j e(x/pi), chi = sextic residue symbol, e(z)=exp(4πi Im z/√3).
# Check gamma_2^3 = -alpha(pi) and gamma_1*gamma_2 = -alpha*G with G = conj(chi(4))*gamma_3.
import cmath, math
w = complex(-0.5, math.sqrt(3)/2)
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**.5)+1))
worst = [0, 0]; count = 0
for p in range(7, 3000):
    if not isprime(p) or p % 3 != 1: continue
    # find primary pi = a + b w with norm p
    found = None
    for b in range(-60, 61, 3):
        for a in range(-60, 61):
            if a % 3 == 1 and a*a - a*b + b*b == p: found = (a, b); break
        if found: break
    a, b = found
    pi = a + b*w
    r = (-a * pow(b, -1, p)) % p          # omega -> r mod pi
    z6 = (-r*r) % p                        # image of e^{i pi/3} = -omega^2
    pw = {pow(z6, k, p): k for k in range(6)}
    def chi(x):
        x %= p
        return 0 if x == 0 else cmath.exp(1j*math.pi*pw[pow(x, (p-1)//6, p)]/3)
    def e(z): return cmath.exp(4j*math.pi*z.imag/math.sqrt(3))
    def gam(j): return sum((chi(x)**j if chi(x) != 0 else 0) * e(x/pi) for x in range(1, p)) / math.sqrt(p)
    g1, g2, g3 = gam(1), gam(2), gam(3)
    alpha = pi/abs(pi)
    G = chi(4).conjugate()*g3
    worst[0] = max(worst[0], abs(g2**3 + alpha))
    worst[1] = max(worst[1], abs(g1*g2 + alpha*G))
    count += 1
print(f"{count} primary split primes p<3000: max|γ2^3+α|={worst[0]:.2e}, max|γ1γ2+αG|={worst[1]:.2e}")
