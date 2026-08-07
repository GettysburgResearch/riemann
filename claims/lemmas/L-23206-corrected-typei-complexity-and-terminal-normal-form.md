# L-23206 — Corrected Type-I complexity reduction and terminal normal form

Claim ID: `L-23206`  
Title: With one fixed reserve below one third, every nonbalanced packet lowers complexity and every terminal row has one unrestricted lattice variable  
Status: **PROPOSED COMPLETE SOURCE REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Updated: 2026-08-07 after residual-expansion ordering audit  
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

## 2. Source normalization before partition

For the Heath--Brown packet, retain the exact tuple variables of `L-15156`.
Truncated Möbius variables are bounded; `q,r_i` are unrestricted.

For the finite Möbius resolvent, first expand every residual coefficient

\[
r_V(n)=-\sum_{\substack{d\mid n\\d\le V}}\mu(d)
\]

and write `n=dm`.  The bounded divisor `d<=V` and unrestricted quotient `m`
are separate exact tuple variables **before** first crossing and complexity
classification.  All signs remain actual Möbius signs.

This ordering is mandatory.  Expanding a residual only after declaring a small
prefix could enlarge that prefix and invalidate its exponent budget.

After the first Type-I split, write

\[
N=S L,
\qquad
S\le e^{\delta J+C_K},
\tag{L-23206.4}
\]

where `S` is the complete small prefix, including every bounded divisor already
absorbed by the exact partition, and `L` is the unresolved large coefficient
word.  Its complexity is the number of unresolved nontrivial variables in `L`.

## 3. Correct internal dichotomy

Suppose the large word has complexity at least two and split it exactly as

\[
L=BC.
\tag{L-23206.5}
\]

### 3.1 One internal factor is too large

If

\[
B>e^{(1-\delta)J+C'_K},
\]

then

\[
SC=N/B<e^{\delta J+O_K(1)}.
\]

Absorb `C` into the small prefix and retain `B` as the new large word.  The
complexity strictly decreases and the **complete** new prefix remains below the
declared budget.  The same argument applies with `B,C` interchanged.

### 3.2 Both internal factors are below the upper threshold

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

Then `B` has the required upper bound, while

\[
SC=N/B
\]

lies between `e^(delta J-O_K(1))` and
`e^((1-delta)J+O_K(1))`.  Thus

\[
\boxed{
B\mid SC
}
\tag{L-23206.8}
\]

is a balanced Type-II split of the two **complete** factor groups.

### 3.3 Exhaustion

Every internal step therefore produces either

1. an exact balanced Type-II destination, or
2. a same-scale Type-I source with strictly lower integer complexity.

The process terminates after finitely many steps.  There is no same-scale cycle.

## 4. Source equality and energy routing

Every split above is a finite re-indexing of the exact expanded tuple sum.  All
rows with the same destination are recombined with their original
Möbius/binomial signs before any norm.

For fixed `K`, destination-word and divisor multiplicities are
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

Thus reduced Type-I routing is an exact finite source reduction plus a
subexponential combinatorial factor.  Balanced destinations are routed into the
family `BTP(K)`; they are not estimated here.

## 5. The terminal variable is unrestricted

At complexity one, the remaining large variable has size

\[
L\ge e^{(1-\delta)J-O_K(1)}.
\tag{L-23206.10}
\]

Every truncated or bounded divisor variable satisfies

\[
d\le e^{J/K+O_K(1)}<e^{\delta J+O_K(1)}.
\tag{L-23206.11}
\]

It cannot be terminal-large.

Consequently:

- in the Heath--Brown packet the terminal variable is one of the unrestricted
  `q,r_i` variables;
- in the fully expanded Möbius-resolvent packet it is one of the unrestricted
  quotient variables `m`.

All truncation and first-crossing conditions lie in the complete small prefix
`S`.  On the active compact window, the terminal variable automatically exceeds
all residual lower cutoffs and runs over the complete positive-integer lattice.

## 6. Exact terminal normal form

After grouping by the complete small product `A`, every terminal signal is a
finite sum of rows

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

## 7. What is and is not eliminated

Closed by the exact source reduction:

- same-scale Type-I complexity chains;
- terminal Type-I rows;
- bounded-divisor and truncation boundaries in terminal rows;
- first-crossing transitions absorbed into the small prefix.

Not estimated:

- the balanced Type-II destinations created in (L-23206.8).

Those destinations are the sole independent arithmetic family in the corrected
proposal.

## 8. Why `delta<1/3` is necessary

For a reserve merely below `1/2`, it may happen that `S<=X^delta` and both
internal factors lie below `X^(1-delta)`, yet neither internal factor reaches
`X^delta`; then neither full split is balanced and no complement is small.
At exponent level with `delta=0.4`,

\[
s=0.37,
\qquad b=0.385,
\qquad c=0.245,
\qquad s+b+c=1,
\]

has exactly this defect.

The inequality `2delta<1-delta` excludes it.

## 9. Proof boundary

Closed here, pending independent reconstruction:

- pre-partition residual expansion;
- corrected internal dichotomy;
- strict complexity decrease for every unbalanced row;
- unrestricted terminal normal form;
- terminal Euler decay.

Open:

- `BTP(K)`;
- its vanishing coefficient rate;
- RH.