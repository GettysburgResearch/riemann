# T-106001 — The auxiliary completed family is synchronized to `HBCQDSP102888`

Claim ID: `T-106001`  
Status: **CORRECTED EXACT MOVING-PARENT SYNCHRONIZATION; MOMENT OPEN**  
Created: 2026-08-24  
Base: PR #719 at `c2e82cfdd254a478731f005b3d83b49d3e1e33ea`  
Depends on: `L-106000--L-106004`; `R-106001`; PR #719 `L-102886--L-102888`  
Programme issues: #743, #736, #737  
RH status: **unproved**

PR #719 now admits a horizon-safe pair gauge in which:

```text
the Vaughan cutoff is frozen on each dyadic block;
cutoff-transfer atoms disappear after exact Type-I/II recombination;
every nonowner label is completable;
the largest-two smooth-boundary current is absent;
the owner-excluded Type-I row is power-small.
```

The sole current arithmetic row is

```text
HBCQDSP102888:
  the coherent balanced distinct-product physical current in the
  owner-excluded horizon-safe pair gauge.
```

## Corrected auxiliary-family construction

For each auxiliary prime `ell != 67`, form the complete source family of
`L-106000`, perform ramified completion, and only then apply the deterministic
residual functor `R_HBC` from `L-106004`:

\[
\mathcal R_{\chi,\ell}=R_{\rm HBC}(\mathcal D_{\chi,\ell}).
\]

For the principal character,

\[
\boxed{
\mathcal R_{\chi_0,\ell}=R_{\rm HBC}
}
\tag{T-106001.1}
\]

coefficientwise. `R-106001` forbids reversing this order.

For a predeclared positive family and amplifier define

\[
\Lambda_X=
\sum_\ell w_{\ell,\chi_0}|A_{\ell,\chi_0}|^2
\]

and

\[
\mathfrak M_{\rm HBC}(Y)=
\int_2^Y\sum_{\ell,\chi}
 w_{\ell,\chi}|A_{\ell,\chi}|^2
 |\mathcal R_{\chi,\ell}(X)|^2{dX\over X}.
\]

Then

```text
PLEV106001:
  Lambda_X >= X^(-o(1));

HCLM106001:
  M_HBC(Y)=Y^o(1)
```

imply

\[
\int_2^Y|R_{\rm HBC}(X)|^2{dX\over X}=Y^{o(1)},
\]

and hence

\[
\boxed{
\mathrm{PLEV}_{106001}\wedge\mathrm{HCLM}_{106001}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106001.2}
\]

Neither premise is proved. The owner-conductor family of `T-106020` removes the
separate leverage premise locally and is now the preferred continuation.

```text
moving-parent source synchronization      PROVED EXACT
post-residual completion shortcut          REFUTED
auxiliary principal leverage               OPEN
auxiliary HBC family moment                OPEN / RH-BEARING
HBCQDSP102888                              OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```