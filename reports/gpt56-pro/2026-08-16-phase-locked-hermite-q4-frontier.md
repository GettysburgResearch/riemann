# Phase-locked First-Hermite/Q4 continuation beyond the centered cubic gate

## Executive verdict

This packet keeps PR #498 frozen at

```text
6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

and first reconstructs its complete centered-cubic chain. The finite endpoint
identity, normalization, real-endpoint interpolation, Mellin transform, pole
survival, centered-energy equivalence, and CPBD equivalence all survive. The
independent exact-head review in PR #515 reaches the same verdict: the packet is
a correct RH-equivalent criterion, while CPBD is open.

The continuation does **not** rename CPBD. It changes the test family. The exact
scale-four Q4 factor and its critical adjoint produce the nonnegative real-line
multiplier

\[
P(u)=5-4\cos((\log4)u)
=(2-e^{i(\log4)u})(2-e^{-i(\log4)u}).
\]

Multiplying the first-Hermite zero test by \(P^{2m}\) gives a new
RH-equivalent hierarchy. On the prime side, critical conjugation factors its
finite-shift operator as

\[
e^{u/2}D_L e^{-u/2}
=(I-T_L)(4I-T_{-L}),
\qquad L=\log4.
\]

Every filter level therefore contributes a genuine order-two backward
difference at the absolute prime saddle. Using only Chebyshev, Stirling, finite
differences, and Hermite derivative bounds gives the unconditional pointwise
estimate

\[
|S_m(q,x)|\ll_m e^{q/4}q^{3/2-m}
\]

for fixed \(m\), and uniformly for sublinear growing order,

\[
|S_m(q,x)|
\le C_0e^{q/4}q^{3/2}
\left({C_0m\over q}\right)^m.
\]

This proves a genuinely larger pointwise positive region. For fixed \(m\ge2\),

\[
q\le4\log\log(2+|x|)
 +(4m-6-o(1))\log\log\log(3+|x|)
\]

is unconditionally positive. With an explicit sublinear order profile, **every
prescribed sublinear excess** above the constant-four line is removed:

\[
q\le4\ell(x)+\Delta(\ell(x)),
\qquad \Delta(t)=o(t).
\]

This is not RH. A maximum-modulus theorem proves that a scalar phase-blind
analytic filter which retains a fixed terminal depth cannot create the fixed
exponential gap needed to cross

\[
q=(4+\delta)\ell(x),\qquad\delta>0.
\]

The remaining theorem is therefore genuinely arithmetic: signed cancellation
at one prescribed carrier, not another diagonal, cardinality, or average
estimate.

## 1. Frozen centered-cubic reconstruction

For

\[
c_\circ(m)=\Lambda(m)-4\mathbf1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r},
\]

let

\[
R_N(j)=C_\circ(N)-C_\circ(j)-C_\circ(N-j-1),
\qquad0\le j<N.
\]

The predecessor \(N-j-1\) is mandatory. Put

\[
M_N={1\over N}\sum_jR_N(j),
\qquad
\mathscr V_\circ(N)={1\over N^2}\sum_j|R_N(j)-M_N|^2.
\]

For the mean-zero Bernoulli weight

\[
w(\theta)=\theta(1-\theta)-{1\over6},
\qquad
\int_0^1w^2={1\over180},
\]

the exact projection is

\[
\mathcal A_\circ(N)
=\int_0^1w(\theta)Q_{\circ,N}(\theta)d\theta
=\sum_{m\le N}c_\circ(m)K(m/N),
\]

where

\[
K(x)={x(1-x)(2x-1)\over3}.
\]

The normalization is

\[
|\mathcal A_\circ(N)|^2
\le {N\over180}\mathscr V_\circ(N).
\]

The Mellin multiplier is

\[
\widehat K(s)={s-1\over3(s+1)(s+2)(s+3)}.
\]

Consequently

\[
\begin{aligned}
\int_1^\infty\mathcal A_\circ(X)X^{-s-1}dX
={}&\widehat K(s)\\
&\times\left[(1-4^{1-s})\left(-{\zeta'\over\zeta}(s)\right)
+3(\log4){4^{-s}\over1-4^{-s}}\right].
\end{aligned}
\]

Every nontrivial open-strip zeta zero remains a pole. For \(N\le X<N+1\),

\[
|\mathcal A_\circ(X)-\mathcal A_\circ(N)|
\le {X-N\over NX}\|K'\|_\infty
\sum_{m\le N}m|c_\circ(m)|=O(1),
\]

where the weighted source bound follows from Chebyshev and the explicit
four-adic tower. Thus

\[
\mathrm{RH}
\iff
\mathscr V_\circ(N)\ll(\log N)^A
\]

and

\[
\mathrm{RH}
\iff
|\mathcal A_\circ(N)|^2\ll N(\log N)^B.
\]

The second display is CPBD after the exact prime-block decomposition. It is a
criterion, not a producer.

## 2. Why the obvious arithmetic continuations do not close

### 2.1 Generic large sieve

The mean-free Q4 major arc still contains the single additive mode \(a=1\) at
modulus \(N\). Its phase varies only once over the prime interval. A large-sieve
average over many frequencies or moduli does not bound that prescribed mode.
A bound of square-root/polylogarithmic strength for it is already the scale of
the centered cubic criterion.

### 2.2 Additive-modulus covariance

The exact character expansion uses characters modulo a large **additive
modulus**, but imprimitive characters can have small primitive conductor. More
importantly, averaging over character families does not remove the one fixed
endpoint and one fixed low numerator. A pointwise amplifier strong enough to do
so would need an independently stated theorem; no such theorem is imported.

### 2.3 Endpoint variation

Hardy inversion and endpoint variation re-express the same low-frequency
object. They preserve power exponents but do not produce cancellation. Treating
the inversion as a gain would be circular.

### 2.4 Positive generalized-prime annulus

The exact Q4 source dictionary gives a positive generalized-prime source
\(\lambda_4\) with

\[
c_\circ=(\varepsilon-4\delta_4)*\lambda_4.
\]

The reciprocal kernel yields the true positive observable

\[
N\sum_{N/4<n\le N}{\lambda_4(n)\over n}\ge0.
\]

Its Mellin transform has an unavoidable real pole at \(s=1\) with residue
\(2\log4\). After subtracting that main term, positivity disappears. Hence
Landau positivity cannot be used to bypass the centered criterion.

### 2.5 Cardinality and alignment

R-93254 remains binding. Many prime blocks in one half-plane can create an
arbitrarily large coherence ratio. The phase-locked route below obtains an
actual analytic gain before taking absolute values; it never treats block count
as an upper bound.

## 3. Exact phase-locked hierarchy

Let

\[
L=\log4,
\qquad
P(u)=5-4\cos(Lu).
\]

For real \(u\), \(1\le P(u)\le9\). For \(u=iy\),

\[
P(iy)=5-4\cosh(Ly)>0
\qquad(0\le|y|<1/2),
\]

and it vanishes only at the horizontal strip boundaries. If
\(z=(s-1/2)/i\), then

\[
P(z)=4(1-4^{s-1})(1-4^{-s})
=-4^s(1-4^{1-s})(1-4^{-s}).
\]

Thus this is precisely the compact-Q4 factor paired with its critical adjoint,
up to a nonzero monomial.

For an integer \(m\ge0\), define

\[
\mathcal M_m(q,x)
=\sum_zm_z(z-x)^2e^{-q(z-x)^2}P(z-x)^{2m}.
\]

Under RH every summand is nonnegative. At a terminal pair \(t\pm iy\),

\[
-2y^2e^{qy^2}P(iy)^{2m}<0.
\]

Hence every fixed level is an RH criterion. The same remains true for any
integer profile \(m(q)=o(q)\). The proof splits nuisance zeros into a finite
bounded window, where terminality supplies a fixed exponent gap, and a Gaussian
tail. The multiplier ratio is only \(e^{o(q)}\).

## 4. Prime-side finite-difference theorem

The resident Hermite kernel is

\[
h_q(u)=\left(1-{u^2\over2q}\right)e^{-u^2/(4q)}.
\]

Let

\[
D_L=5I-2T_L-2T_{-L}.
\]

The filtered prime polynomial is exactly

\[
S_m(q,x)=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
(D_L^{2m}h_q)(\log n)n^{ix}.
\]

After critical conjugation, with \(H_q(u)=e^{u/2}h_q(u)\),

\[
e^{u/2}D_L^{2m}h_q(u)
=(I-T_L)^{2m}(4I-T_{-L})^{2m}H_q(u).
\]

The order-\(2m\) difference is load bearing. The exact shift coefficients have
vanishing moments through degree \(2m-1\), a property checked by the replay.

Chebyshev gives the shell transfer

\[
\sum_{n\ge2}{\Lambda(n)\over\sqrt n}|g(\log n)|
\ll\|e^{u/2}g\|_{W^{1,1}}.
\]

Gaussian-Hermite derivative bounds then give

\[
|S_m(q,x)|\ll_m e^{q/4}q^{3/2-m}
\]

for fixed \(m\), and for \(1\le m\le q/C_0\),

\[
|S_m(q,x)|
\le C_0e^{q/4}q^{3/2}
\left({C_0m\over q}\right)^m.
\]

These are pointwise carrier-uniform estimates. The only cancellation is the
explicit Q4 finite difference, applied before absolute values.

## 5. Archimedean reserve and pointwise positivity

The real-line multiplier obeys \(P(u)^{2m}\ge1\). Stirling therefore gives

\[
\operatorname{gamma}_m(q,x)
\ge c q^{-3/2}\log(2+|x|)-Ce^{Cm}q^{-3/2}.
\]

The pole term is Gaussian-small. Comparing the prime envelope with the reserve
shows positivity whenever

\[
{q\over4}-\log\log(2+|x|)
+{3\over2}\log q
-m\log{q\over C_0m}\to-\infty,
\qquad m=o(\log\log(2+|x|)).
\]

For fixed \(m\ge2\), this yields

\[
q\le4\ell(x)+(4m-6-\varepsilon)\log(2+\ell(x)).
\]

For

\[
m_*(q)=\left\lfloor{q\over\log\log q}\right\rfloor,
\]

it yields, for every \(\eta<16\),

\[
q\le4\ell(x)
+\eta{\ell(x)\log\log\log(3+\ell(x))
\over\log\log(3+\ell(x))}.
\]

Finally, for arbitrary \(\Delta(t)=o(t)\), use the monotone upper envelope

\[
\Delta^*(Q)=\sup_{1\le t\le Q}\Delta(t)=o(Q)
\]

and choose the least sublinear order satisfying

\[
m\log{q\over C_0m}
\ge {\Delta^*(q)\over4}+3\log q.
\]

This proves pointwise positivity throughout

\[
q\le4\ell(x)+\Delta(\ell(x)).
\]

## 6. Why this still does not prove RH

For

\[
G_{q,m}(z)=e^{-qz^2}P(z)^{2m},
\]

maximum modulus in the half-strip gives

\[
e^{qy^2}P(iy)^{2m}
\le\max\left\{9^{2m},
\sup_t e^{q/4-qt^2}|P(t+i/2)|^{2m}\right\}.
\]

For fixed \(m\), or \(m=o(q)\), the real boundary cannot dominate a fixed
terminal depth forever. Hence the critical shifted-line saddle envelope must be
at least as large as the retained terminal amplitude. A scalar analytic filter
cannot preserve the terminal pair and simultaneously create the fixed
exponential gap needed for a leading constant larger than four.

The remaining proof must therefore use information absent from an absolute
strip majorant:

```text
signed prime cancellation at the prescribed carrier;
bilinear dispersion with a genuinely pointwise amplifier;
carrier-specific Euler-product structure;
or a non-scalar positive observable that evades the scalar maximum-modulus wall.
```

## 7. Variance and the binding R-93254 firewall

For fixed \(m\), the coefficient energy remains

\[
V_m(q)=q+O_m(\sqrt q).
\]

The reason is that the energy scale is \(\log n\asymp\sqrt q\), where the
fixed Q4 shifts are infinitesimal after rescaling and \(D_L1=1\). Grouping all
powers of a prime still gives

\[
\sum_p|Y_{p,q,m}(x)|^2\ll_m q+1.
\]

A negative filtered carrier therefore forces

\[
\gg_m{\log^2|x|\over q+1}
\]

positively projecting prime blocks. This is an inverse theorem only. The new
pointwise gain came from finite-difference cancellation at the prime saddle,
not from the block count.

## 8. Input audit

The new positivity theorem uses only:

1. the frozen exact first-Hermite Guinand–Weil formula;
2. Chebyshev \(\psi(x)\ll x\);
3. Stirling for the archimedean density;
4. elementary Gaussian/Hermite derivative bounds;
5. finite differences and maximum modulus.

It does not use:

```text
RH-scale Chebyshev error;
macroscopic RH-strength Selberg integral;
CPBD;
pointwise square-root cancellation;
zero density to eliminate one point;
block cardinality as an upper bound.
```

## 9. Scientific boundary

```text
PR #498 centered cubic chain                  RECONSTRUCTED / CRITERION
CPBD                                            OPEN / RH-EQUIVALENT
Q4 critical-adjoint Hermite hierarchy           EXACT
fixed-level filtered RH criterion               PROPOSED COMPLETE
sublinear-order filtered RH criterion           PROPOSED COMPLETE
fixed-order log-log-log wedge gain               PROPOSED UNCONDITIONAL
all prescribed sublinear excesses above 4        PROPOSED UNCONDITIONAL
fixed positive leading-constant improvement      OPEN / SIGNED ARITHMETIC
scalar phase-blind filter-only closure            REFUTED AT STATED SCOPE
Riemann Hypothesis                               UNPROVEN
```
