# R-23702 — Bounded-rank contagion fails on exact Möbius hypercubes

Claim ID: `R-23702`  
Title: The fixed-logarithm Möbius slice contains balanced same-scale Bohr faces of arbitrarily large exact rank, with no product collision, no free lattice coordinate, and no strict-scale source identity  
Status: **EXACT REFUTATION OF THE ABSOLUTE-RANK HINGE IN `L-23702`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Targets: `L-23702`, `L-23703`, `T-23701`, PR #239  
Dependencies: PR #158 `L-15159`; unique factorization; the prime number theorem in fixed relative intervals  
Scope: refutes `rank(F)<=C_0` with `C_0` independent of packet order; does not refute a genuinely analytic signed Type-II theorem

## 1. Exact fixed-logarithm source

For the order-`K` Heath--Brown inverse packet

\[
A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
   \mu_V^{*j}*1^{*(j-1)},
\]

`L-15159` proves coefficientwise

\[
A_{K,V}(m)=\mu(m)
\qquad(m\le V^K).
\tag{R-23702.1}
\]

Fix the logarithmic variable at `q_0=2`.  Throughout `2m<=V^K`, the complete
signed tuple recombination is therefore

\[
\boxed{
 {\log2\over\sqrt2}
 {\mu(m)\over\sqrt m}
 H(x-\log(2m)).
}
\tag{R-23702.2}
\]

Distinct products are distinct Bohr monomials.  No source-recombination identity
can combine them further, because characters on the full prime torus are
linearly independent.

## 2. A `K`-dimensional squarefree product cube

Fix an arbitrary integer `K>=2`.  Choose a number

\[
0<\epsilon<\log(3/2).
\]

For all sufficiently large `Y`, the prime number theorem permits `K` pairwise
disjoint intervals

\[
I_i\subset
\left[Y,(1+\epsilon/K)Y\right],
\qquad1\le i\le K,
\tag{R-23702.3}
\]

such that each interval contains

\[
\exp\{\log Y-o(\log Y)\}
\]

primes.  The intervals may be chosen with disjoint prime sets.

For every choice of one prime `p_i in I_i`, put

\[
n=p_1\cdots p_K.
\tag{R-23702.4}
\]

Let `mathcal N_(K,Y)` be the resulting product set.  Unique factorization gives:

1. all products in `mathcal N_(K,Y)` are distinct;
2. every product is squarefree with exactly `K` prime factors;
3. every coefficient is
   \[
   \mu(n)=(-1)^K\ne0;
   \tag{R-23702.5}
   \]
4. the number of products is
   \[
   |\mathcal N_{K,Y}|
   =\exp\{K\log Y-o_K(K\log Y)\}.
   \tag{R-23702.6}
   \]

Moreover,

\[
{\max\mathcal N_{K,Y}\over\min\mathcal N_{K,Y}}
\le(1+\epsilon/K)^K
<e^\epsilon
<{3\over2}.
\tag{R-23702.7}
\]

Put

\[
X=\max\mathcal N_{K,Y}.
\]

Then every member of the cube lies in the single fixed-ratio shell

\[
\boxed{
{2X\over3}<n\le X.
}
\tag{R-23702.8}
\]

Choose `V` larger than twice the right endpoint of (R-23702.3).  Then
`2n<=V^K` for sufficiently large `V`, so the exact fixed-`q_0` decoder
(R-23702.2) applies to the entire cube.

## 3. Exact Bohr rank

Choose one base prime `p_i^- in I_i` and another `p_i^+ in I_i` for every
coordinate.  The `2^K` subcube has exponent vectors

\[
v(\omega),\qquad\omega\in\{-,+\}^K.
\]

Relative to the all-minus vertex, the `i`-th edge vector is

\[
e_{p_i^+}-e_{p_i^-}.
\tag{R-23702.9}
\]

These vectors have disjoint supports and are linearly independent over every
field of characteristic zero.  Hence the affine exponent rank of this exact
Bohr face is

\[
\boxed{K.}
\tag{R-23702.10}
\]

Using all primes in the intervals rather than two choices, each of the `K`
coordinates has

\[
\exp\{J/K-o_K(J)\}
\]

source values, where

\[
J=K\log Y+O_K(1).
\tag{R-23702.11}
\]

Thus the face has precisely the range size postulated for each free coordinate
in `L-23702.4`, but its rank is `K`, not an absolute constant.

## 4. None of the other three outcomes applies

### No exact product collision

Distinct coordinate choices give distinct prime factorizations.  The Bohr
monomials are different and their coefficients are nonzero.  Only the literal
Hermitian diagonal `m=n` is an exact collision; the off-diagonal cube remains.

### No Euler-eligible complete lattice

Every active coordinate is a truncated prime coordinate.  It is neither an
unrestricted positive-integer lattice nor a complete interval after the other
coordinates are frozen.  Euler summation in one coordinate would insert a
prime indicator and is not licensed by the terminal lattice theorem.

### No exact strict-scale source identity

Every product remains in the shell (R-23702.8), at logarithmic scale `J+O_K(1)`.
Splitting the product into two smaller factor groups gives a tensor factorization
whose scale weights sum to one.  It does not identify the complete shell source
with one auxiliary packet at scale `(1-delta)J`.

Therefore this is a genuine balanced, same-scale, noncollision family.

## 5. The local shell interaction is not a minor-arc error

For the shell window

\[
H_{2/3}(u)=e^{-u/2}\mathbf1_{[0,\log(3/2))}(u),
\]

all supports corresponding to `n in mathcal N_(K,Y)` have a common
intersection because of (R-23702.7).  At `t=log X`, every term is active and

\[
{\mu(n)\over\sqrt n}
H_{2/3}(\log X-\log n)
=\mu(n)X^{-1/2}.
\]

All coefficients on the cube have the same sign.  Hence its isolated signal is

\[
\boxed{
Q_{\rm cube}(\log X)
=(-1)^K{|\mathcal N_{K,Y}|\over\sqrt X}.
}
\tag{R-23702.12}
\]

The family is a maximally coherent local Kronecker resonance, not an oscillatory
minor-arc packet.  Cancellation can occur only after coupling it to other
Möbius-parity families.  Proving that coupling is the signed balanced theorem
itself.

## 6. The aggregate-product alternative does not rescue the count

One may collapse the `K` factor coordinates to the product `n`.  Then the rank
is one, but that coordinate ranges through

\[
\exp\{J-o_K(J)\}
\]

values, not through

\[
\exp\{J/K+o_K(J)\}.
\]

Thus the enumeration cost is still `exp((1-o(1))J)`, not
`exp(C_0J/K)`.  The two presentations give an unavoidable dichotomy:

```text
retain the actual short factors: rank Omega(K);
collapse to the product: one coordinate of full output scale.
```

Neither yields the claimed `C_0/K` loss.

## 7. Consequence

The absolute-rank statement

\[
\operatorname{rank}F\le C_0
\]

for every surviving balanced resonance face is false in the actual fixed-log
Möbius packet.  Therefore:

```text
L-23702 BCT(K) absolute rank hinge       REFUTED
L-23703 C0/K conclusion for this hinge  NOT APPLICABLE
T-23701 as a completed proposal         GAP/BLOCKED
RH                                      UNPROVED
```

This refutation does **not** say that the balanced packet cannot be controlled.
It says the control cannot come from order-independent face dimension.  A valid
completion must prove cancellation between high-rank opposite-parity families,
for example through a source-specific signed Type-II, carry-minorant, reflected
Selberg, or another genuinely arithmetic theorem.

## 8. Exact finite regression

`X-23702` freezes eight disjoint close prime pairs.  Its `2^8` products are:

- pairwise distinct and squarefree;
- all in one `2/3` shell;
- all of Möbius sign `+1`;
- an exact affine Bohr cube of rank eight.

The regression is finite algebra only.  The all-`K` statement uses the prime
number theorem as in Section 2.