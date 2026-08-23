# R-105202 — Subunit residue coherence is not the sharp last-defect gate

Claim ID: `R-105202`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-104500`, `L-104522`, `L-105212`  
RH status: **not assumed**

`ESDE105212` is a valid sufficient condition for eliminating every wrong
extremum, but it is much stronger than the actual sign theorem and must not be
presented as the canonical low-order target.

## 1. An exact real-rooted counterexample to subunit coherence

Put

\[
p(x)={x^5\over5}-7x^3-10x^2+{8\over5}.
\tag{R-105202.1}
\]

Then

\[
p'(x)=x(x+4)(x+1)(x-5),
\]

so the critical points are

\[
-4,-1,0,5.
\]

Their values and curvatures are

\[
\begin{array}{c|c|c}
c&p(c)&p''(c)\\ \hline
-4&424/5&-108\\
-1&-8/5&18\\
0&8/5&-20\\
5&-2492/5&270
\end{array}
\tag{R-105202.2}
\]

Thus every extremum has the correct sign. Since `p` is increasing or
decreasing strictly between the four displayed critical points, and its two
tails have opposite infinite signs, it has exactly five simple real zeros.
Equivalently, its wrong-extremum count is zero.

The derivative-ratio residues are nevertheless highly nonuniform:

\[
\boxed{
\rho=
\left(
-{106\over135},
-{4\over45},
-{2\over25},
-{1246\over675}
\right).
}
\tag{R-105202.3}
\]

Every residue is negative, so the sharp sign condition is already satisfied.
However, with

\[
R=4,
\qquad
M_1=-\sum_j\rho_j={14\over5},
\qquad
M_2=\sum_j\rho_j^2={1839932\over455625},
\]

the coherence is

\[
\mathfrak C={M_1^2\over RM_2}
={893025\over1839932},
\]

and hence

\[
\boxed{
R(1-\mathfrak C)
={946907\over459983}>2>1.
}
\tag{R-105202.4}
\]

Thus the subunit coherence condition fails by a large exact margin even
though the polynomial is completely real-rooted and has no wrong extremum.

## 2. Consequence for `ESDE105212`

The exact variance identity gives

\[
\sum_{i<j}(\rho_i-\rho_j)^2
=RM_2(1-\mathfrak C)>M_2.
\tag{R-105202.5}
\]

The exterior-square Gram quantity in `L-105212.9` is an upper bound for this
pairwise dispersion. Therefore it cannot satisfy

\[
\Lambda_{2a}(0)
\left[R\operatorname{tr}K^{(b)}-
\mathbf1^TK^{(b)}\mathbf1\right]<M_2
\]

for this benign real-rooted example.

Accordingly:

```text
ESDE105212 -> no wrong extremum       VALID SUFFICIENT IMPLICATION
ESDE105212 as the sharp/native gate   FALSE
coherence near one as necessary       FALSE
pointwise residue sign rho_c<=0       SHARP REAL-CRITICAL CONDITION
```

The correct continuation should isolate each residue sign directly and keep
the independent Levinson boundary remainder explicit. The exact Bezoutian and
Cauchy-remainder decompositions doing this are `L-105213--L-105214`.

## 3. Scope

This example does not refute the possibility that Xi might satisfy
`ESDE105212` in a special regime. It refutes the stronger methodological claim
that subunit global coherence is the intrinsic or necessary low-order
reverse–Rolle condition. A proof programme should not demand a condition that
fails for elementary completely real-rooted polynomials.