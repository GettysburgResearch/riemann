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

The all-degree lower-bound conjecture is now equivalent to finding, for
every `d`, a correction `R_d` such that

\[
 \begin{aligned}
 [s_{H_k}]R_d&=0 &&(0\le k<d),\\
 \pi_0(R_d)&=L_d-\pi_0(\mathcal F_d),\\
 \left|b_{d,\lambda}+[s_\lambda]R_d\right|&\le f^\lambda
 &&(\lambda\vdash d).
 \end{aligned}
\tag{3.4}
\]

The hook-zero requirement is forced because (0.4) already saturates every
hook capacity.  Conversely, (3.4) makes `F_d+R_d` an admissible dual with
objective `2^(d-1)/d`, matching the exact-cycle primal candidate.  Strict
inequality on every nonhook is a sufficient complementary-slackness
certificate for uniqueness.

Thus the missing all-degree theorem is no longer “guess the interior Young
lattice potentials.”  It is the precise **contractive primitive-lift
problem** (3.4): remove all higher odd powers of `tanh(A)` using nonhook
Schur directions without leaving the dimension box.

## 4. What the bounded replay checks

For every `2<=d<=10`, independently of the frozen LP certificates, the
replay:

1. enumerates every standard tableau through its row word;
2. recomputes `b_(d,lambda)` and the hook-length dimensions;
3. checks the spectral capacity and exact hook saturation;
4. recomputes the complete character table by Murnaghan--Nakayama;
5. checks (0.5) on every conjugacy class in exact integer/rational
   arithmetic;
6. lists every forbidden derangement residual.

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
- the equivalence between an optimal dual completion and (3.4);
- the bounded replay statements through degree ten.

Not proved here:

- existence of the correction (3.4) for all `d`;
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
