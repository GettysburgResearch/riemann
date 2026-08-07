# Carry Sandwich: an elementary finite-cone proposal for RH

Agent: `gpt56-pro`  
Date: 2026-08-07  
Issue: #238  
Branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: **FULL PROPOSAL PENDING INDEPENDENT REVIEW; RH NOT CLAIMED PROVED**

## Frozen comparison points

This proposal was developed after comparing the active global routes at the
following heads:

```text
PR #202  b353164805c794c033051dad7b006961a7065d78
PR #216  b76eef1b769584aa9d66d082bfc6634126f986a2
PR #226  63a4d7c0f482a57893db420e64b22f6a605c72e6
PR #236  b303fb8f09cf241be782c64356ae2d3c0012c108
```

The reflected Selberg identity is valuable, but the endpoint-face audit leaves
the balanced Möbius packet open. The high-order Type-II architecture likewise
reduces to a Möbius safe-energy theorem. The present route asks for a weaker
scalar certificate: a finite nonnegative carry sandwich.

## Executive proposal

For each `X`, let

\[
\beta_{nq}
=\frac{\lfloor n/q\rfloor(q-1-(n\bmod q))}{n+1}
\]

and

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

The average logarithmic binomial row

\[
G_n={1\over n+1}\sum_{j=0}^{n}\log\binom nj
\]

satisfies exactly

\[
G_n=\sum_{p^a\le n}\Lambda(p^a)\beta_{n,p^a}.
\]

Construct two nonnegative vectors:

\[
B_X^Td_X\le w_X\le B_X^Te_X.
\]

If their entropy values obey

\[
\sum_nd_X(n)G_n
\ge4\sqrt X-X^{o(1)},
\]

\[
\sum_ne_X(n)G_n
\le4\sqrt X+X^{o(1)},
\]

then the complete prime-power ramp is squeezed to

\[
\sum_{q=p^a\le X}{\Lambda(q)\over\sqrt q}\log{X\over q}
=4\sqrt X+X^{o(1)}.
\]

Its Laplace transform is

\[
{-\zeta'/\zeta(z+1/2)\over z^2}.
\]

Subtracting the exact pole term `4/(z-1/2)`, the subexponential physical-space
error gives a holomorphic function throughout `Re z>0`. An off-line zero would
create a pole there. Hence RH.

This entire deduction is `T-23801`.

## Exact new algebra

The finite carry matrix has the Möbius adjoint

\[
\boxed{
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
={2m-n-1\over n+1}.}
\]

For the exact triangular inverse, this yields

\[
 c_j
 ={(j+1)[j u_j-(j-2)u_{j+1}]
  +2\sum_{m=j+2}^{X}u_m
 \over j(j-1)},
\]

where

\[
u_m
=m^{-1/2}\sum_{k\le X/m}{\mu(k)\over\sqrt k}
 \log{X/m\over k}.
\]

Thus the elementary finite matrix contains the balanced Möbius channel
explicitly. The proposal does not conceal that fact.

## Why the sandwich is weaker than Carry Saturation

Exact Carry Saturation demands that the unique equality solution

\[
B_X^Tc_X=w_X
\]

satisfy `c_X>=0` coordinatewise.

The present route permits:

- one nonnegative vector below the target;
- a different nonnegative vector above it;
- sparse negative entries of the exact inverse;
- off-diagonal greedy saturation.

The canonical choices are:

- descending minimum-ratio greedy packing `d_X^gr`;
- positive part `c_X^+` as a cover.

The sharp theorem may therefore be proved by controlling only a weighted
negative mass and the packing-covering gap, rather than every coefficient sign.

## Proposed quotient-layer mechanism

On the cell

\[
X/(r+1)<m\le X/r,
\]

only `mu(1),...,mu(r)` enter the Möbius coordinate. The proof is required to:

1. combine the complete quotient cell before taking a sign or norm;
2. pair greedy slack with canonical-cover excess;
3. telescope the affine tail terms supplied by the Möbius adjoint identity;
4. retain only floor and cell-boundary ledgers;
5. prove that the total weighted obstacle is `X^(o(1))`.

The load-bearing statement is the Carry Obstacle theorem `CO(X)` in `M-23801`.
It is finite, elementary, and sharply falsifiable.

## Finite reconnaissance

The exact checker validates the finite algebra and small greedy feasibility. A
separate double-precision scan through `X=5000` found:

```text
all tested greedy saturation columns diagonal
all tested inverse coefficients nonnegative
signed half-n mass at X=5000
  4 sqrt(X) + 0.139756...
entropy value at X=5000
  4 sqrt(X) - 26.625648...
entropy deficit / log(X)
  3.126105...
```

The progression is consistent with the desired polylogarithmic ledger, but it
is discovery only.

Exact-interface proof digest:

```text
44b2b584775278a14324650f7709a59b81a9aa4b61c1cab682135b587cfac8bd
```

Nine mutation/interface tests pass.

## Mandatory adversarial questions

1. Is the upper entropy bound `G_n<=n/2` normalized correctly?
2. Does the packing/covering inequality have the correct direction after
   weighting only prime-power columns by `Lambda`?
3. Does the continuous interpolation preserve `X^(o(1))`?
4. Is the pole subtraction in `T-23801` exactly `4/(z-1/2)`?
5. Can one exhibit a quotient layer whose obstacle has power-size negative mass?
6. Does the proposed layer potential actually telescope after floors and
   endpoints are retained?
7. Does the first fixed-ratio Mertens firewall reappear in the complete layer
   ledger rather than being lost by total variation?

Any failure of questions 1--4 rejects the proof spine. Failure of 5--7 rejects
the proposed Carry Obstacle theorem while preserving the exact finite algebra.

## Review order

1. `L-23801-carry-matrix-and-binomial-entropy-ledger.md`
2. `L-23802-carry-packing-covering-duality-and-greedy-producer.md`
3. `L-23803-mobius-adjoint-decoder-for-carry-elimination.md`
4. `T-23801-carry-sandwich-implies-rh.md`
5. `M-23801-carry-sandwich-full-rh-proposal.md`
6. `experiments/X-23801-carry-sandwich/`
7. this report

## Exact status

```text
carry/Legendre matrix algebra       PROPOSED EXACT
packing-covering duality            PROPOSED EXACT
greedy packing and canonical cover  PROPOSED EXACT
Mobius adjoint decoder              PROPOSED EXACT
carry-sandwich-to-RH composition    PROPOSED COMPLETE
Carry Obstacle theorem CO(X)        OPEN / LOAD BEARING
Riemann Hypothesis                  NOT PROVED
```

This is a full review proposal, not a claim that the final finite obstacle
inequality has already been established.