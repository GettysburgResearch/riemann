# L-106022 — Opposite-owner phases are a source-paid even Dirichlet L-family

Claim ID: `L-106022`  
Programme aliases: `LFAM1.OWNER_CONDUCTOR_EVEN_FAMILY`, `STRESS.SOURCE_PAID_PRINCIPAL_LEVERAGE`  
Status: **PROVED EXACT SOURCE/FAMILY IDENTIFICATION**  
Created: 2026-08-24  
Depends on: `L-106020--L-106021`; PR #719 `L-102886--L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The auxiliary family of `L-106000` uses a conductor not already present in the
physical source and therefore needs a separate principal-leverage estimate.
The balanced owner packet contains a different family whose conductor is a
literal opposite owner prime and whose leverage is already paid by the source.

## 1. Even core characters

Fix a clean `N=P a^2` packet and an odd opposite owner prime `rho`, so
`rho` divides the other physical product and

\[
\rho\nmid Pa.
\]

For `chi (mod rho)`, the multiplicative transform of the square-phase field is

\[
\chi(Pa^2)=\chi(P)\eta(a),
\qquad
\eta=\chi^2.
\tag{L-106022.1}
\]

As `chi` ranges over all characters modulo `rho`, `eta` ranges over the even
characters

\[
\eta(-1)=1
\]

with multiplicity two. The two square roots of the principal even character
are the principal character and the quadratic character.

Thus `L-106020.5` is exactly the positive owner-conductor moment

\[
\boxed{
\sum_{h\ne0}\|F_h\|^2
={\rho+1\over\rho-1}\|F_{\eta=1}\|^2
+{2\rho\over\rho-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
\|F_\eta\|^2.
}
\tag{L-106022.2}
\]

The coefficient of the native untwisted field is larger than one. No amplifier
or auxiliary principal-extraction theorem is required at this local interface.

## 2. Twisted owner-excluded Vaughan identity

Fix the deterministic owner pair `P=pq` from `L-102887` and work on the monoid

\[
\mathbb N^{(p,q)}=\{n:(n,pq)=1\}.
\]

Let `eta` be any even character modulo an opposite owner `rho`, extended
multiplicatively on this clean monoid. Character twisting commutes with
Dirichlet convolution:

\[
((f*g)\eta)=(f\eta)*(g\eta).
\tag{L-106022.3}
\]

Therefore the blockwise fixed-cutoff identity of `L-102888` twists
coefficientwise:

\[
\boxed{
\mu^{(p,q)}\eta
=2\mu_U^{(p,q)}\eta
-(\mu_U^{(p,q)}\eta)*(\mu_U^{(p,q)}\eta)*(1^{(p,q)}\eta)
+(a_U^{(p,q)}\eta)*(a_U^{(p,q)}\eta)*(\mu^{(p,q)}\eta).
}
\tag{L-106022.4}
\]

No new Type-I or smooth-boundary row is introduced. The cutoff is fixed on the
dyadic block before the character transform.

On the squared core scale, the full reciprocal source has Dirichlet series

\[
\boxed{
\sum_{(n,pq)=1}{\mu(n)\eta(n)\over n^{2s}}
=
\prod_{\ell\nmid pq}(1-\eta(\ell)\ell^{-2s})
=
{L(2s,\eta)^{-1}
 \over
 (1-\eta(p)p^{-2s})(1-\eta(q)q^{-2s})}.
}
\tag{L-106022.5}
\]

The displayed finite denominators are zero-free for `Re(s)>0`. Hence every
nonprincipal even channel is a genuine reciprocal Dirichlet `L(2s,eta)` core
channel with two explicit owner Euler factors removed.

## 3. Principal leverage is source-paid

The additive owner phases in PR #719 carry the literal opposite-owner
normalization. Under the Gauss--Mellin change of basis, the nonprincipal Gauss
weight is `rho`, while the source supplies the corresponding `rho^(-1)` owner
energy weight. The principal/quadratic root fibre contributes the coefficient

\[
{\rho+1\over\rho-1}=1+O(\rho^{-1}),
\]

not `rho^(-1)`.

Thus the owner-conductor family has an exact local principal embedding. The
remaining difficulty is not individualizing one member of a free auxiliary
family; it is summing the source-coupled owner-conductor moments coherently over
different physical owner packets.

## 4. Exceptional root fibre

The quadratic root is not an independent core-oscillating channel:

\[
\chi=\kappa_\rho
\quad\Longrightarrow\quad
\chi^2=1.
\]

It is an exact copy of the untwisted core field, up to the owner sign
`kappa_rho(P)`. This is recorded as a binding firewall in `R-106020`.

## Scope

This theorem establishes a literal family of Dirichlet `L(2s,eta)` channels
inside the existing CV/XD phase packet and proves its local principal leverage.
It does not prove the coherent short-core family moment `SOCM106020` or RH.