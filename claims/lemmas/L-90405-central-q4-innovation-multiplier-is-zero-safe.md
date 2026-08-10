# L-90405 — The central Q4 compact-innovation multiplier is zero-safe throughout the open critical strip

Claim ID: `L-90405`  
Status: **PROPOSED COMPLETE EXACT SPECTRAL-MULTIPLIER LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: PR #345 `L-34401`; `T-90404`  
Scope: exact monomial/Dirichlet pole visibility; no energy estimate and no proof of RH

## 1. The aligned radix-four error filter

For a complex exponent `z` and a split

\[
n=j+k,
\qquad
\theta=\frac jn\in(0,1),
\]

apply the own-current Chebyshev-error operator of `T-90404.5` to the monomial

\[
E_z(x)=x^z.
\]

Ignoring the explicit constant atom, which has no spectral exponent, define

\[
\begin{aligned}
\mathscr F_z(n,j)
={}&E_z(4n)-E_z(4j)-E_z(4k)\\
&-4\bigl(E_z(n)-E_z(j)-E_z(k)\bigr).
\end{aligned}
\tag{L-90405.1}
\]

Homogeneity gives exactly

\[
\boxed{
\mathscr F_z(n,j)
=(4^z-4)n^z
\bigl[1-\theta^z-(1-\theta)^z\bigr].
}
\tag{L-90405.2}
\]

Thus the radial scale filter and the additive carry filter factor completely.

## 2. Central row

At the central balanced row `j=k=n/2`,

\[
\boxed{
\mathscr F_z(n,n/2)
=M_4(z)n^z,
\qquad
M_4(z)=(4^z-4)(1-2^{1-z}).
}
\tag{L-90405.3}
\]

Equivalently,

\[
M_4(z)=4^z-2^{z+1}-4+2^{3-z}.
\]

## 3. No zero in the open critical strip

Suppose

\[
0<\Re z<1.
\]

If `4^z-4=0`, then taking absolute values gives

\[
4^{\Re z}=4,
\]

so `Re z=1`, contradiction.

If `1-2^{1-z}=0`, then taking absolute values gives

\[
2^{1-\Re z}=1,
\]

again forcing `Re z=1`.

Therefore

\[
\boxed{
M_4(z)\ne0
\qquad(0<\Re z<1).
}
\tag{L-90405.4}
\]

More quantitatively, for `beta=Re z<1`, the reverse triangle inequality gives

\[
\boxed{
|M_4(z)|
\ge(4-4^\beta)(2^{1-\beta}-1)>0.
}
\tag{L-90405.5}
\]

The bound degenerates only as `beta` approaches the boundary line one, not on any closed substrip.

## 4. The delayed bare gauge cannot cancel the leading zeta pole

The compact source multiplier is

\[
B_\circ(s)
=\frac{1-4^{1-s}}{\zeta(s)}.
\tag{L-90405.6}
\]

Let `rho` be a nontrivial zeta zero of multiplicity `m>=1`. The finite numerator is nonzero at `rho`: if `4^{1-rho}=1`, then its modulus forces `Re rho=1`, impossible for a nontrivial zero in the open strip. Hence `B_circ` has a pole of order `m` at `rho`, and its derivative—the own current `q_circ`—has a pole of order `m+1`.

The correction

\[
(\log4)\,4^{-s}B_4(s)
\]

in `i_circ=q_circ-(log4)delta_4*b_4` has only order `m` at `rho`. It cannot cancel the leading order-`m+1` pole. Consequently

\[
\boxed{
I_\circ\text{ retains every nontrivial zeta-zero pole.}
}
\tag{L-90405.7}
\]

The central-row multiplier (L-90405.4) is the explicit finite-difference version of the same zero-safety statement.

## 5. Consequence for PIG

A polynomial positive-innovation energy bound cannot hold because the compact filter accidentally annihilates the off-line zero one is trying to exclude: no such blind exponent exists in the open strip, and the source current has strictly higher pole order than its delayed gauge.

This explains why `T-90404` reaches an RH-equivalent gate rather than a weakened zero statement. It does not supply the required upper bound.

## 6. Proof boundary

Closed exactly:

1. factorization (L-90405.2);
2. the central multiplier (L-90405.3);
3. nonvanishing throughout `0<Re z<1`;
4. the explicit lower bound (L-90405.5);
5. leading-pole zero safety against the delayed gauge.

Open:

1. unconditional polynomial positive-innovation energy;
2. PIG;
3. RH.
