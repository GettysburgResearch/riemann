# L-24533 — Möbius pairing of every central carry row is the constant `-1`

Claim ID: `L-24533`  
Title: The exact Möbius Riesz coordinate of a completed central cascade is `log X` minus the total central coefficient mass, equivalently `log X` minus the sum of the bottom residual values  
Status: **PROPOSED COMPLETE — exact finite algebra**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `L-24523`; elementary Möbius inversion  
Scope: scalar collapse of the fully dyadically filtered eta/Mersenne ledger

## 1. Möbius divisor prefix

For every real `x>=1`,

\[
\sum_{q\le x}\mu(q)\left\lfloor{x\over q}\right\rfloor=1.
\tag{L-24533.1}
\]

Indeed, divisor switching gives

\[
\sum_{q\le x}\mu(q)\left\lfloor{x\over q}\right\rfloor
 =\sum_{n\le x}\sum_{q\mid n}\mu(q)
 =1.
\]

## 2. Constant central-row image

For the central split

\[
n=\lfloor n/2\rfloor+\lceil n/2\rceil
\qquad(n\ge2),
\]

let

\[
\chi_n^{\rm c}(q)
 =\left\lfloor{n\over q}\right\rfloor
  -\left\lfloor{\lfloor n/2\rfloor\over q}\right\rfloor
  -\left\lfloor{\lceil n/2\rceil\over q}\right\rfloor.
\]

Using (L-24533.1) at the parent and both positive children gives

\[
\begin{aligned}
\sum_{q=1}^{n}\mu(q)\chi_n^{\rm c}(q)
&=1-1-1\\
&=-1.
\end{aligned}
\]

The term `q=1` is zero because its carry indicator vanishes.  Hence

\[
\boxed{
\sum_{q=2}^{n}\mu(q)\chi_n^{\rm c}(q)=-1
\qquad(n\ge2).
}
\tag{L-24533.2}
\]

Unlike the reciprocal-eta pairing of `L-24531`, no exceptional Mersenne row
remains after the exact dyadic zeta filter has been applied.

## 3. Total-mass identity for every central certificate

Let `A(2),...,A(X)` be any finite real central-split coefficient vector whose
carry load equals a target `w(q)`:

\[
\sum_{n=q}^{X}A(n)\chi_n^{\rm c}(q)=w(q)
\qquad(2\le q\le X).
\tag{L-24533.3}
\]

Pair (L-24533.3) with `mu(q)` and use (L-24533.2).  Exact finite rearrangement
then gives

\[
\boxed{
\sum_{q=2}^{X}\mu(q)w(q)
 =-\sum_{n=2}^{X}A(n).
}
\tag{L-24533.4}
\]

For the critical logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

define the complete Möbius Riesz coordinate

\[
\widetilde{\mathcal R}_\mu(X)
 =\sum_{q\le X}{\mu(q)\over\sqrt q}\log{X\over q}.
\tag{L-24533.5}
\]

The `q=1` term is `log X`.  Therefore every exact central saturation satisfies

\[
\boxed{
\widetilde{\mathcal R}_\mu(X)
 =\log X-\sum_{n=2}^{X}A(n).
}
\tag{L-24533.6}
\]

This identity has no inequality, asymptotic approximation, or positivity
hypothesis.

## 4. Bottom residual form for the terminating Neumann cascade

For the exact central-Neumann construction of `L-24523`, write

\[
f_0=w_X,
\qquad
f_{j+1}=\mathscr T_Xf_j,
\qquad
f_L=0,
\]

and

\[
A_X(n)=\sum_{j=0}^{L-1}[f_j(n)-f_j(n+1)].
\tag{L-24533.7}
\]

Each stage telescopes over `n`, so

\[
\sum_{n=2}^{X}A_X(n)
 =\sum_{j=0}^{L-1}f_j(2).
\tag{L-24533.8}
\]

Combining (L-24533.6)--(L-24533.8),

\[
\boxed{
\widetilde{\mathcal R}_\mu(X)
 =\log X-\sum_{j=0}^{L-1}f_j(2).
}
\tag{L-24533.9}
\]

Thus the complete RH-bearing arithmetic content of the explicit terminating
central cascade is one scalar bottom-mass ledger.  The cascade still contains
all Möbius difficulty: (L-24533.9) is an exact reformulation, not a bound.

## 5. Relation to the eta–Mersenne ledger

`L-24531` writes the reciprocal-eta pairing as bottom values minus Mersenne
adjacent jumps.  The coefficient identity

\[
\mu=b-2\delta_2*b
\]

forms its exact dyadic difference.  Equation (L-24533.2) proves that, after this
recombination, the entire Mersenne correction collapses to the constant central
row image `-1`.  Therefore

```text
raw eta endpoint              artificial line-Re(s)=1 poles;
raw Mersenne sparse ledger    same artificial dyadic mode;
completed dyadic difference   exact Mobius total-mass identity.
```

A proof must take this dyadic difference before estimating positive parts.

## 6. Scalar stability theorem

The following estimate is sufficient for RH:

\[
\boxed{
\left|
\log X-\sum_{j=0}^{L-1}f_j(2)
\right|=X^{o(1)}.
}
\tag{L-24533.10}
\]

Indeed its left side is exactly the Möbius Riesz mean in (L-24533.9), whose
Mellin transform is

\[
{1\over z^2\zeta(z+1/2)}.
\]

A bound by `O_epsilon(X^epsilon)` for every `epsilon>0` excludes every zeta zero
with real part greater than `1/2`; functional-equation symmetry gives RH.

The point of (L-24533.10) is not to introduce another unexplained equivalence.
It identifies the precise scalar which a central analytic/boundary recurrence
must estimate.  Ambient coefficient variation, the complete Green norm, and the
raw eta atomic source are all strictly stronger consumers.

## 7. Review mutations

A claimed proof of (L-24533.10) must retain:

1. every finite endpoint term in `mathscr T_X`;
2. the `X` and `floor(X/2)` dyadic recombination before absolute values;
3. the first fixed-ratio Mertens shell;
4. the `q=1` term `log X`;
5. all stages through exact nilpotent termination.

Deleting `log X`, bounding the raw eta coordinate, or estimating each Mersenne
jump separately changes the scalar.

## 8. Proof boundary

Proved exactly:

- the Möbius image of every central row;
- total coefficient mass equals the Möbius target pairing;
- the central-Neumann cascade reduces to its bottom-stage values.

Open:

- the scalar stability estimate (L-24533.10);
- RH.
