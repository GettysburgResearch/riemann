# T-105260 — Polarization-paid strict-bandwidth \(90\%\) cut

Claim ID: `T-105260`  
Status: **PROVED CONDITIONAL IMPLICATION; EDGEFLUX105260 OPEN**  
Created: 2026-08-24  
Depends on: L-105260--L-105262; L-105500/L-105520  
RH status: unproved

Let \(C_T\) be the actual Xi critical-residue compression on the retained one-sided real channel, with

\[
d_T=\left(\frac{999}{1000}+o(1)\right)N_1(T,2T).
\tag{1}
\]

By L-105260--L-105261, after normalization,

\[
C_T\succeq(1-o(1))I+H_T+E_T,
\tag{2}
\]

where

\[
\operatorname{tr}((\operatorname{Re}H_T)_-)<\left(\frac1{60}+o(1)\right)d_T
\tag{3}
\]

and \(E_T\) is the non-source edge/strip remainder.

Assume `EDGEFLUX105260`:

\[
\operatorname{tr}((E_T)_-)<\left(\frac{647}{19980}-o(1)\right)d_T.
\tag{4}
\]

Ky Fan subadditivity for the negative trace and the accretive-anchor argument then give

\[
\nu_{\le0}(C_T)<\left(\frac1{60}+\frac{647}{19980}+o(1)\right)d_T
=\left(\frac{49}{999}+o(1)\right)d_T.
\tag{5}
\]

Therefore

\[
\nu_+(C_T)>\left(\frac{950}{999}-o(1)\right)d_T
=\left(\frac{19}{20}+o(1)\right)N_1(T,2T).
\tag{6}
\]

The exact confluent full-signature theorem yields

\[
\boxed{\liminf_{T\to\infty}\frac{N_0(T,2T)}{N(T,2T)}>0.9.}
\tag{7}
\]

The theorem is an exact implication and improves the old all-in-one `STRIPNEG105520` request:

- the physical half-order and cutoff scaling are retained;
- the false \(p p^\#=p^2\) promotion is replaced by exact Toeplitz--Hankel polarization;
- the polarization budget is proved \(<1/60\);
- all pinned coefficient/freezing/tail rows are removed;
- only the explicit \(647/19980\) edge-flux budget remains.

`EDGEFLUX105260` is not proved here. Consequently \(90\%\), density one, and RH remain unproved.
