# O-90010 — Reconnaissance on the 3–7–5–1 annular endpoint

Claim ID: `O-90010` (provisional range; branch-qualified)  
Status: **FINITE RECONNAISSANCE + ROUTE NOTE; NOT A COFINAL SIGN THEOREM**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90015`, `T-90011`

The annular scalar

\[
 \mathcal U_9(729N)=3A_{729N}-7A_{81N}+5A_{9N}-A_N
\]

was evaluated at every multiple of 729 through `X=5,000,000`. It was strictly negative at all 6,858 endpoints. The least-negative value was the first one,

\[
 \mathcal U_9(729)=-1.3302554743085073\ldots,
\]

and the retained last value was

\[
 \mathcal U_9(4,999,482)=-2.4858667332464393\ldots .
\]

Selected endpoints were independently reconstructed from the exact annular radical formula rather than from four precomputed endpoint values; agreement was better than `1.6e-8` at the largest selected endpoint.

The important structural observation is not the finite sign. The filter has traded the global `log^2 X` prime-square moat for a fixed negative constant while deleting every radical/ramp coordinate below `X/729`. Under RH that constant dominates the complete critical-line zero series by more than `1.48`; if RH is false an off-line zero survives and eventually produces polynomial oscillation.

Thus the route is neither a numerical extrapolation nor another equivalent global wrapper. It is a fixed-width annular producer target with a theorem-grade reverse direction and a robust RH-side margin. The open problem is to exploit the local factorization of integers in `[N,729N]` strongly enough to pay the filtered complete-prime-power coordinate from the explicit moat.

Replay: `experiments/X-90015-annular-endpoint/verify.py`.
