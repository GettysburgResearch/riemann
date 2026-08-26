# L-105483 — Historical unregularized analytic-square coordinate

Claim ID: `L-105483`

Status: **WITHDRAWN AND SUPERSEDED BY `L-105490--L-105493`**

Created: 2026-08-26

Corrected: 2026-08-26

The following parts of the historical file remain valid:

```text
the finite Boolean-normal-ordered analytic source amplitude;
the distributional formula for P(D)J;
Cauchy in the Beta parameter at finite labelled-source scope.
```

The historical Plancherel step and the gates

```text
F1ASQ2_105483
F1FOURTH105483
```

are withdrawn.

The omitted multiplier was

\[
(5s+\tfrac32)(1-\sqrt2\,2^{-s})/4.
\]

Without its inverse, the proposed weight

\[
|P(\tfrac14+it)|^2r_A(t)^4
\]

is asymptotically constant. Its integral against the squared modulus of any
nonzero finite Dirichlet polynomial is infinite; see `R-105490`.

The corrected bounded-current weight is

\[
\Omega_K(t)=
\frac{
16|P(\tfrac14+it)|^2r_A(t)^4
}{
((\tfrac{11}{4})^2+25t^2)
(1+\sqrt2-2\,2^{1/4}\cos(t\log2))
}
\asymp(1+t^2)^{-1}.
\]

The replacement gates are

```text
F1KASQ105492
F1KFOURTH105493
```

with the exact implication chain in `T-105490`.

No historical assertion from this file may be used without the correction.
RH remains unproved.
