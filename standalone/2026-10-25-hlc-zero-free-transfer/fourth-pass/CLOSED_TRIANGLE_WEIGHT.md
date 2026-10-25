# A paid common-list triangle in the original HLC path measure

**Status: a proved restricted raw-path bound, followed by a
source-dependent discrete-root transfer.** The first theorem controls an
actual three-edge subfamily with the original state weights, list
symmetrization, cutoffs, damping and one projective-line draw per prime.
Its saving is obtained by counting all integer intermediate paths and
then averaging their gcd ratio. There is no inserted `1/Y` in an edge.

The subfamily has the same shared lists on all three edges and returns
to its initial position and complete unordered lists. This is a
restricted absolute contribution. It does not bound the entire raw
operator, the centered raw-minus-major-arc operator, a full even moment,
or the native inverse expression. Immediate two-edge backtracks and
three-edge paths with changing shared lists are additional cases.

The source is Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242), with PDF SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.
The original state measure and symmetrizer are (4.12)--(4.13); the
definitions of `K_1,T_1` are on p. 18; the root measure and independent
once-only line draws are Proposition 4.4 and (4.29); the position ratio
is (4.40). The discrete assertion below explicitly imports the final
finite-residue count of Appendix A, with its `S^5` discrepancy.

The integer path-count calculation is proved in
[THREE_EDGE_INTEGER_BRIDGE.md](THREE_EDGE_INTEGER_BRIDGE.md), equations
(15d)--(15e). The present note derives its transfer to the genuine
original source weights, outside the auxiliary Fock representation.

## 1. The precise triangle class and its state normalization

Let `P_i` be disjoint finite sets of odd primes, `1<=i<=K`, and put

$$
 V_i=\sum_{p\in\mathcal P_i}\frac1p>0.
$$

Fix the source list length `J+1`, with `J>=1`. In each group choose
an unordered set `D_i` of J shared primes and three unshared primes
`a_i,b_i,c_i`. The consecutive active lists are

$$
 D_i\cup\{b_i\}\ \longrightarrow\
 D_i\cup\{a_i\}\ \longrightarrow\
 D_i\cup\{c_i\}\ \longrightarrow\
 D_i\cup\{b_i\}.
 \tag{1}
$$

Every edge must be legal in the original operator. Consequently the
three unshared primes are pairwise distinct within each group: the
first two transitions exclude `a_i=b_i` and `c_i=a_i`, and the
closing transition excludes `b_i=c_i`. All are outside `D_i`.
Disjointness of the prime groups now gives squarefree, pairwise
coprime products

$$
 D=\prod_i\prod_{p\in D_i}p,\qquad
 a=\prod_i a_i,\quad b=\prod_i b_i,\quad c=\prod_i c_i.
 \tag{2}
$$

Retain `d_0<=D<2d_0` and `a,b,c in [Y,4Y]`, with `Y>=1`.
An integer product determines its prime in each group uniquely; there
is no factorization multiplicity when the products are summed later.
The shared sets are also determined by their product D.

The relative positions are `z_0=z_3=(1,0)`, with primitive integer
`z_1,z_2`; retain the source parity, region and good-state restrictions.
The raw determinants are

$$
 j_0=D(b-a),\qquad j_1=D(a-c),\qquad j_2=D(c-b),
                  \qquad j_0+j_1+j_2=0.
 \tag{3}
$$

The chronological complete products are `(Db,Da,Dc,Db)`, so (3)
uses the original operator's old-minus-new convention exactly.
The three distinct products ensure all three determinants are nonzero.

Write

$$
 \sigma=\prod_iV_i^{-(J+1)},\qquad
 n_{\rm ord}=((J+1)!)^K.
$$

Each unordered state represents `n_ord` ordered states, all with
measure sigma. In the orthonormal basis of permutation-invariant
unordered states, a single symmetric edge has matrix entry

$$
 A_{s,t}=(J+1)^{-K}\prod_iV_i^{-1}
                          K_{\rm raw}(s,t).
 \tag{4}
$$

Indeed, only the `(J!)^K` orderings placing the departing prime last
are compatible among the `((J+1)!)^K` orderings. Equal orbit measures
cancel in the normalized basis. This is the normalization checked
independently in `HLC_PATH_CANCELLATION.md`, Section 6.

The actual root vector is the function one on lists at the root.
Its coordinate on an unordered root state is
`sqrt(n_ord*sigma)`. For the list-diagonal contribution (1), its two
endpoint coordinates therefore contribute `n_ord*sigma`. Combining
this with the three entries (4) gives exactly

$$
 C_{J,K,V}
 =((J+1)!)^K(J+1)^{-3K}\prod_iV_i^{-(J+4)}
 \tag{5}
$$

before the three raw kernels and the root/line averages are applied.
The final ordering need not equal the initial ordering: the complete
**unordered** lists return, as prescribed by the symmetrized source.
Using an ordered-state trace in its place would miss this orbit factor.

## 2. The original prime-line weight is paid once

At fixed real root variables and fixed integer vertices, average the
source's single line `ell_p` uniformly over `P^1(F_p)` for every
prime in the active union. If `p|D`, it is active at every vertex.
Every determinant in (3) is divisible by p. Since the vertices are
primitive, their nonzero reductions have the same projective line;
all its active constraints are therefore consistent and cost exactly
`1/(p+1)`.

A prime in a is active only at `z_1`, a prime in c only at `z_2`,
and a prime in b at the identical endpoints `z_0=z_3`. Each again
has one forced line. In fact, pairwise coprimality in (2) makes its
line different from the lines of the other vertices, by reducing the
corresponding nonzero determinant modulo that prime. Thus its
inactive-vertex damping is one. The remaining primes' damping lies
between zero and one and may be discarded for an upper bound.

It follows that the active-union line average is bounded by

$$
 \prod_{p\mid Dabc}\frac1{p+1}
                         \le\frac1{Dabc}.
 \tag{6}
$$

The primes of D, or of the returning product b, have not been drawn
again. All position and good-state projectors can be retained in this
upper bound; discarding them only enlarges it.

This argument uses actual prime-level distinctness. One cannot first
enlarge to arbitrary distinct integer products and assign them the
weight (6), since two such integers could share a prime. The
enlargement to unrestricted integer triples is made only after (6)
has been proved for the original legal labels.

The three original kernels contribute `(d_0/D)^3<=1`. The raw
arguments of `psi_1` lie in `[-3,3]`, so `psi_1=1` there. Every
unshared product occurs twice in the eta factors, leaving
`eta(a/Y)^2 eta(b/Y)^2 eta(c/Y)^2<=||eta||_infty^6`.
These are the actual original kernel factors. No auxiliary-kernel
normalization and no factor `1/Y` has been transported into (5).

## 3. Count all closed paths before averaging the root

For fixed labels write

$$
 z_1=(h,j_0),\qquad
 z_2=\left(-\frac{j_1+h j_2}{j_0},-j_2\right).
 \tag{7}
$$

The second vector is integral precisely when
`h j_2=-j_1 mod j_0`. Put

$$
 g=\gcd(|j_0|,|j_2|),\qquad q=|j_0|/g.
$$

Since `j_1=-j_0-j_2`, this congruence is exactly `h=1 mod q`.
For each such h there is only one candidate `z_2`. Primitivity and
the other source conditions subsequently delete candidates.

At the global root the source coordinate is `R=-2r`, with
`0<=r<1`; its first relative position satisfies

$$
 \tau_r(z_1)=h-2j_0r\in I=[1/16,16],
                         \qquad |I|=W=255/16.
 \tag{8}
$$

The full multiplicity function
`sum_(h=1 mod q) 1_I(h+j_0 R)` has period `1/g` in R and mean
`W/q`. The interval `R in [-2,0]` contains exactly `2g` periods,
and `dr=|dR|/2`. Thus the exact unprojected candidate count is

$$
 \int_0^1\sum_{h\equiv1\ (q)}1_I(h-2j_0r)\,dr
       =W\frac{g}{|j_0|}
       =W\frac{\gcd(|b-a|,|c-b|)}{|b-a|}.
 \tag{9}
$$

This is a **count**, not the measure of the union of the candidate
events. Its right side need not be at most one. It retains the
multiplicity needed for the original operator expansion. Formula (6)
is first applied only to primitive actual candidates; the count in
(9) then bounds their number by including all integral candidates.

## 4. The continuous root-averaged source triangle bound

Let `T_tri(s,t_0)` denote the absolute contribution of precisely
(1) to the original root pairing, after averaging r and all source
prime lines, with the other normalized root variables fixed at
`s=u/(d_0YM) in [1,16]`, `t_0=v/N in [1,2]`. It uses the root
vector and orbit normalization in (5), and retains the source
cutoffs, positions, parity and good-state projectors. It is a
restricted path sum, not the norm of a new operator.

**Theorem 1 (paid common-shared-list triangle).** Uniformly in s,t_0,

$$
 \boxed{
 T_{\rm tri}(s,t_0)
 \le48W\|\eta\|_\infty^6 (J+1)^{-2K}
       \left(\prod_iV_i^{-4}\right)
             \frac{(1+\log(3Y))^2}{Y}.}
 \tag{10}
$$

Here `48W=765`. This theorem is an exact deduction about the stated
continuous root-and-line model; it does not use the full HLC theorem.

**Proof.** By (5), (6), and (9), its upper bound before summing the
shared lists is

$$
 C_{J,K,V}\|\eta\|_\infty^6 W
 \sum_{D,\,a,b,c}
       \frac1{Dabc}\,
       \frac{\gcd(|b-a|,|c-b|)}{|b-a|}.
 \tag{11}
$$

The labels in this sum still obey all prime-level requirements.
For fixed a,b,c, drop the exclusions on the shared sets and their
dyadic product restriction. The elementary symmetric-sum bound gives

$$
 \sum_{D_1,\ldots,D_K}\frac1D
          \le\prod_i\frac{V_i^J}{J!}.
 \tag{12}
$$

Multiplying (12) by (5) cancels the factorial and shared-prime costs
exactly to

$$
                   (J+1)^{-2K}\prod_iV_i^{-4}.
 \tag{13}
$$

Only now enlarge the remaining a,b,c sum to all pairwise distinct
integers in `[Y,4Y]`. The scalar theorem in the cited bridge note is

$$
 \sum_{\substack{a,b,c\in[Y,4Y]\text{ pairwise distinct}}}
  \frac1{abc}\frac{\gcd(|b-a|,|c-b|)}{|b-a|}
       \le\frac{48}{Y}(1+\log(3Y))^2.
 \tag{14}
$$

For clarity, put `M=floor(3Y)` and fix b. After setting
`h=a-b`, `k=c-b`, there are at most four sign choices. The divisor
identity for gcd gives

$$
 \sum_{1\le k\le M}\gcd(h,k)
 =\sum_{d\mid h}\varphi(d)\lfloor M/d\rfloor
 \le M\tau(h).
$$

Then `sum_(h<=M) tau(h)/h <= (sum_(n<=M)1/n)^2
<= (1+log M)^2`. There are at most `3Y+1<=4Y` choices of b,
`M<=3Y`, and `1/(abc)<=Y^(-3)`, proving (14).
Combining (11)--(14) proves (10). QED.

The full continuous source-root integral includes
`ds dt_0 dr/(3 zeta(2))`. Consequently its bound is (10) multiplied
by at most `15/(3 zeta(2))`. For fixed J,K and `V_i` bounded
below, a polynomial `Y>=x^a` would give a genuine power saving for
this particular triangle class. This does not prove that the entire
source parameter scheme permits the same polynomial redesign.

## 5. A fixed-depth discrete-root transfer with an explicit budget

The discrete conclusion here imports exactly the following source
finite-residue estimate. For an odd squarefree S, fixed projective
lines at its primes, and intervals `I_1,I_2,I_3` in the normalized
root ranges, the normalized count of the original primitive roots
with the required parity is

$$
 \frac{|I_1||I_2||I_3|}{3\zeta(2)\prod_{p\mid S}(p+1)}
       +O\left(S^5\min(d_0YM,N)^{-1/100}\right).
 \tag{15}
$$

This is the final finite-residue formula in the paper's Appendix A.
Its full proof is an external premise of Theorem 2 below. We use its
displayed quantitative estimate, rather than extrapolating the
paper's already-specialized logarithmic parameter choices.

Fix J,K independently of x. Suppose

$$
 \mathcal P_i\subset[x^{a_i},x^{b_i}],\qquad
 \alpha=\sum_i a_i>0,\quad\beta=\sum_i b_i,
 \qquad V_i\ge v_*>0,
 \qquad\min(d_0YM,N)\ge x^\delta.
 \tag{16}
$$

The sets remain disjoint, and all constants in the cutoffs and rho are
fixed. This is a parameter variant of the raw finite-path model:
the source itself uses growing J and subpower prime bands. Let
`T_tri^arith` be the identical restricted absolute triangle
contribution in the original arithmetic root sum, divided by
`d_0YMN` as in Proposition 4.4. The proof below invokes (15)
directly; it does not apply Proposition 4.4's stated even-moment
identity to an odd three-edge expression without a new count.

**Theorem 2 (source-dependent arithmetic triangle).** Under (15)--(16),
for every epsilon>0,

$$
 \boxed{
 T_{\rm tri}^{\rm arith}
 \ll_{J,K,v_*,\eta,\rho,\epsilon}
 x^{-\alpha+\epsilon}
       +x^{(7J+19)\beta-\delta/100}.}
 \tag{17}
$$

In particular both terms save a fixed power whenever
`(7J+19) beta < delta/100`.

**Proof of the discrepancy budget.** For each original label family
the used-prime modulus is the squarefree integer

$$
 S=Dabc\le x^{(J+3)\beta}.
$$

There are at most `x^((J+3) beta)` such families: in each group
there are J shared and three ordered unshared prime choices, and
the unordered choices only reduce this count. For each fixed family,
the first position window in (8) confines h to an interval of length
at most `2|j_0|+W`, where

$$
 |j_0|\le3DY\ll x^{(J+1)\beta}.
$$

Thus there are `O(x^((J+1) beta))` possible integer h before
imposing its congruence, primitivity, parity and other conditions.
The second vertex is uniquely determined by (7). For every retained
primitive candidate, the once-only line at every prime of S is
prescribed; there is no sum over additional line choices.

The event (8) for that fixed h is one interval in `r in [0,1]`.
Drop unused-prime damping, goodness and the other position projectors
for this positive upper count, and take the full s,t_0 root
rectangles. Formula (15) now applies separately to each candidate.
Its main terms sum to the continuous count already bounded by
Theorem 1, with the source factor `15/(3 zeta(2))`.

For the errors, the original orbit and three-edge coefficients are
bounded by a fixed constant under (16). Summing absolute errors gives

$$
 x^{(J+3)\beta}\,x^{(J+1)\beta}\,
 x^{5(J+3)\beta-\delta/100}
       =x^{(7J+19)\beta-\delta/100}.
 \tag{18}
$$

No `1/(Dabc)` factor is assigned to this discrepancy: (15) does not
give one. Finally a nonempty triangle has
`x^alpha<=a<=4Y` and `Y<=a<=x^beta`. Hence
`Y>=x^alpha/4` and `log Y=O(log x)`, so (10) is
`O(x^(-alpha+epsilon))`. This proves (17). QED.

For an explicit budget, take `J=K=1`, `delta=1/4` and one prime
band `[x^(1/80000),x^(1/40000)]`, retaining the lower bound for V
in (16). Then

$$
 (7J+19)\beta-\delta/100=-\frac{37}{20000},
 \qquad
 T_{\rm tri}^{\rm arith}
       \ll x^{-1/80000+\epsilon}+x^{-37/20000}.
 \tag{19}
$$

This is a concrete small polynomial-prime budget for this fixed-depth
class. It establishes neither a growing-depth Fock expansion nor a
bound for the remaining path classes. It does not certify the HLC
paper's full proof or create a new zero-free region.

## 6. Verification and the next unresolved step

`check_closed_triangle_weight.py` independently checks the ordered
and unordered symmetrization factors, the original root-orbit factor,
the shared-list symmetric sums, once-only active-prime line weights,
closed-path multiplicity integrals and the exact polynomial budget.
It uses explicit requirements that remain enabled under `python -O`.
The companion bridge checker independently exercises the integer
candidate count and weighted gcd estimate.

The positive outcome is a paid class of actual raw closed paths with
the source's original weights. To use it in the full even moment one
must still decompose the complete path expansion, pay changing-shared-
list triangles and short backtracks with their genuine weights, and
retain the signed comparison kernels and structured endpoints. An
arbitrary surrounding history cannot be attached to the root average
without controlling its induced weight and conditioning. The
source-dependent discrete transfer in Section 5 only handles this
fixed-depth class; it does not supply those additional estimates.
