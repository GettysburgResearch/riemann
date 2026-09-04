# Countercheck of the Proposition 9.5 height argument

```text
Verdict: the proof of Proposition 9.5 in arXiv:2609.04176v1 is invalid
Scope: equations (3.5), (4.1), (4.5), (5.24), (6.17)-(6.19), and (9.1)
Claim established here: the max-summand majorant used in the paper retains a
positive (rho^2/2) B^2 log B term
Claim not established here: Catalan's constant is rational
Mathematical status after this review: irrationality remains unresolved
```

## 1. The exact majorant used by the paper

Put

\[
\mathcal P_B:=\prod_{i=0}^{N-1}\Pi_i,
\qquad S=\lfloor \rho B\rfloor.
\]

Combining the fixed-scalar identity (3.5), the positive-part denominator
bound (5.24), and the Cauchy--Binet expansion (4.1), the proof of Proposition
9.5 passes to the majorant

\[
\begin{aligned}
\mathcal M_B:=
&\sum_{\substack{p\ \mathrm{odd}\\\nu\ge1}}
  \bigl(a_{p^\nu,B}-m^A_{p^\nu,B}\bigr)\log p
 +\log F_B-\log\mathcal P_B \\
&\quad +\max_{|I|=S}\bigl(\log|\Xi_I|-S\log q\bigr).
\end{aligned}
\tag{H1}
\]

The additional cost of replacing the absolute value of the sum by its largest
absolute summand is at most

\[
\log\binom NS=O(B),
\]

which is irrelevant at both the `B^2 log B` and `B^2` scales. Thus the first
paragraph of Proposition 9.5 can only prove its conclusion by showing that
`M_B` has the asserted negative quadratic upper bound.

The calculation below shows instead that

\[
\boxed{
\mathcal M_B\ge
\frac{\rho^2}{2}B^2\log B-O_\rho(B^2).
}
\tag{H2}
\]

In particular, for the paper's choice `rho=1/20`,

\[
\mathcal M_B\ge
\frac1{800}B^2\log B-O(B^2).
\tag{H3}
\]

Therefore this max-summand route cannot yield equation (9.3).

## 2. A compulsory Cauchy--Binet term

Take

\[
I_0:=\{0,1,\ldots,S-1\}.
\]

For every selected row set

\[
A\subseteq\{0,\ldots,S+2\},\qquad |A|=S,
\]

the Pascal minor

\[
D_A:=\det\!\left[\binom{2B+a}{i}\right]_{
 a\in A,\ 0\le i<S}
\]

is nonzero. Indeed, the polynomials

\[
1,\binom{x}{1},\ldots,\binom{x}{S-1}
\]

form a basis of the polynomials of degree below `S`; their evaluation matrix
at the distinct integers `2B+a` is invertible. Since `D_A` is an integer,

\[
|D_A|\ge1.
\tag{H4}
\]

The Cauchy minor on `I_0` and `J={1,...,S}` is also nonzero, and every tail is
positive. Hence `Xi_{I_0}` is a nonzero summand. The factorization preceding
(4.1) gives the exact absolute identity

\[
\frac{|\Xi_{I_0}|}{q^S}
=|D_A|\,|C_{I_0,J}|
 \prod_{i=0}^{S-1}T_{i+1}\Pi_i,
\tag{H5}
\]

where

\[
C_{I_0,J}=\left[\frac1{2(i+j)+1}\right]_{
0\le i<S,\ 1\le j\le S}.
\]

There is a sign/index inconsistency earlier in the paper: recurrence (2.3)
literally produces `T_i`, while the displayed residual formula and (4.5) use
`T_{i+1}` with the wrong global column sign. Reindexing the recurrence repairs
this by replacing `(-1)^j T_{i+1}` with `(-1)^{j-1} T_{i+1}`. That repair does
not affect (H5) in absolute value or any leading-order calculation below.

## 3. Exact cancellation of the `a_Q` layer

Because every `Pi_i` is odd and, after repairing the undefined symbol in
Section 3, `D=2B`, equation (5.13) gives

\[
\sum_{\substack{p\ \mathrm{odd}\\\nu\ge1}}
 a_{p^\nu,B}\log p
+\log F_B-\log\mathcal P_B
=v_2(F_B)\log2.
\tag{H6}
\]

Substitute the single term (H5) into (H1) and apply (H6). This yields

\[
\begin{aligned}
\mathcal M_B\ge{}&
 v_2(F_B)\log2
-\sum_{\substack{p\ \mathrm{odd}\\\nu\ge1}}
 m^A_{p^\nu,B}\log p
+\log|D_A|+\log|C_{I_0,J}|\\
&+\sum_{i=0}^{S-1}\log\Pi_i
+\sum_{i=0}^{S-1}\log T_{i+1}.
\end{aligned}
\tag{H7}
\]

This identity exposes the missing leading term directly. The `a_Q` baseline
really does cancel, but the product of the clearing factors carried by the
specific nonzero Cauchy--Binet term does not.

## 4. Size of the compulsory term

### 4.1 Selected clearing factors

Uniformly for fixed `rho in (0,1)`,

\[
\begin{aligned}
\sum_{i=0}^{S-1}\log\Pi_i
&=2\sum_{i=0}^{S-1}\sum_{h=1}^{B}
   \log\bigl(2(i+h)+1\bigr)\\
&=2\rho B^2\log B+O_\rho(B^2).
\end{aligned}
\tag{H8}
\]

This follows by extracting `log B` from each of the `SB` factors; the remaining
Riemann sum has finite size `O(B^2)`.

### 4.2 Cauchy determinant

Cauchy's formula gives

\[
|C_{I_0,J}|=
\frac{2^{S(S-1)}V(I_0)V(J)}
 {\prod_{0\le i<S}\prod_{1\le j\le S}(2(i+j)+1)}.
\]

The `S^2 log S` contributions of the two Vandermondes and the denominator
cancel. Stirling summation therefore gives the two-sided estimate

\[
\log|C_{I_0,J}|=O_\rho(B^2).
\tag{H9}
\]

In particular it cannot cancel a `B^2 log B` term.

### 4.3 Tails

The alternating-series estimate supplies the explicit lower bound

\[
T_m>
\frac1{(2m+1)^2}-\frac1{(2m+3)^2}
=\frac{8(m+1)}{(2m+1)^2(2m+3)^2}.
\]

Consequently

\[
\sum_{i=0}^{S-1}\log T_{i+1}
\ge -O_\rho(B\log B).
\tag{H10}
\]

Also `log|D_A|>=0` by (H4), and `v_2(F_B)log 2>=0`.

## 5. The paper's own small-prime singular coefficient

Section 6 defines the limiting ideal local layer and obtains

\[
L_\rho(t)=\frac{A_\rho}{t}+O_\rho(1),
\qquad
A_\rho=2\rho-\frac{\rho^2}{2}.
\tag{H11}
\]

This is not an external reinterpretation: it is exactly equations
(6.17)--(6.19), subsequently invoked in the proof of Proposition 9.5.
Together with (9.1), it entails

\[
\sum_{\substack{p\ \mathrm{odd}\\p^\nu\le S}}
 m^{(0)}_{p^\nu,B}\log p
=A_\rho B^2\log B+O_\rho(B^2).
\tag{H12}
\]

The middle and large ranges contribute only `O(B^2)`, and the higher powers
above `S` are declared `o(B^2)` in Section 8. Granting Lemma 5.5, the passage
from the ideal model to the selected-row model changes the weighted sum by
only `o(B^2)`. Thus the very asymptotic package used by Proposition 9.5 gives

\[
\sum_{\substack{p\ \mathrm{odd}\\\nu\ge1}}
 m^A_{p^\nu,B}\log p
=A_\rho B^2\log B+O_\rho(B^2).
\tag{H13}
\]

If (H12)--(H13) are not available uniformly, then Proposition 9.5 already
lacks its stated asymptotic input. If they are granted, they produce the
contradiction below.

## 6. The uncancelled leading coefficient

Insert (H8)--(H10) and (H13) into (H7):

\[
\begin{aligned}
\mathcal M_B
&\ge
\bigl(2\rho-A_\rho\bigr)B^2\log B-O_\rho(B^2)\\
&=
\frac{\rho^2}{2}B^2\log B-O_\rho(B^2).
\end{aligned}
\]

At `rho=1/20`,

\[
2\rho=\frac{80}{800},
\qquad
A_\rho=\frac{79}{800},
\qquad
2\rho-A_\rho=\frac1{800}.
\]

Hence

\[
\frac{\mathcal M_B}{B^2}\longrightarrow+\infty.
\tag{H14}
\]

This is incompatible with the sentence in Proposition 9.5 asserting that the
`B^2 log B` terms in this largest-summand majorant cancel and leave the finite
quadratic coefficient

\[
\frac{39}{200}+c_{\rm odd}-\Lambda_{\rm mid}-\frac{83}{2400}.
\]

The missing 178-cell and 235-cell certificates cannot repair a wrong leading
order: they affect the finite `B^2` coefficient, whereas (H14) is a positive
`B^2 log B` obstruction.

## 7. Logical scope of the finding

This countercheck establishes that the **published proof of Proposition 9.5**
does not work. It does not produce a rationality proof for Catalan's constant,
and it does not logically falsify the conditional statement of Proposition
9.5 independently of its proof: under the paper's desired conclusion the
rationality premise is false.

A possible repair would require genuinely new mathematics, for example:

1. retain and prove cancellation among the signed Cauchy--Binet summands,
   rather than replacing their sum by the largest absolute term;
2. prove an additional common numerator divisor whose singular coefficient is
   at least `2rho`, and attach it to the same scalar;
3. redesign the weights or completion so the selected clearing-factor tax is
   absent;
4. construct a different scalar with a complete product-formula ledger.

None of these steps appears in arXiv:2609.04176v1. Therefore the correct
repository status is:

```text
posted proof: invalid as written
Catalan irrationality theorem: not established by this preprint
Catalan irrationality problem: still open pending a corrected proof
```
