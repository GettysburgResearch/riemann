# R-26801 — Positive renewal and carry reserve do not close the bottom charge

Claim ID: `R-26801`  
Title: Positive inverse coefficients, a carry-space Schur reserve, and parity Bezout synthesis do not by themselves prove Bottom-Charge Positivity  
Status: **EXACT SCOPE CORRECTION WITH ONE EXPLICIT COUNTEREXAMPLE**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26202`, `L-26204`, `T-26801`; PRs #263 and #269  
Scope: rules out three tempting automatic closures; it does not refute BCP

## 1. The exact positive renewal identity

Let

\[
 \widetilde{\mathcal R}_\omega(X)
 =\sum_{n\le X}\frac{\omega_2(n)}{\sqrt n}\log(X/n)
 =\log X+\mathcal R_\omega(X),
 \tag{R-26801.1}
\]

where the first expression includes the `n=1` term. Let `a_omega` be the
strictly positive Dirichlet inverse of `omega_2`:

\[
 a_\omega*\omega_2=\varepsilon.
 \tag{R-26801.2}
\]

Finite convolution gives the exact renewal equation

\[
 \boxed{
 \sum_{d\le X}\frac{a_\omega(d)}{\sqrt d}
 \widetilde{\mathcal R}_\omega(X/d)
 =\log X.
 }
 \tag{R-26801.3}
\]

Indeed, after writing `m=dn`, the left side is

\[
 \sum_{m\le X}\frac{(a_\omega*\omega_2)(m)}{\sqrt m}\log(X/m).
\]

All renewal weights are positive. This does **not** imply that the renewal state
is positive, nor that it is bounded above by its forcing term.

## 2. Exact failure of the naive positive-state shortcut

At `X=4`, the source coefficients are

\[
 \omega_2(1)=1,
 \quad\omega_2(2)=-\frac52,
 \quad\omega_2(3)=-1,
 \quad\omega_2(4)=2.
\]

The last term has zero logarithmic weight, so

\[
 \boxed{
 \widetilde{\mathcal R}_\omega(4)
 =
 \left(2-\frac{5}{2\sqrt2}\right)\log2
 -\frac1{\sqrt3}\log\frac43
 <0.
 }
 \tag{R-26801.4}
\]

A fully elementary comparison proves the sign. The bounds

\[
 \sqrt2<\frac{99}{70},
 \qquad
 \sqrt3<\frac{26}{15}
\]

give

\[
 \sqrt3\left(2-\frac5{2\sqrt2}\right)
 <\frac{598}{1485}<\frac{41}{100}.
 \tag{R-26801.5}
\]

Moreover

\[
 \frac{\log(4/3)}{\log2}>\frac{41}{100}
 \tag{R-26801.6}
\]

because this is equivalent to `2^159>3^100`, and

\[
 \frac{2^{160}}{3^{100}}
 =\left(1+\frac{13}{243}\right)^{20}
 >1+\frac{260}{243}>2.
\]

Thus the positive inverse does not produce a positive renewal state. Any proof
of BCP must use additional source information.

This counterexample does not contradict BCP: BCP is the upper bound

\[
 \widetilde{\mathcal R}_\omega(X)\le\log X,
\]

not positivity of the inclusive state.

## 3. Carry reserve is in the wrong Hilbert space until an intertwiner is built

PR #269 proves an absolute Schur reserve for the carry vectors

\[
 Z_{n,m}(j),
 \qquad
 P_n(j)=\sum_q\Lambda_\omega(q)\chi_{n,q}(j).
\]

PR #241's physical normal Gram acts instead on compact logarithmic prime
signals. A positive Gram in one space gives no inequality in the other without
an explicit operator and a proved orientation. The exact dyadic translate
matrix in physical space is rank one and has a null direction.

Therefore the implication

```text
strict carry Schur reserve
-> positive physical transition reserve
```

is unproved. `T-26801` isolates the missing operator in F5PBT.

## 4. Positive parity Bezout synthesis is reconstruction, not coercivity

PR #263 constructs positive finite coefficients `U` satisfying a parity-paired
Bezout identity of the form

\[
 U(z)p(z)+U(-z)p(-z)=1.
 \tag{R-26801.7}
\]

This proves exact source reconstruction and a source-frame reserve. It does not
show that either reconstructed physical quadratic form has the sign or
orientation required by the carry bottom charge. A Bezout identity can recover
a vector while losing all order information.

Thus

```text
positive source reconstruction
-> Bottom-Charge Positivity
```

is not an automatic implication.

## 5. High-index transport is exactly invisible

For the underlying dyadic source `b_2`, PR #269 proves

\[
 \sum_q b_2(q)v_q(b)=-2b(2)+b(3),
 \tag{R-26801.8}
\]

and an adjacent correction changes this scalar by

\[
 3F_2-F_3.
 \tag{R-26801.9}
\]

Every flow supported at indices at least four is invisible. Hence a half-scale
or defect-to-slack transport can contribute to the dyadic proof only if its
complete charge is telescoped explicitly into the bottom coordinates.

## 6. Correct surviving target

The exact results above leave one admissible route:

1. retain the complete source before norms;
2. construct the physical-to-carry transition map on quotient cells `2,3,4`;
3. retain every reflected cross term;
4. telescope every digital and transport boundary to rows `2,3`;
5. obtain an explicit positive decomposition of
   `5c_X(2)+3c_X(3)`.

That is F5PBT in `T-26801`.

## 7. Proof boundary

Refuted at the stated scopes:

- positive inverse coefficients automatically make the Riesz renewal state
  positive;
- a carry-space Schur reserve automatically transfers to the physical block;
- positive parity Bezout reconstruction automatically gives the bottom-charge
  sign;
- high-index transport can alter the dyadic scalar without a bottom telescope.

Not refuted:

- BCP;
- F5PBT;
- RH.
