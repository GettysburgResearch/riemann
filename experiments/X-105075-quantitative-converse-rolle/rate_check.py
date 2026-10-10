# B1 rate_check.py — machine verification of every constant in the quantified chain.
# (1) Conrey 1983 I (JNT 16, 49-74) asymptotic corollary, R=1, phi(x)=1-x:
#     psi_m(x) = (1-x)(1-2x)^m,  Phi = int_0^1 e^{2x} psi_m^2,  Phi' = int e^{2x} psi_m'^2,
#     Lambda^2 = (Phi' - 1 - Phi)/(4 Phi),  F_m(1) = 1/2 + 2 Phi Lambda coth Lambda,
#     alpha_m >= 1 - log F_m(1).   Paper claims log F_m(1) <= m^{-2} (large m).
# (2) Master-chain numerics: S_K, theta_0, fixed point, Sum w_k, divergence profile.
import mpmath as mp
mp.mp.dps = 40

def conrey_F(m):
    psi  = lambda x: (1-x)*(1-2*x)**m
    dpsi = lambda x: -(1-2*x)**(m-1)*((2*m+1)-(2*m+2)*x)
    Phi  = mp.quad(lambda x: mp.e**(2*x)*psi(x)**2,  [0, mp.mpf(1)/2, 1])
    Phip = mp.quad(lambda x: mp.e**(2*x)*dpsi(x)**2, [0, mp.mpf(1)/2, 1])
    Lam2 = (Phip - 1 - Phi)/(4*Phi)
    Lam  = mp.sqrt(Lam2)
    F    = mp.mpf(1)/2 + 2*Phi*Lam*mp.coth(Lam)
    return Phi, Phip, F, mp.log(F)

print("== (1) Conrey I asymptotic corollary: m^2 * log F_m(1) ==")
for m in [2, 5, 10, 20, 50, 100, 200, 500, 1000]:
    Phi, Phip, F, lf = conrey_F(m)
    print(f"m={m:5d}  logF={mp.nstr(lf,8):>12}  m^2*logF={mp.nstr(m**2*lf,8):>12}  "
          f"1-logF={mp.nstr(1-lf,8)}")

# (2) chain constants
Z23 = mp.mpf('0.6725007036794117')          # = 3/2 - (1/sqrt2)*cot(1/sqrt2), Z23-UPSTREAM
closed = mp.mpf(3)/2 - mp.cot(1/mp.sqrt(2))/mp.sqrt(2)
print("\nZ23 closed form check:", mp.nstr(closed, 17), " matches:", abs(closed-Z23) < mp.mpf('1e-15'))

alpha = {0: mp.mpf('0.3658'), 1: mp.mpf('0.8137'), 2: mp.mpf('0.9584'),
         3: mp.mpf('0.9873'), 4: mp.mpf('0.9948'), 5: mp.mpf('0.9970')}  # Conrey I Corollary
c = {k: max(Z23, alpha[k]) for k in alpha}   # best available per-rung kappa lower bound
def Ap(k): return max(6, 2*k)                # deposited regime-wise cap (L-105063)

print("\n== (2a) Master chain S_K = sum_{k<=K} A'_k (3/(2 c_k)) (1-c_k); bound_K = S_K + (1-c_{K+1}) ==")
S = mp.mpf(0)
for K in range(0, 5):
    term = Ap(K) * (3/(2*c[K])) * (1-c[K])
    S += term
    bound = S + (1 - c[K+1])
    print(f"K={K}  term_k={mp.nstr(term,6):>10}  S_K={mp.nstr(S,6):>10}  bound_K={mp.nstr(bound,6):>10}")
term5 = Ap(5)*(3/(2*c[5]))*(1-c[5]); S += term5
print(f"K=5  term_k={mp.nstr(term5,6)}  S_5={mp.nstr(S,6)}  (bound needs c_6: only 1-alpha_6<=1/36 asymptotic)")

print("\n== (2b) rung-0 self-reference: theta_0 = 3 A'_0 / (2 c_0) ==")
for A0, lab in [(6,'proved A=6'), (2,'conjectured sharp A=2'), (mp.mpf(16)/15,'forced-minimal A=16/15')]:
    for c0, lc in [(Z23,'c0=Z23'), (mp.mpf(1),'c0=1 (best conceivable)')]:
        th = 3*A0/(2*c0)
        print(f"  {lab:24s} {lc:24s} theta_0={mp.nstr(th,6):>9}  closes(<1)? {th<1}")
print("  needed for closure: A'_0 < 2 c_0/3 =", mp.nstr(2*Z23/3, 6))

print("\n== (2c) irreducible floor: k=1 term with ALL sharpest deposited constants ==")
# minimal count-cap constant forced by L-105063 extremal: A' >= 16/15; pointwise C_omega = 3 sharp
t1min = (mp.mpf(16)/15) * (3/(2*alpha[1])) * (1-alpha[1])
print("  (16/15)*(3/(2*0.8137))*(1-0.8137) =", mp.nstr(t1min, 6), " > 0.3275?", t1min > mp.mpf('0.3275'))
print("  required c_1 for this single term to beat 0.3275: (1-c1)/c1 < 0.3275/1.6 ->  c1 >",
      mp.nstr(1/(1+mp.mpf('0.3275')/mp.mpf('1.6')), 6))

print("\n== (2d) Sum w_k bound (W6 with c=Z23 all rungs, Conrey tail 1/k^2 for k>=6) ==")
head = sum((1-c[k]) for k in range(6))
tail = mp.zeta(2) - sum(mp.mpf(1)/k**2 for k in range(1, 6))   # sum_{k>=6} 1/k^2
wsum = (3/(2*Z23)) * (head + tail)
print("  head Sum_{k<=5}(1-c_k) =", mp.nstr(head, 6), "  tail Sum_{k>=6}1/k^2 =", mp.nstr(tail, 6))
print("  Sum w_k <= (3/(2*0.6725))*(head + C_Conrey*tail) =", mp.nstr(wsum, 6), " (at C_Conrey=1)")

print("\n== (2e) divergence profile of the master majorant with 1-kappa_k = C/k^2, A'_k=2k ==")
for K in [10, 100, 1000, 10**4]:
    s = sum(2*k*(3/(2*Z23))*(mp.mpf(1)/k**2) for k in range(6, K+1))
    print(f"  Sum_(6<=k<=K) 2k*(3/2c)/k^2 at K={K:6d}: {mp.nstr(s,6)}  (~ (3/c) log K = "
          f"{mp.nstr((3/Z23)*mp.log(K),6)})")
print("  => harmonic divergence: bound_K -> infinity; best bound is at FINITE K (2a).")

print("\n== (2f) convergence threshold: Sum 2k * C/k^rho < inf  iff  rho > 2 ==")
for rho in ['2', '2.0001', '2.1', '3']:
    r = mp.mpf(rho)
    conv = r > 2
    val = (mp.zeta(r-1) - sum(mp.mpf(1)/k**(r-1) for k in range(1,6))) if conv else mp.inf
    print(f"  rho={rho}: Sum_(k>=6) k^(1-rho) = {mp.nstr(val,6) if conv else 'DIVERGES'}")

print("\n== (2g) end-to-end bound at K=0 under constant variants (1-k0 <= (1-c1) + A'*(3/(2c0))*(1-c0)) ==")
a1 = alpha[1]
for A0, lab in [(6,"proved A'=6"), (2,"conjectured sharp A'=2"), (mp.mpf(16)/15,"forced floor A'=16/15")]:
    for c0, lc in [(Z23,'c0=Z23=0.6725'), (alpha[0],'c0=Conrey 0.3658 (import-free)')]:
        b = (1-a1) + A0*(3/(2*c0))*(1-c0)
        print(f"  {lab:22s} {lc:30s} bound={mp.nstr(b,6):>9}  vs trivial 1-c0={mp.nstr(1-c0,5)}  vacuous? {b > 1-c0}")
