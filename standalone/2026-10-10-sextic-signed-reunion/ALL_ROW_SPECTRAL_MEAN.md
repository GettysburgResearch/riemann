# The canonical spectral conductor mean includes every element row

**Status:** proposed source-conditional extension of the canonical Gauss-series mean in PR #922. The squarefree-row restriction can be removed without changing the sufficient strict threshold Re(u)>5/8. This does not by itself extend PR #922's entire second-reflection cusp identity to arbitrary rows, or estimate an original inverse moment.

**Authorship:** spectral_descent_attack. This is a new composition, requiring independent review at its frozen source.

**Exact sources:**

- PR #922 mathematical source `8f2acaacddc10bd8fb053a66070a1d06d25aa922` (validation-only head `f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32`), `standalone/2026-10-10-signed-covariance-descent/SPECTRAL_ROW_MEAN.md`, Git blob `bb4f6d8948a3e0ccd0f690e7380c1a71d20cf223`, SHA-256 `5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1`: the canonical series, completed block normalization and Mellin reconstruction. Its squarefree theorem is extended below by a different classical block input.
- The same source, `FULL_CUSP_DESCENT.md`, Git blob `85f28db785765668411f741492309df389a7a19a`, SHA-256 `b025af8af1ac13d07a04fbc7de71401d2a47ef2c8df5a1e89a4edc4973482504`: used only to specify what this extension does not automatically identify.
- PR #913 `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md`, SHA-256 `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8`, Theorem 3.4.
- The separately proved `MOVING_COLUMN_MASKS.md`, SHA-256 `068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee`, with the scalar exponent beta=1, is used for the direct moving-original-exclusion corollary in Section 5. That specialization uses counting in the scalar step and introduces no angular zero-free premise.
- Imported OpenAI/math source `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `build/paper2.tex`, SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`, equations `eq:T`, `eq:completed-twist`, and Proposition `prop:R`. The latter explicitly sums all nonzero element rows. Its analytic proof remains an assumed source-qualified input here.

The classical input ultimately uses the primary squarefree-order sieve of Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*, Theorem 1.3, https://arxiv.org/abs/1112.1650. Its all-row extension retains every sixth-power zero through the frozen coefficient mask. No GRH-conditional dispersion result is imported.

## 1. Exact canonical family

Keep the Eisenstein field, fixed bad set S, primary generators, and fixed finite ray character xi of the sources. Write

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n).
\]

For a squarefree primary d outside S and an arbitrary nonzero element k, define initially on Re(u)>1

\[
G_{k,d}(u)=\sum_{(n,S)=1}^{*}
\frac{a_\xi(n)\chi_n(k)\chi_n(d)^4}{(Nn)^u}.
\tag{1.1}
\]

Every symbol keeps its literal nonunit zero. Put F=Nd. The exact cube completion is

\[
\mathcal T_{k,d}(u)=G_{k,d}(u)
L_{S,kd}\!\left(3u-\tfrac12,
\overline\alpha^{\,3}\xi^3\chi_k^3\right).
\tag{1.2}
\]

The cube-index convention is \(\chi_k^3(b)=\chi_b(k)^3\). It denotes the reciprocal primary convention, with the actual row zeros included. The subscript S,kd deletes all primes in that set. The d deletion in the cube factor is exact because \(\chi_b(d)^{12}=\mathbf1_{(b,d)=1}\).

For H>=1 let \(\mathcal K_H\) be any subset of the nonzero elements with \(H\le Nk<2H\). One may keep all elements, any fixed unit class, any coprimality condition, or a smaller subset. The constants below are uniform in the subset, because both row estimates being used are nonnegative upper bounds for the full row set.

### Theorem 1.1

The functions in (1.1)–(1.2) continue holomorphically to Re(u)>1/2. Fix a closed strip

\[
\frac58<a_0\le a=\Re u\le a_1<1.
\]

For every epsilon>0, a finite M exists such that

\[
\boxed{
\sum_{k\in\mathcal K_H}|G_{k,d}(a+it)|^2
\ll H^{1+\epsilon}F^{1-a+\epsilon}(2+|t|)^M.}
\tag{1.3}
\]

The same bound holds for the completed family \(\mathcal T\). All nonzero element rows, including units, repeated primes and bad-prime powers, are covered. Constants are uniform over the fixed finite ray family. No zero-free theorem is used: the cube reciprocal is in its absolute Euler half-plane.

## 2. The two completed block bounds

For a smooth compactly supported W, with fixed compact support I in the positive reals, put

\[
\begin{split}
T_W(X;k,d)=X^{-1/2}
\sum_{(n,S)=1}^{*}\sum_{(b,dS)=1}
&a_\xi(n)\chi_n(k)\chi_n(d)^4
\overline{\alpha(b)}^{\,3}\xi(b)^3\chi_b(k)^3\sqrt{Nb}\\
&\hspace{20mm}\times W\left(\frac{Nn(Nb)^3}{X}\right).
\end{split}
\tag{2.1}
\]

The b indices are primary and unrestricted in their prime powers; there is no \((n,b)=1\) condition. This is exactly the imported completed sum with \(V_*(y)=\sqrt y W(y)\).

The imported Proposition R gives

\[
\sum_{k\in\mathcal K_H}|T_W(X;k,d)|^2
\ll (HFX)^\epsilon\|W\|_{C^J}^2
\left(H+\frac{H^2F}{X}\right),\qquad X\ge1.
\tag{2.2}
\]

To preserve its finite-seminorm and parameter quantifiers, choose the reference parameter \(D_* =\max(2,H,F,X)\) and its fixed scale ceiling C0=1. The proposition's all-element row sum covers our annulus after a fixed enlargement. A subset restriction is legitimate only after the absolute square. Thus J is independent of H,F,X. No reduction of k to a primitive row is being made.

The refined all-row sieve supplies the second bound

\[
\sum_{k\in\mathcal K_H}|T_W(X;k,d)|^2
\ll (HX)^\epsilon\|W\|_\infty^2
\left[H+H^{1/6}X+(HX)^{2/3}\right].
\tag{2.3}
\]

To prove it, freeze b and write \(L_b=X/(Nb)^3\). The squarefree n sum normalized by \(L_b^{-1/2}\) has bounded squared coefficient mass. Its coefficient includes \(\chi_n(d)^4\), so the sieve constant is independent of d. The all-row estimate is

\[
H+H^{1/6}L_b+(HL_b)^{2/3}.
\]

The completion is the sum of these normalized blocks with weights 1/Nb and bounded row multipliers. Weighted Cauchy uses the finite harmonic sum over \(Nb\ll_I X^{1/3}\). The three resulting sums are bounded by

\[
H\log(2X),\qquad
H^{1/6}X\sum_b(Nb)^{-4},\qquad
(HX)^{2/3}\sum_b(Nb)^{-3}.
\]

The last two converge. Empty child lengths are omitted and nonempty lengths below one lie in a fixed compact positive interval, which changes only support constants. Absorbing the harmonic losses proves (2.3). This calculation keeps the sixth-power row cost explicitly; it does not enlarge a squarefree-row theorem without an adapter.

## 3. Mellin reconstruction and normal convergence

Take a fixed smooth dyadic partition \(W_0\) on positive norms, allowing a separate fixed initial cutoff. For X=2^j put \(W_u(y)=y^{-u}W_0(y)\). On fixed real strips its finite seminorms are bounded by a fixed polynomial in \(2+|\Im u|\).

Absolute convergence on Re(u)>1 gives the termwise exact identity

\[
\mathcal T_{k,d}(u)=\sum_{j\ge0}X^{1/2-u}T_{W_u}(X;k,d).
\tag{3.1}
\]

The coefficient reconstructed by (3.1) is
\((Nn(Nb)^3)^{-u}\sqrt{Nb}\), so its cube Dirichlet exponent is precisely 3u-1/2.

For fixed H,F the row Hilbert space is finite-dimensional. Bound (2.2) and Minkowski imply locally normal convergence of (3.1) in that space throughout Re(u)>1/2, after choosing the preliminary loss below the compact set's distance from the boundary. Each dyadic block is entire and finite, so (3.1) gives a holomorphic continuation of the completed family. For any given nonzero k, choose an annulus containing it to obtain the individual continuation.

On strict interior strips in this half-plane,

\[
L_{S,kd}\!\left(3u-\tfrac12,
\overline\alpha^{\,3}\xi^3\chi_k^3\right)^{-1}
\tag{3.2}
\]

is an absolutely convergent, nonzero Euler product, uniformly bounded in k,d and in the fixed ray family. Its absolute bound follows from \(\Re(3u-1/2)>1\) and comparison with the ideal Euler product for \(1+(Np)^{-1-\delta}\). Dividing (3.1) by the cube L-factor therefore continues G without any zero-free assumption. Literal omitted-prime factors remain omitted in both the product and its reciprocal.

## 4. The all-row conductor calculation

For \(1/2<a<1\), combine (2.2) and (2.3). Distributing the minima gives

\[
\begin{split}
\mathcal B(H,F,X)
&=\min\left(H+H^{1/6}X+(HX)^{2/3},\ H+H^2F/X\right)\\
&\le H+\min(H^{1/6}X,H^2F/X)
+\min((HX)^{2/3},H^2F/X).
\end{split}
\tag{4.1}
\]

The base term in the Mellin norm is summable and costs \(O(H^{1/2})\). For the first minimum, the crossover is now

\[
X_1=H^{11/12}F^{1/2}.
\tag{4.2}
\]

Below that scale the norm contribution is \(H^{1/12}X^{1-a}\), and above it the contribution is \(HF^{1/2}X^{-a}\). Both geometric sums are dominated by the crossover, giving

\[
H^{1-11a/12}F^{(1-a)/2}.
\tag{4.3}
\]

This is the only change forced by the all-row sixth-power term.

The second crossover is unchanged:

\[
X_2=H^{4/5}F^{3/5}.
\tag{4.4}
\]

For a<5/6 its contribution is

\[
H^{1-4a/5}F^{1/2-3a/5}.
\tag{4.5}
\]

For a>5/6 the small-scale contribution is \(O(H^{1/3})\); the logarithm at a=5/6 is absorbed by a small power. Uniformly across a closed strip containing 5/6, the sum of (4.5) and \(H^{1/3}\), with a factor \(\log(2HF)\), is a valid bound without a singular constant.

For a>5/8,

\[
1-\frac{11a}{12}<\frac12,
\qquad
1-\frac{4a}{5}<\frac12,
\qquad
\frac12-\frac{3a}{5}\le\frac{1-a}{2}.
\tag{4.6}
\]

The first inequality already holds for a>6/11, below 5/8. Hence every norm term is bounded by \(H^{1/2}F^{(1-a)/2}\), up to subpowers and the vertical polynomial. The strict margin above 5/8 absorbs preliminary losses in the block estimates. Squaring proves (1.3), and (3.2) gives the same bound for G. □

The unchanged threshold is a useful feature: including all element rows creates an additional cost, but it does not become the dominant spectral obstruction. The quadratic–cubic cross term remains the one that forces 5/8 by this method.

## 5. Direct corollary with the original-column exclusion

Let q0 be a fixed moving squarefree good ideal and define

\[
G_{k,d;q_0}(u)=\sum_{(n,Sq_0)=1}^{*}
\frac{a_\xi(n)\chi_n(k)\chi_n(d)^4}{(Nn)^u}.
\tag{5.1}
\]

Its cube completion deletes q0 from the cube index as well. The proved `MOVING_COLUMN_MASKS.md` supplies, uniformly in polynomially bounded q0,d,

\[
\sum_{k\asymp H}|T_{q_0,W}(X;k,d)|^2
\ll D^\epsilon\|W\|_{C^J}^2
\left(H+\frac{H^2J_0}{X}\right),
\quad
J_0=Nd\,N\!\left(q_0/(q_0,d)\right).
\tag{5.2}
\]

Consequently (5.1) and its cube completion continue holomorphically to Re(u)>1/2 and obey

\[
\boxed{
\sum_{k\in\mathcal K_H}|G_{k,d;q_0}(a+it)|^2
\ll H^{1+\epsilon}J_0^{1-a+\epsilon}(2+|t|)^M,
\qquad 5/8<a_0\le a\le a_1<1.}
\tag{5.3}
\]

Every element row and every overlap among k,d,q0 is included. The classical block bound is unchanged, since the new exclusion is a row-independent coefficient mask. The exact cube reciprocal is now over primes outside S,k,d,q0.

To obtain (5.2), use that local note's Theorem 1.1 with beta=1. Choose outer scale A=1 and a fixed smooth outer test supported in a sufficiently small interval about one, taking value one at one, so the only outer primary ideal is a=1. The resulting two-axis completion is exactly the one-variable completion of (5.1), including deletion of q0 from its cube index. Its costs are \((1,J_0,K_0)\), where

\[
K_0=(Nd)^{2/3}N(q_0/(q_0,d))^{1/3}\le J_0^{2/3}.
\]

The bound becomes

\[
H+H^2J_0/X+K_0(H^2/X)^{2/3}
\ll H+H^2J_0/X,
\]

because \(t^{2/3}\le1+t\) and H>=1. Choose the reference parameter to dominate H,J0,X; it also dominates Nd and Nq0. The resulting finite-seminorm and small-power quantifiers are therefore exactly those needed in Sections 2–4. Replacing F there by J0 proves (5.3).

The beta=1 specialization invokes counting for each scalar Möbius sum. It retains the named imported theta identities and classical upper sieves but no zero-free estimate or higher inverse moment. The corollary is obtained from the local adapter at the physical row height H, not by applying a row mean at the artificially enlarged height H(Nq0)^6.

## 6. What remains open

The source formula for the entire reunited second-reflection object in PR #922 was derived with its specified squarefree row factors. The present theorem changes the row mean of the canonical G family. An identity identifying every arbitrary-row reflected coefficient with that family, with all local amplitudes summed, is still required before extending that full-cusp composition wholesale.

The all-row mean does not improve the 5/8 threshold and does not supply a new spectral scalar exponent. More importantly, neither G nor its cube completion is the original Möbius inverse polynomial. The signed long-range covariance, the exact centered product-column subtraction, and the generalized moment remain open.
