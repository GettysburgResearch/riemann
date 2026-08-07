# L-23003 — The first critical Farey cell is an exact Mertens increment

Claim ID: `L-23003`  
Title: The first nonzero reduced-Farey cluster in the analytic-totient packet is a fixed complex multiple of `M(D)-M(2D/3)`  
Status: **PROPOSED — COMPLETE FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: the reduced-Farey coefficient formula of PR #231 (`L-22801`)  
Scope: every integer `D>=2`

## 1. Reduced-Farey coefficients

Use the completed analytic-totient packet

\[
S_D(x)=\sum_{d\le D}\mu(d)\left(\{x/d\}^2-\frac13\right)
\]

and write each nonzero frequency in reduced form as `a/q`, with `q>=1`,
`a in Z\{0}`, and `(a,q)=1`.  The exact coefficient is

\[
\boxed{
 b_D(a/q)
 =\frac{iq}{2\pi a}U_q(D)
 +\frac{q^2}{2\pi^2a^2}V_q(D),
}
\tag{L-23003.1}
\]

where

\[
 U_q(D)=\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}d,
 \qquad
 V_q(D)=\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}{d^2}.
\tag{L-23003.2}
\]

For the critical frequency partition, put

\[
 I_{D,k}=\left[\frac{k-1/2}{D},\frac{k+1/2}{D}\right)
\]

and

\[
 B_{D,k}=\sum_{a/q\in I_{D,k}}b_D(a/q).
\tag{L-23003.3}
\]

## 2. Exact description of the first positive cell

For `k=1`,

\[
 I_{D,1}=\left[\frac1{2D},\frac3{2D}\right).
\]

Suppose `a/q` lies in this cell and `q<=D`.

If `a>=2`, then

\[
 \frac aq<\frac3{2D}
 \quad\Longrightarrow\quad
 q>\frac{2aD}{3}\ge\frac{4D}{3},
\]

contradicting `q<=D`.  Thus necessarily

\[
 a=1.
\]

The two cell inequalities then give

\[
 \frac{2D}{3}<q\le D.
\tag{L-23003.4}
\]

Conversely every reduced fraction `1/q` in this range belongs to `I_(D,1)`.
Therefore

\[
\boxed{
 I_{D,1}\cap\{a/q:q\le D\}
 =\left\{\frac1q:\frac{2D}{3}<q\le D\right\}.
}
\tag{L-23003.5}
\]

## 3. The divisor coordinates collapse

For every `q>D/2`, the only multiple of `q` not exceeding `D` is `q` itself.
Hence on the range (L-23003.4),

\[
 U_q(D)=\frac{\mu(q)}q,
 \qquad
 V_q(D)=\frac{\mu(q)}{q^2}.
\tag{L-23003.6}
\]

Substitution into (L-23003.1) gives

\[
\boxed{
 b_D(1/q)
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)\mu(q).
}
\tag{L-23003.7}
\]

Let

\[
 M(x)=\sum_{n\le x}\mu(n).
\]

Summing (L-23003.7) over the complete first cell yields the exact identity

\[
\boxed{
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 \left[M(D)-M(2D/3)\right].
}
\tag{L-23003.8}
\]

With integer endpoints, `M(2D/3)` means `M(floor(2D/3))`.
The negative cell is its complex conjugate because `S_D` is real.

Consequently,

\[
\boxed{
 |B_{D,1}|^2
 =\left(\frac1{4\pi^2}+\frac1{4\pi^4}\right)
 \left|M(D)-M(2D/3)\right|^2.
}
\tag{L-23003.9
\]

## 4. Critical-scale consequence

A bound

\[
 |B_{D,1}|\ll_\varepsilon D^{1/2+\varepsilon}
\tag{L-23003.10}
\]

for every `epsilon>0` is equivalent, by (L-23003.8), to

\[
 M(D)-M(2D/3)=O_\varepsilon(D^{1/2+\varepsilon}).
\tag{L-23003.11}
\]

Iterating the fixed-ratio decomposition

\[
 M(D)=M((2/3)^JD)
 +\sum_{j=0}^{J-1}
 \left[
  M((2/3)^jD)-M((2/3)^{j+1}D)
 \right]
\]

and letting `J` terminate at bounded scale gives

\[
 M(D)=O_\varepsilon(D^{1/2+\varepsilon}).
\tag{L-23003.12}
\]

The classical Mertens criterion then gives RH.

Thus the first critical cell alone already carries the full square-root
Möbius-cancellation burden.

## 5. Consequence for `L-23002`

This exact decoder has two uses.

First, it prevents a false simplification.  A proof of the signed critical
correlation lemma cannot arise from a generic bounded operator estimate that
ignores the actual Möbius vector: the first cell contains a coherent sum with
no internal oscillatory phase at all.

Second, it identifies the correct positive target.  The completed endpoint
channel and adjacent cells may redistribute this coherent mode inside the
physical local-energy form, but any valid scalar proof must still produce the
square-root cancellation in (L-23003.11), either explicitly or through an
exact coupled identity.

In particular, the following are not substitutes:

- an entrywise absolute-value bound;
- a uniform cluster-operator norm bound;
- deletion of finitely many low cells;
- the full-period Bohr/Jordan square without critical local transference;
- a finite numerical ladder.

## 6. Proof boundary

- Equations (L-23003.5)--(L-23003.9) are finite algebra.
- The telescoping implication (L-23003.11) => (L-23003.12) is elementary.
- No estimate of the Mertens increment is proved here.
- The completed endpoint polynomial can couple to the first cell under a
  non-translation-invariant localizing weight; this lemma does not discard that
  coupling or assert an isolated lower bound for the physical local energy.
- RH remains unproved.
