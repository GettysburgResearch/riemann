# X-23601 — Exact carry Green regression

This standard-library experiment checks the finite algebra behind the
carry–digital–Selberg proposal.

It verifies:

- the exact carry count in every tested binomial row;
- the affine Möbius contraction
  \[
  \sum_{k\le n/m}\mu(k)\beta_{n,mk}
  ={2m-n-1\over n+1};
  \]
- the closed triangular inverse on an exact rational datum;
- the prime-power valuation identity for average logarithmic binomial
  coefficients;
- the dyadically aligned inverse coefficients `a_2(n)=v_2(n)+1`;
- the binary digit identity
  \[
  \sum_{n\le N}[1-v_2(n)]=s_2(N);
  \]
- the elementary derivative inequalities used by the carry Green spline.

Run:

```bash
python3 verify.py
python3 -m unittest discover -s tests -v
```

Retained verdict:

```text
SYNTHETIC_CARRY_GREEN_ALGEBRA_VERIFIED
```

Proof-object SHA-256:

```text
65dfd3a503e16fee8a5e64b7354d36b43b1ae02e617fc31e666f2fac93c9c0ce
```

## Scope boundary

This is a finite exact regression only. It does **not** verify:

- the quotient-layer identity `(L-23603.15)`;
- conditional-Hankel positivity of the complete source;
- continuum positivity of `mathfrak C`;
- a cofinal carry minorant;
- the Riemann Hypothesis.
