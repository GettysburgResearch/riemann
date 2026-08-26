# T-106081 — Minimum-owner Boolean Vaughan corrected owner-occupancy frontier

Claim ID: `T-106081`  
Programme aliases: `LFAM1.MINIMUM_OWNER_SELECTOR_MOMENT`, `STRESS.LONG_CORE_OWNER_OCCUPANCY`, `LFAM2.BOOLEAN_KUMMER_ASSEMBLY_FRONTIER`  
Status: **EXACT CORRECTED REDUCTION; SOURCE-TIED OWNER ASSEMBLY OPEN**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106080--L-106081`; `R-106080`; parent `L-102880`, `L-102887--L-102888`; `T-106030`; `T-106071`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The self-reconstruction of `T-106080` retains the new Boolean source
coordinate and the minimum-owner geometry, but rejects the attempted direct
application of `L-102883`.

This theorem records the exact conclusion-facing object which remains.

## 1. Retained source reduction and the two horizon sectors

For each deterministic owner pair

\[
P_i=\lambda_i\Lambda_i,
\qquad
\lambda_i<\Lambda_i,
\]

the completed balanced source consists of atoms

\[
n_i=P_i a_i^2,
\qquad
\mu^2(a_i)=1,
\qquad
(a_i,P_i)=1,
\]

with coefficient

\[
\alpha_i
=
\frac{\gamma_i}{a_i\sqrt{\lambda_i\Lambda_i}},
\qquad
|\gamma_i|=X^{o(1)}.
\]

The Boolean balanced coefficient forces at least two distinct core primes.
The minimum-owner rule gives

\[
\boxed{\lambda_i^2\le a_i.}
\tag{T-106081.1}
\]

After the linear block projection

\[
B\le a_i<2B,
\qquad
L\le\lambda_i<2L,
\]

every nonempty block satisfies

\[
\boxed{L^2<2B.}
\tag{T-106081.2}
\]

The geometry is stronger after the exact two-way horizon partition.

### No exceptional label

If the occurrence has no label greater than \(4\sqrt Y\), the two owners are
the two smallest labels. Every core prime is therefore at least the co-owner
\(\Lambda_i\). Since the balanced core has at least two distinct primes,

\[
\boxed{\Lambda_i^2\le a_i,\qquad P_i=\lambda_i\Lambda_i\le a_i.}
\tag{T-106081.3}
\]

Thus the entire semiprime owner product is paid by the literal core in this
sector.

### Unique exceptional label

If an exceptional label occurs, it is the co-owner

\[
\Lambda_i>4\sqrt Y.
\]

The ratio-eight physical horizon has \(n_i\le16Y\), so

\[
\boxed{\lambda_i a_i^2<4\sqrt Y.}
\tag{T-106081.4}
\]

Combining this with (T-106081.1) gives the additional distinguished-owner
restriction

\[
\boxed{\lambda_i^5<4\sqrt Y.}
\tag{T-106081.5}
\]

The fixed-owner Boolean Type-I row is power-saving, and the parent terminal,
repeated-label, equal-product and finite-Euler rows remain closed. Equations
(T-106081.3)--(T-106081.5) are extra geometry for the remaining owner moment;
they do not by themselves control coherent owner aggregation.

## 2. Exact selector-tied phase packet

Let \(I_\ell\) denote the source atoms in the block whose distinguished owner
is \(\ell\), and put

\[
\beta_i=\ell\alpha_i
=
\frac{\gamma_i}{a_i}\sqrt{\frac{\ell}{\Lambda_i}}
\qquad(i\in I_\ell).
\tag{T-106081.6}
\]

For distinct phase owners \(\ell,\rho\), define

\[
\mathcal A_{\ell\to\rho;k}
=
\sum_{i\in I_\ell}
\beta_i e_\rho(k n_i)v_i,
\qquad 1\le k<\rho.
\tag{T-106081.7}
\]

Here \(v_i\) is the complete physical logarithmic-observation vector. All
co-owner, Boolean representation, carrier, shell, marked-prime and overlap
labels remain in \(v_i\); none is declared orthogonal after physical
observation.

The phase modulo \(\ell\) is constant on \(I_\ell\), because
\(\ell\mid n_i\). Expanding the two nonzero Ramanujan identities gives the
exact clean cross-owner Gram

\[
\boxed{
\mathcal G_{B,L}^{\rm clean}
=
\sum_{\substack{\ell,\rho\in\mathcal P_L\\\ell\ne\rho}}
\frac1{\ell\rho}
\sum_{h=1}^{\ell-1}
\sum_{k=1}^{\rho-1}
\left\langle
\mathcal A_{\ell\to\rho;k},
\mathcal A_{\rho\to\ell;h}
\right\rangle .
}
\tag{T-106081.8}
\]

For one ordered pair \((\ell,\rho)\), Cauchy gives

\[
\left|
\sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}
\left\langle
\mathcal A_{\ell\to\rho;k},
\mathcal A_{\rho\to\ell;h}
\right\rangle
\right|
\le
\left((\rho-1)\sum_{k=1}^{\rho-1}
\|\mathcal A_{\ell\to\rho;k}\|^2\right)^{1/2}
\left((\ell-1)\sum_{h=1}^{\ell-1}
\|\mathcal A_{\rho\to\ell;h}\|^2\right)^{1/2}.
\tag{T-106081.9}
\]

After multiplying by \(1/(\ell\rho)\), summing the ordered pairs and using
\(2uv\le u^2+v^2\), one obtains

\[
\boxed{
|\mathcal G_{B,L}^{\rm clean}|
\le \mathfrak P_{B,L},
\qquad
\mathfrak P_{B,L}
=
\sum_{\substack{\ell,\rho\in\mathcal P_L\\\ell\ne\rho}}
\frac{\rho-1}{\ell\rho}
\sum_{k=1}^{\rho-1}
\left\|
\mathcal A_{\ell\to\rho;k}
\right\|^2.
}
\tag{T-106081.10}
\]

The coefficient is \((\rho-1)/(\ell\rho)\): the field
\(\mathcal A_{\ell\to\rho;k}\) has \(\rho-1\) nonzero \(\rho\)-phases. This
corrects the transposed phase-cardinality coefficient in the first draft of
`T-106081`.

This is a mixed owner-squareclass phase moment. Inside
\(\mathcal A_{\ell\to\rho;k}\),

\[
e_\rho(k n_i)
=
e_\rho(k\ell\Lambda_i a_i^2),
\]

and the varying co-owner \(\Lambda_i\) cannot be removed by one common
permutation of \(k\).

## 3. Correct open theorem

Define

```text
MOBOSM106081:
  after exact carrier, Wick, Boolean-Vaughan, owner, shell, marked-67,
  shared-owner and owner/core-overlap recombination, the dyadic sum of the
  selector-tied positive moments

      sum_(B,L: L^2<2B) P_(B,L)

  is X^(o(1)), with every literal source weight used exactly once.
```

Equivalently, one may prove the source-tied bilinear form
\(\mathcal G_{B,L}^{\rm clean}\) directly without passing through Cauchy.

The relation \(L^2<2B\) is available throughout `MOBOSM106081`; hence the
remaining difficulty is no longer a distinguished-conductor/core mismatch. It
is coherent aggregation over varying co-owner squareclasses and source-tied
owner selectors.

A two-way linear projection separates two sharper subtargets at only an
absolute Cauchy cost:

```text
MOBOSM-NE106081:
  the no-exception sector, where P_i <= a_i;

MOBOSM-EX106081:
  the unique-exception sector, where lambda_i^5 < 4 sqrt(Y).
```

Proving both subtargets proves `MOBOSM106081`. Neither is presently closed.

Under the Gauss--Mellin transform, the same target is a restricted long-core
version of the principal and nonprincipal owner-conductor moment in
`T-106030`. In the scale-matched residue coordinate, it is the long-core
owner-crowding component of `HQORO106071`.

## 4. Implication graph

Let `BSFTI106081` denote transport of the fixed-owner Boolean Type-I estimate
through the frozen parent owner ledger. The self-reconstruction finds no new
power loss in this transport, but keeps it explicit for independent review.

Then

\[
\boxed{
\mathrm{BSFTI}_{106081}
\wedge
\mathrm{MOBOSM}_{106081}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106081.11}
\]

The final two arrows are the frozen parent Volterra/Mellin consumer.

## 5. Current status

```text
Boolean Vaughan identity                         PROVED EXACT
balanced Boolean core has two primes             PROVED EXACT
squarefree fixed-owner Type-I                     PROVED POWER-SAVING
minimum-owner rule                                PROVED EXACT
lambda^2 <= a and L^2 < 2B                        PROVED EXACT
no-exception P <= a                               PROVED EXACT
exceptional lambda^5 < 4 sqrt(Y)                  PROVED EXACT
abstract same-family centered identity            PROVED EXACT
selector-tied Gram T-106081.8                     PROVED EXACT
positive-moment reduction T-106081.10             PROVED EXACT
BSFTI106081 global parent-ledger transport        REVIEWABLE / NOT NEWLY CLOSED
MOBOSM106081 source-tied owner moment              OPEN / RH-BEARING
T-106080 direct L-102883 adapter                   RETRACTED BY R-106080
Riemann Hypothesis                                UNPROVED
```
