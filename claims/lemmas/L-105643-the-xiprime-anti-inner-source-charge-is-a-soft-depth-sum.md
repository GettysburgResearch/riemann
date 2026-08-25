# L-105643 — The Xi-prime anti-inner source charge is a soft depth sum

Claim ID: `L-105643`  
Status: **PROVED EXACT AT FINITE REGULAR WINDOW SCOPE; COFINAL INDEX IDENTIFICATION OPEN**  
Created: 2026-08-25  
Depends on: `L-105641--L-105642`; `L-105627--L-105632`  
RH status: **not assumed**

## 1. Shifted derivative and its upper zero packet

Let

\[
\beta_1
=\sup\{\operatorname{Im}\rho:\Xi'(\rho)=0\}.
\]

Fix a total analytic height

\[
H>0
\]

and a physical microscope coefficient

\[
0<h\le H.
\]

The corresponding base is `b=H-h>=0`. Put

\[
D_H(z)=\Xi'(z+iH).
\]

In a finite regular window `|Re rho|<=T`, every zero

\[
\rho=\alpha+i\gamma,
\qquad
\gamma>H,
\]

produces an upper-half-plane zero

\[
b_\rho=\alpha+i(\gamma-H)
\]

of `D_H`. Let

\[
B_{H,T}(z)
=\prod_{\substack{\Xi'(\rho)=0\\
|\operatorname{Re}\rho|\le T\\
\operatorname{Im}\rho>H}}
B_{b_\rho}(z)^{m_\rho}
\tag{L-105643.1}
\]

be the corresponding finite Blaschke product, with multiplicity retained.
This is precisely the anti-inner denominator packet which first appears when
the shifted boundary descends below a zero of `Xi'`.

## 2. Canonical source metric

The current-normalized base-Xi profile at total height `H` and physical
coefficient `h` is

\[
r_{H,h}(\xi)={h\over H}R_H(\xi).
\]

`L-105641` gives the pointwise source bound

\[
\boxed{
0\le r_{H,h}(\xi)
\le {h\over H}e^{-H\xi}.
}
\tag{L-105643.2}

Therefore, on the finite model space of the anti-inner packet,

\[
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le
{h\over H}
\operatorname{tr}_{K_{B_{H,T}}}M_{e^{-H\xi}}.
\tag{L-105643.3}

## 3. Exact soft-depth bound

Applying `L-105642` to every shifted zero gives

\[
\boxed{
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le
{h\over H}
\sum_{\substack{\Xi'(\rho)=0\\
|\operatorname{Re}\rho|\le T\\
\operatorname{Im}\rho>H}}
{2(\operatorname{Im}\rho-H)
 \over
 H+2(\operatorname{Im}\rho-H)}.
}
\tag{L-105643.4}

In particular,

\[
\boxed{
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le
{2h\over H^2}
\sum_{\substack{\Xi'(\rho)=0\\
|\operatorname{Re}\rho|\le T\\
\operatorname{Im}\rho>H}}
(\operatorname{Im}\rho-H).
}
\tag{L-105643.5}

Define the upper-depth counting function

\[
N_1(T;t)
=
\#\{\rho:\Xi'(\rho)=0,
 |\operatorname{Re}\rho|\le T,
 \operatorname{Im}\rho>t\},
\]

with multiplicity. Layer cake gives

\[
\boxed{
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le
{2h\over H^2}
\int_H^{\beta_1}N_1(T;t)\,dt.
}
\tag{L-105643.6]

The upper limit may be replaced by infinity; the integrand vanishes above
`beta_1`.

## 4. A vanishing collar is source-cheap

Assume `beta_1>0` and put

\[
H=\beta_1-\delta,
\qquad
0<\delta\le\beta_1/2.
\]

Since `h<=H` and `N_1(T;t)<=N_1(T;H)`, (L-105643.6) gives

\[
\boxed{
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le
{4\delta\over\beta_1}
N_1(T;H).
}
\tag{L-105643.7]

Thus a collar of relative thickness `delta/beta_1` consumes at most that same
order of the canonical current source dimension.

For any cofinal window family in which

\[
N_1(T;H)=O(N(T))
\]

uniformly in the collar, choosing `delta=delta_T->0` gives

\[
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
=o(N(T)).
\tag{L-105643.8}

The standard order-one zero-count ledger supplies the displayed growth
comparison once the exact window conventions are fixed. Equation
(L-105643.8) is a source-charge statement, not a zero-exclusion theorem.

If `beta_1=0`, no positive-height anti-inner collar exists and this particular
obstruction is absent.

## 5. What this changes

The first failure below the safe region is no longer an unpriced family of
upper derivative zeros. In the actual current metric it is a soft vertical
moment:

```text
raw count:       one unit per Xi-prime zero;
source charge:   approximately 2h(depth)/H^2 near the boundary.
```

Every fixed-depth packet has a fixed positive current charge. Only a packet
whose depths collapse to zero can become source-cheap. This matches the
zero-height/spatial-escape geometry of `T-105446` and the confluent
Paley--Wiener ledgers on sibling PR #731.

## 6. Refined descent target

The remaining descent theorem can therefore be localized to:

```text
BCOLLAR105643 — boundary-collar index conversion

Convert the small current-weighted charge of the Xi-prime anti-inner collar
into a favorable signed all-pass index or a pointwise two-trace inequality,
retaining common zeros and the single cofinal endpoint ledger.
```

All derivative zeros a fixed distance above the boundary are already paid by
(L-105643.4)--(L-105643.6). The only unresolved anti-inner geometry is the
microscopic boundary collar.

## 7. Scope

A boundary-near Blaschke factor has topological degree one even when its
current-weighted charge tends to zero. Hence this theorem does not prove
`BCOLLAR105643`, `POINTID105630`, `SAFEDESC105628`, or RH. The exact separator
is recorded in `R-105640`.