# L-106502 — The Xi odd-current profile saturates at high source frequency

Claim ID: `L-106502`  
Status: **PROVED ANALYTICALLY FROM THE EXPLICIT XI KERNEL; INDEPENDENT CONSTANT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: `L-105413`, `L-106500`; the explicit positive Xi Fourier kernel  
RH status: **not assumed**

Let `Phi` be the positive even Xi Fourier kernel and let `K=2m+1` be fixed.
Retain the positive densities

\[
L_K(\xi)=\widehat{\mathcal L_K}(\xi)
\]

and

\[
J_{K,h}(\xi)=\widehat J_{K,h}(\xi)
\]

from `L-106500`.  Define the **untranslated** current profile

\[
\boxed{
r^\sharp_{K,h}(\xi)
={hL_K(\xi)\over J_{K,h}(\xi)},
\qquad 0\le r^\sharp_{K,h}\le1,
}
\tag{L-106502.1}

with value `1` at a common zero and at `h=0` by continuity.  Unlike the
causally translated profile, (L-106502.1) does not contain an artificial
factor `e^(-h xi)`.

## 1. Conditional-difference representation

Put

\[
u={\xi-d\over2},\qquad v={\xi+d\over2},
\]

and let

\[
d\mu_{K,\xi}(d)
={d(v^K-u^K)\Phi(u)\Phi(v)\,dd
 \over
 \int d(v^K-u^K)\Phi(u)\Phi(v)\,dd}.
\tag{L-106502.2}

The density is nonnegative because `K` is odd.  Equations
`L-106500.2` and `L-106500.6` give the exact scalar identity

\[
\boxed{
{J_{K,h}(\xi)\over hL_K(\xi)}
=\int {\sinh(hd)\over hd}\,d\mu_{K,\xi}(d).
}
\tag{L-106502.3}

Thus the profile defect is precisely the excess hyperbolic moment of the
conditional source difference.

## 2. Xi conditional concentration

For every fixed odd `K`, every `h_0<infinity`, and every integer `q>=1`, there
are constants `C_(K,q,h_0)` and `xi_0` such that

\[
\boxed{
\int |d|^{2q}e^{h_0|d|}\,d\mu_{K,\xi}(d)
\le C_{K,q,h_0}e^{-q\xi},
\qquad \xi\ge\xi_0.
}
\tag{L-106502.4)

The proof is source explicit.  On the balanced region, the first theta orbit
and `L-105413` give

\[
{\Phi((\xi-d)/2)\Phi((\xi+d)/2)
 \over \Phi(\xi/2)^2}
\le C(1+|d|)^A e^{A|d|}
\exp\{-2\pi e^\xi(\cosh d-1)\}.
\tag{L-106502.5}

Since `cosh d-1 >= c min(d^2,|d|)`, its `2q`th weighted moment is
`O(e^(-q xi))`.  On `|d|<=1`,

\[
c_K\xi^{K-1}d^2
\le d(v^K-u^K)
\le C_K\xi^{K-1}d^2,
\]

so the polynomial weight changes only the Gaussian moment order.  If one of
`u,v` leaves the first-orbit region, the explicit theta series is smaller than
the balanced source by `exp(-c e^xi)` and is absorbed.  These estimates also
supply the denominator lower bound required to normalize (L-106502.2).

## 3. Saturation

For `0<=h<=h_0`,

\[
0\le {\sinh(hd)\over hd}-1
\le C_{h_0}h^2d^2e^{h_0|d|}.
\]

Combining this with (L-106502.3)--(L-106502.4) gives

\[
\boxed{
0\le1-r^\sharp_{K,h}(\xi)
\le C_{K,h_0}h^2e^{-\xi},
\qquad \xi\ge\xi_0.
}
\tag{L-106502.6}

In particular, for the fifth endpoint,

\[
\boxed{
r^\sharp_{5,h}(\xi)=1+O_{h_0}(h^2e^{-\xi}).}
\tag{L-106502.7}

The current metric therefore approaches the physical first chaos precisely in
the high-frequency region occupied by shallow model-space exponentials.

## 4. One-factor reserve

Let

\[
e_{a,y}(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi},
\qquad y>0,
\]

be the normalized Fourier model vector of a simple upper-half-plane factor.
Using `1-r<=1` below `xi_0` and (L-106502.6) above it gives

\[
\boxed{
\langle e_{a,y},(I-R^\sharp_{K,h})e_{a,y}\rangle
\le C'_{K,h_0,\xi_0}(1+h^2)y.
}
\tag{L-106502.8)

Thus the reserve cost of a pole approaching the real axis is proportional to
its depth, rather than one unit.

## 5. Scope

The theorem controls the diagonal current reserve.  It does not commute that
reserve through the endpoint all-pass phase, sum it over a nonorthogonal
confluent model space without a causal ordering argument, or prove
`FIFTHPHASE106500`.  No zero-count conclusion is asserted here.
