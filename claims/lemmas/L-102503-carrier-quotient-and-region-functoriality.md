# L-102503 — Exact carrier quotient and simultaneous region functoriality

Claim ID: `L-102503`  
Status: **PROVED EXACT COMPOSITION THEOREM**  
Created: 2026-08-22  
Depends on: `L-102500`  
RH status: **not assumed**

Let `F=P+R` be any exact finite labelled mother-source partition, where `P` is
a deterministic carrier packet and `R` is the retained remainder. Put

\[
A=\partial_u,
\qquad
B=\frac12(\partial_u+\tfrac32).
\]

Then

\[
AF=AP+AR,
\qquad
BF=BP+BR.
\]

Define

\[
\widetilde C=AF-AP,
\qquad
\widetilde X=BF-BP.
\]

The exact Bezout identity gives

\[
\boxed{
\widetilde C=AR,
\qquad
\widetilde X=BR,
\qquad
R=-\frac23\widetilde C+\frac43\widetilde X.
}
\tag{L-102503.1}
\]

Thus a prime, semiprime, homogeneous, or any other explicitly selected carrier
is removed once at the mother level and automatically propagated to both
channels. No asymptotic subtraction is used.

## 1. Exact chaos bookkeeping

Expanding the labelled Euler product gives

\[
F=\sum_{k\ge0}F^{[k]},
\]

where `F^[k]` contains exactly the labelled subsets of cardinality `k`. Any
finite union of chaos levels may be selected as `P`; its compensating
coordinate remains present until the complete physical scalar is recombined.

## 2. Region functoriality

Suppose the common mother has the exact source partition

\[
F=F_{\rm small}+F_{\rm meso}+F_{\rm bal}+F_{\rm act}+F_{\rm fin}.
\tag{L-102503.2}
\]

Because `A`, `B`, multiplicative shifts, finite Euler squaring, endpoint
restriction, and positive dilation renewal commute at source level, both
channels inherit the same partition:

\[
AF=\sum_\mathcal R AF_\mathcal R,
\qquad
BF=\sum_\mathcal R BF_\mathcal R.
\tag{L-102503.3}
\]

This is the exact interface for the assignments

```text
small primes          finite Euler squaring;
mesoscopic products   Dickman/Stieltjes/Bellman;
balanced coprime      same-K1 Vaughan/half-divisor;
activation knots      Volterra/Farkas;
finite terminal       finite certificates only.
```

The theorem supplies equality and one-use ownership. It does not supply the
open arithmetic estimates in the mesoscopic or balanced regions.

## 3. Moving cutoffs

For

\[
\mathscr A_Z=\prod_{p\le Z}(I+p^{-1/2}U_p),
\]

crossing a prime `p` gives

\[
\boxed{
\mathscr A_pF-\mathscr A_{p^-}F
=p^{-1/2}U_p\mathscr A_{p^-}F.
}
\tag{L-102503.4}
\]

For a moving cutoff this jump is an atomic source term in the scale derivative.
Applying `A` or `B` to the continuous packet does not erase it.

## 4. Physical collapse

Let `C_phys` set all labelled phases to zero and combine equal products. Then

\[
\boxed{
\mathcal C_{\rm phys}A=A\mathcal C_{\rm phys},
\qquad
\mathcal C_{\rm phys}B=B\mathcal C_{\rm phys}.
}
\tag{L-102503.5}
\]

No contractivity of physical collapse is claimed. The channel identities and
determinant formula are instead re-established directly on the collapsed real
field, avoiding a source-blind norm inequality.
