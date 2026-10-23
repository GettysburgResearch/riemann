# From a uniform logistic detector inequality to a global zero-free region

Status: proposed analytic theorem wrapper. The conclusion below uses the
explicitly stated finite parameter inequality (M), certified separately by
the root's directed-interval calculation. It is a statement about the actual Riemann zeta
function, not an abstract zero model. It does not imply RH or improve the
repository's separate fixed-width Hecke boundary.

Analytic adapter: ../three-hour-type/LOGISTIC_ADMISSIBILITY.md,
SHA256 a06963aef0863ef1cdf63e93aab27c4b8f0c8051cbab7f159d468e7596d7a25f.
Independent adapter review: REVIEW_LOGISTIC_ADMISSIBILITY.md.
Exact constants: ../three-hour-type/LOGISTIC_REAL_AXIS_CONSTANTS.md,
SHA256 9da9ad7051fcf3deb94db3d951051425c549313074d0ee5bd0dcfae3312c8139,
reviewed in REVIEW_LOGISTIC_CONSTANTS.md.
Scalar certificate: ../three-hour-root/certify_logistic_master.py and
../three-hour-root/LOGISTIC_MASTER_CERTIFICATE.json. Their current hashes
must be bound in the final independent certificate review.
Primary source and notation: Bellotti--Trudgian--Yang (BTY),
https://arxiv.org/html/2603.21490v1 , equation (3),
Definition 1, Lemma 7, and Lehman's zero-counting estimates reproduced
in Lemma 6. The original counting reference is R. S. Lehman,
On the difference pi(x)-li(x), Acta Arith. 11 (1966), 397--410,
Lemmas 1 and 2, DOI https://doi.org/10.4064/aa-11-4-397-410 .

## 1. The exact numerical obligation

Set H=3*10^12, K=16, T0=10^10, theta=1.1338. Let w be BTY's
Heath-Brown function, w0=w(0), and W its Laplace transform. Use the
source's nonnegative trigonometric polynomial P=sum_(k=0)^16 a_k cos(kx),
with a0=1, a1=865534/497079, and a=sum_(k=1)^16 a_k=2919857/828465.
Its squared-polynomial definition proves P>=0; its rational coefficients
are positive. Put

    Astar=1/4.84,
    Lstar=exp(21.233*Astar),
    Carch=-3.0126.

For 0<A<=Astar and log(H)<=l<=Lstar, define

    c(l)=log(16+T0 exp(-l)),
    mu=l/(l+c(l)), eta=A/l, sigma=1-A/(l+c(l)), alpha=2sigma-1,
    f(u)=eta w(eta u)/(1+exp(-alpha u)),
    F(z)=integral_0^infinity exp(-zu)f(u)du.

The finite parameter obligation is the strict inequality

    a1[F(sigma-1+eta)+F(sigma-eta)]-F(sigma-1)
      > eta*w0/2 * [a*l/2+Carch] + 10^(-7).            (M)

A certificate must cover the whole closed parameter rectangle, not only
sample points. The root's certificate covers the larger rational rectangle
(0<=A<=25/121, 28<=l<=81) by closed rational subrectangles, and proves
log H>28 and Lstar<81. Here 25/121=Astar exactly. At A=0 it certifies
the continuous extension of the sufficient scalar expression; the
physical f and F parameterization is used only for A>0.
No prime-power lower contribution is required in (M).

**Conditional conclusion.** If (M) holds, then zeta(s) has no zero with

    Re s > 1-1/(4.84 log |Im s|),      |Im s|>=3.       (G)

This is an improvement of a classical logarithmic zero-free constant,
not an assertion of a fixed-width zero-free strip or the full conjecture.

## 2. Nonzero-frequency terms and the zero-frequency correction

The adapter's exact explicit formula is

    Re sum_n Lambda(n)n^(-s) f(log n)
       =f0 Re A_gamma(s)+Re F(s-1)-Re sum_rho F(s-rho)
          +Re E_f(s),
    A_gamma(s)=-log(pi)/2+psi(s/2+1)/2,
    E_f(s)=integral_0^infinity exp(-(s+2)u)
                   [f0-f(u)]/(1-exp(-2u))du,
    f0=eta*w0/2.                                      (E)

The zero sum is over nontrivial zeros with multiplicity. Its real parts
converge absolutely on bounded s sets; conjugate pairing gives locally
normal convergence of the corresponding analytic sums. The adapter
proves (E) by reduction to BTY Lemma 7, without requiring f'(0)=0.

On the enlarged rectangle sigma>.99, alpha>.98 and eta<.0075. The adapter
supplies |Re E_f(sigma+ikt)|<2500 eta/(kt)^2 for k>=1 and
|Re F(x+iy)|<5 eta/y^2 for -eta<=x<=alpha+eta and |y|>=10^10.
The latter covers the nonzero-frequency pole terms at x=sigma-1.

The exact constants note proves, by rational interval inequalities,
that f(u)>=f0 for 0<=u<=10 and

    E_f(sigma)<=10^(-10)eta.                            (E0)

It also reconstructs the source a_k exactly and proves that the
coefficient independent of log t in the gamma sum is at most Carch.
For completeness, BTY (36) with x=sigma/2+1 in [1,1.5] and
y=kt/2>=H/2 gives

    |Re psi(x+iy)-log y|
       <=x/(2y^2)+1/(12xy)+x^2/(2y^2)
       <=1.875/y^2+1/(12y)<10^(-12).

Since a<4, the gamma sum therefore obeys

    sum_(k=0)^16 a_k Re A_gamma(sigma+ikt)
        <=a log(t)/2+Carch+2*10^(-12).                 (A)

The total weighted high-frequency E error is at most
4*2500*.008/H^2<10^(-20), and the corresponding pole error is at
most 4*5*.008/H^2<10^(-24). The gamma error after multiplying by
f0<.024 is less than 10^(-12); (E0) is also less than 10^(-12).
The distant-zero error below costs at most
(sum a_k)*10^(-8)<5*10^(-8). Their sum is strictly less than
10^(-7), the explicit relaxed budget used in (M).

## 3. A minimum-zero argument replaces infinitesimal iteration

Put b(rho)=(1-beta)log|gamma|. The imported explicit
Littlewood region, BTY (3), gives b(rho)>=log(log|gamma|)/21.233.
In particular every zero at |gamma|>=Tstar:=exp(Lstar) has b>=Astar.
The source finite verification states that all zeros with |gamma|<=H
lie on the critical line.

Suppose (G) is false. A violating positive-height zero must have
H<t<Tstar. There are only finitely many zeros in this bounded closed
region: zeta's nontrivial zeros are isolated, and they lie in the
compact critical strip away from its pole. Select one whose value
b is smallest and call this minimum B. The classical strict critical
strip 0<beta<1 (including the known nonvanishing on Re s=1) gives

    0<B<Astar.

No numerical zero-free constant is needed to initialize this argument.

Every zero of height at least H, including those above Tstar, obeys
b>=B. At the selected rho0=beta0+it choose precisely

    eta=1-beta0=B/log t, sigma=1-B/log(Kt+T0).

No epsilon thickening is needed. If |gamma|<=Kt+T0, the global
minimum property and reflection symmetry imply

    1-sigma<=beta<=sigma.

For |gamma|<=H this follows directly from beta=1/2. Thus every
low-height reflected pair lies in the positivity strip of the
logistic adapter. Pairs are grouped by rho and 1-conjugate(rho);
a zero on the critical line receives half the identical pair.
Multiplicity is retained. Isolate one occurrence of rho0 and its
distinct reflection when k=1. Every other such pair contributes
nonnegatively, including a pair lying on the strip boundary.

For |gamma|>Kt+T0, both zero arguments have real parts in
[-eta,alpha+eta], because 1-sigma<=eta and 0<=beta<=1. Their
imaginary parts have modulus above T0. The adapter's pair lower bound
is -10eta/y^2. We evaluate the tail from the counting inequality
directly, avoiding the numerical constants in BTY's evaluated tail.
For k>=1 put q=kt, d=T0, T=Kt+d and

    phi(x)=(x-q)^(-2)+(x+q)^(-2),       x>=T.

This is continuous, positive and decreasing. Lehman's estimate, after
letting the upper endpoint tend to infinity, states

    sum_(gamma>T) phi(gamma)
       <=(1/(2pi)) integral_T^infinity phi(x)log(x/(2pi))dx
                    +4phi(T)log T+2 integral_T^infinity phi(x)/x dx.

All sums here count positive-height zeros with multiplicity. Since
T>=q+d, replacing the integration range and then x=q+u gives

    integral_T^infinity phi(x)log(x/(2pi))dx
       <=2 integral_d^infinity u^(-2)log(u+q)du
       =2[log(d+q)/d+log(1+q/d)/q]
       <=2*10^(-10)(l+4).

Here log(d+q)<=log T<l+3 and log(1+q/d)<=q/d. Also

    4phi(T)log T<=8*10^(-20)(l+3),
    2 integral_T^infinity phi(x)/x dx<=4*10^(-20).

Even replacing 1/(2pi) by 1 leaves the convenient bound

    sum_(gamma>T) phi(gamma)<10^(-9)(l+4).

Therefore the entire distant-zero loss is at most

    10eta*10^(-9)(l+4)
       <10^(-8)*.21*(1+4/28)=2.4*10^(-9)<10^(-8).

For k=0 use Lehman's reciprocal-square estimate
sum_(gamma>T0) gamma^(-2)<log(T0)/T0. The symmetric-height loss is
at most 20eta log(T0)/T0<4*10^(-10), again below 10^(-8).
Endpoint zeros can be handled by a one-sided limit in the upper
bound; excluding gamma=T only decreases its left side. Consequently

    Re sum_rho F(sigma+it-rho)
       >=F(sigma-1+eta)+F(sigma-eta)-10^(-8),

and the analogous sum for k!=1 is at least -10^(-8).

Multiply (E) at s=sigma+ikt by a_k and sum. The arithmetic side
is nonnegative because Lambda(n)>=0, f>=0 and P>=0. Use (A), the
(E0), the isolated-zero inequality, and the error
budget. The resulting necessary inequality is the reverse of (M),
at A=B and l=log t. This contradiction proves (G) above H.
The finite verification proves it from 3 to H, since its right
boundary exceeds 1/2. Negative heights follow by conjugation.

## 4. Scope of the conclusion

The finite interval certificate, the analytic adapter, this global
wrapper, and the imported finite RH verification and Littlewood region
are distinct proof obligations. Passing the scalar checker does not by
itself prove the analytic inputs. The proposed conclusion is source-
dependent and requires final independent review of their assembled
interfaces; it has not received human mathematical review.
