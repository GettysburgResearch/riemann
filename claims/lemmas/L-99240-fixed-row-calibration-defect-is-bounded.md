# L-99240 — The complete finite/continuum calibration defect is bounded in every fixed component row

Claim ID: `L-99240`  
Status: **PROPOSED COMPLETE FIXED-ROW BOUNDEDNESS THEOREM — LOCAL LEDGER RECONSTRUCTION REQUIRED**  
Created: 2026-08-19  
Frozen sources: PR #513 retained-cell identity; PR #636 endpoint-nested source; PR #638 distributional boundary audit  
RH status: **not assumed**

Fix an integer row \(j\ge2\). Let

\[
\mathcal R b(j)
=(j+1)\Delta_j^2\!\left[\frac{b(j)}{j-1}\right]
\tag{L-99240.1}
\]

be the physical component-row map. The purpose of this lemma is not to force
all endpoint-frame data into a positive measure. It proves that every datum
which is withheld from the positive common parent is uniformly harmless in a
fixed row.

## 1. Exact retained-cell formula

At a node of endpoint \(Y\), put

\[
K_Y=\left\lfloor\frac{Y}{67}\right\rfloor+1
\]

and let \(\mathcal I_Y\) be any retained union of complete integer cells whose
left endpoint is at least \(K_Y+2\). On those cells define

\[
\varepsilon_Y(m)
=d_Y^\star(m)-\int_m^{m+1}d_Y^\star(t)\,dt,
\qquad
E_Y^I(n)=\sum_{\substack{m\in\mathcal I_Y\\m\ge n}}\varepsilon_Y(m).
\]

The adjacent-cell estimate used by the direct-row construction is

\[
|\varepsilon_Y(m)|<\frac{19}{2}m^{-3/2}.
\tag{L-99240.2}
\]

If \(K_Y>j+2\), then

\[
E_Y^I(j)=E_Y^I(j+1)=E_Y^I(j+2)=:\eta_Y.
\]

Therefore

\[
\begin{aligned}
\mathcal R E_Y^I(j)
&=(j+1)\eta_Y
 \left(\frac1{j-1}-\frac2j+\frac1{j+1}\right)\\
&=\boxed{\frac{2\eta_Y}{j(j-1)}}.
\end{aligned}
\tag{L-99240.3}
\]

Moreover,

\[
|\eta_Y|
<
\frac{19}{2}\sum_{m\ge K_Y+2}m^{-3/2}
<\frac{19}{\sqrt{K_Y+1}},
\]

and hence

\[
\boxed{
|\mathcal R E_Y^I(j)|
<
\frac{38}{j(j-1)\sqrt{K_Y+1}}
<
\frac{38\sqrt{67}}{j(j-1)\sqrt Y}.
}
\tag{L-99240.4}
\]

When \(K_Y\le j+2\), the endpoint lies in a fixed bounded interval depending
only on \(j\); those finitely many cell patterns are absorbed into the compact
constant below. No sign of the quadrature defect is asserted or needed.

## 2. Uniform fixed-row bound for endpoint fibres

The exact positive infinitesimal endpoint seed is

\[
g_s(n)=\left(\sqrt n-\frac n{\sqrt s}\right)\mathbf1_{n\le s},
\qquad
p_s=\mathcal Rg_s.
\]

For \(s\ge j+2\),

\[
p_s(j)
=(j+1)\Delta_j^2
\left[
\frac{\sqrt n}{n-1}
-
\frac{n}{(n-1)\sqrt s}
\right]_{n=j}.
\tag{L-99240.5}
\]

Thus \(p_s(j)=a_j+b_js^{-1/2}\) for explicit constants \(a_j,b_j\).
For \(s<j+2\) there are only finitely many activation regimes. Consequently

\[
\boxed{
P_j^\ast:=\sup_{s\ge1}|p_s(j)|<\infty.
}
\tag{L-99240.6}
\]

This is the fixed-row phenomenon which fails in the target and literal-score
coordinates: a compact endpoint-frame coefficient may have large global
meaning, while its observation in one fixed physical row is uniformly bounded.

## 3. Distributional knot and boundary ledger

PR #638 proves the exact distributional formula

\[
f(x)=A_a\sqrt x+B_ax+
\int_{(a,x]}\frac{2(x-\sqrt{xt})}{t^{3/2}}\,d(Vf)(t),
\tag{L-99240.7}
\]

with knot atom

\[
d(Vf)(\{t\})
=t^{3/2}\bigl(f'(t+)-f'(t-)\bigr).
\tag{L-99240.8}
\]

For the compact factor-67 fibre \(1\le x<67\), every equality datum is an
explicit finite sum of activated elementary functions. Hence it has finitely
many activation knots, locally bounded-variation derivative, and finite
boundary coefficients \(A_a,B_a\). There are only finitely many low-prime and
Hall source types. Therefore the complete signed distributional ledger—the
uncertified knot atoms plus the two homogeneous boundary modes—has uniformly
finite total variation over this finite compact family.

No positive anchor representation is required. Keep the two homogeneous modes
as signed row data. Every fixed physical-row feature is continuous on each
compact activation cell and has finite one-sided limits at the knots. Together
with (L-99240.6), this gives a finite constant \(V_j^{\rm bdry}\) such that the
entire knot-and-boundary contribution at one unit source satisfies

\[
|C_Y^{\rm bdry}(j)|\le V_j^{\rm bdry}.
\tag{L-99240.9}
\]

This is exactly where PR #638's rank-two audit is useful: it proves there are
no hidden infinite-dimensional boundary modes.

## 4. Complete local calibration bound

Define the local signed calibration coordinate \(C_Y(j)\) to contain:

1. the retained-cell finite/continuum discrepancy;
2. every derivative-jump atom withheld from the positive source;
3. the two homogeneous Volterra boundary modes;
4. the finitely many bounded small-endpoint patterns.

Equations (L-99240.4) and (L-99240.9), plus finiteness of the small-endpoint
patterns, give

\[
\boxed{|C_Y(j)|\le B_j}
\tag{L-99240.10}
\]

for one constant \(B_j<\infty\), uniformly in the node endpoint \(Y\) and in
its complete provenance label.

The exact application obligation is now only to verify the signed identity

\[
E_Y=J_Y+E_YT_Y+C_Y
\tag{L-99240.11}
\]

in the actual component rows. The sign of \(C_Y\) is immaterial. Target,
literal-score, ordinary-capacity and detail-capacity coordinates are
intentionally absent from this fixed-row theorem.
