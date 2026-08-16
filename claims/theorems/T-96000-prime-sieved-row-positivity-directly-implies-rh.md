# T-96000 — Prime-sieved parabolic-row positivity gives a direct Mellin–Landau proof candidate for RH

Claim ID: `T-96000`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-16  
New analytic spine: `R-96000`, `L-96000`, `L-96001`  
Finite producer: `L-94200--L-94201` on frozen PR #537  
Repository status: **RH is not treated as established before independent review**

For every fixed \(j\ge2\), set

\[
 f_j(X)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]

The prime-sieved theorem gives

\[
 f_j(X)\ge0\qquad(X\ge1).
\tag{T-96000.1}
\]

Let \(\sigma_j\) be the abscissa of convergence of

\[
 \int_1^\infty f_j(X)X^{-s-1}\,dX.
\]

An elementary bound makes \(\sigma_j\) finite. Since \(f_j\ge0\), Landau's
theorem for Mellin transforms says that a finite real abscissa is a singularity
unless the defining integral continues holomorphically beyond it.

But `L-96000` gives

\[
 \mathcal C_j(s)=
 \frac{C_j}{s^2}+
 \frac{P_j(s+\tfrac12)}
 {s^2\zeta(s+\tfrac12)}
\tag{T-96000.2}
\]

and proves that it is analytic at every real \(s>0\). Hence

\[
 \sigma_j\le0,
\]

so the defining Mellin integral is holomorphic throughout \(\Re s>0\).

Suppose \(\zeta(\rho)=0\) with \(\Re\rho>1/2\). Put
\(s_\rho=\rho-\tfrac12\). By `L-96001`, choose a fixed \(j\) with
\(P_j(\rho)\ne0\). Then (T-96000.2) has a nonremovable pole at \(s_\rho\), in
the domain where the defining integral is holomorphic. Contradiction.

The functional equation excludes zeros to the left of the critical line.
Therefore the candidate concludes RH.

```text
canonical parabolic row
 -> finite initial-prime divisor-cube positivity   L-94200
 -> full Möbius row f_j(X)>=0                      L-94201
 -> fixed-row reciprocal-zeta Mellin transform     L-96000
 -> row-kernel noncancellation                     L-96001
 -> Landau real-abscissa theorem
 -> RH candidate                                   T-96000
```

No factor-67 recursion, Target--Lorenz tail, Brownian approximant, CPBD,
First-Hermite exclusion, Mertens square-root bound, power-saving PNT error,
zero-density estimate, or native benchmark bridge is assumed.

The first and dominant hostile-review target is the universal finite
`FRONTIER-CHAIN` reservoir proof in `L-94200`.

```text
full unconditional candidate   yes
accepted proof                  no
RH established                  no
```
