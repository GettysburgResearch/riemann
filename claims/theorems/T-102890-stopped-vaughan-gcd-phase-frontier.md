# T-102890 — Stopped-Vaughan gcd/phase reduction of the coherent squareclass frontier

Claim ID: `T-102890`  
Status: **MAJOR UNCONDITIONAL SOURCE/REGIME REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

The coherent squareclass programme must use the literal finite-prime stopping
condition \(P^+(a)<q\).  The unrestricted Type-I lattice is only a model and
has been superseded at that source-typing interface.

`L-102869--L-102888` give the corrected conclusion-facing decomposition.

## 1. The Type-I adverse part is closed

For every stopped squareclass,

\[
\mathcal C_{p,q}
=
\mathcal T_{p,q}^{\rm full}
+
\mathcal T_{p,q}^{\rm bdry}
+
\mathcal B_{p,q}.
\]

The unrestricted component satisfies

\[
\mathcal T_{p,q}^{\rm full}
=
c_+M_{U,q}^2+O(Y^{-1/6}),
\qquad c_+>0.
\]

Therefore its negative part is power-saving.  The favorable square is spent
only here.

The two literal coherent rows are

```text
smooth stopped-prime boundary;
balanced stopped-Vaughan Type II.
```

They remain on one owner/phase/gauge ledger.

## 2. Free and equal-product costs are closed

The complete stopped packet has subpower free labelled energy and subpower
equal-product multiplicity.  No free Fock norm is substituted for the
different-product physical restriction.

## 3. Common square cores

For two physical products

\[
N=P c^2,\qquad M=Qd^2,
\]

put \(g=(c,d)\).  Common-square extraction contributes the exact factor
\(g^{-2}\).

`L-102887` proves that

\[
g\ge X^{1/3}(\log(3X))^2
\]

has finite logarithmic absolute mass.  Thus the conclusion-bearing current is
supported on the small-gcd range

\[
g<X^{1/3}(\log(3X))^2.
\]

## 4. Exact three-packet normal form

After the common core is removed, the coprime reduced cores belong to exactly
one of:

```text
equal-core base:
  c_1=d_1=1;

one-sided discrepancy:
  exactly one of c_1,d_1 is nontrivial;

two-sided discrepancy:
  c_1>1 and d_1>1.
```

The unequal-core packets carry one or two source-owned nonzero internal phases.
Their fixed-block normalizations retain the gains

\[
\left(\frac1\ell+\frac1C\right)^{1/2}
\]

or

\[
\left[
\left(\frac1{\ell_d}+\frac1{C_N}\right)
\left(\frac1{\ell_c}+\frac1{C_M}\right)
\right]^{1/2}.
\]

No principal internal phase and no positive internal-prime power remain.

## 5. Exact remaining theorem

Let \(\mathscr S_{\rm stop}(X)\) be the carrier-recombined sum of:

```text
the stopped smooth-boundary row;
the balanced stopped-Vaughan row;
the equal-core base packet;
the one-sided internally phased packet;
the two-sided internally phased packet;
```

after:

```text
external owner phases;
shared-owner and owner/core renewals;
Euler/half-divisor/Wick gauge recombination;
equal-product collapse;
very-large-gcd removal;
fixed ratio-eight outer observation.
```

All terms are retained with their literal signs.

Define

```text
SGIC102890:
  on every dyadic physical horizon, the small-gcd coherent scalar
  S_stop has subpower logarithmic negative mass, uniformly in the
  stopped second-owner primes.
```

Then

\[
\boxed{
\mathrm{SGIC}_{102890}
\Longrightarrow
\mathrm{SVQDSP}_{102882}
\Longrightarrow
\mathrm{BQSP}_{102870}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
}
\]

`R-102869` is binding: the equal-core and core-discrepancy negative parts may
not be estimated independently, because their fixed-chaos carriers cancel only
in the complete all-chaos packet.

## Exact boundary

```text
literal stopped-prime Vaughan identity        PROVED EXACT
unrestricted Type-I adverse part              PROVED POWER-SAVING
smooth-boundary fixed-squareclass cost        PROVED POLYLOG
balanced free/equal-product cost              PROVED SUBPOWER
very-large common-core region                 PROVED ABSOLUTELY SUMMABLE
one/two internal nonzero phases               PROVED EXACT
internal phase/weight gains                   PROVED EXACT
small-gcd coherent summation SGIC102890        OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
