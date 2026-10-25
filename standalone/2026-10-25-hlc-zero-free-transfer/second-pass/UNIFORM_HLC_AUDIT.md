# Growing-band audit and a quantitative HLC consequence

Status: **proposed source-dependent theorem, requiring independent review
of this uniform extension.** The finite projection in `TWO_SIGN_HLC.md`
does not depend on this note. The argument imports the arithmetic
root-counting lemma, determinant operator identities, clean-edge estimate,
and analytic character estimates from Lü–Wang–Wu, arXiv:2610.20242v1. It
does not independently certify the entire preprint.

The objective is a logarithmic rate for the source's fixed shift, not a
power of x. Even an accepted theorem here would not improve the
repository's zero-free half-plane.

## 1. Statement and a uniform choice of bands

Write L=log x, fix rho=1/2, and put

\[
 N=\lfloor (\log L)/100\rfloor,\qquad
 A_i=L^{11/100}16^{i-1},\qquad
 \mathcal P_i=(e^{A_i},e^{2A_i}]\cap\mathbb P
 \quad(1\le i\le N).                         \tag{U1}
\]

These bands are disjoint and have the source form with
\(a_i=\log A_i/\log L\), where

\[
 0.11\le a_i\le0.11+(\log16)/100<0.14<0.2.  \tag{U2}
\]

Uniformly,

\[
 A_1=L^{0.11},\quad A_N\le L^{0.14},\quad
 \sum_{j<i}A_j\le A_i/15,\quad
 \sum_{i=1}^N A_i\le(16/15)A_N.             \tag{U3}
\]

Every selected subset retains these bounds after reindexing. Let W_S be
the source mark (2.13) using exactly the bands in S.

**Uniform marked estimate.** For each fixed A>0 there are fixed k_0 and
x_0 such that, uniformly in x>=x_0 and S with k_0<=|S|<=N,

\[
 \left|\sum_{x<p\le2x}(\log p)\mu(p+2)W_S(p+2)\right|
 \ll_A xL^{-A}.                             \tag{U4}
\]

The proposed proof of this extension is the audit below. Combining (U4),
the uniform moment comparison in Section 5, and the exact projection
would give the conservative consequence

\[
 \boxed{\sum_{p\le x}(\log p)\mu(p+2)
            \ll x(\log x)^{-1/1000}.}        \tag{U5}
\]

Partial summation and the prime-power error then give

\[
 \sum_{p\le x}\mu(p+2)\ll x(\log x)^{-1-1/1000},\qquad
 \sum_{n\le x}\Lambda(n)\mu(n+2)\ll x(\log x)^{-1/1000}.
 \tag{U6}
\]

These claims remain source-dependent, and (U4) is not licensed merely by
the published fixed-parameter statement. The exponent is not optimized.

## 2. Fixed parameters and allowed growth

Here K=|S|<=N. Keep the source choices

\[
 J=\lfloor L^{0.01}\rfloor,\quad
 R=\lceil L^{1/2}/2\rceil,\quad Z=\exp(L^{0.24}).
\]

All requested logarithmic precisions, the major-arc parameter A_0, the
coefficient-size exponent, Type I truncation constant, minimum k_0, and
length and height exponents remain fixed. They may be chosen large in
the order given below. The eventually necessary x_0 is not claimed to
be practical.

For a fixed local constant C,

\[
 e^{CK}\le L^{C/100}.                       \tag{U7}
\]

This is a fixed logarithmic loss. The argument does not absorb
exp(C K log K) into a fixed logarithmic loss. Such an unaccounted factor
in a one-edge norm would invalidate that use of (U7).

## 3. Uniformity of the determinant replacement

### 3.1 Good-state separation

The source uses # {DZ}=exp(o(L^{a_i*})) for fixed gaps. A dense moving
grid does not justify that assertion. Our explicit spacing instead gives

\[
 \log\#\{DZ\}\le K\log(J+1)+2\sum_{i<i_*}A_i
 \le O((\log L)^2)+(2/15)A_{i_*}.            \tag{U8}
\]

For each pair of distinct values, the failing-ratio set has measure at
most 200 exp(-A_i*). Squaring the count in (U8) bounds the mean
exceptional weight by exp(-(11/15-o(1))A_i*). Markov's inequality with
the source's allowed exceptional weight exp(-A_i*/4) bounds the bad
ratio measure by exp(-(29/60-o(1))A_i*). The union over at most 2^K
subsets is still O(exp(-c L^.11)). The first good-state test has measure
at most 2(J+1)^K Y^-1/2, also of this size, since log Y>=L^.11+O(1).
This replaces the fixed-gap limit in source (4.15)-(4.16).

### 3.2 Root averaging and modulus budgets

The shared-list product obeys

\[
 \log(d_0Y)\ll(J+1)\sum_{i\in S}A_i\ll L^{0.15}. \tag{U9}
\]

The explicit path count preceding source (4.29) is bounded by

\[
 R\log(Rd_0Y)
 +O\left(R(J+1)\sum_{i\in S}A_i
       +KR(J+1)\log(J+1)\right)\ll L^{0.66}. \tag{U10}
\]

This includes ordered lists and permutations. Their symmetrizations are
averages of mass one; there is no additional K! from permuting band
labels. Keep the source Bonferroni order B=ceil(L^.76). The total mean
deficit of unused-prime damping is O(KR), so the tail is

\[
 (CKR)^B/B!\le(eCKR/B)^B
                \le\exp(-cL^{0.76}\log L),  \tag{U11}
\]

which absorbs (U10). Every retained root modulus satisfies

\[
 \log S\ll R(J+1)\sum_i A_i+B A_N\ll L^{0.90}. \tag{U12}
\]

Appendix A's arithmetic root error is polynomial in the modulus and has
a fixed power saving in the lengths. Since S=exp(O(L^.90))=x^{o(1)},
that saving survives the sum over retained terms and residue choices.
Boundary values and derivatives in source (4.30)-(4.32) are likewise
exp(o(L)), by (U8)-(U12). The source's cube partition retains a fixed
power saving, which is smaller than L^{-2AR} for every fixed A. This
also proves the one-edge replacement, including endpoint failure of
goodness; it does not omit the bad-state removal step.

### 3.3 Local operator constants: the crucial dependence audit

In the source Fock construction choose theta=9/10 and v_0=24.
Since sqrt(rho)<3/4, we have
sqrt(rho)/theta^2+1/(theta v_0)<25/27+5/108=35/36<1,
including the two endpoint values q_j=sqrt(rho), not just the internal
value q_j=rho.
For large x, uniformly in all bands,
1/2<=V_i<=1, s_i<=2, and Delta<=C exp(-L^.11). The explicit weighted
row and column formulas on source page 28 give

\[
 \|G_j\|\le e^{64K}.                        \tag{U13}
\]

The number 64 bounds the displayed exponential factor per group; the
remaining factors in those formulas are at most one.

The following uniform form of the edge bounds is the critical new
bookkeeping assertion. With an absolute C_1 independent of A_0,K,x,

\[
\begin{split}
 \|E_j\|_{\rm abs}&\le C(A_0)e^{C_1K}L^{2K+3A_0+2},\\
 \|E_j^{\rm clean}\|&\le C(A_0)e^{C_1K}
                       (L^{0.2-A_0}+Y^{-0.1}\log Y),\\
 \|E_j^{\rm dirty,raw}\|&\le C e^{C_1K}
       [L(J+1)^{-K/2}+L^K e^{-cL^{0.11}}],\\
 \|E_j^{\rm dirty,comp}\|&\le
 C(A_0)e^{C_1K}L^{2K+3A_0+2}
                    (e^{-L^{0.11}}+Y^{-0.1})^{1/2}.
\end{split}                                 \tag{U14}
\]

The dependence check is as follows. The lattice and determinant
estimates have dimension two, independent of K. A selected band
contributes one fixed reciprocal-mass bound, bounded damping factors,
and one of the four append/remove choices. Their product and the sum
over these choices cost C^K. In the raw dirty term, the unique omitted
list tuple has mass (J+1)^-K, using (U8) and source (4.47)-(4.48).
Repeated eligible memory coordinates cost at most
sup_{h>=1} h theta^{h-1}<infinity in each band; the Schur square root
gives (J+1)^(-K/2). The opposite-direction count of at most L^2 memory
coordinates per band produces exactly L^{2K}. The comparison term's
L^{3A_0} is the source major-arc measure. Smooth-cutoff derivatives and
the two-dimensional Fourier estimate occur once, producing C(A_0),
not C(A_0)^K. These account for the constants in source (4.41), (4.46),
(4.48), and (4.50); no permutations of band labels are summed.

For the clean-edge measure conversion this is especially explicit.
Source page 29 defines m(a)=product_i nu_i(p_i). The inequalities
V_i>=1/2 and (p+1)b'_p>=p/2 give nu_i(p)<=4/p, so m(a)<=4^K/a.
On the dyadic support a is comparable to Y; each endpoint multiplier
sqrt(Y m(a)) is at most a fixed constant times 2^K. Every other
endpoint restriction is a contraction. Thus the two endpoint factors
in (4.45) cost at most C 4^K; the determinant Fourier operator itself
has no band index. This verifies the clean component's C^K dependence
without appealing to an unspecified O_K constant.

For fixed E_0 choose fixed G>E_0+10, then fixed
A_0>G+C_1/100+4, then fixed k_0>200(G+C_1/100+4). Equations (U7),
(U14), and J+1>=L^.01 give, after enlarging x_0 once,

\[
 \|E_j\|\le L^{-G}\qquad(k_0\le K\le N).    \tag{U15}
\]

Terms with L^{2K} and exponential small-prime factors are negligible:
K log L=O((log L)^2)=o(L^.11). A_0 remains fixed, so the analytic
character estimate is not silently extended to a growing conductor
exponent.

### 3.4 Global distinctness and a growing absolute edge exponent

At most 2KR memory coordinates are appended directly by edges. The
unused-prime factor is exp(O(KR)), and (U10) bounds path choices. Thus
the memory tail is at most

\[
 2^{-L^2+2KR}\exp(O(L^{0.66}+KR\log R))\ll L^{-2AR}. \tag{U16}
\]

The source index set has |B|<<KRL^2. Prescribing one new prime costs
at most C^K Delta. The absolute row exponent can be taken as
C_*(K)=2K+3A_0+C_1/100+O(1)=O(K+1). Choose the rank cutoff

\[
 r_0=\lceil C_2(K+A_0+G+1)R\log L/L^{0.11}\rceil,    \tag{U17}
\]

where C_2 is sufficiently large and fixed. Because
log(C^K|B|^2)=O(log L), the high-rank calculation (4.57)-(4.60)
gives O(L^{-2R(E_0+4)}). Also r_0/R tends to zero uniformly.

For r<r_0 at most 2r edge operators are affected by equalities. The
Fourier construction (4.61) is finite algebra with modulus-one
multipliers and mass-one symmetrizations. By (U13), the product of
memory operator norms is at most

\[
 e^{64K(2R+1)}\le L^{1.3R}
\]

for large x. The altered edges and their index choices cost, relative
to the main exponent R log L,

\[
 O((K+1)^2\log L/L^{0.11})=o(1).            \tag{U18}
\]

Consequently (U15), with G>E_0+10, gives the same required saving for
the low-rank sum. This explicitly replaces the source's fixed-C_*
argument, rather than assuming it survives a growing K.

### 3.5 Pairings and removal of restrictions

The endpoint norm bound (4.63) is independent of K,J because the
harmonic list weights are normalized. The dimension factor is

\[
 (d_0Y)^{1/(2R)}=\exp(O(L^{-0.35}))=1+o(1).  \tag{U19}
\]

There are O(L^.15) dyadic auxiliary-product intervals, bounded by O(L).
The one-edge replacement and (U8) give the bad-state removal (4.70)
uniformly. Harmonic-draw collisions have probability at most
C K(J+1)^2 exp(-L^.11). Absolute raw and major-arc pair sums in
(4.74)-(4.76) cost at most exp(CK) times their fixed logarithmic
powers: the divisor-square bound is independent of K, and product
pairs are counted by their normalized harmonic masses. These losses
are absorbed by the collision error. Automatic primitivity remains
valid since log Y=O(L^.14)=o(log Z).

These bounds give the proposed uniform extension of Proposition 4.2.

## 4. Analytic parts of the marked estimate

### 4.1 Type I without hidden coefficient growth

In source Section 3, use divisor truncation order
R_1=ceil(C log L), with fixed C sufficiently large. For the single-band
function n rho^{n-1}, the coefficient of binom(n,l) is
l(rho-1)^{l-1}. At rho=1/2 its magnitude is at most one. Hence the
maximum coefficient of a normalized K-band truncated product is C^K,
not the loose R_1^{2K} bound used in Proposition 2.3. Its absolute
harmonic coefficient sum is also at most C^K.

Each retained mark divisor has log d<<R_1 sum_i A_i<<L^.14 log L.
The rough-sieve divisor has log r<<L^.24 log L. Both are x^{o(1)}.
Truncation errors are C^K times the source factorial tails. The rough
sieve tail is L^{-C log(C/e)}; choosing fixed C large absorbs (U7).
The mark tail K C^K/R_1! is smaller than every fixed logarithmic power.

The weighted Möbius Bombieri–Vinogradov estimate sees moduli
qr<=x^{2/5+o(1)} and lengths at least x^{19/20}, exactly as in the
source. Remaining divisor weights cost C^K, absorbed by a larger
fixed logarithmic precision. The Euler products for the large smooth
factor are 1+o(1) uniformly: omega(d)<<K log L, while every prime in
d exceeds exp(L^.11). This gives the Type I estimate uniformly.

### 4.2 Major arcs and the fixed character hypothesis

The character moduli are at most 2L^{A_0}, with A_0 fixed in Section
3.3. Source Proposition 2.2 is applied with fixed conductor exponent
B=A_0+1 and a fixed polynomial height exponent. Neither depends on K.
Increasing its requested fixed logarithmic precision is legitimate.

The product polynomial in source (5.15) has normalized harmonic mass
one, exactly as in (5.1). Its absolute value is bounded independently
of K. Extracting one band leaves a product of factors of magnitude at
most one. The proof of the large-value lemma for the extracted band
uses only the endpoint restrictions 0.1<a<0.2; (U2) stays inside them.
The Mellin cutoff depends on the single product divided by Y, so its
derivative losses occur once, not once per band. Arc counts and
character expansions cost the displayed fixed powers
L^{2A_0}, L^{6A_0}, and L^{A_0}.

The energy calculation (5.14)-(5.16) therefore supplies every requested
fixed logarithmic saving uniformly in K. This uses no zero-free
half-plane assumption and no character estimate at a growing
logarithmic conductor exponent.

### 4.3 Return from the quadratic estimate

The Type II coefficients remain mu(m) R_Z(m) m^{iv} and
c_V(n) R_Z(n) n^{iv}, of the original fixed logarithmic sizes. The
initial smooth transition error has an extra sup norm
||W_S||<=2^K, which is a fixed logarithmic loss. Increase its fixed
smoothing exponent accordingly. The Mellin cutoff height remains a
fixed power of L and is covered by Proposition 2.2. Dyadic
decompositions cost fixed powers of L; the product scales have
logarithmic range O(L^.14).

The source Cauchy step |T_Y|^2<<(X/Y)Q_Y, together with the uniform
replacement and major-arc estimates, gives any requested logarithmic
saving for the marked Type II sum. The added noncoprime terms in
(4.3) cost at most 2^K X L exp(-L^.11), which is negligible. The
rough-prime and prime-power errors are at most
2^K(exp(L^.24)+x^{1/2}L^2), also negligible. This completes the
proposed proof of (U4).

## 5. Uniform CRT comparison for the required moments

Use the exact finite CRT normalizers and U_i in `TWO_SIGN_HLC.md`,
Section 2, for (U1). For every fixed B>0, uniformly in e_i in {0,1,2},

\[
 \frac1x\sum_{x<p\le2x}(\log p)\prod_iU_i(p+2)^{e_i}
 =\mathbb E_{\rm CRT}\prod_iU_i^{e_i}+O_B(L^{-B}).
 \tag{U20}
\]

The number of active factors may be N. Here is a direct proof, without
an interchange of a fixed-dimensional distribution limit.

Use the binomial expansions of n rho^{n-1} and n^2 rho^{2n-2}.
For the latter, with z=rho^2, the coefficient of binom(n,l) is

\[
 \rho^2\ell(\ell-1)(z-1)^{\ell-2}
       +\ell(z-1)^{\ell-1}.                 \tag{U21}
\]

The first term is zero for l<2. Both sequences of coefficients are
bounded by an absolute constant at rho=1/2. The normalizers F_i'(1/2)
are uniformly bounded above and below by positive constants by
Mertens' theorem, since min A_i tends to infinity. Thus every product
coefficient is at most C^N=L^{O(1)}.

Truncate each expansion at R_2=ceil(C_B log L), with fixed C_B.
The integer-average and CRT tails, including the prime logarithmic
weight, are at most L N C^N/R_2!, smaller than every fixed negative
power of L. To see this, expand absolute values and count multiples:
for coprime band divisors, # {n<=3x:d|n}<=3x/d. For CRT replace 1/d
by 1/phi(d). The individual reciprocal sums remain below one and
their exponential series contribute only C^N. At least one truncated
index exceeds R_2, producing the stated factorial tail.

Retained divisors satisfy log d<<R_2 sum_i A_i<<L^.14 log L, hence
d=x^{o(1)}. The class -2 mod d is reduced. Bombieri–Vinogradov at a
larger fixed precision absorbs C^N and proves (U20), including the
all-zero exponent vector. The coefficient bound is uniform over all
3^N exponent vectors; no further union factor is needed for a maximum.

Uniform reciprocal prime estimates also give

\[
 R_i=r(1/2)+o(1),\qquad
 r(1/2)=2^{1/4}\left(\frac14+\frac1{\log2}\right)<3. \tag{U22}
\]

Only q_i=1/R_i>=1/3 is needed. For clarity, the o(1) is uniform:
sum_{p in P_i}1/p=log2+O(1/A_1), and sum_{p in P_i}1/p^2 tends to
zero uniformly. Expanding the generating-product logarithm and its
first two derivatives near rho and rho^2 gives (U22).

## 6. Quantitative unmarking

Fix k=k_0 from (U4) with enough precision to absorb the exact
normalizers in equation (7) of `TWO_SIGN_HLC.md`. They cost C^N,
so a larger fixed precision suffices. In the prime probability measure
of that note we get

\[
 \max_{|S|\ge k}\left|
   \int\mu(p+2)U_S(p+2)\,d\nu_x(p)\right|\ll L^{-2}. \tag{U23}
\]

The projection coefficient mass is

\[
 A_{N,k}\ll_k N^{k-1}2^N=L^{(\log2)/100+o(1)}. \tag{U24}
\]

Expanding (1-P_{N,k})^2 costs at most (1+A_{N,k})^2 in coefficient
mass. Equation (U20) at fixed B=10 therefore gives an O(L^-9)
discrepancy for large x.

By (U22), the Bernoulli sum of Theorem 1 stochastically dominates
Bin(N,1/3). Thus

\[
 \Pr(\sum B_i<k)
 \le\sum_{j=0}^{k-1}\binom Nj3^{-j}(2/3)^{N-j}
 \ll_k N^{k-1}(2/3)^N.                      \tag{U25}
\]

Its square root is

\[
 L^{-\log(3/2)/200+o(1)}=O(L^{-1/1000}),      \tag{U26}
\]

since log(3/2)/200>1/1000. The exact transfer inequality (9) of
`TWO_SIGN_HLC.md`, with (U23)-(U26), proves the dyadic form of (U5).
Summing dyadic intervals proves (U5). Partial summation and the total
O(x^{1/2}log^2x) contribution from higher prime powers prove (U6).

## 7. Review boundary and failure conditions

The new assertions requiring review are (U4) and (U20), particularly
the one-edge constant bookkeeping in (U14). The finite projection and
its exact checker remain valid if this analytic audit fails.

This argument would fail if the determinant proof needed an extra
exp(c K log K) factor in a one-edge norm, an extra A_0-dependent
derivative loss once per band, or another unaccounted fixed-gap
hypothesis. It also depends on the validity of the imported source's
root replacement, Fock identities, and character–Mellin estimate. The
audit specifies the places needing review; it does not replace an
independent certification of the full source.

If only exp(O(K log K)) local constants can be justified, one can
instead take N=floor(c log L/loglog L), leaving the geometric spacing
and all other budgets intact. Then those constants cost a fixed
power of L, and the same projection gives the weaker explicit decay
exp(-c' log L/loglog L). This is an available fallback, not a reason
to overlook an unbounded constant dependence.

Even if accepted, (U5)-(U6) concern a fixed-shift correlation with a
logarithmic saving. They do not prove a power saving for the full
shift average or the native inverse moment and do not change B_flat.

## Appendix: the source-anticipated Liouville adapter

The source explicitly anticipates Liouville counterparts on page 2.
This appendix is an explicit adapter, **not a claim of a new unanticipated
Liouville theorem**. It also records the coprimality issue in the damping
factor, which does not disappear merely because lambda is completely
multiplicative.

First, the Möbius Bombieri–Vinogradov statement (3.1) implies the same
statement for lambda. Use

\[
 \lambda(n)=\sum_{d^2\mid n}\mu(n/d^2).
\]

For a reduced progression a mod q only d coprime to q contribute. Fix
any requested A>0 and put D=(log x)^C with fixed C>A+3. For d<=D,
apply Möbius Bombieri–Vinogradov at length Y=x/d^2. If
Q<=sqrt(x)(log x)^(-B) and B is a sufficiently large fixed constant,
then Q<=sqrt(Y)(log Y)^(-B_mu) for every such d, where B_mu is the
constant needed for the chosen Möbius precision. Summing the resulting
errors costs sum_d x/d^2, hence O(x(log x)^(-A)). Maxima over upper
endpoints are included in (3.1).

For d>D, the elementary progression count bounds the total absolute
error, including all reduced-residue maxima, by

\[
 \sum_{q\le Q}\sum_{D<d\le\sqrt x}
    \left(\frac{x}{q d^2}+1\right)
 \ll \frac{x\log x}{D}+Q\sqrt x
 \ll x(\log x)^{-A}
\]

after increasing B if needed. This proves the stated Liouville version.

In the Type I argument, after expanding the mark and rough sieve,
write qrj+2=dv. The mark divisor d is odd and coprime to qr. Complete
multiplicativity gives lambda(dv)=lambda(d)lambda(v), and v runs over
a reduced residue class modulo 2qr. Since d=x^{o(1)}, the lengths
x/d and moduli qr<=x^{2/5+o(1)} satisfy the preceding Liouville BV
range. The source's divisor-weighted Cauchy estimate is unchanged.
Unlike the Möbius case, no additional d-smooth factor is needed to
repair lambda(dv).

For Type II, first discard selected tuples with (a,h)>1 in mn+2=ah.
Such a tuple has some selected p with p^2 dividing mn+2. Since m is
Z-sifted and p<Z, p is coprime to m; since the n-length is a fixed
power of x, it greatly exceeds p^2. The total discarded weight is
therefore at most C^K X L^C sum_{p in union bands} p^{-2}, negligible
at every fixed logarithmic precision. On the retained tuples both
lambda(ah)=(-1)^K lambda(h) and omega(ah)=K+omega(h) hold.
Removing the coprimality restriction once more has the same error.
The source Cauchy step uses only |lambda(h)rho^{omega(h)}|<=1, and
its surviving m-coefficient is still the original Möbius coefficient
from Vaughan's identity. The determinant and major-arc estimates
therefore apply with the identical scope.

The mark projection and prime moment comparison use only |f|<=1, so
the same quantitative consequence follows for lambda in place of mu
if the uniform audit is accepted. This additional coefficient adapter
does not address the missing zero-free transfer.
