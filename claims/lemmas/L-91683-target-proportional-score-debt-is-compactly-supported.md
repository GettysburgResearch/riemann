# L-91683 — Target-proportional score debt has compact rough support

Claim ID: `L-91683`  
Status: **PROVED EXACT / DIRECTED**  
Created: 2026-08-14  
Depends on: `L-91680`, `L-91362`  
Replay: `X-91682-post-hall-complete-profile`  
RH status: **unproved**

## 1. Statement

For one stopped `P_61` causal leaf, let `E` and `O` be the positive even- and odd-parity source packets.  The target-proportional producer of `L-91680` has exact score debt

\[
\mathfrak d_S(E,O)
=
\frac{[O_TE_S-E_TO_S]_+}{E_T}.
\]

Then

\[
\boxed{
\mathfrak d_S(E,O)=0
\qquad(p\ge500000).
}
\tag{L-91683.1}
\]

For `67<=p<500000`, the total debt over the complete source-disjoint stopping line is bounded by the absolute constant

\[
\boxed{
\sum_v\mathfrak d_S(E_v,O_v)
<39321600000000000.
}
\tag{L-91683.2}
\]

Thus the aggregate score-debt gate in `O-91680` is closed.

## 2. Two scalar coordinates

Write every causal parity total as

\[
T_\sigma=4a_\sigma-3b_\sigma,
\qquad
S_\sigma=5a_\sigma-3b_\sigma.
\]

A direct expansion gives

\[
\boxed{
O_TE_S-E_TO_S
=3(a_ob_e-a_eb_o).
}
\tag{L-91683.3}
\]

Put `t=sqrt(p)`, `u=sqrt(y)`, `x=py`, and define parity prefix sums

\[
A_\sigma(z)=
\sum_{\substack{d|P_{61}\\d\le z\\\sigma(d)=\sigma}}\frac1d,
\qquad
B_\sigma(z)=
\sum_{\substack{d|P_{61}\\d\le z\\\sigma(d)=\sigma}}\frac1{\sqrt d}.
\]

Then

\[
\frac{a_\sigma}{u}
=tA_\sigma(x)-t^{-1}A_\sigma(y),
\qquad
b_\sigma=B_\sigma(x)-t^{-1}B_\sigma(y).
\]

Let

\[
\Delta_x=A_e(x)B_o(x)-A_o(x)B_e(x).
\]

Expanding the determinant yields

\[
\begin{aligned}
\frac{a_ob_e-a_eb_o}{u}
={}&-t\Delta_x\\
&+[A_e(x)B_o(y)-A_o(x)B_e(y)]\\
&+t^{-1}[A_e(y)B_o(x)-A_o(y)B_e(x)]\\
&+t^{-2}[A_o(y)B_e(y)-A_e(y)B_o(y)].
\end{aligned}
\tag{L-91683.4}
\]

## 3. Tail sign

The exact prefix census checks every divisor cell intersecting `x>=500000` and proves

\[
\boxed{\Delta_x\ge2.}
\tag{L-91683.5}
\]

The minimum prefix begins at `x=501942`.

The complete absolute masses satisfy

\[
A_e+A_o<5,
\qquad
B_e+B_o<60.
\]

Each of the three cross determinants in (L-91683.4) therefore has absolute value below `600`.  For `p>=500000`, `t>700`, and hence

\[
\frac{a_ob_e-a_eb_o}{u}
<-2t+600+\frac{600}{t}+\frac{600}{t^2}<0.
\]

Equations (L-91683.3)--(L-91683.4) prove (L-91683.1).

## 4. Compact range

If `p<500000`, then `x<33.5\times10^6`.  A positive parity score total is bounded by

\[
E_S<5\sqrt x\sum_{d|P_{61}}\frac1d<150000.
\]

At a fixed root endpoint the least-prime/source-disjoint stopping line has at most

\[
2\cdot2^{18}\cdot500000
\]

labelled compact leaves.  Multiplication gives (L-91683.2).  The constant is intentionally crude; only absoluteness is needed by the envelope.

## 5. Verification boundary

This theorem closes score debt for the target-proportional producer.  It does not prove its simultaneous physical row determinants.
