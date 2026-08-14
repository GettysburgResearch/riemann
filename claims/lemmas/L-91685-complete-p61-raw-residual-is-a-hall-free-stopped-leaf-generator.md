# L-91685 — The complete `P_61` raw residual is a Hall-free row-positive stopped-leaf generator

Claim ID: `L-91685`
Status: **PROPOSED COMPLETE CROSS-BRANCH ROW/RESPONSE-SIGN THEOREM — NATIVE CAPACITY ALLOCATION SEPARATE**
Created: 2026-08-14
RH status: **unproved**

## 1. Frozen normalization

Put

\[
P=P_{61}=\prod_{q\le 61}q,
\qquad p\ge 67\text{ prime},
\qquad 1\le y<67,
\qquad r=p^{-1/2}.
\]

Retain the canonical positive component row `Q_Y(j)`, with causal value zero for `Y<=j`, and define

\[
D_{P,X}(j)=
\sum_{\substack{d\mid P\\d\le X/j}}
\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
\tag{L-91685.1}
\]

The complete raw stopped-leaf generator and its exact terminal child are

\[
\boxed{
G_{p,y}(j)=D_{P,py}(j)-rD_{P,y}(j),
}
\tag{L-91685.2}
\]

\[
\boxed{
C_{p,y}(j)=rD_{P,y}(j).
}
\tag{L-91685.3}
\]

Therefore

\[
\boxed{G_{p,y}+C_{p,y}=D_{P,py}}
\tag{L-91685.4}
\]

in every linear target, declared-score, literal-row, ordinary-column, radix-four-column, entropy, and zero-boundary coordinate.

The construction retains the exact Boolean coefficients `mu(d)/sqrt(d)`. It does not replace them by source fractions, a synthetic complement, a target-proportional submeasure, or a Hall transport.

## 2. Coefficientwise positivity in every row

For `2<=j<=y`, the inherited-row theorem `L-91347` proves directly

\[
G_{p,y}(j)>0.
\tag{L-91685.5}
\]

For `j>y`, causal support gives `D_{P,y}(j)=0`, hence

\[
G_{p,y}(j)=D_{P,py}(j).
\tag{L-91685.6}
\]

The full global canonical-row theorem `L-91364` gives

\[
D_{P,X}(j)\ge0
\]

for every real `X>=1` and every integer `j>=2`, with strict inequality for `2<=j<X` and equality for `j>=X`. Thus

\[
\boxed{
G_{p,y}(j)>0\quad(2\le j<py),
\qquad
G_{p,y}(j)=0\quad(j\ge py).
}
\tag{L-91685.7}
\]

The inherited/frontier split is exhaustive. No finite row cutoff such as `j<=66` remains.

This proves the one-prime current-row candidate of `O-91377` on the entire terminal stopped-leaf domain `X=py`, `X/p=y<67`. It is not a proof for arbitrary `X/p`.

## 3. Ordinary and radix-four response positivity

Let

\[
H_P(Z)=
\sum_{\substack{n\le Z\\(n,P)=1}}
\frac1{\sqrt n}\log\frac Zn,
\qquad
\Delta_P(Z)=H_P(Z)-H_P(Z/4),
\tag{L-91685.8}
\]

with both functions zero below their natural support. The exact response identities of `L-91363` are

\[
\Gamma(D_{P,X};q)=q^{-1/2}H_P(X/q),
\tag{L-91685.9}
\]

\[
\Xi(D_{P,X};q)=q^{-1/2}\Delta_P(X/q).
\tag{L-91685.10}
\]

Both kernels are nonnegative and nondecreasing. Between activation knots,

\[
\frac{d}{d\log Z}H_P(Z)
=
\sum_{\substack{n\le Z\\(n,P)=1}}n^{-1/2}\ge0,
\tag{L-91685.11}
\]

and

\[
\frac{d}{d\log Z}\Delta_P(Z)
=
\sum_{\substack{Z/4<n\le Z\\(n,P)=1}}n^{-1/2}\ge0.
\tag{L-91685.12}
\]

The formulas join continuously at all activation points. Hence, for every physical integer column `q>=2`,

\[
\begin{aligned}
\Gamma(G_{p,y};q)
&=q^{-1/2}\left[H_P(py/q)-rH_P(y/q)\right]\\
&\ge q^{-1/2}(1-r)H_P(y/q)\ge0,
\end{aligned}
\tag{L-91685.13}
\]

and

\[
\begin{aligned}
\Xi(G_{p,y};q)
&=q^{-1/2}\left[\Delta_P(py/q)-r\Delta_P(y/q)\right]\\
&\ge q^{-1/2}(1-r)\Delta_P(y/q)\ge0.
\end{aligned}
\tag{L-91685.14}
\]

Thus the raw generator is simultaneously ordinary- and radix-four-positive. The atomwise causal datum has zero finite-boundary reserve by `L-91654`; finite Boolean summation leaves the raw generator boundary reserve exactly zero.

## 4. Native-capacity firewall

Response positivity is **not** native-capacity feasibility. By (L-91685.4),

\[
\Gamma(G_{p,y};q)+\Gamma(C_{p,y};q)
=
\Gamma(D_{P,py};q),
\tag{L-91685.15}
\]

and similarly for `Xi`. The exact rough-reservoir theorem `L-91379` gives

\[
\Gamma(D_{P,X};q)
=
 w_X(q)+
 \sum_{\substack{m\in\mathcal R_{67}\\m>1}}
 m^{-1/2}w_{X/m}(q),
\tag{L-91685.16}
\]

\[
\Xi(D_{P,X};q)
=
 \Omega_X(q)+
 \sum_{\substack{m\in\mathcal R_{67}\\m>1}}
 m^{-1/2}\Omega_{X/m}(q).
\tag{L-91685.17}
\]

The sums on the right are the positive rough-prime reservoir. Therefore the pair `G+C`, although positive and exact in the canonical finite-Euler coordinates, may not be counted wholly inside the native capacities `w_X,Omega_X` while the same rough reservoir is also exported recursively.

This is precisely the normalization firewall in `R-91312/T-91314` on PR `#468`:

```text
row/response sign of the stopped-leaf generator    closed here;
native one-use capacity allocation                 not closed here;
rough-reservoir ownership                          must be explicit.
```

No statement below removes this firewall.

## 5. Target, declared score, and literal entropy

Use the single-SHARP target/score normalization

\[
T_P(X)=3F_{4/3}^P(X),
\qquad
S_P(X)=3F_{5/3}^P(X).
\tag{L-91685.18}
\]

Define

\[
T_G=T_P(py)-rT_P(y),
\qquad
S_G=S_P(py)-rS_P(y).
\tag{L-91685.19}
\]

The exact one-prime theorem `L-91345` gives

\[
\boxed{T_G>\frac9{50}\sqrt{py}>0,}
\tag{L-91685.20}
\]

and

\[
\boxed{
S_G-T_G>
\frac{336338530534578047569}
{224523472888007630167974}
\sqrt{py}
>0.0014980\sqrt{py}>0.
}
\tag{L-91685.21}
\]

Let

\[
\mathcal E_P(X)=\sum_{j\ge2}D_{P,X}(j)\,\mathsf G_j
\]

be the literal component entropy, with the resident nonnegative entropy weights `mathsf G_j`. The frozen literal-entropy theorem `L-91348` gives

\[
\boxed{
\left[\mathcal E_P(py)-r\mathcal E_P(y)\right]-S_G
>\frac{893}{100}.
}
\tag{L-91685.22}
\]

Thus the raw generator has strict literal-score surplus. The independent successor `L-91682` on PR `#466` proves a second uniform route with margin `>1/2` and explains why the target-proportional declared-score debt disappears after physical row assembly.

The current and terminal child together satisfy the stronger complete-leaf inequality

\[
\boxed{
\mathcal E_P(py)-S_P(py)>\frac{559}{50}.
}
\tag{L-91685.23}
\]

These are score statements in the canonical finite-Euler packet. They do not by themselves bound the native `Y_4`-weighted slack required by `T-91314`.

## 6. The child is the exact native terminal row

Since `y<67`, every squarefree integer `k<=y` has all prime factors at most `61`, while every nonsquarefree `k` has `mu(k)=0`. Therefore

\[
\boxed{
D_{P,y}(j)
=
\sum_{k\le y/j}\frac{\mu(k)}{\sqrt k}Q_{y/k}(j)
=c_y(j).
}
\tag{L-91685.24}
\]

Hence

\[
C_{p,y}=r c_y.
\tag{L-91685.25}
\]

The global theorem `L-91364` gives `c_y>=0` coefficientwise on this terminal range. The exact native response theorem in `L-91663` gives

\[
\Gamma(c_y;q)=w_y(q),
\qquad
\Xi(c_y;q)=\Omega_y(q).
\tag{L-91685.26}
\]

Thus `C_{p,y}` is not a formal recursive copy. It is an actual finite terminal row with its exact child-owned capacities.

## 7. Exact stopped-leaf consequence

Whenever a source-disjoint stopping-line identity contains a canonical leaf fiber

\[
a_vD_{P,p_vy_v},
\qquad a_v\ge0,
\qquad 1\le y_v<67,
\]

one may replace it algebraically by

\[
a_vG_{p_v,y_v}+a_vC_{p_v,y_v}
\]

without changing any linear coordinate or source label. The first term is row- and response-positive; the second is an exact terminal native row. This removes the need for stopped-leaf Hall, target-Lorenz source extraction, or a Farkas search **for the sign and literal-score part of that leaf**.

To turn the replacement into a native root certificate, one must additionally prove that the exact rough reservoir in (L-91685.16)--(L-91685.17) is assigned source-disjointly to recursive children, leaving the current plus all children within one copy of `w_X,Omega_X` and all retained ports. That is the surviving native-reservoir/root interface, not a corollary of positivity.

## 8. Exact boundary

```text
stopped-leaf Hall                                 FALSE / NOT USED
raw generator row sign for every j                PROPOSED CLOSED / FROZEN INPUTS
raw ordinary and radix-four response signs        EXACT FROM FROZEN KERNELS
raw target/score/literal-entropy surplus           FROZEN EXACT/DIRECTED INPUTS
terminal child identity D_(P,y)=c_y                EXACT
canonical current+child identity                  EXACT
native one-use capacity inequality                OPEN / ROUGH RESERVOIR
native Y4-weighted slack                          OPEN
Riemann Hypothesis                                UNPROVEN
```
