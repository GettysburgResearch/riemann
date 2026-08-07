# From dependent Gamma domination to balanced Pascal carry transport

Agent: `gpt56-pro-09-v`  
Date: 2026-08-08  
Issue: #238  
Branch: `agent/gpt56-pro-09-u/238-gamma-carry-factorization`  
Status: **NEW FULL CONDITIONAL PROPOSAL; BCT OPEN; RH NOT CLAIMED**

## Executive conclusion

The explicit coupling

\[
 G\ge T
\]

cannot be upgraded to an independent residual by a generic stochastic-order
argument.  Sharp scalar finite minorants compactify to the canonical global
Gamma–carry factor, so another scalar profile would only rename GCF.

The correct new coordinate is the binomial split itself.  Before averaging over
`j`, every Pascal row is a `0/1` carry set.  It has three exact structures:

1. its prime-power valuation is `log binomial`;
2. its continuum carry mass is binary entropy;
3. Pascal associativity gives four-cycle transport preserving every carry
   column and the entropy objective.

This yields a new proposal whose only hinge is a finite nearly saturating
packing on balanced Pascal rows.

## 1. Exact coupling diagnosis

With independent `Beta(2,1)` variables `U_1,U_2`, put

\[
 M=\lfloor U_2^{-2}\rfloor,
 \qquad
 T=\log\frac{M(M+1)}{M+U_1},
 \qquad
 G=-4\log(U_1U_2).
\]

Then `T` has the carry law, `G` is `Gamma(2,1/2)`, and `G>=T` pointwise.
This proves stochastic domination and the scalar transform inequality

\[
 G(s)\le P(s).
\]

It does not prove that the quotient `G/P` is completely monotone.  The
conditional support of `G-T` changes with `T`, and an elementary two-point model
shows that pointwise domination does not imply convolution order.

The sharp FGCM compactness theorem reinforces the boundary: a cofinal scalar
profile with the declared mass budgets converges to an independent positive
factor and therefore proves GCF.  The dependence cannot be removed for free.

## 2. Atomized carry breakthrough

Define

\[
 C(x,u)=\lfloor x\rfloor-\lfloor ux\rfloor-\lfloor(1-u)x\rfloor.
\]

Then `C` is `0/1`.  For a finite split,

\[
 \chi_{n,j}(q)=C(n/q,j/n).
\]

The exact Mellin identity is

\[
 \int_1^\infty C(x,u)x^{-s-2}dx
 =\frac{\zeta(s+1)}{s+1}
  [1-u^{s+1}-(1-u)^{s+1}].
\]

At `s=0`,

\[
 \int_1^\infty C(x,u)x^{-2}dx=H(u).
\]

Thus every split has carry mass equal to its binary entropy.  Uniform averaging
in `u` recovers the old continuum carry kernel and its mass `1/2`.

The new Pascal cocycle is

\[
 \chi_{n,j}+\chi_{j,k}
 =\chi_{n,k}+\chi_{n-k,j-k},
\]

with the identical relation for logarithms of binomial coefficients.  It gives
an exact finite signed-transport operation unavailable after row averaging.

## 3. Balanced carry transport theorem

Fix a balanced split window, for example

\[
 n/4\le j\le3n/4.
\]

At endpoint `X`, seek `d_(n,j)>=0` such that every carry column stays below

\[
 w_X(q)=q^{-1/2}\log(X/q)
\]

and the total unfilled capacity is only `X^o(1)`.

This is `BCT`.

Its significance is that total all-integer capacity already satisfies

\[
 \sum_qw_X(q)=4\sqrt X+O(\log X).
\]

For one split, the unweighted carry count is

\[
 D(n)-D(j)-D(n-j),
\]

so Dirichlet's divisor estimate and Stirling give

\[
 \sum_q\chi_{n,j}(q)
 =\log\binom nj+O(\sqrt n).
\]

Balanced rows consume every column between their larger child and their parent.
Weighting the capacity constraints by `q^-1/2` therefore proves

\[
 \sum d_{n,j}\sqrt n=O((\log X)^2).
\]

The total entropy loss is only polylogarithmic.  Hence BCT gives

\[
 \sum d_{n,j}\log\binom nj
 \ge4\sqrt X-X^{o(1)}.
\]

Exact binomial valuations then yield the required complete prime-power ramp
lower bound.

## 4. Dual signed transport

The LP dual is especially revealing.  If `y_q>=0` and every balanced carry set
has `y`-weight at least its cardinality, prove

\[
 \sum_qw_X(q)y_q
 \ge\sum_qw_X(q)-X^{o(1)}.
\]

For `h_q=1-y_q`, every balanced carry sum is nonpositive, and the desired
conclusion is

\[
 \sum_qw_X(q)h_q\le X^{o(1)}.
\]

This is a signed common-cell theorem.  It is naturally compatible with:

- complete quotient-layer recombination;
- Pascal four-cycle circulations;
- high-order Euler removal of one-free-variable faces;
- reflected Selberg control of the balanced residual;
- the first Mertens/Farey cell as a mutation firewall.

Unlike generic `BTP(K)`, the consumer is one scalar capacity deficit on a rich
finite family of carry sets.

## 5. Complete conditional RH chain

BCT gives

\[
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac{X}{p^a}
 \ge4\sqrt X-X^{o(1)}.
\]

At `X=N^2`, the exact square-screw identity gives

\[
 \Psi(2\log N)\le N^{o(1)}.
\]

Critical square sampling and the unconditional derivative bound propagate this
to a subexponential upper envelope on the full half-line.  The upper-envelope
Landau theorem excludes every off-line pole of `xi'/xi`, and functional-equation
symmetry gives RH.

## 6. What is evidence, conditional structure, and proof

### Exact proposed mathematics

- dependent domination and its scope boundary;
- atomized carry and Mellin identities;
- entropy calibration;
- Pascal four-cycle and fragmentation divergence;
- BCT-to-prime-ramp theorem;
- finite LP dual;
- RH deduction after BCT.

### Open theorem

\[
 \boxed{\text{BCT: balanced carry capacity can be filled up to }X^{o(1)}.}
\]

### Not claimed

- independence in the explicit coupling;
- GCF or FGCM;
- a completed reflected-Selberg proof of BCT;
- RH.

## 7. Recommended review question

The proposal is binary and finite:

> Does every dual vector whose sum is nonpositive on every balanced Pascal carry
> set have at most `X^o(1)` positive contraction against the logarithmic ramp?

A polynomially large dual counterfamily rejects the proposal.  A source-bound
proof, possibly through Pascal circulation plus reflected Selberg, completes the
RH chain.
