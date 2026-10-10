# Moving inner exclusions, auxiliary twists, and the A2 correction operator

**Status:** proposed source-conditional positive-norm theorems and exact
finite arithmetic identities. The moving inner exclusion in PR #918's
mixed theta family is handled explicitly. The completed estimate and its
full cube inverse hold for every nonzero row and for overlapping moving
squarefree ideals `q,f`. The exact A2 correction operators preserve a
quantitative envelope without a polynomial correction loss. None of these
positive norm estimates proves the signed first-Poisson off-diagonal, the
fourth moment, the generalized moment hierarchy, or RH.

**Authorship:** `/root/moving_auxiliary_attack`. Independent review must
bind the final bytes of this note. No computation is used as evidence for
the infinite estimates.

## Sources and the precise imported contract

The new local calculation below uses the following pinned sources.

| Source | Exact pin and interface |
|---|---|
| Imported theta framework | OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`: `eq:T`, `eq:cube-inverse`, `eq:ray-local-transform`, and the complete scalar after `eq:dual-cusp-mellin-series` |
| Exact A2 arithmetic | PR #914, `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`, Theorem 4.1 and equation (5.8) |
| Actual mixed family | PR #918, `cfa102748b26f840ccc4b963a660711424db0ec3`, `standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md`, equations (2.1)–(3.5) |
| All-row and auxiliary calculation | PR #921, `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`, `standalone/2026-10-10-sextic-centered-covariance/ARBITRARY_ROW_MOMENTS.md`, equations (2.1)–(5.2), Section 6, and Corollary 7.2; its `CUBE_INVERSE.md`, Lemma 2.1 and Theorems 4.1–5.1 |
| Outer-mask uniformity and pruned completion | PR #923, `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/ALL_ROW_COMPLETION_AND_RAW_GAIN.md`, Theorem 1.1, and its stated all-cusp inputs |
| Exact cusp coefficient normalization | Parent PR #922 mathematical source `8f2acaacddc10bd8fb053a66070a1d06d25aa922`, `standalone/2026-10-10-signed-covariance-descent/ALL_CUSP_COEFFICIENT_ADAPTER.md` and `FINITE_CUBE_HOMOGENEITY.md` |

The coefficient formulas in the last line derive from Dunn and
Radziwill, [arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
equations (5.7), (5.8), (5.13), and (5.14), with the imported additive
character and conjugate-theta convention. No conditional prime-sum or
dispersion theorem from that paper is invoked.

Fix `1/2 < beta <= 1`. The scalar analytic premise is precisely the
uniform bound used by PR #921: for the fixed finite family of ray
characters `eta`, squarefree primary `s` outside `S`, polynomially bounded
moving exclusions `C`, and fixed compact smooth tests,

\[
\sum_{(g,CS)=1}\mu_K(g)\eta(g)\overline{\alpha(g)}^{3}
 \chi_s(g)^3 V(Ng/X)
 \ll_{\epsilon} D^\epsilon X^\beta\|V\|_{C^J}.
\tag{0.1}
\]

All parameters are bounded by fixed powers of `D`; `J` and the implied
constant are uniform in those parameters. Nonempty subunit lengths lie
in a fixed compact positive interval and are covered by counting.
The choice `beta=1` is elementary. The choice `beta=11/12`, with arbitrary
small-power losses as displayed, retains the source-conditional angular
reciprocal input in PR #920/921. No estimate on its endpoint contour is
being asserted. The theta transformations, their complete three-cusp
coefficient formulas, and the quadratic and cubic large sieves remain
imported analytic inputs. This note proves their new composition and
local parameter accounting, rather than rebuilding those foundations.

## 1. Exact objects and normalizations

Work in `K=Q(omega)`, with `O=Z[omega]`, norm `N`, and multiplicatively
chosen primary generators outside the fixed bad set `S`. All original
column ideals below avoid `S`. The set `S` contains the primes over `6`
and the conductors of the fixed ray data; it is not enlarged by any
moving ideal. Write

\[
\alpha(n)=n/|n|,\qquad
\lambda(n)=\overline{\alpha(n)}\xi(n),\qquad
a_\xi(n)=\lambda(n)\gamma_2(n)\quad(n\text{ squarefree}).
\tag{1.1}
\]

Here `lambda` is a multiplicative coefficient, not the ramified-prime
generator. Every residue-symbol power includes its zero on nonunits,
also when the exponent is zero modulo six.

Let `q,f` be squarefree primary ideals outside `S`, with overlap allowed.
Let `h` be an arbitrary polynomially bounded original outer exclusion.
Set

\[
r=\frac{q}{(q,f)},\quad R_q=Nr,\quad F_f=Nf,\quad
L_{q,f}=R_q F_f=N\operatorname{lcm}(q,f),\quad
M_{q,f}=R_q^{1/3}F_f^{2/3}.
\tag{1.2}
\]

The fixed tests `W_1,W_2` are smooth and compactly supported in positive
intervals. Define the normalized raw polynomial

\[
p_q(A,B;k,f)=\frac1{\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,qS)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
 W_1(Na/A)W_2(Nn/B).
\tag{1.3}
\]

Define the mixed completion in physical, hence finite, form by

\[
\begin{split}
\mathcal C_{q,h}(A,B;k,f)=\frac1{\sqrt{AB}}
\sum_{\substack{a,n\ {\rm squarefree},\ b\ {\rm arbitrary}\\
 (a,nb)=1,\ (anb,qfS)=1,\ (a,h)=1}}
&a_\xi(an)\lambda(b)^3\sqrt{Nb}\,
 \chi_{anb^3}(k)\chi_{an}(f)^4\\
&\times W_1(Na/A)W_2(Nn(Nb)^3/B).
\end{split}
\tag{1.4}
\]

The condition `(n,b)=1` is absent. Its absence is essential. Equation
(1.4) is PR #918's `C_{q,v_h}`, where `v_h(a)=1_(a,h)=1`, obtained by
substituting its literal `T` and using `V_*(y)=sqrt(y)W_2(y)`. Its
reflected cusp indices are not restricted to avoid `S`; the full
reflected sums will be retained.

All scales, moving labels and row lengths are bounded by fixed powers
of `D>=2`. Initially take `A,B,H>=1`. All statements also apply to
nonempty child rectangles in a fixed compact interval below one:
compact support gives a uniform positive lower bound on such scales,
and rescaling to a fixed interval changes only fixed test seminorms.
An empty rectangle contributes zero.

### Lemma 1.1. The moving mask is a principal row twist

For every nonzero element row `k`,

\[
\boxed{
\mathcal C_{q,h}(A,B;k,f)
 =\mathcal C_{1,h}(A,B;k f^4 q^6,1),\qquad
p_q(A,B;k,f)=p_1(A,B;k f^4 q^6,1).
}
\tag{1.5}
\]

**Proof.** In each term of (1.4), complete multiplicativity gives

\[
\chi_{anb^3}(f^4q^6)
=\chi_{an}(f)^4
 \mathbf1_{(anb,qf)=1}.
\tag{1.6}
\]

In particular `chi_b(f)^12` and `chi_(anb^3)(q)^6` are the indicated
unit masks. This is also valid when `q,f,k` overlap. Apply (1.6) to the
unrestricted `q=f=1` physical sum; its zeros produce exactly (1.4).
The raw identity is its `b=1` version. All sums are finite. \(\square\)

The right side of (1.5) is not estimated by enlarging the row ball to
norm `H(Nf)^4(Nq)^6`. The physical row `k` is still averaged at norm
`H`; the local calculation below retains that distinction.

## 2. The mixed completed theorem

Put `T_(A,B)=min(A,sqrt(B))` and
`delta=(2 beta-2)/3`. Then `-1/3<delta<=0`.

### Theorem 2.1. All rows, moving inner mask, and moving auxiliary

Under (0.1), uniformly in the parameters just specified,

\[
\boxed{
\begin{split}
\sum_{H\le Nk<2H}|\mathcal C_{q,h}(A,B;k,f)|^2
\ll_\epsilon D^\epsilon\left[
HA+L_{q,f}\frac{H^2A}{B}T_{A,B}^{2\beta-1}
+M_{q,f}\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].
\end{split}}
\tag{2.1}
\]

The sum includes every nonzero Eisenstein element row in the annulus,
with all units and fixed bad-prime factors. The constants are uniform
in the additional outer mask `h`. At `beta=11/12`, the exponent on
`T_(A,B)` is `5/6`.

The new cost of a principal moving prime outside `f` is `1,Np,(Np)^(1/3)`
in the three monomials. A prime in `f`, including an overlap with `q`,
has the auxiliary costs `1,Np,(Np)^(2/3)`. In particular, overlapping
primes are counted once in `L_(q,f)`.

### 2.1. The reusable reflected block and scalar

Here is the precise part of the source proof being extended. Decompose
an ordinary physical row outside a designated finite list of moving
primes as `k=u k_S tau k_0`, with `k_0` squarefree containing the
valuation-one primes, and every prime in `tau` having valuation at least
two. Fixed moving primes will have their physical valuations recorded
separately. The variable row is `k_0` at its actual remaining norm
`H_0`; every fixed prime restriction on `k_0` is retained until after
the scalar estimate.

Reunite the original outer Ramanujan allocation `a=d g` before taking
norms. The complete projected group vanishes for `Ng>C_S sqrt(B)`.
Insert its smooth support cutoff at this point and only then split
`d=e j`, and write the good reflected frequency as
`epsilon lambda_ram^(m+4) e n_S n_0 (j b')^3`.
Here `j` denotes the positive cube allocation and is unrelated to a
local character exponent below. The relation among their dyadic lengths
is `E J G` comparable to `A`. Every reflected cube index and bad-prime
part is present.

For a fixed row sector and local branch, the proven quadratic-cubic
block calculation has three energy monomials

\[
G^{2\beta-2}
  [H_0 E+Y+(EY)^{2/3}],\qquad
Y=\frac{H_0^2 R_*^2 E G^2}{B J},
\tag{2.2}
\]

times the squared amplitude of any fixed additional separated row
factors. `R_*` is the fixed active row radical. This is PR #921 (4.3),
with the exact scalar and all-cusp adapters retained. The outer mask
`(a,h)=1` remains in the scalar exclusion and in separate positive
column masks, as in PR #923's Theorem 1.1.

The mixed scalar is exactly a fixed ray multiple of

\[
\mu_K(g)\overline{\alpha(g)}^{3}\chi_s(g)^3,
\tag{2.3}
\]

where `s` is the odd good prime radical of the *physical* row `k`.
The shifts `4` and `6` in (1.5) are even, so they do not change `s`.
Its norm is bounded by a fixed multiple of `H`. All of `qf`, all even
row primes, and the outer mask remain in the moving exclusion. Thus
(0.1) is applied to exactly its stated squarefree scalar index and a
polynomially bounded exclusion. No larger fixed-ray family or growing
infinity type is introduced.

For completeness, the source local scalar at an active row prime with
exponent `j modulo 6` has outer-`a` dependence
`chi_p(a)^(2j+2)`. Multiplication by the `a`-prime scalar, Gauss CRT,
and the original exterior row character leaves `chi_p(a)^(3j)` and
the angular factor `alpha(a)^(-3)`. This is PR #921 (2.1)–(2.4),
valid also at active exponent zero and at exponent four. Hence the
scalar assertion remains true at the newly inserted principal primes.

### 2.2. A principal mask prime with physical valuation zero

Let `p|r`, write `z=Np`, and first suppose `p` does not divide the
physical row `k`. The effective row in (1.5) has exponent zero modulo
six at `p`, but a positive actual exponent. Its local zero mask therefore
has two source branches:

| Branch | Scalar magnitude | Active denominator at `p` | Reflected multiplier |
|---|---:|---:|---|
| Inactive | `1-z^(-1)` | none | none |
| Active | `1` | `p` | `z^(-1/2) chi_p(x)^(-2)` |

This table follows directly from `eq:ray-local-transform`, including
the separate scalar in PR #921 (2.2). An inactive prime occurs in
neither the reflected denominator nor the second projection period.
An active prime occurs once in both. Consequently the exact support
cutoff `G^2 << B` survives in both branches: the active radical cancels
out of the ratio of the reflected scale to the squared projection
period. It would be incorrect to leave an inactive prime in either
quantity.

The original column mask makes `p` prime to `a=e j g`. In the active
branch the character of the reflected frequency separates into a
bounded `e` coefficient, a bounded `n_0` coefficient, and frozen
factors of `j,b'` and the bad part. Its zero at `p|n_0b'` is retained.
There is no new interaction with `g`. This allows (2.2) to be used
with squared amplitude `z^(-1)` and effective length multiplier `z^2`.

Take Minkowski over these two local branches before discarding their
phases. For the three monomials in (2.2), their squared norm costs are
at most fixed constants times

\[
\begin{split}
&(1-z^{-1}+z^{-1/2})^2\ll1,\\
&(1-z^{-1}+z^{1/2})^2\ll z,\\
&(1-z^{-1}+z^{1/6})^2\ll z^{1/3}.
\end{split}
\tag{2.4}
\]

The first term of each parenthesis is the inactive branch. These
estimates give the claimed principal-prime costs. Products of the
fixed constants over moving primes cost `C^(omega(qf))`, which is
`D^epsilon` after allocating the preliminary losses; no uniform
convergent Euler product is claimed for those constants.

### 2.3. Auxiliary primes, including overlap with the mask

For `p|f`, the effective local exponent is `nu_p+4 modulo 6`, where
`nu_p=v_p(k)`. If also `p|q`, the extra six does not change this local
exponent or its unit mask. Thus the overlap is the same auxiliary
prime, rather than two successive conductor penalties.

At `nu_p=0`, the reflected factor is

\[
B_{p,4}(x)=-z^{-1/2}
 +z^{1/2}\mathbf1_{p\mid n_0}
 +z^{1/2}\mathbf1_{p\nmid n_0,\ p\mid b'}.
\tag{2.5}
\]

Before freezing the full cube sum, set `n_0=p n_1` in the second term
and `b'=p b_1` in the third. The second retains `p` prime to `n_1`;
the third retains `p` prime to `n_0`, and `b_1` is unrestricted at `p`.
Relative to the length before this prime was inserted, the resulting
three squared amplitudes and lengths are

\[
(z^{-1},z^2),\qquad (1,z),\qquad (z^{-1},z^{-1}).
\tag{2.6}
\]

The factors `1/sqrt(Nn_0)` and `1/Nb'` in the actual cusp expansion
are responsible for these amplitudes. In particular the squarefree
reindexing gives separate CRT factors

\[
\gamma_2(e p n_1)=\gamma_2(p)\gamma_2(e)\gamma_2(n_1)
 \chi_e(p)^4\chi_{n_1}(p)^4\chi_{n_1}(e)^4,
\tag{2.7}
\]

with every zero mask retained. The additional quadratic row factor
`chi_(k_0)(p)^3` is a row contraction on the actual rows. This is the
exact all-cusp reindexing of PR #921, Corollary 7.2, rather than an
arbitrary replacement of the theta coefficients. It is unchanged by
the principal mask at an overlapping prime because that mask was
already present in the exponent-four symbol.

Minkowski in (2.6) gives costs

\[
\begin{split}
&(z^{-1/2}+1+z^{-1/2})^2\ll1,\\
&(z^{1/2}+z^{1/2}+z^{-1})^2\ll z,\\
&(z^{1/6}+z^{1/3}+z^{-5/6})^2\ll z^{2/3}
\end{split}
\tag{2.8}
\]

for the same three monomials. Repeated application of (2.7) introduces
only separate column characters and bounded factors among the fixed
extracted primes. It introduces no character coupling `g` to a theta
column. The fixed bad-prime ray decomposition remains finite and
uniform.

### 2.4. Sum all positive physical valuations

It remains to include the actual rows meeting the moving primes. At
`p|r`, physical valuation `nu>=1` has effective exponent `nu modulo 6`.
The crude source branch and squared-amplitude weights are

\[
b_\nu=4^{\mathbf1_{6\mid\nu}},\qquad
\Lambda_\nu^2=z^{\mathbf1_{\nu\equiv4\ (6)}}.
\tag{2.9}
\]

The active radical contributes at most `z` whereas the remaining row
height is divided by `z^nu`. The three local energy sums are bounded by

\[
\begin{split}
\sum_{\nu\ge1} b_\nu\Lambda_\nu^2z^{-\nu}&=O(z^{-1}),\\
\sum_{\nu\ge1} b_\nu\Lambda_\nu^2z^{2-2\nu}&=O(1),\\
\sum_{\nu\ge1} b_\nu\Lambda_\nu^2z^{4/3-4\nu/3}&=O(1).
\end{split}
\tag{2.10}
\]

Each of the six progressions is geometric. At a prime in `f`, replace
`b_nu` by `4^(1_(nu=2 mod 6))` and `Lambda_nu^2` by
`z^(1_(nu=0 mod 6))`. The same three bounds in (2.10) hold, as shown
in PR #921 (7.11). In both cases their leading possible costs are
already included in (2.4) or (2.8).

The row strata for different physical valuations are disjoint; their
energies are added, with no Minkowski factor for the number of such
strata. Outside `qfS`, the remaining powerful row factors have the
convergent weights of PR #921 Section 6: the local factors are
`1+O(z^(-2))`, `1+O(z^(-2))`, and `1+O(z^(-4/3))`. The fixed bad-prime
powers have geometric sums for the corresponding powers `1,2,4/3`
of row height. All six row units and all finite ray classes add fixed
factors. This includes the terminal unit row and nonempty remaining
row intervals below one.

### 2.5. Finish the completed estimate

Multiply the costs (2.4) over `r` and (2.8) over `f`, then include
(2.10) and the convergent ordinary row-sector sums. The three costs
are exactly bounded by

\[
D^\epsilon(1,L_{q,f},M_{q,f}).
\tag{2.11}
\]

They attach to the three monomials of (2.2) separately. All local
reindexings occur after the complete support cutoff was inserted and
before dyadic frequency estimates. Normalized smooth ratios are
rescaled with their lengths, so the Mellin seminorms and tails remain
uniform in the extracted prime products. All those products are
polynomially bounded. Summing the unrestricted reflected cubes,
ramified towers, fixed bad parts and finite ray families is the
unchanged summation in the pinned all-cusp proofs.

For clarity, the three dyadic allocation monomials after `E J G`
is replaced by `A` are

\[
\frac{HA}{J}G^{2\beta-3},\qquad
\frac{H^2A}{BJ^2}G^{2\beta-1},\qquad
\left(\frac{H^2A^2}{B}\right)^{2/3}J^{-2}G^{2\beta-2}.
\tag{2.12}
\]

Use `G<<min(A,sqrt(B))`, `J,G` bounded below on nonempty dyads, and
`1/2<beta<=1`. These are bounded respectively by
`HA`, `H^2 A T_(A,B)^(2 beta-1)/B`, and
`(H^2 A^2/B)^(2/3)`. Minkowski over their logarithmically many smooth
dyads costs a subpower. With (2.11) this proves (2.1). \(\square\)

## 3. Full cube inversion with the same moving-prime costs

### Theorem 3.1. The literal mixed raw polynomial

Under the same hypotheses,

\[
\boxed{
\sum_{H\le Nk<2H}|p_q(A,B;k,f)|^2
\ll_\epsilon D^\epsilon\left[
HA+L_{q,f}H^2 A B^\delta
+M_{q,f}H^{4/3}A^{4/3}B^\delta
\right].}
\tag{3.1}
\]

The estimate also holds with `A,W_1` and `B,W_2` interchanged. Thus
one may choose the smaller axis as the outer axis. This symmetry is
asserted for the raw polynomial, not for one particular completion.

**Proof.** The exact cube inverse, including its outer mask, is

\[
p_q(A,B;k,f)=
\sum_{\substack{v\ {\rm squarefree}\\(v,qfS)=1}}
\frac{\mu_K(v)\lambda(v)^3\chi_v(k)^3}{Nv}
\mathcal C_{q,v}(A,B/(Nv)^3;k,f).
\tag{3.2}
\]

It follows either by (1.5) from the source inverse or directly by
putting the combined cube index `d=vb` and using
`sum_(v|d) mu_K(v)=1_(d=1)`. The restriction `(a,v)=1` belongs inside
the completion; `v` and the remaining theta squarefree index need
not be coprime after reflection. All identities are finite on the
original smooth support.

Use the full signed inverse proof of PR #921, rather than the sum of
the absolute inverse coefficients. Its second scalar variable `v`
has the same form (0.1), since

\[
\chi_v(k f^4q^6)^3=
\chi_v(k)^3\mathbf1_{(v,qf)=1}.
\tag{3.3}
\]

The two scalar variables `g,v` retain their mutual coprimality. The
exact finite common-divisor correction used by that proof has norm
cost `sum_l (Nl)^(-2 beta)`, which converges. Their two intersections
with the positive squarefree column give costs
`sum_d (Nd)^(-beta-1/2)` and
`sum_j (Nj)^(-beta-1/2)`, both convergent. Enlarging the scalar
exclusions by `qf` does not affect (0.1). No condition between a
remaining positive column and the common correction label is added.

The complete reflected support inserted before the positive split is
now `G^2 Z^3 << B`, with `Z` the inverse-index dyadic norm. The fixed
block bound is PR #921 (5.2),

\[
G^{2\beta-2}Z^{2\beta-2}
[H_0E+Y+(EY)^{2/3}],\qquad
Y=\frac{H_0^2R_*^2 E G^2Z^3}{B J}.
\tag{3.4}
\]

The new local principal and auxiliary calculations in Section 2 act
only on its three energy monomials. They do not couple either scalar
to a theta column: at every moving prime, the original `a` and
inverse `v` avoid `qf`. Thus the same costs (2.11) apply to (3.4).

After `E J G` is replaced by `A`, the monomials are

\[
\frac{HA}{J}G^{2\beta-3}Z^{2\beta-2},\quad
\frac{H^2A}{BJ^2}G^{2\beta-1}Z^{2\beta+1},\quad
\left(\frac{H^2A^2}{B}\right)^{2/3}
J^{-2}G^{2\beta-2}Z^{2\beta}.
\tag{3.5}
\]

The first is `O(HA)`. The support and `beta<=1` give

\[
G^{2\beta-1}Z^{2\beta+1}
\ll B^{(2\beta+1)/3}G^{(2\beta-5)/3}
\ll B^{(2\beta+1)/3},
\]
\[
G^{2\beta-2}Z^{2\beta}
\ll B^{2\beta/3}G^{(2\beta-6)/3}
\ll B^{2\beta/3}.
\tag{3.6}
\]

Their resulting costs are exactly the second and third terms in
(3.1). The full cusp, local and Mellin summations remain those of
Section 2 and the cited inverse proof. Finally interchange the finite
variables `a,n` in (1.3). Its coefficient, zero masks and auxiliary
twist are symmetric, and only the two tests interchange. This proves
the stated second orientation. \(\square\)

At `q=f=1`, Theorem 3.1 reproduces the complete-inverse envelope of
PR #921. It is not the optimized short/long inverse estimate in
PR #923. The companion `OPTIMIZED_A2_TRANSFER.md` uses Theorem 2.1
with that separate optimization.

## 4. Exact A2 children and norm stability

Write `Q_q(A,B;k,f)` for the *unnormalized* A2 arithmetic completion in
PR #914, with the same tensor test and moving mask. Thus its summand
is

\[
\mathfrak a_\xi(n_1,n_2)\chi_{n_1n_2}(k)
\chi_{n_1n_2}(f)^4
W_1(Nn_1/A)W_2(Nn_2/B)\mathbf1_{(n_1n_2,qS)=1}.
\tag{4.1}
\]

Its coefficient normalization is exactly that of the pinned A2
table; no analytic Weyl functional equation is inferred from this
arithmetic definition. Put `q_q=Q_q/sqrt(AB)` in this section only.

For a correction triple `t=(c,d,e)`, let `c,d,e` be pairwise-coprime
squarefree ideals outside `qfS`, and set `C=cde`. Then

\[
A_t=\frac A{Nc(Nd)^2(Ne)^2},\qquad
B_t=\frac B{(Nc)^2Nd(Ne)^2},\qquad
q_t=qC,\qquad f_t=ef.
\tag{4.2}
\]

The exact normalized correction multiplier is

\[
w_t(k,f)=\frac{\omega_t(k,f)}{Nc\,Nd\,(Ne)^{3/2}},
\]
\[
\omega_t(k,f)=\lambda(C)^3a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4,
\qquad |\omega_t(k,f)|\le1.
\tag{4.3}
\]

The phase and all its row zeros are retained in (4.3). The exact
forward and inverse identities from PR #914 give

\[
q_q(A,B;k,f)=\sum_t w_t(k,f)p_{q_t}(A_t,B_t;k,f_t),
\tag{4.4}
\]
\[
p_q(A,B;k,f)=\sum_t\mu_K(C)w_t(k,f)
 q_{q_t}(A_t,B_t;k,f_t).
\tag{4.5}
\]

The unchanged correction labels have the exact parameter updates

\[
\frac{q_t}{(q_t,f_t)}=r c d,\qquad
L_{q_t,f_t}=L_{q,f}\,Nc\,Nd\,Ne,
\]
\[
M_{q_t,f_t}=M_{q,f}(Nc\,Nd)^{1/3}(Ne)^{2/3},\qquad
A_tB_t=\frac{AB}{(Nc\,Nd)^3(Ne)^4}.
\tag{4.6}
\]

In particular the overlap at `e` is literal; it is the reason `e`
does not occur in `q_t/(q_t,f_t)`.

### Theorem 4.1. A quantitative all-row A2 envelope

Under the same imported inputs and (0.1), both `p_q` and `q_q` satisfy

\[
\boxed{
\begin{split}
\sum_{H\le Nk<2H}|X_q(A,B;k,f)|^2
\ll_\epsilon D^\epsilon\bigg[
&H(AB)^{1/2}
+L_{q,f}H^2(AB)^{(1+\delta)/2}\\
&+M_{q,f}H^{4/3}(AB)^{2/3+\delta/2}
\bigg],\qquad X=p,q.
\end{split}}
\tag{4.7}
\]

Both exact correction operators (4.4)–(4.5) preserve the class of
uniform bounds (4.7), with a constant depending on `beta` and the
fixed data. Their correction-label norm sums are absolutely
convergent, rather than merely bounded on a finite horizon.

**Proof.** In Theorem 3.1 choose the smaller raw axis as the outer one.
Since `delta<=0`, that choice minimizes all three of its monomials.
For positive `x,y`,

\[
\min(x,y)\le\sqrt{xy},\quad
\min(xy^\delta,yx^\delta)\le(xy)^{(1+\delta)/2},
\]
\[
\min(x^{4/3}y^\delta,y^{4/3}x^\delta)
\le(xy)^{2/3+\delta/2}.
\tag{4.8}
\]

This proves (4.7) for the raw family at every required child.
Apply Minkowski to (4.4), retain the row contractions (4.3), and
separate the square roots of the three positive monomials. Using
(4.6), the three correction norm weights are exactly bounded by

| Parent monomial | Power of `Nc` and `Nd` in the denominator | Power of `Ne` in the denominator |
|---|---:|---:|
| `H(AB)^(1/2)` | `7/4` | `5/2` |
| `L H^2(AB)^((1+delta)/2)` | `5/4+3delta/4` | `2+delta` |
| `M H^(4/3)(AB)^(2/3+delta/2)` | `11/6+3delta/4` | `5/2+delta` |

For example, the second child monomial has multiplier
`(Nc Nd)^(-1/2-3delta/2)(Ne)^(-1-2delta)` relative to its parent.
Taking its square root and multiplying (4.3) gives the middle row
of the table. Every displayed exponent exceeds one because
`delta>-1/3`. Thus the sums are bounded by products of convergent
ideal zeta series. The actual squarefree and coprimality restrictions
may be dropped only in these nonnegative accounting sums.

All child scales and labels remain polynomially bounded. Preliminary
small-power losses can be chosen with one common `D`; finite fixed
test changes and nonempty subunit scales have already been covered.
Squaring the three convergent norm sums proves (4.7) for the A2
completion. Exactly the same calculation applies to (4.5), since its
extra `mu_K(C)` has modulus one on its squarefree support. This proves
the operator assertion in both directions. \(\square\)

At `A=B=D`, (4.7) reads

\[
\sum_{k\asymp H}|X_q(D,D;k,f)|^2
\ll D^\epsilon\left[
HD+L_{q,f}H^2D^{1+\delta}
+M_{q,f}H^{4/3}D^{4/3+\delta}\right].
\tag{4.9}
\]

For `beta=11/12`, `delta=-1/18`; the second and third powers of `D`
are `17/18` and `23/18`. This is now a uniform theorem for the full
A2 polynomial with the displayed inner exclusions and auxiliaries,
not an identification of A2 with the one-axis completion. The sharper
short/long result is stated separately in the companion note.

### Fixed separate ray twists

All theorems remain valid if the raw summand is multiplied by
`eta_1(a)eta_2(n)`, where `eta_1,eta_2` are fixed finite ray characters
whose conductors are absorbed in the original fixed `S`. For the
corresponding A2 theorem multiply (4.1) by
`eta_1(n_1)eta_2(n_2)`.

To see the analytic assertion, use inner theta character `xi eta_2`
and outer fixed multiplier `eta_1(a)/eta_2(a)`. Its reflected negative
allocation and inverse cube acquire only fixed finite ray factors,
within the family admitted in (0.1). The inverse cube coefficient
uses `(lambda eta_2)(v)^3`, as required by that inner theta character;
it must not be left at `lambda(v)^3`. All good-prime scalar and local
zero calculations are unchanged. Interchanging the raw axes also
interchanges `eta_1,eta_2`.

Arithmetically, the correction multiplier (4.3) acquires the factor

\[
\eta_1(c d^2e^2)\eta_2(c^2d e^2),
\tag{4.10}
\]

and the child retains the same two fixed ray characters. This follows
by substituting the exact A2 column parametrization. The new factor
is multiplicative on disjoint correction triples and has modulus one
on their good support. Hence the forward and inverse corrections
and every norm sum are unchanged. This includes a fixed extra finite
character on just one factor axis.

## 5. Rows with fixed smooth profiles

Theorems 2.1, 3.1 and 4.1 also hold for sharp row balls, with their
same three monomials in `H`, and for a fixed nonnegative Schwartz
weight `Phi(Nk/H)`.

For balls, sum dyadic annuli including the final unit rows. The powers
of `H` are `1,2,4/3`, so the resulting geometric sums converge. For a
Schwartz tail at scale `2^j H`, use a polynomial reference
`D_j=2^j D`, keep the original column and auxiliary parameters fixed,
and bound the row weight by `O_Phi(2^(-jM))` for fixed `M>2+epsilon_0`.
The preliminary theorem contributes at most
`D^epsilon_0 2^(j(2+epsilon_0))` times its original bracket. The
tail therefore converges, exactly as in PR #921 Section 8. This
extension does not assert separability of a row kernel that depends
jointly on both product columns.

## 6. Exact two-column boundary and the next missing estimate

The new adapter closes the moving inner-mask and auxiliary interface
for a *single positive norm*. It also supplies legitimate norms for
every separately corrected child in the exact A2-to-theta expression.
For clarity, insert (3.2) into (4.4):

\[
q_q(A,B;k,f)=\sum_t\sum_{\substack{v\ {\rm squarefree}\\
 (v,q_t f_t S)=1}}
w_t(k,f)\frac{\mu_K(v)\lambda(v)^3\chi_v(k)^3}{Nv}
\mathcal C_{q_t,v}(A_t,B_t/(Nv)^3;k,f_t).
\tag{6.1}
\]

Every original signed coefficient and zero is still in this finite
identity. In a sesquilinear expression, substitute (6.1) independently
in the two columns, with separate triples `t,t'` and inverse labels
`v,v'`, and conjugate the full second coefficient. One must keep the
two changed masks `q_t,q_(t')`, the two generally distinct auxiliary
ideals `ef,e'f`, and the two outer cube masks. Equality of reconstructed
product columns is not equality of those labels.

There is an exact bookkeeping rule for the strict product diagonal.
For the inverse A2 projection (4.5), a child full column `(n_1,n_2)`
reconstructs its parent product as

\[
s_t n_1n_2,\qquad s_t=c^3d^3e^4.
\tag{6.2}
\]

For the forward A2 expansion (4.4), a raw child `(a,n)` similarly
reconstructs `s_t an`. If that raw child is then represented through
its cube inverse, a physical theta term `(a,n,b)` with inverse label
`v` carries the formal reconstructed product

\[
s_t a n(vb)^3.
\tag{6.3}
\]

The equality follows from `a,n` being the residual squarefree indices
and from the *combined* cube index `vb`. For each fixed combined
index the signed sum over its inverse divisors kills it unless
`vb=1`. Therefore any original finite two-column kernel, including
its strict product inequality, can be lifted termwise using (6.2) or
(6.3) before summing. In particular the strict selector compares

\[
s_t a n(vb)^3\ne s_{t'}a'n'(v'b')^3,
\tag{6.4}
\]

rather than simply `an != a'n'` or equality of factor pairs. The
lift is valid because the original kernel is constant on all
subdivisions of a fixed reconstructed column; all such sums are
finite. It does not make that kernel a product of separate column
weights or a nonnegative row weight.

In the source's strict first-Poisson off-diagonal, the complete outer
signed `b,f` sum, its `mu_K(f)` weight, the row-dependent coupled
kernel, and the strict reconstructed product inequality must remain
together. In that original notation, the Poisson index `b` is
different from the theta cube index in (6.3). These new positive
norms do not authorize replacing that signed expression by a single
member, by an unsigned auxiliary average, or by its product-diagonal
part. PR #914 already removed the *total signed* first-Poisson
diagonal exactly; this theorem does not restore it.

The remaining sufficient estimate is still the literal signed
strict off-diagonal of PR #914, equation (6.9), at the required
balanced scales. The initial dual row length is of order
`D^(3-theta)` when the balanced raw axes have length `D`; the
short-row norms here do not control it. A source-faithful joint
estimate for those two corrected columns and the retained outer
signed auxiliary sum is still required. The fixed-ray cube law of
PR #922 supplies exact finite coefficient closure; it does not by
itself provide this missing cancellation or absorb the moving
principal primes into a fixed bad modulus.
