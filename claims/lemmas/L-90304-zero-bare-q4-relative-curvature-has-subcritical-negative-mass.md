# L-90304 — The zero-bare relative Q4 curvature has only subcritical negative spectral mass

Claim ID: `L-90304`  
Title: One further radix-four source difference kills the bare coordinate exactly; the remaining two-state curvature may be indefinite but its negative eigenvalue is `O(n/log n)` uniformly on every fixed balanced cone  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90301`–`L-90303`; PR #345 `L-34406/L-34410`; classical Selberg symmetry and Chebyshev bound  
Scope: cofinal balanced row / finite-state curvature defect; no complete block recurrence or RH conclusion

## 1. Use the compact source system before the extra source difference

Retain the compact main-pole source

\[
 B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)},
 \qquad A_\sharp=B_\sharp^{-1},
\]

with Jordan deformation

\[
 J_{\sharp,\tau}(s)
 =\frac{A_\sharp(s-\tau)}{A_\sharp(s)}.
\]

PR #345 `L-34406` gives, for a fixed balanced row

\[
 e=(n,j),\qquad e^+=(4n,4j),
\]

the relative first coordinate

\[
 H_e(\tau)
 =\frac{1+\mathcal L_{e^+}(J_{\sharp,\tau})}
        {1+\mathcal L_e(J_{\sharp,4\tau})}
\tag{L-90304.1}
\]

with jets

\[
 H_e(0)=1,
 \qquad H_e'(0)=E_e,
 \qquad H_e''(0)=E_e^2-R_e,
\tag{L-90304.2}
\]

where

\[
 \boxed{
 R_e=\Delta_4R_\sharp(e)
 }
\tag{L-90304.3}
\]

is the compact-source radix-four reserve increment.  On every fixed balanced cone, cofinally,

\[
 \boxed{R_e\asymp_\eta n\log n,}
\tag{L-90304.4}
\]

and

\[
 \boxed{E_e=O_\eta(\log(2n)).}
\tag{L-90304.5}
\]

In particular

\[
 \boxed{R_e-E_e^2\ge\frac12R_e>0}
\tag{L-90304.6}
\]

outside a fixed base depending only on the balanced cone.

## 2. Apply one more radix-four source difference to the source leg only

Let `b_sharp=A_sharp^{-1}` and define

\[
 \boxed{
 b_\diamond=(\varepsilon-\delta_4)*b_\sharp.
 }
\tag{L-90304.7}
\]

This is exactly the zero-bare source of PR #345 `L-34410`:

\[
 b_\diamond
 = (\varepsilon-\delta_4)
   *(\varepsilon-4\delta_4)*\mu.
\]

Define the source-convolved Jordan leg

\[
 K_{\diamond,\tau}
 =b_\diamond*J_{\sharp,\tau}
\tag{L-90304.8}
\]

and evaluate it on the scaled row

\[
 G_e(\tau)=\mathcal L_{e^+}(K_{\diamond,\tau}).
\tag{L-90304.9}
\]

Since

\[
 \mathbf1*b_\diamond
 =\varepsilon-5\delta_4+4\delta_{16},
\]

its prefix vanishes identically above sixteen.  Therefore, whenever both children of `e+` are at least sixteen,

\[
 \boxed{G_e(0)=Y_e=0.}
\tag{L-90304.10}
\]

This is exact, not asymptotic.

Differentiating (L-90304.8) at zero gives

\[
 G_e'(0)
 =\mathcal L_{e^+}((\varepsilon-\delta_4)q_\sharp)
 =Q_\sharp(e^+)-Q_\sharp(e)
 =:I_e,
\tag{L-90304.11}
\]

so the first source jet is exactly the hard aligned compact innovation, with no growing gauge.

Put

\[
 T_e
 :=G_e''(0)
 =\mathcal L_{e^+}((\varepsilon-\delta_4)t_\sharp).
\tag{L-90304.12}
\]

## 3. The zero-bare second source current is only linear

Let

\[
 \lambda(s)=-\frac{\zeta'}{\zeta}(s),
 \qquad
 \mathcal C(s)=-\lambda'(s)+\lambda(s)^2,
\]

put

\[
 x=4^{-s},\qquad L=\log4,
\]

and let `C_sharp` be the generalized Selberg coefficient series for `A_sharp`.

Since

\[
 -\frac{A_\sharp'}{A_\sharp}
 =\lambda+4L\frac{x}{1-4x},
\]

a direct differentiation gives

\[
 \boxed{
 C_\sharp
 =\mathcal C
 +8L\frac{x}{1-4x}\lambda
 +4L^2\frac{x(1+4x)}{(1-4x)^2}.
 }
\tag{L-90304.13}
\]

Moreover

\[
 \mathbf1*((\varepsilon-\delta_4)t_\sharp)
 = (\mathbf1*b_\diamond)*C_\sharp
 = (1-x)(1-4x)C_\sharp.
\]

Multiplying (L-90304.13) gives the exact identity

\[
 \boxed{
\begin{aligned}
 (1-x)(1-4x)C_\sharp
={}&(1-x)(1-4x)\mathcal C\\
 &+8Lx(1-x)\lambda\\
 &+4L^2\frac{x(1-x)(1+4x)}{1-4x}.
\end{aligned}}
\tag{L-90304.14}
\]

Let `G(X)` be the summatory function of the coefficient sequence on the left.

For the first line, classical Selberg symmetry gives

\[
 \sum_{m\le X}\mathcal C(m)=2X\log X+O(X).
\]

Hence

\[
\begin{aligned}
&G_\mathcal C(X)-5G_\mathcal C(X/4)+4G_\mathcal C(X/16)\\
&\qquad=O(X),
\end{aligned}
\tag{L-90304.15}
\]

because the `X log X` coefficients cancel exactly.  The second line of (L-90304.14) has summatory size `O(X)` by the elementary Chebyshev bound for `psi`.  The last line is supported on the four-adic tower with coefficients `O(4^r)`, and its summatory size is likewise `O(X)`.

Therefore

\[
 \boxed{G(X)=O(X).}
\tag{L-90304.16}
\]

The prefix/carry identity now gives uniformly on the balanced row

\[
 \boxed{|T_e|=O(n).}
\tag{L-90304.17}
\]

No zero-free region, RH, or cancellation in the unknown current enters this estimate.

## 4. The complete two-state curvature

Define

\[
 W_e(\tau)=(H_e(\tau),G_e(\tau)).
\tag{L-90304.18}
\]

On every sufficiently deep balanced row, its jets are

\[
 \boxed{
 W_e(0)=(1,0),
 \quad W_e'(0)=(E_e,I_e),
 \quad W_e''(0)=(E_e^2-R_e,T_e).
 }
\tag{L-90304.19}
\]

Consequently the complete polarized curvature matrix is

\[
 \boxed{
 K_e
 =\begin{pmatrix}
 R_e& E_eI_e-T_e/2\\
 E_eI_e-T_e/2&I_e^2
 \end{pmatrix}.
 }
\tag{L-90304.20}
\]

and its scalar curvature is simply

\[
 \boxed{\operatorname{tr}K_e=R_e+I_e^2>0.}
\tag{L-90304.21}
\]

Thus the troublesome bare-times-second-current term has disappeared exactly.

## 5. Exact current-independent inertia bound

Let

\[
 \delta_e=\operatorname{tr}(K_e)_-.
\]

If `K_e` is positive semidefinite then `delta_e=0`.  Otherwise its determinant is negative.  Since the `(1,1)` Rayleigh quotient equals `R_e>0`, the positive eigenvalue obeys

\[
 \lambda_+(K_e)\ge R_e.
\]

Hence

\[
 \delta_e=-\lambda_-(K_e)
 =\frac{-\det K_e}{\lambda_+(K_e)}
 \le\frac{-\det K_e}{R_e}.
\tag{L-90304.22}
\]

Now

\[
 \det K_e
 =R_eI_e^2-(E_eI_e-T_e/2)^2.
\]

Therefore

\[
 \delta_e
 \le
 \left[
 \frac{(T_e-2E_eI_e)^2}{4R_e}-I_e^2
 \right]_+.
\tag{L-90304.23}
\]

Put

\[
 H_e^*=R_e-E_e^2>0.
\]

Completing the square in the unknown current `I_e` gives exactly

\[
\begin{aligned}
&\frac{(T_e-2E_eI_e)^2}{4R_e}-I_e^2\\
&\qquad=
 -\frac{H_e^*}{R_e}
 \left(I_e+\frac{T_eE_e}{2H_e^*}\right)^2
 +\frac{T_e^2}{4H_e^*}.
\end{aligned}
\tag{L-90304.24}
\]

Thus the RH-sensitive current disappears from the upper bound:

\[
 \boxed{
 \delta_e
 \le\frac{T_e^2}{4(R_e-E_e^2)}.
 }
\tag{L-90304.25}
\]

This is the load-bearing conclusion.

## 6. Cofinal size

Use (L-90304.4)--(L-90304.6) and (L-90304.17).  Uniformly on every fixed balanced cone,

\[
 \boxed{
 \delta_e=O_\eta\!\left(\frac{n}{\log n}\right).
 }
\tag{L-90304.26}
\]

After critical physical normalization by the parent size, the complete negative spectral mass is only

\[
 \boxed{O_\eta(1/\log n).}
\tag{L-90304.27}
\]

while the positive deterministic reserve is of logarithmic size.

Therefore the full polarized PSD condition at this source is not RH-strength: the matrix may remain indefinite, but its entire bad direction is unconditionally lower order and independent of the unknown first current.

## 7. Relation to Claude's inertia mechanism

The conceptual import from Claude's two-thirds theorem is now realized source-specifically rather than metaphorically.

Claude retains each hyperbolic off-line block and controls only the inertia information needed by the finite compression.  Here the extra source difference creates a two-state Q4 curvature with exact zero bare coordinate.  Instead of proving the curvature matrix PSD, we retain its possible negative eigenvalue and prove directly that its mass is `O(n/log n)`.

This is strictly stronger progress than the generic reduction `L-90301`: the Q4 inertia defect itself is now bounded cofinally at row scope.

## 8. What this closes and what remains

Closed here, subject to review:

1. exact zero-bare relative Jordan source leg;
2. exact identification of its first current with the hard compact innovation;
3. exact filtered second-current identity;
4. unconditional `T_e=O(n)`;
5. exact two-state curvature matrix;
6. current-independent bad-eigenvalue bound;
7. `delta_e=O(n/log n)` on fixed balanced cones.

Still open:

1. inserting this lower-order inertia defect into the **complete independent-frequency block synthesis** with all finite collars and delayed states;
2. the resulting coefficient-one global recurrence;
3. RH.

The next proof step is now bookkeeping/operator composition rather than a new RH-scale current estimate.