# L-34409 — The compact relative current bound is an exact normalized Schur row inequality

Claim ID: `L-34409`  
Title: For the compact two-tap source, the desired RH-scale inequality `|I|^2<=Delta_4 R` is exactly the local contractivity condition of one normalized two-coordinate relative Jordan row  
Status: **PROPOSED COMPLETE EXACT REDUCTION / SCHUR NORMAL FORM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-34406`; positive Jordan algebra of PR #325 `L-32415`; elementary aligned carry scaling  
Scope: exact finite row normalization and equivalence; the Schur inequality itself remains open

## 1. Positive compact-source Jordan row

Retain

\[
 B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)},
 \qquad
 A_\sharp=B_\sharp^{-1}.
\]

Define its Jordan deformation

\[
\boxed{
 J_{\sharp,\tau}(s)
 ={A_\sharp(s-\tau)\over A_\sharp(s)}.
}
\tag{L-34409.1}

For odd primes the local coefficients are the standard positive Jordan coefficients. At the prime two local factor, with `z=2^-s` and `a=2^tau>=1`,

\[
 {1-z\over1-az}
 {1-4z^2\over1-4a^2z^2}
\]

is the product of two coefficientwise nonnegative ratio series. Hence

\[
\boxed{
 J_{\sharp,\tau}(n)\ge0
 \qquad(n\ge1,\tau\ge0).
}
\tag{L-34409.2}

For a row `e=(n,j)` put

\[
\boxed{
 F_e(\tau)=1+\mathcal L_e(J_{\sharp,\tau}).
}
\tag{L-34409.3}

Then

\[
F_e(0)=1,
\qquad
F_e'(0)=P_\sharp(e),
\qquad
F_e''(0)=S_\sharp(e).
\tag{L-34409.4}

## 2. Relative scalar coordinate

For the aligned row

\[
 e^+=(4n,4j)
\]

define

\[
\boxed{
 H_e(\tau)
 ={F_{e^+}(\tau)\over F_e(4\tau)}.
}
\tag{L-34409.5}

Then

\[
H_e(0)=1,
\]

\[
\boxed{
H_e'(0)=E_e
=P_\sharp(e^+)-4P_\sharp(e),
}
\tag{L-34409.6}

and, by `L-34406`,

\[
\boxed{
-\bigl(\log H_e\bigr)''(0)
=\Delta_4R_\sharp(e).
}
\tag{L-34409.7}

Equivalently,

\[
\boxed{
H_e''(0)=E_e^2-\Delta_4R_\sharp(e).
}
\tag{L-34409.8}

## 3. Relative source-convolved leg

Put

\[
 K_{\sharp,\tau}=b_\sharp*J_{\sharp,\tau}.
\]

Since

\[
 K_{\sharp,0}=b_\sharp,
 \qquad
 K_{\sharp,0}'=q_\sharp,
\]

where `q_sharp=B_sharp'` is the hard compact current, define

\[
\boxed{
 G_e(\tau)
 =\mathcal L_{e^+}
  \bigl[(\varepsilon-\delta_4)*K_{\sharp,\tau}\bigr].
}
\tag{L-34409.9}

Aligned carry scaling gives

\[
\mathcal L_{e^+}(\delta_4*f)=\mathcal L_e(f),
\]

so

\[
 G_e'(0)
 =Q_\sharp(e^+)-Q_\sharp(e).
\]

Define the aligned compact-current innovation

\[
\boxed{
 I_\sharp(e)
 :=Q_\sharp(e^+)-Q_\sharp(e).
}
\tag{L-34409.10}

Hence

\[
\boxed{G_e'(0)=I_\sharp(e).}
\tag{L-34409.11}

## 4. The relative bare coordinate vanishes exactly

Because

\[
 \mathbf1*b_\sharp=\varepsilon-4\delta_4,
\]

its prefix is constant equal to `-3` once the argument is at least four. Therefore on every row with

\[
 j\ge4,
 \qquad
 n-j\ge4,
\]

one has

\[
\boxed{
 Y_\sharp(e):=\mathcal L_e(b_\sharp)=3.
}
\tag{L-34409.12}

The same is true at `e+`. Consequently

\[
\boxed{
 G_e(0)
 =Y_\sharp(e^+)-Y_\sharp(e)
 =0.
}
\tag{L-34409.13}

This is the key simplification specific to the finite compact source: its relative source leg starts at the origin, so there is no second-current/bare-source cross in its relative curvature.

## 5. Relative vector curvature

Define

\[
 W_e(\tau)=(H_e(\tau),G_e(\tau)).
\]

Its jets have the form

\[
 W_e(0)=(1,0),
\]

\[
 W_e'(0)=(E_e,I_\sharp(e)),
\]

\[
 W_e''(0)
 =(E_e^2-\Delta_4R_\sharp(e),\,T_e^{\rm rel}),
\]

where the second coordinate is immaterial to the curvature because `G_e(0)=0`.

Thus

\[
\boxed{
 \mathfrak C(W_e)
 :=\|W_e'(0)\|^2
  -\operatorname{Re}\langle W_e(0),W_e''(0)\rangle
 =\Delta_4R_\sharp(e)+|I_\sharp(e)|^2.
}
\tag{L-34409.14}

Unlike the denominator-bearing Q=4 state, no source cross survives.

## 6. Normalize by the relative scalar partition

Define the normalized relative row

\[
\boxed{
 \mathcal S_e(\tau)
 =\left(
   {1\over H_e(\tau)},
   {G_e(\tau)\over H_e(\tau)}
  \right).
}
\tag{L-34409.15}

At the origin,

\[
\mathcal S_e(0)=(1,0).
\]

Using (L-34409.6)--(L-34409.8),

\[
\left({1\over H_e}\right)'(0)=-E_e,
\]

\[
\boxed{
\left({1\over H_e}\right)''(0)
=E_e^2+\Delta_4R_\sharp(e).
}
\tag{L-34409.16}

Also

\[
\left({G_e\over H_e}\right)'(0)=I_\sharp(e).
\]

Therefore the imaginary-Jordan curvature of the normalized row is

\[
\boxed{
 \mathfrak C(\mathcal S_e)
 =|I_\sharp(e)|^2-\Delta_4R_\sharp(e).
}
\tag{L-34409.17}

Equivalently, if

\[
 \tau=iy,
\]

then

\[
\boxed{
 \|\mathcal S_e(iy)\|^2
 =1+y^2
  \bigl[|I_\sharp(e)|^2-\Delta_4R_\sharp(e)\bigr]
 +O(y^3).
}
\tag{L-34409.18}

## 7. Exact Schur equivalence

The desired source-matched RH-scale estimate with coefficient one,

\[
\boxed{
 |I_\sharp(e)|^2
 \le\Delta_4R_\sharp(e),
}
\tag{L-34409.19}

is therefore **equivalent** to any of the following local statements:

\[
\boxed{
 \mathfrak C(\mathcal S_e)\le0,
}
\tag{L-34409.20}

or

\[
\boxed{
 y=0\text{ is a local maximum of }
 \|\mathcal S_e(iy)\|^2,
}
\tag{L-34409.21}

or, more strongly, the finite Schur inequality

\[
\boxed{
 1+|G_e(iy)|^2
 \le |H_e(iy)|^2
}
\tag{L-34409.22}

for all sufficiently small real `y`.

A global proof of (L-34409.22) on the entire imaginary axis would of course imply the local inequality, but only the local second-order statement is needed.

This is no longer an unnamed `current <= reserve` estimate: it is one explicit finite Schur-row contractivity theorem.

## 8. RH consumer

Put

\[
 U_\sharp(e)=Q_\sharp(e)/\sqrt n.
\]

By definition of `I_sharp`,

\[
\boxed{
 U_\sharp(e^+)
 ={1\over2}U_\sharp(e)
 +{I_\sharp(e)\over2\sqrt n}.
}
\tag{L-34409.23}

If (L-34409.19) holds cofinally, then `L-34406` gives

\[
 I_\sharp(e)^2=O_\eta(n\log n).
\]

A standard weighted Young inequality in (L-34409.23) yields a fixed-delay normalized recurrence with only polylogarithmic forcing. Iteration gives polynomial/subexponential local energy for the compact pole current.

Because `B_sharp` retains every nontrivial zeta-zero pole, the existing vector-valued Mellin/Landau pole criterion then excludes every zero with real part greater than one half; functional-equation symmetry gives RH.

Thus the complete new conditional chain is

\[
\boxed{
 \text{finite Schur row (L-34409.22)}
 \Longrightarrow
 |I_\sharp|^2\le\Delta_4R_\sharp
 \Longrightarrow
 \text{critical fixed-delay energy recurrence}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{L-34409.24}

## 9. Production target

The preferred proof attack is now finite and source-complete:

> Prove that the normalized relative row `S_e(tau)` is contractive to second order on the imaginary Jordan axis for every sufficiently large balanced row.

Potential mechanisms include:

1. an explicit source-capacity realization of `S_e` as a Schur transfer row;
2. a finite unitary colligation / Julia operator built from the compact inverse coefficients;
3. a sum-of-squares factorization of
   \[
   |H_e(iy)|^2-1-|G_e(iy)|^2;
   \]
4. a relative Pick kernel for the positive compact-source Jordan partition.

The scalar two-parameter Fisher shortcut ruled out in `L-34403` does not apply here: the nontrivial source coordinate is the source-convolved leg `G_e`, and its zeroth value vanishes after aligned subtraction.

## 10. Proof boundary

Closed exactly here:

1. positive compact-source Jordan row;
2. critical relative scalar partition;
3. exact aligned source-difference leg;
4. zero relative bare coordinate;
5. source-complete relative vector curvature `Delta_4R_sharp+|I_sharp|^2`;
6. normalized Schur row;
7. exact equivalence between current domination and local contractivity;
8. conditional Schur-row -> critical recurrence -> RH chain.

Still open:

1. proof of local/global Schur contractivity;
2. RH.
