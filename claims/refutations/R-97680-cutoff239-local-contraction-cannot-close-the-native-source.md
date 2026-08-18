# R-97680 — The cutoff-239 local contraction does not close the native annular source

Claim ID: `R-97680`  
Status: **EXACT SOURCE-TO-USE REFUTATION + ASYMPTOTIC NO-GO**  
Created: 2026-08-18  
Targets: the reconstructed cutoff-239 T-97400 packet and PR #565  
RH status: **unproved**

The sharp local `P_61` scalar bias is valuable, but a fixed-cutoff local
contraction is not source-complete.

At `X=184`, the native annular scalar is
\[
\mathcal A_{184}
=
F_{61}(184)
-\frac{15}{\sqrt2}
\sum_{p\in\{67,71,73,79,83,89\}}
\frac1{\sqrt p}\log\frac{92}{p}.
\]
The deleted positive term is
\[
D_{184}>1.3631478826704517.
\]
Low-child recombination returns `F_61(184)` rather than `mathcal A_184`.
Therefore it does not satisfy the root-marginal clause (L-97680.6).

More generally, for every fixed rough cutoff and every positive annular base
with
\[
M_B(x)=C_B\sqrt x+O(1),\qquad C_B>0,
\]
the source-complete raw child mass obeys
\[
\sum_{R\le p\le\sqrt x}\frac1{\sqrt p}M_B(x/p)
\ge
\frac{C_B\sqrt x}{2}
\sum_{R\le p\le\sqrt x}\frac1p.
\]
After normalization by `M_B(x)`, this diverges. Hence no fixed cutoff plus
uniform `l^1` child contraction can control arbitrary accumulated parity.

The correct repair is the exact paired-source identity of `L-97680`; its signed
current is necessarily nonlocal.
