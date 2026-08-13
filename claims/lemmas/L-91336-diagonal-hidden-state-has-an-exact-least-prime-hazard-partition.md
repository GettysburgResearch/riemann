# L-91336 — The diagonal hidden state has an exact least-prime hazard partition

Claim ID: `L-91336`  
Status: **PROVED EXACT POSITIVE SOURCE-DISINTEGRATION THEOREM**  
Created: 2026-08-12  
Depends on: `L-91317`, `L-91329`, `L-91335`  
RH status: **unproved**

## 1. One ordered active prime set

Fix a source atom with parent endpoint `x` and node `n`. Let

\[
 p_1<p_2<\cdots<p_k
\]

be exactly the rough primes active at that atom, i.e.

\[
 p_jn\le x.
\]

For the two diagonal hidden modes define

\[
 q_j^{X}=A_{p_j}=1-\frac1{p_j},
 \qquad
 q_j^{Y}=B_{p_j}=1-\frac1{\sqrt{p_j}}.
\tag{L-91336.1}

Both numbers lie in `(0,1)`.

## 2. Exact hazard weights

For `sigma in {X,Y}`, put

\[
 s_0^\sigma=1,
 \qquad
 s_j^\sigma=\prod_{i=1}^jq_i^\sigma,
\tag{L-91336.2}

and

\[
\boxed{
 h_j^\sigma
 =(1-q_j^\sigma)s_{j-1}^\sigma.
}
\tag{L-91336.3
}

Then

\[
 s_{j-1}^\sigma-s_j^\sigma=h_j^\sigma,
\]

so telescoping gives

\[
\boxed{
 s_k^\sigma+\sum_{j=1}^kh_j^\sigma=1.
}
\tag{L-91336.4
}

Every term is nonnegative. Explicitly,

\[
\boxed{
 h_j^X
 =\frac1{p_j}
  \prod_{i<j}\left(1-\frac1{p_i}\right),
}
\tag{L-91336.5
}

and

\[
\boxed{
 h_j^Y
 =\frac1{\sqrt{p_j}}
  \prod_{i<j}\left(1-\frac1{\sqrt{p_i}}\right).
}
\tag{L-91336.6
}

These are genuine least-prime hazard probabilities, not upper bounds.

## 3. Four-state matrix partition

In the positive hidden state of `L-91335`, define diagonal matrices

\[
 H_j=\operatorname{diag}
 (h_j^X,h_j^X,h_j^Y,h_j^Y)
\tag{L-91336.7}

and

\[
 S_k=\operatorname{diag}
 (s_k^X,s_k^X,s_k^Y,s_k^Y).
\tag{L-91336.8}

Equation (L-91336.4) gives the exact positive matrix partition

\[
\boxed{
 S_k+\sum_{j=1}^kH_j=I_4.
}
\tag{L-91336.9
}

Consequently, for every positive hidden source packet `z`,

\[
\boxed{
 z=S_kz+\sum_{j=1}^kH_jz
}
\tag{L-91336.10
}

with coefficientwise nonnegative and disjointly labelled pieces.

The raw hidden `ell^1` mass is spent exactly once:

\[
\boxed{
 \|S_kz\|_1+\sum_j\|H_jz\|_1=\|z\|_1.
}
\tag{L-91336.11
}

This is the source-level subprobability identity missing from the earlier
parallel one-prime construction.

## 4. Child-scale meaning

The `X`-mode hazard `1-A_p=1/p` is exactly the multiplicative scaling of the
square-root mode under the shift `n->pn`. The `Y`-mode hazard
`1-B_p=1/sqrt(p)` is exactly the corresponding scaling of the constant mode.

Thus `H_jz` is the hidden state whose first active rough prime is `p_j`; it is
placed at the canonical child endpoint

\[
\boxed{x/p_j.}
\tag{L-91336.12
}

The survival packet `S_kz` contains no active rough prime and remains in the
finite forcing/frontier channel.

For every rough prime `p_j>=67`,

\[
 x/p_j<c_0x.
\]

Hence every nontrivial hazard child enters the next factor-54 generation.

## 5. Why there is no overdraw

`R-91305` applied the full parent atom independently to many primes. The correct
branch packet is instead `H_jz`, which includes the survival product of all
smaller active primes.

Equation (L-91336.9) proves exactly

\[
 \sum_jH_jz\le z
\]

coefficientwise. No union bound, prime-sum estimate or asymptotic sieve theorem
is used.

The partition is the algebraic least-prime decomposition of the diagonal Euler
semigroup.

## 6. Pointwise activation and measure disintegration

The active set depends measurably on the source atom `(x,n)`. Apply
(L-91336.10) pointwise to a positive hidden-state endpoint/source measure and
integrate. Monotone convergence gives

\[
\boxed{
 \mu^{\rm parent}
 =\mu^{\rm survival}+\sum_{p\ge67}\mu^{(p)}
}
\tag{L-91336.13
}

as an exact equality of positive hidden-state measures.

Every branch measure `mu^(p)` is supported on the canonical child endpoint
coordinate `x/p` and carries the unique least-prime label `p`. Therefore the
parallel rough branches are source-disjoint even if their physical supports
overlap after color erasure.

## 7. Target and score partition

Apply the positive scale-free target kernel of `L-90028` to every scalar hidden
coordinate. Linearity gives the identical target disintegration

\[
\boxed{
 \nu^{\rm parent}
 =\nu^{\rm survival}+\sum_{p\ge67}\nu^{(p)}.
}
\tag{L-91336.14
}

Thus the parent target is used once.

Any positive linear score functional also partitions additively. If a branch is
renormalized to unit hidden mass, its inherited score-loss coefficient is its
mass fraction. Equation (L-91336.11) therefore supplies the exact
subprobability weights required by `T-91302` before physical observation costs
are added.

The physical observation and projective correction are assembled globally by
the common Hilbert endpoint port of `L-91333/L-91334`, not charged once per
branch.

## 8. Sum before quantization

Push every child measure to the parent endpoint coordinate, sum the survival and
all hazard branches, and only then apply the single B-spline quantization and
finite collar repair of `L-91329`.

Because (L-91336.13)--(L-91336.14) are positive measure equalities, this operation
never invokes finite feasibility at a fractional column and never spends one
physical target twice.

## 9. Proof boundary

```text
coordinatewise least-prime hazards                 EXACT
survival + all hazards = identity                  EXACT
positive four-state source partition               EXACT
canonical child endpoint x/p                       EXACT
factor-54 contraction                              EXACT
measure-valued least-prime disintegration          EXACT
target and positive-score disintegration           EXACT
physical observation through one global port       AVAILABLE / L-91334
one-use finite quantization/collar                  AVAILABLE / L-91329
full reset synthesis                               NEXT THEOREM
Riemann Hypothesis                                 UNPROVEN
```
