# Assembled proposed theorem: R=118/25

23 October 2026. All logarithms are natural. This is a proposed
source-dependent analytic theorem with exact finite certificates, awaiting
review of the complete frozen assembly. It is distinct from the fixed
half-plane problem and RH.

**Theorem.** Under the explicitly imported results in SOURCES.md,

    zeta(sigma+it) != 0 if |t|>=3 and sigma>1-25/(118 log|t|).

The imported results are mathematical theorems or identified preprint
results, not assumptions of RH or of a zero-free half-plane.

## 1. One global minimizing zero for both detectors

Let Astar=25/118 and H=3*10^12. The published Littlewood region with
coefficient21.233 excludes a violation at heights for which
loglog|t|>=21.233*Astar. Finite RH verification excludes every violation
with 3<=|t|<=H: the asserted right boundary is greater than1/2 there.

If a violation exists, there is therefore a zero rho=beta+it with t>H
that minimizes B=(1-beta)log t among all zeros above H. Discreteness and
the finite upper localization imply that this minimum is attained;
the classical nonvanishing on Re s=1 gives 0<B<Astar. Conjugation allows
t>0. Every zero above H has its corresponding product at least B.
Reflection gives the matching left edge. This is the same minimum used
in both arguments below. Put l=log t. The exact checker proves
exp(287/10)<H, hence l>28.7.

## 2. The lower-height logistic detector

Use exactly the kernel and polynomial in BASELINE_PROOF.md sections2--4:
theta=5669/5000, w=g*g, w0=w(0), W its one-sided Laplace transform,
and the rational degree12 polynomial P=sum a_k cos(kx). The exact integer
sum-of-two-squares representation gives P>=0, a0=1, a_k>0,
a1=1738295793206197388801164/1000000001299439064580929 and
aP=sum_(k>=1)a_k=3498832394672653287444040/1000000001299439064580929.
The unchanged proofs give w0<6, ||w''||<51, Carch<-3.00317,
E_(f_0)(sigma_0)<=-.31eta, and the four-prime gain
1.26eta-90eta^3 for eta<=.0075.

For 0<A<=25/118 and 28.7<=l<=52 put

    eta=A/l, u=eta/l, c=153/400, d=2/25,
    a=1/2-eta+c*u,
    sigma_k=1/2+sqrt(a^2+2*a*d*u*k^2), k=0,...,12,
    alpha_k=2*sigma_k-1,
    f_k(v)=eta*w(eta*v)/(1+exp(-alpha_k*v)).

The exact finite checks prove eta<.0075, .99<sigma_k<1, a>.4925,
and A/l^2<.21/28^2. Thus the previous uniform analytic domains remain
valid even though Astar now exceeds .21. The earlier lower endpoint28
is deliberately replaced by28.7; using28 would exceed the eta domain.

The quadratic-profile proof is in
three-hour-boundary/QUADRATIC_SIGMA_LOGISTIC_DETECTOR.md sections1--4.
It applies with the new c,d and the bounds just verified. Briefly,
sech(sqrt(s)) is completely monotone, so
sech(v sqrt(a^2+2*a*d*u*k^2)) is a positive-definite sequence in k.
Applying its Toeplitz matrix to each exact square of P proves arithmetic
positivity at the differing sigma_k. Comparing the retained primes to
sigma_0 costs at most336*d*eta^2/l. This uses sum k^2*a_k<14 and an
exact upper bound16 for the retained-prime variation sum.

For each k>=1 take T_k=kt+10^10; take T_0=10^10. The finite cutoff
inequalities, including the square-root correction, prove

    sigma_k >= 1-B/log T_k.

Indeed log(k+.01)-c + [.21/(2*.4925*28^2)](log(k+.01)-c)^2
is less than d*k^2 whenever log(k+.01)>c, and the other case is
immediate. Also 10^10 exp(-28)<.01. The minimum property therefore
puts every zero below T_k in the required reflection strip. The
frequency-specific tail calculation is preserved in
three-hour-boundary/VARIABLE_SIGMA_LOGISTIC_DETECTOR.md section3.
All omitted-zero, high-frequency pole, gamma and E errors together
remain below the unchanged10^-7 allowance.

Write

    r=sqrt(a^2+2*a*d*eta/l),
    rho1=c/l+2*a*d/[l*(r+a)],
    z0=sigma_0-1, z1=eta*rho1, z2=sigma_1-eta.

The stable rho1 expression extends continuously to A=0. For
J(z,alpha)=integral_0^infinity exp(-zv)/(1+exp(alpha*v))dv, the selected
zero signal has the lower bound

    S_low=a1*W(rho1)-W(-1+c/l)
      +eta*w0*[a1/z2+J(z0,alpha_0)
                       -a1*J(z1,alpha_1)-a1*J(z2,alpha_1)]
      -51eta^3*[(z0+alpha_0)^(-3)
                       +a1*(z1+alpha_1)^(-3)+a1*z2^(-3)].

The exact explicit formula and the retained terms imply, at the
minimizing zero,

    S_low-w0*[B*aP/4-3.00317eta/2]
       +1.57eta-90eta^3-336*d*eta^2/l-10^-7 <=0.       (L)

The separate alpha_0 and alpha_1 are essential. The constant1.57
combines the distinct1.26 prime gain and .31 signed E correction.

`two-hour-root-20261023/verify_p12_472_fraction.py` reconstructs (L)
and proves its left side strictly positive on the entire closed rectangle
0<=A<=25/118, 287/10<=l<=52. It accepts28 rectangles, with disjoint
interiors, exact area1165/236, and minimum lower bound greater than
.00009525971317. All acceptance uses outward rational intervals;
the unsupported A=1/4 negative control fails. A=0 is only a continuous
scalar extension, not a physical kernel. Thus l<=52 is impossible.

## 3. The shifted higher-height detector

Use the complete argument S1--S20 in
two-hour-global-20261023/SHIFTED_CENTER_FORD_DETECTOR.md. Its kernel has
theta=23/20 and the same polynomial P. At l>=52 set

    h=log(12t+100), lambda=B/h, sigma=1-lambda, eta=1/2-lambda,
    f(v)=lambda*w(lambda*v), F(z)=W(z/lambda).

The common global minimum puts every zero in the required horizontal
strip throughout [t-100,12t+100]. Here lambda<1/160 and eta>=79lambda.
The exact compact-test formula remains valid at this below-one center.
Its physical prime sum equals the old Ford prime sum, and its pole and
selected-zero signals remain W(-1) and W(h/l-1).

The new local half-disc bound has loss H*lambda^3/eta^3 per zero. A
comparison with the positive Hadamard kernel at sigma+eta gives an
outside-disc bound with the exactly opposite local-count term. They
cancel, leaving a cubic error rather than the previous quadratic one.
All wrong-sign far cotangent terms are retained and bounded by an
explicit exponential tail. Reflection at the real center supplies
a separate .55*lambda gain; the exact four-prime gain is
.255*lambda-18*lambda^3. The real and complex E_f errors are retained.

The right-line Euler constant satisfies C(lambda)<.9 uniformly, and
-zeta'/zeta(1.48)<2, by the new finite-prime-power certificate with
positive analytic tails. The critical-line estimate uses the complete
shifted Revers envelope at every smoothing ordinate, including l<60.

For Astar=25/118 and all l>=52, S20 gives a lower bound M(Astar,l)
for the necessary detector inequality, simultaneously for every
0<B<=Astar. Its signal increases with l and every adverse term decreases;
the note proves these assertions analytically, retaining the full shifted
envelope. The exact checker verifies

    M(25/118,52) > .0002948890299043.

It also checks the kernel and elementary remainder constants. The
separate Euler and prime checkers reconstruct their finite sums and
all phase covers. Hence the minimizing zero cannot have l>=52.

## 4. Conclusion and scope

The same minimizing zero has l>28.7, while sections2 and3 exclude both
sides of52, including their shared endpoint. This proves the proposed
source-dependent conclusion. Negative heights follow by conjugation;
the finite prefix is supplied by the imported verification to3*10^12.

The finite certificates do not reprove the external analytic inputs.
The assembled source requires independent exact-commit review before
integration. It proves no smaller fixed half-plane boundary B_flat and
does not prove RH. In particular, the working imported fixed boundary
already excludes the region relevant here; this result is an independent
classical-form theorem, not an additional zero exclusion relative to it.
