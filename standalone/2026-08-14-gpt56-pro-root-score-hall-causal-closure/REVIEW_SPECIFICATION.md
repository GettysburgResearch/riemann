# Independent review specification

Review target: `T-91657` on branch `research/gpt56-pro/91683-root-score-hall-causal-closure`.

## Required order

### 1. Domain firewall

Reproduce PR #456's stopped-leaf counterexample at

```text
p=67, y=13, py=871, threshold=13.
```

Verify that no theorem in this packet applies Hall to that domain.

### 2. Root Hall certificate

Re-run every fixed-window score Hall endpoint check for

\[
1\le x\le c_0^{-1}<54.2192.
\]

Confirm the strict margin `>3/100`, source support `e<=o`, score equality, and `0<=nu_x(e)<=1`.

### 3. Simultaneous target and row identities

Using the same transport coefficients, reconstruct:

\[
\text{signed target}
=
\text{positive residual target}+	ext{positive slack},
\]

and, for every row `j>=2`,

\[
\text{signed row}
=
\text{positive Hall bonus}+	ext{positive residual row}.
\]

Reject the packet if target, score, and rows use different source allocations.

### 4. Native responses

Reconstruct the exact finite response formulas and Möbius collapse. Verify simultaneously for every physical integer column

\[
\Gamma(B_X;q)+\Gamma(R_X\widehat Z_X;q)=w_X(q),
\]

\[
\Xi(B_X;q)+\Xi(R_X\widehat Z_X;q)=\Omega_X(q).
\]

For the signed detail identity, apply ordinary maps at `q` and `4q` before subtraction.

### 5. Endpoint-frame realization

Verify the deterministic Hall map is measurable and that the positive endpoint-frame producer satisfies the hypotheses of `L-91674`. Reconstruct the positive outer density, common-parent pushforward, one global quantization, finite/continuum mismatch bound, safety factor, top omission, terminal taper, and finite base.

Confirm that every finite correction is current and charged once after summation. A failure here retracts `L-91673`'s realized root bound and `T-91657`.

### 6. Causal envelope

Reconstruct the exact coefficients

\[
s_k+\sum_i\lambda_i=1,
\qquad
\sum_i\alpha_i<1/8,
\]

causal target/row/ordinary/detail positivity, compact literal debt, and same-index child covariance. Check that the actual child coefficient is not square-root scaled twice.

### 7. Conclusion chain

Verify the equality-deficit envelope, the benchmark estimate

\[
J_\Lambda(X)<4\sqrt X+4\log X,
\]

the finite dual orientation

\[
F_\Lambda(X)\le J_\Lambda(X)-\operatorname{Score}(d_X),
\]

and the frozen one-sided endpoint-to-RH implication.

## Immediate falsifiers

```text
stopped-leaf Hall appears;
a root Hall fiber exceeds the certified window;
a source atom has two owners;
independent current pieces are each tested against the full parent budget;
a signed radix-four map is assumed positive on arbitrary rows;
a root-only correction is copied to a child;
endpoint integration or quantization changes the source coefficients;
C_fin or C_cau depends on X;
the external endpoint sign is reversed.
```

## Required verdict language

Until all frozen analytic and finite inputs are reconstructed, classify the result as

```text
candidate complete proof proposal / RH unproved.
```
