# A sharper root count with prescribed projective lines

**Status: a proved refinement of the finite-root estimate.** The
elementary version uses the fourth-moment Kloosterman bound proved in
the supplied HLC paper, whose short proof is repeated here. A separate
classical version imports the stronger Weil--Salié bound explicitly.
Both retain the frequency gcd inside the Fourier sum and the modulus
gcd inside its arithmetic progression.

This is a root-counting theorem. It does not bound the complete HLC
path operator, its centered comparison kernel, the native inverse
polynomial, or zeros of a zeta or L-function. Its fixed-depth triangle
consequence has the restricted scope stated in Section 6.

The source comparison is Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242), Appendix A,
equations (A.1)--(A.5), pp. 48--51. The PDF used here has SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.

## 1. Statement and the two exponential-sum inputs

Let A,B>=2 be real, S a squarefree positive integer, and

$$
 I_1,I_2\subset[1,16],\qquad I_3\subset[0,1]
$$

be intervals. For coprime positive u,v define their unique normalized
completion by

$$
 g(u,v)=\begin{pmatrix}u&c\\v&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z),
 \qquad 0\le c<u,\qquad ud-vc=1.                         \tag{1}
$$

Put H=min(A,B). We use an exponent kappa satisfying the estimate

$$
 |K_m(h,k)|\ll_\eta m^{\kappa+\eta}(h,k,m)^{1-\kappa},
 \quad
 K_m(h,k)=\sum_{y\bmod m}^{*}e((hy+ky^{-1})/m),
 \quad\eta>0.                                           \tag{2}
$$

There are two fully specified versions:

* **Elementary input:** kappa=3/4. The source's argument proving
  (2) is reproduced below. No Weil bound is required for this version.
* **Classical input:** kappa=1/2, using
  $|K_m(h,k)|\le\tau(m)m^{1/2}(h,k,m)^{1/2}$.
  A primary-source statement for all integer frequencies and positive
  moduli is Blomer--Man, *Bounds for Kloosterman sums on GL(n)*,
  Math. Ann. 390 (2024), 1171--1200,
  [equation (1.2)](https://link.springer.com/article/10.1007/s00208-023-02777-6),
  DOI 10.1007/s00208-023-02777-6. The divisor bound gives (2).
  This classical estimate is an imported theorem, not proved here.

**Theorem 1 (matrix class).** For either stated input, uniformly in S,
the intervals and $g_0\in\mathrm{SL}_2(\mathbb Z/S\mathbb Z)$,
and for every epsilon>0,

$$
 \begin{split}
 &\frac1{AB}\#\{u,v>0:(u,v)=1,\ u/A\in I_1,\ v/B\in I_2,
                    \ c/u\in I_3,\ g(u,v)\equiv g_0\pmod S\}\\
 &\quad=
 \frac{|I_1||I_2||I_3|}
       {\zeta(2)|\mathrm{SL}_2(\mathbb Z/S\mathbb Z)|}
       +O_\epsilon(H^{\kappa-1+\epsilon}).
 \end{split}                                               \tag{3}
$$

This is an **absolute** discrepancy, independent of S, not an error
relative to the small matrix-class density. It may exceed the main
term when S is large.

For odd u,v put

$$
 g'=\begin{pmatrix}u&-2c\\(u-v)/2&d-c\end{pmatrix},
 \qquad \ell_p(g')=\ker(u,-2c)\in\mathbb P^1(\mathbb F_p).
 \tag{4}
$$

**Corollary 2 (prescribed lines).** For odd squarefree S and one
prescribed line $\ell_p$ for every $p\mid S$, the normalized
count with the same intervals, $2\nmid uv$, and
$\ell_p(g')=\ell_p$ is

$$
 \boxed{
 \frac{|I_1||I_2||I_3|}{3\zeta(2)\prod_{p\mid S}(p+1)}
            +O_\epsilon(S^2H^{\kappa-1+\epsilon}).}
 \tag{5}
$$

Thus the elementary version has error $S^2H^{-1/4+\epsilon}$;
the classical version has $S^2H^{-1/2+\epsilon}$. Both keep the
source's exact parity normalization and once-only prime-line factors.

### The elementary input is self-contained

Orthogonality gives
$\sum_{h,k\bmod m}|K_m(h,k)|^4=m^2T_m$, where $T_m$ counts
unit quadruples with equal sums and equal inverse sums. Eliminating
the fourth unit gives

$$
                m\mid(y_1+y_2)(z_1-y_1)(z_1-y_2).
$$

The linear map to these three factors has kernel of size at most two.
Every triple with product divisible by m is covered by an ordered
factorization $d_1d_2d_3=m$, with each $d_i$ dividing its
corresponding factor. There are $m^2$ triples for each such
factorization. Hence $T_m\le2m^2\tau_3(m)$.

For every unit s, $K_m(hs,ks^{-1})=K_m(h,k)$. This orbit has
exactly $\varphi(m/(h,k,m))$ elements: its stabilizer is the
kernel of reduction of units modulo $m/(h,k,m)$. Consequently

$$
 |K_m(h,k)|^4\le
          \frac{2m^4\tau_3(m)}{\varphi(m/(h,k,m))}.
$$

The elementary divisor estimate and
$n/\varphi(n)\ll_\eta n^\eta$ prove (2) with kappa=3/4,
after reducing the auxiliary epsilon. This proof permits even
moduli and arbitrary, including zero or noncoprime, frequencies.

## 2. The exact fixed-u congruences

First assume A<=B. Write the prescribed matrix as
$g_0=\left(\begin{smallmatrix}u_0&c_0\\v_0&d_0\end{smallmatrix}\right)$
modulo S. Here $d_0$ is a matrix entry, not the HLC dyadic scale.
Fix u with $u\equiv u_0\pmod S$. Let $\mathcal R_u$ be the
pairs modulo uS satisfying

$$
 c\equiv c_0\pmod S,\quad v\equiv v_0\pmod S,
                 \quad cv\equiv ud_0-1\pmod{uS}.          \tag{6}
$$

These conditions are exactly the matrix congruences after
$d=(1+cv)/u$ is reconstructed. They imply that c and v are
units modulo u. Set

$$
 s_1=(u,S),\quad s_2=S/s_1,\quad m=us_1,\quad C=ud_0-1,
                  \qquad\gamma s_2\equiv1\pmod m.
$$

Squarefreeness gives $(s_2,m)=1$, and both gamma and C are
units modulo m. Modulo $s_2$ the coordinates are fixed. Modulo m,
their product is C and $c\equiv c_0\pmod{s_1}$; the v
congruence modulo $s_1$ follows from the determinant of $g_0$.
CRT and an additive indicator for that c congruence express

$$
 F_u(h,k):=\sum_{(c,v)\in\mathcal R_u}e((hc+kv)/(uS))
$$

as a unit-modulus factor times a unit-modulus-weighted average of

$$
            K_m(\gamma h+ju,\gamma kC),\qquad j\bmod s_1,
                     \quad\text{with normalizer }1/s_1.
 \tag{7}
$$

For **all** integer frequencies,

$$
 (\gamma h+ju,\gamma kC,us_1)\le s_1(h,k,u).              \tag{8}
$$

Modulo u, gamma and C are units, so the gcd of the two entries
with u is $(h,k,u)$. Passing from u to $us_1$ increases it
by at most $s_1$. Apply (2) to (7), and use $s_1\le u$:

$$
 |F_u(h,k)|
 \ll_\eta u^{\kappa+\eta}s_1^{1+\eta}(h,k,u)^{1-\kappa}
 \ll_\eta s_1u^{\kappa+2\eta}(h,k,u)^{1-\kappa}.
 \tag{9}
$$

The exact zero frequency is

$$
 \#\mathcal R_u
       =u\prod_{p\mid u,\ p\nmid S}(1-1/p)\le u.          \tag{10}
$$

## 3. Bounded variation pays the entire Fourier sum

For an interval J in the circle and $0<\Delta<1/10$, expand
or contract J by $2\Delta$, allowing the full circle or empty
set, and convolve its indicator with a nonnegative fixed smooth
probability kernel of width Delta. The resulting functions satisfy

$$
 0\le f_J^-\le1_J\le f_J^+\le1,\qquad
                  \widehat f_J^\pm(0)=|J|+O(\Delta).
 \tag{11}
$$

Their total variation is at most two, independently of Delta.
For every fixed integer N>=2 and n!=0,

$$
 |\widehat f_J^\pm(n)|
       \ll_N\frac1{|n|}\min\{1,(\Delta|n|)^{-N}\}.
 \tag{12}
$$

This uses the interval Fourier coefficient and the mollifier
transform; it is not a claim about arbitrary Delta-dependent
profiles. For every positive integer d it implies

$$
 \sum_{n\ne0,\ d\mid n}|\widehat f_J^\pm(n)|
                    \ll\frac{\log(2/\Delta)}d.             \tag{13}
$$

Indeed write n=dr, sum the harmonic series through
$|r|\le1/(d\Delta)$, and then the tail with N=2. If
$d\Delta>1$ the whole sum is a tail, with the same bound.

Apply the product of two such upper or lower functions to the
two coordinates of $\mathcal R_u/(uS)$. The zero frequency
gives the expected area, with error $O(u\Delta)$. For all
other frequencies use the positive majorant

$$
 (h,k,u)^{1-\kappa}
       \le\sum_{d\mid u,\ d\mid h,\ d\mid k}d^{1-\kappa}.
 \tag{14}
$$

When both frequencies are nonzero, (13) bounds the weighted sum by

$$
 \ll\log^2(2/\Delta)\sum_{d\mid u}d^{-1-\kappa}
       \le\zeta(1+\kappa)\log^2(2/\Delta).                 \tag{15}
$$

When exactly one frequency is zero, its coefficient is at most one,
and the bound is

$$
 \ll\log(2/\Delta)\sum_{d\mid u}d^{-\kappa}
       \ll_\eta u^\eta\log(2/\Delta).                     \tag{16}
$$

The divisor bound proves the last inequality. The pair (0,0) was
already handled by (10) and is excluded from (14)--(16).
All these Fourier series converge absolutely, so no frequency cutoff
or omitted high-frequency estimate is needed.

Choose $\Delta=u^{\kappa-1}/100$, then choose the eta in
(9), (16) sufficiently small in terms of epsilon and absorb
logarithms. Uniformly in any two circle intervals,

$$
 \left|\sum_{(c,v)\in\mathcal R_u}
   1_{J_1}(c/(uS))1_{J_2}(v/(uS))
      -(\#\mathcal R_u)|J_1||J_2|\right|
                \ll_\epsilon (u,S)u^{\kappa+\epsilon}.
 \tag{17}
$$

## 4. Sum the modulus gcd inside its arithmetic progression

The condition $c/u\in I_3$, $0\le c<u$, is a circle interval
of length $|I_3|/S$ in the first coordinate of (17). Split
$BI_2$ for v into pieces of length uS. There are
$O(B/u+1)$ pieces, and their total normalized length is
$B|I_2|/(uS)$. For fixed u the main term is therefore

$$
 \frac{B|I_2||I_3|}{S^2}
               \prod_{p\mid u,\ p\nmid S}(1-1/p),          \tag{18}
$$

with error

$$
 O_\epsilon\big((B/u+1)(u,S)u^{\kappa+\epsilon}\big).
 \tag{19}
$$

On $u\equiv u_0\pmod S$, the gcd is the fixed integer
$d_*=(u_0,S)$. There are at most $15A/S+1$ terms in
$AI_1\subset[A,16A]$. If any term exists, $d_*\le16A$.
Consequently

$$
 \sum_{u\in AI_1,\ u\equiv u_0\ (S)}(u,S)
       \le15A\frac{d_*}S+d_*\le31A.                       \tag{20}
$$

For an empty progression the bound is immediate. Since A<=B and
each retained u is comparable to A, (20) sums (19) to

$$
                       O_\epsilon(AB A^{\kappa-1+\epsilon}).
 \tag{21}
$$

This is why there is no remaining modulus factor in (3).
Bounding $(u,S)$ by S before its progression is summed would
lose this improvement.

For the main term expand the product in (18) as
$\sum_{\ell\mid u,(\ell,S)=1}\mu(\ell)/\ell$.
The two congruences $\ell\mid u$ and $u\equiv u_0\pmod S$
specify one class modulo $\ell S$. Thus

$$
 \begin{split}
 &\sum_{u\in AI_1,\ u\equiv u_0\ (S)}
        \prod_{p\mid u,\ p\nmid S}(1-1/p)\\
 &\quad=\frac{A|I_1|}{S\zeta(2)}
       \prod_{p\mid S}(1-p^{-2})^{-1}+O(\log(2A)).
 \end{split}                                               \tag{22}
$$

The reciprocal-square divisor-series tail costs O(1/S). The error
in (22), multiplied by B/S^2 from (18), is absorbed by (21),
for either kappa. Since
$|\mathrm{SL}_2(\mathbb Z/S\mathbb Z)|
=S^3\prod_{p\mid S}(1-p^{-2})$, this proves (3) for A<=B.

For B<A use the normalized completion

$$
 \widetilde g=\begin{pmatrix}v&v-d\\u&u-c\end{pmatrix},
             \qquad\frac{v-d}{v}=1-\frac cu-\frac1{uv}.
 \tag{23}
$$

For u,v>=2 its second column has the required normalization.
This map is an involution on determinant-one matrices, also modulo S.
Enlarging and contracting $1-I_3$ by O(1/(AB)) sandwiches the
ratio condition after swapping A,B. This changes the unnormalized
predicted main term by O(1), absorbed by (21) with A replaced by B.
Theorem 1 follows in both orders of the scales.

## 5. Prescribed projective lines and parity

Apply Theorem 1 with modulus 2S. Exactly two matrices in
$\mathrm{SL}_2(\mathbb F_2)$ have first column $(1,1)^T$.
For an odd prime p, a prescribed kernel line of $(u,-2c)$
permits p-1 nonzero first rows; each has p determinant-one
completions. The exact number of allowed matrix classes is

$$
                   2\prod_{p\mid S}p(p-1)\le2S^2.          \tag{24}
$$

Their proportion is $\frac13\prod_{p\mid S}(p+1)^{-1}$.
Summing the matrix main terms and absolute discrepancies proves
(5). This uses no second line draw, nor any independence of
different visits of a path to a recorded line.

## 6. Exact consequence for the unchanged closed-triangle theorem

Use (5) in the fixed-J,K arithmetic triangle proof in
`CLOSED_TRIANGLE_WEIGHT.md`, retaining all of that theorem's
hypotheses and its original state and edge weights. In particular
the prime sets are disjoint, $V_i\ge v_*>0$,
$\alpha=\sum_i a_i>0$, $\beta=\sum_i b_i$, and
$H=\min(d_0YM,N)\ge x^\delta$. The $d_0$ here again
denotes the source's dyadic shared-product scale.

The existing proof has at most $O(d_0Y^3)$ integer label
families, at most $O(d_0Y)$ first-position candidates per
family, and used-prime modulus $S=Dabc\le128d_0Y^3$.
The two other position restrictions, goodness and unused damping
are dropped only in its positive upper count. A fixed candidate
then has a single first-position interval in the real root r;
no boundary partition is required. Thus (5) gives total error

$$
        O_\epsilon(d_0^4Y^{10}H^{\kappa-1+\epsilon}),       \tag{25}
$$

with the fixed list and V constants as in the earlier theorem.
There is no reciprocal-prime weight attached to this discrepancy.
Its main term retains precisely the once-line weights already paid
in the continuous triangle bound.

Equivalently, the prime-band count used in Section 5 of that note is

$$
 x^{(J+3)\beta}\,x^{(J+1)\beta}\,
 x^{2(J+3)\beta-(1-\kappa)\delta+\epsilon}
     =x^{(4J+10)\beta-(1-\kappa)\delta+\epsilon}.
 \tag{26}
$$

Hence the **same restricted absolute common-list raw triangle** obeys

$$
 \boxed{
 T_{\rm tri}^{\rm arith}\ll
 x^{-\alpha+\epsilon}
       +x^{(4J+10)\beta-(1-\kappa)\delta+\epsilon}.}
 \tag{27}
$$

This is unconditional for the elementary kappa=3/4 input proved
above. The kappa=1/2 version uses the explicitly named classical
exponential-sum theorem. Neither version imports the full HLC result.

For a concrete parameter choice take J=K=1, delta=1/4 and the
prime band $[x^{1/800},x^{1/400}]$, retaining the fixed positive
V lower bound. Then (27) gives respectively

$$
 T_{\rm tri}^{\rm arith}
  \ll x^{-1/800+\epsilon}+x^{-11/400+\epsilon}
                          \quad(\kappa=3/4),              \tag{28}
$$
$$
 T_{\rm tri}^{\rm arith}
  \ll x^{-1/800+\epsilon}+x^{-9/100+\epsilon}
                          \quad(\kappa=1/2).              \tag{29}
$$

These are fixed-power estimates in the source's x-scale for this
specified path class and fixed-parameter variant. They do not identify
x with the native inverse detector's U or prove its open witness
bound. The source itself has growing J and
subpower prime bands. Moving all its growing lists to polynomial
bands would multiply the union-prime exponent by J; (26) does not
justify that different scheme. The complete centered path expansion,
changing shared lists, arbitrary conditioned histories, and the
Eisenstein inverse detector remain outside this theorem.

### The independently proved extension to both endpoint lists

`COMMON_D_TRIANGLE_EXTENSION.md` proves the same continuous
$Y^{-1}(1+\log(3Y))^2$ upper bound, with its displayed fixed
list/V constants, for **all** common-D three-edge raw root returns.
The initial and final complete lists may differ; that note retains
both actual root-vector coordinates and pays every partial-return
pattern. We use that separate theorem without changing its proof.

For this larger class there are at most $O(d_0Y^4)$ label
families, the same $O(d_0Y)$ first-position candidates, and
used-prime modulus $S\ll d_0Y^4$. Formula (5) therefore gives
the discrepancy

$$
              O_\epsilon(d_0^4Y^{13}H^{\kappa-1+\epsilon}).
 \tag{30}
$$

In prime-band notation its exact exponent ledger is
$(J+4)\beta+(J+1)\beta+2(J+4)\beta$, so

$$
 \boxed{
 T_{\rm common}^{\rm arith}\ll x^{-\alpha+\epsilon}
       +x^{(4J+13)\beta-(1-\kappa)\delta+\epsilon}.}
 \tag{31}
$$

The source line count is again applied to a single first-position
root interval per fixed primitive candidate, after the positive
enlargements made in that theorem. No boundary conversion or
additional endpoint independence is presumed. With the same
J=K=1, delta=1/4 and $[x^{1/800},x^{1/400}]$ band,

$$
 \begin{split}
 T_{\rm common}^{\rm arith}
   &\ll x^{-1/800+\epsilon}+x^{-1/50+\epsilon}
                                     &&(\kappa=3/4),\\
 T_{\rm common}^{\rm arith}
   &\ll x^{-1/800+\epsilon}+x^{-33/400+\epsilon}
                                     &&(\kappa=1/2).
 \end{split}                                               \tag{32}
$$

The elementary version therefore pays a genuine restricted
$x^{-0.00125+\epsilon}$ contribution without the classical input.
The scale is the source's x. There is still no deduction of the
native $U$-scale thin-band witness bound, of changing-shared-list
paths, or of the full centered HLC operator.

## 7. Verification boundary

`check_root_count_refinement.py` checks finite congruence and
normalization identities, the all-frequency gcd divisor inequality,
the normalized-completion involution, matrix and line cardinalities,
the progression-gcd ledger and the rational triangle budgets.
It also checks the finite Kloosterman fourth-moment combinatorics.

The optimized replay passes 31 finite fourth-moment moduli, 11,439
unit-orbit cardinalities, 172,248 exact phase-histogram identities,
1,549 fixed-u congruence cases, 81,258 CRT Fourier phases, 211,840
gcd-frequency cases including axes and large frequencies, 123,070
progression-gcd ledgers, and 2,392 normalized scale swaps. Its
remaining cardinality, harmonic-progression and exponent-budget
checks and negative controls also remain enabled under optimization.

The Fourier majorants, divisor estimates and asymptotic counting
bounds are proved analytically above. Finite tests do not establish
those bounds, the imported classical Weil--Salié estimate, or any
zero-free statement.
