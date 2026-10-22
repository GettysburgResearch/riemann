# L-19872 — Every finite real coefficient vector has a minimal real-rooted sign corrector

Claim ID: `L-19872`  
Status: **PROVED EXACT FINITE DARBOUX LEMMA**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: intermediate value theorem; `L-19871`  
Scope: constructive finite sign-groundification without a lowest-eigenvalue hypothesis  
Nonclaim: the corrected transforms are not proved to converge relatively to Xi

## 1. Statement

Let

\[
 d_1<d_2<\cdots<d_n
 \tag{L-19872.1}
\]

be real nodes, and let `c_1,...,c_n` be nonzero real numbers.  Define the sign
change set

\[
 S=\{j:1\le j<n,\ c_jc_{j+1}<0\}.
 \tag{L-19872.2}
\]

For each `j in S`, choose any

\[
 r_j\in(d_j,d_{j+1}).
 \tag{L-19872.3}
\]

Then there is a choice of global sign `sigma in {+1,-1}` for which

\[
 \boxed{
 M(s)=\sigma\prod_{j\in S}(s-r_j)
 }
 \tag{L-19872.4}
\]

satisfies

\[
 \boxed{M(d_k)c_k>0\qquad(1\le k\le n).}
 \tag{L-19872.5}
\]

Moreover `deg M=|S|` is minimal among all real polynomials `P` satisfying
`P(d_k)c_k` of one strict sign.

Thus, after the centered Fourier rephasing

\[
 c_k=(-1)^ka_k,
 \tag{L-19872.6}
\]

every finite real Fourier coefficient vector with no zero coordinates admits an
explicit real-rooted multiplier whose corrected vector has one sign.  By
`L-19871`, that corrected finite vector has an explicit positive CCM completion
and a transform with only real zeros.

## 2. Proof of the sign property

Order the roots as in (L-19872.3).  Between consecutive nodes, the sign of
`M(d_k)` changes exactly when the interval `(d_k,d_(k+1))` contains one selected
root, namely exactly when `c_k` and `c_(k+1)` have opposite signs.

Therefore the product

\[
 M(d_k)c_k
 \tag{L-19872.7}
\]

has the same sign for every `k`.  Choose `sigma` so that this common sign is
positive.  This proves (L-19872.5).

## 3. Minimality

Let `P` be any real polynomial for which `P(d_k)c_k` has one strict sign.  If
`c_kc_(k+1)<0`, then `P(d_k)` and `P(d_(k+1))` must have opposite signs.
The intermediate value theorem gives at least one real zero of odd multiplicity
in `(d_k,d_(k+1))`.

The intervals indexed by `S` are disjoint, so `P` has at least `|S|` real zeros
counted with multiplicity.  Hence

\[
 \deg P\ge|S|=\deg M.
 \tag{L-19872.8}
\]

This proves minimality.

## 4. Exact finite Darboux interpretation

Let `f` be a compactly supported smooth source whose transform is `F`, and
suppose the selected samples are `c_k=F(d_k)` after the centered phase convention.
Applying the zero-extended differential operator with symbol `M` gives a
compactly supported distribution with transform

\[
 M(z)F(z)
 \tag{L-19872.9}
\]

and samples `M(d_k)c_k>0`.  After a finite Fourier projection, the corrected
coefficient vector is in the positive cone of `L-19871`.

The operation is rank changing and does not use a ground line of the original
localized Weil matrix.

## 5. Limit firewall

Equation (L-19872.9) does not remove a pre-existing nonreal zero of `F`.
Therefore a conclusion about `F` can follow only from a relative approximation
of the projected corrected transform divided by `M` on nonreal compact sets.

For the Xi sign pattern, `R-19851` proves that the minimal polynomial corrector
through height `H` has degree at least `cH log H` and moves the multiplied
function's Fourier energy beyond `H`.  Thus the direct same-band polynomial
implementation does not supply the needed relative limit.

## 6. Proof boundary

- The sign corrector and its minimal degree are exact.
- Together with `L-19871`, this completely solves the finite algebraic
  groundification problem for nonzero real sample vectors.
- It does not solve the moving-band relative convergence problem.
- Nonpolynomial and matrix-valued Darboux mechanisms remain outside the scope of
  `R-19851`.
