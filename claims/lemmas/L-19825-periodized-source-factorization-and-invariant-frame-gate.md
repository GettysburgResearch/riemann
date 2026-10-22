# L-19825 — Periodized source factorization, multiplicity obstruction, and the invariant frame gate

Claim ID: `L-19825`  
Status: **PROVED EXACT FACTORIZATION AND NECESSARY-GATE CORRECTION; POSITIVE FRAME CONSTRUCTION OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: Connes--Consani scale-invariant periodization; Mellin factorization `L-16205`; signed gap `L-19823`; Rayleigh transfer `T-19808`  
Scope: adversarial correction to the requested quantitative signed source-frame theorem

## 1. Purpose

The review requested a theorem of the form

\[
 \sigma_{\min}\!\left(
 P_{N_\lambda}\Sigma_\mu E
 \bigm|_{\mathcal U_{\lambda,+}\oplus\mathcal U_{\lambda,-}}
 \right)
 \ge (\log\lambda)^{-C}.
 \tag{L-19825.1}
\]

There are two separate issues with treating (L-19825.1) as the exact remaining
analytic gate.

1. A singular value is meaningless until a domain metric is fixed.
2. In the natural Mellin-sampling coordinates, the periodized source map has an
   exact diagonal zeta multiplier. A fixed polylogarithmic lower bound therefore
   contains nontrivial information about small values and multiplicities of
   critical-line zeros.

This lemma proves both statements and derives the weaker invariant gate that the
signed `d_4/d_6` ground-state transfer actually needs.

## 2. Exact Fourier factorization of the periodized map

Let

\[
 L=\log\mu=2\log\lambda,
 \qquad
 C_L=\mathbb R/L\mathbb Z,
\]

and use the orthonormal Fourier characters

\[
 e_k(x)=L^{-1/2}e^{2\pi ikx/L},
 \qquad
 t_k={2\pi k\over L}.
 \tag{L-19825.2}
\]

For an even source `f` satisfying the two Connes--Consani cancellations, put

\[
 M_f(t)=\int_0^\infty f(x)x^{-1/2-it}\,dx.
 \tag{L-19825.3}
\]

The scale-invariant periodization has Fourier coefficients equal to the
multiplicative Fourier transform of `E(f)` at the circle frequencies. Hence
`L-16205` gives the exact identity

\[
 \boxed{
 \langle\Sigma_\mu E(f),e_k\rangle_{L^2(C_L)}
 =L^{-1/2}
  \zeta\!\left({1\over2}-it_k\right)M_f(t_k).}
 \tag{L-19825.4}
\]

Let

\[
 J_L:\mathbb C^m\longrightarrow\mathcal S_0^{\rm ev}
 \tag{L-19825.5}
\]

be any finite source synthesis and let the finite Fourier cutoff contain rows
`k in K_L`. Define

\[
 (\mathcal M_L)_{kj}
 =L^{-1/2}M_{J_Le_j}(t_k),
 \qquad
 (D_{\zeta,L})_{kk}
 =\zeta\!\left({1\over2}-it_k\right).
 \tag{L-19825.6}
\]

Then

\[
 \boxed{
 P_{K_L}\Sigma_\mu E J_L
 =D_{\zeta,L}\mathcal M_L.}
 \tag{L-19825.7}
\]

No approximation, RH assumption, or asymptotic theorem enters (L-19825.7).

## 3. Exact cycles and near cycles

Equation (L-19825.7) immediately recovers the exact zeta-cycle obstruction: if

\[
 \zeta\!\left({1\over2}-it_k\right)=0,
\]

then the `k`-th output row vanishes for every source. Avoiding these exact
lengths makes the diagonal multiplier nonzero on a finite cutoff, but gives no
quantitative lower bound on its smallest entry.

This proves directly, without a determinant argument, why deletion of the
countable exact exceptional set is not a conditioning theorem.

## 4. Singular values depend on the source metric

Replace the synthesis `J_L` by

\[
 \widetilde J_L=J_LA_L,
 \qquad A_L\in GL_m(\mathbb C).
\]

The source range is unchanged, but

\[
 P_{K_L}\Sigma_\mu E\widetilde J_L
 =D_{\zeta,L}\mathcal M_LA_L.
 \tag{L-19825.8}
\]

Taking `A_L=cI` makes every Euclidean singular value larger or smaller by the
arbitrary factor `|c|`. Therefore the bare expression in (L-19825.1) is not an
invariant theorem. One must declare a source norm or, equivalently, a source
Gram `G_{\rm src,L}`.

The invariant quantity is the smallest generalized singular value relative to
that Gram and the declared finite-space metric.

## 5. Hidden zero-multiplicity content of a fixed polylogarithmic floor

Assume a natural source metric for which the Mellin sampling rows satisfy

\[
 \|e_k^*\mathcal M_L\|_2\le L^A
 \tag{L-19825.9}
\]

uniformly on the growing packet. Let

\[
 \rho={1\over2}+i\gamma
\]

be a critical-line zero of multiplicity `m`. For every sufficiently large `L`,
choose the nearest integer `k(L)` to `gamma L/(2pi)`. Then

\[
 |t_{k(L)}-\gamma|\le {\pi\over L}.
 \tag{L-19825.10}
\]

The quadratic-log cutoff contains this row eventually. Taylor's theorem at the
zero gives a constant `C_rho` such that

\[
 \left|
 \zeta\!\left({1\over2}+it_{k(L)}\right)
 \right|
 \le C_\rho L^{-m}.
 \tag{L-19825.11}
\]

For a square full-row source frame,

\[
 \sigma_{\min}(T_L)
 =\sigma_{\min}(T_L^*)
 \le\|T_L^*e_{k(L)}\|_2.
\]

Using (L-19825.7), (L-19825.9), and (L-19825.11),

\[
 \boxed{
 \sigma_{\min}(T_L)
 \le C_\rho L^{A-m}.}
 \tag{L-19825.12}
\]

Consequently, a uniform theorem

\[
 \sigma_{\min}(T_L)\ge cL^{-C}
 \tag{L-19825.13}
\]

with fixed `A,C` would imply

\[
 \boxed{m(\rho)\le A+C}
 \tag{L-19825.14}
\]

for every critical-line zero. It would also require quantitative control of the
first nonzero Taylor coefficient when `m=A+C`.

Thus the full periodized polylog frame is not merely a PSWF determinant estimate.
It contains a uniform critical-line zero-multiplicity/small-value statement.
This does not show that (L-19825.13) is false. It shows that it cannot be treated
as a routine consequence of generic support or abstract source density.

## 6. The invariant loss actually used by the RH transfer

Let `H_R` be the ordinary finite-space metric and `M_R` the moving-Hardy metric.
Define the metric inflation

\[
 K_R
 :=\inf\{K>0:M_R\preceq K H_R\}.
 \tag{L-19825.15}
\]

The signed Rayleigh transfer in `T-19808` uses the source frame only through
`K_R`. If the arithmetic target and complete complement have scales `d_4` and
`d_6`, the exact required condition is

\[
 \boxed{
 K_R{d_4(R)\over d_6(R)}\longrightarrow0.}
 \tag{L-19825.16}
\]

Indeed, the target-to-ground error is bounded by

\[
 t_R+C\sqrt{
 K_R{\mu_A(R)-L_R\over g_R}}
\]

and the quotient in the square root is `O(d_4/d_6)+o(1)`.

For fixed prolate modes, Fuchs gives

\[
 {d_4(R)\over d_6(R)}=\Theta(R^{-2}).
 \tag{L-19825.17}
\]

Hence the sufficient invariant gate is only

\[
 \boxed{K_R=o(R^2).}
 \tag{L-19825.18}
\]

A polylogarithmic frame gives (L-19825.18), but is much stronger than necessary.
For example, if the source-to-finite-space inverse enters quadratically and all
other source metric constants are polylogarithmic, even

\[
 \|T_R^{-1}\|=o(R)
 \tag{L-19825.19}
\]

is sufficient.

## 7. Nonresonant/resonant decomposition

For any chosen threshold `tau_R>0`, define the Fourier rows

\[
 \mathcal K_R^{\rm nr}
 =\left\{k:
 \left|\zeta\!\left({1\over2}-it_k\right)\right|
 \ge\tau_R\right\},
 \qquad
 \mathcal K_R^{\rm res}=\mathcal K_R\setminus\mathcal K_R^{\rm nr}.
 \tag{L-19825.20}
\]

On the nonresonant rows, (L-19825.7) gives the exact lower comparison

\[
 \|D_{\zeta,L}y\|\ge\tau_R\|y\|.
 \tag{L-19825.21}
\]

Thus any quantitative Mellin-frame theorem immediately yields a source-frame
floor on the nonresonant quotient. All genuinely zeta-sensitive conditioning is
confined to the finite resonant row block. A viable correction may therefore:

1. prove the invariant loss gate directly without Euclidean periodized
   conditioning;
2. split off the resonant block and control it by a positive critical-line
   evaluation/deflation theorem;
3. use a different exact localized source realization whose metric loss still
   satisfies (L-19825.16).

This decomposition is exact. No claim is made here that the resonant block has
already been controlled.

## 8. Consequence for the review frontier

The review is right that qualitative surjectivity is insufficient. It is not
right to identify the unqualified Euclidean bound (L-19825.1) as the unique
minimal theorem.

The precise remaining source statement is:

```text
construct a complete signed prolate-adapted source/image realization whose
moving-Hardy metric inflation K_R satisfies K_R d_4/d_6 -> 0,
including any resonant critical-line block.
```

The full periodized polylog singular-value theorem is one strong sufficient
solution, but it carries the additional content exposed in Section 5.

## 9. Proof boundary

- The Fourier factorization, metric-dependence observation, multiplicity upper
  obstruction, and invariant loss gate are proved.
- No lower bound for the resonant periodized source block is proved.
- No RH conclusion follows from this lemma alone.
