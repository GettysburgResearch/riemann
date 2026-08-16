# T-96400 — Exact two-row prefix-state frontier for the prime-sieved route

Claim ID: `T-96400`  
Status: **UNCONDITIONAL REDUCTION + RH-BEARING PRODUCER OPEN**  
Created: 2026-08-17  
Inputs: `R-96400`, `L-96400`, `L-96401`  
RH status: **unproved**

## 1. The corrected producer target

Define `TRP23` to be the eventual pair of integer inequalities
\[
 \boxed{
 c_N(2)\ge0,\qquad c_N(3)\ge0
 \quad(N\ge N_0)
 }
\tag{T-96400.1}
\]
for some integer \(N_0\).

By the integer-knot theorem `L-96400`, `TRP23` is exactly equivalent to
eventual nonnegativity of the two real-endpoint rows.  By `L-96401`,
\[
 \boxed{\mathrm{TRP23}\Longrightarrow\mathrm{RH}.}
\tag{T-96400.2}
\]

The all-row initial-prime theorem of PR #537 is not needed.  Nor is positivity
of every finite Euler truncation.  The conclusion-producing arithmetic object
is only the pair of full Möbius Riesz states in (L-96400.2)--(L-96400.3).

## 2. Exact scalar forms

`TRP23` is the pair
\[
 \log N-F(N)+\sqrt2F(N/2)-\frac1{\sqrt3}F(N/3)\ge0,
\tag{T-96400.3}
\]
\[
 \frac13\log N-\frac13F(N)-\frac1{3\sqrt2}F(N/2)
 +\frac5{3\sqrt3}F(N/3)-\frac12F(N/4)\ge0,
\tag{T-96400.4}
\]
where
\[
 F(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}\log(x/n).
\]
They are also the exact four-state recurrence
\[
 (c_2,c_3,M_2,M_3)_{N+1}
\]
obtained from (L-96400.12)--(L-96400.13) and the sparse dictionaries
(L-96400.5)--(L-96400.6).

## 3. Disposition of the attempted completions

The original local `FRONTIER-CHAIN` cannot prove (T-96400.1): its fixed-product
residue may be negative at one knot.  The later global-shadow proposals also
do not prove it: they replace the actual \(P\)-rough store by an all-integer
block, and the exact \(P=30,p=5,u=2\) witness invalidates that capacity step.

Therefore the current verified chain is
```text
exact two-row Riesz state                         PROVED
all-real <-> integer-knot positivity              PROVED
fixed-row reciprocal-zeta transform               PROVED
rows 2 and 3 have no common open-half-plane zero  PROVED
TRP23 -> RH                                       PROVED
TRP23                                             OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```

## 4. Scientific boundary

This packet is deliberately not another nominal complete proof with a hidden
reservoir.  A complete unconditional successor must prove `TRP23` itself, or a
strictly weaker producer sufficient for the same two-row Landau argument.
Finite scans, an under-specified global queue, or an all-integer replacement
for the rough store do not meet that burden.
