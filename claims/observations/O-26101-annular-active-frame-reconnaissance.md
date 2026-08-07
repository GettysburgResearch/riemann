# O-26101 — Annular active-frame reconnaissance

Observation ID: `O-26101`  
Title: Source-generated active prime-power rows retain a visible frame moat while a fixed-annulus projection produces bounded flows and negligible objective cost  
Status: **FLOATING RECONNAISSANCE — NOT A CERTIFICATE OR ASYMPTOTIC THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26103`; NumPy floating linear algebra

## 1. Discovery iteration

For

\[
 I_X=[0.45X,0.80X],
\]

form the complete prime-power matrix

\[
 A_X(q,j)=2\mathbf1_{q\mid j}
 -\mathbf1_{q\mid j-1}
 -\mathbf1_{q\mid j+1}.
\]

Start from the actual parabolic residual. At every step:

1. retain rows with positive residual;
2. compress identical annular rows by keeping the largest residual;
3. apply the half-step minimum-norm correction
   \[
   u=A_S^*(A_SA_S^*)^\dagger r_S,
   \qquad F\leftarrow F+u/2;
   \]
4. update every prime-power residual.

The script uses an ordinary floating least-squares inverse and stops when every residual is below `1e-10`. It is discovery arithmetic only.

## 2. Representative runs

```text
X       initial + rows   initial frame   minimum generated frame
200          5             27.9836              0.6493
500         11             23.0038              0.8219
1000        18             22.7621              1.0543
2000        28             21.4495              0.9321
5000        54             26.8359              0.8046
```

The same runs gave

```text
X       iterations   ||F||_2      ||F||_infinity    objective cost
200         53       0.05714          0.02281        1.77e-6
500         48       0.07586          0.01795        3.68e-8
1000        57       0.07570          0.01158        2.74e-8
2000        68       0.07386          0.00915        3.29e-9
5000        85       0.06566          0.00454        3.07e-10
```

Every reported run had

```text
minimum repaired b coordinate          >= ordinary solver tolerance
maximum final prime-power defect       <= 1.0e-10
```

The generated active-frame floor did not drift toward zero in this range, even though the full annular prime-power matrix contains very ill-conditioned arbitrary row subsets. This supports the source-specific quantifier in `SAF`; it does not support a generic frame theorem.

## 3. Why highly composite sites occur

The adjoint update is

\[
 (A_S^*y)_j
 =2\sum_{q\mid j}y_q
 -\sum_{q\mid j-1}y_q
 -\sum_{q\mid j+1}y_q.
\]

Hence a site `j` with many active prime-power divisors receives many simultaneous central repair contributions. Its neighbors discharge the induced mass into other rows. The largest flow coordinates in the runs are accordingly concentrated at highly composite or divisor-rich upper-support integers.

This is not merely an empirical label: `L-26101` proves the exact divisor-gradient superposition behind the effect.

## 4. Contrast with the refuted cover

The monotone tail-cover cost at the same rough scales grows toward a square-root law and is exactly bounded below by PR #254. The annular signed-flow cost instead becomes tiny because its weight is `j^-2` and its source uses existing negative constraint slack.

The two optimizations are not alternate parameterizations of the same positive cover.

## 5. Strongest suggested theorem

The data nominate the exact `SAF` statement:

```text
initial positive residual norm           X^o(1)
generated active Gram floor              X^-o(1)
positive leakage contraction             rho<1
cumulative annular flow norm              X^o(1)
```

Together these imply an objective loss `X^(-3/2+o(1))`, far below what the RH consumer needs.

## 6. Proof boundary

`experiments/X-26101-annular-divisor-frame/recon.py` reproduces the floating runs. It is intentionally excluded from the exact proof-object digest.

No line in this observation proves `SAF`, the sharp prime-ramp estimate, or RH.