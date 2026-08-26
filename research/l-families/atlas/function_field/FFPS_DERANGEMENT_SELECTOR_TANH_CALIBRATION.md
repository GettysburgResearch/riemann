# A hyperbolic-tangent calibration for the derangement selector

Status: **exact all-degree characteristic-zero symmetric-function theorem;
bounded exact replay through degree ten; the contractive correction, the
all-degree selector optimum, a native FFPS adapter, RH, and GRH remain open**

Bounded replay:
[`ffps_derangement_selector_tanh_calibration.py`](ffps_derangement_selector_tanh_calibration.py).
Canonical summary:
[`ffps_derangement_selector_tanh_calibration.json`](ffps_derangement_selector_tanh_calibration.json).

Frozen source boundary: the exact finite optimization packet at
`6d9e66033c1a00066935cceed9ca66b76b67fd99`, including all four source blobs
pinned by the replay.  That
packet proves the relaxed selector optimum and uniqueness only for
`2<=d<=10`.  Nothing below silently upgrades its finite linear programmes to
an all-degree theorem.

## 0. Outcome

For a partition `lambda|-d`, let

\[
 b_{d,\lambda}
 =\sum_{T\in\operatorname{SYT}(\lambda)}(-1)^{\operatorname{des}(T)},
 \qquad
 \mathcal F_d=\sum_{\lambda\vdash d}b_{d,\lambda}s_\lambda.
\tag{0.1}
\]

Here `des(T)` is the number of ordinary descents of the standard Young
tableau `T`.  Put

\[
 \mathcal A(t)
 =\sum_{r\ge1}{2^{r-1}\over r}p_r t^r.
\tag{0.2}
\]

The exact all-degree identity is

\[
 \boxed{
 \sum_{d\ge1}\mathcal F_d t^d
 =\tanh \mathcal A(t).}
\tag{0.3}
\]

It has two immediate selector consequences.

First, if `H_k=(d-k,1^k)`, then every standard tableau of hook shape has
exactly `k` descents, so

\[
 \boxed{
 b_{d,H_k}=(-1)^k f^{H_k}
 =(-1)^k{d-1\choose k}.}
\tag{0.4}
\]

Thus the normalized spectral coefficients
`b_(d,lambda)/f^lambda` lie in `[-1,1]` and saturate the exact signs required
on every hook by complementary slackness.

Second, for every cycle type `mu|-d`, with `ell=ell(mu)`,

\[
 \boxed{
 \sum_{\lambda\vdash d}b_{d,\lambda}\chi_\lambda(\mu)
 =[x^\ell]\tanh x\;\ell!\,2^{d-\ell}.}
\tag{0.5}
\]

The transform depends only on the number of cycles, not on their lengths.
It is zero for even `ell`; its first odd values are

\[
 2^{d-1},\qquad -2^{d-2},\qquad 2^{d-1},\qquad
 -17\,2^{d-3}
\tag{0.6}
\]

for `ell=1,3,5,7`, respectively.

In particular the full-cycle class coefficient is exactly

\[
 [p_d]\mathcal F_d={2^{d-1}\over d},
\tag{0.7}
\]

the conjectured optimum.  But from degree six onward the same bounded
spectral certificate also has forbidden support on derangement classes with
three, five, and then higher odd numbers of cycles.  Formula (0.3) therefore
does **not** prove the all-degree optimization conjecture.  It identifies the
entire residual exactly.

## 1. Proof of the `tanh` identity

For a composition `alpha` of `d`, write `r_alpha` for its ribbon Schur
function.  The standard descent-set expansion gives

\[
 \mathcal F_d
 =\sum_{\alpha\vDash d}(-1)^{\ell(\alpha)-1}r_\alpha.
\tag{1.1}
\]

The ribbon-to-complete expansion is

\[
 r_\alpha
 =\sum_{\beta\succeq\alpha}
 (-1)^{\ell(\alpha)-\ell(\beta)}h_\beta,
\tag{1.2}
\]

where `beta` runs over the coarsenings of `alpha`.  Fix a composition `beta`
of length `m`.  Its parts admit

\[
 \prod_i2^{\beta_i-1}=2^{d-m}
\tag{1.3}
\]

refinements.  The two signs in (1.1)--(1.2) multiply to
`(-1)^(m+1)`, independently of the refinement.  Hence

\[
 \mathcal F_d
 =\sum_{\beta\vDash d}
 (-1)^{\ell(\beta)+1}2^{d-\ell(\beta)}h_\beta.
\tag{1.4}
\]

Set

\[
 U(t)=\sum_{r\ge1}2^{r-1}h_r t^r.
\tag{1.5}
\]

Summing (1.4) over `d` gives

\[
 \sum_{d\ge1}\mathcal F_d t^d
 =\sum_{m\ge1}(-1)^{m+1}U(t)^m
 ={U(t)\over1+U(t)}.
\tag{1.6}
\]

The complete-function generating series gives

\[
 1+2U(t)
 =\sum_{r\ge0}2^rh_rt^r
 =\exp\!\left(\sum_{r\ge1}{2^rp_rt^r\over r}\right)
 =e^{2\mathcal A(t)}.
\tag{1.7}
\]

Substitution in (1.6) proves (0.3).

## 2. Proof of the cycle-count transform

Write

\[
 \tanh x=\sum_{\ell\ge1}\tau_\ell x^\ell.
\tag{2.1}
\]

For `mu=(1^(m_1)2^(m_2)...)` of length `ell`, the coefficient of `p_mu t^d`
in `A(t)^ell` is

\[
 {\ell!\over\prod_rm_r!}
 \prod_r\left({2^{r-1}\over r}\right)^{m_r}.
\tag{2.2}
\]

Since

\[
 z_\mu=\prod_rr^{m_r}m_r!,
\tag{2.3}
\]

multiplication by `z_mu` reduces (2.2) to
`ell!*2^(d-ell)`.  Finally,

\[
 s_\lambda=\sum_{\mu\vdash d}{\chi_\lambda(\mu)\over z_\mu}p_\mu,
\tag{2.4}
\]

so `z_mu[p_mu]F_d` is the left side of (0.5).  This proves the formula.

## 3. Exact relationship to the relaxed selector dual

For a degree-`d` symmetric function

\[
 Y_d=\sum_{\lambda\vdash d}c_\lambda s_\lambda
 =\sum_{\mu\vdash d}y_\mu p_\mu,
\tag{3.1}
\]

the finite optimization dual requires

\[
 |c_\lambda|\le f^\lambda,
\qquad
 y_\mu=0
 \quad\text{if }1\notin\mu\text{ and }\mu\ne(d),
\tag{3.2}
\]

and maximizes `y_(d)`.  The function `F_d` satisfies the first condition and
has the desired value `y_(d)=2^(d-1)/d`.  Its only failure is the completely
explicit higher odd-power tail of `tanh(A)`.

Let `pi_0` be the endomorphism setting `p_1=0`; this is the usual
`(1-E)`/derangement projection.  Define the linear target

\[
 L_d=[t^d]\mathcal A(t)={2^{d-1}\over d}p_d.
\tag{3.3}
\]

### 3.1 The zero-hook lift exists algebraically in every degree

Let

\[
 V_d^{\rm nh}
 =\operatorname{span}\{s_\lambda:\lambda\vdash d,\ \lambda
 \text{ is not a hook}\}.
\tag{3.4}
\]

There is an exact all-degree image theorem:

\[
 \boxed{
 \pi_0(V_d^{\rm nh})
 =\left\{
 P\in\operatorname{span}\{p_\mu:1\notin\mu\}:
 [p_d]P=0
 \right\}.}
\tag{3.5}
\]

For `d=1`, both sides of (3.5) are zero: there are no nonhook partitions,
and there is no `p_1`-free degree-one power sum.  Thus the identity is
trivial in that endpoint degree.  The annihilator argument below is for
`d>=2`.

To prove it, take the Hall-inner-product annihilator of the left side inside
the `p_1`-free subspace.  Since `pi_0` is an orthogonal projection in the
power-sum basis, an annihilator element is both `p_1`-free and hook-supported
in the Schur basis.  Being `p_1`-free says that its associated class
function vanishes on every fixed-point class, equivalently its restriction
to `S_(d-1)` is zero.

Write its hook coefficients as `a_k` on `H_k`.  At the hook predecessor
`(d-1-k,1^k)`, Young branching gives

\[
 a_k+a_{k+1}=0.
\tag{3.6}
\]

No nonhook predecessor lies below a hook, so there are no further
conditions.  The annihilator is therefore one-dimensional, spanned by

\[
 \sum_{k=0}^{d-1}(-1)^ks_{H_k}=p_d.
\tag{3.7}
\]

Taking the annihilator once more proves (3.5), because the Hall-orthogonal
complement of `p_d` in the `p_1`-free power-sum space is exactly the
`p_d`-coefficient-zero hyperplane.

Since `L_d-pi_0(F_d)` has zero `p_d` coefficient, (3.5) proves that a
zero-hook correction with the first two properties below exists for every
`d`.  There is no remaining algebraic or rank obstruction.

### 3.2 The remaining problem is coefficientwise contraction

The all-degree lower-bound conjecture is now equivalent to choosing such an
algebraic correction `R_d` inside the dimension box:

\[
 \begin{aligned}
 [s_{H_k}]R_d&=0 &&(0\le k<d),\\
 \pi_0(R_d)&=L_d-\pi_0(\mathcal F_d),\\
 \left|b_{d,\lambda}+[s_\lambda]R_d\right|&\le f^\lambda
 &&(\lambda\vdash d).
 \end{aligned}
\tag{3.8}
\]

The hook-zero requirement is forced because (0.4) already saturates every
hook capacity.  Conversely, (3.8) makes `F_d+R_d` an admissible dual with
objective `2^(d-1)/d`, matching the exact-cycle primal candidate.  Strict
inequality on every nonhook is a sufficient complementary-slackness
certificate for uniqueness.

Thus the missing all-degree theorem is no longer “guess the interior Young
lattice potentials,” nor is it existence of an unrestricted lift.  It is
the precise **contractive primitive-lift problem** (3.8): remove all higher
odd powers of `tanh(A)` using nonhook Schur directions without leaving the
dimension box.

### 3.3 A global even-cycle escape firewall

The same calibration completely closes one infinite subspace of possible
escapes.  Let `Q_0=1_(d)` be the exact cycle indicator, and let `U` be a real
or complex class function supported on noncycle derangement types having an
even number of cycles.  Then

\[
 \boxed{
 \|Q_0+U\|_{\rm rank,1}\ge {2^{d-1}\over d},
 \quad\text{with equality iff }U=0.}
\tag{3.9}
\]

To see this, write `u_lambda` for the character coefficients of `U`.  By
(0.5),

\[
 \sum_{\lambda\vdash d}b_{d,\lambda}u_\lambda=0,
\tag{3.10}
\]

because every physical class in the support of `U` has even length.  The
coefficients of `Q_0` are `(-1)^k/d` on the hooks and zero elsewhere.  Hence
the spectral capacity and hook saturation give

\[
 \begin{aligned}
 \|Q_0+U\|_{\rm rank,1}
 &\ge
 \operatorname{Re}\sum_\lambda
 b_{d,\lambda}(a^0_\lambda+u_\lambda)\\
 &=\sum_{k=0}^{d-1}{f^{H_k}\over d}
 ={2^{d-1}\over d}.
 \end{aligned}
\tag{3.11}
\]

The inequality is strict for nonzero `U`.  Indeed, every nonhook shape has
`lambda_2>=2`.  Start with its row-superstandard tableau and interchange the
entries `lambda_1` and `lambda_1+1`.  The result is still standard.  The
swap loses the descent at `lambda_1`, gains descents at `lambda_1-1` and
`lambda_1+1`, and leaves all other descents unchanged.  Thus both descent
parities occur, proving

\[
 |b_{d,\lambda}|<f^\lambda
 \qquad(\lambda\text{ nonhook}).
\tag{3.12}
\]

If all nonhook coefficients of `U` vanished, the annihilator argument of
Section 3.1 would force `U` to be a multiple of the exact cycle direction;
its zero value on `(d)` then forces `U=0`.  Every nonzero `U` therefore has a
nonhook coefficient, where (3.12) makes (3.11) strict.

Consequently an all-degree counterexample or cheaper relaxed selector, if
one exists, must engage at least one odd cycle-count stratum `ell>=3`.
Even-cycle freedom alone can never help, at any magnitude; this is global,
not only a first-order statement.

## 4. What the bounded replay checks

For every `2<=d<=10`, independently of the frozen LP certificates, the
replay:

1. enumerates every standard tableau through its row word;
2. recomputes `b_(d,lambda)` and the hook-length dimensions;
3. checks strict nonhook spectral capacity and exact hook saturation;
4. recomputes the complete character table by Murnaghan--Nakayama;
5. checks (0.5) on every conjugacy class in exact integer/rational
   arithmetic;
6. verifies that the nonhook-to-noncycle-derangement character matrix has
   full row rank, the finite shadow of (3.5);
7. lists every forbidden derangement residual.

The first forbidden residual is `(2,2,2)` at `d=6`, with class transform
`-16=-2^(6-2)`.  At `d=10`, the replay sees both the three-cycle-factor
layer and the first five-cycle-factor type `(2,2,2,2,2)`, exactly as (0.5)
predicts.  No LP solver or floating-point step occurs.

Because a non-cycle derangement has at least two cycles, and the even-cycle
layers vanish, `F_d` is already a valid strict dual for `2<=d<=5`.  This
gives a conceptual proof of the first four degrees, not an extrapolation to
larger `d`.

## 5. Scope and literature boundary

The descent-set ribbon expansion, the power-sum generating series, the
`p_1 -> 0` derangement transform, and Lie-idempotent language are classical.
The `(1-E)` context is described, for example, by Hivert, Luque, Novelli,
and Thibon, *The (1-E)-transform in combinatorial Hopf algebras*, J. Algebraic
Combin. 33 (2011), 277--312, arXiv:0912.0184.  No literature novelty is
claimed for (0.3) or its reformulation here.

Proved here:

- (0.3)--(0.7) for every degree and every cycle type;
- exact spectral capacity and hook saturation;
- the all-degree zero-hook image theorem (3.5);
- the equivalence between an optimal dual completion and (3.8);
- the global even-cycle escape firewall (3.9);
- the bounded replay statements through degree ten.

Not proved here:

- a choice of the algebraic correction (3.8) satisfying the dimension box
  for all `d`;
- strict nonhook slack or unique optimality beyond `d=10`;
- a native FFPS interpretation of the root-incidence boundary;
- an affordable joint source/selector cancellation;
- any trace estimate, individualization, RH, or GRH statement.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_derangement_selector_tanh_calibration.py --check
python -B -O research/l-families/atlas/function_field/ffps_derangement_selector_tanh_calibration.py --check
python -B -m unittest tests.test_ffps_derangement_selector_tanh_calibration
python -B -O -m unittest tests.test_ffps_derangement_selector_tanh_calibration
```

The replay performs no finite-field enumeration, curve or sheaf
construction, `L`-function computation, zero search, external optimization,
or floating-point calculation.
