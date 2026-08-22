# T-105210 — Low-order Levinson descent through one quotient and one Fourier-compound localization gate

Claim ID: `T-105210`  
Status: **MAJOR UNCONDITIONAL LOW-ORDER STRUCTURE + PROPOSED COMPLETE TERMINAL-ENDPOINT THEOREM; RH UNPROVED**  
Created: 2026-08-23  
Updated: 2026-08-23  
Depends on: `R-105201`, `L-105206--L-105212`; PR #720 `L-104518--L-104521`  
RH status: **unproved**

## 1. The previous cumulative budget is not the producer

`R-105201` proves exactly that the `CRDB105200` upper ledger is

\[
\mathcal D_r
=O_0+2\sum_{j<r}
\left[R_j(1-\mathfrak C_j)-E_j\right].
\tag{T-105210.1}
\]

It is the unknown off-real zero count plus nonnegative slack.  The natural
high-derivative entry removes `O_r`, but it does not estimate the fixed
low-order horizontal argument or the last wrong extremum.  Accordingly,
`CRDB105200` is retained only as a correct sufficient ledger and is removed as
the principal research producer of this branch.

## 2. All derivative-level boundary terms collapse to one quotient

Fix one `lambda>0` across a finite ladder and put

\[
G_{k,\lambda}
=\xi^{(k)}+\lambda\xi^{(k+1)}.
\]

`L-105206` proves

\[
\boxed{
\sum_{k<r}
\Delta_{\infty\to1/2}
\arg {G_{k,\lambda}\over G_{k+1,\lambda}}
=
\Delta_{\infty\to1/2}
\arg {G_{0,\lambda}\over G_{r,\lambda}}.
}
\tag{T-105210.2}
\]

The top-boundary logarithmic derivatives telescope in the same way.  Thus the
actual Levinson boundary difficulty is one continued endpoint quotient, not a
sum of `O(T^2 log T)` unrelated argument estimates.

For the native terminal parameter

\[
\lambda_r=M_r/M_{r+1},
\]

`L-105209` proposes a uniform two-tilt saddle proof that, whenever

\[
T\sqrt{\log r/r}\to0,
\]

the high derivative companion stays one-sided on the complete safe ray and

\[
\boxed{
\Theta_{r,\lambda_r}(T)=o(1).
}
\tag{T-105210.3}

This proposed analytic theorem requires independent hostile review.  If
accepted, the terminal denominator contributes no hidden inward unit.

## 3. The one remaining zeta auxiliary

`L-105211` gives the exact factorization

\[
\boxed{
\xi+\lambda\xi'
=H(s)(1+\lambda h(s))
\left[
\zeta(s)+{\lambda\over1+\lambda h(s)}\zeta'(s)
\right].
}
\tag{T-105210.4}

The first two factors are explicit and zero-free on the safe horizontal path.
For the native `lambda_r`, the remaining coefficient is of size `1/log T`.
Thus the sole zero-bearing endpoint is the classical-scale function

\[
\boxed{
V_{\lambda_r}(s)
=\zeta(s)+{\lambda_r\over1+\lambda_rh(s)}\zeta'(s).
}
\tag{T-105210.5}

## 4. Unconditional low-order Fourier structure

For every derivative order define

\[
\Lambda_k(t)
=\Xi^{(k+1)}(t)^2
 -\Xi^{(k)}(t)\Xi^{(k+2)}(t).
\]

`L-105207` proves the all-order exterior-square Gram theorem

\[
\boxed{
\left[
\Lambda_{a_i+a_j}(t_j-t_i)
\right]_{i,j}\succeq0.
}
\tag{T-105210.6}

It follows that:

```text
all even defects are positive-definite functions;
all autocorrelation-windowed derivative Hankel matrices are PSD;
every odd Fourier defect is Schur-dominated by its adjacent even defects;
every even derivative has an explicit central no-wrong-extremum interval.
```

`L-105208` proves the exact mean orientation

\[
\boxed{
\|E_{k,\lambda}(\cdot-iy)\|_2^2
>
\|E_{k,\lambda}^{\#}(\cdot-iy)\|_2^2
\qquad(y>0),
}
\tag{T-105210.7}

and the real-axis phase sum rule

\[
\boxed{
\int |E_{k,\lambda}|^2\theta_{k,\lambda}'
=2\lambda\int |\Xi^{(k+1)}|^2>0.
}
\tag{T-105210.8}

These are unconditional statements at `k=0` and at every fixed low order.
They prove that the source orientation is correct before height localization.

## 5. Critical residues are a positive near-collision Gram

At simple real zeros `c_j` of `Xi^(k+1)`, put

\[
\rho_j={\Xi^{(k)}(c_j)\over\Xi^{(k+2)}(c_j)}.
\]

`L-105212` constructs a curvature-normalized positive matrix

\[
K_{ij}^{(b)}
={\Lambda_{2b}(c_j-c_i)
 \over
 \Xi^{(k+2)}(c_i)^2\Xi^{(k+2)}(c_j)^2},
\qquad a+b=k,
\]

and proves

\[
\boxed{
\sum_{i<j}(\rho_i-\rho_j)^2
\le
\Lambda_{2a}(0)
\left[
R\operatorname{tr}K^{(b)}
-\mathbf1^TK^{(b)}\mathbf1
\right].
}
\tag{T-105210.9}

When the mean residue is negative,

\[
RM_2(1-\mathfrak C)
=\sum_{i<j}(\rho_i-\rho_j)^2.
\]

Thus the formerly opaque residue-coherence loss is one explicit positive
same-height near-collision Dirichlet energy.  `ESDE105212` asks for this energy
to be `o(RM2)`; it remains open.

## 6. The actual remaining theorems

Define `HLOC105210` to be the height-localization theorem:

```text
at the last defective ordinate, upgrade the exact translation-invariant /
line-averaged Fourier-compound positivity to a bound on the continued argument
of V_(lambda_r) strong enough to exclude an inward unit.
```

Define `ESDE105212` as the same-height exterior-square Dirichlet estimate which
forces residue coherence and removes the positive-residue alternative.

The exact last-defect theorem of `L-104518--L-104521` then gives

\[
\boxed{
\mathrm{ESDE105212}
\quad\wedge\quad
\mathrm{HLOC105210}
\Longrightarrow\mathrm{RH}.
}
\tag{T-105210.10}

This implication also requires the mean residue to have the correct negative
orientation at the last level, as stated in `L-105212`.  Neither open theorem
is claimed proved globally.

## 7. Exact boundary

```text
CRDB as an independent low-order producer         REFUTED
all derivative boundary arguments -> one quotient PROVED EXACT
complete high terminal safe-ray sector            PROPOSED COMPLETE / REVIEW REQUIRED
exact low-order zeta Levinson auxiliary            PROVED EXACT
all-order Xi exterior-square Fourier Gram          PROVED UNCONDITIONALLY
mean low-order Hermite-Biehler orientation          PROVED UNCONDITIONALLY
critical residues -> positive Gram Dirichlet energy PROVED UNCONDITIONALLY
ESDE105212 same-height residue dispersion           OPEN / RH-BEARING
HLOC105210 fixed-height argument localization       OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
