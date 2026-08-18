# T-97900 — Factor-67 Lorenz–Bellman frontier after the fixed-angle no-go

Claim ID: `T-97900`  
Status: **UNCONDITIONAL ADVANCE + SHARP OPEN FRONTIER**  
Created: 2026-08-18  
Frozen base: PR #591 at `5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111`  
RH status: **unproved**

The exact source-faithful maps of PR #591 remain valid:

\[
\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}
\Longrightarrow R_X\ge0\Longrightarrow\mathrm{RH},
\]

while `NCBI67` is a distinct sufficient scalar mechanism.

This successor proves two new facts.

1. The literal repaired base cone `F>=M/42` fails after adjoining only the actual
   prime `67`, with first real crossing in
   \[
   160.37507<X<160.37508.
   \]
2. More generally, no fixed positive scalar-to-mass angle can be invariant under
   all finite rough-prime completions. The exact asymptotic angle is
   \[
   \prod_{p\mid P}(p-1)/(p+1),
   \]
   and can be made arbitrarily small.

Therefore every proof architecture of the form

```text
positive P61 bias with fixed aperture
 -> same aperture after each rough prime
 -> scalar positivity
```

is closed by `R-97900`.

The conclusion-producing theorem is now sharply restricted to one of the
following genuinely unnormalized statements:

```text
LBP67: complete Euler-minus Lorenz slack is nonnegative;
CPSL67: complete source Lorenz dual is nonnegative for all lambda;
NCBI67: the exact nonlocal contracted current satisfies c>=Tc;
RBLPTE67: the exact root zero-hinge future tail is paid.
```

The first three are related only by the proved implication graph in PR #591;
they are not renamed equivalents. The future-product quotient profile is
necessary, and any mass aperture used inside it must vanish with the installed
prime set.

```text
source-faithful Lorenz recurrence             PROVED
exact NCBI/CPSL maps                          PROVED
fixed 1/42 Bellman cone                       REFUTED AT p=67
all fixed positive mass-angle cones           REFUTED
future quotient profile                       NECESSARY
LBP67 / CPSL67 / NCBI67 / root scalar         OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
