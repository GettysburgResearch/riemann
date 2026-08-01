# R-15108 — The order-three scalar is zero only after Gram and grading coherence

Claim ID: `R-15108`  
Status: **PROVED SCOPE CORRECTION AND EXACT FINITE OBSTRUCTIONS**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15129`, `L-15130`, `L-15131`; centered functional equation for `xi`  
Scope: smallest exact obstruction to the finite Cauchy--Laplace / cyclic-trace comparison  
Related counterexample candidates: none

## 1. The classical order-three coefficient is forced to vanish

Put

\[
E(w)=\frac{\xi(1/2+w)}{\xi(1/2)}.
\]

The functional equation gives `E(-w)=E(w)`. Hence

\[
\frac{E'(w)}{E(w)}
\]

is odd, so its coefficient of `w^2` is zero. In the normalization of `L-15129`, the classical order-three Cauchy--Laplace coefficient is therefore

\[
\boxed{A_3^{\rm classical}=0.}
\tag{R-15108.1}
\]

Thus order three does not require evaluating a new arithmetic constant. It requires proving that the finite operator family has exact centered parity.

## 2. First obstruction: omitting inverse Gram contractions

In a nonorthonormal readout basis, the represented operator is `T=G^-1 B`, not `B`. The true cubic coefficient is

\[
\operatorname{Tr}((G^{-1}B)^3).
\]

Take the one-dimensional exact example

\[
G=(4),\qquad B=(4).
\]

Then

\[
\boxed{\operatorname{Tr}((G^{-1}B)^3)=1,}
\]

while the naive contraction gives

\[
\boxed{\operatorname{Tr}(B^3)=64.}
\]

Therefore any universal Cauchy--Laplace tensor written in readout coordinates must display one `G^-1` at every cyclic gluing. Equality of an uncorrected coefficient with an operator trace is false even in dimension one.

## 3. Second obstruction: arbitrary finite compression breaks parity

Let

\[
K=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\Gamma=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Then `Gamma K Gamma=-K`, so all odd traces of the full operator vanish. Let

\[
P=\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}
\]

be the orthogonal projection onto `span(2,1)`. Since `[P,Gamma]!=0`, the compressed matrix satisfies

\[
PKP=\begin{pmatrix}16/25&8/25\\8/25&4/25\end{pmatrix}
\]

and

\[
\boxed{\operatorname{Tr}((PKP)^3)=\frac{64}{125}\ne0.}
\tag{R-15108.2}
\]

The exact grading defects are

\[
(P\Gamma P)^2-P
=-\frac1{125}\begin{pmatrix}64&32\\32&16\end{pmatrix},
\]

and

\[
(P\Gamma P)(PKP)+(PKP)(P\Gamma P)
=\frac1{125}\begin{pmatrix}96&48\\48&24\end{pmatrix}.
\]

Thus convergence of arbitrary finite-rank compressions does not give exact finite odd-trace cancellation. Every finite cutoff used in the scalar/cyclic comparison must commute with the transported grading, or its leakage must be retained quantitatively.

## 4. Third obstruction: operator construction does not identify the classical pullback

`L-15129` constructs, from one pair `(G,B)`, a scalar function whose coefficients are exactly the power traces of the represented matrix. This closes the operator-side identity.

Suppose, however, that a classical explicit-formula construction independently produces numbers

\[
A_{\ell,M,N}^{\rm classical}.
\]

The determinant identification still requires the finite theorem

\[
\boxed{
A_{\ell,M,N}^{\rm classical}
=\mathfrak c_\ell(G_{M,N},B_{M,N})
\quad\text{for every }\ell,M,N.}
\tag{R-15108.3}
\]

At order three, the right side is zero after grading. This verifies only the parity value, not that the two constructions are the same tensor. Beginning at order four, (R-15108.3) contains the complete even moment data and is no longer a formal consequence of symmetry.

Calling the two sides “pullbacks of one universal object” proves nothing unless:

1. the universal tensor is explicitly defined independently of both targets;
2. both realization maps are written down;
3. the contractions, including every inverse Gram factor, are shown equal;
4. the same finite matrix is used at every order;
5. one summable majorant justifies the finite-rank and window limits.

## 5. Exact smallest remaining source-level theorem

The operator construction is complete once the following finite source identity is proved:

```text
For one readout Gram G_(M,N), one signed seam form B_(M,N), and every ell>=2,

the classical order-ell Cauchy--Laplace coefficient is the closed Gram-cyclic
contraction

  B G^-1 B G^-1 ... B G^-1

with ell copies of B and ell copies of G^-1.
```

At `ell=3`, this coefficient must be zero because the seam grading is odd. At all even orders it must reproduce the central logarithmic moments of `xi`.

This is the smallest exact obstruction left by the same-matrix construction. It is source-specific; no abstract Hilbert--Schmidt or determinant theorem can supply it.

## 6. Logical strength of the all-orders extension

By `T-15110`, matching the complete even moment hierarchy with a positive self-adjoint determinant model is equivalent to RH. Therefore an all-orders proof of (R-15108.3) cannot emerge from estimates compatible with an off-line zero. It must use the full signed arithmetic content of the classical ledger.

## 7. Verdict

The requested programme splits cleanly:

- order-three operator identity: **proved** by `L-15129`;
- anti-commuting grading and exact vanishing: **proved abstractly** by `L-15130`;
- coherent operator-side identity at every order: **proved** by `L-15131`;
- equality with the independently defined classical coefficients: **open**, in the precise finite form (R-15108.3).

No determinant identity with `xi`, and therefore no proof of RH, is claimed.
