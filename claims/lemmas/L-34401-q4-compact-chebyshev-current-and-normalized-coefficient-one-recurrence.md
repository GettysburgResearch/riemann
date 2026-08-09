# L-34401 — Q=4 compact Chebyshev current and normalized coefficient-one recurrence

Claim ID: `L-34401`  
Title: The one-step Q=4 innovation has an exact compact Chebyshev current coordinate, and critical normalization converts any innovation-square estimate into a coefficient-one fixed-delay recurrence  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Issue: #344  
Dependencies: PR #342 `L-34001/L-34003/L-34005`; PR #341 prefix/carry identity  
Scope: exact source/current algebra and recurrence adapter; does not prove the innovation-square domination or RH

## 1. Compact one-step source

Retain the Q=4 inverse source

\[
B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
\qquad
b_4\leftrightarrow B_4.
\]

Put

\[
\boxed{
 b_\circ=(\varepsilon-\delta_4)*b_4.
}
\tag{L-34401.1}
\]

Then

\[
B_\circ(s)
=(1-4^{-s})B_4(s)
=\frac{1-4^{1-s}}{\zeta(s)}
\]

and, as already recorded on PR #342,

\[
\boxed{
\mathbf 1*b_\circ=\varepsilon-4\delta_4.
}
\tag{L-34401.2}
\]

Define the **own compact current**

\[
\boxed{
q_\circ=-b_\circ\log,
}
\tag{L-34401.3}
\]

so its Dirichlet series is `B_circ'(s)`.

## 2. Exact ordinary-Chebyshev prefix

Differentiate

\[
\zeta(s)B_\circ(s)=1-4^{1-s}.
\]

Writing

\[
\Lambda(s)=-\frac{\zeta'(s)}{\zeta(s)}
\]

and `L=log 4`, one obtains

\[
\zeta B_\circ'
= L4^{1-s}+(1-4^{1-s})\Lambda(s).
\]

Therefore coefficientwise

\[
\boxed{
\mathbf1*q_\circ
=(\varepsilon-4\delta_4)*\Lambda
 +4L\delta_4.
}
\tag{L-34401.4}
\]

If

\[
\psi(x)=\sum_{m\le x}\Lambda(m),
\]

then the prefix of the compact current is exactly

\[
\boxed{
G_\circ(X)
=\psi(X)-4\psi(\lfloor X/4\rfloor)
 +4L\,\mathbf1_{X\ge4}.
}
\tag{L-34401.5}
\]

Thus the own one-step current is an ordinary Chebyshev radix-four finite difference plus one explicit local atom. No generalized-prime tower remains in this coordinate.

By the exact prefix/carry identity of PR #341, for every integer row `n=j+k`,

\[
\boxed{
\mathcal L_{n,j}(q_\circ)
=G_\circ(n)-G_\circ(j)-G_\circ(k).
}
\tag{L-34401.6}
\]

## 3. Relation to the actual PR #342 innovation

Let

\[
\Lambda_4=-A_4'/A_4
\]

be the Q=4 generalized-prime sequence and define the actual source current used on PR #342,

\[
 i_\circ=b_\circ*\Lambda_4.
\tag{L-34401.7}
\]

Since

\[
B_\circ=(1-4^{-s})B_4,
\]

logarithmic differentiation gives

\[
\Lambda_\circ
=\Lambda_4+L\frac{4^{-s}}{1-4^{-s}},
\]

where `Lambda_circ=B_circ'/B_circ` is the own generalized-prime current. Hence

\[
\begin{aligned}
q_\circ-i_\circ
&=b_\circ*(\Lambda_\circ-\Lambda_4)\\
&=L(\varepsilon-\delta_4)*b_4*
   \frac{\delta_4}{\varepsilon-\delta_4}\\
&=L\delta_4*b_4.
\end{aligned}
\]

Therefore

\[
\boxed{
 i_\circ=q_\circ-L\delta_4*b_4.
}
\tag{L-34401.8}
\]

This keeps the exact delayed bare gauge explicit. The own compact current and the actual innovation may not be silently identified.

At the aligned row `(4n,4j)`, PR #342 proves

\[
\boxed{
I_\circ(n,j)
:=\mathcal L_{4n,4j}(i_\circ)
=Q_4^{\rm phys}(4n,4j)-Q_4^{\rm phys}(n,j).
}
\tag{L-34401.9}
\]

## 4. Critical normalized current recurrence

Define the critical normalized row current

\[
\boxed{
U(n,j)=\frac{Q_4^{\rm phys}(n,j)}{\sqrt n}.
}
\tag{L-34401.10}
\]

Since `sqrt(4n)=2sqrt(n)`, equation (L-34401.9) gives exactly

\[
\begin{aligned}
U(4n,4j)
&=\frac{Q_4^{\rm phys}(n,j)+I_\circ(n,j)}{2\sqrt n}\\
&=\boxed{
\frac12U(n,j)+\frac{I_\circ(n,j)}{2\sqrt n}.
}
\end{aligned}
\tag{L-34401.11}
\]

This is the coefficient-one critical recurrence in amplitude form. The inherited current has coefficient `1/2` because the source is normalized at the square-root critical exponent.

## 5. Sharp scalar energy adapter

For all real `a,b`,

\[
\boxed{
\left(\frac a2+b\right)^2
\le a^2+\frac43b^2.
}
\tag{L-34401.12}
\]

Indeed the difference between the right and left sides is

\[
\frac34\left(a-\frac23b\right)^2\ge0.
\]

(The constant `4/3` is the smallest possible coefficient in front of `b^2` when the coefficient of `a^2` is fixed to one.)

Apply (L-34401.12) to

\[
a=U(n,j),
\qquad
b=\frac{I_\circ(n,j)}{2\sqrt n}.
\]

Equation (L-34401.11) yields

\[
\boxed{
|U(4n,4j)|^2
\le |U(n,j)|^2
   +\frac{|I_\circ(n,j)|^2}{3n}.
}
\tag{L-34401.13}
\]

Thus a current-scale square estimate is required only for the **innovation**, not for the complete current.

## 6. Critical reserve implication

PR #342 proves, cofinally and uniformly on the quarter-balanced cone,

\[
(\log2)n\log n
\le\Delta_4R(n,j)
<480n\log(2n).
\tag{L-34401.14}
\]

Consequently any cofinal source-specific estimate

\[
\boxed{
|I_\circ(n,j)|^2
\le C\,\Delta_4R(n,j)
}
\tag{L-34401.15}
\]

with an absolute constant `C` immediately gives

\[
\boxed{
|U(4n,4j)|^2
\le |U(n,j)|^2+160C\log(2n).
}
\tag{L-34401.16}
\]

Iterating along an aligned radix-four chain of length `O(log X)` therefore produces only an `O_C(log^2 X)` pointwise normalized-energy increase, plus the explicit finite base.

This is already of subpower size. The existing atomized physical/carry localization can then consume such a coefficient-one fixed-delay recurrence once (L-34401.15) is established in the complete source-bound block.

## 7. Why this is sharper than the previous frontier

The live Q=4 route no longer needs a strict contraction of the principal zeta mode. The exact normalized recurrence is neutral at coefficient one:

```text
complete current at scale 4n
 = one-half inherited amplitude
   + one-half normalized innovation.
```

The deterministic reserve created at the same step has exactly the critical size `Theta(n log n)`. Therefore the irreducible theorem is the dimensionless innovation domination (L-34401.15), not an oversized quadratic reserve or a source-blind spectral gap.

The compact Chebyshev formula (L-34401.5) and delayed-gauge identity (L-34401.8) are the preferred coordinates for attacking that theorem.

## 8. Proof boundary

Established exactly here:

1. the compact one-step source;
2. the own-current Chebyshev prefix formula;
3. the distinction between own current and actual innovation;
4. the delayed bare gauge;
5. the critical normalized amplitude recurrence;
6. the sharp coefficient-one energy adapter;
7. `innovation domination -> O(log^2 X)` fixed-delay forcing.

Open:

1. the source-specific domination (L-34401.15);
2. the resulting global physical block recurrence;
3. RH.
