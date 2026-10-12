# Native quadratic/quartic transport on a finite slab

Status: proposed directed replay; runtime and independent review pending.
Target: actual `Xi(z)=xi(1/2+i*z)`, derivative order zero, `lambda=1`, and
the closed rectangle `|T|<=500`, `0<=y<=1/2`, `z=T-i*y`.
No companion-sector result on this target is claimed before full PASS.

The checker [check_quartic_slab.py](check_quartic_slab.py) replays every
native census bracket and the same imported historical complete-count
contract in NATIVE_SLAB_CERTIFICATE.md. Directed degree-four Gamma/zeta
series and the complete finite root sums then enclose both native tail log
coefficients `a_1,b_2`. It proves the whole `b_2` interval positive and,
for fixed `K=16384`, the whole Gaussian interval
`a=a_1-sqrt(2K b_2)` positive. Every artificial root lies beyond 8192.
The entire source-bound coefficient rectangle is enclosed in each leaf;
neither coefficient is replaced by a midpoint.

The exact model and full residual are those of
[QUARTIC_ABSORPTION.md](QUARTIC_ABSORPTION.md):
`G=Xi(0)*exp(-a*z^2)*P_R*(1-v*z^2)^K`, `v=sqrt(2b_2/K)`.
To avoid interval loss from canceling the matched Gaussian and artificial
quadratic contributions separately, its bulk logarithmic derivatives use
the exact algebraic identities

\[
\ell_1=L_1-2a_1z-\frac{4b_2z^3}{1-vz^2},
\qquad
\ell_2=L_2-2a_1-
\frac{4b_2z^2(3-vz^2)}{(1-vz^2)^2}.
\tag{QS1}
\]

Here `L_1,L_2` belong to the known finite product's nonvanishing bulk.
These formulas retain the exact relation `Kv^2=2b_2` for the whole
parameter family. All artificial denominators are guarded.

Every finite root above the exact lower-bracket cutoff 1024 is retained
in the 16-term directed finite Taylor sum and full remainder in (FJ1)--(FJ4).
Every remaining known root is handled individually, and nearby factors
use (FJ5)--(FJ7) to cross their real zeros without a singular division.
The protected radius is `B=501`; both the native and artificial residual
disk guards are checked before using the complete degree-six budgets
(QA5)--(QA6). These budgets retain all unseen tail zeros, possible nonreal
zeros and the entire artificial factor.

The positive half starts with 2,000 by 4 exact boxes of widths `1/4` and
`1/8`, covering `[0,500]` by `[0,1/2]`. Every failed enclosure is replaced
by all four exact dyadic children, with depth exhaustion failing the
checker. The full leaf-count identity is `leaves=8000+3*splits`.
The actual even-real companion identity (GS2) reflects the complete cover
to negative T. Every accepted leaf proves the strict QA9 predicate and
extracts its exact rational actual-source sector bound.

All finite, native Taylor, parameter, remainder and transport arithmetic
is directed Arb/acb/acb_series at 192 bits. The planned receipt is full
deterministic gzip JSON, retaining every exact leaf margin and hashing
the direct proof/checker source list and backend binaries. The same
qualified historical finite FLINT count input is imported; its Rosser
rule is not independently rerun, and the arithmetic implementation is
shared with the candidate producer.

This is a finite target with fixed order and lambda. Matching two native
coefficients does not prove a cofinal sector, an Euler bridge or RH.
