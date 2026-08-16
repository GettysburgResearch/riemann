# L-95171 — The dyadic root source has a positive coefficient-one two-channel Julia compiler

Claim ID: `L-95171`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95040/L-95041` at `b7ed54922cee0bb6a62fd189f0f83edd3ff7441a`; the root source `b_2=(epsilon-delta_2)*mu` isolated on PR #474  
Scope: multiplicative source and carry-current positivity; no scalar CRCTP or RH conclusion

## 1. Positive reciprocal and signed root state

Put

\[
G_2(s)={\zeta(s)\over1-2^{-s}}
      =\sum_{n\ge1}{g_2(n)\over n^s},
\qquad
B_2(s)={1\over G_2(s)}
      ={1-2^{-s}\over\zeta(s)}
      =\sum_{n\ge1}{b_2(n)\over n^s}.
\]

Writing `n=2^e m` with `m` odd gives

\[
\boxed{g_2(n)=e+1>0.}
\tag{L-95171.1}
\]

The signed inverse is

\[
\boxed{b_2=(\varepsilon-\delta_2)*\mu.}
\tag{L-95171.2}
\]

More explicitly, for odd squarefree `m`,

\[
b_2(m)=\mu(m),\qquad
b_2(2m)=-2\mu(m),\qquad
b_2(4m)=\mu(m),
\]

and all higher dyadic valuations vanish. Consequently

\[
\boxed{|b_2(n)|\le g_2(n).}
\tag{L-95171.3}
\]

Define the two positive channels

\[
\boxed{u_2^\pm(n)=g_2(n)\pm b_2(n)\ge0.}
\tag{L-95171.4}
\]

## 2. Positive generalized-prime compiler

Let

\[
-{G_2'(s)\over G_2(s)}
=\sum_{n\ge2}{\Lambda_2(n)\over n^s}.
\]

Then

\[
\Lambda_2(p^r)=\log p\quad(p\text{ odd}),
\qquad
\Lambda_2(2^r)=2\log2,
\tag{L-95171.5}
\]

and `Lambda_2(n)=0` off prime powers. In particular `Lambda_2>=0`.

The identities

\[
-G_2'=\left(-{G_2'\over G_2}\right)G_2,
\qquad
-B_2'=-\left(-{G_2'\over G_2}\right)B_2
\]

give coefficientwise

\[
g_2(n)\log n
=\sum_{\substack{d\mid n\\d>1}}
\Lambda_2(d)g_2(n/d),
\tag{L-95171.6}
\]

\[
b_2(n)\log n
=-\sum_{\substack{d\mid n\\d>1}}
\Lambda_2(d)b_2(n/d).
\tag{L-95171.7}
\]

Adding and subtracting yields the exact positive channel swap

\[
\boxed{
u_2^+(n)\log n
=\sum_{\substack{d\mid n\\d>1}}
\Lambda_2(d)u_2^-(n/d),
}
\tag{L-95171.8}
\]

\[
\boxed{
u_2^-(n)\log n
=\sum_{\substack{d\mid n\\d>1}}
\Lambda_2(d)u_2^+(n/d).
}
\tag{L-95171.9}
\]

Every source coefficient is spent exactly once. No signed child coefficient appears in the compiler.

## 3. Matrix Julia state

Define

\[
\boxed{
\Sigma_2(n)=
\begin{pmatrix}
g_2(n)&b_2(n)\\
b_2(n)&g_2(n)
\end{pmatrix}.
}
\tag{L-95171.10}
\]

Its eigenvalues are `u_2^+(n)` and `u_2^-(n)`, so

\[
\Sigma_2(n)\succeq0.
\tag{L-95171.11}
\]

For a split `e=(n,j)`, put

\[
\chi_e(q)=\left\lfloor{n\over q}\right\rfloor
-\left\lfloor{j\over q}\right\rfloor
-\left\lfloor{n-j\over q}\right\rfloor\in\{0,1\}.
\]

The complete matrix carry current is

\[
\boxed{
\mathcal J_2(e)=\sum_{q\ge2}\chi_e(q)\Sigma_2(q)\succeq0.
}
\tag{L-95171.12}
\]

Its trace is a positive generalized-prime reserve. Its off-diagonal entry is exactly the dyadic root-contact carry source which remains after scalar Pascal cycles and which produced the exact separator on PR #474.

Thus the irreducible scalar obstruction is embedded in a positive two-channel current rather than dominated by an unrelated absolute majorant.

## 4. Relation to the CRCTP reset

`L-95040` proves that dyadic root completion closes the signed interior span. `R-95040` proves that root neutrality does not imply scalar positive flow. The present theorem supplies a different positive object:

```text
scalar root target              signed / separated;
two-channel Julia state         positive semidefinite;
source transition               coefficient-one and positive;
carry observation               positive semidefinite.
```

The remaining task is not another generic scalar cone argument. It is to extract the off-diagonal critical current from the positive matrix state without paying the full trace.

## 5. Boundary

```text
positive reciprocal coefficients g_2       EXACT
root inverse b_2 and |b_2|<=g_2              EXACT
nonnegative generalized-prime source         EXACT
positive coefficient-one channel swap        EXACT
positive matrix carry current                 EXACT
trace-free scalar extraction                  OPEN
CRCTP / Cycle Debt                            OPEN
Riemann Hypothesis                            UNPROVED
```
