# T-106710 — Xi carrier-adapted source softening and the remaining physical bridge

Claim ID: `T-106710`  
Status: **EXACT XI-SPECIFIC FOURIER ADVANCE; FULL FREE-ENERGY BOUND OPEN**  
Created: 2026-08-27  
Depends on: `T-106670`, `L-106674`, `L-106710`, `R-106710`, `T-106700`  
RH status: **unproved**

The lossless free energy of `T-106670` is exactly equivalent, at small
regularization, to the physical endpoint canonical charge. `L-106674` splits
that charge into a forced topological index and a balanced phase energy.

`L-106710` supplies the first Xi-specific calculation of the corresponding
antiphase source at the carrier-adapted Fourier scale. For the fifth endpoint,

\[
\frac{a_{5,2/\xi}(\xi)}{(2/\xi)L_5(\xi)}
=\frac1{10}+O\left(\frac{e^{-\xi}}{\xi^2}\right).
\tag{T-106710.1}
\]

The exact generic bound is

\[
0\le a_{5,2/\xi}(\xi)\le\frac5\xi L_5(\xi).
\tag{T-106710.2}
\]

This rules out the low-mode/carrier mechanism of the structural countermodel
at high Xi source frequency and identifies a quantitative constant with room
inside the `11/500` shallow phase allowance after one blockwise phase rotation.
It does not yet control the physical source-Pick free energy because:

```text
(1) the physical mesoscopic scale lambda_j is constant in t, not 2/xi;
(2) the common outer denominator is retained by the Pick determinant;
(3) the full free energy contains the unit topological factor R5-R0;
(4) sampled fifth-residue signs are not determined by diagonal source density.
```

Define the remaining bridge `XICARRIERPICK106710` as the following Xi-specific
statement on the predeclared mesoscopic exhaustion:

```text
Transfer the conditional carrier law (T-106710.1) to the physical constant-
scale endpoint quotient in the exact source-Pick metric, including outer
normalization, confluent nodes and the forced index, with total free energy
strictly below 97/1000 N (or below 11/500 N after the 0.01 height split).
```

Then

\[
\boxed{
\mathrm{XICARRIERPICK}_{106710}
\Longrightarrow
\mathrm{MESOFREE}_{106670}
\Longrightarrow
\liminf_{T\to\infty}\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-106710.3}
\]

The present packet proves the Fourier side of the bridge and proves why it
cannot be promoted by formal substitution. It does not prove
`XICARRIERPICK106710`, the full free-energy bound, ninety percent, density one,
or RH.
