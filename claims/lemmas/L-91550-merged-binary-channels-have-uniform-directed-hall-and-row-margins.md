# L-91550 — The merged survival/hazard channels have uniform directed Hall and component-row margins

Claim ID: `L-91550`  
Status: **PROVED DIRECTED FINITE-INTERVAL CERTIFICATE ON THE LIVE BRANCH**  
Created: 2026-08-13  
Depends on: `L-91452/L-91454`; exact finite forcing; positive component rows  
RH status: **unproved**

## 1. Conservative parameter corridors

Put `r=p^(-1/2)` with `p>=67`.  Then `0<r<1/8`.  The four ordinary branch
parameters satisfy

\[
 \frac43<
 \alpha_s=\frac{2(r+2)}{r+3}
 <\frac32,
 \tag{L-91550.1}
\]

\[
 1<
 \alpha_h=\frac{2(r+1)}{r+2}
 <\frac65,
 \tag{L-91550.2}
\]

\[
 1<
 \beta_h=\frac{4r+1}{2r+1}
 <\frac65,
 \tag{L-91550.3}
\]

while the survival score parameter is exactly `5/3`.

Thus every target and score channel lies in one of the conservative intervals

```text
survival target: [4/3,3/2];
survival score:  {5/3};
hazard target:   [1,6/5];
hazard score:    [1,6/5].
```

## 2. Directed Hall margins

For an active negative Mobius threshold `t<55`, put

\[
 A_t=\sum_{n\le t}\frac{\mu(n)}n,
 \qquad
 B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
 \tag{L-91550.4}
\]

The no-upward prefix Hall margin of the ordinary channel `w_alpha` is

\[
 \mathcal H_{\alpha,t}(x)
 =\alpha\sqrt x\,A_t-B_t.
 \tag{L-91550.5}
\]

It is affine in `alpha` and monotone in `sqrt(x)` with the sign of `A_t`.
Consequently its minimum on a rectangle

\[
 \alpha_-\le\alpha\le\alpha_+,
 \qquad
 t\le x<55
\]

occurs at one exact corner:

```text
(alpha_-,t)  if A_t>=0;
(alpha_+,55) if A_t<0.
```

The directed checker `X-91550` encloses every radical at those corners and
proves

\[
 \boxed{
 \mathcal H_{\alpha,t}(x)>\frac1{250}
 }
 \tag{L-91550.6}
\]

simultaneously for all four corridors, every active negative threshold and the
whole stronger window `1<=x<55`.

The actual factor-54 window is smaller because `c_0^-1<54.219`.

The weakest certified channel is the survival score:

\[
 \mathcal H_{5/3,13}(55)
 >0.007875034703026309\ldots
 >\frac1{250}.
 \tag{L-91550.7}
\]

Selected other directed lower endpoints are

\[
 \mathcal H_{[4/3,3/2],13}>0.10348958,
 \qquad
 \mathcal H_{[1,6/5],13}>0.27559576.
 \tag{L-91550.8}
\]

Thus all four target/score Hall transports exist with a uniform no-upward
margin on the merged live tree.

## 3. Uniform normalized component-row monotonicity

On an activation cell `N<=Y<N+1`, write

\[
 Q_Y(j)=c_{j,N}\log Y-d_{j,N},
 \qquad
 c_{j,N}>0.
 \tag{L-91550.9}
\]

For `alpha>=1`, differentiate

\[
 H_{j,\alpha}(Y)
 =\frac{Q_Y(j)}{\alpha\sqrt Y-1}.
 \tag{L-91550.10}
\]

After multiplying the numerator of the derivative by `2Y`, its sign is the sign
of

\[
 \boxed{
 M_{j,N,\alpha}(Y)
 =\alpha\sqrt Y\,[2c_{j,N}-Q_Y(j)]-2c_{j,N}.
 }
 \tag{L-91550.11}
\]

Within the cell,

\[
 \frac d{dY}M_{j,N,\alpha}(Y)
 =-\frac{\alpha Q_Y(j)}{2\sqrt Y}\le0.
 \tag{L-91550.12}
\]

Therefore the right endpoint is worst.  The factor

\[
 \sqrt Y[2c_{j,N}-Q_Y(j)]
\]

is positive throughout the certified cells, so `alpha=1` is worst over every
branch corridor `1<=alpha<=5/3`.

The directed cell replay checks every

\[
 2\le j\le N<55
\]

and proves

\[
 \boxed{
 M_{j,N,\alpha}(Y)>\frac1{25}
 }
 \tag{L-91550.13}
\]

for all `1<=alpha<=5/3`.  The weakest cell is

\[
 (j,N,Y)=(53,54,55),
 \qquad
 M>0.06477914220635762\ldots.
 \tag{L-91550.14}
\]

Hence every no-upward target-Hall edge lifts to a nonnegative exact component
row for every survival/hazard target and score channel.

## 4. Replay

```bash
cd experiments/X-91550-merged-binary-hall-row
python3 verify.py
```

Retained result:

```text
PASS_MERGED_BINARY_HALL_ROW_CORRIDORS
Hall prefix checks:                 72
component derivative cell checks: 1431
```

The checker uses exact `Fraction` arithmetic and directed rational enclosures of
square roots and logarithms.

## 5. Consequence and boundary

The finite directed arithmetic input imported by `L-91454` has now been replayed
on the merged live branch in corridors strictly larger than the actual branch
ranges.

```text
survival target Hall corridor                     CERTIFIED
survival score Hall channel                       CERTIFIED
hazard target Hall corridor                       CERTIFIED
hazard score Hall corridor                        CERTIFIED
all normalized component-row derivatives          CERTIFIED
merged directed producer replay                    CLOSED
outer typed loss composition                       SEPARATE
Riemann Hypothesis                                 UNPROVEN
```
