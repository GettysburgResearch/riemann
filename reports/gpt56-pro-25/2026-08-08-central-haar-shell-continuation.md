# Central-Haar shell continuation — 2026-08-08

Status: `FULL ELEMENTARY PROPOSAL / CHSS OPEN`  
Issue: #245  
PR: #248  
Branch: `agent/gpt56-pro-25/245-parabolic-carry-transport`

## Refresh against the live graph

This continuation was undertaken after refreshing against the newest elementary
work rather than continuing the original monotone-cover proposal.

The live graph now establishes the following scope corrections.

1. The nonnegative monotone Divisibility Cover is false at polylogarithmic cost:
   a fixed prime-ratio band forces an `Omega(sqrt X)` von-Mangoldt dual bill.
2. The parabolic seed has macroscopic positive and negative defect masses; a
   sharp proof must recombine them before a positive part is taken.
3. The unweighted ordinary-prime queue has a proposed deterministic
   `sqrt(X)/log^2(X)` density drift and is not the correct subpower scalar.
4. The logarithmically weighted dyadic shell removes that first-order drift.
5. The repository's canonical consolidation identifies Weighted Shell-Tail
   Stability (`WSTS`) as RH-equivalent.
6. Pure carry windows cancel the inverse-zeta pole; a proof must retain the
   dyadic boundary/source channel.

The continuation therefore targeted an explicit signed factor-two producer and
its completed dyadic shell, not another monotone cover or unsigned Gram.

## Exact central-Neumann construction

For the central split `n=floor(n/2)+ceil(n/2)`, the carry row is the exact square
wave

```text
chi_n^c(q)=1 iff n mod (2q) belongs to {q,...,2q-2}.
```

For a finite target `f`, first differences of `f` on central rows leave the
residual

```text
(Tf)(q)=sum_k [f((2k+2)q-1)-f((2k+3)q)].
```

The support of `Tf` is at most half the support of `f`, so `T` is nilpotent at
every finite endpoint. The terminating Neumann sum supplies one completely
explicit signed coefficient vector `A_X` which saturates every integer carry
column exactly.

No LP, asymptotic inverse, or unknown flow is involved.

## New exact binary-tree Green formula

Let

```text
U_X(m)=sum_(k<=X/m) mu(k) w_X(mk),
R_X(m)=U_X(m)-U_X(m+1).
```

The central coefficients satisfy

```text
A_X(n)=R_X(n)+A_X(2n-1)+2A_X(2n)+A_X(2n+1).
```

After `r` fragmentations, the multiplicity kernel is the exact tent

```text
K_r(m,n)=(2^r-|m-2^r n|)_+.
```

Summation by parts gives the Haar formula

```text
A_X(n)=sum_r [sum_(2^r(n-1)<m<=2^r n) U_X(m)
             -sum_(2^r n<m<=2^r(n+1)) U_X(m)].
```

Thus, with

```text
G_X(n)=sum_r sum_(2^r(n-1)<m<=2^r n) U_X(m),
```

one has exactly

```text
A_X(n)=G_X(n)-G_X(n+1),
G_X(n)=U_X(n)+G_X(2n-1)+G_X(2n).
```

The negative coefficient ledger is the upward variation of one explicit binary
potential.

## Exact refutation of pure central positivity

The stronger hope `A_X(n)>=0` for every endpoint is false. Directed
100-decimal arithmetic proves

```text
X=10050,
n=11,
A_X(n)<0.
```

This matches the independent pure-halving failure on the fragmentation branch.
The new branch records it as `R-24504` and makes it a mandatory mutation.

This does not reject signed saturation or a subpower negative-variation theorem.
It rejects only the attempt to close the route by pointwise pure-central
positivity.

## Corrected shell theorem

For

```text
Y=floor(X/2),
B_X=A_X-A_Y,
```

linearity proves that `B_X` saturates exactly the logarithmically weighted
endpoint shell

```text
w_X(q)-1_(q<=Y)w_Y(q).
```

Define

```text
S_X=sum_n sqrt(n)(-B_X(n))_+.
```

The proposed Central-Haar Shell Stability theorem is

```text
S_X=X^o(1).
```

Since

```text
A_X=A_Y+B_X,
```

CHSS iterates to global subpower negative variation. Exact weighted carry loading
then pays the positive variation automatically, yielding

```text
prime ramp=4 sqrt(X)+X^o(1),
```

and the existing square-screw/Landau chain gives RH.

## Why this is not merely another equivalence

The arithmetic theorem remains RH-bearing, as it must. The advance is on the
producer side:

- the finite signed certificate is explicit and terminating;
- factor-two descent is an identity at source, Green, and potential levels;
- the pointwise positivity overclaim has been removed by an exact mutation;
- the only remaining cost is the upward variation of one completed dyadic-shell
  potential;
- no existential flow, generic frame, or monotone cover remains hidden.

The proposed proof attack is now to combine the upper and lower shell at the
`U_X-U_Y` level, group complete quotient-knot fibers, apply the proved continuum
shell moat to the smooth block average, and recurse only on the retained signed
Mertens boundary.

## Reconnaissance boundary

Ordinary floating scans show that the full central negative coefficients occur
in dyadically organized low-index bands and have small weighted mass through the
tested endpoints. Shell coefficients themselves are signed, so CHSS is not a
pointwise positivity theorem. No finite trend is promoted.

The exact/directed verifier `X-24504` authenticates only finite algebra and the
specific positivity counterexample.

## Durable files

```text
L-24523  terminating central-Neumann saturation
L-24524  negative variation controls full variation
L-24525  binary-tree Green/Haar potential
R-24504  pure central positivity counterexample
T-24507  Central-Haar Shell Stability proposal
X-24504  exact/directed finite replay
```

## Exact boundary

```text
finite central saturation             proposed complete
binary-tree Green/Haar potential      proposed complete
pure central positivity               refuted
factor-two shell decomposition        proposed complete
CHSS                                  open / RH-bearing
CHSS -> prime ramp -> RH              proposed complete
Riemann Hypothesis                    unproved
```
