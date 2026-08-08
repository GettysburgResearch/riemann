# L-28401 — Shifted central Dirichlet–Taylor contraction

Claim ID: `L-28401`  
Title: The infinite shifted central carry operator is a strict contraction on one explicit analytic power-tail space  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #284  
Dependencies: elementary binomial expansion, the alternating series for `eta`, and `zeta(3/2)<3`  
Scope: the analytic interior/bulk operator; finite cutoff boundary jets are treated separately

## 1. Infinite shifted central operator

For `x>=2` and a function on the positive half-line define

\[
(\mathscr C f)(x)
=\sum_{k\ge1}
\left[f(2kx-1)-f((2k+1)x)\right].
\tag{L-28401.1}
\]

For a power `p_s(x)=x^{-s}`, `s>0`, every paired summand is
`O_s(k^{-s-1}x^{-s})`; hence the series converges.

The operator is the infinite analytic model of the finite central residual of PR #280. It retains the forced lattice shift `-1`; it is not the unshifted continuum surrogate.

## 2. Exact Dirichlet–Taylor expansion

For every `k>=1`,

\[
(2kx-1)^{-s}
=x^{-s}(2k)^{-s}
\left(1-\frac1{2kx}\right)^{-s}.
\]

Since `x>=2`, the binomial series converges absolutely and uniformly. Summing first in `k` and then in the Taylor index gives

\[
\boxed{
\begin{aligned}
\mathscr C p_s(x)
={}&[1-\eta(s)]x^{-s}\\
&+\sum_{\ell\ge1}
\frac{(s)_\ell}{\ell!}
2^{-s-\ell}\zeta(s+\ell)
 x^{-s-\ell},
\end{aligned}}
\tag{L-28401.2}
\]

where `(s)_ell=s(s+1)...(s+ell-1)` and

\[
\eta(s)=\sum_{n\ge1}(-1)^{n+1}n^{-s}.
\]

Indeed, the `ell=0` coefficient is

\[
\sum_{k\ge1}(2k)^{-s}
-
\sum_{k\ge1}(2k+1)^{-s}
=1-\eta(s),
\]

while every `ell>=1` term comes only from the shifted even argument.

Thus the lattice shift does not create an uncontrolled same-order channel. It creates a positive upper-triangular tower of strictly faster powers.

## 3. Analytic coefficient space

Fix `sigma>=1/2` and `0<r<=1/4`. Let `A_(sigma,r)` be the space of expansions

\[
f(x)=\sum_{h\ge0}a_hx^{-\sigma-h}
\]

with norm

\[
\boxed{
\|f\|_{\sigma,r}
=\sum_{h\ge0}|a_h|r^h.
}
\tag{L-28401.3}
\]

Equation (L-28401.2) defines an upper-triangular coefficient operator `M_sigma` on this space.

For a source exponent `s=sigma+h`, the weighted absolute row sum is

\[
\begin{aligned}
m(s,r)
={}&1-\eta(s)\\
&+\sum_{\ell\ge1}
\frac{(s)_\ell}{\ell!}
2^{-s-\ell}\zeta(s+\ell)r^\ell.
\end{aligned}
\tag{L-28401.4}
\]

## 4. Uniform strict contraction

The alternating-series estimate gives

\[
1-\eta(s)\le2^{-s}.
\tag{L-28401.5}
\]

For `ell>=1` and `s>=1/2`,

\[
\zeta(s+\ell)\le\zeta(3/2)<3.
\]

Using

\[
\sum_{\ell\ge0}\frac{(s)_\ell}{\ell!}y^\ell
=(1-y)^{-s},
\]

and taking `r=1/4`,

\[
\begin{aligned}
m(s,1/4)
&\le2^{-s}
+3\,2^{-s}
\left[(1-1/8)^{-s}-1\right]\\
&=3(4/7)^s-2\,2^{-s}.
\end{aligned}
\tag{L-28401.6}

The right side decreases for `s>=1/2`. One elementary proof uses

\[
\log2<7/10,
\qquad
\log(7/4)>11/20,
\]

in its derivative. At the left endpoint,

\[
3(4/7)^{1/2}-2\,2^{-1/2}
=\frac6{\sqrt7}-\sqrt2
<\frac67.
\]

Consequently

\[
\boxed{
\|\mathscr C f\|_{\sigma,1/4}
\le\frac67\|f\|_{\sigma,1/4}
\qquad(\sigma\ge1/2).
}
\tag{L-28401.7}

This is a strict, endpoint-independent reserve for the complete shifted analytic bulk. It is not numerical reconnaissance and does not depend on zeta zeros.

## 5. Logarithmic companion

The critical analytic profile is generated from powers by

\[
x^{-s}\log(X/x)
=\log X\,x^{-s}+\partial_s x^{-s}.
\tag{L-28401.8}

The coefficient operator `M_s` is analytic for real `s>=1/2`. Differentiating

\[
M_s^j
\]

gives

\[
\partial_sM_s^j
=\sum_{a=0}^{j-1}
M_s^a(\partial_sM_s)M_s^{j-1-a}.
\tag{L-28401.9}

The same absolutely convergent majorants used above give one finite constant `C_1` with

\[
\|\partial_sM_s\|_{1/4}\le C_1
\qquad(s\ge1/2).
\]

Hence

\[
\boxed{
\|\mathscr C^j[x^{-s}\log(X/x)]\|_{s,1/4}
\le
\left[\log X+C_1j\right]
\left(\frac67\right)^{j-1}.
}
\tag{L-28401.10
}

The harmless convention at `j=0` is understood. Thus logarithmic Jordan growth is polynomial and is dominated by the strict analytic contraction.

## 6. Consequence for the repository proof graph

Every interior Taylor channel of the shifted central cascade is strictly contracting. Therefore a failure of DCCS cannot arise from:

```text
an uncontrolled analytic power tail;
a same-order shifted lattice term;
accumulation of logarithmic derivatives in the interior.
```

The only channels not covered by (L-28401.7) are those created by finite support and cutoff crossing. They are the **boundary jets** isolated in `L-28402/T-28401`.

This is the same boundary/commutator distinction independently exposed by:

- the Peano columns on PR #262;
- odd-column leakage and the physical boundary on PR #269;
- the endpoint collar on PR #279;
- WSTS's prime-sampling boundary remainder on PR #240.

## 7. Proof boundary

Closed here:

1. the exact shifted Dirichlet–Taylor formula;
2. positivity and triangularity of every faster-power channel;
3. the uniform `6/7` analytic contraction;
4. polynomially harmless logarithmic differentiation.

Not closed here:

1. finite cutoff boundary-jet propagation;
2. DCCS;
3. RH.
