# L-91409 — The full two-sided delayed prime packet, including the bridge, has an explicit safe Green factorization

Claim ID: `L-91409`  
Status: **PROVED EXACT FULL PRIME-SIDE CARRIER/DELAY/ORIENTATION/BRIDGE FACTORIZATION; COMPLETED BOUNDARY OPEN**  
Created: 2026-08-12  
Depends on: `L-91026`, bridge construction in `L-91032`, `L-91408`  
RH status: **unproved**

## 1. Two physical orientations

Retain

\[
 \psi_a(t)=\mathbf1_{t\ge0}
 \sum_{r\in\{1,2,4\}}P_r(t)e^{-rat},
 \qquad
 P_r(t)=A_{r,a}+B_{r,a}t.
\tag{L-91409.1}
\]

For carrier `x` and delay `delta>=0`, define the causal test

\[
 f^+_{x,\delta}(v)
 =\mathbf1_{v\ge\delta}
  e^{ix(v-\delta)}\psi_a(v-\delta).
\tag{L-91409.2}
\]

For carrier `y` and delay `eta>=0`, define the reflected anti-causal test

\[
 f^-_{y,\eta}(v)
 =\mathbf1_{v\le-\eta}
  e^{iy(v+\eta)}
  \overline{\psi_a(-v-\eta)}.
\tag{L-91409.3}
\]

The pure `++` block is `L-91408`; the pure `--` block is its reflection.  It
remains to construct the mixed block.

## 2. Mixed overlap across one prime jump

For `u>0`, put

\[
 k^{+-}_{i,j}(u)
 =\int_{\mathbb R}
  f^+_i(v+u)\overline{f^-_j(v)}dv,
\tag{L-91409.4}
\]

where `i=(x,delta)` and `j=(y,eta)`.

The support conditions imply

\[
 u\ge\delta+\eta.
\]

With the change of variable

\[
 z=v+u,
\]

the overlap region is

\[
 \delta\le z\le u-\eta,
\]

and

\[
\boxed{
\begin{aligned}
 k^{+-}_{i,j}(u)
 =\sum_{r,s}
 \int_0^u &\mathbf1_{z\ge\delta}
 \mathbf1_{u-z\ge\eta}\\
 &\times e^{ix(z-\delta)}e^{iy(u-z-\eta)}\\
 &\times P_r(z-\delta)P_s(u-z-\eta)\\
 &\times e^{-ra(z-\delta)}e^{-sa(u-z-\eta)}dz.
\end{aligned}}
\tag{L-91409.5}
\]

In the opposite jump direction,

\[
 k^{+-}_{i,j}(-u)=0,
\tag{L-91409.6}
\]

because a positive-supported causal state shifted to the left cannot overlap a
negative-supported anti-causal state in that orientation.

## 3. Symmetrically split safe source space

Let

\[
 d\Pi(u)
 =\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
  \delta_{\log n}(du).
\]

For every ordered pair `r,s in {1,2,4}`, put

\[
 \mathcal Y_{r,s,a}
 =L^2\left(
  \{(u,z):0<z<u\},
  d\Pi(u)dz
 \right).
\tag{L-91409.7}
\]

Define the causal source vector

\[
\boxed{
\begin{aligned}
 A^+_{r,s;i}(u,z)
 ={}&\mathbf1_{z\ge\delta}
 e^{ix(z-\delta)}P_r(z-\delta)e^{ra\delta}\\
 &\times e^{-raz/2}e^{-sa(u-z)/2},
\end{aligned}}
\tag{L-91409.8}
\]

and the anti-causal source vector

\[
\boxed{
\begin{aligned}
 B^-_{r,s;j}(u,z)
 ={}&\mathbf1_{u-z\ge\eta}
 e^{-iy(u-z-\eta)}\overline{P_s(u-z-\eta)}e^{sa\eta}\\
 &\times e^{-sa(u-z)/2}e^{-raz/2}.
\end{aligned}}
\tag{L-91409.9}
\]

Their product is exactly the integrand in (L-91409.5):

\[
 A^+_{r,s;i}\overline{B^-_{r,s;j}}
 =\text{the `(r,s)` summand of (L-91409.5)}.
\]

Each vector lies in `Y_(r,s,a)`.  In either squared norm the exponential weight
is

\[
 e^{-raz}e^{-sa(u-z)}
 \le e^{-a u},
\]

and `e^(-a u)dPi(u)` has finite polynomial moments because `a>1/2`.

## 4. Exact mixed-orientation factorization

Let

\[
 \mathcal Y_a=\bigoplus_{r,s}\mathcal Y_{r,s,a},
\]

\[
 A_i^+=(A^+_{r,s;i})_{r,s},
 \qquad
 B_j^-=(B^-_{r,s;j})_{r,s}.
\]

Then

\[
 \boxed{
 \langle A_i^+,B_j^-\rangle_{\mathcal Y_a}
 =\int_0^\infty k^{+-}_{i,j}(u)d\Pi(u).
 }
\tag{L-91409.10}
\]

By (L-91409.6), the prime explicit-formula block is simply

\[
 \boxed{
 \mathfrak P_a^{+-}(i,j)
 =-\langle A_i^+,B_j^-\rangle.
 }
\tag{L-91409.11}
\]

The reverse block is its Hermitian adjoint:

\[
 \mathfrak P_a^{-+}(j,i)
 =\overline{\mathfrak P_a^{+-}(i,j)}.
\tag{L-91409.12}
\]

Thus every opposite-orientation carrier and delay cross term is retained in
one common positive Hilbert space.

## 5. Packet-level mixed Julia identity

For finite causal and anti-causal packets with coefficients `c_i` and `d_j`,
put

\[
 A_c^+=\sum_i c_iA_i^+,
 \qquad
 B_d^-=\sum_j d_jB_j^-.
\]

The total mixed quadratic contribution is

\[
 -2\Re\langle A_c^+,B_d^-\rangle.
\]

Therefore

\[
 \boxed{
 -2\Re\langle A_c^+,B_d^-\rangle
 =\|A_c^+-B_d^-\|^2
  -\|A_c^+\|^2
  -\|B_d^-\|^2.
 }
\tag{L-91409.13}
\]

This is the mixed-orientation Wick–Green production-minus-endpoint identity.
Combined with the two pure-orientation identities of `L-91408` and its
reflection, it factors the complete two-sided prime packet.

## 6. The bridge has the same pole modes

The frequency-side bridge components are

\[
 H_a^+(u)=\frac{\Psi_a(u)}u,
 \qquad
 H_a^-(u)=\frac{\Psi_a^\#(u)}u.
\tag{L-91409.14}
\]

Because `Psi_a(0)=0`, neither quotient has a pole at zero.  Their only poles are
the same double poles

\[
 \mp ira,
 \qquad r\in\{1,2,4\}.
\]

Hence their physical representatives have the same mode form

\[
 b_a^+(t)=\mathbf1_{t\ge0}
  \sum_r(\widetilde A_{r,a}+\widetilde B_{r,a}t)e^{-rat},
\tag{L-91409.15}
\]

\[
 b_a^-(t)=\overline{b_a^+(-t)}.
\tag{L-91409.16}
\]

The bridge

\[
 b_a=b_a^+-b_a^-
\]

is therefore inserted by the identical formulas
(L-91408.4)--(L-91408.13) and
(L-91409.8)--(L-91409.13), replacing `P_r` by the exact bridge residue
polynomials

\[
 \widetilde P_r(t)=\widetilde A_{r,a}+\widetilde B_{r,a}t.
\]

All bridge-to-carrier, bridge-to-delay, and bridge-to-opposite-orientation prime
cross terms are consequently explicit safe-space inner products.

## 7. Full prime packet theorem

Let the index set consist of

```text
all finite causal carrier/delay labels;
all finite anti-causal carrier/delay labels;
one bridge label.
```

Combining `L-91408`, its reflection, the mixed construction above, and the
bridge insertion gives an explicit direct-sum Hilbert source

\[
 \mathcal P_a^{\rm Green}
\]

and source maps

\[
 \mathcal U_a,\mathcal V_a
\]

such that the complete prime contribution on every finite packet is exactly

\[
 \boxed{
 \mathfrak P_a^{\rm full}
 =\operatorname{Gram}(\mathcal U_a-\mathcal V_a)
  -\operatorname{Gram}(\mathcal U_a)
  -\operatorname{Gram}(\mathcal V_a).
 }
\tag{L-91409.17}
\]

Here the notation packages the pure and mixed Julia identities in their common
direct-sum source.  Every metric is positive, and every sign is an explicit
production-versus-endpoint sign.

## 8. Remaining completed boundary theorem

The full delayed two-sided-plus-bridge **prime side** is now closed exactly.
The only missing source term is the completed archimedean/pole/theta boundary
kernel.

Let

\[
 \mathfrak A_a^{\rm full}
\]

be that explicit completed boundary form.  Then the full residual Weil packet
is

\[
\boxed{
\begin{aligned}
 \mathfrak W_a^{\rm full}
 ={}&\operatorname{Gram}(\mathcal U_a-\mathcal V_a)\\
 &+\Big[
  \mathfrak A_a^{\rm full}
  -\operatorname{Gram}(\mathcal U_a)
  -\operatorname{Gram}(\mathcal V_a)
 \Big].
\end{aligned}}
\tag{L-91409.18}
\]

Thus the final RH-bearing joint is one explicit completed Green boundary or
Schur-complement theorem.  No prime, carrier, delay, orientation, or bridge
cross term remains unrepresented.

## 9. Exact boundary

```text
pure causal carrier/delay prime block                EXACT
pure anti-causal block                               EXACT BY REFLECTION
mixed causal/anti-causal block                       EXACT
mixed packet Julia identity                          EXACT
bridge mode expansion                                EXACT
all bridge prime cross terms                         EXACT
full two-sided delayed prime Green source            EXACT
completed archimedean/pole boundary kernel           EXPLICIT BUT UNFACTORED
completed Green Schur complement                     OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
