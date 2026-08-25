# L-105649 — Monotone current charge is an adaptive hard-band mixture

Claim ID: `L-105649`  
Status: **PROVED EXACT ABSTRACT LAYER-CAKE / FIRST-CROSSING THEOREM**  
Created: 2026-08-25  
Depends on: `L-105625`, `L-105640--L-105648`  
RH status: **not assumed**

## 1. Monotone source profile

Let

\[
r:[0,\infty)\longrightarrow[0,\infty)
\]

be bounded, right-continuous and nonincreasing, with

\[
\lim_{\xi\to\infty}r(\xi)=0.
\]

Let `nu_r=-dr` be its positive Stieltjes measure, so that

\[
\boxed{
r(\xi)=\int_{[\xi,\infty)}d\nu_r(L),
\qquad
\nu_r([0,\infty))=r(0).
}
\tag{L-105649.1}

For a rank-one upper-half-plane factor of depth `delta>0`, define its
`r`-weighted charge

\[
\boxed{
q_r(\delta)
=2\delta\int_0^\infty
r(\xi)e^{-2\delta\xi}\,d\xi.
}
\tag{L-105649.2}

## 2. Exact adaptive-band representation

Insert (L-105649.1) in (L-105649.2) and apply Tonelli.  The inner integral is

\[
2\delta\int_0^L e^{-2\delta\xi}d\xi
=1-e^{-2\delta L}.
\]

Therefore

\[
\boxed{
q_r(\delta)
=
\int_{[0,\infty)}
\bigl(1-e^{-2\delta L}\bigr)d\nu_r(L).
}
\tag{L-105649.3

The complementary charge is

\[
\boxed{
c_r(\delta)
=
\int_{[0,\infty)}e^{-2\delta L}d\nu_r(L)
=r(0)-q_r(\delta).
}
\tag{L-105649.4

For each fixed bandwidth `L`, `L-105640` identifies

\[
1-e^{-2\delta L}
\]

as the exact source-visible fraction of the first anti-inner rank-one charge,
and

\[
e^{-2\delta L}
\]

as its exact endpoint/signed-complement fraction.  Equations
(L-105649.3)--(L-105649.4) therefore prove:

\[
\boxed{
\text{monotone weighted charge}
=
\text{positive mixture of exact adaptive source/index splits}.
}
\tag{L-105649.5

No single bandwidth is selected after the zero is observed.  The source profile
itself supplies the complete predeclared bandwidth distribution.

## 3. The actual Xi current profile

For the standard Xi source, let

\[
R_H(\xi)
={H e^{-H\xi}\Lambda_2(\xi)\over\widehat J_H(\xi)}.
\]

`L-105624/L-105640` prove that `R_H` is nonincreasing and tends to zero.
Consequently there is a canonical positive bandwidth measure

\[
\boxed{d\nu_H(L)=-dR_H(L).}
\tag{L-105649.6

For a zero of `Xi'` at height `gamma>H`, put `delta=gamma-H`.  The current
survival function of `L-105644` is exactly

\[
\boxed{
Q_\rho(H)
=
\int_0^\infty
\bigl(1-e^{-2(\gamma-H)L}\bigr)d\nu_H(L).
}
\tag{L-105649.7

Its complementary endpoint mass at that fixed height is

\[
\boxed{
R_H(0)-Q_\rho(H)
=
\int_0^\infty
e^{-2(\gamma-H)L}d\nu_H(L).
}
\tag{L-105649.8

For the physical microscope profile

\[
r_{b,h}={h\over H}R_H,
\qquad H=b+h,
\]

the same formulas hold after multiplying both sides by `h/H`.

Thus the actual Xi current does not merely resemble an adaptive source bank.
It is exactly a positive continuous mixture of the hard-band source/index
conservation laws.

## 4. Relation to logarithmic index flow

The hard-band mixture and the logarithmic random-scale mixture solve two
complementary normalization problems:

```text
L-105649:
  the actual monotone current metric chooses a positive distribution of
  source bandwidths;

L-105647--L-105648:
  the signed divisor at every bandwidth is represented by an additive
  logarithmic interior index.
```

Together they close `HOWNXFER105644` at the one-factor and additive-divisor
normal-form level: the current owner charge and the endpoint index are two
positive pieces of one predeclared adaptive scale resolution.

## 5. Scope

For several nonorthogonal model factors, the complete Hankel/model-space trace
is not the sum of the individual rank-one charges.  The additive object is the
signed divisor or logarithmic index, whereas the remaining degree-zero
interaction is the canonical-correlation/phase-angle defect of sibling
`L-106506/L-106512/L-106514`.  Nor does an energy mixture produce a pointwise
Xi microscope sign.  The finite physical overlap, cofinal endpoint ledger and
RH remain open.
