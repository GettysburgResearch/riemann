# L-100020 — Finite Euler squaring gives a pole-preserving positivity corridor

Claim ID: `L-100020`  
Status: **PROVED UNCONDITIONAL FINITE-CUTOFF THEOREM**  
Created: 2026-08-20  
Base: PR #670 at `f5d37a5f1880749dd33b103d98e2d85bac60ae28`  
RH status: **not assumed**

Put

\[
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1},
\qquad
\beta=(\varepsilon-\delta_{67})*\mu,
\]

and

\[
h(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}T(X/n).
\tag{L-100020.1}
\]

Its Dirichlet source is

\[
\sum_{n\ge1}\frac{\beta(n)}{n^z}
=
\frac{1-67^{-z}}{\zeta(z)}.
\tag{L-100020.2}
\]

For a finite cutoff \(Z\ge67\), define

\[
\boxed{
\mathscr A_Z=
( I+67^{-1/2}S_{67})^2
\prod_{\substack{p\le Z\\p\ne67}}
( I+p^{-1/2}S_p),
}
\tag{L-100020.3}
\]

where \(S_af(X)=f(X/a)\), with zero extension below one.

## 1. Exact completed source

In the variable \(z=s+\tfrac12\), multiplication by \(\mathscr A_Z\) changes
the source exactly into

\[
\boxed{
(1-67^{-2z})^2
\prod_{\substack{p\le Z\\p\ne67}}(1-p^{-2z})
\prod_{p>Z}(1-p^{-z}).
}
\tag{L-100020.4}
\]

Thus the completed labelled source consists of

- one label of cost \(p^2\) for each prime \(p\le Z\), \(p\ne67\);
- two labelled copies of cost \(67^2\);
- one label of cost \(p\) for each prime \(p>Z\).

A label of cost \(q\) has activity \(q^{-1/2}\).

For a labelled subset \(A\), write

\[
Q_A=\prod_{i\in A}q_i,
\qquad
r_A=Q_A^{-1/2},
\]

and define

\[
M_k(X)=\sum_{\substack{A\\|A|=k}}r_AT(X/Q_A)\ge0.
\tag{L-100020.5}
\]

Then

\[
(\mathscr A_Zh)(X)=\sum_{k\ge0}(-1)^kM_k(X).
\tag{L-100020.6}
\]

All sums are finite at fixed \(X\).

## 2. Exact level contraction

For every \(q>1\) and \(y\ge1\),

\[
q^{-1}T(y)-q^{-1/2}T(y/q)
=
3(q^{-1/2}-q^{-1})>0,
\tag{L-100020.7}
\]

where the second term is interpreted as zero when \(y<q\). Therefore

\[
q^{-1/2}T(y/q)\le q^{-1}T(y).
\tag{L-100020.8}
\]

Double-counting pairs \((A,i)\) with \(i\in A\) gives

\[
\boxed{
kM_k(X)\le \Sigma_{Z,X}M_{k-1}(X),
}
\tag{L-100020.9}
\]

where

\[
\Sigma_{Z,X}
=
\sum_{\substack{p\le Z\\p^2\le X}}\frac1{p^2}
+
\mathbf1_{67^2\le X}\frac1{67^2}
+
\sum_{Z<p\le X}\frac1p.
\tag{L-100020.10}
\]

Consequently

\[
M_k(X)\le \frac{\Sigma_{Z,X}^k}{k!}T(X).
\tag{L-100020.11}
\]

## 3. Uniform corridor

Assume

\[
\log Z\ge90,
\qquad
1\le X\le Z^{10/9}.
\tag{L-100020.12}
\]

The elementary bound \(\pi(t)\le2t/\log t\), valid for all sufficiently large
\(t\), and partial summation give

\[
\sum_{Z<p\le Z^{10/9}}\frac1p
\le
\frac{2}{\log(Z^{10/9})}
+
2\log\frac{\log(Z^{10/9})}{\log Z}
<
\frac1{50}+\frac29.
\tag{L-100020.13}
\]

Also

\[
\sum_p\frac1{p^2}
\le
\frac14+\sum_{m\ge1}\frac1{(2m+1)^2}
=
\frac{\pi^2}{8}-\frac34
<
\frac{95}{196},
\tag{L-100020.14}
\]

using \(\pi<22/7\). Hence

\[
\Sigma_{Z,X}
<
\frac{95}{196}
+\frac1{4489}
+\frac1{50}
+\frac29
=
\frac{143947973}{197964900}
<
\frac34.
\tag{L-100020.15}
\]

From (L-100020.6) and (L-100020.11),

\[
\begin{aligned}
(\mathscr A_Zh)(X)
&\ge M_0(X)-\sum_{j\ge0}M_{2j+1}(X)\\
&\ge \bigl(1-\sinh\Sigma_{Z,X}\bigr)T(X).
\end{aligned}
\tag{L-100020.16}
\]

The Taylor series, with a geometric ratio bound on its tail, gives

\[
\sinh(3/4)<5/6.
\tag{L-100020.17}
\]

Therefore

\[
\boxed{
(\mathscr A_Zh)(X)
>
\frac16(4\sqrt X-3)>0
\qquad
(1\le X\le Z^{10/9}).
}
\tag{L-100020.18}
\]

This positivity is unconditional and uses no RH-scale cancellation estimate.
