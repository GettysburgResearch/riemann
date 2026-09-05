# T-106450 — Corrected resolvent-weighted even-endpoint frontier

Claim ID: `T-106450`  
Status: **EXACT CORRECTION AND REDUCTION; RESGRAM106450 OPEN**  
Created: 2026-08-25  
Depends on: `R-106450`; surviving parts of `L-106440--L-106445`; `L-105290`  
RH status: **unproved**

`R-106450` is binding.  The denominator-multiplied source used in the first
endpoint-bank composition belongs to the Hankel kernel.  This theorem records
the strongest valid replacement.

## 1. Surviving endpoint identity

For fixed even `K`, put

\[
N_K=(\Xi-i\lambda\Xi')
    (\Xi^{(K)}+i\lambda\Xi^{(K+1)}),
\]

\[
D_K=(\Xi+i\lambda\Xi')
    (\Xi^{(K)}-i\lambda\Xi^{(K+1)}),
\]

and

\[
U_K={N_K\over D_K}.
\]

Then exactly

\[
\operatorname{wind}U_K=R_0-R_K,
\tag{T-106450.1}
\]

\[
N_K-D_K
 =2i\lambda
  (\Xi\Xi^{(K+1)}-\Xi'\Xi^{(K)}),
\tag{T-106450.2}
\]

and, for `K=2m`, the numerator in (T-106450.2) has Fourier transform

\[
(-1)^m i\xi\Lambda_m(\xi),
\qquad \Lambda_m(\xi)\ge0.
\tag{T-106450.3}
\]

These statements are unconditional.

## 2. Literal conclusion-facing symbol

The Hankel operator is

\[
\boxed{
H_{U_K}=H_{U_K-1}
 =H_{(N_K-D_K)/D_K}.
}
\tag{T-106450.4}

The positive exterior-square numerator is divided by the endpoint denominator.
Every pole and every principal-part weight must remain.

For a finite regular rational truncation, `L-106442` gives

\[
\boxed{
\|H_{U_K}\|_{\mathcal S_2}^2
 =\sum_{z,w\in\mathcal P_+(D_K)}
   r_z\overline{r_w}K_0^+(z,w),
}
\tag{T-106450.5}

where

\[
r_z={2i\lambda
 (\Xi\Xi^{(K+1)}-\Xi'\Xi^{(K)})(z)
 \over D_K'(z)}
\]

at every simple upper pole, and the confluent principal-part vector is used at
multiple poles.  The lower-half-plane matrix gives the opposite Hardy energy.

## 3. Correct fixed-order sufficient conditions

The exact all-pass charge gives

\[
R_0(T,2T)
 \ge R_K(T,2T)-\|H_{U_K}\|_{\mathcal S_2}^2-o(N).
\tag{T-106450.6}

Thus the literal fourth-endpoint theorem

```text
RESGRAM4_106450:
  limsup ||H_(U_4)||_S2^2 / N(T,2T) < 237/2500
```

implies more than ninety percent on the line, because

\[
{2487\over2500}-{237\over2500}={9\over10}.
\]

A weaker signed version is also sufficient.  For any declared Hardy projection
`P_T`, let

\[
\Delta_{K,T}
 =\operatorname{tr}(P_T^\perp H_{U_K}^*H_{U_K}P_T^\perp)
 -\operatorname{tr}(P_T^\perp H_{\overline{U_K}}^*
                    H_{\overline{U_K}}P_T^\perp).
\]

Then the exact source/complement identity remains valid, but its visible term
must be evaluated using `(N_K-D_K)/D_K`, not `N_K-D_K` alone.

## 4. Repaired research target

Define

```text
RESGRAM106450:
  prove either the full fourth-endpoint residue-Gram estimate

    limsup ||H_(U_4)||_S2^2/N < 237/2500,

  or a source-qualified signed decomposition whose complete visible and
  complementary terms sum to less than 237/2500.
```

This is a fixed `9.48%` theorem, not an RH-strength subpower estimate.
`L-106444--L-106445` already supply the exact companion barycenter, half-plane
count ledger and unweighted convex derivative-root compression.  The remaining
load is the denominator derivative/principal-part weight and coherent residue
Gram.

## 5. Supersession boundary

```text
endpoint winding and denominator cancellation       RETAINED PROVED
actual Xi exterior-square numerator                  RETAINED PROVED
signed Fourier/residue-Gram normal form              RETAINED PROVED
companion barycenter/root compression                RETAINED PROVED
finite source density ratios                         RETAINED AT SOURCE SCOPE
Dg source -> nonzero Hankel initial space             REFUTED
visible source cost <1/600 or <1/982 for H_U          WITHDRAWN
T-106430/T-106440 numerical percentage composition   SUPERSEDED
RESGRAM106450                                         OPEN / RECORD-BEARING
ninety percent                                        UNPROVED
density one / RH                                      UNPROVED
```