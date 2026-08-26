# L-106213 — Function-field nonprincipal half-source shells have square-root size

Claim ID: `L-106213`  
Programme aliases: `LFAM2.FF_HALF_SOURCE_SHELL`, `LFAM1.WITT_TOWER_FROBENIUS_BOUND`, `STRESS.NONPRINCIPAL_ROUGH_TRACE`  
Status: **PROVED UNCONDITIONAL FUNCTION-FIELD COEFFICIENT THEOREM**  
Created: 2026-08-26  
Depends on: `L-106212` and function-field RH for Dirichlet \(L\)-functions  
Programme issues: #737, #736, #743  
Number-field RH status: **not assumed; no transfer claimed**

Let \(A=\mathbf F_q[T]\), let \(\mathfrak l\) be irreducible, and let
\(\chi\) be a nonprincipal primitive character modulo \(\mathfrak l\).
Write

\[
L(u,\chi)=\prod_{j=1}^{r}(1-\alpha_ju),
\qquad
r\le\deg\mathfrak l-1,
\qquad
|\alpha_j|\le q^{1/2}.
\tag{L-106213.1}
\]

Let

\[
\mathscr H_\chi(u)=\sum_{n\ge0}H_{\chi,n}u^n
\]

be the half-source Euler product of `L-106212`.

## 1. The leading square-root factor

The \(m=1\) part of the Witt tower is

\[
L(u,\chi)^{-1/2}.
\]

Coefficientwise absolute majorization gives

\[
\left|[u^n]L(u,\chi)^{-1/2}\right|
\le
q^{n/2}
[u^n](1-u)^{-r/2}.
\tag{L-106213.2}
\]

Hence

\[
\left|[u^n]L(u,\chi)^{-1/2}\right|
\ll_{\chi,q}
q^{n/2}(n+1)^{r/2}.
\tag{L-106213.3}
\]

## 2. Higher tower levels

Every nonprincipal \(L(u^m,\chi^m)\) with \(m\ge2\) has its first possible
zero singularity at radius \(q^{-1/(2m)}>q^{-1/2}\).

A principal resonance at level \(m\ge2\) has its first pole at
\(q^{-1/m}\ge q^{-1/2}\), with equality only for the quadratic resonance
\(m=2\). In that case the relevant factor is, up to finite ramified factors,

\[
(1-qu^2)^{-1/8},
\]

whose degree-\(n\) coefficients are still
\(O(q^{n/2}(n+1))\).

Therefore all tower levels \(m\ge2\), after isolating the quadratic
\(m=2\) factor when present, form a power series analytic on a disk strictly
larger than \(|u|=q^{-1/2}\).

Combining this analytic remainder with (L-106213.3) proves

\[
\boxed{
|H_{\chi,n}|
\le
C_{\chi,q}
(n+1)^{r/2+2}q^{n/2}.
}
\tag{L-106213.4}
\]

At the physical half-source normalization \(|F|^{-1}=q^{-n}\),

\[
\boxed{
q^{-n}|H_{\chi,n}|
\le
C_{\chi,q}
(n+1)^{r/2+2}q^{-n/2}.
}
\tag{L-106213.5}
\]

Thus every complete nonprincipal half-source degree shell has Frobenius
square-root size. The principal channel remains of full Euler scale; the
quadratic channel has a deterministic square-degree resonance but no larger
exponent.

## 3. Fully rough stopped half-source

In the fully \(U\)-rough sector, `L-106210` expresses the stopped half-source
through the two states \(f_U(g)\) and \(h(g)\), while the reduced core has at
most three prime factors cofinally. Consequently every complete
nonprincipal fully rough shell is a finite linear combination of the
half-source coefficients in (L-106213.4), with polynomial shell and
conductor factors only.

## Scope

The theorem applies to complete degree shells. It does not transport
incomplete physical cutoffs, source-incidence masks, or the principal member,
and proves no number-field estimate or RH.
