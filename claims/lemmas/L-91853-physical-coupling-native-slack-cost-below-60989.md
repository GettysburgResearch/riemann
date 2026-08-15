# L-91853 — The physical-coupling root slack has direct native cost below 60989

Claim ID: `L-91853`  
Status: **CANDIDATE-COMPLETE DIRECT COST THEOREM ON FROZEN ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Primary inputs: sparse `Y_4`, the factor-67 all-column estimate, the terminal omission and the elementary Chebyshev bound  
RH status: **unproved**

For `X>=10^12`, let

\[
 r_X=\Omega_X-\Xi(d_X)\ge0
\]

be the external slack of `L-91851`.

The source and observation ledgers contribute four and only four classes:

1. common square-root thinning;
2. retained-cell mismatch plus intrinsic quantization collar;
3. terminal comparison;
4. positive bottom/top omissions.

Hall transport, causal splitting, physical child placement, label erasure and the one quantizer are internal positive operations and add no fifth cost class.

The frozen estimates give

\[
 \langle Y_4,r_X\rangle
 <12012+4+48972+1=60989.
\tag{L-91853.1}
\]

The signed comparison is paid by absolute `Y_4` domination; it is not paid by a positive-source mass theorem. The exact native dual identity yields

\[
 \boxed{
 0\le J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,r_X\rangle<60989.
 }
\tag{L-91853.2}
\]

No estimate of `J_Lambda(X)-4sqrt(X)` is used.

```text
thinning             <12012
nonterminal           <4
terminal              <48972
omissions             <1
port/base              0
root native deficit   <60989
Riemann Hypothesis     unproved
```
