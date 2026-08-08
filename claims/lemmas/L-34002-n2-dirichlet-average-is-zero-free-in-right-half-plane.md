# L-34002 — The first nontrivial raw Brownian Dirichlet average is zero-free in the right half-plane

Claim ID: `L-34002`  
Title: For `N=2`, the Dirichlet-average Mellin transform has no zero in `Re z>=0`, hence the raw Brownian factor is zero-free in `Re s>=0`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Issue: #340  
Dependencies: `L-34001`  
Scope: exact `N=2` stability control; no cofinal or RH conclusion

## 1. The `N=2` Dirichlet average

For `N=2`,

\[
(W_1,W_2)\sim\operatorname{Dirichlet}(2,2),
\]

so `W_1` has density

\[
6w(1-w),\qquad0<w<1.
\]

The average is

\[
Q_2=W_1+\frac14W_2
=\frac14+\frac34W_1.
\]

After the change of variable

\[
q=\frac14+\frac34w,
\]

its density on `[1/4,1]` is

\[
\boxed{
f_{Q_2}(q)=\frac{32}{9}(4q-1)(1-q).
}
\tag{L-34002.1}
\]

## 2. Exact Mellin transform

For every complex `z`, direct integration gives

\[
\begin{aligned}
M_2(z)
&=\mathbb E[Q_2^z]\\
&=\frac{32}{9}
\left[
-4\frac{1-4^{-(z+3)}}{z+3}
+5\frac{1-4^{-(z+2)}}{z+2}
-\frac{1-4^{-(z+1)}}{z+1}
\right].
\end{aligned}
\]

After elementary simplification,

\[
\boxed{
M_2(z)
=\frac{2\big[(48z+16)+(3z+11)4^{-z}\big]}
       {9(z+1)(z+2)(z+3)}.
}
\tag{L-34002.2}
\]

The apparent poles at `-1,-2,-3` are removable in the original entire Mellin transform; for the right-half-plane theorem they play no role.

## 3. Strict modulus domination

Let

\[
z=x+iy,
\qquad x\ge0.
\]

Since

\[
|4^{-z}|=4^{-x}\le1,
\]

it is enough to compare the two affine factors. Exact expansion gives

\[
\begin{aligned}
|48z+16|^2-|3z+11|^2
={}&2295(x^2+y^2)+1470x+135.
\end{aligned}
\tag{L-34002.3}
\]

Every term on the right is nonnegative and the constant is strictly positive. Therefore

\[
\boxed{
|(3z+11)4^{-z}|
\le|3z+11|
<|48z+16|
\qquad(x\ge0).
}
\tag{L-34002.4}
\]

The numerator in (L-34002.2) cannot vanish. Hence

\[
\boxed{
M_2(z)\ne0
\qquad(\operatorname{Re}z\ge0).
}
\tag{L-34002.5}
\]

In particular it is zero-free on the much smaller RH-facing half-plane `Re z>1/4`.

## 4. Raw Brownian consequence

By `L-34001`,

\[
D_2(s)
=\frac{\Gamma(4+s/2)}{\Gamma(4)\Gamma(1+s/2)}M_2(s/2).
\]

The gamma ratio is zero-free for `Re s>=0`. Therefore

\[
\boxed{
D_2(s)\ne0
\qquad(\operatorname{Re}s\ge0).
}
\tag{L-34002.6}
\]

This is the first nontrivial exact one-sided half-plane stability theorem for the raw Brownian truncations.

## 5. What the proof suggests

The argument has a useful form:

```text
near-endpoint polynomial contribution
+
far-endpoint exponential contribution,
```

with the near endpoint strictly dominating throughout the right half-plane. For general `N`, the Dirichlet-average density is a repeated-knot B-spline on

```text
[1/N^2,1].
```

A viable induction or endpoint-dominance theorem would generalize the same mechanism without invoking zeta.

This observation is a research direction, not a claimed all-`N` proof.

## 6. Proof boundary

Established exactly:

1. the `Q_2` density;
2. its entire Mellin transform;
3. strict right-half-plane numerator dominance;
4. `M_2` zero-free for `Re z>=0`;
5. raw `D_2` zero-free for `Re s>=0`.

Open:

1. a uniform/cofinal generalization in `N`;
2. RH.
