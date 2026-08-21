# T-26202 — Parity-paired Euler-fiber reflected contraction: strengthened RH proposal

Claim ID: `T-26202`  
Status: `FULL CONDITIONAL PROPOSAL — one paired source-bound physical-block contraction remains open`  
Scope: fixed two-channel refinement of `T-26201`  
Date: 2026-08-08  
Depends on: `L-26204`, `L-26205`; PR #241 `L-9518`; fixed-window block-Laplace/Landau transfer

## 1. Fixed paired sources

Retain

\[
b_+=b_{\mathcal E},
\qquad
b_-=\chi_2b_{\mathcal E},
\qquad
\chi_2(n)=(-1)^{v_2(n)}.
\]

Let `W` be the nonnegative compact window of `L-26201` and define

\[
\boxed{
Z_\pm(t)
=\sum_{n\ge1}\frac{b_\pm(n)}{\sqrt n}
 W(t-\log n).
}
\tag{T-26202.1}
\]

For dyadic blocks

\[
I_m=[m\log2,(m+1)\log2],
\]

put

\[
\boxed{
\mathcal E_m
=\int_{I_m}
 \left(|Z_+(t)|^2+|Z_-(t)|^2\right)dt.
}
\tag{T-26202.2}
\]

By the sharp paired frame of `L-26205`, the two multipliers have no common zero on the closed critical strip and satisfy a uniform sum-square lower bound. Hence

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E_m=e^{o(m)}.
}
\tag{T-26202.3}
\]

This criterion retains every odd Möbius coefficient and every same-sign odd Möbius cube.

## 2. Why the paired source is stronger

The pair has three exact features unavailable to the single channel:

1. the closed-strip local reserve
   \[
   |p(z)|^2+|p(-z)|^2\ge45/4;
   \]
2. coefficientwise positivity of the summed Selberg forcing
   \[
   C_++C_-=(1+\chi_2)C_+\ge0;
   \]
3. exact orthogonalization of even and odd two-adic fibers.

The even local subfiber has taps

\[
1,\quad 2+3\sqrt2,\quad1,
\]

while the odd local subfiber has two equal taps

\[
-\left(2+\frac{3\sqrt2}{2}\right).
\]

No bounded-rank assertion is used.

## 3. Paired physical-block contraction (`PEFRC`)

A production certificate must apply PR #241's independent-frequency reflected identity to both channels before summing. It must retain:

- the complete two-channel inverse pair;
- the window packet required by the logarithmic derivative;
- every quotient, collision, cutoff, and endpoint row;
- the even/odd parity decomposition;
- the same-sign odd Möbius-cube mutation;
- the `2/3` shell mutation.

The required inequality is

\[
\boxed{
\kappa_0m^2\mathcal E_m+Q_m
\le
C(1+m)^A
+
\sum_{r=1}^{R_0}
 \theta_r(m-r)^2\mathcal E_{m-r},
}
\tag{T-26202.4}
\]

where

\[
Q_m\ge0,
\qquad
\kappa_0>0,
\qquad
R_0<\infty,
\qquad
\theta_r\ge0,
\qquad
\boxed{
\sum_{r=1}^{R_0}\theta_r<\kappa_0.
}
\tag{T-26202.5}
\]

The source has a four-step local Euler fiber and a three-step compact window, so a production proof must give an explicit finite `R_0`; it may not hide a same-scale or unbounded-delay row inside the notation.

The coefficientwise positive forcing in `L-26205` is only an input to the proof of (T-26202.4). It is not itself the inequality.

## 4. Conditional completion

Put

\[
F_m=m^2\mathcal E_m.
\]

Dropping `Q_m` and taking a running maximum over the last `R_0` indices gives

\[
F_m
\le
C_1(1+m)^A
+
\frac{\sum_r\theta_r}{\kappa_0}
\max_{1\le r\le R_0}F_{m-r}.
\]

The ratio is strictly below one. Finite induction therefore gives

\[
F_m=O((1+m)^A),
\qquad
\mathcal E_m=e^{o(m)}.
\]

Equation (T-26202.3) yields RH.

Thus

\[
\boxed{
\mathrm{PEFRC}\Longrightarrow\mathrm{RH}.
}
\tag{T-26202.6}
\]

## 5. What this proposal rules out

A purported proof is rejected if it uses only:

- the real positive-exponential adjoint, which is gauge-invariant by `R-26201`;
- one Euler channel rather than the complete parity pair;
- coefficientwise positivity without the inverse source pair;
- an absolute rank or endpoint count;
- finite block numerics without a uniform cell theorem.

## 6. Production milestones

1. **Exact small blocks.** Emit the complete two-channel source ledger and reflected matrices for the first nontrivial blocks.
2. **Cell grammar.** Prove a finite symbolic classification of all interior and boundary rows.
3. **Reserve.** Produce the exact Schur/SOS certificate for `kappa_0`.
4. **Charge.** Route every remaining row to finitely many prior blocks and prove (T-26202.5).
5. **Uniform theorem.** Prove the grammar and constants for every sufficiently large `m`.

A negative reserve eigenvector or a same-scale unmatched row is a decisive refutation of this mechanism and must be published.

## 7. Exact status

```text
paired source and closed-strip frame       PROPOSED COMPLETE
positive summed forcing                    PROPOSED COMPLETE
parity orthogonalization                   PROPOSED COMPLETE
paired RH block criterion                  PROPOSED COMPLETE TRANSFER
production PEFRC inequality                OPEN / RH-BEARING
PEFRC -> RH                                PROPOSED COMPLETE
Riemann Hypothesis                         UNPROVED
```
