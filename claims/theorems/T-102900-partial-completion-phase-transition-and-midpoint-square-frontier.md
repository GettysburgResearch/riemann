# T-102900 — Partial-completion phase transition and the geometric-midpoint square frontier

Claim ID: `T-102900`  
Status: **MAJOR UNCONDITIONAL PHASE-TRANSITION THEOREM; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

The completion programme has a sharp analytic transition at the native
endpoint.

## 1. Every strict completion is eventually positive

For

\[
0<c<1,
\]

let \(\gamma_c\) have labelled Euler factors

\[
(1-p^{-z})(1+c p^{-z})
\]

and let \(H_c\) be its observation through the fixed centered outer kernel
\(R_L\).

`L-102891` proves the unconditional asymptotic

\[
\boxed{
H_c(X)
=
K_c\sqrt X(\log X)^{c-2}
\left(1+O_c(1/\log X)\right),
\qquad K_c>0.
}
\tag{T-102900.1}
\]

Hence every fixed strict positive completion is eventually positive.

At the arithmetic midpoint,

\[
H_{1/2}(X)
\sim
\frac{2(3-2\sqrt2)\log2}{\sqrt\pi}
G_{1/2}(1)
\frac{\sqrt X}{(\log X)^{3/2}}>0.
\tag{T-102900.2}
\]

No Möbius cancellation theorem at the RH scale is used.

## 2. A canonical eventually positive geometric half-source

Let \(\lambda*\lambda=\beta\), let \(\lambda^\square\) be its square lift,
and put

\[
\eta=\lambda*\lambda^\square.
\]

Then

\[
\boxed{
\eta*\eta=\beta*\beta^\square.
}
\tag{T-102900.3}
\]

The source \(\eta\) is the exact geometric midpoint between the native and
squared Euler factors.  `L-102892` proves

\[
\boxed{
H_\eta(X)
=
K_\eta\frac{\sqrt X}{(\log X)^{3/2}}
\left(1+O(1/\log X)\right),
\qquad K_\eta>0.
}
\tag{T-102900.4}
\]

Thus one fixed eventually positive half-source has an exact arithmetic square
which contains the complete native detector.

## 3. Positive recovery of the native source

Let

\[
\sum_d\omega(d)d^{-z}
=
\frac{\zeta(2z)}{1-67^{-2z}}.
\]

Then \(\omega(d)\ge0\),

\[
\omega*(\eta*\eta)=\beta,
\]

and

\[
\sum_{d\le Y}\frac{\omega(d)}{\sqrt d}
\ll\log(2Y).
\]

If \(\mathscr S_\eta\) denotes the fixed outer observation of
\(\eta*\eta\), then

\[
\boxed{
H_\beta(X)
=
\sum_d\frac{\omega(d)}{\sqrt d}
\mathscr S_\eta(X/d).
}
\tag{T-102900.5}
\]

Consequently

\[
\boxed{
\int_1^Y(H_\beta)_-\frac{dX}{X}
\ll
\log(2Y)
\int_1^Y(\mathscr S_\eta)_-\frac{dX}{X}.
}
\tag{T-102900.6}
\]

Define

```text
GMBC102893:
  the arithmetic geometric-midpoint square observation S_eta has subpower
  logarithmic negative mass in the fixed outer kernel.
```

Then

\[
\boxed{
\mathrm{GMBC}_{102893}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-102900.7}
\]

This gives a second exact route beside the stopped small-gcd current
`SGIC102890`.

## 4. The sharp phase transition

For every fixed \(c>0\), the real branch at \(s=1/2\) dominates and forces
eventual positivity.  At \(c=0\), its Selberg–Delange coefficient vanishes:

\[
\frac1{\Gamma(-1)}=0.
\]

The real branch becomes the analytic reciprocal-zeta zero at \(z=1\), and
every hypothetical off-line zeta zero again survives in the fixed detector.

Thus

\[
\boxed{
\text{strict completion: unconditional positive tail;}
\qquad
\text{native endpoint: RH-bearing.}
}
\tag{T-102900.8}
\]

`R-102870` is binding.  The positive half-source is not itself the detector,
and its arithmetic source square is not a pointwise scalar square.

## 5. Research meaning

The remaining arithmetic difficulty has acquired two compatible exact
coordinate systems:

```text
stopped-prime / all-chaos coordinate:
  SGIC102890;

geometric-midpoint square coordinate:
  GMBC102893.
```

The first exposes gcd, owner and phase geometry.  The second exposes a canonical
unconditionally positive half-source and a positive square-lattice inverse.
A source-faithful theorem transferring the midpoint tail sign through its
arithmetic square would close the fixed native detector.

## Exact boundary

```text
strict partial-completion asymptotic          PROVED
strict partial-completion eventual sign       PROVED POSITIVE
geometric midpoint source factorization       PROVED EXACT
geometric midpoint eventual sign              PROVED POSITIVE
positive square-lattice inverse                PROVED EXACT / POLYLOG
GMBC102893 midpoint-square negative mass       OPEN / RH-BEARING
SGIC102890 stopped coherent negative mass      OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
