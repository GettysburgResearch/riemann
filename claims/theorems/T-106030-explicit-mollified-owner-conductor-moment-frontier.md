# T-106030 — Explicit mollified owner-conductor moment frontier

Claim ID: `T-106030`  
Programme aliases: `LFAM1.MOLLIFIED_OWNER_CONDUCTOR_MOMENT`, `LFAM2.KUMMER_MOMENT_HANDOFF`, `STRESS.EXPLICIT_ASSEMBLY_FRONTIER`  
Status: **EXACT SPECTRAL NORMAL FORM; MOMENT ESTIMATES OPEN**  
Created: 2026-08-24  
Depends on: `L-106025--L-106027`; `T-106020`; PR #719 `HBCQDSP102888`  
Programme issues: #743, #736, #737  
RH status: **unproved**

This theorem replaces the descriptive gate `SOCM106020` by one explicit family
moment. It does not estimate that moment.

## 1. Source-owned spectral packets

Fix a dyadic physical horizon. For every opposite owner conductor `rho`, split
owner pairs by

\[
\sigma=\kappa_\rho(P)\in\{+1,-1\}
\]

as required by `L-106027`. Let `eta` range over the even characters modulo
`rho`.

For each source-owned packet `i` in the sector `(rho,sigma,eta)`, retain:

```text
its deterministic owner pair P_i;
its physical shell S_i;
its dyadic-frozen Vaughan cutoff U_i;
its literal owner, gauge and selector coefficient omega_i;
one square root chi_(rho,eta) with chi_(rho,eta)^2=eta.
```

The choice of square root is harmless inside one `sigma` sector: replacing it
by `chi*kappa_rho` multiplies every owner factor by the same scalar `sigma`.

Define

\[
\boxed{
\mathcal A_{\rho,\sigma,\eta}(t)
=
\sum_{i\in\mathcal I_{\rho,\sigma,\eta}}
\omega_i\,\chi_{\rho,\eta}(P_i)
P_i^{-1/2-it}
B_{U_i;P_i,\eta}^{\mathcal S_i}(1+2it),
}
\tag{T-106030.1}
\]

where

\[
B_{U;P,\eta}^{\mathcal S}
=
\Pi_{\mathcal S}
\left[
{(1-M_{U;P,\eta}Z_{P,\eta})^2\over Z_{P,\eta}}
\right]
\tag{T-106030.2}
\]

is the exact physical-shell projection of the mollified reciprocal-`L` defect.
The coefficient `omega_i` includes the literal source allocation, including
the selected conductor weight `rho^(-1/2)`; no free family weight is inserted.

## 2. Exact positive moment

Let `kappa(u)=K_L(e^u)`. The complete source-owned owner-conductor moment on the
horizon is

\[
\boxed{
\begin{aligned}
\mathfrak M_L
={1\over2\pi}
\sum_\rho\sum_{\sigma=\pm1}
\int_{\mathbb R}|\widehat\kappa(t)|^2
\Bigg[&
{\rho+1\over\rho-1}
|\mathcal A_{\rho,\sigma,1}(t)|^2\\
&+{2\rho\over\rho-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\mathcal A_{\rho,\sigma,\eta}(t)|^2
\Bigg]dt.
\end{aligned}
}
\tag{T-106030.3}
\]

Equation (T-106030.3) follows exactly from:

1. the Gauss--Mellin square-phase identity;
2. the two owner quadratic classes;
3. the fixed-shell Mellin--Plancherel identity;
4. the owner-conductor Vaughan ratio in (T-106030.2).

Every summand is nonnegative. The principal/quadratic root fibre and every
nonprincipal even character are retained.

The principal pole at `t=0` is harmless because

\[
\widehat\kappa(t)=O(t)
\]

and the projected balanced ratio has at most a simple pole.

## 3. Two genuine analytic subproblems

Define

```text
PCM106030:
  the eta=1 principal/quadratic-root contribution to M_L is 2^(o(L));

NEM106030:
  the sum of the eta!=1 even-character contributions to M_L is 2^(o(L)).
```

Because the decomposition is positive,

\[
\boxed{
\mathrm{PCM}_{106030}\wedge\mathrm{NEM}_{106030}
\Longrightarrow
\mathfrak M_L=2^{o(L)}.
}
\tag{T-106030.4}
\]

The distinction is scientific rather than cosmetic:

- `NEM106030` is a true family moment over nonprincipal Dirichlet
  `L(1+2it,eta)` channels and is the natural large-sieve/trace-formula target;
- `PCM106030` contains the coherent semiprime owner amplifier and the exact
  principal carrier cancellation. It is not implied by a nonprincipal family
  estimate.

## 4. Conclusion chain

The local observation in each `(rho,sigma)` sector has norm squared
`(rho-1)/(rho+1)`, and recombining the two `sigma` sectors costs at most `2`.
The inherited long-core and Type-I rows are already closed. Therefore

\[
\boxed{
\mathfrak M_L=2^{o(L)}
\Longrightarrow
\mathrm{SOCM}_{106020}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106030.5}
\]

Equivalently,

\[
\boxed{
\mathrm{PCM}_{106030}
\wedge
\mathrm{NEM}_{106030}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106030.6}
\]

Neither moment estimate is proved.

## 5. Function-field target

Over `F_q[T]`, replace owner primes by owner irreducibles and the even
Dirichlet characters by Kummer sheaves on their residue fields. The exact local
Fourier transform is already proved in `L-106023`; the open theorem is the
coherent moment analogue of (T-106030.3), with degree-shell projections and
all resonant strata explicit.

A useful geometric proof should identify whether `NEM106030` is supplied by
Deligne-type trace cancellation, monodromy averaging or a relative trace
formula, and should state what replaces `PCM106030`. It must not infer the
number-field estimate merely from function-field RH.

## 6. Exact boundary

```text
balanced source = projected mollifier defect / L     PROVED EXACT
fixed-shell Mellin--Plancherel form                   PROVED EXACT
owner quadratic-class partition                      PROVED EXACT
local occupancy / root-fibre leverage                 PROVED EXACT
PCM106030 principal moment                            OPEN / RH-BEARING
NEM106030 nonprincipal even-family moment             OPEN
SOCM106020 owner-packet assembly                      OPEN / RH-BEARING
HBCQDSP102888                                         OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
