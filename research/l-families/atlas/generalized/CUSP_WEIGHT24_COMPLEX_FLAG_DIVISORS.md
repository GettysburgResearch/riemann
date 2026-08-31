# Which weight-24 flags suppress poles?

Status: proposed theorem; independent exact-source review required.
Scope: every fixed complex line in the actual two-dimensional space
`S_24(SL_2(Z))`; genuine divisors in `Re s>1`. No weight limit, numerical
divisor census, simplicity, effective Booker--Thorne width, or RH assertion.
Authoring base: `ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf` (FI).

Arithmetic class: **MIXED: EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE**;
rounding: **none**. Gaussian rationals and the exact real quadratic field
`Q(sqrt(144169))` are represented by rational pairs. The finite controls do
not machine-certify the analytic theorem, prime twists, contours, or onset.

## 1. Native object, including complex conjugations

Retain FI1-FI7 verbatim: the full-domain completed Eisenstein period `I_s`,
the real, first-q-coefficient-one Hecke eigenforms

\[
 f_\pm=g+(540\pm12\sqrt{144169})b,\qquad
 g=\Delta E_4^3-696\Delta^2,\quad b=\Delta^2,
\]

and the actual four finite-part Euler products

\[
 Z=\zeta(s),\quad S_\pm=L(s,\operatorname{sym}^2 f_\pm),
 \quad C=L(s,f_+\times f_-),\quad X=ZS_+,\quad Y=ZS_-.
\]

Unlike FI7's completed-entry notation, `X,Y` in this note have their common
gamma factor removed. With
`A=pi^(-s)Gamma(s)(4pi)^(-s-23)Gamma(s+23)`, the actual period matrix is

\[
 I_s|_{(f_+,f_-)}=A\begin{pmatrix}X&C\\C&Y\end{pmatrix},
 \qquad N=XY-C^2.                                      \tag{FC1}
\]

Choose a nonzero pair `(a,b_0)` and the line
`W=C(a f_+ + b_0 f_-)`. The subscript avoids confusing this coefficient with
the modular form `b=Delta^2`. Normalize `|a|^2+|b_0|^2=1` and set

\[
 p=|a|^2,\quad q=|b_0|^2,\quad d=2\Re(\overline a b_0),
 \qquad p+q=1,\quad d^2\le4pq.                         \tag{FC2}
\]

The letter `q` in FC2 is a nonnegative scalar, not the Fourier variable.
The first period argument is conjugate-linear. The cross entries agree as
meromorphic functions because the source eigenforms have real q coefficients.
Therefore

\[
 I_s(w,w)/A=D_W:=pX+qY+dC.                              \tag{FC3}
\]

In particular the cross coefficient is not `2ab_0`, `2|ab_0|`, or a
holomorphic function of the flag coordinate. Imaginary mixtures can have
`d=0` while both `p,q` are positive.

For a convenient exact scalar normalization take
`v=-conjugate(b_0) f_+ + conjugate(a) f_-` and define

\[
 Q_W(s)=\frac{\det I_s|_{(v,w)}}{I_s(w,w)}
       =A(s)\frac{N(s)}{D_W(s)}.                        \tag{FC4}
\]

The coefficient-basis matrix `(v,w)` has determinant `-1`. Changing its
representatives by unit phases does not change FC4. The Euclidean norm here
is only a declared coordinate normalization, not the Petersson norm. Any
other nonzero quotient coordinate associated with the same fixed line changes
FC4 by a positive nonzero constant, so its divisor is unchanged. For an
unnormalized pair FC4 is `A(|a|^2+|b_0|^2)N/(|a|^2X+|b_0|^2Y+dC)`.
For the canonical first-coefficient line `W=C(f_+-f_-)`, this normalization
gives `Q_W=2 Q_1`; its divisor is exactly the original FI divisor.

## 2. Classification and compact-set quantifiers

**Theorem FC.** Exactly the two Hecke eigenlines `C f_+` and `C f_-` have
no poles anywhere on `Re s>1`.

Every other fixed complex line has a number `eta_W>0` such that, for every
fixed `1<sigma_1<sigma_2<=1+eta_W`, its quotient has at least `c_W T`
distinct genuine poles in
`sigma_1<=Re s<=sigma_2, 0<Im s<=T` for all sufficiently large `T`.
Here `c_W>0` and the onset can depend on the line and strip.

Every line, including both eigenlines, has the analogous linear lower bound
for distinct genuine zeros. For zeros the near-one width can be chosen
independently of the line. More precisely:

- For any compact set of mixed lines, a common positive pole width exists.
  At each fixed substrip within it, the positive count constant and onset
  can also be chosen uniformly on that compact set.
- For zeros, the corresponding uniform statement holds on all of `CP^1`.
- There is **no** common positive pole width valid for every mixed line
  approaching an eigenline. Section 5 proves this failure, not merely the
  absence of a uniform estimate in the construction.

These assertions concern the actual completed quotient FC4, not a freely
chosen matrix pencil, a new Euler product, or an eigenbasis diagonalization
of `I_s`. The nonzero cross period `AC` is retained throughout.

## 3. Explicit noncancelling targets for all complex lines

FI section 3 verifies the four pairwise nonisomorphic unitary cuspidal
automorphic inputs of degrees `1,3,3,4`, including non-dihedral and non-twist
conditions and finite-place Ramanujan. Its cited Gelbart--Jacquet and
Ramakrishnan lift theorems, and the correction-aware Booker--Thorne Proposition
3.1, are analytic imports here with the same normalization. In particular,
for any `R>1`, all tuples in the closed coordinate annulus `[R^-1,R]` are
attainable at every sufficiently near-one real sigma using **one common
phase at each prime**. Choose the prime cutoff `3/2`, so every prime occurs.
No independence of the actual four untwisted functions is postulated.

For `p,q>0`, take the explicit target

\[
 (Z,S_+,S_-,C)=
 \left(1,1,-\frac pq-i\frac d{q^2},\frac i q\right).
                                                               \tag{FC5}
\]

Direct substitution, including the `d=0` case, gives

\[
 D_W=0,\qquad N=\frac{1-pq-id}{q^2},\qquad
 \Re N\ge\frac{3}{4q^2}>0.                              \tag{FC6}
\]

All four target coordinates are nonzero. If `p,q>=epsilon>0`, with
`epsilon<=1/2`, they lie in the annulus with `R=2/epsilon^2`:
`|S_-|>=p/q>=epsilon`, `|S_-|<=p/q+|d|/q^2<=1/epsilon+1/epsilon^2`,
and `|C|=1/q<=1/epsilon`. The upper bound is at most `R`; the lower bound
is at least `R^-1`. This gives a common eta on every compact mixed-flag set.

For zeros, choose `e=1` if `d>=0`, and `e=-1` if `d<0`, and use

\[
 (Z,S_+,S_-,C)=(1,1,1,e),\qquad
 N=0,\quad D_W=1+|d|\ge1.                              \tag{FC7}
\]

Both choices belong to the fixed annulus `R=2`; they work even for eigenlines.
The pointwise targets alone are not a divisor proof. The following steps pay
nonconstancy, the entire tails, common contour approximation, and counting.

Every `D_W` has an absolutely convergent ordinary Dirichlet series. Its
coefficient at index one is `1+d=|a+b_0|^2`. If this vanishes, necessarily
`p=q=1/2,d=-1`; its coefficient at index two is then
`83041344/(2*2^23)>0`. This also follows directly from the literal formula

\[
 D_W(s)=\zeta(2s)\sum_{n\ge1}
     |a a_{f_+}(n)+b_0 a_{f_-}(n)|^2 n^{-s-23}.         \tag{FC8}
\]

The common phase twist multiplies its first nonzero coefficient by the
nonzero phase `chi(n)`, so `D_{W,chi}` is not identically zero. The analogous
fact for `N_chi` follows from FI11: its coefficient at index two is
`1297521/131072`, while its constant coefficient is zero. The absolute
coefficient bounds, uniform in all normalized lines and common prime twists,
are

\[
 |[n^{-s}]D_W|\le(p+q+|d|)d_4(n)\le2d_4(n),\qquad
 |[n^{-s}]N|\le2d_8(n).                                \tag{FC9}
\]

Here products use Dirichlet convolution, and `d_j` is the ordered divisor
function. FI13 supplies a complete tail majorant on every closed sub-half-plane
`Re s>=sigma_1>1`.

For FC5 choose a small closed disk about the target sigma, strictly inside
the desired substrip, on which `N_chi` has no zero and on whose boundary
`D_{W,chi}` has no zero. Pay both uniform tails in FC9, and approximate the
finitely many remaining prime phases simultaneously by one vertical shift.
Rouche then gives a denominator zero while the full-disk numerator margin
keeps it uncancelled. Since `A` has no zeros or poles on `Re s>1`, it is a
genuine pole of FC4. For FC7 interchange numerator and denominator. No
approximation of the gamma factor is needed.

The finite prime logarithms are rationally independent. The resulting open
phase box has positive lower density of good positive shifts by torus
equidistribution. A divisor can lie in translated radius-rho disks for at
most `2 rho` measure of shifts. Restricting to `rho<t<T-rho` and dividing
the good-shift measure by `2 rho` proves the asserted **distinct-point**
linear lower counts, without assumptions on multiplicity or simplicity.

For the compact-set uniform claims, first fix the substrip. At each flag the
above construction has strict contour and full-disk margins. Those margins
persist for nearby flags because `D_W` depends continuously and linearly on
`p,q,d`, uniformly on that closed disk. The same phase box, tails, radius and
count bound therefore work on a flag neighborhood. A finite subcover of the
compact set permits taking the minimum positive count constant and the maximum
onset. For zeros take the compact set to be all `CP^1`, using the common
annulus `R=2`. No continuity of the Booker--Thorne selected phases is needed.

Finally, for an eigenline `D_W=X` or `Y`. Both are products of absolutely
convergent, nonvanishing Euler products on `Re s>1`; `A,N` are holomorphic
there. This proves pole-freeness for exactly the two stated lines and completes
the classification.

## 4. Euler bounds: a cancellation improves the proposed exponent

For `a!=0`, let `r=b_0/a`. Dividing the denominator by its nonzero `pX` gives

\[
 D_W/(pX)=1+|r|^2\frac YX+2\Re(r)\frac CX.              \tag{FC10}
\]

Let `sigma=Re s>1` and `x=p_0^{-s}` at a prime `p_0`, with `t=|x|`.
For every unit-modulus parameter `omega`,
`1-t<=|1-omega x|<=1+t`. The symmetric-square factors are
`(1-x)^-1(1-u^2 x)^-1(1-u^-2 x)^-1`. Their common `(1-x)^-1`
factor cancels exactly in `Y/X=S_-/S_+`. Consequently

\[
 \left|\frac YX\right|\le
 \prod_{p_0}\left(\frac{1+p_0^{-\sigma}}{1-p_0^{-\sigma}}\right)^2
 =:M_4(\sigma)=\frac{\zeta(\sigma)^4}{\zeta(2\sigma)^2}. \tag{FC11}
\]

Treating all three factors separately would give the valid but weaker
`M_6=zeta(sigma)^6/zeta(2sigma)^3`. It is not the best bound from this
elementary source factorization. For `C/X` there are four denominator and
four numerator factors, giving the sufficient bound

\[
 \left|\frac CX\right|\le
 \prod_{p_0}\left(\frac{1+p_0^{-\sigma}}{1-p_0^{-\sigma}}\right)^4
 =:M_8(\sigma)=\frac{\zeta(\sigma)^8}{\zeta(2\sigma)^4}.
                                                               \tag{FC12}
\]

All products converge absolutely; no finite-prime truncation is substituted.
Each displayed positive factor decreases with sigma. Thus, for any
`sigma_0>1`, the strict condition

\[
 |r|^2M_4(\sigma_0)+2|\Re r|M_8(\sigma_0)<1             \tag{FC13}
\]

excludes denominator zeros, and hence all quotient poles, on the **entire
closed half-plane** `Re s>=sigma_0`, uniformly in height. The same statement
holds near the other eigenline after exchanging `+,-` and using `a/b_0`.
Replacing `M_4` by `M_6` remains sufficient but loses the exact common factor.

## 5. Explicit sufficient escape scales, not sharp pole locations

For `0<delta<=1`, the elementary integral bound gives
`zeta(1+delta)<=1+1/delta<=2/delta`, while `zeta(2+2delta)>=1`.
Hence `M_4(1+delta)<=16 delta^-4` and
`M_8(1+delta)<=256 delta^-8`. For `r!=0` put

\[
 \delta_r=4\max\{|r|^{1/2},|\Re r|^{1/8}\}.            \tag{FC14}
\]

Whenever `delta_r<=1`, FC13's left side is at most
`1/16+1/128=9/128<1`. Therefore every pole with `Re s>1` lies in
`1<Re s<1+delta_r`. These are sufficient upper widths, not asymptotic
locations or optimal exponents. A nonzero purely imaginary `r` removes the
cross term exactly and yields the stronger sufficient width `4|r|^(1/2)`.
The classification nevertheless gives infinitely many genuine poles for
each such fixed imaginary mixture; a zero real cross coefficient does not
make its denominator an Euler product.

For any fixed `sigma_0>1`, FC13 holds once `r` is sufficiently small.
Thus all right-half-plane poles escape toward its boundary `Re s=1` as
the line approaches either Hecke eigenline, in this uniform-in-height sense.
If a fixed positive eta worked for every mixed line, choose one substrip
strictly between `1` and `1+eta`. For a sufficiently near-eigenline mixed
flag, FC13 excludes all poles in that substrip, contradicting its purported
positive count. The global uniform-width assertion is therefore false.

## 6. Replay boundary and sources

The producer replays FI's frozen primitive q-series computation before using
its exact coefficients. It covers a declared complete rational flag grid plus
held-out imaginary, near-eigenline and nonreal controls; it checks every native
denominator coefficient through index 64 against the literal squared-amplitude
formula FC8. Gaussian-rational target checks verify FC5-FC7, annulus membership,
and numerator/denominator noncancellation. Exact polynomial and rational controls
verify the shared Euler-factor cancellation and the `9/128` escape ledger.
None of these finite calculations proves the all-parameter analytic quantifiers.

The literal FI proof, producer, fixture, manifest and tests at the authoring
base, and its independent review at `0f29fd2d687c57402a14723dde2bc2b7e74fa317`,
are bound by raw Git blob identities and LF-normalized SHA256. The new manifest
and four non-fixture artifacts are authenticated, and the entire fixture is
reconstructed. Strict types, bit/work/byte/depth/node caps and rejection tests
remain active under optimized Python. There are no floating Euler-product or
zero evaluations. The sample flag grid is not called exhaustive in `CP^1`.

Primary analytic inputs are classical: [Booker--Thorne Proposition 3.1](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf)
and its [correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf),
with the actual lift hypotheses verified in FI using
[Gelbart--Jacquet](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf)
and [Ramakrishnan](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf).
The present contribution is the all-complex-flag classification and explicit
source-factor escape bound for this actual period family, not a new general
value theorem, an automorphic representation, or a literature-priority claim.
The smallest load-bearing imported premise is the correction-aware common-prime
joint-value theorem for the four already verified inputs.
