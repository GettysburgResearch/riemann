# R-29002 — Rowwise Selberg reserve is not source-cone coercivity

Claim ID: `R-29002`  
Title: The ordinary Selberg–Kummer row inequality is not homogeneous under source amplitudes, and its naive opposite-parity generalized-prime lift fails at the exact row `(n,j)=(6,2)`  
Status: **EXACT SCOPE REFUTATION; ORDINARY `L-29002` RETAINED**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Frozen target: PR #297 before this correction, head `99ab5a6264762d428dfea09d8d246a73b5458c33`  
Dependencies: `L-29002`; PR #269 `L-26903/L-26904`; finite exact carry algebra  
Scope: refutes two automatic source-lifting steps; it does not refute the ordinary row theorem or a future coupled source matrix

## 1. The ordinary theorem and the missing homogeneity

For one ordinary binomial carry row put

\[
 F_n(j)=\sum_q\Lambda(q)\chi_{n,q}(j)=\log\binom nj
\]

and

\[
 S_n(j)=\sum_d[\Lambda(d)\log d+(\Lambda*\Lambda)(d)]
                 \chi_{n,d}(j).
\]

`L-29002` proves exactly

\[
 F_n(j)^2-S_n(j)\ge0.
\tag{R-29002.1}
\]

This statement is correct.  It is not a conic statement in the row amplitude.
If the row is multiplied by a scalar `alpha>0`, the corresponding quadratic
minus linear expression is

\[
 \alpha^2F_n(j)^2-\alpha S_n(j).
\tag{R-29002.2}
\]

For every row with `S_n(j)>0`, (R-29002.2) is negative for all sufficiently
small positive `alpha`.

There is an exact elementary control at

\[
 (n,j)=(4,2),\qquad \alpha=\frac12.
\]

Here

\[
 F_4(2)=\log6,
\qquad
 S_4(2)=\log^23+3\log^22.
\]

Therefore

\[
\begin{aligned}
4\left[
 \frac14F_4(2)^2-rac12S_4(2)
\right]
&=\log^26-2\log^23-6\log^22\\
&=-\log^2(3/2)-4\log^22<0.
\end{aligned}
\tag{R-29002.3}
\]

Consequently a proof may not pass from the diagonal row inequalities of
`L-29002` to an arbitrary positive source superposition without constructing
the complete quadratic source Gram and its linear forcing in the same
normalization.

## 2. Exact failure of the generalized-prime pointwise lift

Retain the opposite-parity generalized von Mangoldt sequence

\[
 \Lambda_\omega(q)
 =\Lambda(q)+(\log2)(1+2^{-r})\mathbf1_{q=2^r}
\]

and

\[
 C_\omega
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
\]

Define the natural generalized carry rows

\[
 P_{\omega,n}(j)=\sum_q\Lambda_\omega(q)\chi_{n,q}(j),
\]

\[
 S_{\omega,n}(j)=\sum_qC_\omega(q)\chi_{n,q}(j).
\]

At `(n,j)=(6,2)`, the nonzero carry columns are exactly

\[
 q\in\{3,5,6\}.
\]

The generalized-prime values are

\[
 \Lambda_\omega(2)=\frac52\log2,
\quad
 \Lambda_\omega(3)=\log3,
\quad
 \Lambda_\omega(5)=\log5,
\quad
 \Lambda_\omega(6)=0.
\]

Hence

\[
 \boxed{P_{\omega,6}(2)=\log3+\log5=\log15.}
\tag{R-29002.4}
\]

The three forcing coefficients are

\[
 C_\omega(3)=\log^23,
\qquad
 C_\omega(5)=\log^25,
\]

and

\[
 C_\omega(6)
 =2\Lambda_\omega(2)\Lambda_\omega(3)
 =5\log2\log3.
\]

Therefore

\[
\begin{aligned}
P_{\omega,6}(2)^2-S_{\omega,6}(2)
&=2\log3\log5-5\log2\log3\\
&=\boxed{\log3\log(25/32)<0.}
\end{aligned}
\tag{R-29002.5}
\]

The reflected row `j=4` gives the same counterexample.

Thus the implication

```text
positive inverse + Lambda_omega>=0 + C_omega>=0
    -> P_omega(n,j)^2>=S_omega(n,j)
```

is false.

## 3. What remains valid

The counterexample does not affect:

1. the ordinary Selberg–Kummer theorem `L-29002`;
2. the coefficientwise generalized Selberg defect of PR #301 `L-29804`;
3. the zero/first/second moment identities of PR #269 `L-26904`;
4. positivity of `Lambda_omega` or `C_omega`;
5. the atomized pole criterion of `L-29001`.

The failure is the conversion from those coefficient identities to one
pointwise generalized Kummer square.

## 4. Correct source-binding requirement

A valid completion must use one of the following:

- the complete source-coupled quadratic matrix before taking a diagonal;
- an exact positive recombination of complete source fibers;
- a boundary/interior block decomposition whose Schur complement is checked in
  the physical normal orientation.

`L-29006` supplies such a positive recombination for the complete endpoint
packet.  The coupled interior matrix remains a separate theorem.

## 5. Proof boundary

Established exactly:

- nonhomogeneity of the ordinary row reserve;
- the exact ordinary scaling counterexample (R-29002.3);
- the exact source-matched generalized-prime counterexample (R-29002.5);
- the resulting source-cone scope correction.

Not established:

- failure of every coupled source matrix;
- failure of the endpoint-fiber repair;
- a cofinal energy bound;
- RH.
