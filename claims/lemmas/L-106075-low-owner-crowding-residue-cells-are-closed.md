# L-106075 — Low owner-crowding residue cells are closed at the scale-matched conductor

Claim ID: `L-106075`  
Programme aliases: `LFAM1.OWNER_CROWDING_CRITERION`, `STRESS.RESIDUE_CELL_MULTIPLICITY`, `LFAM2.LOW_CROWDING_CLOSURE`  
Status: **PROVED UNCONDITIONAL MULTIPLICITY CRITERION AND SECTOR CLOSURE**  
Created: 2026-08-25  
Depends on: `L-106070--L-106074`; parent `L-102883`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Retain one block-colour packet and the notation of `L-106074`.  For a physical
residue \(r\ne0\), define its active owner crowding

\[
\boxed{
\nu_r
=
\#\left\{
P:\ \exists c\in[B,8B)
\text{ with }Z_{P,c}\ne0,
\ Pc^2\equiv r\pmod\ell
\right\}.
}
\tag{L-106075.1}
\]

## 1. At most two cores per owner and residue

For fixed \(P\) and \(r\), the congruence is

\[
c^2\equiv rP^{-1}\pmod\ell.
\]

It has at most two residue roots.  Since \([B,8B)\) has length less than
\(\ell\), each root has at most one lift to the declared block.  Hence every
owner contributes at most two physical core cells to one residue.

Therefore, writing

\[
A_r=\sum_{Pc^2\equiv r}Z_{P,c},
\]

Hilbert-space Cauchy gives

\[
\boxed{
\|A_r\|^2
\le
2\nu_r
\sum_{Pc^2\equiv r}
\|Z_{P,c}\|^2.
}
\tag{L-106075.2}
\]

This is quadratic and homogeneous in the source.

## 2. Low-crowding closure

Let \(K\ge1\) and let

\[
\mathcal R_{\le K}
=\{r:\nu_r\le K\}.
\]

Summing (L-106075.2) over these residues yields

\[
\boxed{
\sum_{r\in\mathcal R_{\le K}}
\|A_r\|^2
\le
2K
\sum_{P,c}\|Z_{P,c}\|^2.
}
\tag{L-106075.3}
\]

The block energy of `L-106074.8` and \(\ell\asymp B\) therefore imply

\[
\boxed{
\ell
\int_{I_X}
\sum_{r\in\mathcal R_{\le K}}
\|A_r(t)\|^2\frac{dt}{t}
\ll
K X^{o(1)}.
}
\tag{L-106075.4}
\]

In particular every block-colour sector with

\[
\max_r\nu_r=X^{o(1)}
\]

satisfies `QORO106074` unconditionally.

## 3. Exact high-crowding remainder

For the complementary cells put

\[
\mathcal Q_{>K}
=
\sum_{r:\nu_r>K}
\|A_r\|^2.
\tag{L-106075.5}
\]

Then

\[
\boxed{
\mathcal Q_{\mathcal B,A}
=
\mathcal Q_{\le K}
+
\mathcal Q_{>K},
}
\tag{L-106075.6}
\]

and the first term is closed by (L-106075.4).  Thus one may take
\(K=X^{o(1)}\) and restrict the live theorem to cells containing a genuinely
power-sized coherent family of different owner packets.

The partial-matching result of `L-106071` says that this crowding cannot come
from repeated cores for one fixed owner pair.  It is entirely an owner
occupancy phenomenon.

## 4. Relation to global physical occupancy

The map

\[
(P,c)\longmapsto Pc^2\pmod\ell
\]

is a finite residue model of the physical product observation.  High-crowding
cells are exactly the finite-field shadow of the global embedding norm
`BPOE103300`: many source-orthogonal owner packets become coherent after their
arithmetic labels are physically identified.

A source-blind divisor count cannot close (L-106075.5), because the vectors in
one cell may be parallel.  A valid proof must exploit the retained
owner phases, the Möbius/Vaughan signs, the Kummer character-square channels,
or an equivalent positive physical-observation theorem.

## Exact boundary

```text
at most two cores per fixed owner/residue        PROVED EXACT
quadratic crowding inequality                    PROVED EXACT
all X^(o(1))-crowding cells                      PROVED SUBPOWER
high owner-crowding cells                        OPEN / RH-BEARING
quartic pair-tensor substitute                   REFUTED BY R-106071
```

This theorem is a strict narrowing of `QORO106074`, not a proof of the remaining
high-crowding owner assembly.