# L-23719 — Endpoint kernel, constant quotient jumps, and fixed-depth atom-tail order

Claim ID: `L-23719`  
Title: The endpoint residual has one explicit sawtooth kernel with a favorable divisor correction; every fixed quotient depth is eventually nonpositive by the PNT  
Status: **PROPOSED COMPLETE PARTIAL THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23717`; the classical prime number theorem for `vartheta(x)`  
Scope: endpoint-atom geometry and fixed-depth tails; neither AWTO nor RH is claimed

## 1. Exact endpoint residual kernel

Put

\[
N=T-1,
\qquad
\ell_N=\log\left(1+\frac1N\right),
\qquad
d_N=4\left(\frac1{\sqrt N}-\frac1{\sqrt{N+1}}\right).
\tag{L-23719.1}
\]

For real `2<=x<=N`, let

\[
K_N(x)=\left\lfloor\frac Nx\right\rfloor
\tag{L-23719.2}
\]

and define the open-cell kernel

\[
\boxed{
 g_N^{\circ}(x)
 =d_NK_N(x)
 -2\ell_N\sum_{k=1}^{K_N(x)}
   \left(\sqrt{kx+1}-\sqrt{kx}\right)
 -\frac{\ell_N}{\sqrt x}.
}
\tag{L-23719.3}
\]

The analytic endpoint profile used in `L-23717` is

\[
\widetilde F_N(m)=2\ell_N\sqrt m-d_Nm.
\tag{L-23719.4}
\]

At the entering endpoint `m=N+1`, however, the physical profile is zero rather
than `widetilde F_N(N+1)`.  Define the exact endpoint correction

\[
\boxed{
 b_N
 =\widetilde F_N(N+1)
 =2\ell_N\sqrt{N+1}-d_N(N+1).
}
\tag{L-23719.5}
\]

Then, for every prime `p<=N`, direct substitution into `L-23717.11` gives

\[
\boxed{
 e_{N+1}(p)
 =g_N^{\circ}(p)+b_N\mathbf1_{p\mid N}.
}
\tag{L-23719.6}
\]

The correction is favorable.  Writing `x=1+1/N`,

\[
 b_N
 =2\sqrt{N+1}\,[\log x-2(\sqrt x-1)]<0,
\tag{L-23719.7}
\]

because `log x<2(sqrt(x)-1)` for every `x>1`.

This divisor correction is load bearing: omitting it gives a wrong value whenever
`p|N`.

## 2. Monotone cells and one constant jump

On the open quotient cell

\[
\frac N{K+1}<x<\frac NK,
\tag{L-23719.8}
\]

`K_N(x)=K` is fixed.  Differentiating (L-23719.3) gives

\[
\boxed{
 (g_N^{\circ})'(x)
 =\ell_N\left[
  \sum_{k=1}^{K}k
   \left(\frac1{\sqrt{kx}}-\frac1{\sqrt{kx+1}}\right)
  +\frac1{2x^{3/2}}
 \right]>0.
}
\tag{L-23719.9}
\]

At every reciprocal boundary `x=N/K`, increasing `x` removes the last summand.
The right-minus-left jump is independent of `K`:

\[
\boxed{
 j_N
 =-d_N+2\ell_N(\sqrt{N+1}-\sqrt N)
 =2(\sqrt{N+1}-\sqrt N)
   \left[\ell_N-\frac2{\sqrt{N(N+1)}}\right]<0.
}
\tag{L-23719.10}
\]

The last sign follows from

\[
\ell_N<\frac1N<\frac2{\sqrt{N(N+1)}}.
\]

Thus the endpoint residual is an increasing function on each quotient cell,
with one identical downward jump at every quotient boundary, plus the favorable
prime-divisor correction (L-23719.6).

## 3. Exact continuum atom and its upper tails

For `0<u<=1`, put

\[
K=\left\lfloor\frac1u\right\rfloor,
\qquad
S_K=\sum_{k=1}^{K}\frac1{\sqrt k},
\tag{L-23719.11}
\]

and define

\[
\boxed{
 \phi(u)=2K-\frac{S_K+1}{\sqrt u}.
}
\tag{L-23719.12}
\]

For every fixed `a>0`, uniformly on the closures of the finitely many quotient
cells in `[a,1]` with the declared one-sided conventions,

\[
\boxed{
 N^{3/2}g_N^{\circ}(Nu)\longrightarrow\phi(u).
}
\tag{L-23719.13}
\]

Indeed,

\[
N^{3/2}d_N\to2,
\qquad
N\ell_N\to1,
\]

and

\[
2\sqrt N\,(\sqrt{kNu+1}-\sqrt{kNu})\to\frac1{\sqrt{ku}}.
\]

The continuum upper tail can be evaluated exactly.  If

\[
\frac1{K+1}\le c\le\frac1K,
\]

then finite summation by parts over the complete quotient cells gives

\[
\boxed{
 \mathcal H(c):=\int_c^1\phi(u)\,du
 =2\big[(S_K+1)\sqrt c-Kc-1\big].
}
\tag{L-23719.14}
\]

Let

\[
\delta_K=2\sqrt K-(S_K+1).
\tag{L-23719.15}
\]

Then

\[
\boxed{
 \mathcal H(c)
 =-2\left[(1-\sqrt{Kc})^2+\delta_K\sqrt c\right].
}
\tag{L-23719.16}
\]

For `K=1`, `delta_1=0`.  For `K>=2`,

\[
\delta_{K+1}-\delta_K
 =2(\sqrt{K+1}-\sqrt K)-\frac1{\sqrt{K+1}}>0,
\]

and

\[
\delta_2=2\sqrt2-2-\frac1{\sqrt2}>\frac1{10}.
\]

Consequently

\[
\boxed{
 \mathcal H(c)<0\quad(0<c<1),
}
\tag{L-23719.17}
\]

and, throughout `0<c<=1/2`,

\[
\boxed{
 \mathcal H(c)\le-\frac15\sqrt c.
}
\tag{L-23719.18}
\]

The continuum endpoint atom therefore has a strict negative weighted upper tail
at every fixed positive ratio.  Its total tail tends to zero as `c downarrow 0`;
the deep quotient layers remain load bearing.

## 4. Fixed-depth prime-tail theorem

Let

\[
\vartheta(x)=\sum_{p\le x}\log p
\]

and retain the endpoint prime tail

\[
\mathcal A_{N+1}(z)
 =\sum_{z\le p\le N}(\log p)e_{N+1}(p).
\tag{L-23719.19}
\]

Fix an integer `R>=2`.  Then there is `N_R` such that, for every `N>=N_R`
and every real cutoff

\[
\frac N{R+1}\le z\le N,
\]

one has

\[
\boxed{
 \mathcal A_{N+1}(z)\le0.
}
\tag{L-23719.20}
\]

### Proof

For `z>N/2`, this is the termwise upper-half theorem `L-23717.23`.
It remains to treat

\[
N/(R+1)\le z\le N/2.
\]

Put `c=z/N`.  After multiplying by `sqrt(N)`, equation (L-23719.6) gives a
Stieltjes integral against the normalized prime measure

\[
d\nu_N(u)=N^{-1}d\vartheta(Nu),
\]

plus the nonpositive divisor correction.  The prime number theorem gives

\[
\nu_N([a,b])\longrightarrow b-a
\]

uniformly on every fixed compact subinterval of `(0,1]`.

On `[1/(R+1),1]`, the functions

\[
h_N(u)=N^{3/2}g_N^{\circ}(Nu)
\]

have uniformly bounded total variation: there are only `R` quotient cells,
(L-23719.9) controls the variation inside each cell, and (L-23719.10) controls
the finitely many jumps.  Equation (L-23719.13), followed by Stieltjes
integration by parts on each cell, therefore gives the uniform convergence

\[
\boxed{
 \sup_{1/(R+1)\le c\le1/2}
 \left|
  \sqrt N\,\mathcal A_{N+1}(cN)-\mathcal H(c)
 \right|\longrightarrow0.
}
\tag{L-23719.21}
\]

By (L-23719.18), on this interval

\[
\mathcal H(c)\le-\frac1{5\sqrt{R+1}}.
\]

Hence the prime tail is negative for every sufficiently large `N`, uniformly in
all declared cutoffs.  This proves (L-23719.20).

## 5. Consequence: every obstruction has unbounded quotient depth

Suppose there is a sequence of endpoint-tail violations

\[
\mathcal A_{N_j+1}(z_j)>0,
\qquad N_j\to\infty.
\]

Then (L-23719.20), applied for every fixed `R`, forces

\[
\boxed{
 \frac{z_j}{N_j}\longrightarrow0,
 \qquad
 \left\lfloor\frac{N_j}{z_j}\right\rfloor\longrightarrow\infty.
}
\tag{L-23719.22}
\]

Thus no finite quotient-layer enumeration can prove or refute AWTO cofinally.
The only possible obstruction is the deep quotient family in which the number of
constant jumps tends to infinity.  This is precisely the source that must be
handled by a digital, Möbius, reflected, or lower-scale recurrence.

## 6. Relation to the repository-wide frontier

- `L-23717` closed the complete upper half termwise.  The present theorem closes
  every fixed finite quotient depth asymptotically.
- PR #276 identifies the summed dyadic shell tail with WSTS.  Equation
  (L-23719.22) shows that the remaining endpoint source is not a fixed-ratio
  prime-sampling problem.
- The constant jump (L-23719.10) explains why absolute-value Stieltjes estimates
  accumulate a long harmonic boundary ledger: there are `N/z` equal quotient
  charges.  A successful proof must recombine them before taking norms.
- The favorable divisor correction (L-23719.7) must be retained in every exact
  finite checker.

## 7. Proof boundary

Proposed complete in this file, pending independent review:

1. the exact endpoint residual kernel including divisor endpoints;
2. monotonicity inside every quotient cell;
3. the constant negative quotient jump;
4. the exact continuum upper-tail formula and strict sign;
5. eventual atom-tail nonpositivity at every fixed quotient depth;
6. concentration of any possible AWTO obstruction in unbounded quotient depth.

Not proved:

1. uniform control as the quotient depth tends to infinity;
2. AWTO or RCT;
3. WSTS;
4. RH.
