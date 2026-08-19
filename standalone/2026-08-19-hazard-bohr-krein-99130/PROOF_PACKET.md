# T99130 — The Bernoulli-hazard rabbit, its Bohr obstruction, and the unique pole-safe prime–continuum generator

**Scientific status:** proposed exact successor; independent review required.  
**Riemann Hypothesis:** unproved.  
**Frozen base:** PR #623 at `712412e286cc309bbe9960ee839df158316df9e5`.  
**Namespace:** mechanically migrated from the unpublished `99100` draft because the live repository already contains unrelated `99100` branches.  
**Carry/factor-67 routes:** not imported.

## 1. The rabbit

Let

\[
B_\diamond(s)
=
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
=
(1-2^{-s})^2(1-2^{-s-1})
\prod_{p\ {\rm odd}}(1-p^{-s}).
\]

The natural real-carrier-free logarithmic hazard is

\[
\boxed{
\mathcal H(s)=\frac{B_\diamond'(s)}{1-B_\diamond(s)}.
}
\tag{1.1}
\]

At a nontrivial zero \(\rho\) of \(\zeta\), of multiplicity \(m\),

\[
B_\diamond(s)=c_\rho(s-\rho)^{-m}(1+O(s-\rho)),
\]

so

\[
\boxed{
\mathcal H(s)=\frac{m}{s-\rho}+O(1).
}
\tag{1.2}
\]

At the real pole of zeta,

\[
B_\diamond(s)=\frac38(s-1)(1+O(s-1)),
\]

and therefore \(\mathcal H(1)=3/8\). Thus (1.1) appears to remove the deterministic real carrier while retaining every zeta zero with a simple multiplicity residue.

## 2. Exact conditional-singleton representation

For a finite family of channels

\[
x_j(s)=c_j e^{-\lambda_j s},
\qquad 0<c_j\le1,\quad \lambda_j>0,
\]

put

\[
B_J(s)=\prod_{j\in J}(1-x_j(s)).
\]

For real \(s>0\), take independent Bernoulli variables \(X_j\) with \(\Pr(X_j=1)=x_j(s)\). Then

\[
1-B_J(s)=\Pr\!\left(\sum_jX_j\ne0\right)
\]

and

\[
B_J'(s)=\sum_j\lambda_jx_j(s)\prod_{k\ne j}(1-x_k(s)).
\]

Consequently

\[
\boxed{
\frac{B_J'(s)}{1-B_J(s)}
=
\mathbb E\!\left[
\lambda_j\mathbf1_{\{\{k:X_k=1\}=\{j\}\}}
\ \middle|\ 
\sum_kX_k\ne0
\right]\ge0.
}
\tag{2.1}
\]

For \(B_\diamond\), the channels are one channel \(p^{-s}\) for every odd prime \(p\), two copies of \(2^{-s}\), and one channel \(2^{-s-1}\). Absolute convergence passes (2.1) to the full Euler product for real \(s>1\).

## 3. Bohr twist and the counterfeit-pole theorem

Let the completely multiplicative Euler phase be

\[
\omega_2=-1,
\qquad
\omega_p=1\quad(p\ {\rm odd}).
\]

The corresponding equivalent Euler product is

\[
B_\omega(s)=(1+2^{-s})^2(1+2^{-s-1})\prod_{p\ {\rm odd}}(1-p^{-s}).
\]

For real \(\sigma>1\), with \(a=2^{-\sigma}\),

\[
\boxed{B_\omega(\sigma)=\frac{(1+a)^2(1+a/2)}{(1-a)\zeta(\sigma)}.}
\tag{3.1}
\]

At \(\sigma=6/5\), one has \(a<7/16\), because \(64\cdot7^5>16^5\), and \(\zeta(6/5)>5\). Therefore

\[
B_\omega(6/5)<\frac{20631}{23040}<1.
\tag{3.2}
\]

At \(\sigma=2\),

\[
B_\omega(2)>\frac{75}{64}>1.
\tag{3.3}
\]

By continuity, \(B_\omega(\sigma_0)=1\) for some \(6/5<\sigma_0<2\).

For every finite prime set, rational independence of the prime logarithms and Kronecker's theorem give ordinates for which the phase of \(2\) approaches \(-1\) and the phases of all included odd primes approach \(+1\). A diagonal choice over increasing prime sets gives \(t_k\to\infty\) with

\[
2^{-it_k}\to-1,\qquad p^{-it_k}\to1\quad(p\ {\rm odd})
\]

prime by prime. Uniform Euler tails on compact subsets of \(\Re s>1\) give

\[
B_\diamond(s+it_k)\to B_\omega(s)
\]

locally uniformly. Choose an isolated zero \(\sigma_*\in(6/5,2)\) of \(B_\omega-1\). Hurwitz's theorem gives zeros \(z_k\) of \(B_\diamond-1\) with \(\Re z_k\to\sigma_*>1\) and \(|\Im z_k|\to\infty\). Hence

\[
\boxed{\mathcal H(s)\text{ has infinitely many counterfeit poles in }\Re s>1.}
\tag{3.4}
\]

## 4. Uniqueness of the pole-safe first-order transform

Consider \(\mathcal T_R=B_\diamond'R(B_\diamond)\) with rational \(R\). Require no poles at finite nonzero values of \(B_\diamond\), at most a simple multiplicity pole at every pole of \(B_\diamond\), and at most a simple pole at the zero \(s=1\). Then \(R\) is a Laurent polynomial. Pole behavior forces its largest exponent to be at most \(-1\), and zero behavior forces its smallest exponent to be at least \(-1\). Thus

\[
\boxed{R(z)=c/z.}
\tag{4.1}
\]

## 5. The unique normalized signed generator

Define

\[
\boxed{\mathcal K_\diamond(s)=\frac{B_\diamond'}{B_\diamond}(s)-\frac1{s-1}+\frac1s.}
\tag{5.1}
\]

It is analytic at \(s=1\), tends to zero at positive real infinity, and at a zeta zero \(\rho\) of multiplicity \(m\),

\[
\boxed{\mathcal K_\diamond(s)=-\frac{m}{s-\rho}+O(1).}
\tag{5.2}
\]

Moreover

\[
\boxed{\mathcal K_\diamond(s)=\int_0^\infty e^{-st}\,d\eta_\diamond(t),}
\]

where

\[
\boxed{d\eta_\diamond(t)=\sum_{n\ge2}\Lambda_\diamond(n)\delta_{\log n}(dt)-(e^t-1)\,dt.}
\tag{5.3}
\]

## 6. Why every positive completion loses the cancellation

The atomic and continuous parts are mutually singular. If a positive matrix measure has \(d\eta_\diamond\) in its off-diagonal, then

\[
\boxed{d\alpha+d\beta\ge2|d\eta_\diamond|.}
\tag{6.1}
\]

For \(k_T(t)=e^{-t/2}e^{-t^2/(4T)}\), the continuum total variation alone satisfies

\[
\boxed{\int_0^\infty k_T(t)(e^t-1)\,dt\ge\frac12e^{T/4-1/4}.}
\tag{6.2}
\]

Thus every positive completion has heat type at least \(1/4\) and cannot yield the required subexponential signed estimate.

## 7. The genuinely new frontier

On the graded space consisting of the generalized-prime atomic Hilbert space and the continuum Hilbert space with signature \(J=\operatorname{diag}(1,-1)\), the correct observable is a supertrace.

> **PCSS — Prime–Continuum Supersymmetric Similarity.** Construct a source-prescribed odd transport pairing the prime and continuum multiplication operators before absolute values, and prove a fixed-center subexponential supertrace estimate for the exact source.

PCSS would exclude every off-line zero by (5.2). It remains RH-bearing and unproved.

## 8. Exact status

```text
Bernoulli conditional-singleton identity        PROVED EXACT
real-axis hazard positivity                     PROVED EXACT
Bohr-twist counterfeit poles in Re(s)>1         PROVED
hazard denominator as RH detector               REFUTED
unique pole-safe rational first-order transform PROVED
pole-centered prime-continuum signed source     PROVED EXACT
positive completion heat floor exp(T/4)         PROVED
Krein/supertrace theorem PCSS                    OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
