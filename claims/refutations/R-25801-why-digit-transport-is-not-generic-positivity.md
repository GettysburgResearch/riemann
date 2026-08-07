# R-25801 — Why digit transport is not generic reflected positivity

Claim ID: `R-25801`  
Title: The new proposal survives the exact zero Schur complement, the Möbius hypercube, and the positive-cover obstruction only because it transports a reciprocal-free signed dipole on the complete source graph  
Status: **PROPOSED SCOPE AND REJECTION THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Targets: PR #250 automatic reserve; unsigned carry covers; bounded-rank packet closures  
Dependencies: `L-25801`--`L-25805`; PRs #239, #250, #251, #254

## 1. Aggregate reflected positivity has zero reserve

If the complete physical source is split as

\[
Q=T+R,
\]

then its aggregate reflected square has block matrix

\[
\begin{pmatrix}
I&I\\
I&I
\end{pmatrix}.
\]

The Schur complement of the lower-right block is

\[
I-I^*I^{-1}I=0.
\]

Thus the aggregate identity cannot give a positive top-source reserve. Making
`R` small proves only that the full and top energies have the same exponent.

`PADT` does not reuse this block. It first applies the exact source-specific
operator

\[
a_Q=\mathbf1*(\varepsilon-\delta_Q)
\]

and transports the reciprocal-free dipole

\[
Z=a_QT.
\]

The recovery `T=H_Q*mu_V*Z` is verified separately. Any proof which replaces
this source operation by the aggregate Schur block has reverted to the rejected
argument.

## 2. The Möbius hypercube refutes rank, not complete-source flow

PR #239 constructs, for every `K`, an exact same-sign Möbius product cube of
affine rank `K` inside one fixed-ratio shell. It refutes:

```text
every surviving balanced face has absolute rank O(1).
```

The cube is obtained after retaining only the all-large Möbius corner. Each
coordinate toggle which moves a divisor below `V` leaves that corner and enters
a lower-depth sibling.

`PADT` requires those siblings in its source graph before the flow is formed.
Its proposed contraction is a divergence identity across the complete
allocation graph, not an enumeration of the isolated top face.

Therefore the hypercube is a mandatory mutation:

- if its lower-depth siblings are absent, reject the certificate;
- if they are present but the signed flow cost is not bounded, `PADT` remains
  open;
- the cube alone does not refute the proposed transport theorem.

## 3. Positive cover has square-root cost

PR #254 proves that replacing a signed constraint dipole by its positive part
forces a fixed square-root cost on one explicit carry seed. The same logical
failure applies here.

The depleted source is

\[
Z=Z^{\rm current}-Z^{\rm shifted}.
\]

A valid producer must transport current defect into shifted slack before taking
absolute values. A nonnegative cover of `Z^current` is not a substitute and is
expected to lose the sharp exponent.

## 4. The positive kernel is not generically coercive

The transform of `C_Q` contains `zeta(s)`. Generic inversion of convolution by
`C_Q` in the counterexample strip would exclude every off-line zeta zero and is
therefore already RH-bearing.

`PADT` does not claim such an inverse. It uses:

\[
T=H_Q*\mu_V*(\partial+1/2)(C_Q*T),
\]

which is valid only because `r_V*T=0` on the finite coefficient range. The
transport estimate is required only for the resulting exact source.

Any certificate which asserts a lower bound for `C_Q` on arbitrary functions is
rejected.

## 5. Almost-all Type-II estimates do not supply the theorem

The 2026 higher-uniformity Type-II machinery for multiplicative functions gives
powerful estimates on almost all intervals and uses contagion to scale
approximate structure. `PADT` requires a deterministic certificate on every
sufficiently large physical block and on one exact source vector.

An exceptional-set estimate cannot be inserted without a separate theorem
showing that the fixed-ratio Mertens mode avoids the exceptional set.

## 6. Why the proposal is genuinely narrower than `PARC`

`PARC(K)` asks directly for an upper bound on the top source. `PADT(K)` instead
requires a finite object with the following fixed structure:

1. one explicit radix `Q`;
2. one exact reciprocal-free depletion;
3. one stable recovery filter;
4. one marked prime-power anchor;
5. adjacent-flow incidence;
6. bounded same-scale cluster solves;
7. factor-two child descent;
8. one quadratic two-frequency cost certificate.

A counterexample to any of these finite components rejects the mechanism. The
proposal is therefore more falsifiable than a black-box signed Type-II bound.

## 7. Correct status

```text
aggregate reflected Schur reserve          exactly zero
absolute bounded-rank closure               refuted
unsigned positive cover                     refuted as a sharp mechanism
positive nonmultiple kernel                 exact
source-specific depletion resolvent         exact
adjacent-flow and cluster algebra            exact/proposed source adapter
production PADT transport                    open
PADT family -> RH                            conditional complete
Riemann Hypothesis                           unproved
```

## 8. Proof boundary

This file does not prove `PADT(K)`. It specifies why the proposal is not already
refuted by the known no-go results and prevents those rejected mechanisms from
being silently reintroduced under transport terminology.
