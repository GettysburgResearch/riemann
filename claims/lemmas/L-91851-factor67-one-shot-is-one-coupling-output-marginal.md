# L-91851 — The factor-67 one-shot row is the output marginal of one explicit coupling

Claim ID: `L-91851`  
Status: **CANDIDATE-COMPLETE PHYSICAL COMPILER ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-15  
Primary frozen inputs: `L-91362`, `L-91690`, `L-91688`, `L-91650`, `L-91658`, `L-91674`, `L-91110`, `L-91733`  
RH status: **unproved**

## 1. Whole-cell endpoint source

For integer `X`, put

\[
 K=\left\lfloor X/67\right\rfloor+1,
 \qquad W=10000,
\]

and use the tagged disjoint union

\[
 \mathcal T_X=
 \coprod_{n=K+2}^{X-W-3}\{n\}\times[0,1).
\tag{L-91851.1}
\]

The tag prevents adjacent cells from sharing a physical boundary point. On `s=n+u`, the quotient `x=X/s` satisfies `1<x<67`. The positive endpoint density is

\[
 d\lambda_X(s)=\frac{2L(X/s)}sds,
\tag{L-91851.2}
\]

with the frozen directed bound `159/500<L<183/100`.

## 2. Fiber Hall coupling

The finite `P_61` source on each quotient fiber is split into even capacity and odd demand in the target normalization of `L-91690`. Let `pi_x(o,e)=t_x(o,e)` be its deterministic no-upward Hall coupling. Then

\[
 (\pi_x)_O=O_x,
 \qquad
 (\pi_x)_E\le E_x,
\]

and the residual even coefficient is the displayed `nu_x(e)`. The target-normalized row theorem gives

\[
 e\le o\Longrightarrow
 \frac{Q_{x/e}(j)}{4\sqrt{x/e}-3}
 \ge
 \frac{Q_{x/o}(j)}{4\sqrt{x/o}-3}.
\]

Hence `L-91850.4` is exactly the simultaneous target/row identity of the frozen root Hall theorem. The Hall bonus is current-owned.

## 3. Rough ownership and causal colours

Attach the least rough prime to every residual source occurrence before labels are grouped. Use the restricted first-owner operator, so a monomial divisible by several rough primes enters only its first owner. Apply the exact causal coefficients

\[
 s_k+\sum_i\lambda_i=1,
 \qquad
 \alpha_i=r_i\lambda_i,
 \qquad
 \sum_i\alpha_i<1/8.
\tag{L-91851.3}
\]

Every current difference and child is a positive typed packet on the frozen causal inputs. Children are placed at the same literal row indices through positive same-index kernels. They remain internal labels of the common physical coupling; the exported recursive family is empty.

## 4. One common quantizer

Sum the Hall bonus, all causal currents and every physically placed child in the common tagged target. Apply the martingale B-spline kernel once. It is indexed only by the physical endpoint state and is independent of all internal labels.

The final nonnegative row is the output marginal

\[
 \boxed{
 d_X(j)=
 \Gamma_X(
 S_X\times A_X\times\mathcal T_X\times\{j\}).
 }
\tag{L-91851.4}
\]

The two Hall input marginals and every first-owner child class remain available for audit before label erasure.

## 5. Native comparison

The quantized continuum output is compared with the exact finite native datum by the retained-cell signed defect and the intrinsic width-three collar. Let `e_X` denote that signed observation vector. Let `u_X` denote the positive unused native capacity from the one common square-root thinning and the bottom/top omissions. The frozen all-column and terminal estimates prove

\[
 e_X(q)\le u_X(q)
 \qquad(q\ge2).
\tag{L-91851.5}
\]

Therefore

\[
 \boxed{
 r_X=u_X-e_X\ge0,
 \qquad
 \Omega_X=\Xi(d_X)+r_X.
 }
\tag{L-91851.6}
\]

The last equality is an observation identity after every internal child has already been physically inserted. It does not assert that `e_X` is positive source.

Positive radix-four inversion gives

\[
 C_{d_X}(q)\le w_X(q)
 \qquad(q\ge2).
\tag{L-91851.7}
\]

## 6. Exact boundary

```text
source owner per Hall marginal                 explicit
complete tagged cells                          explicit
rough first-owner operator                     explicit
child physical placement                       same-index positive kernel
exported child family                          empty after actual placement
one global quantizer                           exact by construction
signed finite comparison                       separate ledger
all physical columns                           frozen all-column estimates
auxiliary Schur port                           absent
Riemann Hypothesis                             unproved
```
