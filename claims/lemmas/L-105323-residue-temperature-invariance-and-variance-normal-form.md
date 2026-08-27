# L-105323 — Residue temperature is invariant under differentiation

Claim ID: `L-105323`  
Status: **PROPOSED EXACT FINITE-ALGEBRA THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105300`; PR #720 `L-104524`; `L-105320`  
RH status: **not assumed**

## 1. A derivative-invariant centered root quantity

Let `p` be monic of degree `n>=3`, with roots `z_1,...,z_n` counted with
multiplicity. Put

\[
\bar z={1\over n}\sum_{j=1}^{n}z_j,
\qquad
V_2(p)=\sum_{j=1}^{n}(z_j-\bar z)^2,
\]

and define the normalized centered second moment

\[
\boxed{
\mathcal T(p)={V_2(p)\over n(n-1)}.
}
\tag{L-105323.1}
\]

Normalize the derivative to be monic:

\[
q={p'\over n}.
\]

Then

\[
\boxed{
V_2(q)={n-2\over n}V_2(p),
\qquad
\mathcal T(q)=\mathcal T(p).
}
\tag{L-105323.2}
\]

Thus `mathcal T` is exactly invariant under every derivative step for which
the degree is at least three.

### Proof

Write

\[
p(z)=z^n-s_1z^{n-1}+e_2z^{n-2}+\cdots.
\]

The root sum and second elementary symmetric coefficient of `q` are

\[
s_1(q)={n-1\over n}s_1,
\qquad
e_2(q)={n-2\over n}e_2.
\]

For a monic degree-`d` polynomial,

\[
V_2={d-1\over d}s_1^2-2e_2.
\]

Substitution with `d=n-1` gives

\[
V_2(q)
={n-2\over n}
\left[{n-1\over n}s_1^2-2e_2\right]
={n-2\over n}V_2(p).
\]

Division by `(n-1)(n-2)` proves the invariant.

Equivalently,

\[
\boxed{
\mathcal T(p)
={1\over n^2(n-1)}
\sum_{1\le i<j\le n}(z_i-z_j)^2.
}
\tag{L-105323.3}
\]

For distinct real roots this quantity is strictly positive.

## 2. Exact first-residue spectral flow

Assume `p'` is squarefree and define the critical residues

\[
\rho_c={p(c)\over p''(c)},
\qquad p'(c)=0.
\]

The first residue identity gives

\[
-\sum_{p'(c)=0}\rho_c={V_2(p)\over n^2}.
\]

Hence

\[
\boxed{
A(p):=-\operatorname{Tr}U_p
={n-1\over n}\mathcal T(p).
}
\tag{L-105323.4}
\]

Applying the same identity to `q=p'/n` and using (L-105323.2),

\[
\boxed{
A(q)
={n-2\over n-1}\mathcal T(p)
={n(n-2)\over(n-1)^2}A(p).
}
\tag{L-105323.5}
\]

Thus the relative first-moment loss in one derivative step is exactly

\[
\boxed{
1-{A(q)\over A(p)}={1\over(n-1)^2}.
}
\tag{L-105323.6}
\]

It is a square-summable degree loss, not an uncontrolled multiplicative
constant.

For the monic derivative ladder

\[
p_r={p^{(r)}\over n(n-1)\cdots(n-r+1)},
\qquad d_r=n-r,
\]

one has, whenever the required critical points are simple,

\[
\boxed{
\mathcal T(p_r)=\mathcal T(p),
\qquad
A(p_r)={d_r-1\over d_r}\mathcal T(p).
}
\tag{L-105323.7}
\]

Equivalently,

\[
\boxed{
{d_r\over d_r-1}A(p_r)=\mathcal T(p)
}
\tag{L-105323.8}
\]

is an exact conserved first-residue carrier across the complete finite
derivative ladder.

## 3. Coherence is exactly normalized inverse-curvature variance

Assume now that `p` has distinct real roots. Put

\[
a_c=-\rho_c>0,
\qquad
R=n-1.
\]

By (L-105323.4), the exact mean residue magnitude is

\[
\boxed{
{1\over R}\sum_ca_c={\mathcal T(p)\over n}.
}
\tag{L-105323.9}
\]

Define the dimensionless inverse-curvature variables

\[
\boxed{
\alpha_c={n a_c\over\mathcal T(p)}.
}
\tag{L-105323.10}
\]

They satisfy

\[
{1\over R}\sum_c\alpha_c=1.
\tag{L-105323.11}
\]

Let

\[
\operatorname{Var}_p(\alpha)
={1\over R}\sum_c(\alpha_c-1)^2.
\]

The residue coherence becomes

\[
\begin{aligned}
\mathfrak C(p)
&={\left(\sum_ca_c\right)^2\over R\sum_ca_c^2}\\
&={1\over R^{-1}\sum_c\alpha_c^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathfrak C(p)
={1\over1+\operatorname{Var}_p(\alpha)},
}
\tag{L-105323.12}
\]

and exactly

\[
\boxed{
{1-\mathfrak C(p)\over\mathfrak C(p)}
=\operatorname{Var}_p(\alpha).
}
\tag{L-105323.13}
\]

Thus coherence is not an opaque two-moment ratio. It is the inverse of one
plus the variance of the local inverse curvatures after normalization by the
single derivative-invariant carrier `mathcal T`.

## 4. Reverse-Rolle and compression consequences

Let `E(p)` be the number of wrong real extrema. The exact coherence inequality
gives

\[
E(p)\le R(1-\mathfrak C(p)).
\]

Using (L-105323.12),

\[
\boxed{
E(p)
\le
R{\operatorname{Var}_p(\alpha)
 \over1+\operatorname{Var}_p(\alpha)}
\le R\operatorname{Var}_p(\alpha).
}
\tag{L-105323.14}
\]

The angle in `L-105320` obeys the sharper normal form

\[
\boxed{
\sin^2\theta_p
\le
\min\left(1,\operatorname{Var}_p(\alpha)\right).
}
\tag{L-105323.15}
\]

Hence the same normalized inverse-curvature variance controls both:

```text
wrong-extremum creation in reverse Rolle;
and
spectral mismatch between the actual derivative and physical Krylov flow.
```

## 5. Xi interpretation

For a real-rooted finite approximation to one Xi derivative, the quantity
`mathcal T` is one common carrier for every lower derivative of that same
finite polynomial. The high-derivative saddle theorem predicts

\[
a_c=w_m^{-2}(1+o(1)),
\]

which is equivalent to

\[
\alpha_c=1+o(1)
\]

once the conserved carrier is matched to the saddle moments. The low-order
problem is therefore a **variance-production problem around a conserved
carrier**, not a decay problem for the first residue moment.

## 6. Scope

The invariant is an exact algebraic statement for finite polynomials. For
complex roots, `mathcal T` and the algebraic residue sum need not be positive.
The variance and wrong-extremum conclusions require a real-rooted parent.
Canonical-product localization, Xi boundary winding, and the cumulative
low-order variance budget remain open. RH is not proved.
