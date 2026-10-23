# A short squarefree-label vector bound for Möbius residue pairings

23 October 2026. Proposed analytic theorem; independent review pending.
The statement concerns squarefree labels, not every sixth-power-free
label, and retains the actual pure Möbius coefficient. It supplies a
larger controlled residual subspace, not a bound on its complement.

Use the notation, fixed sections, actual inverse input, and completed
functional equation of `LABEL_UNIFORM_MOBIUS_RESIDUES.md`, SHA256
`12c765c1fdcccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d`.
We additionally import de Faveri, Theorem 1.1,
<https://arxiv.org/html/2610.04045v1>, in the sixth-power-free orientation:

\[
 \Delta_6(K,L)\ll(KL)^\epsilon
 \{K+L+K^{5/6}L^{1/3}+K^{1/3}L^{5/6}\}.             \tag{V1}
\]

Both index sets may be restricted to sixth-power-free ideals; a
squarefree row subset is allowed. No claim about a sharper generic
squarefree norm is used. All characters have their literal zeros.

The proposed result, for any subset of distinct good squarefree labels
R with NR<=K, is

\[
 \boxed{\quad
 \sum_R |P_R^{\rm full}(D)|^2
 \ll(DKNQ)^\epsilon
 \{D^{2/3}+D^{-1/3}K^2+D^{1/2}K^{7/6}\},\quad}       \tag{V2}
\]

and consequently

\[
 \boxed{\quad
 \sum_R\bigl(|P_R^{\rm full}(D)|^2+|P_R^{\rm prim}(D)|^2\bigr)
 \ll(DKNQ)^\epsilon D^{2/3},\qquad 1\le K\le D^{1/7}.
 \quad}                                                \tag{V3}
\]

All epsilon losses can be assigned internally; strict power margins
are required when comparing V3 with a separate detector error.

## 1. The finite full-modulus vector, with both shared factors retained

For the scalar finite sum S_R(U) of L4, we first prove

\[
 \sum_{R\ {\rm sf},\,NR\le K}|S_R(U)|^2
 \ll(UDKNQ)^\epsilon
 \min\{K,1+K^2/U\}\{U+U^{1/6}D^{5/6}\}.             \tag{V4}
\]

The K bound follows by summing the label-uniform scalar L5. The other
bound uses the following exact decomposition of each nonzero local term:

\[
 R=f g R_0,\qquad n=e g m,\qquad
 c=e^2 f^2 g^3 c_0.                                   \tag{V5}
\]

Here e,f,g are pairwise coprime squarefree factors: e consists of primes
in n and c but not R, f of primes in R and c but not n, and g of primes
in all three. The residual c0 is squarefree and prime to nR. The
squarefree m may share primes with R0; that case is not excluded. The
factors m and R0 are each coprime to efg. There is no unstated condition
(m,R0)=1. Primes common to n and R but absent from c simply occur in
both m and R0.

The full local exponents are exactly 2,2,3 on e,f,g. The raw Gauss
coefficient g_6(nR,c)/Nc and the n-normalization leave scalar modulus

\[
                     e^{-1}f^{-1/2}g^{-1}c_0^{-1/2}.  \tag{V6}
\]

Before any absolute value, local Fourier scaling supplies the free
characters

\[
 \overline{\chi_m(c_0e^2f^2g^3)}\,
 \overline{\chi_{R_0}(c_0e^2f^2g^3)},                 \tag{V7}
\]

after fixed reciprocity-sector partition. Remaining CRT roots are
independent of m and R0. They may depend on e,f,g,c0 and are bounded
column multipliers. The second character's f^2g^3 factor is a common
row phase in R0 and has modulus one on the retained R0 rows. Fixed
ray phases in m and R0 are resolved by a finite partition.

Fix f,g and a dyad e~E. Put r=e^2c0, which is sixth-power-free and
determines e and c0 uniquely. Its length is

\[
                  L=U/(f^2g^3).                       \tag{V8}
\]

The free inverse index in m is r f^2g^3 and has norm O(U). Its zero
mask already enforces (m,efg)=1, so the only separately fixed puncture
needed in the inverse input is Q. Smooth separation of the norm
coordinates e/E and m/(D/(gE)) gives a common Möbius inverse polynomial
of length D/(gE), with allowed norm twists. Its row coefficients retain
the e-coordinate. This is why it is legitimate to aggregate e into r
before applying V1; applying Minkowski separately to every e would lose
the useful square norm.

After V1 on rows R0<=K/(fg), the fixed f,g,E contribution has squared
norm at most

\[
 {fg\over U}\Delta_6(K/(fg),U/(f^2g^3))
                  I(CU,D/(gE);Q),                    \tag{V9}
\]

apart from subpowers and common smooth seminorms. Indeed V6 is
f^(-1/2)g^(-1)r^(-1/2), so its squared coefficient mass is bounded by
f^(-1)g^(-2)L^(-1) times the inverse row norm. The map
r -> r f^2g^3 is injective. Any additional support restrictions may be
discarded from this nonnegative row norm. No arithmetic multiplier in
the free m coefficient is discarded.

For a fixed R there are only divisor-many choices of f,g. Cauchy on
these choices costs K^epsilon, after which f,g may be summed positively.
The e-dyads and the smooth norm separations cost logarithms/subpowers.
Since I(U,D/(gE))<=I(U,D) at the displayed upper-bound level, expand
the scalar factor in V9. Its four terms are

\[
 {1\over fg^2},\qquad {K\over U},\qquad
 K^{5/6}U^{-2/3}f^{-1/2}g^{-5/6},\qquad
 K^{1/3}U^{-1/6}f^{-1}g^{-11/6}.                      \tag{V10}
\]

The sums over fg<=K are respectively bounded by a subpower times

\[
 1,\qquad K^2/U,\qquad K^{4/3}U^{-2/3},\qquad
 K^{1/3}U^{-1/6}.                                    \tag{V11}
\]

For example sum_f<=K/g f^(-1/2)<<sqrt(K/g), and the remaining
g-sum has exponent 4/3. The other two weighted sums converge or cost
one logarithm. The last two expressions are (K^2/U)^(2/3) and
(K^2/U)^(1/6), hence their sum is O(1+K^2/U). This proves V4.

## 2. Completion tails in the original vector

The completed original finite vector is

\[
                 B_R(Y)=\sum_b b^{-1}S_R^{\rm phys}(Y/b^6). \tag{V12}
\]

Its square norm is bounded by

\[
 \sum_R|B_R(Y)|^2\ll(YDKNQ)^\epsilon
   \{Y+Y^{1/6}D^{5/6}+K^2+D^{5/6}K^{7/6}\}.          \tag{V13}
\]

Here are explicit summation bounds. Write L=Y/b^6 in V4 and use
Minkowski in b, retaining the support cutoff at L comparable to one.
The volume part contributes amplitude O(sqrt(Y)+K), up to logarithms.
For the nonvolume part split at b=(Y/K^2)^(1/6) and
b=(Y/K)^(1/6), omitting empty ranges. On the first range use the 1
term of 1+K^2/L, giving amplitude D^(5/12)Y^(1/12) after summing
b^(-3/2). On the middle range use K^2/L; its b-weight is b^(3/2),
so its endpoint contribution is at most D^(5/12)K^(7/12). On the
last range use the K bound; the b^(-3/2) tail gives the same quantity.
If Y<K, the whole sum may use K and gives
sqrt(K)D^(5/12)Y^(1/12)<=D^(5/12)K^(7/12).
The volume bounds follow in the same ranges from b^(-4), b^(-1),
and b^(-4), respectively. Thus all completion ideals are retained.

## 3. Isolate the entire full residue vector

At reference Y=D, the label-uniform reflected scalar L13 gives directly

\[
 \sum_{NR\le K}|F_R(D)|^2
 \ll(DKNQ)^\epsilon\{K^2+D^{5/6}K^{7/6}\}.           \tag{V14}
\]

This is just the sum of I(NR,D) over squarefree R; no unjustified
vector reflection is needed. In particular the possibly decreasing
term K^2/L in V4 is not inserted into a small-argument kernel estimate.

Choose the fixed nonnegative w used in the scalar residue proof.
The exact completed identity is
B_R(D)-F_R(D)=zeta_S(2) w_hat(2/3)D^(1/6)P_R^full(D).
Combining V13 at Y=D with V14 proves V2. For K<=D^(1/7), both
D^(-1/3)K^2 and D^(1/2)K^(7/6) are O(D^(2/3)).

## 4. Primitive density without losing the short-label range

Use the exact residue density L16--L17. Since R is squarefree, the
divisor expansion has (d,R)=1; the new label dR is therefore squarefree.
For each fixed d the new coefficient length is A=D/d, its puncture is
Qd, and its outside scalar is at most d^(-3/2). The set of new labels
is a subset of those of norm at most dK. Its row-dependent fixed
factor prod_(p|R)(1+1/p)^(-1) is bounded by one.

For d<=sqrt(D), apply V2 with length D/d and label limit dK, then
Minkowski. The three resulting amplitude sums are bounded by

\[
 D^{1/3}\sum_d d^{-11/6},\quad
 D^{-1/6}K\sum_{d\le\sqrt D}d^{-1/3},\quad
 D^{1/4}K^{7/12}\sum_d d^{-7/6}.                       \tag{V15}
\]

Their squared total is
O(D^(2/3)+D^(1/3)K^2+D^(1/2)K^(7/6)), which is O(D^(2/3))
for K<=D^(1/7).

For d>sqrt(D), use the improved scalar L2 and sum the at most O(K)
original labels R. The squared term, including d^(-3), is at most

\[
 D^{2/3}K d^{-11/3}+D^{1/3}K^{4/3}d^{-3}.             \tag{V16}
\]

The two square-root tails sum to squared costs
O(D^(-1/6)K+D^(-1/6)K^(4/3)), smaller than D^(2/3) in the stated
range. All divisors d with nonempty original annuli are included;
bounded subunit endpoint annuli change constants only. This proves V3.

## 5. A genuine but partial inverse consumer

At a physical inverse row scale U, suppose the squarefree-label Gram
matrix from PR1013 is conditioned in its proved range K<=U^(1/2-delta).
Its subset inherits that property. The squared pole contribution to
the actual Gauss-vector projection is then at most

\[
                       (UDKNQ)^\epsilon U^{1/3}D^{2/3}, \tag{V17}
\]

uniformly for K<=D^(1/7). Compared with the inherited nonvolume
inverse term U^(1/6)D^(5/6), this has ratio (U/D)^(1/6).
The previous residue-vector bound retained an extra factor K.

V17 controls the pole part of that projection only. It does not supply
the matching primitive continuous vector, the orthogonal complement,
or the signed shared-kernel initial Poisson return. Those missing terms
remain necessary before inferring a smaller B_flat or RH. The new
quantitative improvement is the uniform residue-vector bound V3 and
its explicitly limited residual-subspace consumer.
