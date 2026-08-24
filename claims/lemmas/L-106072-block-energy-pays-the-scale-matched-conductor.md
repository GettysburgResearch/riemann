# L-106072 — The stopped-Vaughan block energy pays the conductor for the quartic matched-pair tensor

Claim ID: `L-106072`  
Programme aliases: `LFAM1.QUARTIC_CONDUCTOR_PAYMENT`, `STRESS.PAIR_TENSOR_BUDGET`, `LFAM2.HILBERT_SCHMIDT_SHADOW`  
Status: **PROVED UNCONDITIONAL QUARTIC TENSOR BOUND; NOT A QUADRATIC FAMILY-MOMENT BOUND**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106070--L-106071`; `R-106070--R-106071`; parent `L-102880`, `L-102883`, `L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Retain one block-colour piece \((\mathcal B,A)\), with

\[
B=UVM,
\qquad
16B<\ell=\ell(B,A)<256B.
\]

All estimates below are uniform in the colour, marked-\(67\) sector, fixed
carrier/gauge labels and dyadic physical horizon.

## 1. Load-bearing quadratic source energy

For one owner squareclass \(P=pq\), a balanced stopped-Vaughan atom has
coefficient

\[
\frac{1}{\sqrt P}
\frac{a_U(u)a_U(v)\mu(m)}{uvm},
\qquad
u\asymp U,\quad v\asymp V,\quad m\asymp M,
\]

where the first variable is the ordinary variable \(u\asymp U\).
Using

\[
|a_U(n)|\le\tau(n),
\qquad
\sum_{n\sim N}\frac{\tau(n)^2}{n^2}
\ll\frac{\log^3(2N)}N,
\]

and the bounded fixed-kernel translate gives

\[
\boxed{
E^{\rm free}_{P,\mathcal B}
:=
\sum_{u,v,m}\|z_{P;u,v,m}\|^2
\ll
\frac{(\log(2X))^{O(1)}}{P B}.
}
\tag{L-106072.1}
\]

After equal-core representation aggregation,

\[
\boxed{
E_{P,\mathcal B}
:=
\sum_c\|Z_{P,c}\|^2
\ll
\frac{X^{o(1)}}{P B}.
}
\tag{L-106072.2}
\]

This quadratic estimate remains conclusion-facing and, by itself, pays the
power-scale conductor on the diagonal:

\[
\ell\sum_P E_{P,\mathcal B}=X^{o(1)}.
\tag{L-106072.3}
\]

## 2. Quartic matched-pair tensor

For a fixed owner pair and either partial-matching line, put

\[
D^{(4)}_{P,Q,\pm}
=
\sum_d
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2.
\tag{L-106072.4}
\]

`L-106071.8` gives

\[
D^{(4)}_{P,Q,\pm}
\le E_{P,\mathcal B}E_{Q,\mathcal B},
\]

and therefore

\[
\boxed{
D^{(4)}_{P,Q,+}+D^{(4)}_{P,Q,-}
\ll
\frac{X^{o(1)}}{P Q B^2}.
}
\tag{L-106072.5}
\]

Multiplying by the scale-matched conductor and summing owners yields

\[
\boxed{
\ell
\sum_{P,Q,\pm}D^{(4)}_{P,Q,\pm}
\ll
\frac{X^{o(1)}}B
\left(\sum_P\frac1P\right)^2
=X^{o(1)}.
}
\tag{L-106072.6}
\]

All block, colour, marked-prime, line, carrier and common-square labels add
only fixed or subpower cost.  Thus the complete quartic matched-pair tensor is
indeed conductor-paid.

## 3. Homogeneity firewall

The quantity in (L-106072.6) is homogeneous of degree four in the source atoms.
The character-family moment

\[
\sum_r
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2
\]

is homogeneous of degree two.  `R-106071` proves that no source-independent
inequality can replace the latter by the former.

Consequently (L-106072.6) does **not** prove `CROP106060`, `QORO106074`,
`HBCQDSP102888`, or RH.  The first version of this file incorrectly identified
its quartic tensor as the required root-residue occupancy; that interpretation
is withdrawn.

## 4. Surviving uses

The theorem remains useful for:

```text
finite mutation checking of the matching geometry;
quartic/Hilbert--Schmidt observables;
showing that the scale-matched conductor itself is not expensive;
separating core multiplicity from owner coherence;
confirming that the diagonal quadratic energy is conductor-paid.
```

The conclusion-facing quadratic owner-residue Gram is stated in `L-106074`.
Its low-crowding sector is closed in `L-106075`, while the high-crowding owner
assembly remains open in `T-106071`.