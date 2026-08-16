# L-95101 — Two positive policy flows with opposite terminal defects give an exact positive CRCTP certificate

Claim ID: `L-95101`  
Status: **PROPOSED COMPLETE EXACT FINITE GLUING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-95100`; PR #538 `L-95040`  
Scope: finite positive-flow gluing; no theorem producing the two flows cofinally

Let `d^+` and `d^-` be two split flows for the same root-completed source.
Assume every split coefficient is nonnegative and their terminal parameters in
(L-95100.6) satisfy

\[
\tau_+\ge0\ge\tau_-.
\tag{L-95101.1}
\]

If both are zero, either flow is already exact. Otherwise put

\[
\lambda={\tau_+\over\tau_+-\tau_-}\in[0,1]
\tag{L-95101.2}
\]

and define

\[
d=(1-\lambda)d^++\lambda d^-.
\tag{L-95101.3}
\]

Every coefficient of `d` is nonnegative. Its internal divergence is the common
source, and

\[
(1-\lambda)\tau_++\lambda\tau_-=0.
\]

Hence both terminal coordinates vanish. Therefore

\[
\boxed{d\text{ is an exact nonnegative interior realization of the root-completed target}.}
\tag{L-95101.4}
\]

This proves that a sign-changing **control bank**, rather than one globally
positive stationary producer, is sufficient for CRCTP. The interpolation is
performed only after complete source-specific occupations have been computed;
it does not average two completed arithmetic targets or duplicate source mass.

The retained directed replay supplies such pairs at 96 endpoints from `40`
through `1024`, with both preliminary occupations strictly positive. That is a
finite certificate bank and not an all-scale theorem.
