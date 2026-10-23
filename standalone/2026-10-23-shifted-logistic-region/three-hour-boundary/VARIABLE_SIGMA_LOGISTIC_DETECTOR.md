# A frequency-dependent logistic detector: proposed R=4.813 extension

2026-10-21. This is a separate extension of the degree-12 logistic
detector. It retains the exact rational polynomial, theta=5669/5000,
and all published finite-height, Littlewood and zero-count inputs.
It changes the real part and logistic kernel at each frequency.
Its conclusion requires the analytic interfaces and full parameter
certificate below; a scalar computation alone is not the theorem.
No statement about RH or the separate fixed-width Hecke boundary is made.

## 1. Exact choices and arithmetic positivity

Use the polynomial in LOGISTIC_DEGREE12_PRIME_GAIN.md, with K=12,
a0=1, ak>0, sum_(k>=1)ak<4 and sum_(k>=1)k ak<7. Set

    c=9/8, d=3/25, eta=A/l, delta=d*eta/l,
    sigma_k=1-eta+eta*(c+kd)/l=sigma_0+k delta, k=0..12,
    alpha_k=2sigma_k-1,
    f_k(u)=eta*w(eta*u)/(1+exp(-alpha_k*u)),
    F_k(z)=integral_0^infinity exp(-zu)f_k(u)du.

On the certified rectangle 0<A<=1000/4813, 28<=l<=8241/100,
one has eta<.0075 and .99<sigma_k<1. Each kernel therefore satisfies
the earlier explicit-formula and reflection-positivity lemmas, with
its own alpha_k. Their common value at zero is eta*w0/2.

The combined arithmetic side is

    D=sum_n Lambda(n) sum_(k=0)^12
                  ak n^(-sigma_k)f_k(log n)cos(k t log n).

It is nonnegative term by term. In fact, for u>=0,

    n^(-sigma_k)f_k(u)
      =(eta/2)w(eta*u)exp(-u/2)
                         sech((sigma_0-1/2)u+k delta*u).

SHIFTED_SECH_POSITIVITY.md proves the required positive definiteness
for every nonnegative shift and scale. Applying its finite matrix
inequality to the two exact squares defining P proves the assertion.
Thus discarded prime powers are nonnegative even though the kernels
now depend on k. Merely knowing every f_k>=0 would not suffice.

## 2. A quantitative prime lower bound survives

Compare the retained prime powers (2,m<=10),(3,m<=6),(5,m<=5),
(7,m<=4) to the constant-sigma_0 detector. The latter satisfies
the proved lower bound 1.26eta-90eta^3. The derivative of sech has
absolute value at most 1/2. Using w<=6 and |cos|<=1, the total change
in these retained terms has absolute value at most

    (3/2)eta*delta*(sum_k k ak)
           sum_(p,m retained) (log p)^2*m*p^(-m/2).

The exact checker proves sum_k k ak<7 and bounds the second sum by
the larger infinite sum

    sum_(p=2,3,5,7) (log p)^2*r_p/(1-r_p)^2 <16,
    r_p=p^(-1/2).

It uses rational upper square-root reciprocals
(.708,.578,.448,.378) and rational upper logarithms
(.6932,1.0987,1.6095,1.9460), checking each direction. Hence

    D >=1.26eta-90eta^3-168eta*delta.                    (V1)

The loss is uniform over all phases and is not a numerical minimum.
It is only charged on retained prime powers; all other terms remain
nonnegative by Section 1.

## 3. Frequency-specific zero cutoffs

Let H=3*10^12,T0=10^10. In the global minimum-zero argument take
A=B=(1-beta0)log t and l=log t, for a chosen minimizing zero above H.
For each k>=1 use the cutoff T_k=kt+T0. The checker proves

    T0 exp(-28)<.01,
    log(k+.01)<c+kd,   k=1,...,12.

Consequently, writing C_k=log(k+T0 exp(-l)),

    (c+kd)/l >= C_k/(l+C_k),
    sigma_k >=1-B/log(kt+T0).                          (V2)

The minimum-zero property and reflection symmetry put every zero
with |gamma|<=T_k in [1-sigma_k,sigma_k]. For k=0 use T_0=T0<H;
all zeros below that cutoff are on the critical line by the imported
finite verification. The chosen zero and its reflection are retained
at k=1. Multiplicities are handled exactly as in the baseline.

For the omitted zeros, |gamma|>kt+T0 implies |kt-gamma|>T0.
Their real arguments lie in [-eta,alpha_k+eta], because
0<=1-sigma_k<=eta. Thus the adapter's -10eta/y^2 pair lower bound
applies. The baseline's direct Lehman calculation is valid with
T=T_k=q+T0, q=kt: it already enlarged the integration interval to
this endpoint, and only requires log T_k<l+3. Therefore each
nonzero-frequency loss remains below 1e-8. The k=0 reciprocal-square
tail remains below 4e-10. No common cutoff 12t+T0 is used in (V2).

## 4. Explicit formula and sufficient scalar inequality

Apply the exact explicit formula separately to (sigma_k+ikt,f_k),
multiply by ak, and sum. Its validity does not require the different
real points sigma_k to belong to one common zero-free half-plane.
The prime side is finite because every f_k is compactly supported.

The gamma coefficient is bounded by the same Carch=-3.00317:
all sigma_k<=1, all ak>=0, and f_k(0)=eta*w0/2. High-frequency
gamma, pole and E errors retain the old bounds because their
parameters stay in the same uniform range. The zero-frequency
correction is E_(f_0)(sigma_0)<=-.31eta. Keeping the full old 1e-7
remaining error allowance is conservative.

Put

    z0=sigma_0-1,
    z1=sigma_1-1+eta=eta*(c+d)/l,
    z2=sigma_1-eta.

The necessary inequality obtained from a minimizing zero is

    a1[F_1(z1)+F_1(z2)]-F_0(z0)
      <=eta*w0/2*(aP*l/2-3.00317)+1e-7
                       -1.57eta+90eta^3+168eta*delta.  (V3)

The extra .31eta and the prime contribution concern distinct
summands. The transform lower bound on the left side is

    a1 W((c+d)/l)-W(-1+c/l)
      +eta*w0[a1/z2+J(z0,alpha_0)
                      -a1J(z1,alpha_1)-a1J(z2,alpha_1)]
      -51eta^3[(z0+alpha_0)^(-3)
                     +a1(z1+alpha_1)^(-3)+a1 z2^(-3)]. (V4)

This follows from the same logistic-complement identities as the
baseline, using ||w''||<51. In particular the pole term uses alpha_0
and the selected-zero terms use alpha_1; interchanging them would
not be justified.

The companion `certify_variable_sigma.py`, with the margin defined
in `probe_variable_sigma.py`, proves that (V4) minus the right side
of (V3) is strictly positive throughout

    0<=A<=1000/4813, 28<=l<=8241/100.                   (V5)

Despite the helper filename, it is this full-rectangle replay, not
the helper's point-probe main block, that supplies the certificate.
Its initial run accepts 24 closed rational boxes with minimum
directed lower bound greater than .00002666. All transforms have
the same rigorous moment/Taylor and positive-beta-series errors as
the frozen baseline. A=0 is only the continuous scalar extension.
The JSON binds the producer, margin source and degree-12 dependency.
An independent exact Fraction replay is a separate review obligation.

## 5. Global conclusion and scope

Put Astar=1000/4813=1/4.813 and Lstar=exp(21.233 Astar)<82.41.
The published Littlewood region excludes violations above
exp(Lstar); the finite verification excludes them below H. A
violation in between has a positive global minimum B, using the
classical strict strip and discreteness exactly as in the earlier
wrapper. Use (V2), isolate its pair, and obtain (V3). This contradicts
(V5). Conjugation gives the negative-height statement.

Thus the proposed assembled conclusion, subject to the stated
analytic/imported inputs and independent certificate review, is

    zeta(s)!=0 when Re s>1-1/(4.813 log|Im s|), |Im s|>=3.

The new analytic point is the positive-definite shifted-sech factor,
which permits the frequency-dependent real parts while retaining
arithmetic positivity. No empirical zero census, RH assumption, or
new fixed-width Hecke conclusion is used. Human mathematical review
remains outstanding.
