# T-108320 — Direct companion winding is the exact endpoint zero-count coordinate

Claim ID: `T-108320`  
Status: **EXACT WINDING REDUCTION; XI WINDING ESTIMATE AND NINETY PERCENT OPEN**  
Created: 2026-08-31  
Depends on: `T-108310`, `L-108320`  
RH status: **unproved**

For every fixed positive odd `K`, put

\[
E_{K,\epsilon}(z)
=
\Xi^{(K)}(z)+i\epsilon\Xi(z).
\]

On a regular dyadic height window define the corrected real-axis winding

\[
\mathfrak W_K(T)
=
\lim_{\epsilon\downarrow0}
{1\over\pi}
\left|
\Delta_{[T,2T]}\arg E_{K,\epsilon}
-
\pi\mathcal B_K(T)
\right|.
\tag{T-108320.1}
\]

Then `L-108320` gives the direct conclusion

\[
\boxed{
N_0(T,2T)
\ge
\mathfrak W_K(T)
-1
-\mathcal E_{K,\rm reg}(T).
}
\tag{T-108320.2}
\]

This theorem does not sum a derivative cascade. It does not pay a positive
canonical-correlation overestimate. It asks for the actual winding of one
entire endpoint companion.

## Endpoint 31

Define

```text
XI31WIND108320:
  liminf [W_31(T)-E_(31,reg)(T)]/N(T,2T) > 9/10.
```

Then

\[
\boxed{
\mathrm{XI31WIND}_{108320}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-108320.3}
\]

In the simple regular case,

\[
\mathfrak W_{31}
=|U_{31,+}-U_{31,-}|
=M_{31}-2\min(U_{31,+},U_{31,-}).
\]

Therefore `XI31WIND108320` and `XI31MINPHASE108310` are exact coordinate
forms of the same direct endpoint obstruction, not two independent premises.

## Contour route

For every zero-free boundary rectangle,

\[
\mathfrak W_K
=
\left|
2N_\Omega(E_{K,\epsilon})
-{1\over\pi}
\Delta_{\partial\Omega\setminus[T,2T]}
\arg E_{K,\epsilon}
-\mathcal B_K
\right|
\]

in the limit. This opens a source-defined phase/argument-principle attack that
can use the safe-line prime field while retaining every vertical and endpoint
charge.

```text
minority phase = winding deficit      PROVED EXACT
parent real zeros >= companion winding PROVED EXACT
argument-principle boundary ledger     PROVED EXACT
XI31WIND108320                          OPEN
more than 90 percent                    UNPROVED
density one / RH                        UNPROVED
```
