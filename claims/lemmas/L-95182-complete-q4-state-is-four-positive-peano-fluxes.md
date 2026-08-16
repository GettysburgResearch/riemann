# L-95182 — The reciprocal-smoothed Q4 state is a difference of four positive Peano fluxes

Claim ID: `L-95182`  
Status: **PROPOSED COMPLETE EXACT CANCELLATION-PRESERVING FACTORIZATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-93263` at `e1b3b03d97d47c5046aa84f31e51c925d92baabd`; `L-95180/L-95181`; the scale-four logarithmic-derivative dictionary from PR #474  
Scope: reciprocal-smoothed complete Q4 source in the positive Peano geometry; no centered-curvature norm

## 1. Positive Peano potential

Let `Phi` be the compact nonnegative potential of `L-93263`:

\[
\Phi(x)=
\begin{cases}
{x^2(85x^2-56x+10)\over8},&0\le x\le1/4,\\[2mm]
{(1-x)^3(3x+1)\over72},&1/4\le x\le1,\\
0,&x>1.
\end{cases}
\tag{L-95182.1}
\]

For `D=x d/dx`, it satisfies

\[
\boxed{D^2\Phi(x)=xW(x).}
\tag{L-95182.2}
\]

## 2. Two positive source channels

Define

\[
U_\pm(X)=\sum_{n\le X}{u_4^\pm(n)\over n}\Phi(n/X)\ge0.
\tag{L-95182.3}
\]

Because `Phi` is bounded and compactly supported, `L-95181` gives

\[
U_+(X)+U_-(X)=O(\log^2 X).
\tag{L-95182.4}
\]

Define the positive generalized-prime fluxes

\[
V_\pm(X)
=\sum_{\substack{dm\le X\\d>1}}
{\Lambda_4(d)u_4^\mp(m)\over dm}\Phi(dm/X)
\ge0.
\tag{L-95182.5}
\]

The channel-swap identities imply coefficientwise

\[
\boxed{
V_\pm(X)=\sum_{n\le X}{u_4^\pm(n)\log n\over n}\Phi(n/X).
}
\tag{L-95182.6}
\]

Hence

\[
V_+(X)+V_-(X)=O(\log^3 X).
\tag{L-95182.7}
\]

Every positive source occurrence is owned once by one divisor transition.

## 3. Signed reciprocal flux

Since `u_4^+-u_4^-=2a_4`,

\[
\boxed{
C_4(X):=
\sum_{n\le X}{a_4(n)\log n\over n}\Phi(n/X)
={V_+(X)-V_-(X)\over2}.
}
\tag{L-95182.8}
\]

Put

\[
d_4=(\varepsilon-4\delta_4)*(a_4\log).
\tag{L-95182.9}
\]

The `1/n` Peano normalization cancels the dilation coefficient four exactly:

\[
\begin{aligned}
\sum_{n\le X}{d_4(n)\over n}\Phi(n/X)
&=C_4(X)-C_4(X/4)\\
&={V_+(X)-V_-(X)\over2}
 -{V_+(X/4)-V_-(X/4)\over2}.
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{n\le X}{d_4(n)\over n}\Phi(n/X)
={1\over2}\bigl[V_+(X)+V_-(X/4)\bigr]
-{1\over2}\bigl[V_-(X)+V_+(X/4)\bigr].
}
\tag{L-95182.10}
\]

The right side is a difference of four positive Peano fluxes whose total mass is `O(log^3 X)`.

## 4. Exact relation to the complete Q4 source

Let `c_circ` denote the complete compact-Q4 logarithmic-derivative source normalized by

\[
\sum_n{c_\circ(n)\over n^s}
=(1-4^{1-s}){A_4'(s)\over A_4(s)}.
\tag{L-95182.11}
\]

Multiplying by `A_4(s)` gives

\[
\boxed{c_\circ*a_4=-d_4.}
\tag{L-95182.12}
\]

Therefore (L-95182.10) is the exact positive-flux representation of the complete Q4 state after one reciprocal-state convolution. No absolute `g_4` majorization is used in the signed output.

## 5. What remains

The factorization controls source mass, not the critical centered curvature. Applying `D^2` or an arbitrary positive scalar projection before removing the principal channel can amplify the real pole. A closing theorem must perform a centered nonlocal extraction—orthogonal projection, Schur complement, passive boundary response, or critical Carleson embedding—while retaining the channel swap.

## 6. Boundary

```text
positive Peano source channels               EXACT
positive coefficient-one fluxes              EXACT
four-positive-flux Q4 factorization          EXACT
polylog total positive flux mass             UNCONDITIONAL
reciprocal-smoothed source identity           EXACT
centered-curvature/Carleson extraction        OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
