# A complete smooth rectangular estimate for a coherent Möbius theta block

Date: 22 October 2026. **Proposed source-dependent component theorem.**
This controls all complementary-divisor terms, including the full divisor,
for one completed, free-inner expression. It does not establish a smaller
zero-free boundary. The completed expression must not be replaced by its
uncompleted Gauss sum or by the quadratic/sextic terminal detector.

## 1. Sources, conventions, and statement

Use the Eisenstein field, primary generators, normalized cubic Gauss sum
`g_tilde`, and angular character `alpha` of the frozen branch #1012,
commit `64cb43c038d1828a478cb97cbc32e435e111d2d2`. The analytic inputs are:

1. `type_i/FINITE_PROFILE_CLOSURE.md`: the four actual scalar profiles,
   entire continuation at fixed nonzero angular degree, and the exact
   27-cusp reflection from Dunn–Radziwill, arXiv:2109.07463v3.
2. `type_i/DUAL_RESUMMATION.md`, especially (D5): the complete signed
   Ramanujan-divisor identity, with all cube powers and deleted factors.
3. `average/ANGULAR_SELF_ABSORPTION.md`, (2): the proposed natural-count
   completed cubic second moment to the right of one-half.
4. `type_i/COHERENT_TYPE_III_INTERFACE.md`, (T1)–(T5): the retained moving
   angular phase and exact coherent reflection.
5. `type_i/SIGNED_MOBIUS_COMPLEMENT.md`, (MC5)–(MC9): the signed smooth
   complementary-variable estimate, under the common Hecke premise below.

These remain imported analytic dependencies. This note proves a new
consumer of the stated identities and estimates; it does not independently
certify their underlying automorphic proofs or claim literature priority.

Fix a nonzero angular integer `ell`. Put

\[
Q_r(s;\ell)=L_E^{(3r)}(3s-1/2,\alpha^{3\ell})
 \sum_c \widetilde g(c)\overline{(c/r)_3}
                \alpha(c)^\ell(Nc)^{-s}.
\tag{1}
\]

Rows `r` are squarefree, primary, and prime to 3. Characters are extended
by zero at nonunits. The prime above 3 and the fixed finite ray conventions
are those of the source. Let `f,W` be fixed smooth compactly supported
functions on the positive real axis, supported away from zero. Define

\[
\begin{split}
\mathcal T_{\rm comp}(A,B)
={}&\sum_r^*\mu_E(r)\widetilde g(r)\alpha(r)^\ell f(Nr/B)\,
 \frac1{2\pi i}\int_{(c)}\widehat W(s)A^sQ_r(s;\ell)\,ds,
 \qquad c>1.
\end{split}
\tag{2}
\]

The inner expression is literally the smooth completed coefficient sum

\[
\sum_{c,d}\widetilde g(c)\overline{(c/r)_3}
  \alpha(cd^3)^\ell(Nd)^{1/2}
  \mathbf1_{(d,r)=1}\,W(Nc(Nd)^3/A).
\tag{3}
\]

All common-prime zeros, cube powers, and the unrestricted smooth inner
column are retained. Fixed finite-ray factors on `r` and the four source
profiles are also allowed; they only change the finite list of reflected
components below. No arbitrary arithmetic multiplier may replace the
Möbius row coefficient or enter the free inner variable.

Suppose `1/2 <= beta <= 1` and the specific Hecke functions occurring in
the complementary Euler products have a common zero-free half-plane
`Re z > beta`, with conductor-uniform reciprocal estimates on every
strictly smaller closed half-plane. A common all-unitary Hecke theorem is
a sufficient stronger premise. Here the actual finite ray types and the
nonzero angular orders are fixed. At `beta=1`, ordinary Euler convergence
provides this premise without any quasi-RH assertion.

**Theorem.** For every `epsilon>0`, uniformly for `A >= B >= 2`,

\[
\boxed{\quad
 |\mathcal T_{\rm comp}(A,B)|
 \ll_{\ell,\beta,\epsilon,f,W}
 (AB)^\epsilon B^{3/2}
              (A/B)^{-(1-\beta/2)}.
 \quad}
\tag{4}
\]

In particular, with only the Euler-region reciprocal input,

\[
 |\mathcal T_{\rm comp}(A,B)|
       \ll (AB)^\epsilon B^2A^{-1/2}.
\tag{5}
\]

The stronger substitution `beta=B_flat` is conditional on the actual
angular Hecke premise; Liu's finite-order theorem alone does not supply it.
The exponent of `A/B` is then about `0.562556676480018`, instead of `1/2`.
Neither exponent is a zero-free boundary.

## 2. Exact reflection before any triangle inequality

Move the integral in (2) to `s=1/2-delta+it`, with `0<delta<1/4`.
The source says `Q_r` is entire at nonzero angular order, and the fixed
smooth Mellin transform absorbs its polynomial vertical growth. Apply the
complete reflection, including its finite cusp matrix and common gamma
quotient. Expand the finitely many row-class factors into ray characters.
For each resulting component, the arithmetic expression is

\[
\begin{split}
\sum_{k,m:(k,m)=1}&\mu_E(k)\widetilde g(k)\kappa(k)
   \alpha(k)^{2\ell}\varphi(k)(Nk)^{1/2-s}
   Q_{k,\kappa}(1-s;-\ell)\\
&\quad\times\mu_E(m)\varphi(m)(Nm)^{1/2-2s}
 \prod_{\mathfrak p\mid m}
       \{q^{3s-3/2}-\alpha(\mathfrak p)^{3\ell}\}
 f(NkNm/B).
\end{split}
\tag{6}
\]

It is multiplied by the source's common gamma factor and fixed
ramified scalar functions and integrated against `A^s W_hat(s)`.
Both `k,m` are squarefree and retain every source coprimality. The
full divisor is exactly `m=1`; it has not been discarded.

Introduce a smooth split at `Nm=M0>=1`, with bounded overlap. This split
is imposed on the exact reflected expression and does not change the
original coefficient class. Its smooth derivatives on each dyad are
uniform in `M0`. Treat short and long complements separately.

## 3. Short complements, including the full divisor

For the part `Nm <= 2M0`, shift the component integral farther left to
`Re s=-J`, with any fixed `J>0`. This shift has no poles:

- The gamma numerator has its poles to the right, at
  `s=5/6+|ell|/2+n` and `7/6+|ell|/2+n`.
- `Q_{k,kappa}(1-s;-ell)` is entire and, on this new line, has an
  absolutely convergent coefficient series bounded uniformly in `k`.
- Scalar extraction from the original cusps uses only the exceptional
  minor and the trivial-channel projection. It has no geometric
  denominator. The 27-to-four expansion is used only at `1-s`, whose
  real part is at least `1/2+delta` throughout the shift and greater
  than one on the final line. Its ramified geometric factors are
  therefore bounded throughout this leftward shift.

The last point is precisely the left-line observation in Section 2 of
`type_i/ANGULAR_UNIFORMITY.md`; no divergent expansion at the original
left argument is being used.

On `Re s=-J`, the complementary prime product in (6) is bounded by
`prod_(p|m)(1+q^(-3J-3/2))`, uniformly in `m`. Since `Nk Nm` is
comparable to `B`, the remaining moving norm factor is bounded by

\[
 (Nk)^{1/2+J}(Nm)^{1/2+2J}
       \ll B^{1/2+J}(Nm)^J.
\tag{7}
\]

The number of pairs with `Nk Nm ~ B` is `O(B^(1+epsilon))`.
The fixed gamma quotient has polynomial vertical growth on the line;
the required number of seminorms of `W` may depend on `J`. Thus

\[
 |\mathcal T_{\rm short}|
       \ll (AB)^\epsilon B^{3/2}(BM0/A)^J.
\tag{8}
\]

This is the missing length information in a bound that takes absolute
values of `Q_k(1-s)` on the original reflected line. At the full divisor,
the effective length ratio is `B/A`, not the raw `B^2/A` ratio.

## 4. Long complements, with their signs retained

For `Nm~M >= M0`, keep the line `s=1/2-delta+it`. The inherited signed
complement theorem, applied before triangle in `m`, gives

\[
 \left|\sum_m (\text{the signed }m\text{ factor in (6)})\right|
 \ll (Nk)^\epsilon(1+|t|)^C M^{\tau_\beta(\delta)+\epsilon},
\tag{9}
\]

where

\[
\tau_\beta(\delta)=\max\{
 \beta/2-1/2+2\delta,\;
 \beta-1/2-\delta,\;\delta/2\}.
\tag{10}
\]

The profile `f(Nk Nm/B)` has uniformly bounded normalized `m`
derivatives when `Nk~K`, `Nm~M`, `KM~B`. The smooth split has the
same property. The finite ray factor is exactly an allowed `varphi`,
and the missing primes at `k` cost only its prescribed small power.

The natural-count cubic mean at `1-s=1/2+delta-it`, followed by Cauchy,
gives

\[
 \sum_{Nk\asymp K}^*|Q_{k,\kappa}(1/2+\delta-it)|
                    \ll K^{1+\epsilon}(1+|t|)^C.
\tag{11}
\]

Use (9)–(11), the factor `(Nk)^delta` in (6), and rapid Mellin decay:

\[
 |\text{one long dyad}|
   \ll (AB)^\epsilon A^{1/2-\delta}
           K^{1+\delta}M^{\tau_\beta(\delta)}.
\tag{12}
\]

Since `K M~B` and `tau_beta(delta)<1+delta`, summing all long dyads gives

\[
 |\mathcal T_{\rm long}|
 \ll (AB)^\epsilon A^{1/2-\delta}B^{1+\delta}
                 M0^{-(1+\delta-\tau_\beta(\delta))}.
\tag{13}
\]

## 5. Choose the split and optimize the complete bound

Put `R=A/B >= 1`. For any fixed small `eta>0`, take
`M0=R^(1-eta)`. If this exceeds the possible complementary range,
the long part is empty and (8) only improves. Equations (8) and (13)
become

\[
 |\mathcal T_{\rm short}|
       \ll (AB)^\epsilon B^{3/2}R^{-\eta J},
\tag{14}
\]

\[
 |\mathcal T_{\rm long}|
 \ll (AB)^\epsilon B^{3/2}
 R^{-\rho_\beta(\delta)
       +\eta(1+\delta-\tau_\beta(\delta))},
\tag{15}
\]

with

\[
\begin{split}
\rho_\beta(\delta)
 &=1/2+2\delta-\tau_\beta(\delta)\\
 &=\min\{1-\beta/2,\;1-\beta+3\delta,\;1/2+3\delta/2\}.
\end{split}
\tag{16}
\]

Choose

\[
 \delta=\max\{\beta/6,(1-\beta)/3\}.
\tag{17}
\]

For `1/2<=beta<=1`, this lies in `[1/9,1/6]`, so all used cubic mean
lines lie strictly within the licensed strip. The three terms in (16)
show exactly that `rho_beta(delta)=1-beta/2`. Choose `eta` sufficiently
small in terms of the final epsilon; then choose a fixed `J` sufficiently
large that `eta J >= 1-beta/2`. Allocate all earlier small-power losses
inside the final epsilon. This proves (4). For bounded `A/B`, the same
argument or the elementary right-line mean gives the stated bound with
a changed constant.

This is a continuous parameter argument, not an extrapolation from a
finite grid. At `beta=1`, `delta=1/6`, `tau=1/3`, and `rho=1/2` exactly.

## 6. What has and has not been closed

The old proper-complement estimate retained an unsaved `m=1` term in
the Mellin expression. Here the *complete smoothed rectangle* supplies
an additional ratio `A/B`: it makes all short complements, including
`m=1`, small after their legal left shift. Thus (4) is a bound for the
whole expression (2), not for a proper portion of its reflected expansion.

Two interfaces still prevent a zero-free conclusion:

1. **Cube removal.** The original uncompleted Gauss block uses
   `Q_r(s)/L_E^(3r)(3s-1/2,alpha^(3ell))`. Its reciprocal can have poles
   at unknown zeros and prevents the short-complement contour from moving
   to `Re s=-J`. It is not valid to carry (8) across this division.
   `JOINT_EULER_FACTOR.md` reassembles the cube inverse and complement
   exactly, instead of silently making that substitution.
2. **The actual quadratic terminal.** A nonmatching quadratic conductor
   of norm `H` multiplies the moving reflection factor by `H^(1-2s)`.
   The full-divisor effective dual ratio becomes `B H^2/A`. At the
   binding terminal `A=H B`, it is `H`, so no short-complement left-shift
   saving follows. The pure cubic theorem is not a bound for that term.

### Comparison with the supplied estimates

This note does not claim to improve the pure cubic second moment itself.
The right-line moment and Cauchy give the completed rectangle the bound
`A^(1/2+epsilon) B`. The reflected mean on a fixed line `p<1/2`
gives `A^p B^(3/2-p)`, within its licensed range. Both are at least
`B^(3/2)` for `A>=B`. Direct absolute reflection on a line just left
of zero gives `B^(3/2+epsilon)` in the intermediate range
`B<=A<=B^2`, and arbitrary decay when `A` is polynomially larger
than `B^2`. The bound (4) is a strict improvement over those particular
supplied resources when `B<A<=B^2` with a power separation. At `A=B`
it agrees with their scale, and beyond `B^2` the already available rapid
tail may be preferable. These are comparisons of supplied bounds, not
lower bounds for the actual sum or a literature-wide novelty claim.

The additional input is precisely the retained signed complementary
Euler product. This gain cannot be obtained by applying the positive
pure cubic mean to the whole reflected divisor sum and then taking
triangle in every complement.

No new zero-free boundary or RH proof is claimed. The completed estimate
is a source-dependent analytical component available for a future
consumer that preserves its exact completion and coefficient class.
