# L-90305 — The balanced physical Q4 aggregate has only polylogarithmic negative inertia

Claim ID: `L-90305`  
Title: On the exact compact relative Q4 source, aggregation over carry position and one logarithmic block makes the negative spectral mass polynomially small without estimating the RH-sensitive current  
Status: **PROPOSED COMPLETE COFINAL APPLICATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-10  
Dependencies: `L-90304`; PR #345 `L-34406/L-34409/L-34410`; PR #339 `L-33803`; PR #346 continuous-row placement; elementary generalized-prime mass bounds  
Scope: balanced compact-source physical block; fixed collars and unbalanced rows are retained in their existing ledgers

## 1. Exact compact relative row

Use the finite main-pole source

\[
B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)}
\]

and the relative compact row of PR #345. For every sufficiently deep balanced carry row

\[
e=(n,j),
\qquad
\eta n\le j\le(1-\eta)n,
\]

the relative bare source vanishes exactly:

\[
Y_e=0.
\tag{L-90305.1}
\]

Its centered curvature matrix is therefore

\[
\boxed{
K_e=
\begin{pmatrix}
R_e&-\frac12(T_e-2E_eI_e)\\[1mm]
-\frac12\overline{(T_e-2E_eI_e)}&|I_e|^2
\end{pmatrix},
}
\tag{L-90305.2}
\]

where

\[
R_e=\Delta_4R_\sharp(e),
\]

\[
E_e=P_\sharp(4e)-4P_\sharp(e),
\]

\[
I_e=Q_\sharp(4e)-Q_\sharp(e),
\]

and `T_e` is the exact relative source second current.

The trace is

\[
R_e+|I_e|^2.
\]

No source cross remains.

## 2. Source-side estimates

For every fixed `eta in (0,1/2)`, the existing compact-source reserve theorem gives constants

\[
c_\eta,C_\eta>0
\]

such that, cofinally and uniformly,

\[
\boxed{
c_\eta n\log n
\le R_e
\le C_\eta n\log(2n).
}
\tag{L-90305.3}
\]

The same fourfold-binomial/Stirling calculation gives

\[
\boxed{
|E_e|\le C_\eta\log(2n).
}
\tag{L-90305.4}
\]

A completely source-bound estimate for the second current is sufficient here. Let

\[
\Psi_\sharp(x)=\sum_{m\le x}\Lambda_\sharp(m).
\]

The positive generalized-prime mass bound on the compact source gives

\[
\Psi_\sharp(x)\ll x.
\tag{L-90305.5}
\]

For

\[
C_\sharp
=
\Lambda_\sharp\log
+
\Lambda_\sharp*\Lambda_\sharp,
\]

partial summation and divisor switching give

\[
\sum_{m\le x}|C_\sharp(m)|
\ll x\log(2x).
\tag{L-90305.6}
\]

Indeed,

\[
\sum_{m\le x}\Lambda_\sharp(m)\log m
\le\log x\,\Psi_\sharp(x)\ll x\log x,
\]

and

\[
\sum_{ab\le x}\Lambda_\sharp(a)\Lambda_\sharp(b)
\le
Cx\sum_{a\le x}\frac{\Lambda_\sharp(a)}a
\ll x\log x.
\]

Since

\[
\mathbf1*b_\sharp=\varepsilon-4\delta_4,
\]

the ordinary prefix of

\[
t_\sharp=b_\sharp*C_\sharp
\]

is a fixed radix-four difference of the prefix of `C_sharp`. Hence every compact-source carry row and every aligned relative difference satisfy

\[
\boxed{
|T_e|\le C_\eta n\log(2n).
}
\tag{L-90305.7}
\]

The sharper `O(n)` cancellation available from the Selberg main term is not needed.

## 3. Aggregate at one endpoint

Let

\[
\mathcal J_{n,\eta}
=
\{j\in\mathbf Z:\eta n\le j\le(1-\eta)n\}.
\]

The exact physical/carry formula of PR #339 assigns each normalized carry-position cell the weight

\[
w_{n,j}=\frac1{n^2}.
\tag{L-90305.8}
\]

Define

\[
\overline K_{n,\eta}
=
\frac1{n^2}
\sum_{j\in\mathcal J_{n,\eta}}K_{(n,j)}.
\tag{L-90305.9}
\]

In the notation of `L-90304`,

\[
A_n
=
\frac1{n^2}\sum_jR_{n,j},
\qquad
F_n
=
\frac1{n^2}\sum_j|E_{n,j}|^2,
\]

\[
U_n
=
\frac1{n^2}\sum_jT_{n,j}.
\tag{L-90305.10}
\]

Equations (L-90305.3)–(L-90305.7), together with

\[
|\mathcal J_{n,\eta}|\asymp_\eta n,
\]

give

\[
\boxed{
A_n\gg_\eta\log n,
}
\tag{L-90305.11}
\]

\[
\boxed{
F_n\ll_\eta\frac{\log^2(2n)}n=o(A_n),
}
\tag{L-90305.12}
\]

and

\[
\boxed{
|U_n|\ll_\eta\log(2n).
}
\tag{L-90305.13}
\]

Therefore `A_n>F_n` cofinally, and `L-90304` gives

\[
\boxed{
\delta(\overline K_{n,\eta})
\ll_\eta\log(2n).
}
\tag{L-90305.14}
\]

The unknown quantity

\[
\frac1{n^2}\sum_j|I_{n,j}|^2
\]

does not occur on the right.

If one inserts the classical Selberg main-term cancellation which improves (L-90305.7) to `T_e=O(n)`, then the same argument gives the stronger

\[
\delta(\overline K_{n,\eta})
\ll_\eta\frac1{\log n}.
\tag{L-90305.15}
\]

Only the polylogarithmic form (L-90305.14) is used below.

## 4. One physical logarithmic block

Let

\[
\mathcal N_J
=
\{n\in\mathbf Z:e^J\le n<e^{J+1}\}
\]

and put

\[
\ell_n=\log\frac{n+1}{n}.
\]

The continuous endpoint cell has length `ell_n`, with

\[
\frac1{2n}\le\ell_n\le\frac1n.
\tag{L-90305.16}
\]

Define the balanced block curvature

\[
\boxed{
K_{J,\eta}
=
\sum_{n\in\mathcal N_J}
\ell_n\,\overline K_{n,\eta}.
}
\tag{L-90305.17}
\]

This is the exact nonnegative cellwise aggregation supplied by the continuous physical/carry placement; one-unit augmented rows obey the same cofinal estimates and alter only constants.

Its source summaries obey

\[
A_J
=
\sum_n\ell_nA_n
\gg_\eta
\sum_{e^J\le n<e^{J+1}}\frac{\log n}{n}
\gg_\eta J,
\tag{L-90305.18}
\]

\[
F_J
\ll_\eta
\sum_{e^J\le n<e^{J+1}}
\frac{\log^2n}{n^2}
\ll_\eta J^2e^{-J},
\tag{L-90305.19}
\]

and

\[
|U_J|
\le
\sum_n\ell_n|U_n|
\ll_\eta
\sum_{e^J\le n<e^{J+1}}\frac{\log n}{n}
\ll_\eta J.
\tag{L-90305.20}
\]

Hence `A_J-F_J\gg_eta J`, and the aggregate theorem gives

\[
\boxed{
\delta(K_{J,\eta})
\ll_\eta J.
}
\tag{L-90305.21}
\]

With the sharper second-current cancellation, this improves to `O_eta(1/J)`. Again, the polynomial bound is sufficient.

## 5. Why this closes the Claude/Q4 defect estimate

`T-90301` isolated the remaining production estimate as a polynomial bound for the negative spectral mass of the complete two-state Q4 block. Equation (L-90305.21) is precisely such a bound on the balanced physical block.

The proof does not use:

1. a rowwise Schur inequality;
2. a bound for the compact RH-sensitive current;
3. positivity of each microscopic curvature matrix;
4. cancellation between hypothetical zero ordinates;
5. RH, a zero-free strip, or a zero table.

Instead, the deterministic reserve creates `A_J~J`, the relative score has negligible quadratic mass `F_J`, and the signed second-current mean is only `O(J)`. The complete current energy strengthens the determinant and is optimized out.

## 6. Collars and unbalanced rows

This theorem does not discard the complement of the fixed balanced cone. The live Q4 graph separately supplies:

- fixed-width endpoint collars with polynomial forcing;
- unbalanced/Type-I routing to strict lower scale;
- the exact delayed Möbius and bare-source gauges;
- the neutral principal predecessor state.

Those terms must be retained in the final recurrence. They do not enter the balanced aggregate defect (L-90305.21).

## 7. Proof boundary

Closed here, subject to review:

1. the compact-source second-current mass estimate;
2. the exact endpoint aggregate;
3. `A_n>>log n`, `F_n=o(A_n)`, and `U_n=O(log n)`;
4. polylogarithmic endpoint negative inertia;
5. polynomial unit-block negative inertia independent of the current.

Still requiring composition review:

1. the exact current-scale synthesis/return identity inherited by `T-90301`;
2. collar and lower-scale bookkeeping in one final theorem;
3. the RH conclusion.
