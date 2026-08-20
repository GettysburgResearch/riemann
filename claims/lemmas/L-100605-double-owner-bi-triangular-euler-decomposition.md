# L-100605 — First-owner and largest-prime decompositions are opposite triangularizations of the same Euler source

Claim ID: `L-100605`
Status: **PROVED EXACT FINITE COEFFICIENT DECOMPOSITION; MIDDLE-BLOCK ESTIMATE OPEN**
Depends on: PR #652 `L-99601`; PR #688 `L-100410`
RH status: **not assumed**

Fix a finite ordered prime set

\[
p_1<\cdots<p_k
\]
and a squarefree subset `A`. If `A` is nonempty, it has both a least selected index

\[
i_-(A)=\min A
\]
and a greatest selected index

\[
i_+(A)=\max A.
\]

The sequential first-owner identity of PR #652 partitions every nonempty Euler monomial according to `i_-(A)`. The largest-prime identity of PR #688 partitions the same monomial according to `i_+(A)`.

Therefore the complete nonempty native Euler source admits the exact double-owner refinement

\[
\boxed{
\sum_{\emptyset\ne A\subseteq[k]}
(-1)^{|A|}r_AU_A
=
\sum_{1\le i\le j\le k}\mathcal D_{i,j},
}
\]
where `D_(i,j)` is the sum of precisely those monomials with

\[
i_-(A)=i,\qquad i_+(A)=j.
\]

For `i=j`, the block is the singleton monomial `-r_iU_i`. For `i<j`, factor the endpoints:

\[
\boxed{
\mathcal D_{i,j}
=r_ir_jU_iU_j
\prod_{i<h<j}(I-r_hU_h),
}
\]
with sign determined by the two endpoint selections and the interior Euler product. More explicitly, expanding the interior product yields exactly all subsets whose least and greatest selected indices are `i,j`, each once with its native coefficient.

Thus the two one-sided decompositions combine into a **bi-triangular interval decomposition**: all unknown future/past complexity is confined to the finite prime interval `(p_i,p_j)`.

## Why this is new leverage

- first-owner alone leaves an arbitrary future Euler profile;
- largest-prime alone leaves an arbitrary past/cofactor Möbius profile;
- together they leave only an **interior interval Euler product** between two explicit endpoint primes.

After compact wavelet projection, support `X/8<=n<=X` forces

\[
p_ip_j\,m_{i,j}\asymp X
\]
with every prime factor of `m_(i,j)` lying strictly between `p_i` and `p_j`.

This creates a natural three-region matrix:

1. short prime intervals `p_j/p_i <= 8`: the interior product is constrained by wavelet support and admits direct finite-band treatment;
2. long intervals: finite squaring may be applied to the interior primes without touching either endpoint owner;
3. diagonal singleton blocks: explicit one-prime terms.

The remaining theorem `DOBI100605` is a subpower logarithmic estimate for the projected sum of the double-owner blocks. It is strictly more localized than either `FCHD67` or the largest-prime rough bilinear alone.
