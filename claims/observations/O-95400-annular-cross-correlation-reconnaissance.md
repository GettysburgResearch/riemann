# O-95400 — Annular cross-correlation reconnaissance

Claim ID: `O-95400`  
Status: **FLOATING DISCOVERY ONLY — NON-PROBATIVE**  
Created: 2026-08-18  
Depends on: exact kernels in `X-95400`

The lightweight replay evaluates the exact piecewise formulas in ordinary double precision at selected integer endpoints. Representative values for

\[
\mathcal A(X),
\qquad
\mathcal D_A(X),
\qquad
\mathcal X_A(X)=\mathcal A(X)^2-\mathcal D_A(X)
\]

are:

```text
X=       256   A=  1.9060461908   D=  4.8548052343   Xcorr= -1.2217931527
X=     1,000   A=  0.3212714358   D=  8.9887748156   Xcorr= -8.8855594801
X=    10,000   A= -0.1120869776   D= 22.5595378563   Xcorr=-22.5469743657
X=   100,000   A= -0.4926485529   D= 44.5929654588   Xcorr=-44.3502628622
```

The observed negativity suggests the stronger inequality

\[
|\mathcal A(X)|^2\le\mathcal D_A(X)
\]

may be worth testing. No proof is supplied, and `R-95400` shows that no source-blind matrix argument can establish it.

The retained result records the scan separately from exact algebra. No finite scan is used in `T-95400`.
