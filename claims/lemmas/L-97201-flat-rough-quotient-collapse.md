# L-97201 — Every accumulated rough history collapses to one flat quotient packet

Claim ID: `L-97201`  
Status: **PROVED EXACT FINITE ALGEBRA**  
Created: 2026-08-17  
Depends on: `L-97200`  
RH status: **not assumed**

Let \(R\) be any finite set of primes at least 67 and let

\[
\mu_R=\mathop{*}_{p\in R}(\delta_1-\delta_p).
\]

For an integer \(n\), write uniquely

\[
n=rm,
\qquad r\mid\prod_{p\in R}p,
\qquad (m,\prod_{p\in R}p)=1.
\tag{L-97201.1}
\]

The product \(r\) is the complete accumulated rough colour. Its sign is
\(\mu(r)=(-1)^{\omega(r)}\).

## 1. Exact 5:3 collapse

If \(r>1\), divisor convolution gives

\[
(q_* *\mu_R)(rm)=\sum_{e\mid r}\mu(e)q_*(rm/e).
\tag{L-97201.2}
\]

Since \(q_*\) is identically six from index five onward, the sum vanishes for
all quotients except \(m=1,2,4\). Precisely,

\[
\boxed{
(q_* *\mu_R)(rm)=
\begin{cases}
-6\mu(r),&m=1,\\
 9\mu(r),&m=2,\\
-3\mu(r),&m=4,\\
0,&m\notin\{1,2,4\}.
\end{cases}}
\tag{L-97201.3}
\]

Thus every nonempty rough history, regardless of its length, is one three-knot
packet

\[
\mu(r)(-6,9,-3)
\quad\text{at}\quad r,2r,4r.
\tag{L-97201.4}
\]

No recursive parity label remains implicit.

## 2. Exact boundary-null collapse

For \(q_\partial\), the same calculation uses its constant tail from index
three. If \(r>1\),

\[
\boxed{
(q_\partial *\mu_R)(rm)=
\begin{cases}
-\mu(r),&m=1,\\
\sqrt2\,\mu(r),&m=2,\\
0,&m\ge3.
\end{cases}}
\tag{L-97201.5}
\]

Every nonempty rough history is therefore one two-knot packet

\[
\mu(r)(-1,\sqrt2)
\quad\text{at}\quad r,2r.
\tag{L-97201.6}
\]

## 3. Meaning of the theorem

Equations (L-97201.3) and (L-97201.5) are the exact accumulated-parity
replacement for the leafwise first-owner tree. They prove simultaneously:

```text
one coefficient per complete rough colour       yes
history parity                                  mu(r)
no duplicate first owner                        automatic
no parity reset                                 attempted nowhere
no individual oriented child promoted           yes
finite versus grouped issue                      explicit
```

The theorem does not prove that the sum over all rough colours is nonnegative.
It removes a false compositional interface and replaces it by one exact global
Fourier coefficient.
