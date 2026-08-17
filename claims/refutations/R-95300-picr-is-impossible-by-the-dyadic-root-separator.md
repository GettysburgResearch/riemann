# R-95300 — PICR is impossible by the exact dyadic root separator

Claim ID: `R-95300`  
Status: **PROPOSED COMPLETE EXACT REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen parent: PR #562 at `9537096f498c7ee0ca2141394f43f0a2f704cce4`  
Scope: integer square-root hinges and carry realizations using only splits whose children are at least two

## 1. Root source

Put

\[
b_2=(\varepsilon-\delta_2)*\mu.
\]

Since \(1*\mu=\varepsilon\),

\[
1*b_2=\varepsilon-\delta_2.
\tag{R-95300.1}
\]

For real \(x\ge0\), define

\[
G_2(x)
=
\sum_{q\le x}b_2(q)\left\lfloor\frac{x}{q}\right\rfloor.
\]

Divisor switching gives

\[
\boxed{
G_2(0)=0,\qquad G_2(1)=1,\qquad G_2(x)=0\quad(x\ge2).
}
\tag{R-95300.2}
\]

For a split \(e=(n,j)\), \(n=j+k\), its carry column is

\[
\chi_e(q)
=
\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac kq\right\rfloor.
\]

If both children are at least two, then

\[
\boxed{
\sum_q b_2(q)\chi_e(q)
=
G_2(n)-G_2(j)-G_2(k)
=
0.
}
\tag{R-95300.3}
\]

Therefore every signed interior carry flow, not merely every nonnegative one,
has zero \(b_2\)-response.

## 2. The critical hinge has nonzero response

For an integer endpoint \(T\ge2\), put

\[
h_T(q)
=
q^{-1/2}-T^{-1/2},
\qquad 2\le q\le T,
\]

and define

\[
\rho_T
=
\sum_{q=2}^{T}
b_2(q)
\left(q^{-1/2}-T^{-1/2}\right).
\tag{R-95300.4}
\]

Write \(q=2^em\), \(m\) odd. Then

\[
b_2(2^em)=
\begin{cases}
\mu(m),&e=0,\\
-2\mu(m),&e=1,\\
\mu(m),&e=2,\\
0,&e\ge3.
\end{cases}
\tag{R-95300.5}
\]

The values vanish unless \(m\) is squarefree.

Let \(\operatorname{sf}(n)\) be the squarefree kernel. Square roots of distinct
squarefree integers are linearly independent over \(\mathbb Q\).

If \(\operatorname{sf}(T)\ne2\), the only nonzero \(b_2(q)\) term in
(R-95300.4) with radical \(\sqrt2\) is \(q=2\), and its coefficient is

\[
\frac{b_2(2)}{\sqrt2}=-\sqrt2.
\]

The endpoint term has radical \(\sqrt{\operatorname{sf}(T)}\), so it cannot
cancel this coefficient.

If \(\operatorname{sf}(T)=2\) and \(T\ge7\), then \(T\ge8\). The only nonzero
\(b_2(q)\) term with radical \(\sqrt6\) is \(q=6\), and

\[
\frac{b_2(6)}{\sqrt6}
=
\frac{\sqrt6}{3}.
\]

The endpoint term again lies in the \(\sqrt2\) radical class.

Hence

\[
\boxed{\rho_T\ne0\qquad(T\ge7).}
\tag{R-95300.6}
\]

## 3. Refutation

Every signed interior realization would have zero \(b_2\)-response by
(R-95300.3), while the critical hinge has response \(\rho_T\ne0\). Therefore

\[
\boxed{
T\ge7
\Longrightarrow
h_T\text{ has no signed interior realization.}
}
\tag{R-95300.7}
\]

A fortiori the `PICR` statement in `T-95270` is false.

This refutation does not affect:

```text
the 5:3 bottom-contact identity;
the positive Julia compression;
the scalar interval on the positive two-leaf cone.
```

It refutes only the proposed entry of the unmodified hinge into the
root-free interior cone.
