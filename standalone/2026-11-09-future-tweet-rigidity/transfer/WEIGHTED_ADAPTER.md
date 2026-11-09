# The exact weighted bridge, and the cost of separating it

**Status:** proved finite identities; an imported prime-field bilinear theorem;
an explicit sufficient condition that is not proved for the repository's native
arithmetic coefficients. No new zero-free region is claimed.

**Scope:** completion of a local affine sextic correlation, with all signs,
nonunit masks, and exceptional axes retained. This note isolates the additional
information needed to use the hypergeometric identification in
[`../coupled/LOCAL_KERNEL.md`](../coupled/LOCAL_KERNEL.md).

**Dependencies:** ordinary finite Fourier inversion and Plancherel; FKMS,
*Bilinear forms with trace functions*, arXiv:2511.09459v2, Theorems 1.1/9.1
and Section 9.6. The exact arithmetic target is the repository's
[#1022 fourth-pass transfer](https://github.com/GettysburgResearch/riemann/blob/8b2c6d50ad2d729c681745717c615095bd8f1d9d/standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/OFF_DIAGONAL_TRANSFER.md).

**Smallest gap:** control the joint completed arithmetic weight on rectangles
where the prime-field theorem applies, including the cost of passing from the
integer/Eisenstein source to these rectangles. Neither a pointwise trace bound
nor a bound on its Frobenius norm supplies this control.

## 1. Completion without changing the coefficients

Let q be an odd prime with q = 1 modulo 6, let chi be a character of exact order
six on F_q^*, extend chi by zero, and put psi(x) = exp(2 pi i x/q). All norms
below use counting measure. Define

\[
 S_\chi(z)=\sum_y\chi(y)\overline{\chi(y-1)}\psi(zy),
 \qquad K_\chi(z)=q^{-1/2}S_\chi(z).
\]

The companion note identifies this normalized kernel, up to a scalar of modulus
one, with a rank-two hypergeometric trace function. For arbitrary complex
functions f,g,w on F_q, set

\[
 F_h(x)=f(x)\overline{g(x-h)},\quad
 \widehat F_h(t)=\sum_x F_h(x)\psi(-tx),
\]

\[
 \mathcal S_w(f,g)=\sum_{h,x}w(h)F_h(x)
             \chi(x)\overline{\chi(x-h)}.
\]

Then the following identity is exact:

\[
\boxed{
\begin{aligned}
\mathcal S_w(f,g)
={}&w(0)\sum_{x\ne0}f(x)\overline{g(x)}\\
&-q^{-1}\sum_{h\ne0}w(h)\widehat F_h(0)\\
&+q^{-1/2}\sum_{h\ne0,t\ne0}
          w(h)\widehat F_h(t)K_\chi(ht).
\end{aligned}}
\tag{1}
\]

**Proof.** Fourier inversion gives the contribution of a fixed h as
q^(-1) sum_t Fhat_h(t) T_chi(h,t), where

\[
 T_\chi(h,t)=\sum_x\chi(x)\overline{\chi(x-h)}\psi(tx).
\]

For h nonzero, x = hy gives T_chi(h,t) = S_chi(ht). At t = 0 this equals -1:
the map y -> y/(y-1) maps F_q minus {1} bijectively to F_q minus {1}, and the
nontrivial character sums to zero on the full field. At h = 0 the character
product is the indicator of x nonzero; this entire axis contributes the first
line of (1). Separating t = 0 from h nonzero proves the formula. In particular,
the h = 0 axis is not interchangeable with the t = 0 axis. QED.

### Affine coefficients

If A and B are nonzero in F_q, the weighted affine correlation

\[
 \sum_{p,b}w(Ap-Bb)f(p)\overline{g(b)}
                    \chi(Ap)\overline{\chi(Bb)}
\tag{2}
\]

is (1) with f replaced by x -> f(A^(-1)x) and g by
y -> g(B^(-1)y). This is a reindexing, not an estimate. If either A or B is
zero, (2) vanishes under the stated zero extension; this fact does not justify
removing other bad-prime or gcd terms in a different arithmetic model.

Folding an integer sum into residue classes is also exact, but the folded
functions must contain their original arithmetic coefficients. In the #1022
source those include prime restrictions, four Mobius signs, smooth cutoffs,
coprimality conditions, and a sum over affine parameters. Some weights couple
the two variables; such a term is represented by a general F(h,x), rather
than by one factored f(x) conjugate(g(x-h)). Fourier completion still holds
for that general F, but the product-norm bound in the next section does not.
Equation (1) is a local adapter for a factored block, not an assertion that
the whole native source has already been factored or bounded.

## 2. What the automatic energy estimate actually controls

For the factored F above, finite Plancherel gives the exact Moyal identity

\[
 \sum_{h,t}|\widehat F_h(t)|^2
       =q\|f\|_2^2\|g\|_2^2.
\tag{3}
\]

Indeed, for each h the t sum is q sum_x |f(x)|^2 |g(x-h)|^2;
summing h proves (3). Thus W(h,t) = w(h) Fhat_h(t) satisfies

\[
 \|W\|_{\mathrm F}
 \le \sqrt q\,\|w\|_\infty\|f\|_2\|g\|_2.
\tag{4}
\]

Restriction to any rectangle only decreases this Frobenius norm. This is an
energy budget. It does not measure how cheaply the h and t variables separate.

## 3. The precise sufficient condition for using FKMS

Fix delta > 0. For intervals h ~ M, t ~ N contained in F_q^*, suppose

\[
 1\le M,N\le q/2,\qquad M\ge q^\delta,
 \qquad MN\ge q^{3/4+\delta}.
\tag{5}
\]

The FKMS theorem, specialized to the companion note's rank-two sheaf and
b = c = 1, supplies eta > 0 with

\[
 \left|\sum_{h\sim M,t\sim N}\alpha_h\beta_tK_\chi(ht)\right|
 \le C_\delta(MN)^{1/2-\eta}\|\alpha\|_2\|\beta\|_2.
\tag{6}
\]

The saving is (MN)^(-eta), exactly as in Theorem 1.1. The exponent and implied
constant depend on delta and the bounded sheaf complexity; this is a
prime-modulus statement. A fixed scalar of modulus one in the identification
of K does not change it. The source does not give a usable polynomial
dependence on arbitrary growing complexity (Remark 1.2).

For an arbitrary complex matrix W on this rectangle, let

\[
 \nu(W)=\inf_{W(h,t)=\sum_j\alpha_j(h)\beta_j(t)}
                    \sum_j\|\alpha_j\|_2\|\beta_j\|_2.
\]

This projective norm equals the usual nuclear norm ||W||_*: use the singular
value decomposition with the conjugation absorbed in beta, and duality with
the operator norm for the reverse inequality. Applying (6) to every summand
and taking the infimum gives the rigorous extension

\[
 \left|\sum_{h,t}W(h,t)K_\chi(ht)\right|
 \le C_\delta(MN)^{1/2-\eta}\|W\|_*.
\tag{7}
\]

Consequently the corresponding contribution to the last line of (1) is at
most q^(-1/2) times the right side of (7). For a target saving (MN)^(-epsilon)
relative to the generic scale (MN)^(1/2) ||W||_F, a sufficient condition is

\[
 \boxed{\quad
 \frac{\|W\|_*}{\|W\|_{\mathrm F}}
       \le (MN)^{\eta-\epsilon},\qquad 0<\epsilon<\eta.
 \quad}
\tag{8}
\]

The zero matrix is harmless and omitted from this ratio. Since
||W||_* <= sqrt(rank W) ||W||_F, a suitable rank bound also suffices.
There is no assertion that (8) holds for the Mobius/prime source. Moreover,
(8) is sufficient, not necessary: a coefficient supported on a curve might
instead admit a separate one-variable trace-function argument.

## 4. A sharp warning, even for a same-vector correlation

Take c nonzero, w = 1, and

\[
 f(x)=g(x)=\psi(cx^2).
\]

Although the two coefficient vectors agree exactly, completion gives

\[
 \widehat F_h(t)
 =q\psi(-ch^2)\,\mathbf 1_{t=2ch}.
\tag{9}
\]

This follows by expanding x^2 - (x-h)^2 = 2hx - h^2 and summing an additive
character. Thus the complete q by q weight is a phase-weighted permutation
matrix with every singular value equal to q. On h,t nonzero the size is q-1
and all q-1 singular values are still q. In particular,

\[
 \frac{\|W\|_*}{\|W\|_{\mathrm F}}=\sqrt{q-1}
 \quad\text{on }(\mathbb F_q^*)^2.
\tag{10}
\]

The obstruction is not restricted to the full field. For c = 1, take
h in (M,2M], t in (2M,4M], with 4M < q. The restricted weight has M orthogonal
nonzero rows, all of norm q, and the ratio is sqrt(M). Taking M a fixed
fraction below q/4 puts these rectangles in the size regime (5) for any
fixed sufficiently small delta and large q. Therefore product structure
before completion, a same-vector origin, and an L2 energy bound do not force
the small separation cost needed by this particular use of (6).

This is not a counterexample involving Mobius, nor a counterexample to a
bound proved directly on the curve t = 2ch. It rules out the proposed
generic inference from (3) to cheap bilinear separation. A successful native
argument must use more arithmetic information or a different estimate.

## 5. A concrete next theorem to try

Starting from the frozen #1022 source, retain its exact lambda coefficient
(a truncated Mobius convolution, not a single Mobius function). Isolate good
prime blocks, keep the complete sixth-power-core resonances and both axes,
and derive the actual W(h,t). Then prove either:

1. a decomposition into rectangles satisfying (5), with a total nuclear-norm
   cost small enough for (7) to beat the full transfer budget; or
2. an estimate that exploits the geometric support/correlation of W directly,
   without replacing it by arbitrary product weights.

The resulting estimates must be summed over all affine parameters and shifts,
with the original one-sided sign and the factor D log U restored. A fixed-h
saving, the local frame inequality, or a factored toy weight alone does not
complete this step.

## Verification

From the package root:

```sh
python transfer/check_weighted_adapter.py --output transfer/CHECKS.json
```

The checker uses integer arithmetic in Q(zeta_6,zeta_q), imported from the
companion finite-field checker. It independently compares the direct affine
sum with the completed, axis-separated expression for signed complex
coefficients; verifies the energy identity with distinct f and g; and checks
the chirp support formula exactly. These checks detect normalization and
mask mistakes at the stated finite primes. The proofs above establish the
identities in general; computation does not prove the imported analytic
theorem or condition (8) for the native source.
