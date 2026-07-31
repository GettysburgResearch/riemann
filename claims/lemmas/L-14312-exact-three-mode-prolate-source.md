# L-14312 — Exact three-mode prolate source repair and Schwartzification

Claim ID: L-14312  
Title: Three same-sign prolate modes are the minimal exact codimension-two source packet  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: unitary Fourier transform; standard density of `C_c^infinity`; the Connes--Consani `S_0^ev -> radical(QW)` interface  
Scope: source-space repair for the positive prolate/Weil routes in PRs #150 and #152  
Related counterexample candidates: none

## Source audit

The exact global source space used by Connes--Consani is the codimension-two
space

\[
 \mathcal S_0^{\rm ev}
 =\left\{f\in\mathcal S(\mathbb R):
 f\text{ real and even},\ f(0)=0,\ \widehat f(0)=\int_{\mathbb R}f=0\right\}.
 \tag{L-14312.1}
\]

For `f` in this space the arithmetic map

\[
 \mathcal E(f)(u)=u^{1/2}\sum_{n\geq1}f(nu)
 \tag{L-14312.2}
\]

belongs to the radical of the global Weil form, under the imported normalization.
The Poisson identity is

\[
 \mathcal E(\widehat f)(u)=\mathcal E(f)(u^{-1}).
 \tag{L-14312.3}
\]

By contrast, the explicit two-mode target in CCM equation (7.6) is defined by
choosing a linear combination of `h_(0,lambda)` and `h_(4,lambda)` with
vanishing integral. Vanishing at the origin is a second independent condition
at every finite `lambda`, because the concentration eigenvalues of the two
modes are distinct. Thus that two-mode target is not automatically the
truncation of an exact vector in the global radical.

This lemma gives a minimal algebraic repair and then removes the remaining
endpoint-regularity problem by exact Schwartz approximation.

## Statement

Let `F` be the unitary additive Fourier transform on `L2(R)`, normalized so
that `F^2` is reflection. Fix `lambda>0`, let `P_lambda` be multiplication by
`1_[-lambda,lambda]`, and suppose

\[
 p_0,p_1,p_2\in L^2(\mathbb R)
 \tag{L-14312.4}
\]

are real, even, orthonormal, supported in `[-lambda,lambda]`, continuous at the
origin, and satisfy

\[
 P_\lambda\mathcal Fp_j=\chi_jp_j,
 \qquad
 1\geq\chi_0>\chi_1>\chi_2>0.
 \tag{L-14312.5}
\]

Assume also

\[
 v_j:=p_j(0)\neq0.
 \tag{L-14312.6}
\]

Since zero belongs to the support interval,

\[
 m_j:=\int_{\mathbb R}p_j(x)\,dx
      =\widehat p_j(0)
      =\chi_jv_j.
 \tag{L-14312.7}
\]

### A. Two-mode obstruction

For any pair `j != k`, the only linear combination

\[
 ap_j+bp_k
\]

satisfying both value and integral constraints is the zero function. Indeed,
the determinant of its two constraint rows is

\[
 \det\begin{pmatrix}
 v_j&v_k\\
 \chi_jv_j&\chi_kv_k
 \end{pmatrix}
 =v_jv_k(\chi_k-\chi_j)\neq0.
 \tag{L-14312.8}
\]

Thus three modes are the minimum possible packet when the finite prolate
eigenvalues are distinct.

### B. Exact three-mode packet

Put

\[
 v=(v_0,v_1,v_2),
 \qquad
 m=(m_0,m_1,m_2),
 \qquad
 a=v\times m.
 \tag{L-14312.9}
\]

Explicitly,

\[
 \begin{aligned}
 a_0&=v_1v_2(\chi_2-\chi_1),\\
 a_1&=v_2v_0(\chi_0-\chi_2),\\
 a_2&=v_0v_1(\chi_1-\chi_0).
 \end{aligned}
 \tag{L-14312.10}
\]

Then `a` is nonzero. For

\[
 p=\frac{a_0p_0+a_1p_1+a_2p_2}{\|a\|_2}
 \tag{L-14312.11}
\]

one has exactly

\[
 \boxed{p(0)=0,\qquad\int_{\mathbb R}p(x)\,dx=0.}
 \tag{L-14312.12}
\]

Moreover,

\[
 \boxed{
 \|\mathcal Fp-p\|_2^2
 =2\frac{\sum_{j=0}^2a_j^2(1-\chi_j)}{\sum_{j=0}^2a_j^2}
 \leq2(1-\chi_2).}
 \tag{L-14312.13}
\]

### C. Exact Schwartzification without losing the leakage scale

For every `epsilon>0`, there exists a real even function

\[
 f_\epsilon\in C_c^\infty((-\lambda,\lambda))
 \subset\mathcal S(\mathbb R)
 \tag{L-14312.14}
\]

such that

\[
 \boxed{
 f_\epsilon(0)=0,
 \qquad
 \int f_\epsilon=0,
 \qquad
 \|f_\epsilon-p\|_2<\epsilon.}
 \tag{L-14312.15}
\]

Consequently,

\[
 \boxed{
 \|\mathcal Ff_\epsilon-f_\epsilon\|_2
 \leq\sqrt{2(1-\chi_2)}+2\epsilon.}
 \tag{L-14312.16}
\]

In particular `f_epsilon` belongs to the exact source space
`S_0^ev`. Under the imported Connes--Consani radical theorem,
`E(f_epsilon)` is therefore an exact global Weil-radical vector, not merely a
formal prolate approximation.

## Proof

Equation (L-14312.7) follows by evaluating the compressed Fourier eigenvalue
equation at zero. Formula (L-14312.8) proves the two-mode obstruction.

The vectors `v` and `m` are linearly independent: if `m=c v`, then every
nonzero coordinate would give `chi_j=c`, contradicting the strict ordering.
Hence `a=v cross m` is nonzero. Orthogonality of a cross product gives

\[
 a\cdot v=a\cdot m=0,
\]

which is exactly (L-14312.12).

Because the modes are orthonormal and supported in the range of `P_lambda`,

\[
 \langle\mathcal Fp_j,p_k\rangle
 =\langle P_\lambda\mathcal Fp_j,p_k\rangle
 =\chi_j\delta_{jk}.
 \tag{L-14312.17}
\]

The Fourier transform is unitary, so for the normalized packet

\[
 \begin{aligned}
 \|\mathcal Fp-p\|_2^2
 &=2-2\operatorname{Re}\langle\mathcal Fp,p\rangle\\
 &=2-2\frac{\sum_j a_j^2\chi_j}{\sum_j a_j^2},
 \end{aligned}
\]

which is (L-14312.13).

It remains to prove the exact smooth source statement. Choose a fixed real even
bump

\[
 b\in C_c^\infty((-\lambda,\lambda)\setminus\{0\}),
 \qquad
 \int b=1.
 \tag{L-14312.18}
\]

Since `p` is square integrable, supported in `[-lambda,lambda]`, and continuous
at zero with `p(0)=0`, real even smooth functions supported away from the
origin and the two endpoints are dense at `p` in `L2`. Thus for arbitrary
`delta>0` one may choose such a `g` with

\[
 g(0)=0,
 \qquad
 \|g-p\|_2<\delta.
 \tag{L-14312.19}
\]

Define

\[
 f=g-\left(\int g\right)b.
 \tag{L-14312.20}
\]

Then `f(0)=0` and `integral f=0` exactly. Since `integral p=0`,

\[
 \left|\int g\right|
 \leq\sqrt{2\lambda}\,\|g-p\|_2,
\]

and therefore

\[
 \|f-p\|_2
 \leq\delta\left(1+\sqrt{2\lambda}\|b\|_2\right).
 \tag{L-14312.21}
\]

Taking `delta` sufficiently small proves (L-14312.15). Finally, Fourier
unitarity and the triangle inequality give

\[
 \|\mathcal Ff-f\|_2
 \leq\|\mathcal Fp-p\|_2+2\|f-p\|_2,
\]

which proves (L-14312.16). QED.

## Prolate specialization

For the standard even prolate modes `h_(4j,lambda)`, fixed-index
Sturm--Liouville theory gives nonzero values at zero, and the concentration
eigenvalues are simple and strictly ordered. Thus the hypotheses apply to

\[
 p_j=h_{4j,\lambda},\qquad j=0,1,2.
\]

The natural finite packet is therefore the three-mode span

\[
 \operatorname{span}\{h_{0,\lambda},h_{4,\lambda},h_{8,\lambda}\},
 \tag{L-14312.22}
\]

with the first excluded same-sign mode `h_(12,lambda)` supplying the first
adjacent coercivity comparison. The two-mode CCM vector remains a valid
educated approximation to `Xi`; what fails without an extra argument is only
its promotion to an exact global radical source.

## Relation to the lower-floor route

`L-14309` transfers a localized residual to the discarded tail only when the
untruncated vector is genuinely radical. This lemma supplies exact radical
sources arbitrarily close in `L2` to the three-mode prolate packet. It does not,
by itself, prove the graph/form-norm continuity needed to transfer the small
Fourier leakage through the Weil form. That stronger continuity is isolated in
`L-14313`.

## Source and normalization audit

Primary interfaces used here:

1. Connes--Consani, *Spectral triples and zeta-cycles*, equations (1.3),
   (1.4), (3.1), (3.2), and Section 6.1: `S_0^ev` requires both `f(0)=0`
   and `integral f=0`, and `E(S_0^ev)` lies in the global radical.
2. Connes--Consani--Moscovici, *Zeta Spectral Triples*, equations (7.6),
   (7.12), and the identity `integral h_(n,lambda)=chi_n h_(n,lambda)(0)`:
   the explicit two-mode target imposes vanishing integral, while the finite
   prolate eigenvalues remain mode dependent.

The exact Fourier convention and the radical normalization remain imported
repository gates and are not promoted by this lemma.

## Gap audit

- No production prolate values or eigenvalue intervals are supplied.
- The Schwartzification is existential. A proof-producing implementation must
  freeze explicit bumps and directed approximation bounds.
- `L2` Fourier leakage alone does not control the unbounded Weil graph norm.
- The exact radical statement depends on the imported global source theorem.
- No lower spectral floor and no proof of RH are claimed.

## Adversarial tests

1. Mutate one `chi_j` so the strict ordering fails.
2. Set all three `chi_j` equal and require the cross product to vanish.
3. Verify both exact source constraints independently.
4. Recompute (L-14312.13) from the full Fourier inner-product matrix.
5. Smooth a discontinuous endpoint model, impose the two constraints by the
   one-bump correction, and verify arbitrarily small `L2` error.
6. Do not infer a Weil graph bound from (L-14312.16) alone.

## Immediate handoff

Construct directed prolate data for the modes `0,4,8,12`, form the exact
three-mode coefficient vector, and compare three separately reported scales:

```text
ordinary Fourier leakage,
Weil radical-tail cross-form norm,
first-excluded same-sign coercivity.
```

Only the second divided by the third enters the remaining lower-floor closure.
