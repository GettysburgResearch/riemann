# Research reset: four-adic annular SHARP candidate

## Headline

The strongest route found in this pass is a direct scale-four induction in the
native carry inverse.

The exact native row \(c_X\) is not constructed from Hall packets or rough
children. Instead, define its scale-four annulus

\[
 a_X^{(4)}=c_X-c_{X/4}.
\]

The new candidate theorem `L-94201` gives a four-block Peano decomposition of
every row coefficient of \(a_X^{(4)}\) into nonnegative square terms. If the
identity survives independent reconstruction, then

\[
 c_X=\sum_{j\ge0}a_{X/4^j}^{(4)}\ge0
\]

for every endpoint. This is full SHARP, with exact native capacities and zero
deficit, and the resident endpoint theorem yields RH.

## Why this route was selected

It removes every repeatedly failing interface:

```text
no signed-to-positive source promotion;
no branchwise child realization;
no root/child capacity duplication;
no activation-cell quantizer;
no directed Target-Lorenz tail;
no port;
no recursive mass normalization;
no asymptotic blocker theorem.
```

The sole load-bearing object is one explicit finite-algebra identity in the
average-binomial inverse.

## Stress tests

The retained checker:

- builds the exact lower-triangular beta matrix;
- solves native rows and scale-four annuli by backward substitution;
- checks every reconstructed ordinary column;
- checks annular and full-row positivity on a deterministic endpoint suite;
- checks nonmultiples of four;
- rejects the unsmoothed step target, whose inverse has negative rows;
- verifies telescoping and native-zero-deficit arithmetic;
- records that RH is not established by the replay.

The computation is deliberately lightweight. It is evidence for the symbolic
identity, not its proof.

## Scientific status

```text
exact inverse/telescope algebra       proved
four-block annular identity           candidate-complete; review required
annular inverse positivity            candidate theorem
full SHARP                            candidate theorem
endpoint/Mellin composition           frozen conditional input
RH                                    proposed, not accepted
```
