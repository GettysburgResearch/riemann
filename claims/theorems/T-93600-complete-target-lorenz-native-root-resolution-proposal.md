# T-93600 — Complete Target-Lorenz native-root resolution proposal

Claim ID: `T-93600`  
Status: **CANDIDATE-COMPLETE NATIVE-ROOT PROPOSAL ON FROZEN INPUTS — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93602--L-93605`, `L-91377--L-91380`  
RH status: **unproved pending independent reconstruction**

For every integer `X>=10^12`, the construction supplies one finite row `d_X`
such that

\[
\boxed{d_X\ge0,}
\]

\[
\boxed{C_{d_X}(q)\le w_X(q),
\qquad
\Xi_{d_X}(q)\le\Omega_X(q)
\quad(q\ge2),}
\]

and

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<61000.
}
\]

The source ledger is atomwise and one-use. The same Target-Lorenz coefficient
vector is used in target, score and all rows. Actual rough-child responses stay
inside the one common row. Mismatch, collar and terminal data occur only in the
signed observation ledger. The exported recursive family is empty, and the
root-global port is zero.

This is the exact producer strength requested by the Native-Root Capacity
Theorem, in the equivalent bounded `Y_4`-weighted-slack form.

## Immediate falsifiers

Reject this proposal at the first failure of any of the following:

```text
one compact or tail proportional determinant cell is nonpositive;
the stopped-leaf weights do not reproduce the frozen source tree;
one leaf uses different source coefficients in different rows;
a signed mismatch/collar/terminal vector enters the positive source measure;
a source atom has two owners;
a full child capacity is substituted for an actual child response;
any physical column q>=2 exceeds native detail capacity;
the root-global port or exported recursive family is nonzero;
the direct Y4 charge is at least 61000.
```
