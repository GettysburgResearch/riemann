# Repository-wide attack: greedy carry minorant and parity-digit blocker theorem

Authoring agent: `gpt56-pro-22`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Frozen parent: PR #236 at `0a8ede99666b8ad01b661da0cc21959c56486a8d`  
Status: **FULL PROPOSAL; ONE AGGREGATE DIGITAL BLOCKER THEOREM OPEN; RH NOT CLAIMED PROVED**

## Executive conclusion

The newest repository work makes the arithmetic frontier smaller and more
honest than the review supplied to this pass.

1. The original Farey determinant completion remains rejected.
2. The reflected Selberg identity is useful, but its endpoint-count theorem does
   not estimate the balanced all-truncated Möbius sector.
3. The first-order terminal routing required repair; PR #235 supplies a direct
   full-tuple terminal/balanced partition.
4. PR #234 reduces the surviving core to one fixed-ratio Mertens shell.
5. PR #236 proves exact causal equivalence of every fixed ratio and reduces the
   dyadic shell to stable inversion of one positive parity comb.
6. The affine ground-state route on PR #202 has also reached an RH-bearing
   central-cardinal obstruction rather than a routine profile estimate.

The common lesson is that another generic upper bound or inverse theorem is not
the right attack. The present proposal instead constructs a positive finite
**lower certificate** for the prime ramp and asks only for aggregate near
saturation.

The proposal is

```text
exact carry matrix
-> canonical nonnegative greedy minorant
-> positive average-binomial prime factorization
-> entropy lower bound
-> Digital Blocker Theorem
-> 4 sqrt(X) prime-ramp lower bound
-> square-screw polylogarithmic negative part
-> Landau pole exclusion
-> RH.
```

The sole open theorem is explicit:

```text
M_X=sum n d_X(n) >= 8 sqrt(X)-polylog(X),
L_X=sum d_X(n)(log(n+1)+3) <= polylog(X),
```

for the exact greedy carry vector `d_X`.

## 1. Latest frozen state

### PR #235: terminal review and repair

Frozen head:

```text
1a86fd1f645d0ca208c0689bf2f0b41ae6448858
```

Its review verifies the one-row Euler theorem, rejects the recursive routing in
`L-15450`, and repairs the terminal family by a direct full-tuple partition.
The terminal family is therefore plausible and sharply reviewable, while the
balanced Möbius packet remains RH-bearing.

### PR #234: one fixed-ratio shell

Frozen head:

```text
2d5043070e15fe6be94307381f4023eaa48c17a5
```

The source is

\[
I_c(x)=M(x)-M(cx),
\qquad
Q_c(t)=e^{-t/2}I_c(e^t),
\]

with transform

\[
\widehat Q_c(z)
=
\frac{1-c^{z+1/2}}{(z+1/2)\zeta(z+1/2)}.
\]

Its local block energy is an explicit positive balanced Gram on the actual
Möbius vector. At `c=2/3` it is exactly the first Farey-cell Mertens firewall.

### PR #236: causal ratio transfer and parity comb

Frozen parent head:

```text
0a8ede99666b8ad01b661da0cc21959c56486a8d
```

It closes the following exact transfers.

- Every fixed ratio is a causal `ell^1` filter of every other fixed ratio.
- The triangular renewal forcing is a bounded causal self-map.
- The dyadic shell is a first-order Sobolev primitive of
  \[
  b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).
  \]
- The positive binary-digit kernel
  \[
  S_2(t)=e^{-t/2}s_2(\lfloor e^t\rfloor)
  \]
  and the positive parity comb
  \[
  P_2(t)=e^{-t/2}\mathbf1_{\lfloor e^t\rfloor\text{ odd}}
  \]
  turn the dyadic source into elementary two- and three-tap exponentials.

The parity-comb transform is

\[
\widehat P_2(z)=\frac{\eta(z+1/2)}{z+1/2}.
\]

Thus generic stable inversion is already RH-bearing. This exact reduction is
valuable, but it does not itself provide the missing coercivity.

### PR #226: reflected Selberg proposal

Current head at this pass:

```text
63a4d7c0f482a57893db420e64b22f6a605c72e6
```

The reflected coefficient identity genuinely produces a Hermitian square.
However, the current endpoint-coordinate theorem does not control the balanced
Möbius packet, and the claimed higher Mertens-difference export is not automatic.
The reflected square remains a possible component of the present DBT mechanism,
not a completed proof by endpoint counting.

### PR #202: affine route

Current head at this pass:

```text
d4c8e59f8f3f992a76fd48ad13bef78505dca7cc
```

The affine source reservoir and min-max transfer are durable. The latest
cardinal audit proves that the remaining central profile theorem already
excludes the off-line cardinal block. Thus the route is conditionally complete
but still RH-bearing at its arithmetic profile gate.

## 2. Why another BTP upper bound is not the only option

The shell and BTP routes seek an upper bound for a signed quadratic Möbius
object. The parity-comb route seeks a lower singular-value estimate for a
positive convolution kernel. Both contain the hypothetical off-line mode in
their ambient function spaces.

The carry route admits a different polarity.

For every finite endpoint it constructs a vector

\[
d_X(n)\ge0
\]

such that

\[
B_Xd_X\le w_X.
\]

Because the von Mangoldt coefficients are nonnegative, the inequality is in the
right direction for a prime-ramp lower bound. No inverse of a Möbius operator is
needed.

The exact triangular inverse `c_X` is not sacred. Its pointwise positivity may
be a stronger theorem than RH requires. What matters is retaining the sharp
leading entropy mass.

## 3. Exact greedy construction

The carry matrix is

\[
\beta_{nq}
=
\frac{
 \lfloor n/q\rfloor(q-1-(n\bmod q))
}{n+1}.
\]

Initialize the residual by

\[
\rho_X^{(X)}(q)=q^{-1/2}\log(X/q).
\]

At stage `n`, put

\[
d_X(n)
=
\min_{\beta_{nq}>0}
\frac{\rho_X^{(n)}(q)}{\beta_{nq}}
\]

and subtract this multiple of row `n`.

The diagonal entry

\[
\beta_{nn}=(n-1)/(n+1)
\]

is positive. Therefore the minimum exists, every coefficient is nonnegative,
and every residual stays nonnegative. The result is a canonical feasible vector
with no solver inside the trust boundary.

The algorithm also emits the exact blocker

\[
q_X(n)=\operatorname*{argmin}_{\beta_{nq}>0}
\rho_X^{(n)}(q)/\beta_{nq}.
\]

This blocker/slack ledger is the finite arithmetic object DBT must control.

## 4. Exact prime factorization

For a prime power `q=p^k`, `beta_(nq)` is the average indicator of a base-`q`
carry in the addition `j+(n-j)=n`. Kummer and Legendre give

\[
G_n
=
\frac1{n+1}\sum_{j=0}^n\log{n\choose j}
=
\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.
\]

Thus

\[
\sum_{q=p^k\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge
\sum_{n=2}^X d_X(n)G_n.
\]

This is the exact positive bridge from carries to primes.

## 5. Entropy supplies the archimedean constant

An elementary binomial-mode bound gives

\[
G_n\ge n/2-\log(n+1)-3.
\]

Define

\[
\mathfrak M_X=\sum n d_X(n),
\qquad
\mathfrak L_X=\sum d_X(n)(\log(n+1)+3).
\]

Then

\[
\mathcal P(X)
\ge
\frac12\mathfrak M_X-\mathfrak L_X.
\]

Hence DBT gives

\[
\mathcal P(X)\ge4\sqrt X-O(\log^A X),
\]

which exactly cancels the `4 sqrt(X)` square-screw archimedean term.

## 6. The Digital Blocker Theorem

The exact remaining theorem is

\[
\boxed{
\mathfrak M_X
\ge8\sqrt X-C\log^A(2X),}
\]

\[
\boxed{
\mathfrak L_X
\le C\log^A(2X).}
\]

This theorem permits:

- off-diagonal blockers;
- positive carry slack;
- sign changes in the exact inverse coefficients;
- infinitely many quotient layers.

It forbids only a macroscopic loss of the sharp entropy mass.

This is both weaker and more proof-facing than full Carry Saturation.

## 7. Proposed mechanism for DBT

### Complete quotient layers

Group all blocker events with the same quotient

\[
r=\lfloor n/q\rfloor
\]

before applying any inequality. On one quotient cell, the carry kernel is affine
in the remainder. The complete cell is controlled by its two endpoints plus a
finite carry boundary ledger.

### Digit martingale reserve

For each prime `p`, the sum of the `p^k` carry indicators is a base-`p` digit
loss. The binary case is exactly coupled to the positive kernels `S_2` and
`P_2`. The finite identities

\[
\sum_{m\le N}b_2(m)
\mathbf1_{\lfloor N/m\rfloor\text{ odd}}
=0
\quad(N\ge4)
\]

and

\[
\sum_{m\le N}b_2(m)s_2(\lfloor N/m\rfloor)
=-1
\quad(N\ge2)
\]

are the boundary mutations.

### Reflected square only for the unmatched part

The reflected Selberg identity should be used after complete quotient-layer and
digit recombination, only for the parity component not paid by conditional
variance. This avoids importing a generic BTP estimate and avoids claiming that
endpoint count removes the balanced source.

### Lower-scale telescoping

Every nonboundary residual must be routed to a strictly smaller endpoint.
Summing the geometric endpoint ladder leaves a polylogarithmic boundary debt.
The desired final ledger is

\[
8\sqrt X-\mathfrak M_X+\mathfrak L_X
\le C\log^A(2X).
\]

This is exactly DBT, with no hidden operator quantifier.

## 8. Exact regression

`X-23701` verifies:

```text
carry-count rows                    276
binary Kummer rows                  322
parity convolution through N        512
digit convolution through N         512
rational greedy endpoint            24
minimum greedy coefficient          0
minimum residual slack              0
mutation tests                       6/6 PASS
```

Proof-object bindings:

```text
verify.py
bcd49b987615bad83a6468687513b6a59f8b43f396458f964f18ee7c50eddc95

tests/test_verify.py
f47b9a632fdc4012716a5bfe796529481ccdb24b214c4cb488fb68f433e5190a

results/synthetic-verification.json
7328aebc262ccafda0691c8fd7b94b6c2854d17d67f3ec2e717b5c7f650b819f
```

The regression is exact finite algebra only. It does not test DBT.

## 9. Serious resolution path

```text
canonical greedy carry vector
-> symbolic quotient-layer blocker identity
-> multi-base digit conditional-variance ledger
-> parity boundary mutation
-> reflected square for unmatched residue
-> polylogarithmic cumulative blocker debt
-> DBT
-> prime ramp >= 4 sqrt(X)-polylog(X)
-> square-screw Landau transfer
-> RH.
```

The next mathematical object should be a complete symbolic blocker packet for
one quotient layer, not a larger numerical endpoint. It must display all
endpoint cancellations and the exact lower-scale route.

## 10. Honest status

```text
greedy carry minorant                 PROPOSED EXACT
carry/prime factorization             PROPOSED EXACT
entropy transfer                      PROPOSED EXACT
carry/parity digital dictionary       PROPOSED EXACT
Digital Blocker Theorem               OPEN
conditional deduction DBT -> RH       PROPOSED COMPLETE
Riemann Hypothesis                    NOT PROVED
```

This is an ambitious full proposal, not a verified proof. Its advantage is that
the one remaining theorem is finite, canonical, weaker than Carry Saturation,
and cannot hide the Möbius shell behind an arbitrary packet norm.