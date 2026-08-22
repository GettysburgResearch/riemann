# L-90023 — The improved factor-64 criterion is a positive three-tap smoothing of one factor-16 critical state

Claim ID: `L-90023` (provisional range; branch-qualified)  
Title: The rational unit-circle filter factors into a factor-16 critical shell followed by a positive three-tap scale smoother, and its exact annular radical/ramp kernel has one sign change  
Status: **PROPOSED COMPLETE EXACT STATE/SPLINE NORMAL-FORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90018`, `L-90022`  
Scope: exact state and finite annular formulas; no sign theorem or RH claim

## 1. Positive smoothing factorization

Let

\[
 (\mathcal Sf)(X)=f(X/2),
 \qquad q=1/\sqrt2.
\]

The preferred filter factors as

\[
\boxed{
 P_{64}^*(y)
 =\left(1+{3\over4}y+y^2\right)
 (1-y^2)(1-y)(1-qy).
}
\tag{L-90023.1}

Define successively

\[
\boxed{
 C(X)=(I-q\mathcal S)A(X),
}
\tag{L-90023.2}

\[
\boxed{
 H(X)=(I-\mathcal S)C(X),
}
\tag{L-90023.3}

and the factor-16 critical shell

\[
\boxed{
 G(X)=(I-\mathcal S^2)H(X)
 =H(X)-H(X/4).
}
\tag{L-90023.4}

Then the unscaled improved factor-64 scalar is

\[
\boxed{
 \mathcal U_{64}^*(X)
 =G(X)+{3\over4}G(X/2)+G(X/4).
}
\tag{L-90023.5}

Thus the conclusion-producing filter is a positive three-tap smoothing of one fixed factor-16 state. The smoothing polynomial

\[
 1+{3\over4}y+y^2
\]

has both roots on the unit circle, so it damps selected critical-line phases without canceling an off-line pole.

A stronger sufficient theorem is

\[
 G(X)<0\quad(X\gg1),
\tag{L-90023.6}

but (L-90023.6) is not asserted and need not be equivalent to RH. The exact RH-equivalent target is the positive average (L-90023.5).

## 2. Exact ramp spline

Let

\[
 P_{64}^*(y)=\sum_{j=0}^6a_jy^j
\]

with the coefficients of `L-90022`, and define

\[
 \Phi_{64}^*(u)=\sum_{j=0}^6a_j(u-j)_+.
\]

Exact cumulative summation gives

\[
\boxed{
\Phi_{64}^*(u)=
\begin{cases}
 u,&0\le u\le1,\\
 1+(3/4-q)(u-1),&1\le u\le2,\\
 7/4-q-(3q/4)(u-2),&2\le u\le3,\\
 {7\over4}(1-q)-{3\over4}(u-3),&3\le u\le4,\\
 1-{7q\over4}+(-1+3q/4)(u-4),&4\le u\le5,\\
 q(u-6),&5\le u\le6,\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-90023.7}

The first three pieces are positive. At `u=3`,

\[
 \Phi_{64}^*(3)={7\over4}(1-q)>0,
\]

while at `u=4`,

\[
 \Phi_{64}^*(4)=1-{7q\over4}<0
\]

because `49>32`. The fourth piece is strictly decreasing. The fifth piece remains negative and decreases; the last piece increases from `-q` to zero.

Hence there is exactly one interior sign change, at

\[
\boxed{
 u_*={16\over3}-{7\over3\sqrt2}.
}
\tag{L-90023.8}

Therefore

\[
 \Phi_{64}^*(u)>0\quad(0<u<u_*),
 \qquad
 \Phi_{64}^*(u)<0\quad(u_*<u<6).
\tag{L-90023.9}

The critical moment is

\[
\boxed{
 \int_0^6\Phi_{64}^*(u)2^{u/2}\,du=0.
}
\tag{L-90023.10}

## 3. Exact critical seed step function

Define

\[
 \Psi_{64}^*(u)
 =\sum_{0\le j\le u}a_j2^{j/2}.
\]

Exact summation in `Q(sqrt(2))` gives

\[
\boxed{
\Psi_{64}^*(u)=
\begin{cases}
 1,&0\le u<1,\\
 -\sqrt2/4,&1\le u<2,\\
 -3/2,&2\le u<3,\\
 -3\sqrt2/2,&3\le u<4,\\
 -1,&4\le u<5,\\
 4\sqrt2,&5\le u<6,\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-90023.11}

The final return to zero is exactly `P_64^*(sqrt(2))=0`.

## 4. Complete finite radical/ramp formula

Let

\[
 d(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1),
 \qquad
 u_m=\log_2(X/m).
\]

For every `X/64<m<=X`, the filtered parabolic seed coefficient is

\[
\boxed{
 \beta_{64,X}^*(m)
 =2\sqrt m(\log2)\Phi_{64}^*(u_m)
 +{4m\over\sqrt X}\Psi_{64}^*(u_m).
}
\tag{L-90023.12}

It vanishes for `m<=X/64`. Therefore

\[
\boxed{
\begin{aligned}
 \mathcal U_{64}^*(X)
 ={}&\sum_{X/64<m\le X}
 \beta_{64,X}^*(m)d(m)\\
 &-(\log2)
 \sum_{X/64<p\le X}
 {\log p\over\sqrt p}
 \Phi_{64}^*(\log_2(X/p)).
\end{aligned}}
\tag{L-90023.13}

Equation (L-90023.13) is the complete finite preferred coordinate. It contains one annular radical seed and one signed two-sector prime ramp, and nothing outside `[X/64,X]`.

## 5. Two-sector ramp split

Put

\[
 p_*=X/2^{u_*}.
\]

Then

\[
\begin{aligned}
 \mathcal R_+^*(X)
 &=\sum_{p_*<p\le X}{\log p\over\sqrt p}
 \Phi_{64}^*(\log_2(X/p)),\\
 \mathcal R_-^*(X)
 &=\sum_{X/64<p<p_*}{\log p\over\sqrt p}
 [-\Phi_{64}^*(\log_2(X/p))].
\end{aligned}
\]

Both are nonnegative, and

\[
\boxed{
 \mathcal F_{64}^*P_{\mathbb P}(X)
 =\log2\,[\mathcal R_+^*(X)-\mathcal R_-^*(X)].
}
\tag{L-90023.14}

The open arithmetic theorem is precisely to place the annular radical seed against this signed sector difference inside the explicit prime-power moat.

## 6. Proof boundary

Closed exactly:

1. positive three-tap state factorization;
2. exact preferred ramp spline;
3. uniqueness and location of its sign change;
4. exact critical seed step function;
5. complete finite radical/ramp formula;
6. two-sector ramp decomposition.

Still open:

1. a source-specific inequality for (L-90023.13);
2. eventual sign of the improved factor-64 scalar;
3. RH.
