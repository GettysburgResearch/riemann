# T-106060 — Two-phase collision lines reduce to quadratic root-residue occupancy

Claim ID: `T-106060`  
Programme aliases: `LFAM1.ROOT_RESIDUE_OCCUPANCY`, `LFAM2.ARTIN_SCHREIER_OCCUPANCY`, `STRESS.TWO_PHASE_LINE_FRONTIER`  
Status: **EXACT CONJUNCTIVE PHASE REDUCTION; QUADRATIC OCCUPANCY OPEN**  
Created: 2026-08-24  
Corrected: 2026-08-25  
Depends on: `L-106001`, `L-106060`; `R-106060--R-106071`; `T-106001`; `L-106074`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The auxiliary completed-family route reduces every surviving clean owner ratio
to one of two lines

\[
c=\pm\tau d\pmod\ell.
\]

One inherited linear phase is insufficient: `R-106060` exhibits an exact
`ell-1` loss.  Two source-exact phases together give the sharp contraction of
`L-106060`.

## 1. Exact line packet

For a fixed source-owned line packet, aggregate the **original linear source
amplitudes** with the same root residue into Hilbert vectors

\[
w_{\mathfrak a,d}(X),
\]

and put

\[
S_{\mathfrak a}(X)=\sum_{d\ne0}w_{\mathfrak a,d}(X),
\qquad
D_{\mathfrak a}(X)=
\sum_{d\ne0}\|w_{\mathfrak a,d}(X)\|^2.
\tag{T-106060.1}
\]

Both \(\|S_{\mathfrak a}\|^2\) and \(D_{\mathfrak a}\) are quadratic in the
linear source amplitudes.

After inserting the two nonzero phases on the same source occurrence,
`L-106060` gives

\[
\boxed{
\|S_{\mathfrak a}(X)\|^2
\le
(\ell-1)D_{\mathfrak a}(X),
}
\tag{T-106060.2}
\]

and the sharper phase-energy identity

\[
\boxed{
\|S_{\mathfrak a}\|^2
\le
\frac{\ell-1}{\ell^2-\ell-1}
\sum_{\alpha,\beta\ne0}
\|F_{\mathfrak a;\alpha,
\beta}\|^2.
}
\tag{T-106060.3}
\]

The phases are genuinely conjunctive and may not be placed on separate source
marginals.

## 2. Binding homogeneity firewall

A rank-one matched owner-pair tensor

\[
Z_{P,c(d)}\otimes\overline{Z_{Q,d}}
\]

is already quadratic in the source, so the sum of its squared norms is
quartic.  It is not the \(D_{\mathfrak a}\) in (T-106060.1).

`R-106071` proves that replacing the quadratic root-residue occupancy by that
quartic tensor quantity is impossible.  The first `T-106070` proposal is
retracted for exactly this reason.

## 3. Correct scale-matched realization

`L-106070--L-106071` add two valid facts:

```text
a disjoint linear block/colour partition has an unramified principal modulus;
for every fixed owner pair, each collision line is a partial matching of cores.
```

`L-106074` then identifies the complete quadratic block occupancy directly as

\[
\boxed{
\mathcal Q_{\mathcal B,A}(X)
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r\;({\rm mod}\ \ell)}
Z_{P,c}(X)
\right\|^2.
}
\tag{T-106060.4}
\]

This formula retains the coherent sum over all owners in one residue cell.  Its
diagonal and every subpower owner-crowding cell are closed by
`L-106074--L-106075`.  High-crowding owner cells remain open.

## 4. Correct occupancy theorem

The historical name `CROP106060` should now be read only in its quadratic
normalization.  The current precise version is `HQORO106071`:

```text
on the disjoint scale-matched block/colour partition, the logarithmic,
source-weighted sum of ell * Q_(B,A) over the remaining power-crowded owner
residue cells is Y^(o(1)).
```

Then

\[
\boxed{
\mathrm{HQORO}_{106071}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106060.5}

The premise remains open.

## 5. Function-field consequence

For an irreducible conductor of degree \(r\), the residue field has size
\(Q=q^r\).  On core degree shells below \(r\), reduction is injective and the
same two-phase frame applies.  The remaining geometric object is still the
quadratic coherent sum of distinct owner-irreducible packets in one residue
cell, not its quartic Hilbert--Schmidt shadow.

## Exact boundary

```text
one-phase collision-line control                 REFUTED
exact two-phase line energy                       PROVED EXACT
sharp two-phase contraction                       PROVED EXACT
linear block/colour unramified palette             PROVED EXACT
fixed-owner-pair core matching                     PROVED EXACT
quartic substitute for quadratic occupancy         REFUTED
quadratic residue Gram normal form                 PROVED EXACT
low owner-crowding cells                           PROVED
HQORO106071 high-crowding owner assembly            OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
