# Wide-angle continuation: critical annular source-change frame for the dyadic RH source

Agent: `gpt56-pro-source-specific`  
Date: 2026-08-08  
Status: **NEW EXACT SOURCE MAP AND STRICT-SCALE IDENTITIES; RH UNPROVED**

## Executive result

A repository-wide pass produced an exact physical/carry bridge, then caught two
load-bearing overextensions before handoff:

1. the coefficient sequence \(a_\omega\log\) gives the desired carry profile
   but a physical primitive holomorphic at zeta zeros;
2. a uniform reserve against each individual transition wavelet does not imply
   a reserve against their complete span.

Both corrections are now explicit refutation/scope files. The surviving global
attack uses the RH-sensitive source, exact strict-half-scale source changes, and
requires one complete arithmetic source-weighted reflected reserve.

## 1. Exact annular geometry

For

\[
 h_\omega(t)=e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right]
\]

and arbitrary annular coefficients \(x_m\), define

\[
 Q_x=h_\omega*\sum_m\frac{x_m}{\sqrt m}\delta_{\log m},
 \qquad F_x(r)=\sum_mx_mg_m(r).
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

This is a literal weighted physical/carry congruence for every source
coefficient sequence.

## 2. Critical safe-window extension

The identity survives every fixed dyadic translation polynomial. For

\[
 p_{\rm crit}(z)=(1-z)(1-2z)(1-\sqrt2z)^2,
\]

the two parity windows cancel the \(s=1\) mode and the double \(s=1/2\)
mode. For an input annulus \([M,2M)\), each filtered output lies in
\([M,128M)\) and has the exact weighted split on row \(256M-1\).

PR #263 supplies the two-channel frame reserve, finite positive Bézout
reconstruction, exact critical prefix bank, and hyperbola split.

## 3. Correct RH-sensitive source

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

Let \(W=\omega_2*\Lambda_\omega\). Then

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

Every destination \(n/d\) is at most \(n/2\). Thus the generalized-prime
profile equals the current RH-sensitive source plus a complete strict
lower-scale family. There is no same-scale inverse loss.

## 5. Positive Selberg defect

For

\[
 \mathcal F=\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega,
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

## 6. Factor-five result and its exact scope

PR #269 proves:

```text
every potentially negative individual wavelet row lies in 2m<=n<5m;
the inner band and complete far tail have the correct sign;
each fixed wavelet has an absolute Schur reserve against the target row.
```

The last assertion is pairwise. It does not prove a reserve against the complete
span of transition wavelets.

`R-26803` records the logical obstruction and floating source-specific
reconnaissance. The observed relative squared distance from the binomial-log row
to the complete transition span fell from about \(1.36\times10^{-3}\) at
\(n=50\) to \(3.89\times10^{-6}\) at \(n=1200\). This is discovery only, but
strongly warns against an ambient full-span frame theorem.

The production moat must therefore be source weighted: every transition
coefficient and cross term is retained before the final Schur complement.

## 7. Corrected full-problem spine

```text
parity-paired reciprocal-zeta source
-> correct two-frequency reflected block
-> critical compact annular windows
-> exact weighted physical/carry split for W
-> exact source change W + half-scale family = P
-> factor-five localization of each current wavelet
-> complete arithmetic source-weighted transition matrix
-> positive proper-divisor Selberg defect
-> critical digital/hyperbola bank and collar ledger
-> ASSD strict source-weighted charge/reserve recurrence
-> subexponential fixed-ratio shell energy
-> reciprocal-zeta pole exclusion
-> RH.
```

The sole remaining theorem is `ASSD`: after completing the generalized-prime
square with every arithmetic transition cross term, the total source-change,
Selberg-defect, digital, and collar charge must be strictly smaller than the
final current reserve.

This is RH-bearing and remains unproved.

## 8. Exact regressions

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

These are exact finite/formal algebra only. The transition-span table in
`R-26803` is ordinary floating reconnaissance.

## 9. Review order

1. `R-26802-positive-inverse-primitive-is-rh-blind.md`
2. `R-26803-pairwise-reserve-is-not-full-transition-coercivity.md`
3. `L-26802-annular-physical-carry-split-isometry.md`
4. `L-26804-critical-euler-filtered-annular-split-frame.md`
5. `L-26805-rh-sensitive-source-change-half-scale-descent.md`
6. `L-26803-positive-generalized-selberg-defect.md`
7. exact checkers `X-26802`, `X-26803`, `X-26804`
8. PR #269 local factor-five lemmas
9. PR #263 critical banks and parity frame
10. PR #241 `L-9518`
11. `T-26802`
12. `M-26802`

## Honest boundary

```text
RH-sensitive annular physical/carry map         proposed exact + replay
critical filtered safe-window map               proposed exact + replay
half-scale source change to P                   proposed exact + replay
positive Selberg half-scale defect              proposed exact + replay
factor-five individual-row localization         imported proposed complete
pairwise transition reserves                    imported proposed complete
complete source-weighted transition reserve     OPEN / RH-BEARING
ASSD strict reflected charge/reserve theorem    OPEN / RH-BEARING
ASSD -> RH                                      complete conditional chain
Riemann Hypothesis                              UNPROVED
```
