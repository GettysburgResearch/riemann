# The block-checkerboard coset interferometer

Status: **exact formal block-Gram/Fourier theorem and exact transverse path
model; no native FFPS source, varying-conductor estimate, RH, or GRH claim**

Exact replay:
[`ffps_block_checkerboard_coset_interferometer.py`](ffps_block_checkerboard_coset_interferometer.py)

## 0. Outcome

Splitting one global checkerboard into several disjoint checkerboard blocks
creates an exact leverage--spectrum tradeoff.

Let the local square-phase factors be partitioned into `r` nonempty blocks
`B_1,...,B_r`.  For `i in B_j` put

\[
 m_i={p_i-1\over2},\qquad q_i={p_i+1\over2},
\]

and define

\[
 M_j=\prod_{i\in B_j}m_i,\qquad
 Q_j=\prod_{i\in B_j}q_i,\qquad
 P_j=\prod_{i\in B_j}p_i,\qquad
 M=\prod_jM_j.
\tag{0.1}
\]

Impose the top-character parity separately in every block.  The retained
subgroup has quotient

\[
 K=C_2^r,\qquad h=|K|=2^r.
\]

The restricted constant eigenvalue and sharp hard leverage are

\[
 \boxed{
 \mu_A={1\over2^r}\prod_{j=1}^r(P_j+Q_j),
 \qquad
 L_A={4^rM\over\prod_j(P_j+Q_j)}
 =\prod_{j=1}^r{4M_j\over P_j+Q_j}.}
\tag{0.2}
\]

This is the **block-leverage factorization theorem**.  Every quotient coset
has the same sharp uniform weight `h` and the same leverage.

The cost is spectral: the quotient has `h-1` nonprincipal characters.  For a
finite source atom set with quotient phase `Phi:Omega -> K`, put

\[
 P=\sum_{\omega}z_\omega,
 \qquad
 H_\chi=\sum_\omega\chi(\Phi(\omega))z_\omega,
\]

and normalize the coset observations by

\[
 O_a=h\sum_{\Phi(\omega)=a}z_\omega
 \qquad(a\in K).
\tag{0.3}
\]

Then the ordered **off-coset interferometer** is

\[
 \boxed{
 \mathcal I
 ={1\over h(h-1)}\sum_{a\ne b}O_a\overline{O_b}
 =|P|^2-{1\over h-1}\sum_{\chi\ne\mathbf1}|H_\chi|^2.}
\tag{0.4}
\]

It is literally atom-free.  If `D=sum_omega |z_omega|^2`, the principal
term in (0.4) has atomic diagonal `D`, while the **averaged selected atomic diagonal**
is also exactly `D`:

\[
 {1\over h-1}\sum_{\chi\ne\mathbf1}|H_\chi|^2
 \quad\hbox{has diagonal}\quad D.
\tag{0.5}
\]

Thus exact cancellation of the interferometer requires, and is equivalent
to,

\[
 \boxed{
 \sum_{\chi\ne\mathbf1}|H_\chi|^2=(h-1)|P|^2.}
\tag{0.6}
\]

This is the zero threshold for the *averaged off-coset interferometer*.
It is not the different extremal problem of forcing one chosen `O_a` to
vanish; Cauchy--Schwarz gives the sharp selected-energy cost
`|P|^2/(h-1)` for that one-coset cancellation.

There is also an exact sheaf-complexity candidate for these `h-1` modes.
Realize the `r` block-top generators by `r` endpoint-disjoint telescoping
path blocks.  Their selected subspace has injective incidence boundary, so
it contains no nonzero invariant mode.  If all endpoint primes have degree
`e`, the average modewise maximally extended first Betti number is

\[
 \boxed{
 \overline b_1
 ={2er2^{r-1}-2(2^r-1)\over2^r-1}
 ={er\over1-2^{-r}}-2
 =er-2+{er\over2^r-1}.}
\tag{0.7}
\]

Hence `overline b_1 ~ er-2`.  The normalized interferometer sees a selected
average with linear geometric complexity even though its quotient contains
exponentially many modes.  This is a **coupled candidate, not a native-source theorem**:
the Gram, source, maximal-extension, and global trace gates remain separate.

## 1. Frozen dependencies and scope

| source | commit | blob | role |
|---|---|---|---|
| `FFPS_CORRELATED_MASK_AMPLIFIER.md` | `12f52a223` | `4569c521e99e8c591f1694126605f8abee8a75f8` | formal product Gram and one-checkerboard leverage |
| `FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md` | `9e116ec41` | `19d0ce572fcd70e68b1618462bea29a2958b7f9e` | quotient-coset Fourier projector and Wick normalization |
| `FFPS_GRAPH_KUMMER_CHARACTER_SPECTRUM.md` | `2e06d1561` | `a981ff9f50bc2b5e434f83a2023dd0b298a84e4a` | incidence boundary, invariant modes, and transversality |
| `FFPS_CHECKERBOARD_TELESCOPING_CURVE_MODEL.md` | `cb45027c1` | `7d478fa212d39f9d222b05e1d94e266415e8d641` | path telescoping and maximal/common-open firewall |

The finite theorem uses distinct primes `p_i=1 mod 4`, so the sign-pair group
`F_{p_i}^x/{+-1}` has a nontrivial quadratic character.  The path model is a
separate function-field construction on `P^1`.  No line below identifies the
number-field phase primes with closed places of one native FFPS family.

The cohomology dimensions import Grothendieck--Ogg--Shafarevich and duality
for tame nonconstant rank-one Kummer sheaves.  Deligne's trace bounds would
apply to each legally maximally extended pure line, but this packet does not
turn the squared family energies in (0.4) into one such trace sum.

## 2. Exact block-restricted Gram

Let

\[
 G=\bigotimes_i(p_iI-J)
\tag{2.1}
\]

on the complete sign-pair coordinate group.  For block `j`, let `tau_j` be
the product of the local quadratic characters in `B_j`.  The `tau_j` are
independent because the blocks are disjoint.  Put

\[
 A=\bigcap_{j=1}^r\ker\tau_j.
\tag{2.2}
\]

Then `A` has index `h=2^r` and size `M/h`.  Its indicator has the exact
Fourier expansion

\[
 \mathbf1_A={1\over2^r}
 \sum_{S\subseteq[r]}\tau_S,
 \qquad
 \tau_S=\prod_{j\in S}\tau_j.
\tag{2.3}
\]

The complete Gram eigenvalue on `tau_S` is

\[
 \lambda_S
 =\prod_{j\in S}P_j\prod_{j\notin S}Q_j.
\tag{2.4}
\]

On `A`, every `tau_S` equals one.  Restricting `G1_A` to `A`, (2.3)--(2.4)
therefore give the constant row sum

\[
 \mu_A
 ={1\over2^r}\sum_{S\subseteq[r]}\lambda_S
 ={1\over2^r}\prod_j(P_j+Q_j).
\tag{2.5}
\]

Translation invariance gives the same row sum on every coset of `A`.
Consequently

\[
 E_A=\mathbf1_A^*G\mathbf1_A
 ={M\over4^r}\prod_j(P_j+Q_j).
\tag{2.6}
\]

The frozen restricted-Gram extremal identity says that the sharp dual cost
is `M^2/E_A`.  This proves (0.2).  It also gives the unique optimal weight

\[
 \alpha_{\rm opt}
 ={M\,G_A\mathbf1\over E_A}
 =2^r\mathbf1_A.
\tag{2.7}
\]

The factorization in (0.2) is exact, but it does not say that arbitrarily
many block constraints are legal in the physical FFPS source.  The frozen
source bridge realizes only its declared fixed bilateral checkerboard.

The bounded replay separates two controls.  The small `(5,13)|(17)` panel is
used for direct matrix row sums, even though its one-prime second block does
not improve the complete-frame leverage.  The formula-only
`(5,13)|(17,29)` panel has

\[
 L_A={24\over43}{112\over157}
 ={2688\over6751}
 <{448\over945}=L_{\rm full},
\tag{2.8}
\]

so product block amplification is nonvacuous without enlarging the direct
matrix replay.

## 3. Quotient Fourier algebra

For `a in K`, Fourier inversion of the normalized coset indicator gives

\[
 O_a
 =\sum_{\chi\in\widehat K}\chi(a)^{-1}H_\chi,
 \qquad H_{\mathbf1}=P,
\tag{3.1}
\]

up to the harmless simultaneous inverse convention.  Orthogonality gives

\[
 {1\over h}\sum_a|O_a|^2
 =|P|^2+\sum_{\chi\ne\mathbf1}|H_\chi|^2.
\tag{3.2}
\]

Also `sum_a O_a=hP`.  Removing the diagonal `a=b` from the complete ordered
coset square yields

\[
\begin{aligned}
 \sum_{a\ne b}O_a\overline{O_b}
 &=\left|\sum_aO_a\right|^2-\sum_a|O_a|^2\\
 &=h^2|P|^2-h\left(
 |P|^2+\sum_{\chi\ne\mathbf1}|H_\chi|^2
 \right).
\end{aligned}
\tag{3.3}
\]

Dividing by `h(h-1)` proves (0.4).

The selected energy also has the exact dispersion form

\[
 \boxed{
 \sum_{\chi\ne\mathbf1}|H_\chi|^2
 ={1\over h^2}\sum_{a<b}|O_a-O_b|^2.}
\tag{3.4}
\]

Indeed the usual pair-difference identity gives

\[
 \sum_{a<b}|O_a-O_b|^2
 =h\sum_a|O_a|^2-\left|\sum_aO_a\right|^2,
\]

and (3.2) finishes the calculation.  Thus the nonprincipal energy measures
the exact dispersion among the sharp coset observations.

### 3.1 Atomic and same-coset cancellation

Put `D=sum_omega |z_omega|^2`.  The normalization ledger is

| quadratic object | literal atomic diagonal |
|---|---:|
| `|P|^2` | `D` |
| `sum_(chi!=1)|H_chi|^2` | `(h-1)D` |
| `(h-1)^(-1)sum_(chi!=1)|H_chi|^2` | `D` |
| `h^(-1)sum_a|O_a|^2` | `hD` |
| `I` | `0` |

This keeps two repairs distinct.  The *total* selected covariance has Wick
coefficient `h-1`; the selected average appearing in (0.4) has coefficient
one.  Neither number is the phase-Gram diagonal repair studied in the
separate phase-spectrum packet.

The cancellation is stronger than deletion of `omega=nu`.  For quotient
phases `x,y`, the kernel of (0.4) is

\[
 1-{1\over h-1}\sum_{\chi\ne\mathbf1}
 \chi(x)\overline{\chi(y)}
 =\begin{cases}
 0,&x=y,\\
 h/(h-1),&x\ne y.
 \end{cases}
\tag{3.5}
\]

Thus every same-coset pair disappears.  What remains is a signed off-coset
correlation, not a positive quadratic form.  Equation (0.6) is an exact
balance condition; this packet proves no arithmetic estimate forcing it.

## 4. Endpoint-disjoint path blocks

Fix an odd prime power `q`.  Let block `j` contain `d_j>=1` local factors.
Choose distinct monic irreducibles

\[
 R_{j,0},R_{j,1},\ldots,R_{j,d_j}\in\mathbf F_q[T]
\]

of one common degree `e`, with all polynomials distinct across all blocks,
and set

\[
 f_{j,k}={R_{j,k-1}\over R_{j,k}}
 \qquad(1\le k\le d_j).
\tag{4.1}
\]

The ambient graph is a disjoint union of `r` paths.  It has

\[
 D=\sum_jd_j\quad\hbox{edges},\qquad D+r\quad\hbox{vertices},
\]

and binary cycle dimension zero.  Hence all `D` edge squareclasses are
geometrically independent and the ambient product torsor has deck group
`C_2^D`.

Let `w_j` be the all-edge vector of path `j`, and put

\[
 W=\langle w_1,\ldots,w_r\rangle_{\mathbf F_2}.
\tag{4.2}
\]

Under the formal identification `tau_j <-> w_j`, this is the annihilator
character space of the retained subgroup `A`.  Its `2^r-1` nonzero vectors
therefore index exactly the nonprincipal quotient modes in (0.4).

For the incidence boundary `partial`, telescoping gives

\[
 \partial w_j
 =\delta_{R_{j,0}}+\delta_{R_{j,d_j}}.
\tag{4.3}
\]

These endpoint pairs are disjoint.  Therefore the `r` boundary vectors are
linearly independent:

\[
 \boxed{
 \partial|_W\text{ is injective},\qquad
 W\cap Z_1=0.}
\tag{4.4}
\]

By the frozen mask-transversality theorem, `W` contains no nonzero invariant
selected mode.

For a nonempty subset `S subset [r]`, multiplication telescopes separately
inside each path:

\[
 \prod_{j\in S}\prod_{k=1}^{d_j}f_{j,k}
 =\prod_{j\in S}{R_{j,0}\over R_{j,d_j}}.
\tag{4.5}
\]

It is ramified at exactly `2|S|` degree-`e` closed places, hence at
`2e|S|` geometric points.  On its modewise maximal lisse open it is a
nonconstant tame rank-one Kummer line with

\[
 \dim H_c^0=\dim H_c^2=0,
 \qquad
 \dim H_c^1=2e|S|-2.
\tag{4.6}
\]

There are `binom(r,k)` modes with `|S|=k`.  Since

\[
 \sum_{k=1}^rk\binom rk=r2^{r-1},
\]

the total selected first Betti number is

\[
 \boxed{
 B_{1,\rm total}
 =2er2^{r-1}-2(2^r-1).}
\tag{4.7}
\]

Division by `2^r-1` proves (0.7).

### 4.1 The maximal-extension firewall

Formula (0.7) is a modewise maximal-extension average.  The common ambient
torsor open removes the roots of all `D+r` vertex primes.  On that one
common open, every nonzero selected line instead has

\[
 \dim H_c^1=e(D+r)-2.
\tag{4.8}
\]

For mode `S`, the removable-puncture tax is

\[
 e(D+r-2|S|).
\tag{4.9}
\]

Its average is

\[
 \boxed{
 e\left(D+r-{r2^r\over2^r-1}\right).}
\tag{4.10}
\]

Different selected modes generally have different maximal opens.  Filling
their inactive endpoints and all path interiors changes the trace statistic
unless the native source supplies exact boundary corrections.  One may not
insert (0.7) into (0.4), apply Deligne mode by mode, and call the result a
common-source estimate.  This is the load-bearing **maximal-extension
firewall**.

The unnormalized selected sum also contains `2^r-1` terms and pays the total
cost (4.7), not the average (0.7).  The average is relevant only because the
interferometer itself contains the explicit factor `1/(h-1)`; turning that
formal normalization into an arithmetic moment bound is open.

## 5. Coupled architecture and exact boundary

The candidate coupling is

\[
\begin{array}{c}
\text{block-top parities }\tau_1,\ldots,\tau_r\\
\downarrow\\
K=C_2^r\text{ hard cosets and product leverage (0.2)}\\
\downarrow\\
\text{off-coset signed recombination (0.4)}\\
\downarrow\\
W=\langle w_1,\ldots,w_r\rangle
\text{ with transverse path endpoints (4.4)}.
\end{array}
\tag{5.1}
\]

Each arrow is exact in its own declared model.  The packet does not prove
that all arrows occur inside one native FFPS source.  In particular it does
not prove:

1. a many-block physical orientation compatible with varying owners and
   conductors;
2. permission to impose every hard quotient coset before squaring;
3. an identification of the selected source modes with the path Kummer
   lines on one common open;
4. legal filling of the mode-dependent removable punctures;
5. a signed varying-conductor estimate for (0.4);
6. survival and individualization of a hypothetical principal anomaly.

The exact positive result is narrower but useful: product hard leverage,
atom-free quotient interferometry, invariant-free selected geometry, and a
linear average maximal Betti cost are mutually compatible at the formal
algebraic level.  This is a candidate architecture for a future producer,
not that producer.

## 6. Proof ledger

| statement | grade |
|---|---|
| restricted constant eigenvalue (2.5) | **PROVED EXACT FORMAL GRAM** |
| sharp hard leverage and block factorization (0.2) | **PROVED EXACT FORMAL GRAM** |
| uniform coset optimizer `h` | **PROVED EXACT FORMAL GRAM** |
| coset Fourier identities (3.1)--(3.4) | **PROVED EXACT FINITE FOURIER ALGEBRA** |
| atomic/same-coset cancellation (0.5), (3.5) | **PROVED EXACT** |
| cancellation criterion (0.6) | **PROVED AS AN EQUIVALENT FINITE IDENTITY; NOT AN ESTIMATE** |
| endpoint-disjoint boundary injectivity (4.4) | **PROVED EXACT GRAPH ALGEBRA** |
| absence of invariant selected modes | **PROVED FROM IMPORTED TRANSVERSALITY THEOREM** |
| maximal `H_c^1` formula (4.6) | **PROVED FROM IMPORTED GOS + DUALITY** |
| total and average Betti formulas (4.7), (0.7) | **PROVED EXACT FROM (4.6)** |
| common-open tax (4.9)--(4.10) | **PROVED EXACT FROM IMPORTED OPEN-CURVE FORMULA** |
| one native source realizing (5.1) | **OPEN** |
| legal maximal extension in that source | **OPEN / CENTRAL** |
| varying-conductor estimate, principal individualization, RH, or GRH | **OPEN / UNPROVED** |

## 7. Bounded replay

The producer uses exact integers, Gaussian-integer pairs, and rational
numbers.  It:

- directly checks all four restricted coset row sums on the small
  `(5,13)|(17)` block panel using `2,304` Gram cells;
- checks the strict formal leverage gain on `(5,13)|(17,29)` without
  constructing its large matrix;
- checks the Fourier and off-coset kernels for `1<=r<=5`;
- checks a literal single-atom cancellation row;
- checks path-block boundary injectivity and every selected mode for
  `1<=r<=6`;
- performs no finite-field, polynomial, curve, conductor-family, or
  `L`-function-zero enumeration.

Run:

~~~powershell
python research/l-families/atlas/function_field/ffps_block_checkerboard_coset_interferometer.py --check
python -O research/l-families/atlas/function_field/ffps_block_checkerboard_coset_interferometer.py --check
python -m unittest tests.test_ffps_block_checkerboard_coset_interferometer
python -O -m unittest tests.test_ffps_block_checkerboard_coset_interferometer
python -m ruff check research/l-families/atlas/function_field/ffps_block_checkerboard_coset_interferometer.py tests/test_ffps_block_checkerboard_coset_interferometer.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_block_checkerboard_coset_interferometer.py tests/test_ffps_block_checkerboard_coset_interferometer.py
~~~

## 8. Novelty boundary

The subgroup indicator, finite Fourier identities, binary incidence map,
and binomial average are elementary.  The project contribution is their
source-aware coupling into a block-leverage/interferometer/transverse-path
candidate with explicit Wick and maximal-extension ledgers.  No external
novelty or priority claim is made.
