# L-99902 — Native normalized specialization with two labelled copies of 67

Claim ID: `L-99902`  
Status: **PROVED EXACT SOURCE SPECIALIZATION**  
Created: 2026-08-20  
Depends on: `L-99705`, `L-99900`  
RH status: **not assumed**

After neutral-trace cancellation in PR #658, the normalized occurrence mass is

\[
\frac{|\beta(n)|}{n}\Phi_X^{\Box}(n).
\]

The support is squarefree away from the local \(67\) fibres, and

\[
\beta(m)=\mu(m),
\qquad
\beta(67m)=-2\mu(m),
\qquad
\beta(67^2m)=\mu(m).
\]

Represent the coefficient \(-2\) by two distinct labelled vertices
\(67_1,67_2\). Every ordinary prime label \(p\) has activity

\[
r_p=1/p,
\]

and each labelled \(67\) copy has activity \(1/67\).

Then every occurrence is a labelled subset, its sign is its labelled parity,
and its normalized arithmetic mass is exactly the product of the label
activities times the common box potential. Applying `L-99900` to any fully
active label block gives exact residual

\[
\boxed{
\Delta_B
=
\prod_{p\in B_{\rm ordinary}}\left(1-\frac1p\right)
\left(1-\frac1{67}\right)^{m_{67}},
}
\tag{L-99902.1}
\]

where \(m_{67}\) is zero, one, or two according to the labelled block.

The two copies of \(67\) are never merged before transport. This preserves the
native coefficient, source owner, and exact parity channel.
