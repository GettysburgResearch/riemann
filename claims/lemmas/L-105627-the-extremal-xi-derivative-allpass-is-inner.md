# L-105627 — Every zero-free-height Xi derivative all-pass is inner

Claim ID: `L-105627`  
Status: **PROVED XI-SPECIFIC CANONICAL-PRODUCT THEOREM; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: `L-105062`; `L-105418`; `L-105442`; the standard Xi Fourier kernel  
RH status: **not assumed**

## 1. Total-height shift

Let

\[
F_r=\Xi^{(r)},
\qquad
\beta_r=\sup\{\Im z:F_r(z)=0\}.
\]

Fix one total physical height

\[
\boxed{H\ge\beta_{r+1}.}
\tag{L-105627.1}
\]

Put

\[
D_{r,H}(z)=F_{r+1}(z+iH)
\]

and

\[
D_{r,H}^{\#}(z)
=\overline{D_{r,H}(\overline z)}.
\]

After cancelling common real zeros, define

\[
\boxed{
U_{r,H}(z)
={D_{r,H}^{\#}(z)\over D_{r,H}(z)}.
}
\tag{L-105627.2}
\]

The extremal-base case used later is `H=beta_r+h`, because
`beta_(r+1)<=beta_r` and `h>0`.

## 2. Analyticity and boundary modulus

Equation (L-105627.1) implies that every zero of `D_(r,H)` lies in the
closed lower half-plane. Hence the quotient in (L-105627.2), after removable
real factors are cancelled, is analytic in the open upper half-plane.

For real `x`,

\[
D_{r,H}^{\#}(x)=\overline{D_{r,H}(x)},
\]

so

\[
\boxed{|U_{r,H}(x)|=1}
\tag{L-105627.3}
\]

at every regular boundary point.

## 3. Canonical product orientation

Every Xi derivative is a real entire function of order one and belongs to the
Cartwright/bounded-type class in each fixed half-plane. Its shifted canonical
product shows that `U_(r,H)` is a product of:

- Blaschke factors associated with zeros of `D_(r,H)` in the lower
  half-plane;
- a possible exponential inner/outer factor `exp(i tau z)`;
- a unimodular constant.

Each zero factor has modulus at most one in the upper half-plane. It remains to
orient the exponential factor.

For `y>0`, reality and parity give

\[
|U_{r,H}(iy)|
=
{|F_{r+1}(i(y-H))|
 \over
 |F_{r+1}(i(y+H))|}.
\tag{L-105627.4}
\]

The positive Xi Fourier kernel gives, up to the fixed parity phase,

\[
|F_m(iY)|
=
\begin{cases}
\displaystyle
2\int_0^\infty u^m\Phi(u)\cosh(|Y|u)\,du,&m\text{ even},\\[2mm]
\displaystyle
2\int_0^\infty u^m\Phi(u)\sinh(|Y|u)\,du,&m\text{ odd}.
\end{cases}
\tag{L-105627.5}
\]

These positive integrals are strictly increasing in `|Y|`. Since

\[
|y-H|\le y+H,
\]

one obtains

\[
\boxed{|U_{r,H}(iy)|\le1.}
\tag{L-105627.6}
\]

Therefore the exponential factor has the inner orientation `tau>=0`.

## 4. Inner-function conclusion

The canonical product now gives

\[
\boxed{
U_{r,H}\in H^\infty(\mathbb C_+),
\qquad
\|U_{r,H}\|_\infty\le1,
\qquad
|U_{r,H}(x)|=1\text{ a.e.}
}
\tag{L-105627.7}
\]

Thus `U_(r,H)` is inner. Under the Paley--Wiener transform, multiplication by
its boundary value is a causal isometry on `L^2(0,infinity)`.

The conclusion includes an unattained extremal height: for every `h>0`, the
choice `H=beta_(r+1)+h` puts all denominator zeros strictly below the shifted
boundary.

## 5. Consequence for monotone source profiles

Combining the inner/causal conclusion with `L-105625`, every nonincreasing
source profile `r_source` satisfies

\[
V_{r,H}^*M_{r_{\rm source}}V_{r,H}
\preceq M_{r_{\rm source}},
\]

where `V_(r,H)` is the Paley--Wiener realization of the actual derivative
all-pass at total height `H`.

For the base-Xi current profile at a safe base `b>=beta_0`, the total height is

\[
H=b+h,
\]

and the microscope coefficient is the scalar multiple

\[
{h\over H}
\left[
{H e^{-H\xi}\Lambda_2(\xi)\over j_H(\xi)}
\right].
\]

Its monotonicity is paid by `L-105624--L-105626`.

## 6. Scope

The theorem does not say that the all-pass is inner below the derivative zero
height. That failure is exactly the pole obstruction in the zero-height
variational principle. Nor does it identify a finite-window two-trace
observation map with the full Paley--Wiener causal isometry. Boundary zeros
require the stated removable/confluent treatment. RH remains unproved.
