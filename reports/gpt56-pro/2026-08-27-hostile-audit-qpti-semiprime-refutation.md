# Hostile audit of the QPTI semiprime-main refutation

Date: 2026-08-27  
Audited remote head: `e59109975bd251c0095ce1d15207b328bbfe499c`  
PR: #719  
Primary files: `L-103121`, `R-103121`, `T-103130`  
Disposition: **THE REFUTATION IS SOUND AT ITS STATED SCOPE; RH REMAINS UNPROVED**

This is a second-agent audit of the binding correction that refutes the literal
quarter-power Euler--Beta gate. It creates no new RH claim and does not promote
the restored native wavelet frontier to a theorem.

## 1. Core-mass sign

The live-core coefficient is

\[
D_{\ge 2}
=\sum_{\substack{c\ge1\\\mu^2(c)=1\\\omega(c)\ge2}}
\frac{\mu(c)}{\binom{\omega(c)+2}{2}c^2}.
\]

Using

\[
\binom{k+2}{2}^{-1}=2\int_0^1(1-\theta)\theta^k\,d\theta
\]

and the absolutely convergent Euler product gives

\[
D_{\ge2}
=2\int_0^1(1-\theta)
\left[
\prod_p\left(1-\frac{\theta}{p^2}\right)
-1+\theta\sum_p\frac1{p^2}
\right]d\theta.
\]

For `0<theta<=1`, the bracket is strictly positive: the elementary finite
product inequality

\[
\prod_j(1-a_j)\ge1-\sum_j a_j
\]

is strict once at least two of the positive `a_j` are present, and the passage
to the infinite product is justified by absolute convergence. Hence
`D_{>=2}>0`. This part of `L-103121` is exact and does not use RH.

## 2. Detector moment

For the corrected bounded derivative-outer detector,

\[
\widehat K_L(s)
=\frac{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})}
{s(s-1/2)}.
\]

At `s=1/2`, the final numerator factor cancels the denominator zero to first
order, with quotient `log 2`. Substitution in the remaining factors gives

\[
\widehat K_L(1/2)=-(2-\sqrt2)^2\log2<0.
\]

Thus the first squarefree-semiprime density coefficient is strictly negative:

\[
D_{\ge2}\widehat K_L(1/2)<0.
\]

The sign and normalization in `L-103121` check out.

## 3. Semiprime transfer and varying-core summation

The imported input is the classical squarefree-semiprime asymptotic

\[
A_2(Z)=\#\{p<q:pq\le Z\}
\sim Z\frac{\log\log Z}{\log Z}.
\]

For a compactly supported bounded-variation kernel, Stieltjes partial
summation on a fixed multiplicative interval gives

\[
\sum_{p<q}\frac1{\sqrt{pq}}K\left(\frac Z{pq}\right)
=\widehat K(1/2)\sqrt Z\frac{\log\log Z}{\log Z}(1+o(1)).
\]

Deleting the finitely many primes dividing a fixed core does not alter the
leading term. The passage from fixed core to all squarefree cores is also
legitimate by the three-range split in `R-103121`:

```text
c <= C;                 fixed-core asymptotic;
C < c <= X^eta;         semiprime upper bound and sum_{c>C} c^{-2};
c > X^eta;              support plus a trivial weighted semiprime bound.
```

For `eta<1/4`, the middle range has the required uniform logarithmic scale,
and the last range is `O(X^(1/2-eta))`, negligible relative to
`sqrt(X) loglog(X)/log(X)`. Absolute convergence of the core coefficient then
permits `X -> infinity` followed by `C -> infinity`.

Consequently the displayed asymptotic

\[
H_{\rm EB}(X)
=-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
\qquad
C_0=D_{\ge2}(2-\sqrt2)^2\log2>0,
\]

is supported by the stated input. Its dyadic logarithmic negative mass is
therefore power-sized. A field whose logarithmic `L1` mass is `Y^o(1)` cannot
cancel it.

## 4. Binding disposition

The audit supports the following exact status:

```text
finite Euler--Beta owner-core algebra                    RETAINED EXACT
live-core mass sign                                      PROVED POSITIVE
bounded-detector semiprime moment                        PROVED NEGATIVE
literal Euler--Beta current semiprime asymptotic         PROVED
EBD103120                                                 REFUTED
QPTI103112 as the declared completed field               REFUTED
completed-source QPTI <=> BCI <=> HMO chain              WITHDRAWN
BCI102990 and HMO102940 themselves                       REOPENED FOR SOURCE AUDIT
Riemann Hypothesis                                       UNPROVED
```

This refutes a stronger producer criterion, not RH.

## 5. Native-wavelet normalization firewall

The restored non-refuted front door in `T-103130` is the ordinary same-`K1`
Möbius wavelet

\[
G_1(X)=\sum_n\frac{\mu(n)}{\sqrt n}K_1(X/n),
\]

whose Mellin-side Euler factor is `1/zeta(s+1/2)`. This is the normalization
that must be retained in subsequent source-faithful audits.

It must not be silently replaced by a squared-core expression such as

\[
\sum_n\frac{\mu(n)}n K(X/n^2)
\]

unless an explicit source-exact change-of-variables and kernel theorem is
proved. The two presentations have different Mellin variables and can carry
different deterministic density modes. This distinction is load-bearing in
view of the QPTI failure.

`L-102885` does prove that the derivative outer detector and the corrected
same-`K1` detector are fixed differential coordinates on the same literal
stopped source. It does **not** prove that differentiation preserves one-sided
logarithmic mass, so no reverse one-sided estimate may be inferred from the
kernel identity alone.

## 6. Correct continuation target

The honest conclusion-facing task is now

```text
OPEN.ARITH.XD:
  prove critical signed cross-core dispersion for the native ordinary-Mobius
  same-K1 wavelet after exact carrier/Vaughan recombination.
```

A valid continuation must preserve the native source coefficient, the same
compact detector, and the order of global recombination before absolute
values. It must not reintroduce the refuted pair-owned Euler--Beta completion.

## Final audit verdict

```text
R-103121 asymptotic refutation       ACCEPT AT STATED SCOPE
T-103130 reset                       ACCEPT WITH NORMALIZATION FIREWALL ABOVE
new proof of RH                      NOT CLAIMED
remaining native signed estimate     OPEN / RH-BEARING
```
