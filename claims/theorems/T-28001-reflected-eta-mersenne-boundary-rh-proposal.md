# T-28001 — Reflected eta–Mersenne boundary proposal for RH

Claim ID: `T-28001`  
Title: A source-specific reflected estimate for the sparse Mersenne boundary of the exact eta cascade would prove the Riemann Hypothesis  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL — ONE EXPLICIT BOUNDARY THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `R-28001`, `L-28001`--`L-28004`; reflected local block `L-9518`; square-screw/Landau consumer  
Scope: corrected global attack; RH is not claimed proved

## 1. Corrected proof spine

The proposed chain is

```text
central first-difference carry cascade
-> coefficientwise reciprocal-eta resolvent
-> exact dyadic staircase carry image
-> sparse Mersenne boundary telescope
-> reflected eta Selberg Hermitian block
-> source-specific Mersenne boundary recurrence
-> subpower reciprocal-eta Riesz coordinate
-> Mellin/Landau pole exclusion
-> RH.
```

The all-order continuum monotonicity claim of the original central-cascade
proposal is not used.  `R-28001` gives its exact product-six counterexample.

## 2. Exact finite cascade

For the critical carry target

\[
 r_0(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X,
\]

let

\[
 r_{j+1}=\mathcal T_Xr_j,
\qquad
 c_j(n)=r_j(n)-r_j(n+1),
\]

where

\[
 (\mathcal T_Xr)(q)
 =\sum_{k\ge1}[r(2kq-1)-r((2k+1)q)].
\]

After

\[
 J_X=\lceil\log_2X\rceil+1
\]

stages the residual is zero, so the central cascade is an exact signed
saturation of every carry column.

## 3. Reciprocal-eta consumer

Let `b` be the explicit inverse-eta coefficients

\[
 b(2^rm)=
 \begin{cases}
 \mu(m),&r=0,\\
 2^{r-1}\mu(m),&r\ge1,
 \end{cases}
\]

for odd `m`.  Put

\[
 \boxed{
 \mathcal R_\eta(X)
 =\sum_{q=2}^{X}{b(q)\over\sqrt q}\log{X\over q}.
 }
\tag{T-28001.1}

For `Re(z)>1/2`, termwise Mellin integration gives

\[
 \boxed{
 \int_1^\infty\mathcal R_\eta(X)X^{-z-1}dX
 ={B(z+\frac12)-1\over z^2},
 \qquad
 B(s)={1\over\eta(s)}.
 }
\tag{T-28001.2}

The finite factor `1-2^(1-s)` has no zero in the open strip
`1/2<Re(s)<1`.  Therefore

\[
 \boxed{
 \mathcal R_\eta(X)=O_\varepsilon(X^\varepsilon)
 \text{ for every }\varepsilon>0
 \quad\Longrightarrow\quad
 \mathrm{RH}.
 }
\tag{T-28001.3}

This is the standard Mellin/Landau pole-exclusion step, now attached to one
explicit eta source.

## 4. Sparse exact representation

`L-28004` proves

\[
 \boxed{
 \mathcal R_\eta(X)
 =\sum_{j=0}^{J_X-1}r_j(2)
  -\sum_{j=0}^{J_X-1}\sum_{P=2^a}
   P[r_j(2P-1)-r_j(2P)].
 }
\tag{T-28001.4}

Only Mersenne parents `2P-1` occur.  Thus the dense Möbius source has been
compressed to a deterministic `O(log^2 X)` stage/scale ledger.

The first nontrivial mutation is the product-six overlap of `R-28001`; it must
appear in any complete proof object.

## 5. Reflected eta block

`L-28003` supplies the exact independent-frequency identity

\[
 \mathcal C_\eta(\sigma;t,-u)
 -\mathcal C_\eta(\sigma;t)
 -\mathcal C_\eta(\sigma;-u)
 =2L_\eta(\sigma+it)L_\eta(\sigma-iu),
\]

and on the diagonal

\[
 2|L_\eta(\sigma+it)|^2,
 \qquad
 L_\eta=-\eta'/\eta.
\]

The two-frequency localization of `L-9518` turns this into the exact physical
normal block for the generalized prime source `Lambda_eta`.  Every off-line
zeta pole remains present.

## 6. Sole load-bearing theorem — RMBR

The **Reflected Mersenne Boundary Recurrence**, abbreviated `RMBR`, is the
following source-specific production theorem.

There exist one fixed `delta>0`, an absolute `A`, and, for an unbounded sequence
of safe-window orders `K`, numbers `epsilon_K->0` such that every sufficiently
large logarithmic block `J` admits a complete arithmetic certificate with:

1. the exact reciprocal-eta source and its dyadic generalized-prime correction;
2. the complete two-frequency reflected block;
3. every central cascade stage through support exhaustion;
4. every Mersenne row `2P-1` and its charge `P`;
5. all ordered binary--ternary product overlaps, beginning with `6=2*3=3*2`;
6. high-order Euler closure of every row with one unrestricted macroscopic
   lattice variable;
7. signed recombination before every norm;
8. a nonnegative reflected reserve `Q_K(J)`;
9. lower-scale destinations at most `(1-delta)J+O_K(1)`;
10. the estimate

\[
 \boxed{
 \begin{aligned}
 |\mathcal M_K(J)|+Q_K(J)
 \le{}&
 \exp[(\epsilon_K+o_K(1))J]\\
 &\times\left[
  1+\max_{u\le(1-\delta)J+O_K(1)}
    |\mathcal M_K(u)|
 \right],
 \end{aligned}}
\tag{T-28001.5}

where `mathcal M_K` is the complete signed Mersenne ledger in
(T-28001.4), not its termwise total variation.

A production certificate must also reproduce the fixed-ratio Mertens/Farey
mutation.  A proof that deletes the eta factor, omits a Mersenne row, or bounds
the two ordered factors of six separately is rejected.

## 7. Conditional completion

The usual scale-contraction lemma applied to (T-28001.5) gives

\[
 \mathcal M_K(J)
 \le\exp[(o_K(1)+\epsilon_K/\delta)J].
\]

Letting `K` increase yields

\[
 \mathcal M_K(J)=e^{o(J)}.
\]

The bottom values `sum_j r_j(2)` have only the declared boundary and safe-window
budgets in the same certificate, so (T-28001.4) gives

\[
 \mathcal R_\eta(X)=X^{o(1)}.
\]

Equation (T-28001.3) then proves RH.

## 8. Why this is a different review target

`RMBR` does not ask for:

- positivity of all continuum central iterates;
- a generic balanced Type-II operator norm;
- a complete finite source-frame lower singular value;
- pointwise positivity of the reciprocal-eta coefficients;
- total variation of all Möbius words.

It asks for one exact reflected recurrence on a source whose complete carry image
has already collapsed to sparse dyadic boundary rows.

The theorem is still RH-bearing.  The present branch does not prove it.

## 9. Automatic rejection tests

Reject an asserted `RMBR` certificate if it:

1. uses the false all-order central monotonicity;
2. loses the product-six coefficient `-2`;
3. omits any row `2P-1` or changes its charge `P`;
4. replaces independent frequencies by one vertical integral;
5. uses `H(z)^2` instead of a reflected modulus square;
6. takes absolute values before binary--ternary recombination;
7. cancels the factor `1/eta` with a complete Euler product;
8. leaves an uncharged current-scale boundary;
9. lacks a strict lower-scale destination;
10. fails the fixed-ratio Mertens mutation.

## 10. Exact status

```text
central cascade finite saturation             proposed exact
all-order continuum monotonicity               refuted
reciprocal-eta resolvent                       proposed exact
eta carry image and Mersenne telescope          proposed exact
reflected eta Hermitian identity                proposed exact
RMBR sparse boundary recurrence                 OPEN / RH-BEARING
RMBR -> reciprocal-eta subpower -> RH           complete conditional chain
Riemann Hypothesis                              UNPROVED
```
