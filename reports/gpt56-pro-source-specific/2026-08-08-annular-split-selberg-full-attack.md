# Wide-angle continuation: critical annular split frame for the dyadic RH source

Agent: `gpt56-pro-source-specific`  
Date: 2026-08-08  
Status: **NEW EXACT SOURCE MAP AND SOURCE-CHANGE DESCENT; RH UNPROVED**

## Executive result

A fresh repository-wide pass found an exact physical/carry bridge, then caught
and corrected a load-bearing source mismatch before handoff.

The geometry is valid for every coefficient sequence. The RH-sensitive
physical source uses coefficients \(\Lambda_\omega\), not
\(a_\omega\log\). The latter gives the generalized-prime carry profile but its
physical primitive is holomorphic at zeta zeros.

The correction yields an additional exact theorem:

\[
 a_\omega*(\omega_2*\Lambda_\omega)=\Lambda_\omega.
\]

Thus the RH-sensitive carry feature differs from the already-reserved
PR #269 profile only by a complete proper-divisor family at scale at most one
half.

## 1. Exact annular geometry

For

\[
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right]
\]

and any annular coefficients \(x_m\), define

\[
 Q_x=h_\omega*
 \sum_m\frac{x_m}{\sqrt m}\delta_{\log m},
 \qquad
 F_x(r)=\sum_mx_mg_m(r).
\]

Then

\[
 Q_x(t)=e^{-t/2}F_x(r)
 \quad(\log r\le t<\log(r+1)).
\]

If \(x\) is supported on \([M,2M)\), then on row \(N=16M-1\),

\[
 \boxed{
 \|Q_x\|_2^2
 =\sum_{j=1}^{8M-1}
 \frac{|F_x(N)-F_x(j)-F_x(N-j)|^2}{j(j+1)}.
 }
\]

This is a literal weighted physical/carry congruence.

## 2. Critical safe-window extension

The identity survives every fixed dyadic translation polynomial. For

\[
 p_{\rm crit}(z)=(1-z)(1-2z)(1-\sqrt2z)^2,
\]

the two parity windows cancel the \(s=1\) mode and the double \(s=1/2\)
mode. For an input annulus \([M,2M)\), each filtered output lies in
\([M,128M)\) and has the exact weighted split on row \(256M-1\).

PR #263 supplies the two-channel frame reserve and finite positive Bézout
reconstruction.

## 3. Source correction

The specialization

\[
 x_m=a_\omega(m)\log m
\]

has carry image

\[
 P_n(j)=\sum_q\Lambda_\omega(q)\chi_{n,q}(j),
\]

but its physical transform is

\[
 \frac{-\zeta'(s)+\zeta(s)E'(s)/E(s)}s,
\]

which is holomorphic at every zeta zero. It is not an RH detector.

The RH-sensitive physical choice is

\[
 \boxed{x_m=\Lambda_\omega(m).}
\]

Its carry image is

\[
 \mathcal W_N(j)
 =\sum_q(\omega_2*\Lambda_\omega)(q)\chi_{N,q}(j),
\]

and its transform retains every logarithmic-derivative pole of zeta.

## 4. Exact half-scale source change

Let

\[
 W=\omega_2*\Lambda_\omega.
\]

Then

\[
 \boxed{a_\omega*W=\Lambda_\omega.}
\]

Coefficientwise,

\[
 \boxed{
 W(n)=\Lambda_\omega(n)
 -\sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)W(n/d).
 }
\]

Every destination \(n/d\) is at most \(n/2\). Thus the source with the known
carry reserve equals the current RH-sensitive source plus a complete strict
lower-scale family. There is no same-scale inversion loss.

## 5. Positive Selberg defect

For

\[
 \mathcal F
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega,
\]

one has

\[
 \boxed{
 a_\omega(n)\log^2n-\mathcal F(n)
 =\sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)\mathcal F(n/d)
 \ge0.
 }
\]

This second proper-divisor family also lies at strict half scale. The
source-change and Selberg-defect rows use the same positive inverse coefficients
and must be assembled in one reflected ledger.

## 6. New full-problem spine

```text
parity-paired reciprocal-zeta source
-> correct two-frequency reflected block
-> critical compact annular windows
-> exact weighted physical/carry split for W
-> exact source change W + half-scale family = P
-> factor-five localization and strict carry reserve for P
-> positive proper-divisor Selberg defect
-> complete digital and collar ledger
-> ASSD strict charge/reserve recurrence
-> subexponential fixed-ratio shell energy
-> reciprocal-zeta pole exclusion
-> RH.
```

The sole remaining theorem is `ASSD`: after completing the reserved `P` square,
the total source-change, Selberg-defect, digital, and collar charge must be
strictly smaller than the current reflected reserve.

This is RH-bearing and remains unproved.

## 7. Exact regressions

```text
X-26802
EXACT_ANNULAR_SPLIT_AND_SELBERG_DEFECT_VERIFIED
compact floor rows                  650
split rows                       49,710
weighted isometries                  10
formal Selberg rows                  64
positive defect rows                 64

X-26803
EXACT_CRITICAL_FILTERED_ANNULAR_SPLIT_VERIFIED
filtered rows                     4,600
weighted isometries                  8

X-26804
EXACT_RH_SENSITIVE_SOURCE_CHANGE_HALF_SCALE_VERIFIED
source-change rows                  128
proper-divisor destinations         517
```

These are exact finite/formal algebra only.

## 8. Review order

1. `R-26802-positive-inverse-primitive-is-rh-blind.md`
2. `L-26802-annular-physical-carry-split-isometry.md`
3. `L-26804-critical-euler-filtered-annular-split-frame.md`
4. `L-26805-rh-sensitive-source-change-half-scale-descent.md`
5. `L-26803-positive-generalized-selberg-defect.md`
6. exact checkers `X-26802`, `X-26803`, `X-26804`
7. PR #269 `L-26901`--`L-26903`
8. PR #241 `L-9518`
9. PR #263 parity frame
10. `T-26802`
11. `M-26802`

## Honest boundary

```text
RH-sensitive annular physical/carry map       proposed exact + replay
critical filtered safe-window map             proposed exact + replay
half-scale source change to reserved profile  proposed exact + replay
positive Selberg half-scale defect            proposed exact + replay
factor-five localization/reserve for P         imported proposed complete
ASSD strict reflected charge/reserve theorem  OPEN / RH-BEARING
ASSD -> RH                                    complete conditional chain
Riemann Hypothesis                            UNPROVED
```
