# L-91003 — The complete safe-line hierarchy has one square-root generating transform

Claim ID: `L-91003`  
Status: **EXACT GENERATING-FUNCTION IDENTITY AND EULER-RADIUS FIREWALL**  
Created: 2026-08-11  
Depends on: `L-90905` and `T-91001`  
RH status: **unproved**

## 1. The confluent differential source

Let

\[
 \mathscr X(s)=-\frac{\xi'(s)}{\xi(s)},
 \qquad r=\sqrt\alpha,
\]

and write the confluent safe-line source of `L-90905` as

\[
 \mathcal D_\alpha\mathscr X(s)
 =\frac{\mathscr X(s+r)}{2r^3}
 -\frac{\mathscr X'(s+r)}{2r^2}
 -\frac{\mathscr X''(s+r)}{2r}.
\tag{L-91003.1}
\]

It has the exact first-derivative form

\[
\boxed{
 \mathcal D_\alpha\mathscr X(s)
 =-\frac d{d\alpha}
 \left[
  \mathscr X'(s+\sqrt\alpha)
  +\frac{\mathscr X(s+\sqrt\alpha)}{\sqrt\alpha}
 \right].
}
\tag{L-91003.2}
\]

For `k>=0`, put

\[
 \mathcal H_k(s)
 =(-\partial_\alpha)^k
  \mathcal D_\alpha\mathscr X(s)\big|_{\alpha=1}.
\tag{L-91003.3}
\]

## 2. Exact ordinary generating function

Define

\[
 \mathcal G_s(w)
 =\sum_{k\ge0}\frac{\mathcal H_k(s)}{(k+2)!}w^k.
\tag{L-91003.4}
\]

Taylor's theorem and

\[
 \int_0^1(1-t)t^kdt=\frac1{(k+1)(k+2)}
\]

give

\[
 \mathcal G_s(w)
 =\int_0^1(1-t)\,
   \mathcal D_{1-wt}\mathscr X(s)\,dt.
\tag{L-91003.5}
\]

Let

\[
 r_w=\sqrt{1-w}
\]

with the branch satisfying `r_0=1`. Integrating (L-91003.2) exactly yields

\[
\boxed{
 \mathcal G_s(w)
 =\frac{
  (2-w)\mathscr X(s+1)
  -w\mathscr X'(s+1)
  -2r_w\mathscr X(s+r_w)
 }{w^2}.
}
\tag{L-91003.6}
\]

The apparent singularity at `w=0` is removable and its Taylor coefficients are precisely (L-91003.4).

For `s_x=1/2+ix`, the real-coefficient Stieltjes function of `T-91001` is

\[
\boxed{
 \mathcal A_x(w)
 =-\frac12\left[
  \mathcal G_{s_x}(w)+\mathcal G_{\overline{s_x}}(w)
 \right].
}
\tag{L-91003.7}
\]

Equation (L-91003.6) makes every pole correspondence immediate:

\[
 s_x+\sqrt{1-w}=\rho
 \quad\Longleftrightarrow\quad
 w=1-(\rho-s_x)^2.
\tag{L-91003.8}
\]

## 3. Closed Euler weight

Apply (L-91003.6) to one Euler exponential

\[
 \mathscr X(s+r)=e^{-t(s+r)}.
\]

Since `mathscr X'=-t mathscr X`, one obtains

\[
\boxed{
 \sum_{k\ge0}
  \frac{e^{-t}P_k(t)}{(k+2)!}w^k
 =\frac{
   (2-w+wt)e^{-t}
   -2\sqrt{1-w}\,e^{-t\sqrt{1-w}}
 }{w^2}.
}
\tag{L-91003.9}
\]

Equivalently,

\[
\boxed{
 \sum_{k\ge0}
  \frac{P_k(t)}{(k+2)!}w^k
 =\frac{
   2-w+wt
   -2\sqrt{1-w}\,e^{t(1-\sqrt{1-w})}
 }{w^2}.
}
\tag{L-91003.10}
\]

This is the complete all-order generating weight for the single safe Euler line.

## 4. The exact absolute-Euler disk

If `|w|<3/4`, then

\[
 \Re(1-w)>\frac14
\]

and therefore

\[
 \Re\sqrt{1-w}
 =\sqrt{\frac{|1-w|+\Re(1-w)}2}
 >\frac12.
\tag{L-91003.11}
\]

Hence

\[
 \Re(s_x+\sqrt{1-w})>1,
\]

so every term in (L-91003.6) has an absolutely convergent Euler expansion. In particular,

\[
\boxed{
 \mathcal G_{s_x}^{\rm prime}(w)
 =\sum_{n\ge2}\Lambda(n)n^{-s_x}
  \frac{
   (2-w+w\log n)n^{-1}
   -2\sqrt{1-w}\,n^{-\sqrt{1-w}}
  }{w^2}
}
\tag{L-91003.12}
\]

converges absolutely and locally uniformly on `|w|<3/4`.

The radius `3/4` is sharp for this direct absolute-Euler realization. On the positive real radius,

\[
 \Re(s_x+\sqrt{1-w})
 =\frac12+\sqrt{1-w},
\]

which equals `1` at `w=3/4` and enters the critical strip for `w>3/4`.

Thus:

```text
coefficient-by-coefficient hierarchy:  always evaluated at Re(s)=3/2;
all-order generating sum:              absolutely Eulerian only for |w|<3/4;
RH-detecting poles:                     live precisely in 3/4<w<1.
```

Crossing the annulus `3/4<|w|<1` is not a routine dominated-convergence step. It is the analytic continuation in which off-line zero poles can occur.

## 5. Boundary

Exact here:

```text
all safe-line orders -> one square-root transform;
closed all-order Euler weight;
pole map w=1-(rho-s_x)^2;
maximal direct absolute-Euler disk |w|<3/4.
```

Open:

```text
prime-side Stieltjes/Pick continuation through 3/4<|w|<1;
Riemann Hypothesis.
```