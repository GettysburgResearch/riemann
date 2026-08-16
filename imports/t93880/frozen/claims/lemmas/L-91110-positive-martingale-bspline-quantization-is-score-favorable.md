# L-91110 — Positive martingale B-spline quantization is exact in the bulk and score-favorable

Claim ID: `L-91110` (provisional research range)  
Title: Every nonnegative continuum endpoint density has a canonical local martingale quantization on the integer endpoint-state grid; the quantized endpoint weights are nonnegative, reproduce both parabolic seed modes exactly away from a width-three diagonal collar, and never decrease the exact entropy score  
Status: **PROPOSED COMPLETE EXACT QUANTIZATION / SCORE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91101/L-91102`; the real-endpoint parabolic seed  
Scope: exact continuum-to-finite positive endpoint lift and score comparison; carry/detail feasibility of the local collar remains open

## 1. Continuous endpoint atoms

For real \(s\ge2\), define the zero-extended parabolic seed \(b_s(m)\) as in PR #352. Its endpoint derivative is
\[
\boxed{
 \dot b_s(m)
 :=\partial_s b_s(m)
 =\left(
 \frac{2\sqrt m}{s}-\frac{2m}{s^{3/2}}
 \right)\mathbf1_{m\le s}.
}
\tag{L-91110.1}

The activation value at \(s=m\) is zero, so this is a continuous causal family.

Put
\[
 a(s)=\frac2s,
 \qquad
 r(s)=s^{-1/2}.
\]
Then
\[
\boxed{
 \dot b_s(m)=a(s)[\sqrt m-r(s)m]\mathbf1_{m\le s}.
}
\tag{L-91110.2}

For an integer endpoint \(T\),
\[
 e_T=b_T-b_{T-1}
 =\int_{T-1}^{T}\dot b_s\,ds.
\tag{L-91110.3}

Its two mode coordinates are
\[
 \alpha_T=\int_{T-1}^{T}a(s)\,ds,
 \qquad
 \delta_T=\int_{T-1}^{T}a(s)r(s)\,ds,
\]
and the state node is
\[
 r_T=\frac{\delta_T}{\alpha_T}.
\tag{L-91110.4}

`L-91101` proves that \(r_T\) decreases strictly.

## 2. Local hat kernel on the endpoint-state grid

For \(s\in[T-1,T]\),
\[
 r_{T-1}>r(s)>r_{T+1}.
\]
Define nonnegative hat weights \(q_U(s)\) as follows.

If \(r(s)\ge r_T\), use the bracket \(r_{T-1}\ge r(s)\ge r_T\):
\[
 q_{T-1}(s)=\frac{r(s)-r_T}{r_{T-1}-r_T},
 \qquad
 q_T(s)=\frac{r_{T-1}-r(s)}{r_{T-1}-r_T}.
\tag{L-91110.5}

If \(r(s)\le r_T\), use \(r_T\ge r(s)\ge r_{T+1}\):
\[
 q_T(s)=\frac{r(s)-r_{T+1}}{r_T-r_{T+1}},
 \qquad
 q_{T+1}(s)=\frac{r_T-r(s)}{r_T-r_{T+1}}.
\tag{L-91110.6}

All other \(q_U(s)\) vanish. Then
\[
\boxed{
 q_U(s)\ge0,
 \qquad
 \sum_Uq_U(s)=1,
 \qquad
 \sum_Ur_Uq_U(s)=r(s).
}
\tag{L-91110.7}

This is the canonical nearest-neighbor martingale, or linear B-spline, quantization of the continuous state \(r(s)\).

## 3. Positive discrete endpoint weights

Let \(\lambda(s)\ge0\) be integrable and supported in a compact endpoint interval where both neighboring state nodes exist. Define endpoint-state masses
\[
\boxed{
 M_U=\int\lambda(s)a(s)q_U(s)\,ds
}
\tag{L-91110.8}
and discrete endpoint weights
\[
\boxed{
 \Lambda_U=\frac{M_U}{\alpha_U}\ge0.
}
\tag{L-91110.9}

The quantization preserves both endpoint modes exactly:
\[
\boxed{
 \sum_U\Lambda_U\alpha_U
 =\int\lambda(s)a(s)\,ds,
}
\tag{L-91110.10}
\[
\boxed{
 \sum_U\Lambda_U\delta_U
 =\int\lambda(s)a(s)r(s)\,ds.
}
\tag{L-91110.11}

Thus it is a positive martingale discretization, not a scalar Riemann sum.

## 4. Exact bulk reproduction

Define the continuous and discrete seeds
\[
 F_{\rm cont}(m)=\int\lambda(s)\dot b_s(m)\,ds,
\tag{L-91110.12}
\]
\[
 F_{\rm disc}(m)=\sum_U\Lambda_Ue_U(m).
\tag{L-91110.13}

For a fixed \(s\), every active grid index in (L-91110.5)--(L-91110.6) lies among
\[
 U\in\{\lfloor s\rfloor,\lfloor s\rfloor+1,\lfloor s\rfloor+2\}
\]
up to the harmless integer-boundary convention.

If \(s\ge m+2\), then \(m\le U-1\) for every active \(U\), so the exact rank-two formula for \(e_U(m)\) applies. Equations (L-91110.7) give
\[
\begin{aligned}
 \sum_Uq_U(s)\frac{e_U(m)}{\alpha_U}
 &=\sum_Uq_U(s)[\sqrt m-r_Um]\\
 &=\sqrt m-r(s)m
 =\frac{\dot b_s(m)}{a(s)}.
\end{aligned}
\tag{L-91110.14}

If \(s\le m-1\), both the continuous atom and every active discrete atom vanish at \(m\).

Therefore the discrepancy is confined to one local strip:
\[
\boxed{
 F_{\rm disc}(m)-F_{\rm cont}(m)
 \text{ depends only on }
 s\in[m-1,m+2].
}
\tag{L-91110.15}

In particular, if the support of \(\lambda\) begins at \(K+2\), then
\[
\boxed{
 F_{\rm disc}(m)=F_{\rm cont}(m)
 \qquad(m\le K).
}
\tag{L-91110.16}

The entire inherited bulk is reproduced exactly; continuum-to-finite error is a width-three moving boundary collar.

## 5. Pointwise score majorization

Let
\[
 \ell_m=\log\frac m{m-1}.
\]
The continuous score density is
\[
 \dot H(s)=\sum_m\dot b_s(m)\ell_m.
\tag{L-91110.17}

On \(T-1<s<T\), the active prefix is \(m\le T-1\), so
\[
 \frac{\dot H(s)}{a(s)}
 =P_{T-1}-r(s)Q_{T-1},
\tag{L-91110.18}
where
\[
 P_N=\sum_{m=2}^{N}\sqrt m\ell_m,
 \qquad
 Q_N=\sum_{m=2}^{N}m\ell_m.
\]
This is the affine line through the discrete point
\[
 (r_T,h_T),
 \qquad
 h_T=H_T/\alpha_T.
\]

At the left neighboring state,
\[
\begin{aligned}
&h_{T-1}-[P_{T-1}-r_{T-1}Q_{T-1}]\\
&\quad=\sqrt{T-1}\,\ell_{T-1}
 [r_{T-1}\sqrt{T-1}-1]>0.
\end{aligned}
\tag{L-91110.19}

At the right neighboring state,
\[
\begin{aligned}
&h_{T+1}-[P_{T-1}-r_{T+1}Q_{T-1}]\\
&\quad=\sqrt T\,\ell_T
 [1-r_{T+1}\sqrt T]>0.
\end{aligned}
\tag{L-91110.20}

Therefore the piecewise-linear interpolation of the neighboring discrete scores lies above the continuous cell line. Using the same barycentric weights \(q_U(s)\),
\[
\boxed{
 \sum_Uq_U(s)h_U
 \ge\frac{\dot H(s)}{a(s)}.
}
\tag{L-91110.21}

Integrating against \(\lambda(s)a(s)ds\),
\[
\boxed{
 \sum_U\Lambda_UH_U
 \ge\int\lambda(s)\dot H(s)\,ds.
}
\tag{L-91110.22}

Thus martingale quantization can only increase the exact entropy score. The discretization has favorable—not adverse—objective curvature.

## 6. Relation to the butterfly basis

For each \(s\), the signed difference
\[
 \sum_Uq_U(s)\delta_{r_U}-\delta_{r(s)}
\]
has zero mass, zero mean, and is positive in convex order. After integrating over \(s\), the quantization error is a positive convex-order spread.

`L-91101` therefore decomposes it into nonnegative adjacent butterflies. `L-91102` identifies (L-91110.22) as the integrated sum of their positive score gains.

Hence the continuum shadow, the discrete B-spline quadrature, and the compact endpoint butterfly cone are the same object in three coordinates.

## 7. Application to the outer equality density

`L-91107` proves that the equality density
\[
 \lambda_X^\star(s)=L(X/s)
\]
is strictly positive on the factor-\(54.2\) outer window. Applying Sections 2--5 to this density gives:

1. nonnegative integer endpoint weights;
2. exact reproduction of the outer equality seed below the splice collar;
3. a discrepancy supported only on width-three endpoint collars;
4. a score at least as large as the continuum equality score.

Thus the score part of the reset hypothesis `T-91101` is automatically favorable. The only remaining issue is the sign of the finite carry/detail response of the local collars.

## 8. Exact remaining collar theorem

The final reset gate can now be stated locally:

> For the width-three seed discrepancy in (L-91110.15), after equal divisor destinations and radix-four descendants are recombined, construct a nonnegative adjacent-butterfly correction whose detail-column response is nonpositive and whose endpoint weights remain nonnegative.

Every relevant normalized quotient lies in the finite \(54\)-cell window, and `L-91109` supplies a 33-atom parity shadow with at most one upward integer displacement. No global quadrature or score estimate remains.

## 9. Proof boundary

Closed exactly, subject to review:

1. the continuous endpoint atom and state coordinate;
2. the local positive martingale/B-spline kernel;
3. nonnegative integer endpoint weights;
4. exact preservation of both seed moments;
5. exact bulk reproduction and width-three collar localization;
6. pointwise and integrated score majorization;
7. equivalence with nonnegative endpoint butterflies;
8. application to the positive outer equality density.

Still open:

1. sign and capacity of the width-three carry/detail collar;
2. its divisor-faithful realization through the parity shadow;
3. coefficient-one transfer of the inner two-state residual;
4. RH.
