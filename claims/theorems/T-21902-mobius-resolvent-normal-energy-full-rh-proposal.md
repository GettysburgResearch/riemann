# T-21902 — Full RH proposal from primitive-determinant Möbius contraction

Claim ID: `T-21902`  
Title: A polylogarithmic delayed normal-energy bound for the exact Möbius residual forces the rightmost-zero exponent to vanish  
Status: **FULL PROOF PROPOSAL — COMPLETE DEDUCTION FROM L-21909; PENDING INDEPENDENT REVIEW OF THE NEW DETERMINANT LEMMA**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21909`; `T-15123`; the standard functional equation for zeta  
Scope: a complete scalar proof proposal avoiding the blocked `SH(L)` construction

## 1. Möbius Hardy observable

Fix the safe window `H` of `L-21909` and define

\[
 Q_\mu(x)=\sum_{n\ge1}{\mu(n)\over\sqrt n}H(x-\log n),
 \tag{T-21902.1}
\]

\[
 E(J)=\int_J^{J+1}|Q_\mu(x)|^2dx,
 \qquad
 M(X)=1+\max_{J\le X}E(J).
 \tag{T-21902.2}
\]

`T-15123` gives the exact rightmost-zero exponent

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}{\log M(X)\over2X},
 }
 \tag{T-21902.3}
\]

and therefore

\[
 \Theta_\zeta=0\quad\Longleftrightarrow\quad\mathrm{RH}.
 \tag{T-21902.4}
\]

The window is fixed throughout the argument; no limiting filter can attenuate a
hypothetical off-line pole.

## 2. Exact delayed recurrence

For every integer `V>=2`, let

\[
 r_V=\varepsilon-\mathbf1*\mu_V.
 \]

The exact identity

\[
 \mu=\mu_V+\mu*r_V
 \tag{T-21902.5}
\]

and compact support of `H` imply, on every sufficiently late block,

\[
 E(J)=E_{\mu*r_V}(J).
 \tag{T-21902.6}
\]

Apply `L-21909.24` with `c=mu`.  There are constants `C_0,C_1>0`, depending
only on the fixed window, such that

\[
 \boxed{
 E(J)
 \le C_0(1+\log V)^8
 \left[
  1+\max_{u\le J-h_V+C_1}E(u)
 \right],
 }
 \tag{T-21902.7}
\]

where

\[
 h_V=\log(V+1).
 \tag{T-21902.8}
\]

Choose `V` so large that `h_V>2C_1`, and put

\[
 \widetilde h_V=h_V-C_1>0,
 \qquad
 C_V=2C_0(1+\log V)^8.
 \tag{T-21902.9}
\]

After absorbing the finite initial blocks into `C_V`, equation (T-21902.7)
gives

\[
 \boxed{
 M(X)\le C_VM(X-\widetilde h_V)
 }
 \tag{T-21902.10}
\]

for every sufficiently large `X`.

## 3. Iteration

Let

\[
 N=\left\lfloor{X-X_0\over\widetilde h_V}\right\rfloor.
\]

Iterating (T-21902.10) exactly `N` times gives

\[
 M(X)\le C_V^{N+1}M(X_0).
 \tag{T-21902.11}
\]

Hence

\[
 \boxed{
 \limsup_{X\to\infty}{\log M(X)\over X}
 \le {\log C_V\over\widetilde h_V}.}
 \tag{T-21902.12}
\]

Since

\[
 \log C_V=O_H(1)+8\log\log V
 \tag{T-21902.13}
\]

and

\[
 \widetilde h_V=\log V+O_H(1),
 \tag{T-21902.14}
\]

we obtain

\[
 \boxed{
 2\Theta_\zeta
 \le
 {O_H(1)+8\log\log V\over\log V+O_H(1)}.}
 \tag{T-21902.15}
\]

The inequality holds for every sufficiently large **fixed** `V`.  Letting
`V` tend to infinity yields

\[
 \boxed{\Theta_\zeta=0.}
 \tag{T-21902.16}
\]

The functional equation then places every nontrivial zero on
`Re(s)=1/2`.

Therefore

\[
 \boxed{\mathrm{RH}.}
 \tag{T-21902.17}
\]

## 4. Why the argument is not a finite-window limit trick

For each fixed `V`, the exact same Möbius signal and the exact same safe window
are used at every block.  The limit `V->infinity` is taken only after deriving
an upper bound on the single invariant `Theta_zeta`.  No convergence of windows,
packets, matrices, or finite zero tables is involved.

At a hypothetical off-line zero, the residual multiplier equals one, so no
algebraic finite-resolvent identity can hide the pole.  The proof instead uses
the source-specific **normal-energy** determinant cancellation of `L-21909` to
show that the delayed residual has only polylogarithmic transfer norm.  That is
the substantive arithmetic assertion.

## 5. Cross-route consequences

The conclusion automatically supplies every equivalent global criterion
already isolated in the repository:

1. the prime-power polygon eventually dominates the archimedean conjugate;
2. every square-screw and dyadic Haar defect has subpower negative part;
3. the prime-only and full-von-Mangoldt safe energies are subexponential;
4. the analytic-totient second moment has its critical bound;
5. every fixed-ratio Mertens difference has square-root size up to `x^epsilon`;
6. the localized Weil forms have a cofinal nonnegative lower envelope.

These are consequences, not inputs.

## 6. Mandatory adversarial review

The proof has one new load-bearing lemma rather than one omitted theorem.  An
independent reviewer should reconstruct `L-21909` in this order:

1. expand the exact residual in both legs of the normal Gram;
2. verify that all continuous and mixed Euler terms vanish by the declared
   null moments;
3. use the true primitive step `(e/g,d/g)` and enumerate all residue chains;
4. verify the four-term second difference before any principal-value limit;
5. check the factor `g/(de)=1/[d,e]` in `L-21909.19`;
6. reconstruct the `J_1` rather than `J_2` Jordan factorization;
7. test the `q=v=5,r=5` and odd--odd cotangent mutations;
8. verify the first-cell Mertens consequence.

A failure at any one of these steps rejects the proposal but does not affect the
previously verified Möbius Hardy criterion or the other exact repository
reductions.

## 7. Status boundary

This file contains no unproved hypothesis beyond the proposed lemma
`L-21909`, whose proof is written in full on the branch.  The deduction from
that lemma to RH is elementary and complete.

The result is submitted as a **proposed proof candidate**, not as an accepted or
independently verified proof of the Riemann hypothesis.
