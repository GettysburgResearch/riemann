# T-93920 — Review-503-safe anchored/Volterra direct-row repair

Claim ID: `T-93920`  
Status: **CANDIDATE-COMPLETE COMPOSITION ON FROZEN DIRECTED ANCHORED AND ENDPOINT INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Frozen base: PR #495 at `50f45b46cbe3c471d6e702c41c7ef178b530e1ab`  
Review answered: PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`  
Anchored finite input: PR #508 at `4ae97dffd1f76ed3244b8f3028560ffa80663caf`  
Endpoint inputs: PR #352 at `906b5a477a1ed7c88a40db7569924f15f3d54b72` and PR #353 at `ed566f3198e236c54ba18049181016536f56d456`  
RH status: **unproved pending reconstruction**

## 1. Producer

For every integer `X>=10^12`, `L-93920` constructs the actual row

\[
d_X^0=d_{X,A}+d_{X,I}\ge0,
\]

where:

```text
anchored cells:
    literal finite native occurrences realized by the directed
    Target–Lorenz typed leaf compiler;

bulk complete cells:
    the direct positive Volterra row
    integral 2L(X/s)p_s ds/s;

comparison:
    one signed retained-cell quadrature defect E_X^I.
```

No derivative-fibre current, rough-lift parent, exported child, endpoint quantizer, collar, omission, or auxiliary port occurs.

The exact negative witness

```text
(rough prime, child endpoint, parent endpoint, row)
=(67,15,1005,14)
```

is mandatory and is required to remain strictly negative. The theorem succeeds by never forming that operator.

## 2. All-column realization

With

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24},
\qquad
d_X=\tau_Kd_X^0,
\]

`L-93921` proves for the same row

\[
C_{d_X}(q)\le w_X(q),
\qquad
\Xi_{d_X}(q)\le\Omega_X(q)
\qquad(q\ge2).
\]

Both ordinary `q` and ordinary `4q` are observed on the common row before detail is formed. Every small column `2<=q<K` and every terminal column is included.

## 3. Native deficit

`L-93922` gives

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<3457.
}
\]

Hence the exact finite dual yields

\[
F_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X)
<3457
=o(\log^2X).
\]

## 4. Endpoint consumer

On the frozen unconditional prime-square moat and the frozen Mellin-pole/Landau one-sign theorem, the preceding bound implies that no nontrivial zero has real part greater than one half. Functional-equation symmetry gives the proposed RH conclusion.

This final analytic consumer is not re-certified here. The theorem is a review packet, not an accepted proof of RH.

## 5. Immediate falsifiers

Reject the packet at the first failure of:

1. the exact negative witness in `R-93920`;
2. positivity of `p_s` or of the factor-67 density on the bulk;
3. the directed finite Target–Lorenz theorem on an anchored occurrence;
4. the exact hybrid identity (L-93920.1);
5. the retained-cell error bound;
6. the terminal relative estimate using `W_X`;
7. any omitted `q<K` column;
8. any use of `L-91763`, `T-92910`, or PR #509 as confirmation;
9. the one-sided finite-dual orientation;
10. any use of `J_Lambda(X)-4sqrt(X)`.

```text
L-91760--L-91762                    preserved
review #503                         accepted
new direct-row producer             proposed complete on frozen AVLT
all ordinary/detail columns         proposed complete
native deficit                      <3457
endpoint implication                frozen / reconstruct
Riemann Hypothesis                  unproved pending independent review
```
