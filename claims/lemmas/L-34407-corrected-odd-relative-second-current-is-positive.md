# L-34407 — The corrected odd relative second-current term is exactly positive

Claim ID: `L-34407`  
Title: Although the odd relative bare charge is `-2` rather than zero, its relative second current is exactly the sum of the scale-two and scale-four odd Selberg rows, so the corrected curvature remains positive with a larger deterministic moat  
Status: **PROPOSED COMPLETE EXACT REPAIR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `R-34401`; PR #346 `L-34404`; standard odd Selberg prefix identity  
Scope: aligned integer rows; no upper bound for the odd current innovation and no RH conclusion

## 1. Odd Selberg source

Retain

\[
 B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\]

with generalized primes

\[
 \Lambda_{\rm odd}(n)=\Lambda(n)\mathbf1_{n\ {m odd}},
\]

and Selberg sequence

\[
 C_{\rm odd}
 =\Lambda_{\rm odd}\log
  +\Lambda_{\rm odd}*\Lambda_{\rm odd}
 \ge0.
\tag{L-34407.1}
\]

Let

\[
 H_{\rm odd}(N)=\sum_{m\le N}C_{\rm odd}(m),
 \qquad H_{\rm odd}(0)=0.
\tag{L-34407.2}
\]

For a row `e=(n,j)`, `k=n-j`, its odd Selberg carry forcing is exactly

\[
\boxed{
 S_{\rm odd}(e)
 =H_{\rm odd}(n)-H_{\rm odd}(j)-H_{\rm odd}(k)
 =\mathcal L_e(C_{\rm odd})
 \ge0.
}
\tag{L-34407.3}
\]

The final inequality is coefficientwise: `C_odd>=0` and every carry indicator is zero or one.

## 2. Source second current

Let

\[
 t_{\rm odd}=b_{\rm odd}*C_{\rm odd}.
\tag{L-34407.4}
\]

`R-34401` retains the exact source identity

\[
 \mathbf1*b_{\rm odd}
 =\sum_{a\ge0}\delta_{2^a}.
\tag{L-34407.5}
\]

Therefore

\[
\boxed{
 \mathbf1*t_{\rm odd}
 =\sum_{a\ge0}\delta_{2^a}*C_{\rm odd}.
}
\tag{L-34407.6}
\]

Let the ordinary prefix of this sequence be

\[
 G_{\rm odd}(N)
 =\sum_{m\le N}(\mathbf1*t_{\rm odd})(m).
\tag{L-34407.7}
\]

Finite divisor switching gives the exact dyadic tower

\[
\boxed{
 G_{\rm odd}(N)
 =\sum_{a\ge0}
 H_{\rm odd}\!\left(\left\lfloor{N\over2^a}\right\rfloor\right).
}
\tag{L-34407.8}
\]

Only finitely many terms are nonzero.

The carry of `t_odd` is the additive prefix defect

\[
\boxed{
 T_{\rm odd}(n,j)
 =G_{\rm odd}(n)-G_{\rm odd}(j)-G_{\rm odd}(k).
}
\tag{L-34407.9}

## 3. Exact dyadic prefix renewal

For every integer `N>=0`, (L-34407.8) gives

\[
\begin{aligned}
 G_{\rm odd}(2N)
 &=H_{\rm odd}(2N)
   +\sum_{a\ge1}H_{\rm odd}\!\left(\left\lfloor{2N\over2^a}\right\rfloor\right)\\
 &=H_{\rm odd}(2N)
   +\sum_{b\ge0}H_{\rm odd}\!\left(\left\lfloor{N\over2^b}\right\rfloor\right).
\end{aligned}
\]

Hence

\[
\boxed{
 G_{\rm odd}(2N)=G_{\rm odd}(N)+H_{\rm odd}(2N).
}
\tag{L-34407.10}
\]

Iterating once,

\[
\boxed{
 G_{\rm odd}(4N)
 =G_{\rm odd}(N)
  +H_{\rm odd}(2N)
  +H_{\rm odd}(4N).
}
\tag{L-34407.11}

No asymptotic estimate enters.

## 4. Relative second-current identity

Apply (L-34407.11) to the parent and both children of `e=(n,j)`.  Subtracting the row at scale `e` from the row at scale `4e=(4n,4j)` gives

\[
\begin{aligned}
&T_{\rm odd}(4n,4j)-T_{\rm odd}(n,j)\\
&=\bigl[H_{\rm odd}(4n)-H_{\rm odd}(4j)-H_{\rm odd}(4k)\bigr]\\
&\quad+\bigl[H_{\rm odd}(2n)-H_{\rm odd}(2j)-H_{\rm odd}(2k)\bigr].
\end{aligned}
\]

By (L-34407.3),

\[
\boxed{
 T_{\rm odd}^{\rm rel}(e)
 :=T_{\rm odd}(4e)-T_{\rm odd}(e)
 =S_{\rm odd}(4e)+S_{\rm odd}(2e).
}
\tag{L-34407.12}

Consequently

\[
\boxed{
 T_{\rm odd}^{\rm rel}(e)\ge0
}
\tag{L-34407.13}

for every integer row.

## 5. Repaired relative curvature

`R-34401` proves that the relative bare source coordinate is

\[
\boxed{
Y_{\rm odd}^{\rm rel}(e)
=Y_{\rm odd}(4e)-Y_{\rm odd}(e)=-2.
}
\tag{L-34407.14}

The relative odd-Jordan current coordinate is

\[
 I_{\rm odd}(e)
 =Q_{\rm odd}(4e)-Q_{\rm odd}(e).
\tag{L-34407.15}

The scalar relative Jordan coordinate contributes

\[
\Delta_4R_{\rm odd}(e)
=R_{\rm odd}(4e)-16R_{\rm odd}(e).
\tag{L-34407.16}

Therefore the correct source-complete vector curvature is

\[
\begin{aligned}
\mathfrak C(W_e^{\rm odd})
&=\Delta_4R_{\rm odd}
 +|I_{\rm odd}|^2
 -Y_{\rm odd}^{\rm rel}T_{\rm odd}^{\rm rel}\\
&=\boxed{
 \Delta_4R_{\rm odd}(e)
 +|I_{\rm odd}(e)|^2
 +2S_{\rm odd}(4e)
 +2S_{\rm odd}(2e).
}
\end{aligned}
\tag{L-34407.17}

Every term on the final line is nonnegative once the inherited critical-scale theorem gives `Delta_4 R_odd>=0`.

On every fixed balanced cone, PR #346 `L-34404` proves cofinally

\[
\Delta_4R_{\rm odd}(e)
\ge12h_\eta n\log n.
\]

Hence

\[
\boxed{
\mathfrak C(W_e^{\rm odd})
\ge |I_{\rm odd}(e)|^2
   +12h_\eta n\log n
>0
}
\tag{L-34407.18}

outside the same finite base.

Thus the false `bare=0` mechanism is unnecessary for positivity: the **correct nonzero bare charge makes the second-current term favorable**.

## 6. Manifest positive decomposition

PR #346 `L-34404` defines

\[
E_{\rm odd}(e)=O(4e)-4O(e)
\]

and proves the exact reserve-increment identity

\[
\boxed{
\Delta_4R_{\rm odd}
=E_{\rm odd}(8O+E_{\rm odd})
 -\left[S_{\rm odd}(4e)-16S_{\rm odd}(e)\right].
}
\tag{L-34407.19}

Substitute (L-34407.19) into (L-34407.17).  The forcing terms combine without approximation:

\[
\boxed{
\begin{aligned}
\mathfrak C(W_e^{\rm odd})
={}&|I_{\rm odd}(e)|^2
 +E_{\rm odd}(e)\bigl(8O(e)+E_{\rm odd}(e)\bigr)\\
&+16S_{\rm odd}(e)
 +2S_{\rm odd}(2e)
 +S_{\rm odd}(4e).
\end{aligned}}
\tag{L-34407.20}

This is the most useful repaired form.

Every Selberg term on the second line is nonnegative for every row.  On every fixed balanced cone, `L-34404` proves cofinally

\[
O(e)\ge0,
\qquad
E_{\rm odd}(e)\ge0.
\]

Therefore every displayed summand in (L-34407.20) is individually nonnegative cofinally.

The false cross-free simplification would have *deleted* the last two positive forcing scales.  The corrected ledger instead exposes a five-piece positive package:

```text
odd current innovation square;
odd first-moment scale cross;
scale-e odd Selberg forcing with weight 16;
scale-2e odd Selberg forcing with weight 2;
scale-4e odd Selberg forcing with weight 1.
```

This form is particularly suited to the remaining reflected/Hermitian problem because every non-current term is now an already-typed generalized-prime or Selberg forcing at one of three explicit adjacent scales.

## 7. Stronger interpretation

The repaired relative state is not merely positive after a cancellation estimate.  Cofinally it is a **manifest sum of source-matched nonnegative pieces** before any norm or reflected recombination.

It still does not upper-bound `I_odd`; positivity remains a lower/containment statement.  The new opportunity is narrower: a reflected identity only has to route the three explicit forcing scales in (L-34407.20) to the dissipative side while retaining the current square.

## 8. Proof boundary

Closed exactly:

1. the dyadic-tower formula for `1*t_odd`;
2. the exact prefix renewal `G(2N)=G(N)+H(2N)`;
3. the exact relative identity
   \[
   T_{\rm odd}(4e)-T_{\rm odd}(e)
   =S_{\rm odd}(4e)+S_{\rm odd}(2e);
   \]
4. nonnegativity of the relative second current;
5. the repaired positive curvature (L-34407.17);
6. the manifest decomposition (L-34407.20).

Open:

1. an upper/dissipative recurrence for the repaired relative curvature;
2. critical control of `I_odd` or the compact innovation;
3. global subpower pole-current energy;
4. RH.
