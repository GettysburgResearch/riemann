# M-23401 — Minimal balanced Möbius-shell programme

Methodology ID: `M-23401`  
Title: Replace the broad signed-correlation lemma by one explicit fixed-ratio positive Gram and a source-specific balanced recurrence  
Status: **PROPOSED RESEARCH AND REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-23401`--`L-23404`, `T-23401`, `R-23401`; PR #165 terminal Euler closure; PR #158 exact Möbius decoder

## 1. Minimal target

Fix

\[
c=\frac23,
\qquad B=\log2.
\]

Put

\[
I(x)=M(x)-M(2x/3),
\qquad
Q(t)=e^{-t/2}I(e^t).
\]

The proof-facing scalar is

\[
\boxed{
E(J)=\int_J^{J+\log2}|Q(t)|^2dt.}
\tag{M-23401.1}

By `T-23401`,

\[
\boxed{
E(J)=e^{o(J)}\quad\Longrightarrow\quad RH.}
\tag{M-23401.2}

The exact finite arithmetic object is

\[
\boxed{
E(J)
=\sum_{m,n}\mu(m)\mu(n)K_J(m,n),}
\tag{M-23401.3}

where

\[
K_J(m,n)=
\int_J^{J+\log2}
 e^{-t}
 {\bf1}_{\{(2/3)e^t<m\le e^t\}}
 {\bf1}_{\{(2/3)e^t<n\le e^t\}}dt.
\]

The kernel is positive semidefinite and supported on the fixed factor-ratio range

\[
\frac23<{m\over n}<\frac32.
\]

No endpoint polynomial, omitted prime power, zero tail, or generic Farey vector remains.

## 2. Why this is smaller than `L-23002`

The earlier signed-correlation gate was stated simultaneously in prime, semiprime, Farey, and analytic-totient coordinates. The first-cell decoder showed that this broad statement already contains the full Mertens problem.

The present programme keeps only the actual coherent source:

```text
one fixed ratio,
one compact inverse-zeta window,
one positive finite Gram,
one normalized block energy.
```

A proof of (M-23401.2) is sufficient by itself. The larger Type-II hierarchy is now an optional method for proving this scalar bound, not part of the logical conclusion.

## 3. Exact nonlinear identities available

Two exact recurrences may be used before any absolute value.

### Divisor recurrence

\[
I(x)=-\sum_{k\ge2}I(x/k).
\tag{M-23401.4}

This routes every term to a lower physical scale but is not contractive after entrywise absolute values.

### Centered prime renewal

\[
\log x\,I(x)
+\sum_{a\le x}\Lambda(a)I(x/a)
=J(x),
\tag{M-23401.5}

where

\[
J(x)=\sum_{2x/3<n\le x}
 \mu(n)\log(x/n).
\]

Squaring (M-23401.5) before decomposing the convolution produces the reflected prime/Möbius Type-II channel. This is the preferred nonlinear input.

## 4. Terminal/free-variable sector

The exact high-order Heath--Brown source contains an exact Möbius slice by `L-15159`. PR #165 and `L-15160` prove that every packet with one genuinely macroscopic unrestricted integer variable is exponentially small after sufficiently high Euler smoothing.

`L-23404` then confines every unresolved packet to the top identity orders, where almost all output scale is carried by truncated Möbius variables.

Thus the terminal and one-free-variable sectors are not the final obstruction.

`R-23401` gives the physical reason: adding or deleting one prime factor leaves the narrow shell. Internal sign cancellation begins only in a balanced factor-ratio geometry.

## 5. The exact remaining theorem

A full proposal must prove a source-specific recurrence for the shell energy or an equivalent finite auxiliary system. A representative form is

\[
\boxed{
E(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
 1+
 \max_{u\le(1-\delta_K)J+C_K}E(u)
\right],}
\tag{M-23401.6}

for an unbounded sequence of orders `K`, with

\[
\boxed{
{\varepsilon_K\over\delta_K}\longrightarrow0.}
\tag{M-23401.7}

The tensor alternative is permitted if its weighted scale sum `kappa_K` satisfies

\[
\varepsilon_K/(1-\kappa_K)\to0.
\]

Every coefficient in (M-23401.6) must come from the actual signed Möbius/Heath--Brown packet. A generic operator theorem is forbidden.

## 6. Suggested top-order attack

Use the schedule from `L-23404`, for example

\[
\eta_K=K^{-1/2},
\qquad R_K=K^2.
\]

Then:

1. higher Euler summation closes every packet with unrestricted scale at least `eta_K J`;
2. the hard dictionary lies in the top `O(sqrt K)` identity orders;
3. those orders must be recombined exactly into the Möbius source;
4. apply a centered Selberg/dispersion identity only after this recombination;
5. route every nonresonant factor-ratio cell below scale `(1-delta_K)J`;
6. prove `epsilon_K=o(delta_K)`;
7. recover (M-23401.6).

The first-cell mutation is automatic because the target signal itself is the first cell.

## 7. Mandatory fail-closed checks

A proposed proof must reject or explicitly handle:

1. total variation before top-order signed recombination;
2. a one-prime pairing inside the shell;
3. a same-scale Type-I cycle;
4. a truncated variable mislabeled as an unrestricted terminal variable;
5. a factor-ratio destination above the declared contracted scale;
6. deletion of shell endpoints or transition rows;
7. a coefficient rate which does not vanish relative to the contraction reserve;
8. inference from finitely many block computations.

It must also reproduce the exact shell transform

\[
{1-(2/3)^s\over s\zeta(s)}
\]

and the first-cell Mertens increment.

## 8. Promotion threshold

A child PR becomes a full RH proof proposal only after it contains:

1. a complete proof of (M-23401.6) or another direct proof of `E(J)=e^{o(J)}`;
2. an exact theorem invoking `T-23401` to conclude RH;
3. a frozen dependency graph and quantifier audit;
4. the `X-23401` mutation suite;
5. no open `BTP`, `CP`, `STC`, or signed-correlation hypothesis.

## 9. Current status

```text
fixed-ratio shell transform and Gram       PROPOSED COMPLETE
RH equivalence of shell energy              PROPOSED COMPLETE TRANSFER
terminal/free-variable closure              PROPOSED COMPLETE ON SOURCE BRANCHES
hard-core top-order concentration           PROPOSED COMPLETE SCALE GEOMETRY
balanced Möbius shell recurrence            OPEN
Riemann Hypothesis                           NOT PROVED
```
