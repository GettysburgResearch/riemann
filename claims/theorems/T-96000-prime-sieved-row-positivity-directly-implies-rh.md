# T-96000 — Prime-sieved parabolic-row positivity gives a direct Mellin–Landau proof candidate for RH

Claim ID: `T-96000`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-16  
New analytic spine: `R-96000`, `L-96000`, `L-96001`  
Finite producer: `L-94200--L-94201` on the frozen parent  
Repository status: **RH is not treated as established before independent review**

## 1. Nonnegative fixed-row functions

For every `j>=2`, define

\[
 f_j(X)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]

The prime-sieved parabolic theorem gives

\[
 f_j(X)\ge0\qquad(X\ge1).
\tag{T-96000.1}
\]

No endpoint optimization, factor-67 recurrence, Target--Lorenz packet, Brownian approximant, Schur port, or native benchmark comparison occurs below.

## 2. Landau's theorem forces convergence in every positive half-plane

Let `sigma_j` be the abscissa of convergence of

\[
 \int_1^\infty f_j(X)X^{-s-1}\,dX.
\]

The elementary growth estimate in `L-96000` makes `sigma_j` finite. Since `f_j>=0`, Landau's theorem for Mellin transforms says that, if `sigma_j` is finite, the real point `s=sigma_j` is a singularity unless the integral already converges beyond it.

But `L-96000.8` gives the meromorphic continuation

\[
 \mathcal C_j(s)=\frac{C_j}{s^2}+\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)},
\]

and `L-96000.9` proves that this continuation is analytic at every positive real `s`. Hence

\[
 \boxed{\sigma_j\le0.}
\tag{T-96000.2}
\]

The defining Mellin integral is therefore holomorphic throughout

\[
 \Re s>0.
\tag{T-96000.3}
\]

## 3. Exclusion of an off-line zero

Suppose that

\[
 \zeta(\rho)=0,\qquad \rho=\beta+i\gamma,\qquad \beta>\frac12.
\]

Set `s_rho=rho-1/2`, so `Re(s_rho)>0`. By `L-96001`, choose a fixed `j` for which

\[
 P_j(\rho)\ne0.
\]

Then `L-96000.8` has a nonremovable pole at `s=s_rho`, whereas (T-96000.3) says the same function is holomorphic there. This contradiction excludes every zero with real part greater than `1/2`.

The functional equation reflects the conclusion across the critical line. Therefore

\[
 \boxed{\mathrm{RH}.}
\tag{T-96000.4}
\]

## 4. Complete proof graph

```text
canonical parabolic row
 -> initial-prime divisor-cube positivity        L-94200
 -> full Möbius component row f_j(X)>=0          L-94201
 -> explicit fixed-row Mellin transform          L-96000
 -> row-kernel noncancellation                   L-96001
 -> Landau real-abscissa theorem
 -> exclusion of every beta>1/2 zero
 -> functional equation
 -> RH.
```

## 5. No-RH-input audit

The proof candidate uses only:

```text
finite divisor-cube algebra and convexity;
the exact canonical row formula;
the absolutely convergent Möbius Dirichlet series for Re z>1;
classical meromorphic continuation of zeta;
the elementary absence of real zeta zeros in (1/2,1);
Euler--Maclaurin for a fixed complex exponent;
Landau's theorem for nonnegative Mellin transforms;
the functional equation.
```

It does not assume:

```text
RH or GRH;
a power-saving prime-number theorem;
Mertens square-root cancellation;
a zero-density estimate;
CPBD, SID, or a balanced Type-II estimate;
the native benchmark bridge;
an endpoint deficit estimate.
```

## 6. Hostile review boundary

The shortest route-killer is a counterexample to `L-94200/L-94201`, or a gap in its universal `FRONTIER-CHAIN` reservoir proof. The new Mellin and Landau interfaces are separately reconstructible and have no numerical campaign.

```text
finite row positivity                 conclusion-producing theorem
Mellin transform                      exact
kernel noncancellation                exact asymptotic
Landau composition                    classical
accepted proof of RH                  no
Riemann Hypothesis                    unproved pending review
```
