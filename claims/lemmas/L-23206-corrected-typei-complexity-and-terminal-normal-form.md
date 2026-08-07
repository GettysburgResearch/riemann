# L-23206 — Corrected Type-I complexity reduction and terminal normal form

Claim ID: `L-23206`  
Title: With one fixed reserve below one third, every nonbalanced packet lowers complexity and every terminal row has one unrestricted lattice variable  
Status: **PROPOSED COMPLETE SOURCE REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: PR #158 `L-15156/L-15157`; `L-23201`; `L-23205`  
Scope: exact Type-I routing and terminal closure; balanced Type-II estimates remain open

## 1. Canonical reserve

Fix

\[
\boxed{
\delta=\frac15
}
\tag{L-23206.1}
\]

and take `K>=6`, so

\[
\frac1K<\delta<\frac13.
\tag{L-23206.2}
\]

The strict inequality `delta<1/3` is load bearing.  A generic reserve only below
`1/2` is sufficient for the first-crossing dichotomy, but not for the internal
complexity reduction used here.

At logarithmic output scale `J`, every active product satisfies

\[
e^{J-C_K}\le N\le e^{J+C_K}.
\tag{L-23206.3}
\]

After the first Type-I split, write

\[
N=S L,
\qquad
S\le e^{\delta J+C_K},
\tag{L-23206.4}
\]

where `S` is the complete small prefix and `L` is the unresolved large
coefficient word.  Its complexity is the number of unresolved nontrivial
variables in `L`.

## 2. Correct internal dichotomy

Suppose the large word has complexity at least two and split it exactly as

\[
L=BC.
\tag{L-23206.5}
\]

There are three cases.

### 2.1 One internal factor is too large

If

\[
B>e^{(1-\delta)J+C'_K},
\]

then

\[
SC=N/B<e^{\delta J+O_K(1)}.
\]

Absorb `C` into the small prefix and retain `B` as the new large word.  The
complexity strictly decreases.  The same argument applies with `B,C`
interchanged.

### 2.2 Both internal factors are below the upper threshold

Assume

\[
B,C\le e^{(1-\delta)J+O_K(1)}.
\tag{L-23206.6}
\]

From (L-23206.3)--(L-23206.4),

\[
BC=N/S\ge e^{(1-\delta)J-O_K(1)}.
\tag{L-23206.7}
\]

Since

\[
2\delta<1-\delta,
\]

both `B` and `C` cannot be below `e^(delta J-O_K(1))`.  Suppose, after
interchanging them if necessary,

\[
B\ge e^{\delta J-O_K(1)}.
\]

Then (L-23206.6) gives the upper bound for `B`, while

\[
SC=N/B\le e^{(1-\delta)J+O_K(1)}.
\]

Thus

\[
\boxed{
B\mid SC
}
\tag{L-23206.8}
\]

is a balanced Type-II split: both full factor groups lie between the declared
strict lower and upper logarithmic scales, up to fixed support slack.

### 2.3 Exhaustion

Every internal step therefore produces either

1. an exact balanced Type-II destination, or
2. a same-scale Type-I source with strictly lower integer complexity.

The process terminates after finitely many steps.  There is no same-scale cycle.

## 3. Source equality and the energy routing inequality

The split (L-23206.5) is a finite re-indexing of the exact Heath--Brown or
Möbius-resolvent tuple sum.  All rows with the same destination are recombined
with their original Möbius/binomial signs **before** any norm.

For fixed `K`, the number of destination words and tuple multiplicities is
`exp(o_K(J))`.  If an exact source row is decomposed after signed recombination
as

\[
Q_\tau=\sum_{r=1}^{R_K(J)}Q_{\tau,r},
\qquad
R_K(J)=e^{o_K(J)},
\]

then Gram Cauchy--Schwarz gives

\[
\boxed{
\|Q_\tau\|_{L^2(J,J+1)}^2
\le
R_K(J)
\sum_{r=1}^{R_K(J)}
\|Q_{\tau,r}\|_{L^2(J,J+1)}^2.
}
\tag{L-23206.9}
\]

Thus reduced-complexity Type-I routing is an exact finite source reduction plus
a subexponential combinatorial factor.  It does not assume a balanced Type-II
estimate; it merely routes balanced destinations into the family whose estimate
is named `BTP(K)`.

## 4. The terminal variable is unrestricted

At complexity one, the remaining large variable has size

\[
L\ge e^{(1-\delta)J-O_K(1)}.
\tag{L-23206.10}
\]

Every truncated Möbius variable in the order-`K` packet satisfies

\[
d\le e^{J/K+O_K(1)}<e^{\delta J+O_K(1)}.
\tag{L-23206.11}
\]

Therefore a truncated variable cannot be terminal-large.

For the Heath--Brown packet, the terminal variable is one of the unrestricted
`q,r_i` variables.  For the finite Möbius resolvent, expand

\[
r_V(n)=-\sum_{\substack{d\mid n\\d\le V}}\mu(d)
\]

and absorb the divisor `d<=V` into the small prefix.  The remaining quotient
variable runs over the complete positive-integer lattice on the active compact
window.  Because the terminal variable is exponentially larger than `V`, the
condition `n>V` is automatic and introduces no extra terminal boundary.

All truncation and first-crossing conditions are now contained in the small
coefficient packet.

## 5. Exact terminal normal form

After grouping by the small product `A`, every terminal signal is a finite sum
of rows

\[
\boxed{
\sum_{n\ge1}
\frac{P_A(\log n)}{\sqrt{An}}
H_K\!\left(x-\log(An)\right),
}
\tag{L-23206.12}
\]

where

\[
H_K=H^{[K+1]},
\qquad
A\le e^{\delta J+O_K(1)},
\qquad
\deg P_A\le K.
\]

The high-order window has the half-pole moments required by `L-23205`.
At fixed `K`, divisor-order multiplicity and polynomial coefficient mass give

\[
\sum_A |c_A|
\max_{J\le x\le J+1}\mathcal P_{A,x}
\le e^{(\delta+o_K(1))J}.
\tag{L-23206.13}
\]

Applying `L-23205` yields

\[
\boxed{
E_{K,\mathrm{term}}(J)
\le
\exp\left[-\left(\frac35-o_K(1)\right)J\right].
}
\tag{L-23206.14}
\]

The terminal coefficient exponent is therefore zero.

## 6. What is actually eliminated

The exact source reduction closes:

- same-scale Type-I complexity chains;
- terminal Type-I rows;
- truncated-variable boundaries in terminal rows;
- first-crossing transition rows absorbed into the small prefix.

It does **not** estimate the balanced Type-II destinations created in
(L-23206.8).  Those destinations are the sole independent arithmetic family in
the corrected proposal.

## 7. Why `delta<1/3` is necessary for this proof

For a reserve merely below `1/2`, it may happen that `S<=X^delta` and both
internal factors lie below `X^(1-delta)`, yet neither internal factor reaches
`X^delta`; then neither full split is balanced and no complement is small.
For example, at exponent level with `delta=0.4`,

\[
s=0.37,
\qquad b=0.385,
\qquad c=0.245,
\qquad s+b+c=1,
\]

has exactly this defect.

The inequality `2delta<1-delta` excludes the defect and is the reason for the
canonical choice `delta=1/5`.

## 8. Proof boundary

Closed here, pending independent reconstruction:

- corrected fixed-reserve internal dichotomy;
- strict complexity decrease for every unbalanced row;
- exact unrestricted terminal normal form;
- terminal Euler decay.

Open:

- the signed balanced Type-II theorem `BTP(K)`;
- its vanishing coefficient rate;
- RH.