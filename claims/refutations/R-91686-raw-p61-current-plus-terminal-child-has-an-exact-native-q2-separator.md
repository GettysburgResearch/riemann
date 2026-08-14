# R-91686 — The raw `P_61` current plus terminal child has an exact native `q=2` separator

Claim ID: `R-91686`  
Status: **EXACT REFUTATION OF THE UNTHINNED RAW-LEAF CAPACITY INFERENCE**  
Created: 2026-08-14  
Frozen input: PR `#469` at `3cf685181bd367b92cdcfeef9249e0b9b542a09e`  
Depends on: `L-91379`, `L-91685`  
Replay: `X-91686-native-root-compiler-separator`  
RH status: **unproved**

## 1. Raw stopped-leaf basis

Put

\[
P=P_{61}=\prod_{q\le61}q.
\]

For a rough prime `p>=67`, a terminal endpoint `1<=y<67`, and `X=py`, the raw leaf basis of `L-91685` is

\[
G_{p,y}=D_{P,X}-p^{-1/2}c_y,
\qquad
C_{p,y}=p^{-1/2}c_y,
\tag{R-91686.1}
\]

with

\[
G_{p,y}+C_{p,y}=D_{P,X}.
\tag{R-91686.2}
\]

The row and response signs in `L-91685` are retained. The question here is the stronger native one-use inequality.

## 2. Exact endpoint `X=136`, `p=67`, `q=2`

Take

\[
p=67,
\qquad
X=136,
\qquad
y=\frac{136}{67},
\qquad q=2.
\]

The only `P_61`-rough integers not exceeding `X/q=68` are `1` and `67`. Therefore the exact rough-reservoir identity gives

\[
\Gamma(D_{P,136};2)
=w_{136}(2)+\delta,
\qquad
\boxed{
\delta=\frac1{\sqrt{134}}\log\frac{68}{67}>0.
}
\tag{R-91686.3}
\]

The terminal child has

\[
\Gamma(C_{67,136/67};2)
=67^{-1/2}w_{136/67}(2)
=\delta.
\tag{R-91686.4}
\]

Hence the raw current alone exactly saturates the native ordinary column:

\[
\boxed{
\Gamma(G_{67,136/67};2)=w_{136}(2).
}
\tag{R-91686.5}
\]

But current plus mandatory child overdraws it:

\[
\boxed{
\Gamma(G_{67,136/67};2)
+
\Gamma(C_{67,136/67};2)
=w_{136}(2)+\delta>w_{136}(2).
}
\tag{R-91686.6}
\]

This is an exact violation of `T-91314.2` for the unthinned raw-leaf basis.

## 3. The same exact detail obstruction

At `4q=8`, one has `X/(4q)=17`. The only `P_61`-rough integer at most `17` is `1`, and the terminal child is inactive at column `8`. Thus

\[
\Gamma(G_{67,136/67};8)=w_{136}(8),
\qquad
\Gamma(C_{67,136/67};8)=0.
\]

Consequently

\[
\boxed{
\Xi(G_{67,136/67};2)=\Omega_{136}(2)
}
\tag{R-91686.7}
\]

while

\[
\boxed{
\Xi(G_{67,136/67};2)
+
\Xi(C_{67,136/67};2)
=
\Omega_{136}(2)+\delta.
}
\tag{R-91686.8}
\]

So `T-91314.3` fails by the same strictly positive amount.

The elementary inequalities

\[
\log(1+x)>\frac{2x}{2+x}
\quad(x>0),
\qquad
\sqrt{134}<12
\]

give

\[
\boxed{
\delta>\frac1{810}.
}
\tag{R-91686.9}
\]

Since `Y_4(2)=Lambda(2)=log 2>2/3`, the corresponding positive `Y_4`-weighted violation is greater than

\[
\boxed{
\frac1{1215}.
}
\tag{R-91686.10}
\]

## 4. Exact one-column Farkas certificate

Write `x` for the total ordinary use at column `2`. The raw identity forces

\[
x=w_{136}(2)+\delta,
\]

while native feasibility requires

\[
x\le w_{136}(2).
\]

For the equality multiplier `y=-1` and capacity multiplier `z=1`, the variable coefficient vanishes and the dual value is

\[
-(w_{136}(2)+\delta)+w_{136}(2)=-\delta<0.
\tag{R-91686.11}
\]

This is an exact rational-sign Farkas separator after adjoining the positive algebraic-logarithmic constant `delta`.

## 5. Infinite asymptotic current-only obstruction

The obstruction is not confined to a finite base endpoint. For every prime `p>=71`, set

\[
X_p=2(p+1),
\qquad
y_p=\frac{2(p+1)}p<3,
\qquad q=2.
\tag{R-91686.12}
\]

The terminal child removes exactly the rough-reservoir term indexed by `m=p`. The positive `m=67` term remains in the raw current, so

\[
\begin{aligned}
\Gamma(G_{p,y_p};2)-w_{X_p}(2)
&=
\sum_{\substack{2\le m\le p+1\\m\in\mathcal R_{67}\\m\ne p}}
\frac1{\sqrt m}w_{X_p/m}(2)\\
&\ge
\frac1{\sqrt{134}}
\log\frac{p+1}{67}.
\end{aligned}
\tag{R-91686.13}
\]

For `p>=71`,

\[
\log\frac{p+1}{67}
\ge
\log\frac{72}{67}
>
\frac{10}{139},
\]

and hence

\[
\boxed{
\Gamma(G_{p,y_p};2)-w_{X_p}(2)
>
\frac5{834}.
}
\tag{R-91686.14}
\]

Thus the raw current itself violates the native ordinary capacity on an infinite family with `X_p -> infinity`.

## 6. Consequence

The following inference is false:

```text
raw current row/response signs are nonnegative
+ terminal child is exact and nonnegative
------------------------------------------------
raw current + child is a native one-use packet.
```

The raw leaf theorem remains valuable, but the current must be **source-ownedly thinned or re-realized** before the child is retained. Adding further nonnegative current generators cannot repair the separated column. A successful enlarged cone needs a replacement operation that removes current usage while preserving nonnegative rows, target/score, provenance, ports, and bounded `Y_4` slack.

```text
raw terminal row sign                         RETAINED
raw ordinary/detail response sign             RETAINED
raw current+child native ordinary capacity    FALSE / EXACT SEPARATOR
raw current+child native detail capacity      FALSE / EXACT SEPARATOR
raw current alone on an infinite family       FALSE / EXACT SEPARATOR
Native-Root Capacity Theorem                  OPEN
Riemann Hypothesis                            UNPROVEN
```
