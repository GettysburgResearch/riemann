# L-23204 — Finite Selberg–Hankel certificate for terminal packet energies

Claim ID: `L-23204`  
Title: A positive exponential-adjoint majorant plus a source-bound residual gives a fail-closed terminal Type-I energy estimate  
Status: **PROPOSED EXACT CERTIFICATE ADAPTER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: PR #229 `L-23001`; PR #216 `L-21503`; `L-15157`; `L-23203`  
Scope: finite terminal packet closure; construction of the certificate remains open

## 1. Centered Selberg equation

Let

\[
dP_0(y)=e^{y/2}\mathbf1_{y\ge0}\,dy,
\qquad
\mathscr L\nu=y\,d\nu+2dP_0*d\nu.
\tag{L-23204.1}
\]

Use the exact centered Selberg equation in the normalization of `L-21503`:

\[
\boxed{
\mathscr L\nu+\nu*\nu=R.
}
\tag{L-23204.2}
\]

The normalization, signs, and shift by `1/2` must be source bound in every
production packet.

For `lambda>1/2`, define

\[
w_\lambda(s)
=
\mathbf1_{s\ge\lambda}
\left(\frac{\lambda-1/2}{s-1/2}\right)^2,
\qquad
f_\lambda(y)=
\int_\lambda^\infty e^{-sy}w_\lambda(s)\,ds.
\tag{L-23204.3}
\]

`L-23001` proves

\[
\mathscr L^*f_\lambda=e^{-\lambda y},
\tag{L-23204.4}
\]

and the Hankel kernel `f_lambda(u+v)` is positive semidefinite.

## 2. One terminal packet

Let `tau` be a terminal Type-I packet at output block `J`. Its exact
source-bound energy is

\[
E_\tau(J)
=
\iint K_{\tau,J}(u,v)\,d\nu(u)d\nu(v),
\qquad
K_{\tau,J}\succeq0.
\tag{L-23204.5}
\]

A **finite terminal Selberg–Hankel certificate** consists of:

1. exponents `lambda_ell>1/2`;
2. nonnegative rational or directed weights `a_ell`;
3. the positive Hankel mixture
   \[
   F_{\tau,J}(y)=\sum_{\ell=1}^{L}a_\ell f_{\lambda_\ell}(y);
   \tag{L-23204.6}
   \]
4. a declared lower-scale positive kernel `K_tau,J^low`;
5. a finite exact Loewner certificate on the actual represented source span:
   \[
   \boxed{
   K_{\tau,J}(u,v)
   \preceq
   F_{\tau,J}(u+v)+K_{\tau,J}^{\rm low}(u,v);
   }
   \tag{L-23204.7}
   \]
6. a source-bound forcing estimate
   \[
   \boxed{
   \langle R,F_{\tau,J}\rangle
   -
   \sum_\ell a_\ell H(\lambda_\ell)
   \le A_{\tau,J},
   }
   \tag{L-23204.8}
   \]
   where
   \[
   H(\lambda)=\int e^{-\lambda y}\,d\nu(y);
   \tag{L-23204.9}
   \]
7. a routing certificate
   \[
   \langle\nu\otimes\nu,K_{\tau,J}^{\rm low}\rangle
   \le L_{\tau,J}
   \tag{L-23204.10}
   \]
   expressed entirely in declared lower-scale auxiliary energies.

No sign of `nu` is assumed.

## 3. Exact terminal bound

Pair (L-23204.2) with `F_tau,J`. Equations (L-23204.4) and
(L-23204.6) give

\[
\begin{aligned}
\langle\nu*\nu,F_{\tau,J}\rangle
&=
\langle R,F_{\tau,J}\rangle
-
\langle\nu,\mathscr L^*F_{\tau,J}\rangle\\
&=
\langle R,F_{\tau,J}\rangle
-
\sum_\ell a_\ell H(\lambda_\ell).
\end{aligned}
\tag{L-23204.11}
\]

The left side is nonnegative because `F_tau,J` is a positive Hankel mixture.
Using the Loewner majorization and the two certificate bounds,

\[
\boxed{
E_\tau(J)\le A_{\tau,J}+L_{\tau,J}.
}
\tag{L-23204.12}
\]

This is an exact implication. The positive quadratic Selberg channel is retained
rather than discarded or replaced by total variation.

## 4. The terminal contraction certificate `STC(K)`

Fix one `0<delta<1/2` using `L-15157`. For packet order `K`, `STC(K)` requires
a certificate of the form above for every terminal type and every sufficiently
large block, with

\[
A_{\tau,J}+L_{\tau,J}
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+\max_h\max_{u\le(1-\delta)J+O_K(1)}E_h(u)
\right].
\tag{L-23204.13}
\]

The finite terminal list is supplied by the source packet dictionary. The
certificate must bind:

```text
source and normalization digests
terminal kernel
positive exponential weights and exponents
Hankel Gram/Loewner proof
Selberg forcing contraction
real-axis linear reserve
lower-scale residual routes
all endpoint and cutoff terms
eta_K and fixed delta
```

Because `delta` is fixed, `eta_K -> 0` is sufficient in the linear system.
Together with `L-23203` and `T-15122`, this closes the complete packet system and
implies RH. The tensor version retains its separate
`eta_K/(1-kappa_K) -> 0` requirement.

## 5. Connection to dyadic prime transport

The linear quantities `H(lambda_ell)` are ordinary real-axis exponential
probes. They are the natural interface to the prime-polygon and Haar/dilation
transport reserves of PRs #218/#219.

A valid production proof may pay (L-23204.8) through:

- an exact prime-transport reserve;
- a directed real-axis Selberg identity;
- a positive Stieltjes/Hankel factorization;
- another independently reviewed one-sided inequality.

It may not assume compact stop-loss Hankel positivity: `R-23001` proves that
shortcut false.

## 6. First-cell audit

The complete output block controlled by `STC(K)` has the same rightmost-zero
exponent as the original safe prime block. Through the cross-route transfer, it
must in particular imply the fixed-ratio Mertens bounds of `L-23202`.

Therefore a certificate that closes all terminal packets while leaving the
first-cell Mertens coordinate uncontrolled is incomplete. The first-cell
decoder is a mandatory mutation test, not an optional interpretation.

## 7. Proof boundary

Closed here:

- the finite positive-Hankel adapter;
- the exact Selberg pairing;
- the terminal-energy implication;
- the fail-closed certificate schema.

Open:

- construction of `STC(K)` for an unbounded sequence of orders;
- the rate `eta_K -> 0`;
- RH.
