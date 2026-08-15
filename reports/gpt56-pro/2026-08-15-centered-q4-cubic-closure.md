# Centered-Q4 cubic closure and the common First-Hermite prime-coherence frontier

**Date:** 2026-08-15  
**Status:** proposed research packet; independent review required  
**RH status:** unproved  
**Branch base:** PR #483 at `87bd7ad2127f98b6141b4c03355556f2b95f6404`

## 1. Objective

This pass returned to the two lanes joined on PR #483:

1. First-Hermite heat at one exceptional carrier;
2. complete compact-Q4 endpoint energy after prime-base grouping.

The requested target was the aligned-prime-block / distinct-prime boundary, especially the square-root major arc. The main result is a reformulation that removes a previously load-bearing part of that boundary:

\[
\boxed{\text{the Q4 mean coordinate is unnecessary.}}
\]

A fixed mean-zero Bernoulli projection of the centered Q4 field is itself a zero-safe RH detector. Consequently, the Q4 route reduces to **nonzero** distinct-prime major modes only.

The same projection is one scalar sum of complete prime-tower blocks, so the Q4 and First-Hermite endgames now share the same one-dimensional projective normal form.

## 2. Frozen genealogy

```text
PR #483
87bd7ad2127f98b6141b4c03355556f2b95f6404
prime-block coherence for First-Hermite and Q4

PR #474
0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b
Q4 diagonal O(log N) and square-root major-arc localization

PR #392
d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4
linear-resolution First-Hermite density-one theorem

PR #390
ea20af8867c3119c23efc27738d343aac2f79362
First-Hermite prime-block moments

PR #383
d764be15bd8ea902ad260484eab44d19a9e82175
Q4 Fourier/Haar/character coordinates and R-90412
```

The factor-67 review/proposal line through #488/#489 was inspected only for live genealogy and is not imported.

The packet explicitly respects `R-90412`: the macroscopic critical Selberg estimate formerly used to close all nonmean Haar modes is RH-strength and is not an unconditional input.

## 3. The new centered Bernoulli projection

For the complete Q4 field \(Q_{\circ,N}\), put

\[
w(\theta)=\theta(1-\theta)-\frac16=-B_2(\theta).
\]

This weight is symmetric, has mean zero, and satisfies

\[
\int_0^1w^2=\frac1{180}.
\]

Define

\[
\mathcal A_\circ(N)
=\int_0^1w(\theta)Q_{\circ,N}(\theta)d\theta.
\]

Because \(w\) is mean zero, it sees only the centered field. Therefore

\[
|\mathcal A_\circ(N)|^2
\le\frac{N}{180}\mathscr V_\circ(N),
\]

where

\[
\mathscr V_\circ(N)
=\frac1N\int_0^1|Q_{\circ,N}-M_N|^2.
\]

The exact arithmetic kernel is

\[
K(x)=2\int_0^xw(u)du
=\frac{x(1-x)(2x-1)}3.
\]

Reversing the endpoint prefixes gives, with no limiting argument,

\[
\boxed{
\mathcal A_\circ(N)
=\sum_{m\le N}c_\circ(m)K(m/N).
}
\]

This identity was checked on arbitrary rational sources. The checker deliberately mutates the reflected predecessor \(N-j-1\) to \(N-j\); the identity then fails.

## 4. Zero-safe Mellin transform

The cubic kernel has the rational Mellin multiplier

\[
\widehat K(s)
=\frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

Hence

\[
\begin{aligned}
\int_1^\infty\mathcal A_\circ(X)X^{-s-1}dX
={}&
\frac{s-1}{3(s+1)(s+2)(s+3)}
\\
&\times
\left[
(1-4^{1-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
+3(\log4)\frac{4^{-s}}{1-4^{-s}}
\right].
\end{aligned}
\]

Every nontrivial open-strip zero survives:

- the cubic multiplier vanishes only at \(s=1\);
- \(1-4^{1-s}=0\) forces \(\Re s=1\);
- \(1-4^{-s}=0\) forces \(\Re s=0\);
- the cubic poles are at \(-1,-2,-3\).

The real-endpoint scalar differs from its nearest integer endpoint by \(O(1)\), using \(\|K'\|_\infty\le1/3\) and

\[
\sum_{m\le N}m|c_\circ(m)|\ll N^2.
\]

Thus integer endpoint bounds legitimately feed the Mellin integral.

## 5. Centered Q4 is RH-equivalent

Under RH, von Koch gives

\[
R_N(j)\ll\sqrt N\log^2N
\]

uniformly, so

\[
\mathscr V_\circ(N)\ll\log^4N.
\]

Conversely, if

\[
\mathscr V_\circ(N)\ll\log^A N,
\]

then the Bernoulli projection satisfies

\[
\mathcal A_\circ(N)
\ll\sqrt N\log^{A/2}N.
\]

Endpoint interpolation gives the same bound for real \(X\), so the Mellin transform is holomorphic in \(\Re s>1/2\). The exact formula above then excludes every zeta zero in that half-plane. Functional-equation symmetry gives RH.

Therefore

\[
\boxed{
\mathrm{RH}
\iff
\mathscr V_\circ(N)\ll\log^A N
\text{ for some fixed }A.
}
\]

This is stronger than the earlier direct endpoint consumer at the level of route architecture: it proves that the mean is not required to preserve the zeta poles.

## 6. Mean-free distinct-prime major arc

Center each PR #483 prime row:

\[
\widetilde R_{N,p}
=R_{N,p}-m_{p,N}\mathbf1.
\]

Then

\[
R_N-M_N\mathbf1
=\sum_p\widetilde R_{N,p}.
\]

Centering affects only the zero Fourier coordinate. Importing the exact safe estimates of PR #474 gives

```text
centered complete prime diagonal / N^2 <= 720 log(2N);
absolute distinct-prime minor arc      <= 744 log(2N).
```

Let \(\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)\) contain only the nonzero modes with

\[
d_N(a)=\min(a,N-a)<\lceil\sqrt N\rceil.
\]

Then

\[
\boxed{
\left|
\mathscr V_\circ(N)
-\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)
\right|
\le1464\log(2N).
}
\]

Combining this with the centered-energy theorem gives the new direct criterion

\[
\boxed{
\mathrm{RH}
\iff
\left|
\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)
\right|
\ll\log^A N.
}
\]

The remaining Q4 object now contains:

```text
no zero mode;
no same-prime term;
no minor-arc term;
fewer than 2 sqrt(N)+O(1) nonzero modes;
reduced additive modulus > sqrt(N).
```

This is the main route advance.

## 7. One-dimensional prime-block form

Write

\[
\mathcal A_\circ(N)=\sum_pZ_{p,N},
\qquad
Z_{p,N}=\sum_mc_{\circ,p}(m)K(m/N).
\]

The sharpened complete-tower accounting of PR #474 gives

\[
\sum_pA_{p,N}^2\le80N\log(2N),
\]

while

\[
\|K\|_\infty^2=\frac1{972}.
\]

Therefore

\[
\boxed{
\sum_p|Z_{p,N}|^2
\le\frac{20}{243}N\log(2N).
}
\]

Any large cubic obstruction is consequently pure distinct-prime coherence in one complex dimension.

This is exactly parallel to PR #483's First-Hermite block form:

\[
S_{q,a}(t)=\sum_pY_{p,q,a}(t),
\qquad
\sum_p|Y_{p,q,a}(t)|^2\ll q+1.
\]

A negative heat carrier forces

\[
\frac{|S_{q,a}(t)|^2}
{\sum_p|Y_{p,q,a}(t)|^2}
\gg\frac{\log^2T}{q+1}.
\]

An off-line zero forces the cubic Q4 coherence ratio to grow polynomially along an endpoint sequence.

Thus both routes reduce to

\[
\kappa(v)
=\frac{|\sum_pv_p|^2}{\sum_p|v_p|^2}.
\]

The arithmetic block geometry differs, but the abstract obstruction is now identical.

## 8. Candidate-complete producer

Define Cubic Prime-Block Decorrelation (CPBD):

\[
\left|\sum_pZ_{p,N}\right|^2
\ll N\log^B N
\]

for one fixed \(B\), uniformly in \(N\).

Every downstream interface is now closed:

\[
\mathrm{CPBD}
\Longrightarrow
|\mathcal A_\circ(N)|\ll\sqrt N\log^{B/2}N
\Longrightarrow
\text{zero-free }\Re s>1/2
\Longrightarrow
\mathrm{RH}.
\]

RH conversely implies CPBD with \(B=4\). Hence CPBD is an exact complete arithmetic closure interface, not an independently proved estimate.

Equivalent producer coordinates are:

1. the cubic scalar;
2. its distinct-prime scalar cross term;
3. the mean-free nonzero square-root major arc;
4. the independent First-Hermite one-carrier positivity theorem.

## 9. Hostile checks and failed shortcuts

### Cardinality is not enough

The synthetic family \(v_1=\cdots=v_M=1\) has

\[
E=M^2,\qquad D=M,\qquad E/D=M,
\]

and saturates every positive-block and rank-one-cross lower bound. Therefore the stronger PR #483 heat count is an inverse theorem, not a contradiction.

### Macroscopic Selberg is not imported

`R-90412` remains normative. An \(Xh\operatorname{polylog}X\) Selberg integral uniformly through \(h\asymp X\) would already carry critical prime-error information.

### Generic large sieve is not enough

The first low additive mode remains RH-bearing. Averaging over many moduli cannot remove the modulus-\(N\) family with \((a,N)=1\).

### Mean removal is genuine

The new Mellin consumer uses a mean-zero test vector and a nonzero cubic multiplier. It does not smuggle the old mean back through endpoint interpolation or a constant Fourier coefficient.

## 10. Exact replay

```bash
cd experiments/X-93250-centered-q4-cubic
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_X_93250_CENTERED_Q4_CUBIC
```

Coverage:

```text
205   exact arbitrary-source projection identities
205   exact centered Cauchy inequalities
596   formal Q4 source coefficients
596   prime-row reconstruction checks
14    centered Gram identities
179   scalar prime-diagonal checks
79    sharp coherence-firewall fixtures
702   hostile mutations detected
```

The checker is exact rational arithmetic. It does not authenticate the analytic zeta imports or CPBD.

## 11. Final boundary

```text
Bernoulli/cubic centered projection          PROPOSED COMPLETE
cubic Mellin zero safety                     PROPOSED COMPLETE
centered Q4 energy <=> RH                     PROPOSED COMPLETE
mean-free distinct-prime major-arc criterion PROPOSED COMPLETE
cubic complete-tower diagonal O(N log N)     PROPOSED COMPLETE
common heat/Q4 coherence normal form         PROPOSED COMPLETE
cardinality-only shortcut                    REFUTED
CPBD / deterministic prime decorrelation     OPEN / RH-BEARING
First-Hermite one-carrier exclusion          OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
