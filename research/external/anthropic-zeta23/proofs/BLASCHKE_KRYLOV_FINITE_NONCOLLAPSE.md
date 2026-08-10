# Blaschke–Krylov finite-packet noncollapse

Status: **PROPOSED COMPLETE EXACT THEOREM — independent review required**  
Date: 2026-08-10  
Continuation of: PR #364 finite off-line isolation and PR #363 off-line pair spectrum  
RH status: **unproved**

## 1. Half-plane inner delay

Work in centered coordinates \(z=s-\tfrac12\), with reflection

\[
z^\#=-\overline z.
\]

For \(0<a<1\), \(L>0\), and a real phase \(\eta\), put

\[
\boxed{
\phi(z)=
\frac{a-e^{i\eta}e^{-Lz}}
     {1-ae^{i\eta}e^{-Lz}}.
}
\tag{BK.1}
\]

Then

\[
|\phi(iy)|=1,\qquad |\phi(z)|<1\quad(\Re z>0),
\tag{BK.2}
\]

and the reflection law is exact:

\[
\boxed{
\phi(z^\#)=\frac1{\overline{\phi(z)}}.
}
\tag{BK.3}
\]

The Q4 Euler–Blaschke factor of PR #325 is the special case
\(a=\tfrac12\), \(L=\log4\), \(\eta=0\).

## 2. Scalar inner powers do not amplify a reflected pair

Let

\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
D_k(w)=
\begin{pmatrix}
w^k&0\\
0&\overline w^{-k}
\end{pmatrix}.
\]

Equation (BK.3) gives

\[
\boxed{
D_k(w)^*JD_k(w)=J.
}
\tag{BK.4}
\]

Thus multiplying one scalar Weil test by \(\phi^k\) leaves the complete
reflected-pair contribution unchanged. Any argument claiming a free
exponential gain from a scalar inner power is false.

This is consistent with PR #363: a coherently closed same-lattice window bank
has the same nonzero spectrum as its scalar aggregate.

## 3. The open Krylov evaluation bank

For \(k\ge1\), define

\[
u_k(w)=(1,w,\ldots,w^{k-1}).
\tag{BK.5}
\]

Let \(0<|w|=r<1\), and put

\[
u=u_k(w),\qquad
v=u_k(\overline w^{-1}).
\]

Then

\[
A_k(r)=\|u\|^2=\sum_{j=0}^{k-1}r^{2j},
\tag{BK.6}
\]

\[
\|v\|^2=r^{-2(k-1)}A_k(r),
\tag{BK.7}
\]

and, crucially,

\[
\langle u,v\rangle=k.
\tag{BK.8}
\]

For a reflected zero pair of multiplicity \(m\), the open channel block is

\[
H_k=m(uv^*+vu^*).
\tag{BK.9}
\]

Its two nonzero eigenvalues are exactly

\[
\boxed{
\lambda_\pm
=
m\left(
k\pm A_k(r)r^{-(k-1)}
\right).
}
\tag{BK.10}
\]

Writing \(r=e^{-\tau}\),

\[
A_k(r)r^{-(k-1)}
=
\frac{\sinh(k\tau)}{\sinh\tau}.
\tag{BK.11}
\]

Hence the negative moat is

\[
\boxed{
-\lambda_-
=
m\left[
\frac{\sinh(k\tau)}{\sinh\tau}-k
\right]>0
\quad(k\ge2,\ \tau>0).
}
\tag{BK.12}
\]

For \(k\tau\ll1\),

\[
-\lambda_-
=
\frac{m\,k(k^2-1)}6\tau^2+O_m(k^5\tau^4),
\tag{BK.13}
\]

while for fixed \(\tau>0\) it grows exponentially in \(k\).

The exponential number in (BK.12) belongs to the **open evaluation bank**.
It is not a free gain for the completely closed physical compression; the
missing state/collar is load bearing.

## 4. Exact target-pair interpolation cost

The target-pair evaluation Gram is

\[
G_k(r)=
\begin{pmatrix}
A_k(r)&k\\
k&r^{-2(k-1)}A_k(r)
\end{pmatrix}.
\tag{BK.14}
\]

It is positive definite for \(k\ge2\), \(r<1\). The minimum coefficient norm
for the interpolation values

\[
p(w)=1,\qquad
p(\overline w^{-1})=-1
\]

is

\[
\boxed{
C_k(r)
=
(1,-1)G_k(r)^{-1}(1,-1)^T
=
\frac{
A_k(r)+r^{-2(k-1)}A_k(r)+2k
}{
A_k(r)^2r^{-2(k-1)}-k^2
}.
}
\tag{BK.15}
\]

Although the open-pair negative eigenvalue grows exponentially, the capture
cost does not. In fact

\[
\boxed{
\lim_{k\to\infty}C_k(r)=1-r^2.
}
\tag{BK.16}
\]

Thus a reflected pair can be separated by one scalar polynomial in the inner
coordinate with bounded Hardy/model-space cost.

## 5. Exact model-space state kernel

The one-step defect kernel is

\[
\boxed{
K_\phi(z,w)
=
\frac{1-\phi(z)\overline{\phi(w)}}{z+\overline w}
=
(1-a^2)
\frac{
1-e^{-L(z+\overline w)}
}{
(z+\overline w)
(1-ae^{i\eta}e^{-Lz})
(1-ae^{-i\eta}e^{-L\overline w})
}.
}
\tag{BK.17}
\]

For every \(k\),

\[
\boxed{
K_{\phi^k}(z,w)
=
K_\phi(z,w)
\sum_{j=0}^{k-1}
\phi(z)^j\overline{\phi(w)^j}.
}
\tag{BK.18}
\]

Equation (BK.18) is the exact \(k\)-state innovation ledger. It shows where the
open-bank gain lives. Closing the all-pass colligation without retaining these
states restores the scalar \(J\)-unitary invariance (BK.4).

## 6. Finite-packet noncollapse theorem

Let a finite zero packet contain:

1. one target reflected pair \(z_0,z_0^\#\), with
   \(w_0=\phi(z_0)\), \(0<r_0=|w_0|<1\);
2. finitely many other right-half-plane points \(z_i\), their reflections, and
   finitely many critical-line points;
3. distinct inner coordinates;
4. the strict depth ordering
   \[
   |w_0|<|w_i|
   \quad\text{for every other right-half-plane nuisance point.}
   \tag{BK.19}
   \]

Let \(V_k\) be the evaluation matrix whose row at a point \(z\) is
\(u_k(\phi(z))\), and put

\[
K_k=V_kV_k^*.
\tag{BK.20}
\]

For all sufficiently large \(k\), \(K_k\) is positive definite. Partition its
target pair from all nuisance rows and let \(S_k\) be the target Schur
complement.

Let \(s_+>0\) be the Schur complement at \(w_0\) in the finite Szegő matrix

\[
\left(\frac1{1-w_i\overline w_j}\right)
\tag{BK.21}
\]

formed by \(w_0\) and the other right-half-plane nuisance coordinates. Then

\[
\boxed{
(1,-1)S_k^{-1}(1,-1)^T
\longrightarrow
\frac1{s_+}<\infty.
}
\tag{BK.22}
\]

### Proof

Order the evaluation rows into:

- right-half-plane rows \(u_k(w)\);
- reflected rows \(u_k(\overline w^{-1})\);
- critical-line rows \(u_k(\omega)\), \(|\omega|=1\).

For right-half-plane rows,

\[
\langle u_k(w_i),u_k(w_j)\rangle
\longrightarrow
\frac1{1-w_i\overline w_j}.
\tag{BK.23}
\]

The limiting Szegő matrix is positive definite at distinct points.

For one reflected row, multiply by \(\overline w^{\,k-1}\) and reverse the
\(k\) coefficient coordinates. Up to an irrelevant unimodular scalar, the row
becomes

\[
(1,\overline w,\ldots,\overline w^{\,k-1}),
\]

so the scaled reflected block also converges to a positive Szegő matrix.

Every scaled right/reflected cross entry tends to zero: depending on the
relative moduli it is bounded by either \(O(|w_i|^k)\) or \(O(|w_j|^k)\).
The critical-line Gram is \(kI+O(1)\) after duplicate phases are removed.
Its correlations with an inside row are bounded; its correlations with a
scaled reflected row are bounded. Consequently eliminating the finite
critical-line block changes the two Szegő limits by \(O(k^{-1})\).

Therefore, with

\[
D_k=\operatorname{diag}(1,\overline w_0^{\,k-1}),
\]

\[
D_kS_kD_k^*
\longrightarrow
\begin{pmatrix}
s_+&0\\
0&s_-
\end{pmatrix}
\tag{BK.24}
\]

for a second positive reflected Szegő Schur value \(s_->0\). Hence

\[
(1,-1)S_k^{-1}(1,-1)^T
=
(1,-\overline w_0^{\,k-1})
(D_kS_kD_k^*)^{-1}
(1,-w_0^{k-1})^T
\longrightarrow s_+^{-1}.
\]

This proves (BK.22).

For right-half nuisance points \(v_1,\ldots,v_q\), the Schur value has the
closed Blaschke-product form

\[
\boxed{
s_+
=
\frac1{1-|w_0|^2}
\prod_{\ell=1}^q
\left|
\frac{w_0-v_\ell}{1-\overline v_\ell w_0}
\right|^2.
}
\tag{BK.25}
\]

It is strictly positive for every finite distinct packet.

## 7. Generic inner coordinate selection

For a finite collection of distinct points, choose \(L\) outside the finite set
of delay aliases

\[
L(\Im z_i-\Im z_j)\in2\pi\mathbb Z.
\]

For this \(L\), the functions
\(\eta\mapsto|\phi_{a,L,\eta}(z_i)|^2\) are real analytic. Pairwise equality is
not an identity unless the two delayed points coincide. Hence all but finitely
many phase values give distinct interior moduli and distinct inner coordinates.

Therefore, if a finite packet contains any off-line zero, one can choose an
inner delay coordinate for which some off-line pair is the unique
minimum-modulus pair, and the theorem applies.

## 8. Compact-test approximation

The inner factor has the stable causal expansion

\[
\phi(z)
=
a-(1-a^2)
\sum_{n\ge1}
a^{n-1}e^{in\eta}e^{-nLz}.
\tag{BK.26}
\]

For fixed \(k\), every polynomial \(p(\phi)\) has an exponentially decaying
causal delay expansion. Truncating that expansion gives compact tests converging
in the Hardy norm and uniformly on every fixed finite zero packet separated
from the boundary.

Thus the bounded finite-packet capture in (BK.22) is not merely formal: it can
be approximated by admissible compact finite-delay tests with arbitrarily small
perturbation of the pair values and coefficient norm.

## 9. Consequence for PR #364

PR #364 exposed two possible survival mechanisms for a hypothetical off-line
pair:

```text
persistent corrected-kernel/tail floor;
collapse of the finite zero-interpolation metric.
```

The present theorem removes the second mechanism at **every fixed finite
packet** after a generic Blaschke–Krylov reparameterization:

\[
\boxed{
\text{finite nuisance packet}
\quad\Longrightarrow\quad
\sup_k C_{Z,k}(1,-1)<\infty
\text{ along a cofinal Krylov subsequence}.
}
\tag{BK.27}
\]

The remaining theorem is no longer local Gram conditioning. It is a
dependency-preserving passage to the complete zero set:

> construct a joint packet/support schedule for which the compact-test
> truncation error, corrected arithmetic floor, and unseen-zero tail tend to
> zero while the Blaschke–Krylov capture norm remains bounded.

If that full-tail passage holds, PR #364 gives

\[
W(f_k,f_k)\le -2m+o(1)<0,
\]

contradicting Weil positivity and proving RH.

## 10. Scope firewall

This file does **not** claim that the full-tail passage has been proved.

Do not infer it from:

- scalar inner powers, which are exactly \(J\)-unitary;
- coherent same-lattice channels, which collapse by PR #363;
- the exponential open-bank eigenvalue without its state/collar;
- finite-packet bounded capture alone;
- a tail estimate obtained after changing the test.

The completed contribution is the exact finite-packet noncollapse theorem and
the removal of local interpolation conditioning as an independent obstruction.
