# L-105200 — One positive Poisson localizer simultaneously measures critical count and the first two residue moments

Claim ID: `L-105200`  
Status: **PROVED EXACT FINITE-POLYNOMIAL THEOREM**  
Created: 2026-08-23  
Depends on: PR #720 `L-104523`; PR #723 `L-105100`  
RH status: **not assumed**

Let `p` be a real polynomial of degree `n>=2`. Assume:

1. every zero `c` of `p'` is simple and `p(c)!=0`;
2. every zero `d` of `p''` is simple.

Then `p'(d)!=0` at every zero of `p''`. Put

\[
\rho_c=\frac{p(c)}{p''(c)},
\qquad
\tau_d=\frac{p(d)^2}{p'(d)p'''(d)}.
\tag{L-105200.1}
\]

Fix a real centre `a` and a scale `T>0`. Define the common positive real-axis
localizer

\[
\boxed{
\Omega_{a,T}(z)
=\frac{T^6}{\bigl((z-a)^2+T^2\bigr)^3}.
}
\tag{L-105200.2}
\]

For real `x`,

\[
0<\Omega_{a,T}(x)\le1.
\]

Let

\[
\zeta=a+iT
\]

and, for a rational function `R` with real coefficients and growth at most
cubic at infinity, define

\[
\boxed{
\mathfrak B_{a,T}[R]
=\frac18\left[
T^3\Im R''(\zeta)
+3T^2\Re R'(\zeta)
-3T\Im R(\zeta)
\right].
}
\tag{L-105200.3}
\]

## 1. Universal localized-residue identity

Suppose the finite poles of `R` are simple, real or conjugate paired, and let
`r_w=Res_(z=w) R(z)`. Then

\[
\boxed{
\sum_w \Omega_{a,T}(w)r_w
=\mathfrak B_{a,T}[R].
}
\tag{L-105200.4}
\]

The sum is algebraic; nonreal poles are included with their conjugates.

### Proof

The localizer has triple poles at `zeta` and `bar(zeta)`. Since

\[
\Omega_{a,T}(z)R(z)
=\frac{T^6R(z)}{(z-\zeta)^3(z-\bar\zeta)^3},
\]

the residue at `zeta` is

\[
\frac{T^6}{2}
\left[
\frac{R''(z)}{(z-\bar\zeta)^3}
-\frac{6R'(z)}{(z-\bar\zeta)^4}
+\frac{12R(z)}{(z-\bar\zeta)^5}
\right]_{z=\zeta}.
\]

Using `zeta-bar(zeta)=2iT`, this is

\[
\frac1{16}
\left[iT^3R''(\zeta)-3T^2R'(\zeta)-3iTR(\zeta)\right].
\tag{L-105200.5}
\]

The residue at `bar(zeta)` is its conjugate. Since
`Omega R=O(z^-3)` or better at infinity, its residue at infinity is zero.
The residue theorem therefore says that the residues at the finite poles of
`R` equal minus twice the real part of (L-105200.5), which is exactly
(L-105200.3).

## 2. Localized critical-point count

Apply (L-105200.4) to

\[
R_0(z)=\frac{p''(z)}{p'(z)}.
\]

Its residue at every zero of `p'` is one. Therefore

\[
\boxed{
\sum_{p'(c)=0}\Omega_{a,T}(c)
=\mathfrak B_{a,T}\!\left[\frac{p''}{p'}\right].
}
\tag{L-105200.6}

## 3. Localized first residue moment

Apply (L-105200.4) to

\[
R_1(z)=\frac{p(z)}{p'(z)}.
\]

The residue at `c` is `rho_c`, so

\[
\boxed{
\sum_{p'(c)=0}\Omega_{a,T}(c)\rho_c
=\mathfrak B_{a,T}\!\left[\frac p{p'}\right].
}
\tag{L-105200.7}

This is a height-localized replacement for the global centred-root-variance
identity of `L-104524`.

## 4. Localized second residue balance

Apply (L-105200.4) to

\[
R_2(z)=\frac{p(z)^2}{p'(z)p''(z)}.
\]

At a zero `c` of `p'` its residue is `rho_c^2`. At a zero `d` of `p''` its
residue is `tau_d`. Hence

\[
\boxed{
\sum_{p'(c)=0}\Omega_{a,T}(c)\rho_c^2
+
\sum_{p''(d)=0}\Omega_{a,T}(d)\tau_d
=
\mathfrak B_{a,T}\!\left[\frac{p^2}{p'p''}\right].
}
\tag{L-105200.8}

Unlike `L-105100`, this is localized by one positive real-axis weight and does
not use a root-moment ledger at infinity.

## 5. Exact real/nonreal split

Let

\[
\mathcal R=\{c\in\mathbb R:p'(c)=0\},
\qquad
\mathcal C=\{c\notin\mathbb R:p'(c)=0\}.
\]

Define

\[
N_{a,T}=\sum_{c\in\mathcal R}\Omega_{a,T}(c),
\]

\[
M_{1;a,T}=-\sum_{c\in\mathcal R}\Omega_{a,T}(c)\rho_c,
\]

\[
M_{2;a,T}=\sum_{c\in\mathcal R}\Omega_{a,T}(c)|\rho_c|^2.
\]

Then

\[
\boxed{
M_{1;a,T}
=-\mathfrak B_{a,T}\!\left[\frac p{p'}\right]
+
\sum_{c\in\mathcal C}\Omega_{a,T}(c)\rho_c,
}
\tag{L-105200.9}
\]

and

\[
\boxed{
M_{2;a,T}
=
\mathfrak B_{a,T}\!\left[\frac{p^2}{p'p''}\right]
-
\sum_{c\in\mathcal C}\Omega_{a,T}(c)\rho_c^2
-
\sum_{p''(d)=0}\Omega_{a,T}(d)\tau_d.
}
\tag{L-105200.10}

Conjugate pairing makes both right-hand sides real. Neither correction has a
fixed sign in general.

## 6. Smooth residue coherence

When `N_(a,T) M_(2;a,T)>0`, define

\[
\boxed{
\mathfrak C_{a,T}
=\frac{M_{1;a,T,+}^2}{N_{a,T}M_{2;a,T}}.
}
\tag{L-105200.11}
\]

Because the same positive weight occurs in all three quantities,
Cauchy--Schwarz gives

\[
0\le\mathfrak C_{a,T}\le1.
\]

More precisely, if

\[
G_{a,T}=\sum_{\substack{c\in\mathcal R\\\rho_c<0}}
\Omega_{a,T}(c),
\]

then

\[
\boxed{
G_{a,T}\ge\frac{M_{1;a,T,+}^2}{M_{2;a,T}}
=N_{a,T}\mathfrak C_{a,T}.
}
\tag{L-105200.12}

Thus `mathfrak C_(a,T)>1/2` forces more than half of the localized critical
mass to have the Rolle-generating orientation. This is the smooth weighted
counterpart of `L-104522`.

## 7. Scope

The theorem is finite and exact. It does not pass automatically to an entire
function, does not remove the `p''` debt in (L-105200.10), and does not bound
the nonreal-critical correction. `L-105201` gives a canonical finite Bézout
removal of the debt; an entire-function interpolation analogue remains a
separate theorem.
