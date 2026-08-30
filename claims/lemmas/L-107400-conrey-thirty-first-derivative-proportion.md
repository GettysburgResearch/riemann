# L-107400 — Conrey's variational functional gives \(\alpha_{31}>999/1000\)

Claim ID: `L-107400`  
Programme aliases: `XI90.HIGH_ODD_ENDPOINT`, `XI.CONREY31`  
Status: **PROVED UNCONDITIONALLY FROM THE RECONSTRUCTED CONREY FUNCTIONAL**  
Created: 2026-08-30  
Depends on: `L-104602`; Conrey 1983 mean-square theorem  
Programme issue: #744  
RH status: **not assumed**

Retain the unconditional variational implication of `L-104602`:

\[
\alpha_m>
1-\frac{\log\mathcal F_m(R,\phi)}R.
\tag{L-107400.1}
\]

Take

\[
m=31,\qquad R=1,\qquad \phi(x)=1-x.
\]

Then

\[
q_{31}(x)=(1-x)(1-2x)^{31}.
\]

The exact rational-interval replay evaluates the two weighted polynomial
integrals in Conrey's functional and proves

\[
\boxed{
\mathcal F_{31}(1,1-x)<e^{1/1000}.
}
\tag{L-107400.2}
\]

Consequently

\[
\boxed{
\alpha_{31}>\frac{999}{1000}.
}
\tag{L-107400.3}
\]

Here \(\alpha_{31}\) is the short-window lower proportion of zeros of
\(\xi^{(31)}\) on the critical line in Conrey's normalization.

No numerical zero data and no RH assumption enter the proof. The replay uses
exact rational arithmetic; exponential and square-root bounds are enclosed by
one-sided Taylor and integer-square certificates.

## Why order 31 is useful

For an odd endpoint block of order \(K\), the carrier-adapted Xi source
constant is \(1/(2K)\), proved in `L-107401`. At \(K=31\),

\[
\frac1{2K}=\frac1{62},
\]

while the exact \(90\%\) endpoint allowance from (L-107400.3) is

\[
\frac{999}{1000}-\frac9{10}
=\frac{99}{1000}.
\]

The remaining quantitative margin is therefore

\[
\boxed{
\frac{99}{1000}-\frac1{62}
=
\frac{2569}{31000}
>0.0828.
}
\tag{L-107400.4}
\]

This is much wider than the fifth-endpoint source budget.

## Scope

The lemma proves the high endpoint proportion only. It does not transport the
source-soft Fourier density through the physical all-pass quotient or pay its
topological unit spectrum.
