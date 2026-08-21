# L-94001 — The anchored/affine-Volterra split produces one actual finite nonnegative native row

Claim ID: `L-94001`  
Status: **PROPOSED COMPLETE ON FROZEN DIRECTED INPUTS — INDEPENDENT REVIEW REQUIRED**  
Date: 2026-08-16

## 1. Frozen library inputs

The construction uses, as mathematical theorems rather than lineage confirmation:

```text
PR #495 at 50f45b46...   exact Volterra antiderivative and p_s>=0;
review #503 at db77e579... mandatory negative witness and scope firewall;
PR #508 at 4ae97dffd...   directed complete Target–Lorenz typed-leaf theorem;
PR #352 at 906b5a477...   exact prime endpoint Mellin symbol;
PR #353 at ed566f319...   prime-square moat and complete-gap consumer.
```

No theorem from PR #509 is used.

## 2. Native cell partition

For integer `X`, put

\[
K=\lfloor X/67\rfloor+1,
\qquad
W_X=6\lceil\sqrt K\rceil+4.
\]

Partition the exact finite native endpoint cells into

```text
anchored cells:  m<K+2 or m>X-W_X-3;
outer cells:     K+2<=m<=X-W_X-3.
```

The anchored cells remain literal finite native occurrences. Apply the complete directed Target–Lorenz typed-leaf theorem to them. At each leaf the theorem gives a positive residual source `nu`, a current-only nonnegative row bonus `B`, and the exact physical identity

\[
R(\nu)+B=R(E)-R(O).
\]

Summing the exact leaf paths gives one finite coefficientwise nonnegative anchored row `d_(X,A)` with the exact anchored native row observation.

## 3. Outer direct row

On every outer cell one has `1<X/s<67`. Use the positive Volterra row

\[
\int_m^{m+1}\frac{2L(X/s)}s p_s\,ds
\]

and compress it by `L-94000` to two actual finite rows. Summing gives a finite coefficientwise nonnegative row `d_(X,I)`.

Let `E_X^I` be the exact retained-cell finite/continuum defect. The native finite row identity is

\[
\boxed{
c_X=d_{X,A}+d_{X,I}+\mathcal R E_X^I.
}
\]

Define

\[
\boxed{d_X^0=d_{X,A}+d_{X,I}\ge0.}
\]

Then for every ordinary column and every detail column,

\[
C_{d_X^0}(q)=w_X(q)-v_q(E_X^I),
\]

\[
\Xi_{d_X^0}(q)=\Omega_X(q)-\mathcal D_4v_q(E_X^I).
\]

The same actual row is observed at `q` and `4q` before detail is formed. There is no rough-lift parent, derivative-fibre causal operation, exported child, auxiliary port, or bulk quantizer.
