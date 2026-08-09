# L-34006 — The compact Q=4 innovation second-current cross term is lower order

Claim ID: `L-34006`  
Title: After one radix-four source difference, the complete Selberg second current has only linear prefix mass; consequently the source-augmented innovation curvature dominates the true innovation current square cofinally  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-34003`, `L-34005`; classical Selberg symmetry formula; elementary Chebyshev bound  
Scope: aligned quarter-balanced Q=4 innovation rows; no current upper bound, block recurrence, or RH conclusion

## 1. Innovation source and its three jets

Retain

\[
 b_\circ=(\varepsilon-\delta_4)*b_4,
 \qquad
 \mathbf1*b_\circ=\varepsilon-4\delta_4.
\tag{L-34006.1}
\]

Keep the **original Q=4 Jordan deformation** `J_(4,tau)` and define the compact source-convolved path

\[
 K_{\circ,\tau}=b_\circ*J_{4,\tau}.
\tag{L-34006.2}
\]

Its first three jets are

\[
 K_{\circ,0}=b_\circ,
 \qquad
 K'_{\circ,0}=i_\circ=b_\circ*\Lambda_4,
 \qquad
 K''_{\circ,0}=t_\circ=b_\circ*C_4.
\tag{L-34006.3}
\]

At the aligned row `(4n,4j)`, write

\[
 Y_\circ=\mathcal L_{4n,4j}(b_\circ),
 \quad
 I_\circ=\mathcal L_{4n,4j}(i_\circ),
 \quad
 T_\circ=\mathcal L_{4n,4j}(t_\circ).
\tag{L-34006.4}
\]

By the exact source renewal,

\[
\boxed{
 I_\circ
 =Q_4^{\rm phys}(4n,4j)-Q_4^{\rm phys}(n,j).
}
\tag{L-34006.5}
\]

Thus `I_circ` is the actual one-step physical-current innovation.

## 2. Bare innovation charge is exactly three in the balanced interior

The divisor-prefix potential of `1*b_circ=epsilon-4delta_4` is

\[
 D_\circ(x)
 =\begin{cases}
 0,&0\le x<1,\\
 1,&1\le x<4,\\
 -3,&x\ge4.
 \end{cases}
\tag{L-34006.6}
\]

If `n>=16` and

\[
 n/4\le j\le3n/4,
\]

then the parent `4n` and both children `4j,4(n-j)` are at least four. Therefore

\[
\boxed{
Y_\circ
=D_\circ(4n)-D_\circ(4j)-D_\circ(4n-4j)
=3.
}
\tag{L-34006.7}
\]

No asymptotic estimate enters this identity.

## 3. Exact Dirichlet identity for the innovation second-current coefficient

Let

\[
 \lambda(s)=-{\zeta'(s)\over\zeta(s)},
 \qquad
 \mathcal C(s)=-\lambda'(s)+\lambda(s)^2
\]

be the ordinary von-Mangoldt and Selberg Dirichlet series, and put

\[
 z=4^{-s},\qquad L=\log4.
\]

The Q=4 generalized prime is

\[
 \lambda_4(s)=\lambda(s)
 -L{z\over1-z}
 +4L{z\over1-4z}.
\tag{L-34006.8}
\]

Its Selberg series is

\[
 C_4=-\lambda_4'+\lambda_4^2.
\]

A direct differentiation and simplification gives the exact identity

\[
\boxed{
\begin{aligned}
(1-4z)C_4
={}&(1-4z)\mathcal C
 +6L{z\over1-z}\lambda\\
&+3L^2+{2L^2\over1-4z}-{5L^2\over1-z}.
\end{aligned}
}
\tag{L-34006.9}
\]

The constant coefficient on the second line is zero after expansion. Therefore coefficientwise

\[
\boxed{
\begin{aligned}
 g_4:=(\varepsilon-4\delta_4)*C_4
={}&(\varepsilon-4\delta_4)*\mathcal C\\
&+6L\sum_{r\ge1}\delta_{4^r}*\Lambda\\
&+L^2\sum_{r\ge1}(2\cdot4^r-5)\delta_{4^r}.
\end{aligned}
}
\tag{L-34006.10}
\]

This exact formula is the load-bearing cancellation: the potentially large local Q=4 second-current correction reduces to an ordinary Selberg radix-four difference, a geometrically decaying family of Chebyshev prefixes, and explicit local atoms.

## 4. Linear summatory bound

Let

\[
 G_4(X)=\sum_{m\le X}g_4(m).
\]

The classical Selberg symmetry formula is

\[
\sum_{m\le X}\mathcal C(m)
=2X\log X+O(X).
\tag{L-34006.11}
\]

Consequently

\[
\sum_{m\le X}
[(\varepsilon-4\delta_4)*\mathcal C](m)
=2X\log4+O(X).
\tag{L-34006.12}
\]

The elementary Chebyshev estimate `psi(Y)=O(Y)` gives

\[
\sum_{r\ge1}\psi(X/4^r)=O(X),
\tag{L-34006.13}
\]

and the explicit local series satisfies

\[
\sum_{4^r\le X}(2\cdot4^r-5)=O(X).
\tag{L-34006.14}
\]

Combining (L-34006.10)--(L-34006.14),

\[
\boxed{
 G_4(X)=O(X).
}
\tag{L-34006.15}
\]

All constants are absolute.

## 5. The source second current is only linear on aligned rows

Since

\[
 \mathbf1*t_\circ
 =(\mathbf1*b_\circ)*C_4
 =(\varepsilon-4\delta_4)*C_4
 =g_4,
\]

the general prefix/carry identity of PR #341 gives

\[
 T_\circ
 =G_4(4n)-G_4(4j)-G_4(4n-4j).
\tag{L-34006.16}
\]

Equation (L-34006.15) therefore gives uniformly in `j`

\[
\boxed{
 |T_\circ(4n,4j)|=O(n).
}
\tag{L-34006.17}
\]

Together with the exact bare charge (L-34006.7),

\[
\boxed{
 |Y_\circ T_\circ|=O(n).
}
\tag{L-34006.18}
\]

on every quarter-balanced aligned row.

## 6. Source-augmented innovation curvature dominates the current square

Define the deterministic radix-four reserve increment

\[
 \Delta_4R(n,j)
 =R_4(4n,4j)-16R_4(n,j),
\]

and the source-augmented innovation curvature

\[
\boxed{
 \mathcal A_\circ(n,j)
 =\Delta_4R(n,j)+I_\circ(n,j)^2-Y_\circ T_\circ.
}
\tag{L-34006.19}
\]

`L-34005` proves uniformly

\[
 \Delta_4R(n,j)\ge(\log2)n\log n
\]

outside one fixed finite base. Equation (L-34006.18) is only `O(n)`. Hence there exists an absolute `N_1` such that for every `n>=N_1` and every quarter-balanced `j`,

\[
\boxed{
 \Delta_4R(n,j)-Y_\circ T_\circ
 \ge\frac12\Delta_4R(n,j)>0.
}
\tag{L-34006.20}
\]

Consequently

\[
\boxed{
 \mathcal A_\circ(n,j)
 \ge I_\circ(n,j)^2
   +\frac12\Delta_4R(n,j)
 >0.
}
\tag{L-34006.21}
\]

Thus the complete source-augmented curvature of the **actual one-step RH-sensitive current innovation** is cofinally positive and contains its current square with coefficient one, while retaining a deterministic critical-scale moat.

## 7. Exact product-curvature accounting

The physical Jordan energy of the compact source path has

\[
\frac12\mathscr E_\circ''(0)
=I_\circ^2+Y_\circ T_\circ.
\tag{L-34006.22}
\]

Therefore

\[
\boxed{
 \mathcal A_\circ
 -\frac12\mathscr E_\circ''(0)
 =\Delta_4R-2Y_\circ T_\circ.
}
\tag{L-34006.23}
\]

The right side is also positive cofinally by (L-34006.18) and `L-34005`. Hence the entire source-convolved product curvature fits inside the augmented innovation curvature with coefficient one outside a finite base.

This is a placement/no-double-spend theorem. It does **not** bound `A_circ` above independently of the current square.

## 8. What remains

The formerly separate current-scale objects now satisfy one exact positive ledger:

```text
deterministic new reserve Delta_4R = Theta(n log n)
+
true physical innovation square I_circ^2
-
lower-order bare x second-current cross
=
positive augmented innovation curvature.
```

And the complete product-source Jordan curvature is coefficient-one absorbed by that same object.

The remaining theorem is therefore no longer source placement or the sign of the source-convolved product block. It is an **upper/delayed recurrence for the positive augmented innovation curvature itself**. Such a recurrence would immediately control the current square by (L-34006.21).

No such recurrence is claimed here.

## 9. Proof boundary

Closed, subject to review:

1. exact compact-source second-current identity;
2. `O(X)` summatory bound using Selberg symmetry;
3. exact bare charge `Y_circ=3` on the aligned balanced cone;
4. lower-order `Y_circ T_circ` cross term;
5. cofinal positivity of the source-augmented innovation curvature;
6. coefficient-one absorption of the complete product curvature.

Open:

1. an upper/coefficient-one delayed recurrence for `A_circ`;
2. a global physical block energy bound;
3. RH.
