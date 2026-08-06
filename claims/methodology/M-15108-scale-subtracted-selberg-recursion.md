# M-15108 — Scale-subtracted Selberg recursion attack

Methodology ID: `M-15108`  
Status: **PROPOSED METHODOLOGY**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15146`; Selberg's exact coefficient identity; PR #216 `L-21503`  
Scope: full-problem positive attack; no claimed recursive estimate

## 1. Freeze the arithmetic target

Use scale four and put

\[
 A(x)=\psi(x)-4\psi(x/4).
\]

The RH-equivalent energy is

\[
 \boxed{
 \mathcal E_4(N)
 =\sum_{m=2}^{N-1}{A(m)^2\over m(m+1)}.}
 \tag{M-15108.1}
\]

The target is

\[
 \boxed{
 \mathcal E_4(N)=N^{o(1)}.}
 \tag{M-15108.2}
\]

No moving candidate, zero ordinate, matrix packet, or numerical primitive
remains in the statement.

## 2. Start from the exact Selberg identity

Use the coefficient identity

\[
 \Lambda(n)\log n+(\Lambda*\Lambda)(n)
 = (\mu*\log^2)(n).
 \tag{M-15108.3}
\]

Let `S(x)` be its exact summatory form. Construct the scale difference

\[
 \boxed{
 \mathscr D_4S(x)=S(x)-4S(x/4)}
 \tag{M-15108.4}
\]

before estimating any term.

The linear part contains the same Chebyshev increment `A(x)` after one exact
partial summation. The quadratic convolution splits into:

1. pairs with both factors below `x/4`;
2. one factor below and one above `x/4`;
3. pairs with product between `x/4` and `x`.

The first sector is a lower-scale copy. The second and third sectors are the
signed cross-scale terms that must pay the current energy. They may not be
replaced by absolute values.

## 3. Required finite ledger

For every unit logarithmic block, a proof-producing derivation should emit:

```text
exact current-scale energy
exact lower-scale energy
linear partial-summation boundary
quadratic low/low sector
quadratic mixed sector
quadratic current-annulus sector
Möbius forcing
archimedean or endpoint terms
final recursion coefficients
```

Every equality should be checked first on exact integer prefix arrays. Only the
final analytic estimates may widen terms.

## 4. Target recursion

The preferred theorem is

\[
 \boxed{
 \mathcal B_4(J)
 \le C(1+J)^A
 +\varepsilon_J
  \max_{J_0\le k<J}\mathcal B_4(k),
 \qquad \varepsilon_J\to0.}
 \tag{M-15108.5}
\]

A uniform coefficient `<1` is already sufficient. A coefficient tending to zero
would match the PR #216 empirical pattern more closely.

A second acceptable form is a cumulative renewal inequality

\[
 \boxed{
 \mathcal E_4(N)
 \le C(\log N)^A
 +\int_2^{N/4}K_N(t)\,d\mathcal E_4(t),
 \qquad
 \sup_N\int|K_N|<1.}
 \tag{M-15108.6}
\]

Either estimate yields a polylogarithmic or polynomial-logarithmic energy and
therefore RH through `T-15119`.

## 5. Why the empirical work matters

At the final complete scale-four block of `X-15122`,

```text
total          0.249166414237714545
diagonal      40.7125639348243382
off diagonal -40.4633975205866250
```

and PR #216's compact smoothing leaves only about `3.67e-5` of the diagonal at
its last retained block. Hence the quadratic sector of Selberg's identity is
not an error term. It is the dominant cancellation mechanism.

The correct proof should explain why the forcing and lower-scale sectors make
this cancellation stable. An argument that proves only a good pointwise PNT
remainder after discarding the quadratic term has lost the RH-scale content.

## 6. Adversarial gates

Reject any proposed recursion that:

- applies the triangle inequality before the scale subtraction;
- replaces `Lambda*Lambda` by a positive majorant;
- omits prime powers;
- assumes RH to express the quadratic term by critical-line zeros;
- infers a cofinal coefficient from a finite block fit;
- hides an exponentially large term inside an `O`-constant depending on the
  block endpoint.

A valid proof must expose a literal contraction or renewal mass below one.

## 7. Parallel negative route

The same exact block producer may be paired with the finite RH-valid notch moat.
A directed lower energy exceeding that moat is an unconditional finite
disproof certificate. The positive and negative programmes therefore share the
same integer source ledger.

## 8. Status boundary

This file specifies the full-problem proof attempt. It does not derive
(M-15108.5) or (M-15108.6), and it does not claim RH.