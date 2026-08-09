# L-90015 — Every parabolic column residual is driven by one positive occupancy source

Claim ID: `L-90015` (provisional branch range)  
Title: The residual of every individual carry column is a positive occupancy-deficit source convolved with the universal one-sign-change Green kernel  
Status: **PROPOSED COMPLETE EXACT ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #352 `L-90004`; the parabolic seed definition; elementary Mellin/Laplace calculus  
Scope: every integer carry column; no aggregate endpoint sign and no RH conclusion

## 1. Column residual

Retain the parabolic seed

\[
 b_X(m)=2\sqrt m\left[
  \log\frac Xm-2\left(1-\sqrt{\frac mX}\right)
 \right]\mathbf 1_{m\le X},
\tag{L-90015.1}
\]

the column response

\[
 v_q(X)=\sum_{k\ge1}
 [b_X(kq)-b_X(kq+1)],
\tag{L-90015.2}
\]

and

\[
 r_X(q)=v_q(X)-q^{-1/2}\log(X/q)
 \qquad(X\ge q,\ q\ge2).
\tag{L-90015.3}
\]

For complex `z` with `Re z>1/2`, put

\[
 w=z-\frac12.
\]

The single-node Mellin integral is

\[
 \int_m^\infty b_X(m)X^{-z-1}\,dX
 ={m^{-w}\over z^2(w+1)}.
\tag{L-90015.4}
\]

Consequently, with

\[
 D_q(w)=\sum_{k\ge1}
 [(kq)^{-w}-(kq+1)^{-w}],
\tag{L-90015.5}
\]

one has exactly

\[
\boxed{
 \widehat r_q(z)
 :=\int_q^\infty r_X(q)X^{-z-1}\,dX
 ={1\over z^2}\left[
 {D_q(w)\over w+1}-q^{-w-1}
 \right].
}
\tag{L-90015.6}
\]

The difference series is absolutely convergent for `Re w>0`.

## 2. Occupancy deficit

Define the periodic unit-occupancy set

\[
 \mathcal U_q=\bigcup_{k\ge1}[kq,kq+1]
\tag{L-90015.7}
\]

and, for `x>=q`,

\[
 H_q(x)=|\mathcal U_q\cap[q,x]|,
 \qquad
 \Delta_q(x)={x\over q}-H_q(x).
\tag{L-90015.8}
\]

If `x=kq+r`, `0<=r<q`, then directly

\[
\boxed{
 \Delta_q(x)=
 \begin{cases}
  1-(1-q^{-1})r,&0\le r\le1,\\[1mm]
  r/q,&1\le r<q.
 \end{cases}}
\tag{L-90015.9}
\]

Hence

\[
\boxed{q^{-1}\le\Delta_q(x)\le1.}
\tag{L-90015.10}
\]

In particular, `Delta_q` is an explicit positive continuous sawtooth. It contains no prime or Möbius input.

For real `w>0`, the fundamental theorem of calculus gives

\[
 D_q(w)=w\int_{\mathcal U_q}x^{-w-1}\,dx.
\tag{L-90015.11}
\]

Integrating the cumulative deficit in (L-90015.8) by parts, using

\[
 \Delta_q(q)=1,
 \qquad
 \Delta_q'(x)=q^{-1}-\mathbf1_{\mathcal U_q}(x)
\]

away from the harmless corners, gives

\[
\boxed{
 q^{-w-1}-{D_q(w)\over w+1}
 =w\int_q^\infty\Delta_q(x)x^{-w-2}\,dx>0.
}
\tag{L-90015.12}
\]

Combining (L-90015.6) and (L-90015.12),

\[
\boxed{
 \widehat r_q(z)<0
 \qquad(q\ge2,\ z>1/2\text{ real}).
}
\tag{L-90015.13}
\]

Thus every individual column already has the desired sign against every positive real Mellin probe.

An equivalent one-line proof uses the Hurwitz-zeta formula

\[
 D_q(w)
 =wq^{-w}\int_0^{1/q}\zeta(w+1,1+u)\,du
\tag{L-90015.14}
\]

and the strict integral-test bound

\[
 \zeta(w+1,1+u)
 <(1+u)^{-w-1}+{(1+u)^{-w}\over w}
 \le{w+1\over w}.
\]

## 3. Exact causal Green form

Put

\[
 X=qe^t,
 \qquad
 f_q(t)=\sqrt q\,r_{qe^t}(q),
\tag{L-90015.15}
\]

and define the positive source

\[
\boxed{
 Q_q(u)=e^{-u/2}\Delta_q(qe^u)>0.
}
\tag{L-90015.16}
\]

Changing variables in (L-90015.12) gives, for `Re z>1/2`,

\[
\boxed{
 -\widetilde f_q(z)
 ={z-\frac12\over z^2}\widetilde Q_q(z).
}
\tag{L-90015.17}
\]

The inverse Laplace transform of

\[
 {z-\frac12\over z^2}
 ={1\over z}-{1\over2z^2}
\]

is the universal kernel

\[
 k(a)=1-{a\over2}.
\]

Laplace uniqueness therefore yields the exact physical identity

\[
\boxed{
 -f_q(t)
 =\int_0^t\left(1-{t-u\over2}\right)Q_q(u)\,du.
}
\tag{L-90015.18}
\]

No asymptotic estimate or analytic continuation is used in this time-domain formula.

Let

\[
 A_q(t)=\int_0^tQ_q(u)\,du,
 \qquad
 \bar u_q(t)={\int_0^tuQ_q(u)\,du\over A_q(t)}.
\]

Then

\[
\boxed{
 f_q(t)
 ={A_q(t)\over2}
 [t-2-\bar u_q(t)].
}
\tag{L-90015.19}
\]

Thus the sign of one column is exactly a backward-mean-age comparison for one positive source.

## 4. Fixed columns are eventually positive

The source satisfies

\[
 0<Q_q(u)\le e^{-u/2}.
\]

Therefore

\[
 A_q(\infty)=\int_0^\infty Q_q(u)\,du\in(0,\infty),
\]

and its first moment is finite as well. Equation (L-90015.19) gives

\[
\boxed{
 f_q(t)
 ={A_q(\infty)\over2}t+O_q(1)
 \longrightarrow+\infty.
}
\tag{L-90015.20}
\]

On the other hand `f_q(0)=0`, and (L-90015.18) gives

\[
 f_q'(0)=-Q_q(0)=-1.
\]

Hence every fixed carry column is negative immediately after activation but positive for all sufficiently large scale ratios:

\[
\boxed{
 r_X(q)<0\text{ for }X/q>1\text{ sufficiently close to }1,
 \qquad
 r_X(q)>0\text{ for }X/q\text{ sufficiently large}.
}
\tag{L-90015.21}
\]

This is a mandatory firewall. The strict real-Mellin sign (L-90015.13) cannot be upgraded to pointwise negativity, and a proof of the prime endpoint must retain the moving column boundary.

## 5. Proof boundary

Closed exactly here:

1. the fixed-column Mellin transform;
2. the positive occupancy-deficit sawtooth;
3. the strict negative sign of every positive-real Mellin moment;
4. the positive-source Green factorization;
5. the mean-age sign formula;
6. eventual positivity of every fixed column.

Open:

1. aggregate control after prime or prime-power weighting;
2. eventual sign of the prime endpoint;
3. RH.