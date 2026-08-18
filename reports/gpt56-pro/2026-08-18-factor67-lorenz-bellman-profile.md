# Factor-67 central frontier: source-faithful Lorenz-Bellman profile

## Frozen graph

```text
cutoff UTC       2026-08-18T03:35:00Z
main             f789265569013ebff254b082c2e0428970bdaf57
PR #576          0f6ea6eae813c1d867ae50744cf5fd57e2720bb7
PR #581          62aaa54ac49f0aa89fd58f14a539cc53089f884c
PR #582          699f9f119a66823702e96fba95cc8b14b8251c60
PR #584          e919c6afd1e95fffa505f7ba3f532cb12b8c410c
PR #587          8a0f074c5b96600b461fdd6e23b47ee2162c4a70
```

## Headline

The three named frontiers are not equivalent.

```text
completed-parity source problem
  = finite target/scalar common-source LP
  = D^plus(lambda)>=0 for all lambda;

CPSL67
  = uniform validity on the literal arithmetic source;

NCBI67
  = c>=Tc on a contracted scalar-current DAG;

LBP67
  = complete Euler-minus monotonicity of the base P61 Lorenz slack.
```

The exact implication graph is

\[
\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}\Longrightarrow f\ge0,
\qquad
\mathrm{NCBI}_{67}\Longrightarrow f\ge0.
\]

Exact finite countermodels disprove both abstract implications between NCBI67 and CPSL67.

## Exact source-faithful recurrence

For a paired source `(E,O)`, define

\[
D^+(\lambda)=\lambda T_O+\sum_{i\in E}a_i(r_i-\lambda t_i)_+-R_O,
\]

\[
D^-(\lambda)=\lambda T_E+\sum_{i\in O}a_i(r_i-\lambda t_i)_+-R_E.
\]

Forward common-source feasibility is exactly `D^plus>=0` for all real `lambda`. The two orientations satisfy

\[
D^++D^-=\sum_i a_i(\lambda t_i-r_i)_+\ge0.
\]

Adjoining a rough prime gives

\[
D_{Qp}^+(X,\lambda)=D_Q^+(X,\lambda)+p^{-1/2}D_Q^-(X/p,\lambda),
\]

and the reversed equation with orientations interchanged.

## Parity diagonalization

With

\[
P_Q^\pm=\prod_{p\in Q}(I\pm p^{-1/2}U_p),
\]

one obtains

\[
D_Q^+=P_Q^-D_0^++\frac{P_Q^+-P_Q^-}{2}(D_0^++D_0^-).
\]

The second term is the explicit sum over odd rough subsets and is nonnegative. This isolates the new sufficient producer

\[
\boxed{\mathrm{LBP}_{67}:\quad P_Q^-D_0^+(X,\lambda)\ge0.}
\]

At `lambda=0`, the cushion vanishes, so this is the actual completed scalar and no reserve is spent twice.

## Map to NCBI67

For the contracted paired-source identity `P=C plus T swap(P)`, let `f=D_P^plus(0)` and `c=D_C^plus(0)`. Then `f+Tf=c`. NCBI is `c>=Tc`, equivalently `(I-T^2)f>=0`, and hence implies `f>=0`. It controls the zero-frequency scalar slice only; it does not include target capacity or nonzero Lorenz thresholds.

The exact Lorenz residual is

\[
\mathfrak B_v(\lambda)=G_v^+(\lambda)-\sum_wt_{vw}D_w^+(\lambda),
\]

with

\[
D_v^+(\lambda)=\mathfrak B_v(\lambda)+\sum_wt_{vw}(D_w^++D_w^-).
\]

Thus `mathfrak B>=0` closes CPSL. At zero it equals the actual source scalar, not the child-current quantity used by NCBI.

## Exact no-go results

1. NCBI does not imply CPSL: one node has positive scalar but target capacity `1<2`; `D^plus(-10)=-9`.
2. CPSL does not imply NCBI: a three-node shift has CPSL at every node but violates `c>=Tc` at the root.
3. Forward slack alone is not Markov: the same `D^plus` can have different `D^minus` and therefore different swapped parents.
4. A root-only state is not Markov: prime addition uses the actual value at `X/p`.
5. The invariant two-sided nonnegative cone is unavailable: the literal base at `X=1`, `lambda=-1` has `(D^plus,D^minus)=(1,-1)`.
6. PR #581's two-node one-channel separator remains binding.

## Future-prime quotient profile

For activated squarefree future products `m`, the exact state is

\[
\mathbf D_Q(m)=(D_Q^+(X/m,\lambda),D_Q^-(X/m,\lambda)).
\]

In the diagonalized state,

\[
G_{Qp}(m)=G_Q(m)-p^{-1/2}G_Q(mp).
\]

A floor-only profile is insufficient for logarithmic/square-root coordinates unless the analytic germ inside every activation cell is retained.

At finite horizon, every Bellman transform is piecewise affine in `lambda`. A failure occurs on a target-capacity ray or at one explicit atom ratio, giving an exact endpoint/prime-set/quotient dual separator.

## Hostile fixtures

The exact directed odd-history fixture is reproduced:

```text
X=61841
history=(67)
terminal=(71,13)
active P61 divisors=239
canonical target gap >17.0050865382190525
reverse leafwise Hall infeasible
```

A separate full completed-source binary64 diagnostic at the same endpoint finds:

```text
even target       3402.241840353183
odd target        3400.468097872050
Lorenz slack        74.294612511978
marginal lambda      0
```

Thus the leaf separator is not automatically a global separator; other histories numerically pay it at this endpoint. This is non-probative.

The Bellman profile was scanned diagnostically through horizon `256`, all `3895` finite lambda breakpoints and `36` rough stages. No failure was found. The minimum was `27.84112422472556` at `p=X=67`, `lambda=0`.

## Strongest honest conclusion

The remaining theorem is exactly

\[
\boxed{\prod_{p\in Q}(I-p^{-1/2}U_p)D_0^+(X,\lambda)\ge0}
\]

for all finite rough sets, endpoints and Lorenz thresholds. A proof yields CPSL67 and RH; a single negative finite state yields a complete dual separator.

```text
LBP67             OPEN / RH-BEARING
CPSL67            OPEN / IMPLIED BY LBP67
NCBI67            OPEN / INDEPENDENT SUFFICIENT ROUTE
RH                UNPROVEN
```