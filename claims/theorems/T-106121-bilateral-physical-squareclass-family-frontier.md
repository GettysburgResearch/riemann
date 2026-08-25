# T-106121 — Corrected bilateral physical-squareclass family frontier

Claim ID: `T-106121`  
Programme aliases: `LFAM1.BILATERAL_PHYSICAL_SQUARECLASS`, `LFAM2.DOUBLE_KUMMER_COLLISION`, `STRESS.BILATERAL_TENSOR_AUDIT`  
Status: **EXACT FAMILY GEOMETRY RETAINED; PRINCIPAL MOMENT SUFFICIENT; UNCENTERED NONPRINCIPAL DIAGONAL CLAIMS CORRECTED BY `R-106131`; PREFERRED REPAIR `T-106140`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106120--L-106126`; `R-106122--R-106123`; `R-106131`; corrected `L-106121`; parent `BCI102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral tensor family is source-exact. Its character coordinates are
the complete physical squareclasses

\[
X=Pc^2,
\qquad
Y=Qd^2,
\]

not the owner products alone.

## 1. Exact retained channel geometry

For a nonprincipal character modulo `rho`, full/even character orthogonality
produces

\[
Pc^2\equiv\pm P'c'^2\pmod\rho.
\]

For a nonprincipal character modulo `ell`, it produces

\[
Qd^2\equiv\pm Q'd'^2\pmod\ell.
\]

Thus:

```text
principal--principal:
  no Kummer collision;

principal--nonprincipal:
  one physical-squareclass collision;

nonprincipal--principal:
  the opposite physical-squareclass collision;

nonprincipal--nonprincipal:
  both collisions simultaneously.
```

After the owner quadratic-class split, each one-sided collision is a union of
two or four linear core lines, as proved in `L-106126`.

The owner-only collision interpretation and its global large-conductor
consequence remain retracted by `R-106122`.

## 2. Correct conclusion-facing positive gate

Let `mathfrak P_PP` be the principal--principal moment in corrected
`L-106121.5`. It contains the native unphased bilateral member with the exact
source-dual weight, and its literal atomic diagonal is subpower.

Therefore

\[
\boxed{
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106121.1}
\]

This single principal gate was previously named `BTPS106121`.

## 3. Binding atomic correction to the other channels

The complete character weight of one conductor is `q-1`; for two conductors it
is `(ell-1)(rho-1)`. Hence the complete uncentered tensor atomic diagonal is

\[
g^2\ell\rho(\ell-1)(\rho-1)|z_\omega|^2.
\]

Only the bounded principal--principal part

\[
g^2\ell\rho c_\ell c_\rho|z_\omega|^2
\]

is paid by the source sum in corrected `L-106121`.

Consequently the first statuses

```text
BTMS106121 mixed positive moment             diagonal paid;
BTDS106121 double-NP positive moment         diagonal paid;
```

are withdrawn. These uncentered moments are not required companions to
`BTPS106121`.

## 4. Preferred repaired family route

`L-106131` normal orders every channel with respect to the literal source atom
and proves

\[
\mathfrak A^\circ
=
\mathfrak P^\circ+\mathfrak K^\circ.
\]

`T-106140` defines:

```text
WCADD106140:
  the global Wick-centered additive/CV-XD trace is subpower;

WCKUM106140:
  the global Wick-centered mixed/double Kummer trace is subpower.
```

The principal atomic diagonal is already paid, so

\[
\boxed{
\mathrm{WCADD}_{106140}
\wedge
\mathrm{WCKUM}_{106140}
\Longrightarrow
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106121.2}
\]

This is now the preferred L-family implication matrix because it keeps the
nonprincipal family information without paying one literal diagonal per
character.

## 5. Current status

```text
bilateral least-prime source partition          PROVED EXACT
tensor Gauss transform                          PROVED EXACT
physical-squareclass collision geometry         PROVED EXACT
linear core-line reduction                      PROVED EXACT
principal atomic diagonal                       PROVED SUBPOWER
full uncentered atomic diagonal                  NOT PROVED
BTPS / principal positive moment                OPEN / SUFFICIENT
WCADD106140                                      OPEN / RH-BEARING
WCKUM106140                                      OPEN / RH-BEARING
BCI102990                                        OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
