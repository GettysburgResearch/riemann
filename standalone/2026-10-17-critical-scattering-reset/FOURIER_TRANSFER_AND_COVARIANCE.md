# Additive Fourier transfer for weighted completions, and the remaining coherent mode

Research note, 17 October 2026. This is a proposed elementary deduction from
explicit local coefficient families and established analytic inputs. It is
not a proof of RH. The local multiplier and Fourier/covariance arguments
received a separate mathematical read during this session; this is not an
independent human referee report. Global literature novelty is not claimed.
No publication is performed by this note's author.

## 1. Current source map

The live OpenAI mathematics repository was read at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` (main, commit date 12 October
2026). Its current CONTENTS lists 719 manuscripts and 372 result families.

* Result 003: `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/`.
  `paper.pdf` (blob `8132b77eeb270a70b25df8d6609f008e83e65d91`) states
  nonvanishing for every Dirichlet L-function and every finite-order Hecke
  L-function over Q(sqrt(-3)) on Re(s)>7/8. The full TeX source was fetched
  and its architecture inspected; this is not a line-by-line proof audit.
* Companion: `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf`
  (blob `3ea94d87ffdee8db02c6ef1e563e6d166021ad2f`) states >11/12 by a
  sextic-twist mean square and extraction of sixth powers. Its TeX source
  was fetched and the introduction/reduction inspected.
* Result 007: `preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf`
  (blob `a1fa025a59ecbfc5176d16cfdc6e0afd418cc82e`). The entire introduction
  and the quantitative setup and spectral-transfer sections were read.
  The quantitative result is for Liouville along fixed nonproportional
  affine forms, with an absolute logarithmic-saving exponent but constants
  depending on those forms. It explicitly asserts **no uniformity for
  coefficients growing with X**. The general corrected Elliott result
  asserts qualitative ordinary cancellation, with no quantitative rate.
* Cureton--Thorner: https://hexagonmath.org/2610.00200v2 , current version
  submitted 14 October 2026. Both its PDF and version-specific TeX were
  inspected. The theorem remains the all-number-field >31/32 statement.
  https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The >7/8, >11/12 and >31/32 conclusions above are descriptions of the
sources' assertions, not claims that this note rebuilt their proofs or Lean
dependencies. No additional later Dirichlet result was found in a complete
current CONTENTS scan.

The existing repository packet
`standalone/2026-10-17-affine-cancellation-lift/THEOREMS.md` was read at
`943d7714f81b97a75652ebc6e19990a88c917d4d` (#956). That packet already proves
fixed-affine logarithmic correlation transfer and qualifies its ordinary
version separately. Euler stripping itself is also already in #948/#950;
it is not claimed here as new. The purpose below is a quantitative Fourier
interface that avoids passing a fixed-form theorem to growing CRT moduli.

## 2. The coefficient families and their convolution multipliers

Use precisely the rational-integer families of #956. Fix a finite excluded
prime set S and a Dirichlet character xi, with all its conductor primes in
S. Write a(n)=mu(n)xi(n)1_((n,S)=1). For p outside S set

    A = xi(p) x,  B = z_p p^((m-2)/2) x^m,  v = 1-1/p,

where m>=2 is an integer and |z_p|<=1. The local factors of F are

    native:       1-A;
    coupled:      1-vA-B;
    two-channel:  (1-A)(1-B);
    geometric:    1-vA/(1-B).

At p in S both a and F have Euler factor 1. These are formal coefficient
identities, not Euler products presumed convergent on a critical line.

Let b be the multiplicative sequence whose local generating series is
F_p(x)/(1-A). Then, exactly as arithmetic functions,

    F = a * b.                                                   (2.1)

### Lemma 2.1: an invertible weighted convolution multiplier

For every fixed sigma>1/2 there is a constant C_sigma such that

    sum_n |b(n)|/n^sigma <= C_sigma,
    sum_n |b_inverse(n)|/n^sigma <= C_sigma,                       (2.2)

uniformly in all m>=2, S, permitted xi and powerful profiles. The second
sequence is the Dirichlet-convolution inverse of b, so a=F*b_inverse.

Proof. Put delta=sigma-1/2>0 and evaluate the absolute coefficient norm of
each power series at x=p^(-sigma). Then |A| has majorant p^(-sigma), and
|B| has majorant p^(-1-m delta). For the coupled family,

    b_p-1 = (A/p-B)/(1-A),
    b_p^(-1)-1 = (-A/p+B)/(1-vA-B).                               (2.3)

The denominator majorants are uniformly separated from zero, since

    1-v p^(-sigma)-p^(-1-m delta)
      >= (1-1/p)(1-p^(-1/2))
      >= (1/2)(1-1/sqrt(2)) > 0.

Consequently their absolute coefficient norms minus one are at most a
universal constant times

    p^(-1-sigma) + p^(-1-m delta).

For the two-channel family b_p=1-B and b_p^(-1)=1/(1-B), and the same
majorant works. For the geometric family,

    b_p-1 = (A/p-AB)/((1-A)(1-B)),
    b_p^(-1)-1 = (-A/p+AB)/(1-vA-B),                              (2.4)

so the same, or a smaller, majorant again works. The native multiplier is
1. Finally m>=2 gives p^(-1-m delta)<=p^(-1-2 delta), whose prime sum
converges. Multiplying the absolute local norms proves (2.2). The identities
also prove the stated inverse relation coefficient by coefficient. QED.

The constant need not remain bounded as sigma approaches 1/2. The
uniformity here applies at every fixed sigma>1/2; no endpoint bound is
being inferred. A stronger convergence domain for a particular geometric
factor can coexist with this uniform family statement.

## 3. Quantitative additive and polynomial phase transfer

Write e(t)=exp(2 pi i t) and S_f(X,alpha)=sum_(n<=X) f(n)e(alpha n).
The exact identity, retaining all coefficient signs, is

    S_F(X,alpha)=sum_(d<=X) b(d) S_a(X/d,d alpha).                 (3.1)

### Theorem 3.1: no loss of a power exponent

If, for some lambda>1/2,

    sup_alpha |S_a(Y,alpha)| <= C Y^lambda  (Y>=1),               (3.2)

then

    sup_(profiles,m>=2,alpha) |S_F(X,alpha)|
           <= C C_lambda X^lambda.                              (3.3)

Conversely a bound (3.3) for any one such F implies (3.2), with its
constant multiplied by the inverse norm in (2.2). The same result holds
with an arbitrary fixed epsilon loss and for phases alpha_k n^k+...+alpha_1 n,
uniformly in their coefficients, provided the native bound is uniform in
those coefficients.

Proof. Apply (3.2) inside the exact finite sum (3.1) and sum
|b(d)|d^(-lambda). The converse uses b_inverse. Polynomial phases are
stable under n=dr, with coefficients alpha_j d^j, so the identical proof
works. QED.

Thus this entire family of completions has the same additive Fourier power
threshold as its native Möbius skeleton. The theorem does not manufacture
the missing native estimate; it transfers one with all profile dependence
under control.

### Theorem 3.2: an unconditional quantitative conclusion

For every A>0, with xi and S fixed,

    sup_(profiles,m>=2,alpha) |S_F(X,alpha)|
        <<_(A,xi,S) X/(log(2X))^A.                               (3.4)

The same statement holds for all quadratic phases, uniformly in their
coefficients.

External input: Davenport's uniform Möbius exponential-sum estimate,
reproved in Green--Tao, *Quadratic uniformity of the Möbius function*,
arXiv:math/0606087v2, Example 3, (1.3), and Section 5. The quadratic input is
their (1.7), proved in Section 7. https://arxiv.org/pdf/math/0606087
The paper's statements and proof references were read. These established
analytic theorems are imported, not newly proved here.

Proof. The factor xi(n)1_((n,S)=1) is a fixed periodic sequence. Its finite
additive Fourier expansion reduces the required native estimate to the
quoted uniform estimates; it only changes the constant. Fix
sigma_0 in (1/2,1), for example 3/4. In (3.1), for d<=sqrt(X) apply the
native logarithmic estimate and log(2X/d)>=1/2 log(2X), after a harmless
change to the constant. Sum |b(d)|/d using (2.2) at sigma=1. For d>sqrt(X)
use the trivial |S_a(X/d)|<=X/d and

    X sum_(d>sqrt(X)) |b(d)|/d
        <= C_sigma0 X^((1+sigma_0)/2).

This is absorbed by the right side of (3.4). Polynomial phases use the same
argument. No growing-mask or growing-affine-form estimate is inserted.
QED.

## 4. Complete covariance at growing shifts

For an integer N>=2 let f(n)=F(n)1_(1<=n<=N), extended by zero to Z,
and similarly g(n)=G(n)1_(1<=n<=N), where F,G can be different families.
Define the complete signed cross-correlation

    C_(F,G)(N,h)=sum_(n in Z) f(n) conjugate(g(n+h)).               (4.1)

The ordinary square-mass bound of #956, Lemma 3.1, is

    sum_(n<=N)|F(n)|^2 <= zeta(2) N.                              (4.2)

This bound is inherited from that packet, with its short proof repeated for
self-containment. Every supported n has a unique representation n=r d^m,
with r squarefree and |F(n)|^2<=d^(m-2). The coupled and two-channel families
have d squarefree (their respective coprimality rules differ); the geometric
family permits arbitrary d and requires rad(d)|r. The native case has d=1.
For each d, overcounting the allowed r gives at most N/d^m possibilities.
The square masses therefore sum to at most N sum_d d^(-2)<=zeta(2)N.

### Corollary 4.1: all-shift squared correlation saving

For every A>0,

    sum_(h in Z) |C_(F,G)(N,h)|^2
          <<_(A,xi_F,xi_G,S_F,S_G) N^3/(log(2N))^A.               (4.3)

Uniformity includes all powerful profiles and m_F,m_G>=2.

Proof. Fourier inversion and Parseval give exactly

    sum_h |C_(F,G)(N,h)|^2
      = integral_0^1 |S_F(N,t)|^2 |S_G(N,t)|^2 dt.

Bound the first factor by (3.4) with exponent A/2 and integrate the second
using (4.2). QED.

This also bounds the sum of absolute correlations on any H selected shifts
by O_A(N^(3/2) sqrt(H)/(log(2N))^A), after relabeling A. In particular it
gives arbitrary logarithmic savings in average absolute correlation when
H>=N/(log(2N))^B for any fixed B, on choosing A sufficiently large. It does
not prove cancellation for every individual growing shift.

### Corollary 4.2: smooth signed filters of any growing width

Let w be a fixed Schwartz function on R. Uniformly for H>=1 and alpha_0 in R,

    |sum_(h in Z) w(h/H)e(alpha_0 h) C_(F,G)(N,h)|
       <<_(A,w,xi_F,xi_G,S_F,S_G) N^2/(log(2N))^A.                (4.4)

All signs, the diagonal and both orientations are retained. Removing the
diagonal costs only O(N), by (4.2) and Cauchy--Schwarz.

Proof. The Fourier series of C is S_F times conjugate(S_G). Poisson
summation gives a periodic filter whose L1 norm is at most

    integral_R |widehat(w)(u)| du,

independent of H and its modulation alpha_0. Bound the product by the two
supremum bounds in (3.4), with exponent A/2 each, and integrate. QED.

If one has native power bounds with exponents lambda_F,lambda_G>1/2,
the same proof gives the power N^(lambda_F+lambda_G) in (4.4).
The bound (4.3) becomes O(N^(1+2 lambda_F)) using only a power bound for F.

These are quantitative statements for shifts that grow, unlike a
term-by-term application of fixed-shift little-o. They remain far weaker
than the critical signed energy estimate needed for RH.

## 5. Why corrected Elliott plus a quasi-RH-type power is insufficient

There is a simple exact obstruction to treating uniform nonpretentiousness
as a square-root mechanism. Fix 1/2<theta<1 and set

    f_theta(n)=n^(theta-1).

This is one-bounded and completely multiplicative. For every Dirichlet
character chi and every real t,

    D(f_theta,chi n^(it);X)^2
       >= sum_(p<=X) 1/p - sum_p p^(theta-2) -> infinity,          (5.1)

uniformly in t. It therefore satisfies the exact qualitative
nonpretentiousness hypothesis of OpenAI 007, even with no restriction on
the height of t. Nevertheless

    sum_(n<=X) f_theta(n) = X^theta/theta + O(1),                 (5.2)

and uniformly for every h>=0,

    0 <= sum_(n<=X) f_theta(n) f_theta(n+h)
       <= sum_(n<=X) n^(2theta-2)
       <<_theta X^(2theta-1).                                   (5.3)

Thus even a **uniform power saving for every shifted correlation**,
combined with a one-point power exponent theta<1 and complete
multiplicativity/nonpretentiousness, need not yield a square-root bound.
For the zero-extended finite sequence the exact all-shift identity is

    sum_h C_(f_theta,f_theta)(X,h)
       = |sum_(n<=X) f_theta(n)|^2
       ~ X^(2theta)/theta^2.                                    (5.4)

The individual correlations are small compared with X, but they have a
coherent sign and enough of them survive to carry the full large mean.
This counterexample is not a model of the Möbius prime values, nor does it
show the QRH papers false. It proves the narrower logical point: the
stated generic estimates and nonpretentiousness interface alone cannot
bootstrap a one-point exponent to 1/2. A genuinely Möbius-specific estimate
controlling this aggregate coherent component is still required.

For the actual Möbius-bearing completions, Lemma 2.1 says that this
component cannot be removed merely by choosing a bounded powerful-prime
profile: the change of coefficients is invertible above 1/2. A useful next
attack should therefore target a native structured Fourier/spectral bound,
or introduce a new arithmetic identity whose cancellation survives the
whole sum of growing shifts. The present note supplies rigorous transfer
and diagnostics, not that missing estimate.

## 6. Finite verification performed

`check_fourier_transfer.py` was executed successfully using ordinary Python.
Its exact output is archived in `FOURIER_CHECK_RESULTS.json`.
It checks 96 coefficient cases through n=256, local coefficients through
degree 20, and complete cross-correlations through n=48. It uses rational
arithmetic throughout and tests the inverse as well as the forward
convolution, the literal alpha-to-d-alpha substitution, Parseval by an
independently computed additive convolution, and a complete Fejer filter.
Negative controls reject dropping signs, the negative-shift orientation,
the off-diagonal, or the dilation of the additive phase. Shared prime
powers and successive geometric local powers are explicitly retained.
These checks do not prove the infinite-product estimates, asymptotics,
external analytic theorems, or any RH statement. Complex profiles and odd
degrees are handled by the mathematical majorants above; the finite
fixtures use real rational phases and m=2,4,6.
