# R-19876 — The Radon–Nikodym multiplier does not intertwine the triangular input

Claim ID: `R-19876`  
Status: **EXACT OPERATOR-IDENTITY REFUTATION / L-19874.20 WITHDRAWN**  
Created: 2026-08-13  
Depends on: `L-19874`, `L-91307`  
RH status: **unproved**

## 1. The claimed identity

Let

\[
 d\omega(u)=m(u)^2d\beta(u)
\]
and let

\[
 (V_\mu g)(t,u)=\mathbf1_{0<t<u}g(u-t)
\]
be the triangular synthesis.  `L-19874.20` claims

\[
 \widetilde U V_\omega=V_\beta M_m,
\tag{R-19876.1}
\]
where

\[
 (\widetilde UF)(t,u)=m(u)F(t,u).
\]

## 2. Exact variable mismatch

Direct evaluation gives

\[
 (\widetilde UV_\omega g)(t,u)
 =\mathbf1_{t<u}m(u)g(u-t),
\tag{R-19876.2}
\]
whereas

\[
 (V_\beta M_mg)(t,u)
 =\mathbf1_{t<u}m(u-t)g(u-t).
\tag{R-19876.3}
\]

Therefore

\[
\boxed{
 \widetilde UV_\omega=V_\beta M_m
 \iff m(u)=m(u-t)\text{ on the triangular support}.
}
\tag{R-19876.4}
\]

The Jordan/scattering multiplier

\[
 m_a(u)^2
 =\frac{1-(1+2au)e^{-2au}}{a^3u}
\]
is nonconstant: it behaves as `2u/a` at zero and as `1/(a^3u)` at infinity.
Hence (R-19876.1) is false.

The correct lifted identity is only

\[
\boxed{
 \widetilde UV_\omega=M_{m(u)}V_\beta,
}
\tag{R-19876.5}
\]
where the multiplier acts **after** triangular lifting, in the output carrier
`u`.

## 3. Tail-Hankel consequence

The two tail-Hankel expressions are

\[
 H_\omega g(t)
 =\int_{u>t}m(u)^2g(u-t)d\beta(u),
\]

\[
 H_\beta(M_mg)(t)
 =\int_{u>t}m(u-t)g(u-t)d\beta(u).
\]

They are generically different.  Thus the atomic unitary between
`L^2(omega)` and `L^2(beta)` does not identify the Jordan tail-Hankel block
with the ordinary-prime block of `L-91307`.

## 4. Surviving scope

The following parts of `L-19874` survive unchanged:

```text
atomic Radon–Nikodym unitary                    EXACT
atomic carrier multiplication covariance        EXACT
atomic delay-phase covariance                    EXACT
metric-compatible radial connection              EXACT
triangular input intertwining L-19874.20          FALSE
ordinary-prime Julia block obtained automatically FALSE
```

`L-19876` supplies the correct replacement: a radial direct integral with two
carrier ports.
