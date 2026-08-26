# T-106120 — Bilateral Kummer prime-Wick tensor: exact construction, superseded uncentered moment frontier

Claim ID: `T-106120`  
Programme aliases: `LFAM1.BILATERAL_KUMMER_TENSOR`, `LFAM2.DOUBLE_PRIME_WICK_MOMENT`, `STRESS.SOURCE_SYMMETRIC_FAMILY`  
Status: **EXACT BILATERAL CONSTRUCTION RETAINED; FIRST UNCENTERED MOMENT FRONTIER SUPERSEDED BY `R-106122`, `R-106131`, `T-106121`, AND `T-106140`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106120--L-106126`; `R-106122--R-106123`; `R-106131`; parent `BCI102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The following bilateral construction remains exact.

After common-square extraction,

\[
N=Pg^2c^2,
\qquad
M=Qg^2d^2,
\qquad
(c,d)=1,
\]

and the canonical internal phase primes are

\[
\ell=P^-(c),
\qquad
\rho=P^-(d).
\]

They supply two same-occurrence nonzero Ramanujan phases. Both source sides
and both semiprime-owner sums are assembled before the square, and the tensor
Gauss transform gives four channels:

```text
principal--principal;
principal--nonprincipal;
nonprincipal--principal;
nonprincipal--nonprincipal.
```

The complete character coordinates are the physical squareclasses `Pc^2` and
`Qd^2`.

## Superseded parts of the first frontier

Two later hostile audits are binding:

1. `R-106122`: varying core characters prevent replacement of
   `Pc^2` by `P` or `Qd^2` by `Q`;
2. `R-106131`: the full atomic diagonal carries
   `(ell-1)(rho-1)`, not one.

Therefore the first claims that:

```text
owner-product collisions describe the global nonprincipal family;
the complete positive tensor atomic diagonal is already subpower;
all three positive channel groups form the preferred conclusion conjunction;
```

are withdrawn.

## What remains conclusion-facing

The principal--principal positive moment of corrected `L-106121` is sufficient:

\[
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
\]

Its principal atomic diagonal is paid. The mixed and double uncentered
positive moments are exploratory and have dimension-bearing atomic traces.

The preferred repaired family route is the exact Wick-centered identity of
`T-106140`:

\[
\mathrm{WCADD}_{106140}
\wedge
\mathrm{WCKUM}_{106140}
\Longrightarrow
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
\]

## Retained exact mathematics

```text
bilateral least-prime partition              retained;
double Ramanujan identity                    retained;
source-symmetric amplification order         retained;
tensor Gauss transform                       retained;
owner Wick-square factorization              retained;
physical-squareclass collision geometry      retained;
four linear core-line reduction              retained;
function-field nonprincipal shell theorem    retained locally.
```

RH remains unproved.
