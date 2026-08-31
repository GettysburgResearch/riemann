# L-107300 — Reduced Kummer augmentation is the exact connected squareclass projector

Claim ID: `L-107300`  
Programme aliases: `RIEMANNSTRUCT.AUGMENTATION_PROJECTOR`, `LFAM2.REDUCED_KUMMER_OBJECT`  
Status: **PROVED EXACT FINITE-FOURIER AND SHEAF-THEORETIC NORMAL FORM**  
Created: 2026-08-30  
Depends on: PR #765 shared-fibre squareclass cells; standard Kummer sheaves  
Programme issues: #763, #737, #739  
RH/GRH status: **not assumed**

Let \(k=\mathbf F_Q\) have odd cardinality \(Q\), put

\[
G_Q=k^\times,\qquad X_Q=G_Q/\{\pm1\},\qquad m_Q=\frac{Q-1}{2},
\]

and let \(\widehat X_Q\) be the even multiplicative characters
\(\eta:G_Q\to\overline{\mathbf Q}_\ell^\times\), equivalently
\(\eta(-1)=1\).

Let \(V_Q=\overline{\mathbf Q}_\ell[X_Q]\), let \(P_Q^0\) be the orthogonal
projection onto constants, and put

\[
P_Q^\perp=I-P_Q^0.
\]

## 1. Exact character projector

For \(x,y\in G_Q\),

\[
\boxed{
P_Q^\perp([x],[y])
=
\mathbf1_{[x]=[y]}-\frac1{m_Q}
=
\frac1{m_Q}
\sum_{\substack{\eta\in\widehat X_Q\\\eta\ne1}}
\eta(xy^{-1}).
}
\tag{L-107300.1}
\]

Thus the connected squareclass kernel is not a virtual subtraction chosen
after the fact. It is the augmentation representation of the actual finite
quotient \(X_Q\).

## 2. Honest Kummer object

For each \(\eta\in\widehat X_Q\), let \(\mathcal L_\eta\) be the rank-one
Kummer sheaf on the multiplicative torus. Define

\[
\boxed{
\mathscr A_Q
=
\bigoplus_{\substack{\eta\in\widehat X_Q\\\eta\ne1}}
\mathcal L_\eta.
}
\tag{L-107300.2}
\]

This is an actual lisse sheaf, not a class in a Grothendieck group. It is tame,
pure of weight zero, and has rank \(m_Q-1\). Its normalized trace kernel is
exactly (L-107300.1).

Equivalently, \(\mathscr A_Q\) is the kernel of the summation map from the
permutation local system of \(X_Q\) to the constant local system.

## 3. Two-place connected projector

For two odd residue fields \(k_\ell,k_\rho\), the external product

\[
\mathscr A_\ell\boxtimes\mathscr A_\rho
\]

has normalized trace kernel

\[
\boxed{
\left(\mathbf1_{[x]=[x']}-\frac1{m_\ell}\right)
\left(\mathbf1_{[y]=[y']}-\frac1{m_\rho}\right).
}
\tag{L-107300.3}
\]

At the finite Hilbert-space level this is precisely

\[
P_\ell^\perp\otimes P_\rho^\perp.
\]

Hence the connected Kummer–Möbius inclusion–exclusion appearing in PR #751
and the shared-fibre trace algebra of PR #765 have an honest positive
augmentation object before atomic Wick centering.

## Scope

The lemma constructs the local connected object and its exact trace kernel. It
does not prove that its pullback along the complete live Boolean source has no
constant constituent; the only possible square-pullback resonances are
classified in `L-107301`.
