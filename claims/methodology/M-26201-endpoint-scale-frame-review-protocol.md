# M-26201 — Endpoint-scale frame adversarial review protocol

Method ID: `M-26201`  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Scope: `L-26201`--`L-26203`, `T-26201`, and `X-26201`

## 1. Freeze

Record the exact head SHA of the proposal branch and the exact inherited head of
PR #248.  A later repair is a new proposal and may not retroactively verify the
frozen object.

## 2. Review order

1. `L-26201` Section 2: parabolic row positivity;
2. `L-26201` Section 3: endpoint-increment positivity, including the two
   entering boundary rows;
3. `L-26201` Section 4: response support and diagonal formula;
4. `L-26202` reciprocal-cell integration and signs;
5. `X-26201` exact rational interval gates;
6. `L-26203` scale-greedy residual induction;
7. `L-26203` diagonal slack and interval-freeze identities;
8. `L-26203` diagonal `q^(-3/2)` bounds;
9. `T-26201` use of PR #244's mass--slack theorem;
10. the source-pinned square-screw/Landau consumer.

## 3. Required independent derivations

A reviewer should derive independently:

\[
 A_X''>0,
\]

\[
 \partial_{\log Y}A_Y(x)
 =\frac{2(\sqrt x-x/\sqrt Y)}{x-1},
\]

\[
 H_N(\theta)
 =4N\theta-4+\sqrt\theta
 [4-4S_N-2A_N-2(S_N+1)\log\theta],
\]

\[
 K_N-K_{N-1}
 =(S_{N-1}+1)\log(N/(N-1))-2/\sqrt N,
\]

and

\[
 s_X^{\rm sc}(T-1)=\Gamma_T(T-1)\ell_T.
\]

Agreement between the prose proof and the independent derivation is required.

## 4. Mandatory mutations

The following changes must be detected.

### Atom mutations

1. replace `b_X/(m-1)` by `b_X/m`;
2. omit the entering row `T-2`;
3. extend the endpoint atom one row beyond its support;
4. reverse the sign of one endpoint difference;
5. use only pointwise positivity of `b_X` instead of convexity of `A_X`.

### Tail mutations

6. reverse `g=-B'`;
7. omit the factor `1/k` in the integrated dilation sum;
8. change the target primitive by the sign of `2 sqrt(theta) log theta`;
9. use a floating check for `K_16` in place of the rational enclosure;
10. delete one reciprocal-cell boundary convention.

### Greedy mutations

11. use a response column with `q>=T`;
12. choose a nonminimum ratio;
13. allow a negative endpoint weight;
14. charge final column `T-1` to a later atom;
15. claim residue-class rather than contiguous scale freezing;
16. replace `Gamma_(q+1)(q)` by `beta_(q,q)` in the slack sum.

Every mutation above must fail either the human proof or the checker schema.

## 5. Exact versus reconnaissance firewall

`X-26201` has two assurance classes.

```text
EXACT_RATIONAL_INTERVAL
    K_16 and the first fourteen reciprocal-cell derivative gates;

HIGH_PRECISION_DECIMAL_RECONNAISSANCE
    finite endpoint atoms and finite scale-greedy behavior.
```

The second class may detect algebraic regressions and suggest blocker geometry.
It may not certify:

- positivity for all endpoints;
- `ESBT` or `ESGS`;
- any asymptotic exponent;
- RH.

## 6. Automatic UNPROVEN verdicts

Classify the full proposal `UNPROVEN` if any of the following is absent:

1. a uniform proof of `ESBT` or `ESGS`;
2. a complete finite-floor ledger for the continuum-tail transfer;
3. the exact fixed-ratio Möbius mutation;
4. an independently audited mass--slack normalization;
5. the correct one-sided Landau orientation.

A flaw in one proposed derivation does not make the endpoint frame or the
continuum theorem false unless an exact hypothesis-matching counterexample is
supplied.

## 7. Preferred production object for `ESBT`

For every endpoint `X`, export:

```text
all endpoint atoms a_T;
all response columns Gamma_T;
all residual rows before and after each step;
all blockers q_T;
all weights lambda_T;
all diagonal candidates and losses ell_T;
all maximal frozen intervals;
reciprocal-cell labels crossed by each interval;
continuum tail budget assigned to each interval;
finite-floor error and terminal-scale charge;
final total slack.
```

The symbolic proof must establish a uniform square-root/polylogarithmic loss.
Finitely many passing endpoints remain reconnaissance.
