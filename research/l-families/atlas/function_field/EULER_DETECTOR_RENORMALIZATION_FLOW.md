# A finite-dimensional renormalization flow for Euler detectors

## Status and scope

**Status:** exact compact-model theorems, exact formal cumulant algebra, and one
explicit obstruction packet.

**Scope:** independent Haar `SU(2)` local factors and finite cumulant jets.  The
arithmetic proposal in Section 8 is an experiment, not a result.

**Exact sources or dependencies:** native Clebsch--Gordan algebra, exact
rational probability laws, and the elementary divergence of
`sum_p 1/p`.  No curve table, finite field, zero table, random sample,
floating-point integration, or external database is consumed.

**What was actually run:**

```text
python research/l-families/atlas/function_field/euler_detector_renormalization_flow.py
python -m pytest -q tests/test_euler_detector_renormalization_flow.py
python -O -m pytest -q tests/test_euler_detector_renormalization_flow.py
```

The producer uses `Fraction` arithmetic, eight declared primes, character
weight at most 96, moment order at most 10, and at most 64 local factors.

**Smallest remaining gap:** compute one exact two-prime mixed-cumulant residual
for a complete, source-locked function-field family.  Without that global
family coupling, this packet says what the independent compact background is,
not what an arithmetic family does.

Nothing here proves a statement about an arithmetic L-function family, a
global Euler product, zeros, RH, or GRH.  No external novelty claim is made for
the compact-model probability theorem.

## 1. The local Euler source and its character coordinates

For a conjugacy class `U in SU(2)` and `|z|<1`, the local logarithm is

\[
 \log\det(1-zU)^{-1}
 =\sum_{r\geq 1}{z^r\over r}\operatorname{Tr}(U^r).
 \tag{1}
\]

Let `chi_j` denote the irreducible `SU(2)` character of highest weight `j`.
The exact identity

\[
 \operatorname{Tr}(U^r)=\chi_r(U)-\chi_{r-2}(U),
 \qquad \chi_{-1}=\chi_{-2}=0,
 \tag{2}
\]

puts every finite truncation of (1) in a declared representation-ring basis.
For example, at `z=1/2` and trace-power cutoff two,

\[
 D(U)={1\over2}\operatorname{Tr}U
      +{1\over8}\operatorname{Tr}(U^2)
 =-{1\over8}\chi_0+{1\over2}\chi_1+{1\over8}\chi_2.
 \tag{3}
\]

After exact Haar centering,

\[
 X=D-\mathbb E D={1\over2}\chi_1+{1\over8}\chi_2.
 \tag{4}
\]

The producer obtains, with no quadrature,

\[
 (\kappa_2,\kappa_3,\kappa_4,\kappa_5,\kappa_6)(X)
 =\left({17\over64},{49\over512},-{5\over128},
        -{961\over8192},-{5605\over131072}\right).
 \tag{5}
\]

Thus even this two-trace local Euler packet is skew: centering does not impose
the center symmetry enjoyed by `chi_1` alone.

## 2. Why a fixed finite character ring is not an exact flow

The Clebsch--Gordan rule is

\[
 \chi_a\chi_b
 =\sum_{j=0}^{\min(a,b)}\chi_{a+b-2j}.
 \tag{6}
\]

Let `V_R=span_Q{chi_0,...,chi_R}`.

**Proposition 2.1 (finite-character closure obstruction).**  No `V_R` with
`R>=1` is closed under pointwise multiplication.

**Proof.**  Formula (6) shows that `chi_R^2` contains `chi_(2R)` with
coefficient one, and `chi_(2R)` is not in `V_R`.  QED.

This is not a cosmetic defect.  At `R=1`,

\[
 \chi_1^2=\chi_0+\chi_2.
 \tag{7}
\]

If the `chi_2` term is projected away after every multiplication, the computed
fourth moment is one.  Exact multiplication before Haar projection gives

\[
 \int_{SU(2)}\chi_1^4=2.
 \tag{8}
\]

Consequently a finite representation basis is usable only with one of two
contracts:

1. expand far enough to cover every requested product exactly (weight at most
   `mR` for an `m`-th moment); or
2. record the discarded character component as a projection defect.

The script implements both.  It never treats a projected character product as
an exact local law.

## 3. Cumulant jets give genuine finite-dimensional closure

For a random variable with the required moments, write the formal cumulant
series

\[
 K_X(t)=\log\mathbb E e^{tX}
       =\sum_{j\geq1}\kappa_j(X){t^j\over j!}.
 \tag{9}
\]

Let `J_m K_X` be its image in `Q[[t]]/(t^(m+1))`.

**Theorem 3.1 (exact jet aggregation).**  If `X_1,...,X_N` are independent,
then

\[
 J_mK_{X_1+\cdots+X_N}
 =\sum_{i=1}^N J_mK_{X_i}.
 \tag{10}
\]

Thus `(kappa_1,...,kappa_m)` is an exact finite-dimensional aggregation state.
There is no closure error through order `m`.  If the next cumulant exists, the
first omitted formal coefficient is

\[
 {1\over(m+1)!}\sum_i\kappa_{m+1}(X_i).
 \tag{11}
\]

**Proof.**  Independence multiplies moment-generating series; formal logarithms
turn the product into a sum.  Reduction modulo `t^(m+1)` proves (10), and the
next coefficient gives (11).  QED.

Equation (10) is exact as a formal jet.  It is not an analytic error bound for
the omitted tail and does not reconstruct the probability law.  Section 7
shows that this limitation is load-bearing.

For local increments with variance `v_p` and cumulants `k_(j,p)`, define

\[
 V_n=\sum_{p\leq p_n}v_p,
 \qquad c_{j,n}={\sum_{p\leq p_n}k_{j,p}\over V_n^{j/2}}.
 \tag{12}
\]

Adding one local factor gives the exact nonautonomous cocycle

\[
 V'=V+v_p,
 \qquad
 c_j'={V^{j/2}c_j+k_{j,p}\over(V+v_p)^{j/2}}.
 \tag{13}
\]

The prime or local-factor schedule is part of the state.  Calling (13) a
single autonomous universal flow would lose information.

## 4. Fixed and contracting directions

There is an autonomous benchmark: take four independent copies and rescale to
preserve variance,

\[
 \mathcal R_4X={X_1+X_2+X_3+X_4\over2}.
 \tag{14}
\]

**Theorem 4.1 (exact linearized spectrum).**  In cumulant coordinates,

\[
 \kappa_j(\mathcal R_4X)=2^{2-j}\kappa_j(X).
 \tag{15}
\]

Hence:

| coordinate | eigenvalue | interpretation |
|---|---:|---|
| mean `kappa_1` | `2` | relevant; centering is necessary |
| variance `kappa_2` | `1` | marginal normalization coordinate |
| skew `kappa_3` | `1/2` | slowest centered symmetry-breaking direction |
| kurtosis `kappa_4` | `1/4` | leading direction when odd cumulants vanish |
| order `j>=3` | `2^(2-j)` | strictly contracting |

**Proof.**  Cumulants add over four independent copies and scale by `2^-j`
under division by two.  QED.

The centered, variance-one Gaussian jet is therefore the unique fixed point in
every finite cumulant chart.  This does not classify infinite-variance stable
laws, which lie outside the chart, and equality of finitely many zero higher
cumulants does not identify a Gaussian distribution.

For the degree-one `SU(2)` character,

\[
 \mathbb E\chi_1^{2k}=1,2,5,14\quad(k=1,2,3,4),
 \tag{16}
\]

and

\[
 (\kappa_2,\kappa_4,\kappa_6,\kappa_8)
 =(1,-1,5,-56).
 \tag{17}
\]

These exact numbers drive the weighted Euler proxy below.

## 5. A compact-model phase transition at one half

Let `U_p` be independent Haar `SU(2)` conjugacy classes indexed by the primes,
and put

\[
 X_p=\chi_1(U_p),\qquad
 S_x(\sigma)=\sum_{p\leq x}p^{-\sigma}X_p,
 \qquad
 V_x(\sigma)=\sum_{p\leq x}p^{-2\sigma},
 \tag{18}
\]

for real `sigma>=0`.  This is the degree-one term of the compact Euler-log
model.  It is not an arithmetic Euler product.

For general positive variance weights `a_p`, set

\[
 A=\sum_pa_p,qquad H_k={\sum_pa_p^k\over A^k},qquad
 \rho={\max_pa_p\over A}.
 \tag{19}
\]

Equations (17) and exact cumulant addition give

\[
 \boxed{c_4=-H_2,\qquad c_6=5H_3,\qquad c_8=-56H_4.}
 \tag{20}
\]

Moreover,

\[
 H_k\leq\rho^{k-1}.
 \tag{21}
\]

This follows termwise from `a_p^k <= (max a)^(k-1)a_p`.

**Theorem 5.1 (variance-budget transition).**

1. If `0<=sigma<=1/2`, then
   \[
    {S_x(\sigma)\over\sqrt{V_x(\sigma)}}
    \Longrightarrow N(0,1).
    \tag{22}
   \]
   Every fixed standardized cumulant of order above two tends to zero.
2. If `sigma>1/2`, then `S_x(sigma)` converges in `L^2` to a finite-variance
   limit `S_infinity(sigma)`, and its variance-normalized limit is not
   Gaussian.  In fact
   \[
    \kappa_4\left({S_\infty\over\sqrt{V_\infty}}\right)
    =-{\sum_pp^{-4\sigma}\over(\sum_pp^{-2\sigma})^2}<0.
    \tag{23}
   \]

**Proof.**  If `sigma<=1/2`, comparison with the divergent prime harmonic
series gives `V_x -> infinity`, while the largest variance weight divided by
`V_x` tends to zero.  Since `X_p` is bounded, centered, symmetric, and has
variance one, the logarithm of the characteristic function has the uniform
expansion

\[
 \log\mathbb E\exp(itp^{-\sigma}X_p/\sqrt{V_x})
 =-{t^2p^{-2\sigma}\over2V_x}
  +O_t(p^{-4\sigma}/V_x^2).
 \tag{24}
\]

Summing the error and using (21) makes it tend to zero, proving (22).  The
cumulant statement follows from the same power-sum bound.

If `sigma>1/2`, comparison with `sum_n n^(-2sigma)` makes the variance series
convergent, so the independent centered partial sums are `L^2` Cauchy.  Their
tails also tend to zero in `L^4`, because for any finite tail `T`,

\[
 \mathbb ET^4=3(\operatorname{Var}T)^2-
               \sum_{p\text{ in tail}}p^{-4\sigma}
 \leq3(\operatorname{Var}T)^2.
 \tag{25}
\]

The fourth moments therefore pass to the limit.  Exact cumulant addition and
`kappa_4(X_p)=-1` give (23), which excludes a Gaussian limit.  QED.

There is a residual invariant exactly on the critical boundary.  Write
`P_x(k)=sum_(p<=x)p^(-k)`.  At `sigma=1/2`, equation (20) gives

\[
 V_x^2c_4=-P_x(2),\qquad
 V_x^3c_6=5P_x(3),\qquad
 V_x^4c_8=-56P_x(4).
 \tag{25a}
\]

Hence these rescaled coordinates converge to `-P(2)`, `5P(3)`, and
`-56P(4)`, where `P(k)=sum_p p^(-k)`.  The normalized law becomes Gaussian,
but its irrelevant directions retain exact early-prime memory at their next
scale.  These compact prime-zeta amplitudes are universal background, not an
arithmetic-family anomaly.

The first eight primes in the executable packet already separate the two
finite-prefix regimes: with variance weights `1/p`, `|c_4|` is about `0.209`;
with weights `1/p^2`, it is about `0.394`.  These decimals are only readable
renderings of exact fractions and are not evidence for the limiting theorem.

At the critical value `sigma=1/2`, every fixed `r>=2` term of a truncated
Euler logarithm has square-summable coefficients `p^(-r/2)/r`.  Thus the
degree-one component is the only divergent variance channel in this
independent fixed-truncation model; the higher trace powers do not change the
Gaussian bulk after normalization by `sqrt(V_x)`.

This observation extends to a hierarchy.  Put

\[
 T_r(U)=\operatorname{Tr}(U^r)-
        \mathbb E\operatorname{Tr}(U^r).
 \tag{26}
\]

Character orthogonality gives

\[
 \operatorname{Var}(T_r)=
 \begin{cases}1,&r=1,2,\\2,&r\geq3.\end{cases}
 \tag{27}
\]

Consider a finite channel packet whose first nonzero trace coefficient is
`r_0`:

\[
 Y_x(\sigma)=\sum_{p\leq x}\sum_{r=r_0}^R
 c_rp^{-r\sigma}T_r(U_p),\qquad c_{r_0}\ne0.
 \tag{28}
\]

**Theorem 5.2 (trace-channel critical hierarchy).**  For `sigma>0`, the
variance boundary of (28) is

\[
 \boxed{\sigma_c(r_0)={1\over2r_0}.}
 \tag{29}
\]

If `sigma<=sigma_c(r_0)`, the variance diverges and the variance-normalized
packet tends to a standard Gaussian.  If `sigma>sigma_c(r_0)`, the packet
converges in `L^2`.

**Proof.**  At one prime the leading variance term is

\[
 c_{r_0}^2\operatorname{Var}(T_{r_0})p^{-2r_0\sigma}.
 \tag{30}
\]

Every cross or higher-channel term is this weight times a factor tending to
zero.  If the leading prime sum diverges, weighted Cesaro convergence makes
the sum of all such errors little-oh of the leading sum.  The largest bounded
local increment is negligible compared with the square root of total
variance, so the same characteristic-function argument as (24) proves the
Gaussian limit.  The leading sum diverges exactly when
`2r_0 sigma<=1`, by comparison with `sum_p 1/p`.  Above that boundary, every
square and cross coefficient is summable, making the partial sums `L^2`
Cauchy.  QED.

This gives inverse detector design a concrete renormalization cost.  On
`sigma=1/2`, retaining the first trace lies exactly on the divergent-variance
boundary.  Exactly nulling it makes `r_0>=2`, so all remaining fixed trace
channels are square-summable and early-prime-sensitive.  That change of basin
is a compact-model fact, not evidence that the nulled detector has isolated an
arithmetic or RH-relevant signal.

## 6. What is universal background and what could be signal

The previous theorem identifies a compact independent background:

* divergent distributed variance gives Gaussian attraction;
* a small number of high-leverage primes delays that attraction;
* summable variance retains a non-Gaussian memory of the early factors;
* exact center symmetry removes odd directions, making kurtosis the slowest
  surviving compact perturbation;
* conditioning that breaks center symmetry exposes the more slowly contracting
  skew direction.

This supplies a concrete detector-design rule.  An arithmetic anomaly should
not be declared from raw skew or kurtosis until the exact local compact
cumulants and the maximum-variance leverage have been removed or reported.
The residual to study is not merely a histogram difference; it is the
mixed-prime cumulant defect in Section 8.

## 7. A finite jet cannot certify a sign cone

The formal closure of Section 3 does not make a finite jet a sufficient
statistic.  Here is an exact counterexample.

Define two probability laws

\[
 \begin{array}{c|ccc}
  x&0&2&4\\ \hline
  \mu_+(x)&1/16&10/16&5/16
 \end{array}
 \qquad
 \begin{array}{c|ccc}
  x&1&3&5\\ \hline
  \mu_-(x)&5/16&10/16&1/16.
 \end{array}
 \tag{31}
\]

The alternating fifth finite difference annihilates every polynomial of
degree at most four, so the two laws have exactly the same raw moments and
cumulants through order four:

\[
 \kappa_1={5\over2},\quad
 \kappa_2={5\over4},\quad
 \kappa_3=0,\quad
 \kappa_4=-{5\over8}.
 \tag{32}
\]

But

\[
 \kappa_5(\mu_+)=-{15\over4},\qquad
 \kappa_5(\mu_-)={15\over4},
 \tag{33}
\]

and, after centering at their common mean,

\[
 \Pr_{\mu_+}(X-\mathbb EX>0)={5\over16},\qquad
 \Pr_{\mu_-}(X-\mathbb EX>0)={11\over16}.
 \tag{34}
\]

**Corollary 7.1 (four-jet sign obstruction).**  No rule depending only on the
first four cumulants can determine even the direction of centered sign bias.

More generally, splitting the positive and negative parts of the alternating
`(m+1)`-st binomial difference produces distinct probability laws with equal
moments through order `m`.  A claimed one-sided invariant cone therefore needs
support, transform, total-positivity, or full-law input beyond a finite
cumulant chart.

## 8. The arithmetic residual that should be measured next

In a genuine family, local Frobenius variables attached to the same global
member need not be independent.  For `S=sum_p X_p`, multilinearity of joint
cumulants gives the exact identity

\[
 \kappa_m(S)=
 \sum_{p_1,\ldots,p_m}
 \kappa(X_{p_1},\ldots,X_{p_m}).
 \tag{35}
\]

The independent compact baseline retains only the all-equal tuples.  Define

\[
 \Delta_m=
 \kappa_m(S)-\sum_p\kappa_m(X_p)
 =\sum_{\substack{p_1,\ldots,p_m\\
                   \text{not all equal}}}
   \kappa(X_{p_1},\ldots,X_{p_m}).
 \tag{36}
\]

This `Delta_m` is the exact finite-dimensional arithmetic coupling channel.
For `m=2` it is twice the sum of cross-prime covariances.  It vanishes in the
model proved above, so a nonzero value in a complete arithmetic family cannot
be blamed on independent Haar aggregation.

Local marginals cannot recover this channel.  Take two formal places whose
individual detector at each place has the Haar `chi_1` law.  Compare three
joint couplings:

\[
 (X,Y)=(X,X'),\qquad (X,X),\qquad (X,-X),
 \tag{37}
\]

where `X'` is independent of `X`.  Symmetry of the `chi_1` law makes both
marginals identical in every case.  Nevertheless,

\[
 \begin{array}{c|ccc}
  &\text{independent}&\text{diagonal}&\text{central antidiagonal}\\ \hline
  \kappa_2(X+Y)&2&4&0\\
  \kappa_4(X+Y)&-2&-16&0\\
  \Delta_2&0&2&-2\\
  \Delta_4&0&-14&2
 \end{array}
 \tag{38}
\]

**Proposition 8.1 (local-marginal nonidentifiability).**  Even complete exact
knowledge of every one-place law does not determine the aggregate
renormalization flow.  Joint-place provenance is indispensable.

The table is a proof: all one-place marginals agree while their aggregate
cumulants differ.  The central-antidiagonal coupling also shows why variance
normalization must occur after, not before, cross-place covariance is measured.

### Falsifiable moonshot target (not a claim)

Choose one source-locked genus-two family, two prime places, and one detector
that has already been quotiented by its forced Haar channels.  Compute
`Delta_2,...,Delta_6` over several extension degrees.  Test the exact target:

> after Tate/boundary terms are subtracted, the extension-degree residual
> vector lies in a recurrence of rank at most two.

This target can fail cleanly: a third nonzero recurrence eigenvalue, or failure
on a held-out extension degree, refutes it.  If it survives, the recurrence
roots become a precise proposed Frobenius/cohomological channel rather than a
visual renormalization metaphor.

The first bounded experiment should use an existing complete family table and
only two places.  Broad prime sweeps, zero computations, and new curve
enumeration are neither necessary nor justified by this packet.

## 9. Interpretation boundary

The exact conclusions are:

1. a fixed finite initial character span is not multiplicatively closed;
2. cumulant jets are exactly closed under independent aggregation to their
   declared formal order;
3. the four-copy centered variance-one flow has a Gaussian fixed jet and the
   explicit spectrum `2^(2-j)`;
4. the independent degree-one `SU(2)` Euler proxy has a sharp variance-budget
   transition at `sigma=1/2`;
5. a detector's first surviving trace channel `r_0` shifts that boundary to
   `sigma=1/(2r_0)`;
6. a four-cumulant jet cannot identify a centered sign bias;
7. equal one-place marginal laws need not determine any aggregate flow; while
8. mixed-prime joint cumulants are the exact residual omitted by the
   independent compact model.

None of these statements supplies arithmetic equidistribution, an
individualization theorem, a zero-free region, or an RH implication.  Their
use is methodological: they separate universal aggregation effects,
projection artifacts, high-leverage local factors, and genuine cross-prime
arithmetic coupling before a detector is interpreted.
