# M-106070 — Hostile review verdict for the attempted scale-matched CROP closure

Claim ID: `M-106070`  
Status: **HOSTILE SELF-AUDIT COMPLETED — FULL CLOSURE REJECTED**  
Created: 2026-08-25  
Verdict recorded: 2026-08-25  
Applies to: `R-106070--R-106071`, `L-106070--L-106075`, `T-106070--T-106071`, `X-106070--X-106071`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The first `T-106070` proposal was reviewed against the mandatory source,
multiplicity and homogeneity interfaces in the original version of this
contract.  It fails at a precise arithmetic edge and has been retracted.

## 1. Audit verdict

```text
three-prime block palette                         ACCEPTED
linear nonduplicating owner colours               ACCEPTED
marked-67 exclusion                               ACCEPTED
coefficientwise unramified principal recovery     ACCEPTED
partial matching of cores for fixed owner pair    ACCEPTED
representation aggregation                        ACCEPTED
exact 1/(P B) block energy                        ACCEPTED
diagonal conductor payment                        ACCEPTED
quartic pair-tensor conductor payment              ACCEPTED
quartic tensor -> quadratic family moment          REJECTED
HBCQDSP102888 closure                              NOT REACHED
RH composition                                     RETRACTED
```

The first invalid interface is the attempted use of a quartic
Hilbert--Schmidt quantity to control a quadratic character-family Gram.
`R-106071` gives both the homogeneity proof and an explicit finite
counterfixture.

## 2. The failed equations

The exact family moment is

\[
\frac1{\ell-1}\sum_\chi\|V_\chi\|^2
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2.
\tag{M-106070.1}
\]

The attempted closure bounded instead

\[
\ell\sum_{P,Q,d}
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2.
\tag{M-106070.2}
\]

Equation (M-106070.1) scales quadratically; (M-106070.2) scales quartically.
The former cannot be bounded by the latter uniformly as the source amplitude
tends to zero.  The first attempted `L-106073.6` was therefore unsupported.

## 3. Correct reconstruction order

A reviewer of the corrected packet should now reconstruct:

1. the exact HBC residual and absence of the smooth-boundary row;
2. the block coefficient and `1/(P B)` energy;
3. the four Bertrand candidates and removal of `67`;
4. the three-prime linear owner-colour partition;
5. residual-level unramified principal recovery;
6. character Parseval in the exact quadratic form (M-106070.1);
7. the diagonal payment `ell * E = X^(o(1))`;
8. square/nonsquare owner-ratio classification;
9. fixed-owner-pair partial matching of physical cores;
10. the distinction between quadratic owner coherence and its quartic
    Hilbert--Schmidt shadow;
11. the at-most-two-cores-per-owner/residue theorem;
12. closure of every subpower owner-crowding cell;
13. the remaining high-crowding quadratic Gram `HQORO106071`;
14. its identification with the physical occupancy norm `BPOE103300`.

## 4. Binding mutations for future work

Any later closure attempt fails automatically if it:

```text
chooses a modulus after an owner pair is exposed;
duplicates one source atom across several modulus colours;
allows the selected modulus to divide an owner or core;
uses post-residual ramified completion without an unramified proof;
forgets the marked-67 sectors;
replaces the block energy 1/(P B) by 1/P before paying the conductor;
confuses a core partial matching with bounded owner occupancy;
replaces ||sum owner vectors||^2 by sum of products of squared norms;
uses a quartic replay as evidence for a quadratic family theorem;
drops the principal-character factor ell;
applies independent negative parts before all-chaos carrier recombination;
claims BPOE103300 from low-crowding residue cells alone;
claims RH while HQORO106071 remains open.
```

## 5. Replay boundaries

`X-106070` remains a valid finite mutation detector for:

```text
palette construction;
owner colours;
unramifiedness;
core-line injectivity;
representation Cauchy;
quartic pair-tensor payment;
compact-support constants.
```

`X-106071` checks the exact quadratic residue Gram, scaling counterexample and
low-crowding inequality.  Neither replay proves the high-crowding owner
assembly, the Mellin consumer, or RH.

## 6. Correct acceptance classifications

### Current accepted mathematics

```text
scale-matched source partition and core matching     proved;
diagonal and low-crowding residue sectors            proved;
quadratic owner-residue normal form                   proved;
high-crowding owner assembly                         open.
```

### Future full acceptance

A complete proof must establish `HQORO106071` in the exact quadratic
normalization of `L-106074`, after which the frozen implication

\[
\mathrm{HQORO}_{106071}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}
\]

may be reviewed.

The rejection is substantive rather than reputational: it names the first
false mathematical interface and preserves every preceding theorem that
survived the audit.