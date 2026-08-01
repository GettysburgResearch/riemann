# X-18505 — First immutable real Suzuki P1 complete-complement certificate

## Classification

```text
CERTIFIED_POSITIVE_FINITE_GALERKIN_COMPLETE_COMPLEMENT
NO_RH_VERDICT
```

This experiment evaluates a genuine localized Suzuki form at the exact support

\[
a=\frac25
\]

on four uniform interior P1 Dirichlet hats on \([-2/5,2/5]\). It freezes a two-dimensional rational low packet `Q_W`, its exact mass-orthogonal two-dimensional ambient complement, a dyadic trial harmonic solve, and every matrix needed by `L-18512/T-18504` in one declared metric.

It proves

\[
\mathscr D_N\succeq \frac1{1000}G_W,
\qquad
\Delta_{a,N}=0
\]

for this finite Galerkin block.

It does **not** identify this four-hat space with the complete infinite-dimensional Suzuki low hierarchy, and it does not prove RH.

## Why this is an actual arithmetic level

Suzuki's exact screw kernel is used in its equation-(1.3) normalization. Since

\[
e^{2a}=e^{4/5}\in(2,3),
\]

the complete prime-power manifest contains exactly

```text
q = 2, Lambda(q) = log 2.
```

No prime cutoff or omitted-prime tail exists at this support.

Let `H''=g` with `H(0)=H'(0)=0`. For piecewise-constant P1 derivatives, every rectangle is evaluated exactly by

\[
H(x_1-y_0)-H(x_0-y_0)-H(x_1-y_1)+H(x_0-y_1).
\]

The producer freezes the six required primitive values at

\[
0,\frac4{25},\frac8{25},\frac{12}{25},\frac{16}{25},\frac45.
\]

The nonprime screw primitive contains the pole, gamma, and Lerch/Hurwitz terms. The prime primitive is

\[
H_2(t)=\frac{\log2}{\sqrt2}\frac{(t-\log2)_+^3}{6}.
\]

## Declared metric and packet

The metric is the exact P1 `L2` mass matrix. The exact packet matrices are stored as rational strings:

```text
Q_W : 4 x 2 frozen parity packet
Q_E : 4 x 2 exact G-orthogonal ambient complement
G_W = Q_W^T G Q_W
G_E = Q_E^T G Q_E
Q_E^T G Q_W = 0 exactly
```

At this first pipeline-control level the radical packet is empty, so `W=U` inside the frozen two-dimensional low packet. This is stated in the certificate and is not promoted to the cofinal radical architecture.

## Emitted production matrices

The immutable certificate contains:

```text
Q_W
P_W                 complete nonprime Suzuki compression
E_W                 complete q=2 prime compression
B_W = P_W + E_W
Z_W = Q_E^T A Q_W
C   = Q_E^T A Q_E
X_N                 exact dyadic trial harmonic solve
R_N = Z_W - C X_N
G_W
G_E
trial_lift_energy
C - (1/2) G_E
direct_block_LMI
```

Here the declared decomposition is `B_W=P_W+E_W`; `E_W` means the complete prime block at this support, not a midpoint terminal-window surrogate.

## Directed proof

The producer proves

\[
C\succeq\frac12G_E
\]

and forms the exact interval block

\[
\begin{pmatrix}
J_{X_N}^*\mathcal HJ_{X_N}-10^{-3}G_W & \mathscr R_N^*\\
\mathscr R_N & \frac12G_E
\end{pmatrix}.
\]

Every special-function primitive is outward enclosed with Python `Decimal` at 130 working digits. Euler's constant and the Hurwitz values use explicit Euler--Maclaurin remainders; the exponential Lerch series has an explicit positive tail. After scalar evaluation, every matrix operation is replayed with exact `Fraction` interval endpoints.

For a symmetric interval matrix `M`, the verifier writes

\[
M\succeq \operatorname{mid}(M)-\operatorname{diag}(r_i),
\qquad
r_i=\sum_j\operatorname{rad}(M_{ij}),
\]

and performs exact rational unpivoted `LDL^T` on that lower matrix.

The coercivity pivots are

```text
0.0227255815519965672503281666448
0.0789292609418339100582286733674
```

and the direct-block pivots are

```text
0.000301421703927576586792415763862
0.0111086382843888247916462396612
0.114128480786192049706108331413
0.0826567491824516351973969266348
```

All are strict. The block Schur complement therefore proves

\[
\mathscr D_N\succeq\frac1{1000}G_W.
\]

## Independent replay

`independent_midpoint.py` uses `mpmath`, not the Decimal interval implementation. It checks every primitive value against the directed box and reconstructs the ordinary Schur spectrum:

```text
0.0018466472663126740934856889529962303584347759139114
0.037798824882212158859711373842024232173924364972452
```

This replay is diagnostic only. The proof is the interval certificate plus exact rational consumer.

## Verification

```bash
python3 produce.py
python3 verify.py
python3 independent_midpoint.py
python3 -m unittest discover -s tests -v
```

The mutation suite rejects support drift, prime-manifest deletion, packet/metric changes, trial-solve changes, primitive corruption, direct-LMI corruption, pivot forgery, digest drift, and Boolean-as-integer inputs.

## Proof boundary

This closes the first real, nonzero-prime, finite Galerkin `W` block and validates the complete artifact schema. The remaining production obstruction is not this level's sign. It is the promotion to a form-core sequence whose packet captures the complete low hierarchy, followed by the cofinal estimate

\[
\|[G_{W,\lambda}^{-1/2}\mathscr D_{\lambda,N(\lambda)}G_{W,\lambda}^{-1/2}]_-\|\to0.
\]
