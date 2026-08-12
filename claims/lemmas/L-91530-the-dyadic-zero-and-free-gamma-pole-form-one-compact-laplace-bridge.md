# L-91530 — The dyadic zero and free gamma pole form one compact Laplace bridge

Claim ID: `L-91530`  
Status: **PROVED EXACT COMPLETED FACTORIZATION AND COMPACT POLE CANCELLATION**  
Created: 2026-08-12  
Depends on: `L-91430`; `L-91330` on PR #403  
RH status: **unproved**

## 1. Endpoint notation

Fix

\[
 0<\omega<\frac12,
 \qquad
 s_0=1-\omega,
 \qquad
 s_1=1+\omega,
 \qquad
 L=\log2.
 \tag{L-91530.1}

\]

Define the entire finite-interval Laplace function

\[
\boxed{
 F_L(z)
 =\frac{1-e^{-Lz}}{z}
 =\int_0^L e^{-zt}\,dt,
 \qquad F_L(0)=L.
}
\tag{L-91530.2}

\]

## 2. Dyadic and gamma endpoint factors

The eta/dyadic factorization gives

\[
 \frac{\zeta(s-\omega)}{\zeta(s+\omega)}
 =\frac{\eta_D(s-\omega)}{\eta_D(s+\omega)}
  \frac{1-e^{-L(s-s_0)}}
       {1-e^{-L(s-s_1)}}.
 \tag{L-91530.3}

\]

The rational endpoint part of the completed gamma factor is

\[
 \frac{s-\omega-1}{s+\omega-1}
 =\frac{s-s_1}{s-s_0}.
 \tag{L-91530.4}

\]

Multiplying (L-91530.3) and (L-91530.4), the zero and pole cancel exactly:

\[
\boxed{
 \frac{1-e^{-L(s-s_0)}}
      {1-e^{-L(s-s_1)}}
 \frac{s-s_1}{s-s_0}
 =\frac{F_L(s-s_0)}{F_L(s-s_1)}.
}
\tag{L-91530.5}

\]

Both apparent singularities at `s_0` and `s_1` are removable.

## 3. Exact completed Xi factorization

Using

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

we obtain

\[
\boxed{
\begin{aligned}
 \frac{\xi(s-\omega)}{\xi(s+\omega)}
 ={}&
 \frac{\eta_D(s-\omega)}{\eta_D(s+\omega)}
 \frac{F_L(s-s_0)}{F_L(s-s_1)}\\
 &\times
 \pi^\omega
 \frac{s-\omega}{s+\omega}
 \frac{\Gamma((s-\omega)/2)}
      {\Gamma((s+\omega)/2)}.
\end{aligned}}
\tag{L-91530.6}

\]

This is an exact reorganization of the completed horizontal quotient. The
global pole-zero cancellation is now one finite-interval Laplace ratio, not a
limit of finite Euler products.

## 4. Compact physical bridge

The dangerous free pole component is proportional to

\[
 \frac1{s-s_0},
\]

whose inverse Laplace source is the non-Hilbert tail

\[
 e^{s_0t}\mathbf1_{t>0}.
\]

Multiplication by the dyadic numerator gives

\[
\boxed{
 \frac{1-e^{-L(s-s_0)}}{s-s_0}
 =F_L(s-s_0),
}
\tag{L-91530.7}

\]

whose inverse Laplace source is

\[
\boxed{
 e^{s_0t}\mathbf1_{0<t<L}.
}
\tag{L-91530.8}

\]

Thus the coefficient-one dyadic zero truncates the unstable gamma pole tail to
one compact log interval before any norm is taken.

After the standard Hardy weight `e^(-t/2)`, the bridge vector is

\[
 b_\omega(t)
 =e^{(1/2-\omega)t}\mathbf1_{0<t<L},
 \tag{L-91530.9}

\]

and

\[
\boxed{
 \|b_\omega\|_2^2
 =\frac{2^{1-2\omega}-1}{1-2\omega},
}
\tag{L-91530.10}

\]

with the removable limit `log 2` at `omega=1/2`.

## 5. Endpoint values

The compact ratio has finite positive values at both old singular nodes:

\[
\boxed{
 \left.\frac{F_L(s-s_0)}{F_L(s-s_1)}\right|_{s=s_0}
 =\frac{L}{F_L(-2\omega)}>0,
}
\tag{L-91530.11}

\]

\[
\boxed{
 \left.\frac{F_L(s-s_0)}{F_L(s-s_1)}\right|_{s=s_1}
 =\frac{F_L(2\omega)}{L}>0.
}
\tag{L-91530.12}

\]

The pole coefficient of `L-91330` and the dyadic zero coefficient of
`L-91430` are therefore incorporated in one regular positive source factor.

## 6. Significance

The most dangerous part of the sector-changing proposal is no longer an
unbounded pole bridge. It is a compact finite-interval exponential-tilt
channel. This cancellation is global and coefficient one, but it is now
performed explicitly before Hilbert completion.

The remaining noncompact sector change lies in the paired eta tail and the
residual beta/gamma factor of (L-91530.6).

## 7. Exact boundary

```text
dyadic zero x gamma rational pole              COMPACT LAPLACE RATIO
completed Xi eta/bridge/gamma factorization     EXACT
free non-Hilbert pole tail                      CANCELED EXACTLY
compact Hardy bridge norm                       EXACT
paired eta tail sector change                   OPEN
critical/stable model exhaustion                OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
