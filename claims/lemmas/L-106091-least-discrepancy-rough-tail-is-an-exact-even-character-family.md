# L-106091 — A least-discrepancy rough tail is an exact even-character L-family

Claim ID: `L-106091`  
Programme aliases: `LFAM1.ROUGH_TAIL_EVEN_FAMILY`, `LFAM2.KUMMER_GAUSS_FIRST_DIFFERENCE`, `STRESS.LEAST_PRIME_FAMILY_FRAME`  
Status: **PROVED EXACT HILBERT-VALUED GAUSS/CHARACTER NORMAL FORM**  
Created: 2026-08-25  
Depends on: `L-106020`, `L-106090`; parent `L-102956--L-102959`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix one least-discrepancy anchor from `L-106090`, with conductor
\(\ell\).  Freeze the common square core \(g\), the opposite semiprime owner
product \(Q\), one physical shell and every source-incidence mask.  The
opposite reduced core is squarefree and \(\ell\)-rough:

\[
P^-(d)>\ell,\qquad(d,\ell gQ)=1.
\tag{L-106091.1}
\]

Let \(H\) be the physical logarithmic-observation Hilbert space and let
\(z_d\in H\) be any finitely supported packet satisfying the masks in
(L-106091.1).  Put

\[
u\equiv Qg^2\pmod\ell,\qquad u\in\mathbf F_\ell^\times,
\]

and

\[
F_h=\sum_d z_d\,e_\ell(-hu d^2),
\qquad 0\le h<\ell.
\tag{L-106091.2}
\]

For every even multiplicative character \(\eta\bmod\ell\), define

\[
M_\eta=\sum_d z_d\,\eta(d).
\tag{L-106091.3}
\]

Repeated residues are aggregated before the transform.

## 1. Exact Gauss transform

Let \(\chi\) range over all multiplicative characters of
\(\mathbf F_\ell^\times\), and put

\[
\tau(\chi)=\sum_{x\in\mathbf F_\ell^\times}\chi(x)e_\ell(x).
\]

For \(h\ne0\), multiplicative Fourier inversion gives

\[
\boxed{
F_h=
\frac1{\ell-1}
\sum_\chi
\tau(\overline\chi)\,
\chi(-hu)\,
M_{\chi^2}.
}
\tag{L-106091.4}
\]

Thus the least-discrepancy additive phase is already an exact moment of the
complete even character family modulo \(\ell\).  The square map on the
character group has kernel \(\{1,\kappa_\ell\}\).

## 2. Exact positive family identity

Orthogonality in \(h\), the principal Gauss sum \(\tau(1)=-1\), and
\(|\tau(\chi)|^2=\ell\) for nonprincipal \(\chi\) yield

\[
\boxed{
\sum_{h=1}^{\ell-1}\|F_h\|^2
=
\frac{\ell+1}{\ell-1}\|F_0\|^2
+
\frac{2\ell}{\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
\|M_\eta\|^2.
}
\tag{L-106091.5}
\]

In particular,

\[
\boxed{
\|F_0\|^2
\le
\frac{\ell-1}{\ell+1}
\sum_{h=1}^{\ell-1}\|F_h\|^2.
}
\tag{L-106091.6}
\]

The strict local principal leverage has no factor \(\ell\).

## 3. Arithmetic meaning

The untwisted term \(F_0\) is the literal opposite rough tail occurring in
(L-106090.10).  The nonprincipal terms are genuine even Dirichlet-character
channels.  Their coefficients retain:

```text
the universal Boolean balanced coefficient;
the p-rough cutoff P^-(d)>p;
the common-core and anchor-coprimality Euler exclusions;
the opposite owner product;
the fixed physical shell and common-mother observation.
```

At finite source scope this is an exact Dirichlet-polynomial family.  Under
the Mellin realization of `T-106030`, its members are projected
mollified-reciprocal-L defects with the primes at most \(\ell\) and the
anchor primes removed.

No ramified completion is needed at the conductor: (L-106091.1) gives
\(\ell\nmid Qgd\) coefficientwise.

## 4. Function-field mirror

Over \(\mathbf F_q[T]\), replace \(\ell\) by the least discrepancy
irreducible \(\mathfrak l\).  The opposite reduced core is
\(\mathfrak l\)-rough, and (L-106091.4) is the finite Fourier transform between
an Artin--Schreier phase and the complete even Kummer family on
\((\mathbf F_q[T]/\mathfrak l)^\times\).

This identifies the exact geometric target for programme #737: the coherent
anchor-amplified moment of these rough-tail Kummer local systems, with
constant constituents and resonant strata removed explicitly.

## Scope

The identity is local in the anchor.  Summing it source-blindly over all
common cores, left reduced cores and owner pairs is not justified.  The local
analytic size is closed in `L-106092`; the remaining anchor amplification is
the conclusion-facing theorem in `T-106090`.
