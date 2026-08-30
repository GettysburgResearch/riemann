# L-107100 — Exact multiplicity-sensitive reverse–Rolle identity

Claim ID: `L-107100`  
Status: **PROVED EXACT REAL-ANALYTIC THEOREM**  
Created: 2026-08-30  
Programme parent: PR #714 at `d1a9fea34aa0620a5cb2da41061518638ab8b219`  
RH status: **not assumed**

Let `f` be real analytic on a neighbourhood of a compact interval `[a,b]` and assume

\[
f(a)f'(a)f(b)f'(b)\ne0.
\]

Write

\[
N_I(f)=\sum_{x\in(a,b):f(x)=0}\operatorname{ord}_x f
\]

for the real-zero count with multiplicity. Put

\[
g={f'\over f}.
\]

At a zero `z` of `f` of multiplicity `m`,

\[
g(x)={m\over x-z}+O(1),
\]

so `g` crosses its pole from `-infinity` to `+infinity` exactly once, independently of `m`.

## 1. Nonshared derivative zeros and their orientation

Let

\[
\mathcal C_I(f)
=
\{c\in(a,b):f'(c)=0,\ f(c)\ne0\}.
\]

For `c in C_I(f)`, define

\[
r_c=\operatorname{ord}_c(f')\ge1
\]

and the topological orientation

\[
\iota_c
={1\over2}
\left[
\operatorname{sgn}g(c+)-\operatorname{sgn}g(c-)
\right]
\in\{-1,0,1\}.
\]

Thus `iota_c=+1` for an upward crossing, `-1` for a downward crossing, and `0` for a non-sign-changing derivative zero. Define the exact reverse–Rolle defect

\[
\boxed{
\mathfrak R_I(f)
=
\sum_{c\in\mathcal C_I(f)}(r_c+\iota_c).
}
\tag{L-107100.1}
\]

Every summand is a nonnegative even integer:

```text
simple downward Rolle extremum      r=1, iota=-1, cost 0;
simple upward extra extremum        r=1, iota=+1, cost 2;
even-order stationary criticality   r even, iota=0, cost r;
higher odd downward crossing        r odd, iota=-1, cost r-1;
higher odd upward crossing          r odd, iota=+1, cost r+1.
```

## 2. Exact identity

Define the boundary index

\[
\varepsilon_I(f)
={1\over2}
\left[
\operatorname{sgn}{f'(b)\over f(b)}
-
\operatorname{sgn}{f'(a)\over f(a)}
\right]
\in\{-1,0,1\}.
\tag{L-107100.2}
\]

Then

\[
\boxed{
N_I(f)
=
N_I(f')
-
\mathfrak R_I(f)
+
\varepsilon_I(f).
}
\tag{L-107100.3}
\]

### Proof

Let `Z` be the number of distinct real zeros of `f` in `(a,b)`. If those zeros have multiplicities `m_z`, then the zeros shared by `f` and `f'` contribute

\[
\sum_z(m_z-1)=N_I(f)-Z
\]

to `N_I(f')`. Hence

\[
N_I(f')=N_I(f)-Z+\sum_{c\in\mathcal C_I(f)}r_c.
\tag{L-107100.4}
\]

Track the sign of `g=f'/f` from `a` to `b`. Each zero of `f` contributes one upward pole crossing. Each nonshared derivative zero contributes its index `iota_c`. Therefore

\[
\varepsilon_I(f)
=Z+\sum_{c\in\mathcal C_I(f)}\iota_c.
\tag{L-107100.5}
\]

Eliminating `Z` between (L-107100.4) and (L-107100.5) gives (L-107100.3).

## 3. Laguerre defect in the Morse case

Define

\[
\mathcal L_f(x)=f'(x)^2-f(x)f''(x).
\]

If every nonshared derivative zero is simple, then at `f'(c)=0`,

\[
\mathcal L_f(c)=-f(c)f''(c).
\]

Moreover

\[
\iota_c
=
\operatorname{sgn}{f''(c)\over f(c)}.
\]

Thus an upward extra extremum is exactly a derivative zero with

\[
\mathcal L_f(c)<0.
\]

If `E_I(f)` counts those points, then

\[
\boxed{
N_I(f)
=
N_I(f')-2E_I(f)+\varepsilon_I(f).
}
\tag{L-107100.6}
\]

In particular,

\[
\boxed{
N_I(f)\ge N_I(f')-2E_I(f)-1.
}
\tag{L-107100.7}
\]

The coefficient `2` is sharp. A wrong-sign extremum adds an upward derivative crossing and forces a compensating downward crossing before the next parent zero or endpoint.

## Scope

This theorem completes the programme’s purely real-variable target. It neither bounds the defect nor supplies an Xi-specific descent estimate. It is valid with arbitrary parent-zero multiplicities and arbitrary derivative-zero multiplicities.