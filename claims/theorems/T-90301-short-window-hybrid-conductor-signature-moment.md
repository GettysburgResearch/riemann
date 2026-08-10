# T-90301 — Short-window and hybrid-conductor extension of the signature-moment theorem

Claim ID: `T-90301`  
Status: **PROPOSED COMPLETE UNIFORM THEOREM — ANALYTIC REVIEW AND LEAN PORT REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Anthropic zeta-23 Theorems A--E and their prime-side proof, the uniform Riemann--von Mangoldt/local-count estimates for primitive Dirichlet \(L\)-functions, `L-90301` only for the frontier discussion  
Scope: unconditional zero-proportion theorem in polynomial short windows and polynomial conductor; not a proof of RH

## 1. Counts

Let \(\chi\) be primitive modulo \(q\ge2\). For \(1\le H\le T\), let

\[
N_\chi(T,T+H)
 :=\sum_{\rho:\,T<\Im\rho\le T+H}m_\rho,
\]

where \(\rho\) ranges over the nontrivial zeros of \(L(s,\chi)\). Let

- \(N^*_{0,\chi}(T,T+H)\) count distinct zeros on \(\Re s=1/2\);
- \(N^s_{0,\chi}(T,T+H)\) count simple zeros on that line;
- \(N_{d,\chi}(T,T+H)\) count all distinct zeros.

The same notation with the subscript omitted refers to \(\zeta\). The zeta case is included separately because its explicit formula has the pole term.

For \(0<\lambda\le1\), put

\[
c^*_{\lambda}
 :=\frac{\sqrt2\tan(\lambda/\sqrt2)}
 {1+(\lambda/\sqrt2)\tan(\lambda/\sqrt2)},
\tag{T-90301.1}
\]

\[
S(\lambda):=\max\!\left(0,2-\frac1{c^*_{\lambda}}\right),
\qquad
D(\lambda):=\max\!\left(c^*_{\lambda},\frac{3-1/c^*_{\lambda}}2\right).
\tag{T-90301.2}
\]

## 2. Adaptive theorem

Fix \(\alpha\in(0,1]\) and \(\theta\ge0\). Uniformly for

\[
T^\alpha\le H\le T,
\qquad
q\le T^\theta,
\]

set

\[
L:=\log\frac{H}{2\pi},
\qquad
\ell_{\chi}:=\log\frac{qT}{2\pi},
\qquad
\lambda_{T,H,q}:=\frac{L}{\ell_{\chi}}.
\tag{T-90301.3}
\]

For sufficiently large \(T\), \(0<\lambda_{T,H,q}\le1\). Then

\[
\boxed{
\frac{N^*_{0,\chi}(T,T+H)}{N_\chi(T,T+H)}
\ge
S(\lambda_{T,H,q})-o_{\alpha,\theta}(1),
}
\tag{T-90301.4}
\]

\[
\boxed{
\frac{N^s_{0,\chi}(T,T+H)}{N_\chi(T,T+H)}
\ge
S(\lambda_{T,H,q})-o_{\alpha,\theta}(1),
}
\tag{T-90301.5}
\]

and

\[
\boxed{
\frac{N_{d,\chi}(T,T+H)}{N_\chi(T,T+H)}
\ge
D(\lambda_{T,H,q})-o_{\alpha,\theta}(1).
}
\tag{T-90301.6}
\]

The error is uniform over the displayed range and may be taken conservatively as

\[
O_{\alpha,\theta}\!\left(
\frac{\log\ell}{\ell}+\frac{\ell^4}{\sqrt H}
\right),
\qquad
\ell:=\log(qT+3).
\tag{T-90301.7}
\]

The same statements hold for \(\zeta\) with \(q=1\), including the pole density in the explicit formula.

## 3. Uniform worst-case corollary

The function \(c^*_{\lambda}\) is strictly increasing. Indeed, with

\[
a=\lambda/\sqrt2,
\]

a direct differentiation gives

\[
\frac{d}{d\lambda}c^*_{\lambda}
=\frac1{(1+a\tan a)^2}>0.
\tag{T-90301.8}
\]

Since

\[
\lambda_{T,H,q}
\ge \frac{\alpha}{1+\theta}-O_{\alpha,\theta}\!\left(\frac1{\log T}\right),
\]

putting

\[
\lambda_{\alpha,\theta}:=\frac{\alpha}{1+\theta}
\tag{T-90301.9}
\]

gives the uniform lower bounds

\[
\frac{N^*_{0,\chi}}{N_\chi},
\frac{N^s_{0,\chi}}{N_\chi}
\ge S(\lambda_{\alpha,\theta})-o_{\alpha,\theta}(1),
\tag{T-90301.10}
\]

\[
\frac{N_{d,\chi}}{N_\chi}
\ge D(\lambda_{\alpha,\theta})-o_{\alpha,\theta}(1).
\tag{T-90301.11}
\]

At \((\alpha,\theta)=(1,0)\), this recovers the imported constants

\[
S(1)=0.6725007036\ldots,
\qquad
D(1)=0.8362503518\ldots .
\]

For \(H=T\) and \(q\le T^\theta\), this turns the heuristic hybrid-conductor remark in the imported paper into a uniform proposed theorem. For fixed \(q\) and \(H=T^\alpha\), it gives a polynomial short-window theorem.

## 4. Positivity threshold

The on-line/simple constant is positive exactly when \(c^*_{\lambda}>1/2\). There is one threshold

\[
\lambda_{\mathrm{crit}}
=0.5501939647441547\ldots,
\tag{T-90301.12}
\]

determined by

\[
\tan(\lambda/\sqrt2)
\left(2\sqrt2-\lambda/\sqrt2\right)=1.
\]

Thus the uniform on-line/simple result is nonvacuous whenever

\[
\frac{\alpha}{1+\theta}>0.5501939647\ldots .
\tag{T-90301.13}
\]

At full window length \(\alpha=1\), this permits

\[
\theta<0.8175408384659566\ldots .
\tag{T-90301.14}
\]

The distinct-zero branch remains positive below this threshold through the Cauchy term \(c^*_{\lambda}\).

## 5. Proof

### 5.1 Endpoint-safe Gabor family

Take

\[
X=e^L=\frac{H}{2\pi},
\qquad
h=\frac{2\pi}{L},
\qquad
\tau_k=T+kh,
\]

with \(0\le k<d:=\lfloor H/h\rfloor\). Use the imported optimal profile

\[
v_{\lambda}(s)=\cos(\sqrt2\lambda s),
\qquad |s|\le\frac12,
\]

and the same fixed-width smooth endpoint ramp. Because \(\lambda\) stays in a compact subinterval of \((0,1]\), all taper norms used in the tail and end-effect estimates are uniform in \(q,H,T\).

The support of every test function lies in \([-L/2,L/2]\), so the explicit formula uses only prime powers \(n\le X\le H\). This is the entire short-window/conductor budget.

### 5.2 Zero side

The functional equation and Schwarz reflection preserve the zero multiset of a fixed primitive \(L(s,\chi)\) under

\[
\rho\longmapsto1-\overline\rho.
\]

Therefore the imported block decomposition is unchanged:

- a distinct on-line point gives a positive rank-one form;
- an off-line pair gives a pullback of a signature-\((1,1)\) block.

Let

\[
I=[T,T+H],
\qquad
I'=(T-H^{1/2},T+H+H^{1/2}].
\]

The uniform local count

\[
N_\chi(t+1)-N_\chi(t)\ll\log(q(t+3))
\]

and two integrations by parts in the tapered Fourier transform give

\[
\|E_{\mathrm{far}}/L\|
\ll \frac{X^{1/2}\ell}{H}
\ll \frac{\ell}{\sqrt H}.
\tag{T-90301.15}
\]

The boundary count is

\[
N_\chi(I'\setminus I)\ll H^{1/2}\ell=o(N_\chi(I)),
\tag{T-90301.16}
\]

since

\[
N_\chi(I)\asymp H\ell.
\]

Hence Propositions 4.1, 4.4, and 4.5 of the imported proof hold uniformly after replacing the dyadic interval length \(T\) by \(H\).

### 5.3 First trace

Poisson summation on the completed grid still gives

\[
\sum_{k\in\mathbb Z}
|\widehat\phi(\tau-\tau_k)|^2
=L\int\phi^2.
\]

The gamma density is essentially constant on the mean-spacing scale and its integral over \(I\) equals the Riemann--von Mangoldt main term. The prime and pole pieces contribute only boundary-size errors. Uniformly,

\[
\operatorname{tr}\widetilde G
=aL\,N_\chi(T,T+H)
\left(1+O_{\alpha,\theta}\!\left(
\frac1L+\frac{\ell^2}{\sqrt H}
\right)\right).
\tag{T-90301.17}
\]

No character orthogonality is used.

### 5.4 Second trace: diagonal

For a primitive character,

\[
|\chi(n)|^2=\mathbf1_{(n,q)=1}.
\]

Thus the prime diagonal is the zeta diagonal with the Euler factors dividing \(q\) omitted. The total omitted mass satisfies

\[
\begin{aligned}
\sum_{p\mid q}\sum_{k\ge1}
\frac{(\log p)^2}{p^k}\,g(k\log p)
&\le L\sum_{p\mid q}\frac{(\log p)^2}{p-1}\\
&\le L\sum_{p\mid q}\log p\\
&\le L\log q.
\end{aligned}
\tag{T-90301.18}
\]

Here \(\log p\le p-1\). Since the full diagonal has size \(L^3\), the conductor omission is relatively

\[
O\!\left(\frac{\log q}{L^2}\right)
=O_{\alpha,\theta}(1/\log T).
\tag{T-90301.19}
\]

The limiting diagonal is therefore the same scalar functional as for zeta.

### 5.5 Second trace: off diagonal and end effects

The Montgomery--Vaughan generalized Hilbert inequality applies to the frequencies \(\log n\), with the character phases absorbed into coefficients of unchanged modulus. The off-diagonal term is

\[
O(L^2X)=O(L^2H),
\tag{T-90301.20}
\]

whereas the prime diagonal is of size \(HL^3\). Hence the relative error is \(O(1/L)\), including the endpoint \(X\asymp H\).

The finite-grid end effects are the same completed-kernel subtraction as upstream. Replacing the interval length by \(H\) gives the relative bound

\[
O_{\alpha,\theta}\!\left(
\frac{(\ell^2+X)\log\ell}{H\ell}
\right)
=O_{\alpha,\theta}\!\left(
\frac{\log\ell}{\ell}+\frac{\ell\log\ell}{H}
\right).
\tag{T-90301.21}
\]

The mixed gamma/prime and pole terms are smaller. Combining (T-90301.18)--(T-90301.21),

\[
\frac{(\operatorname{tr}\widetilde G)^2}
 {\operatorname{tr}(\widetilde G^2)}
=c^*_{\lambda_{T,H,q}}
N_\chi(T,T+H)
\left(1+o_{\alpha,\theta}(1)\right).
\tag{T-90301.22}
\]

The more conservative master error (T-90301.7) absorbs every displayed remainder.

### 5.6 Assembly

Normalize so that one isolated simple on-line zero contributes eigenvalue one. The imported rank--trace inequality gives

\[
N^*_{0,\chi},\ N^s_{0,\chi}
\ge
\left(2-\frac1{c^*_{\lambda}}-o(1)\right)N_\chi.
\]

The same multiplicity regrouping gives

\[
N_{d,\chi}
\ge
\left(\frac{3-1/c^*_{\lambda}}2-o(1)\right)N_\chi.
\]

Thresholded Cauchy--Schwarz gives the additional distinct bound

\[
N_{d,\chi}
\ge(c^*_{\lambda}-o(1))N_\chi.
\]

Taking the nonnegative/maximal branches proves (T-90301.4)--(T-90301.6). Monotonicity (T-90301.8) gives the uniform corollary.

## 6. Numerical instances

The finite diagnostic replay gives:

| \(\alpha\) | \(\theta\) | \(\lambda=\alpha/(1+\theta)\) | on-line and simple | distinct |
|---:|---:|---:|---:|---:|
| 1.00 | 0.00 | 1.000000 | 0.672501 | 0.836250 |
| 0.90 | 0.00 | 0.900000 | 0.593102 | 0.796551 |
| 0.75 | 0.00 | 0.750000 | 0.419075 | 0.709538 |
| 0.60 | 0.00 | 0.600000 | 0.134554 | 0.567277 |
| 1.00 | 0.10 | 0.909091 | 0.601315 | 0.800658 |
| 1.00 | 0.25 | 0.800000 | 0.486267 | 0.743134 |
| 1.00 | 0.50 | 0.666667 | 0.279459 | 0.639730 |
| 1.00 | 0.75 | 0.571429 | 0.060577 | 0.530288 |
| 0.75 | 0.25 | 0.600000 | 0.134554 | 0.567277 |

## 7. Review checklist

A reviewer should verify, in this order:

1. the interval-length replacement in every occurrence of the upstream end-effect bound;
2. the uniform local zero count and Riemann--von Mangoldt error in \(q\);
3. the missing-Euler-factor estimate (T-90301.18);
4. uniform taper norms when \(\lambda\) varies;
5. the endpoint Montgomery--Vaughan ratio \(X/H\asymp1\);
6. the zeta pole term when \(q=1\);
7. the exact error claimed in (T-90301.7).

## 8. Exact boundary

```text
imported dyadic fixed-conductor theorem             FORMALIZED UPSTREAM
co-lattice multiwindow collapse                     PROPOSED COMPLETE EXACT
short-window/hybrid conductor trace asymptotics     PROPOSED COMPLETE UNIFORM
short-window/hybrid proportion theorem              PROPOSED COMPLETE UNIFORM
independent analytic review                         REQUIRED
Lean formalization of the extension                 NOT STARTED
Riemann Hypothesis                                   UNPROVED
```
