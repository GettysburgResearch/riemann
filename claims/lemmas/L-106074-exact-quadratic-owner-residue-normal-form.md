# L-106074 — The scale-matched character family has an exact quadratic owner-residue normal form

Claim ID: `L-106074`  
Programme aliases: `LFAM1.QUADRATIC_OWNER_RESIDUES`, `STRESS.PHYSICAL_RESIDUE_GRAM`, `LFAM2.BLOCK_CHARACTER_PARSEVAL`  
Status: **PROVED EXACT FAMILY-MOMENT NORMAL FORM**  
Created: 2026-08-25  
Depends on: `L-106001`, `L-106070--L-106071`; `R-106071`; parent `L-102883`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix one block-colour piece \((\mathcal B,A)\) from `L-106070`, with core
scale \(B\), colour-safe prime \(16B<\ell<256B\), and complete
Hilbert-valued source atoms

\[
Z_{P,c}(X),
\qquad c\in[B,8B),
\qquad \ell\nmid Pc.
\]

Equal literal representations of one physical core have already been
aggregated as in `L-106071.5`.  All carrier, marked-prime, gauge and shell
labels remain in the Hilbert coordinate.

## 1. Exact residue Gram decomposition

For \(r\in\mathbf F_\ell^*\), define

\[
\boxed{
A_r(X)
=
\sum_{\substack{P,c\\Pc^2\equiv r\;({\rm mod}\ \ell)}}
Z_{P,c}(X).
}
\tag{L-106074.1}
\]

For a Dirichlet character modulo \(\ell\), put

\[
V_\chi(X)
=
\sum_{P,c}\chi(Pc^2)Z_{P,c}(X).
\tag{L-106074.2}
\]

Complete character orthogonality gives the Hilbert-valued Parseval identity

\[
\boxed{
\frac1{\ell-1}
\sum_{\chi\;({\rm mod}\ \ell)}
\|V_\chi(X)\|^2
=
\sum_{r\ne0}\|A_r(X)\|^2.
}
\tag{L-106074.3}
\]

Denote the right side by

\[
\boxed{
\mathcal Q_{\mathcal B,A}(X)
:=
\sum_{r\ne0}\|A_r(X)\|^2.
}
\tag{L-106074.4}
\]

This is the exact quadratic owner-residue occupancy.  It is homogeneous of
degree two in the source and is the only residue quantity that can control the
character family moment.

Because the principal character is literally the native coloured block,

\[
V_{\chi_0}(X)=R_{\mathcal B,A}(X),
\]

so

\[
\boxed{
\|R_{\mathcal B,A}(X)\|^2
\le
(\ell-1)\mathcal Q_{\mathcal B,A}(X).
}
\tag{L-106074.5}
\]

## 2. Diagonal cost is already paid

Expanding (L-106074.4) gives

\[
\mathcal Q_{\mathcal B,A}
=
\mathcal E_{\mathcal B,A}
+
\mathcal C_{\mathcal B,A},
\tag{L-106074.6}
\]

where

\[
\mathcal E_{\mathcal B,A}
=
\sum_{P,c}\|Z_{P,c}\|^2
\tag{L-106074.7}
\]

is the exact diagonal and \(\mathcal C\) is the real off-diagonal congruence
correlation.

The retained stopped-Vaughan block energy and representation collapse give

\[
\mathcal E_{\mathcal B,A}(X)
\ll
\frac{X^{o(1)}}B
\sum_{P\in\mathcal O_{\mathcal B,A}}\frac1P.
\tag{L-106074.8}
\]

Since \(\ell<256B\),

\[
\boxed{
\ell\,\mathcal E_{\mathcal B,A}(X)
\ll
X^{o(1)}
\sum_P\frac1P
=X^{o(1)}.
}
\tag{L-106074.9}
\]

Thus the power-scale principal-character cost does not reopen the equal-product
diagonal.  The first version of `L-106073` was nevertheless invalid because
it attempted to pay the **off-diagonal** quadratic correlation by a quartic
pair-tensor quantity.

## 3. Partial matching normal form for the off-diagonal

For fixed owners \(P,Q\), `L-106071` proves that a surviving congruence is one
of at most two partial matchings

\[
c=c_{P,Q,\pm}(d).
\]

Consequently

\[
\boxed{
\mathcal C_{\mathcal B,A}(X)
=
\sum_{P,Q}
\sum_{\pm}
\sum_{d\in\mathcal L_{P,Q,\pm}}
\left\langle
Z_{P,c_{P,Q,\pm}(d)}(X),
Z_{Q,d}(X)
\right\rangle,
}
\tag{L-106074.10}
\]

with nonsquare owner ratios absent and the four marked-\(67\) sectors retained
separately.  Formula (L-106074.10) is quadratic.  It may not be replaced by

\[
\sum_{P,Q,d}
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2,
\]

which is quartic.

The scale-matched modulus has therefore removed all repeated-core occupancy
inside one fixed owner pair.  The only remaining coherence is the sum of
**different owner packets** landing in the same physical residue cell.

## 4. Exact conclusion-facing criterion

On a dyadic horizon \(I_X=[X,2X]\), define

```text
QORO106074:
  for the disjoint scale-matched block/colour partition,

    sum_(B,A) ell(B,A)
      integral_(I_X) Q_(B,A)(t) dt/t

  is X^(o(1)).
```

Then (L-106074.5), finite block-colour Cauchy and logarithmic
Cauchy--Schwarz give

\[
\boxed{
\mathrm{QORO}_{106074}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}.
}
\tag{L-106074.11}
\]

The diagonal part of `QORO106074` is proved by (L-106074.9).  Its remaining
content is the quadratic owner-coherence term (L-106074.10).

## Scope

This theorem supplies the corrected exact normal form after the failed
quartic adapter.  It proves neither the owner-coherence estimate nor RH.  A
sharp sufficient criterion and the low-crowding sector are proved in
`L-106075`; the global frontier is stated in `T-106071`.