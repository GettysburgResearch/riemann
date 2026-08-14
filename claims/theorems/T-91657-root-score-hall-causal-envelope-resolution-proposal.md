# T-91657 — Root score-Hall plus the causal envelope gives a candidate factor-67 resolution

Claim ID: `T-91657`  
Status: **CANDIDATE COMPLETE RH PROOF PROPOSAL; INDEPENDENT FROZEN-COMMIT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Normative new inputs: `R-91673`, `L-91673`, `L-91674`  
Retained inputs: exact causal coefficient budget `L-91650`, causal datum positivity `L-91654`, compact causal debt `L-91657`, same-index functor `L-91658`, homogeneous packet envelope `T-91650`, fixed-67 entropy theorem `L-91666`, finite dual `L-91660`, one-sided endpoint criterion `L-91662`  
RH status: **unproved pending independent reconstruction**

## 1. Purpose

The stopped-leaf Hall implication used by the previous direct-row proposal is false. This theorem does not repair or reuse it. It moves Hall to the root, where the quotient lies in the certified finite window, and uses the already proved positive causal packet reset at every later rough generation.

## 2. Root entry

The finite equality datum has the exact native ordinary and radix-four responses

\[
\Gamma(c_X;q)=w_X(q),
\qquad
\Xi(c_X;q)=\Omega_X(q).
\]

`L-91673` applies score Hall only at normalized quotients

\[
1\le x\le c_0^{-1}<54.2192
\]

and constructs, with one common set of source coefficients,

\[
\boxed{c_X=B_X+R_X\widehat Z_X,}
\tag{T-91657.1}
\]

where

```text
B_X                         is a nonnegative current row;
R_X Zhat_X                  is a positive recursive certificate row;
score of the residual       equals the signed root score;
target residual             is subordinate with explicit positive slack;
all component-row bonuses   are nonnegative.
```

Applying the same response maps to the displayed row identity gives

\[
\Gamma(B_X;q)+\Gamma(R_X\widehat Z_X;q)=w_X(q),
\tag{T-91657.2}
\]

\[
\Xi(B_X;q)+\Xi(R_X\widehat Z_X;q)=\Omega_X(q).
\tag{T-91657.3}
\]

Thus the current and recursive pieces spend one parent capacity, not two coordinatewise copies. The inherited coarse certificate-mass estimate is

\[
\widehat m(\widehat Z_X)\le54.
\tag{T-91657.4}
\]

## 3. Endpoint-frame realization

The root score-Hall identity is integrated only over the positive certified outer endpoint window. `L-91674` proves the formal commutation with endpoint integration, common-parent pushforward, same-index child placement, ordinary responses, radix-four responses, and one global positive quantizer.

Under the frozen endpoint-frame, quantization, mismatch, safety, and terminal estimates, all current terms are summed before the finite corrections are applied. There is one absolute constant `C_fin` such that the current root equality deficit obeys

\[
\Delta_X^{\rm eq}(B_X)\le C_{\rm fin}.
\tag{T-91657.5}
\]

This is the principal independent-review burden. It imports no global positivity of the reciprocal-zeta equality weight, no stopped-leaf Hall theorem, no negative butterfly center, and no colored-to-physical Schur projection.

## 4. Causal reset after the root

For ordered active rough primes `67<=p_1<...<p_k`, put

\[
r_i=p_i^{-1/2},
\qquad
s_i=\prod_{h\le i}(1-r_h),
\qquad
\lambda_i=r_i s_{i-1},
\qquad
\alpha_i=r_i\lambda_i.
\]

The exact realized identity is

\[
\boxed{
P_X
=s_kP_X
+
\sum_i\lambda_i\bigl(P_X-r_iU_{p_i}P_{X/p_i}\bigr)
+
\sum_i\alpha_iU_{p_i}P_{X/p_i}.
}
\tag{T-91657.6}
\]

Moreover

\[
s_k+\sum_i\lambda_i=1,
\qquad
\rho:=\sum_i\alpha_i<67^{-1/2}<\frac18,
\tag{T-91657.7}
\]

and every child endpoint is at most `X/67`.

Each causal difference in (T-91657.6) is nonnegative in target, component rows, ordinary capacity, and radix-four capacity. Its positive declared-minus-literal debt is uniformly bounded on the compact child window. The same-index functor inserts arbitrary feasible child rows with exactly the coefficient `alpha_i`; there is no double square-root scaling.

## 5. Packet envelope

Let `Lambda_eq(X)` be the worst positive equality deficit among mass-one positive causal certificates at endpoints at most `X`. Positive homogeneity and subadditivity give

\[
\boxed{
\Lambda_{\rm eq}(X)
\le C_{\rm cau}+ho\Lambda_{\rm eq}(X/67),
\qquad \rho<\frac18.
}
\tag{T-91657.8}
\]

Hence

\[
\boxed{
\Lambda_{\rm eq}(X)
\le\frac{C_{\rm cau}}{1-\rho}
<\frac87C_{\rm cau}.
}
\tag{T-91657.9}
\]

Combining the root mass bound, (T-91657.5), and (T-91657.9), the constructed root row satisfies

\[
4\sqrt X-\operatorname{Score}(d_X)\le C_0
\tag{T-91657.10}
\]

for one absolute constant `C_0`, subject to reconstruction of the frozen root realization.

A weaker per-generation implementation would still give `O(log X)` equality deficit and is enough for the endpoint theorem; the subcritical causal envelope gives the stronger bounded form.

## 6. Native parabolic loss

The continuum equality score `4sqrt(X)` is a declared packet score. It is not identified with the literal score of the finite equality row. The native benchmark obeys the unconditional elementary estimate

\[
J_\Lambda(X)<4\sqrt X+4\log X.
\tag{T-91657.11}
\]

Therefore

\[
\begin{aligned}
\mathfrak L_X(d_X)
&=J_\Lambda(X)-\operatorname{Score}(d_X)\\
&=[J_\Lambda(X)-4\sqrt X]
  +[4\sqrt X-\operatorname{Score}(d_X)]\\
&\le4\log X+C_0
=o(\log^2X).
\end{aligned}
\tag{T-91657.12}
\]

## 7. Finite dual and endpoint conclusion

For every ordinarily feasible row,

\[
\operatorname{Score}(d)
=
\sum_q\Lambda(q)\Gamma(d;q)
\le
\sum_q\Lambda(q)w_X(q)=P_\Lambda(X).
\]

Thus

\[
\boxed{
F_\Lambda(X)\le\mathfrak L_X(d_X)=o(\log^2X).
}
\tag{T-91657.13}
\]

The frozen higher-prime-power separation and Mellin-Landau endpoint theorem then give the proposed RH conclusion. The one-sided version is sufficient; no lower bound for `F_Lambda` is used.

## 8. Immediate falsifiers

Reject this proposal upon the first occurrence of any of the following:

```text
stopped-leaf Hall is used;
a root Hall fiber leaves the certified 54.2192 window;
one source atom has two owners;
target, score, and rows use different transport coefficients;
ordinary/detail responses fail to commute with the common root sum;
a finite correction is charged both current and recursively;
the same-index child coefficient is scaled twice;
C_fin or C_cau depends on X;
the finite dual or endpoint sign is reversed.
```

## 9. Exact status

```text
stopped-leaf Hall                              FALSE / REMOVED
fixed-window root score Hall                   DIRECTED EXACT
simultaneous target/score/row decomposition    EXACT
common ordinary/detail root normalization      EXACT
formal endpoint-frame intertwining             EXACT / L-91674
analytic endpoint-frame realization            FROZEN / RECONSTRUCT
causal positive reset                          EXACT
recursive coefficient mass <1/8                EXACT
packet envelope                                EXACT CONDITIONAL
native O(log X) loss                           CANDIDATE COMPLETE
full implication to RH                         PROPOSAL / REVIEW REQUIRED
Riemann Hypothesis                             UNPROVEN
```
