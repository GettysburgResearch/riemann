# L-105627 — The extremal Xi derivative all-pass is an inner function

Claim ID: `L-105627`  
Status: **PROVED XI-SPECIFIC CANONICAL-PRODUCT THEOREM; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: `L-105062`; `L-105418`; `L-105442`; the standard Xi Fourier kernel  
RH status: **not assumed**

## 1. Extremal shift

Let

\[
F_r=\Xi^{(r)},
\qquad
\beta_r=\sup\{\Im z:F_r(z)=0\}.
\]

The derivative zero heights satisfy

\[
\beta_{r+1}\le\beta_r.
\tag{L-105627.1}
\]

Put

\[
D_{r,\beta}(z)=F_{r+1}(z+i\beta_r)
\]

and

\[
D_{r,\beta}^{\#}(z)
=\overline{D_{r,\beta}(\overline z)}.
\]

After cancelling common real zeros, define

\[
\boxed{
U_{r,\beta}(z)
={D_{r,\beta}^{\#}(z)\over D_{r,\beta}(z)}.
}
\tag{L-105627.2}
\]

## 2. Analyticity and boundary modulus

Equation (L-105627.1) implies that every zero of `D_(r,beta)` lies in the
closed lower half-plane. Hence the quotient in (L-105627.2), after removable
real factors are cancelled, is analytic in the open upper half-plane.

For real `x`,

\[
D_{r,\beta}^{\#}(x)=\overline{D_{r,\beta}(x)},
\]

so

\[
\boxed{|U_{r,\beta}(x)|=1}
\tag{L-105627.3}
\]

at every regular boundary point.

## 3. Canonical product orientation

Every Xi derivative is a real entire function of order one and belongs to the
Cartwright/bounded-type class in each fixed half-plane. Its shifted canonical
product shows that `U_(r,beta)` is a product of:

- Blaschke factors associated with zeros of `D_(r,beta)` in the lower
  half-plane;
- a possible exponential inner/outer factor `exp(i tau z)`;
- a unimodular constant.

Each zero factor has modulus at most one in the upper half-plane. It remains to
orient the exponential factor.

For `y>0`, reality and parity give

\[
|U_{r,\beta}(iy)|
=
{|F_{r+1}(i(y-\beta_r))|
 \over
 |F_{r+1}(i(y+\beta_r))|}.
\tag{L-105627.4}
\]

The positive Xi Fourier kernel gives, up to the fixed parity phase,

\[
|F_m(iY)|
=
\begin{cases}
\displaystyle
2\int_0^\infty u^m\Phi(u)\cosh(Yu)\,du,&m\text{ even},\\[2mm]
\displaystyle
2\int_0^\infty u^m\Phi(u)\sinh(Yu)\,du,&m\text{ odd},
\end{cases}
\tag{L-105627.5}
\]

with the absolute value and odd parity interpreted symmetrically for negative
`Y`. These positive integrals are strictly increasing in `|Y|`. Since

\[
|y-\beta_r|\le y+\beta_r,
\]

one obtains

\[
\boxed{|U_{r,\beta}(iy)|\le1.}
\tag{L-105627.6}
\]

Therefore the exponential factor has the inner orientation `tau>=0`.

## 4. Inner-function conclusion

The canonical product now gives

\[
\boxed{
U_{r,\beta}\in H^\infty(\mathbb C_+),
\qquad
\|U_{r,\beta}\|_\infty\le1,
\qquad
|U_{r,\beta}(x)|=1\text{ a.e.}
}
\tag{L-105627.7}
\]

Thus `U_(r,beta)` is inner. Under the Paley--Wiener transform, multiplication
by its boundary value is a causal isometry on `L^2(0,infinity)`.

The conclusion remains valid when the extremal height is not attained. In that
case the denominator is zero-free even on the boundary except for possible
lower-height projections; no top-line zero factor is needed.

## 5. Consequence for the current–Turán profile

Combining the inner/causal conclusion with `L-105625`, every nonincreasing
source profile `r` satisfies

\[
V_{r,\beta}^*M_rV_{r,\beta}\preceq M_r,
\]

where `V_(r,beta)` is the Paley--Wiener realization of the actual derivative
all-pass.

For the canonical Xi profile, monotonicity is paid by
`L-105624--L-105626`. Hence the actual extremal-base all-pass phase is favorable
in the infinite-line one-sided current-normalized energy.

## 6. Scope

The theorem does not identify a finite-window two-trace observation map with
the full Paley--Wiener causal isometry. Boundary zeros require the stated
removable/confluent treatment. It does not control horizontal endpoints,
finite tapers, or prove the pointwise microscope sign. RH remains unproved.
