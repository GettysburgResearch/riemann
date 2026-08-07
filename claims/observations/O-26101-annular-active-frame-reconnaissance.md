# O-26101 — Annular active-frame reconnaissance

Observation ID: `O-26101`  
Title: Source-generated prime-power rows remain numerically well conditioned on the canonical annulus and produce tiny signed-flow costs  
Status: **FLOATING RECONNAISSANCE — NOT A CERTIFICATE OR ASYMPTOTIC THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Updated: 2026-08-08  
Issue: #261  
Depends on: `L-26103`, `L-26105`, `L-26108`; NumPy floating linear algebra

## 1. Discovery iteration

Use the canonical annulus

\[
 I_X=[0.20X,0.80X]
\]

and the complete prime-power matrix

\[
 A_X(q,j)=2\mathbf1_{q\mid j}
 -\mathbf1_{q\mid j-1}
 -\mathbf1_{q\mid j+1}.
\]

Starting from the actual parabolic residual, the discovery script:

1. retains rows with positive residual;
2. compresses identical annular rows by keeping the largest residual;
3. applies the half-step minimum-norm correction
   \[
   u=A_S^*(A_SA_S^*)^\dagger r_S,
   \qquad F\leftarrow F+u/2;
   \]
4. updates every prime-power residual.

The script uses ordinary floating least squares and stops when every residual is below `1e-10`.

## 2. Representative canonical-annulus runs

```text
X       iterations    minimum generated frame    ||F||_2
200         35                 4.3250              0.03623
500         35                 3.2317              0.04467
1000        42                 2.9885              0.04608
2000        35                 3.0555              0.04404
5000        38                 2.8630              0.04005
```

The exact formal objective changes were approximately

```text
X=200      -1.38e-7
X=500       9.30e-8
X=1000      2.10e-8
X=2000     -4.54e-9
X=5000     -8.15e-11
```

A negative value means the signed flow slightly increased the objective; the proof-facing quantity is its absolute magnitude.

Every reported run had

```text
minimum repaired b coordinate          >= ordinary solver tolerance
maximum final prime-power defect       <= 1.0e-10
```

The wider annulus improved the observed frame floor and lowered the flow norm compared with the initial top-half annulus.

## 3. Correction to the original recursive guess

The currently active residuals halve exactly, but leakage can activate other rows. In several runs an individual half-step increased the complete positive-residual norm; the largest observed ratios were slightly above one.

Therefore the uniform per-step contraction proposed in the first draft of `L-26103` is not supported and has been withdrawn.

The correct globally monotone quantity is the Hilbert--Farkas dual energy in `L-26106`. The active-set iteration remains a fast primal producer and a source-conditioning diagnostic.

## 4. Why highly composite sites occur

The adjoint update is

\[
 (A_S^*y)_j
 =2\sum_{q\mid j}y_q
 -\sum_{q\mid j-1}y_q
 -\sum_{q\mid j+1}y_q.
\]

A site `j` with many active prime-power divisors therefore receives many simultaneous central repair contributions. Its neighbors discharge the induced mass into other rows. The largest flow coordinates are accordingly concentrated at highly composite or divisor-rich integers.

This is structural rather than metaphorical: `L-26101` proves the exact divisor-gradient superposition.

## 5. Contrast with the refuted cover

The monotone tail-cover cost grows on a square-root scale and is exactly bounded below by PR #254. The signed annular flow has a tiny `j^-2` objective price because it moves mass into existing negative constraint slack.

The two optimizations are not alternate parameterizations of the same cover.

## 6. Proof-facing interpretation

The data support two narrower statements:

1. the source-generated row systems are much better conditioned than arbitrary annular subsets;
2. the exact optimum radius in `L-26105` may remain bounded or subpower.

The acceptance theorem is nevertheless `ADF`, not a numerical frame trend. The projected-dual potential of `L-26106` solves the finite optimization once its subpower optimum is proved.

## 7. Proof boundary

`experiments/X-26101-annular-divisor-frame/recon.py` reproduces floating runs when called with

```bash
python recon.py X 0.20 0.80
```

It is excluded from the exact proof objects.

No numerical row in this observation proves `ADF`, the sharp prime-ramp estimate, or RH.