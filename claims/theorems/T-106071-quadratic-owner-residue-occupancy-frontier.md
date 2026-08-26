# T-106071 — Quadratic owner-residue occupancy is the corrected scale-matched frontier

Claim ID: `T-106071`  
Programme aliases: `LFAM1.QUADRATIC_OWNER_RESIDUE_FRONTIER`, `STRESS.HIGH_CROWDING_PHYSICAL_OCCUPANCY`, `LFAM2.RESIDUE_GRAM_ASSEMBLY`  
Status: **EXACT CORRECTED REDUCTION; HIGH-CROWDING OWNER ASSEMBLY OPEN**  
Created: 2026-08-25  
Depends on: `R-106071`; `L-106070--L-106075`; `T-106060`; parent `HBCQDSP102888`; `BPOE103300`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The self-audit of the first `T-106070` proposal found an exact homogeneity
failure.  Its block palette and line-injectivity geometry remain valid, but a
quartic owner-pair tensor norm cannot control the quadratic character-family
moment.  `R-106071` is binding.

## 1. Exact scale-matched source geometry

For every stopped-Vaughan core block \(c\in[B,8B)\), `L-106070` gives a
disjoint linear owner-colour partition and a prime

\[
16B<\ell<256B,
\qquad \ell\ne67,
\]

which divides no physical index in the colour.  The principal character is
therefore literally the native coloured source.

For each fixed owner pair, `L-106071` converts every surviving character
collision into at most two partial matchings

\[
c\equiv\pm\tau d\pmod\ell.
\]

This removes all repeated-core occupancy inside one owner pair.

## 2. The correct quadratic object

For the complete Hilbert-valued source atoms \(Z_{P,c}(X)\), define

\[
A_r(X)
=
\sum_{Pc^2\equiv r\;({\rm mod}\ \ell)}Z_{P,c}(X)
\]

and

\[
\boxed{
\mathcal Q_{\mathcal B,A}(X)
=
\sum_{r\ne0}\|A_r(X)\|^2.
}
\tag{T-106071.1}
\]

Exact character Parseval gives

\[
\frac1{\ell-1}
\sum_\chi\|V_\chi(X)\|^2
=
\mathcal Q_{\mathcal B,A}(X),
\]

while principal inclusion gives

\[
\|R_{\mathcal B,A}(X)\|^2
\le
(\ell-1)\mathcal Q_{\mathcal B,A}(X).
\tag{T-106071.2}
\]

The diagonal contribution to \(\ell\mathcal Q\) is already subpower because
the exact block energy is \(X^{o(1)}/(PB)\) and \(\ell\asymp B\).

## 3. Closed and open residue cells

Let \(\nu_r\) be the number of distinct owner packets represented in residue
cell \(r\).  `L-106075` proves

\[
\|A_r\|^2
\le
2\nu_r
\sum_{Pc^2\equiv r}\|Z_{P,c}\|^2.
\]

Hence every cell with \(\nu_r=X^{o(1)}\) is closed at subpower cost.  The
remaining packet consists only of cells containing power-sized coherent
families of different owners.

Define

```text
HQORO106071:
  after the complete carrier/Wick/HBC source construction and the disjoint
  scale-matched block-colour partition, the source-weighted logarithmic sum

      sum_(block,color) ell
        integral sum_(r: nu_r > X^(o(1))) ||A_r(X)||^2 dX/X

  is Y^(o(1)), with all marked-67, phase, gauge, shell and overlap labels
  retained exactly once.
```

Equivalently, one may state the full quadratic estimate `QORO106074`; its
diagonal and low-crowding parts are already proved.

## 4. Exact implication graph

By `L-106074`,

\[
\boxed{
\mathrm{HQORO}_{106071}
\Longrightarrow
\mathrm{QORO}_{106074}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106071.3}

The last implication is the frozen parent detector/Mellin consumer.  The first
premise remains open.

## 5. Identification with the common occupancy frontier

The high-crowding residue cell is not a new independent obstruction.  It is a
finite-field block coordinate for the physical observation map of
`BPOE103300`:

```text
source-orthogonal labels:
  different semiprime owners and core histories;

finite residue observation:
  (P,c) -> P c^2 mod ell;

physical observation:
  (P,c) -> the integer product P c^2 and its compact translate.
```

The scale-matched theorem proves that core multiplicity and conductor
normalization are not the obstruction.  What remains is coherent physical
aggregation of many owner packets in the same observation cell.

## 6. Correct status of the attempted closure

```text
R-106070 source-order firewall                  VALID
L-106070 linear prime palette                   PROVED EXACT
L-106071 partial-matching core geometry         PROVED EXACT
L-106072 quartic pair-tensor payment             PROVED BUT NON-CONCLUSION-FACING
first L-106073 quartic-to-quadratic adapter       RETRACTED
first T-106070 full RH composition               RETRACTED
R-106071 homogeneity counterexample              PROVED EXACT
L-106074 quadratic residue normal form           PROVED EXACT
L-106075 low owner-crowding cells                PROVED
HQORO106071 high-crowding owner assembly         OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```

The draft PR must retain this corrected status until the quadratic
high-crowding theorem, rather than its quartic shadow, is proved.