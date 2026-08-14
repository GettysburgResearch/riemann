# L-91663 — Direct Hall child replacement is native-capacity faithful in every physical column

Claim ID: `L-91663`  
Status: **PROVED EXACT ROW/CAPACITY THEOREM ON FROZEN HALL INPUTS**  
Created: 2026-08-14  
Imports: `L-91545`, `L-91550`, `L-91556`, `L-91559`, `L-91560`, `L-91562`, `L-91621`  
Retains: `L-91112.25--26`, `L-90029`  
RH status: **unproved; score and global conclusion are separate**

## 1. Literal component row

For real `Y>=1`, define

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad S_Y(n)=\sum_{m\ge n}h_Y(m),
\]

and

\[
 \boxed{
 Q_Y(n)=(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right]\ge0.
 }
 \tag{L-91663.1}
\]

The retained finite formula is

\[
\boxed{
\begin{aligned}
Q_Y(n)={}&\frac{n+1}{n-1}[h_Y(n)-h_Y(n+1)]\\
&+\frac{2(n+1)}{n(n-1)}h_Y(n+1)
 +\frac{2}{n(n-1)}S_Y(n+2).
\end{aligned}}
 \tag{L-91663.2}
\]

Put

\[
 H(Z)=\sum_{k\le Z}k^{-1/2}\log(Z/k),
 \qquad H(Z)=0\quad(Z<1).
\]

Exact double summation gives, for every integer `q>=2`,

\[
 \boxed{
 \Gamma_Y(q)=\sum_{n\ge2}Q_Y(n)\beta_{nq}
 =q^{-1/2}H(Y/q).
 }
 \tag{L-91663.3}
\]

Hence

\[
 \boxed{
 \Xi_Y(q)=\Gamma_Y(q)-2\Gamma_Y(4q)
 =q^{-1/2}[H(Y/q)-H(Y/(4q))].
 }
 \tag{L-91663.4}
\]

Both responses are nonnegative and nondecreasing in `Y`. Indeed, away from
activation knots,

\[
 H'(Z)=Z^{-1}\sum_{k\le Z}k^{-1/2},
\]

and for `D(Z)=H(Z)-H(Z/4)`,

\[
 \boxed{
 D'(Z)=Z^{-1}\sum_{Z/4<k\le Z}k^{-1/2}\ge0.
 }
 \tag{L-91663.5}
\]

Continuity at the knots gives global monotonicity. The literal rows `Q_Y` are
also nondecreasing by the exact cell formula and the retained normalized-row
theorem.

## 2. Native equality response

Define the exact finite equality row

\[
 \boxed{
 c_X(j)=\sum_{k\le X}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
 }
 \tag{L-91663.6}
\]

Applying (L-91663.3), writing `n=km`, and using Möbius convolution,

\[
\begin{aligned}
\Gamma(c_X;q)
&=q^{-1/2}
  \sum_{km\le X/q}\frac{\mu(k)}{\sqrt{km}}
  \log\frac{X}{qkm}\\
&=q^{-1/2}
  \sum_{n\le X/q}\frac1{\sqrt n}\log\frac{X}{qn}
  \sum_{k\mid n}\mu(k).
\end{aligned}
\]

Only `n=1` survives, so

\[
 \boxed{
 \Gamma(c_X;q)=w_X(q)
 =q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
 }
 \tag{L-91663.7}
\]

Taking the radix-four difference,

\[
 \boxed{
 \Xi(c_X;q)=\Omega_X(q)=w_X(q)-2w_X(4q).
 }
 \tag{L-91663.8}
\]

This is the native row. The canonical `P_61` row of `R-91654` has a larger
packet-specific response and cannot replace it.

## 3. Leafwise Hall row identity

Freeze the one-prime controlled cocycle and merged Hall inputs. Hall is applied
separately on mutually singular stopped leaves, as in `L-91621`, and only its
positive outputs are summed. The result is a coefficientwise row identity

\[
 \boxed{
 R_{\rm parent}=R_{\rm pre}+R_s(c_s)+R_h(c_h)+B_s+B_h,
 }
 \tag{L-91663.9}
\]

where

\[
 c_s,c_h\ge0,
 \qquad B_s,B_h\ge0,
 \qquad R_{\rm pre}\ge0.
\]

No nonlinear Hall choice is commuted through the rough tree and no source atom
is duplicated.

For `tau in {s,h}`, restrict to the deterministic child support

\[
 c_\tau^{ch}=c_\tau|_{\{n\le X/67\}}
\]

and let `R_ch` be the sum of the two canonical child rows at endpoint `X/67`.
Endpoint monotonicity gives

\[
 \boxed{
 R_{\rm cur}:=R_{\rm parent}-R_{ch}\ge0.
 }
 \tag{L-91663.10}
\]

All Hall bonuses and activation-frontier terms are included in `R_cur`.

## 4. Arbitrary child replacement

Let `d_ch>=0` be any row feasible for the complete canonical child capacities.
Insert it at the same literal row indices and put

\[
 \boxed{d_X=R_{\rm cur}+d_{\rm ch}.}
 \tag{L-91663.11}
\]

Then, simultaneously for every integer `q>=2`,

\[
\boxed{
\begin{aligned}
\Gamma(d_X;q)
 &=\Gamma(R_{\rm parent};q)-\Gamma(R_{ch};q)
   +\Gamma(d_{ch};q)\\
 &\le\Gamma(R_{\rm parent};q),
\end{aligned}}
 \tag{L-91663.12}
\]

and

\[
\boxed{
\begin{aligned}
\Xi(d_X;q)
 &=\Xi(R_{\rm parent};q)-\Xi(R_{ch};q)
   +\Xi(d_{ch};q)\\
 &\le\Xi(R_{\rm parent};q).
\end{aligned}}
 \tag{L-91663.13}
\]

These are the simultaneous residual-capacity inequalities requested by PR
#450, after the complete current row is summed. The ordinary inequality is
direct. Alternatively, (L-91663.13) supplies the antecedent of `L-90029`, whose
positive telescope reconstructs ordinary feasibility.

The child embedding is the identity on row indices. There is no affine Pascal
lift, fractional physical column, duplicated small-prime block or hidden scalar
child.

## 5. Boundary and score firewall

Hall bonuses are literal current rows, not signed boundary certificates. The
recursive child carries no root-only collar, omission or common-port coordinate.
Any finite root correction is current and used once.

This theorem is a row/capacity theorem. Exact capacity does not identify the
continuum equality score with the finite row score up to an absolute constant.
The finite/continuum and endpoint-boundary score ledger is paid generation by
generation in `L-91665/T-91101`.

```text
component response formula                         EXACT
native equality response                           EXACTLY w_X, Omega_X
leafwise Hall row identity                         EXACT ON FROZEN INPUTS
current row after child subtraction                NONNEGATIVE
ordinary residual inequality                       DISPLAYED
radix-four residual inequality                     DISPLAYED
negative butterfly centers                         NOT USED
recursive root port                                NOT USED
score transfer                                     SEPARATE
Riemann Hypothesis                                 UNPROVEN
```
