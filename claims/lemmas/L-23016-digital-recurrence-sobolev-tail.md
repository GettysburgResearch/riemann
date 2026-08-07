# L-23016 — Digital recurrence and a compact Sobolev tail

Claim ID: `L-23016`  
Title: The dyadic shell satisfies a strict lower-scale digital recurrence whose infinite tail is arbitrarily small from H1 to L2  
Status: **PROPOSED COMPLETE EXACT RECURRENCE AND ANALYTIC TAIL BOUND PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: PR #234 `L-23406`; PR #236 `L-23010`; Abel summation  
Scope: compactness reduction to a finite digital prefix; no finite-prefix coercivity claim

## 1. Exact digital recurrence

Let

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2),
\qquad
B_2(x)=\sum_{n\le x}b_2(n).
\]

Put

\[
c_2(n)=1-v_2(n),
\qquad
C_2(N)=\sum_{n\le N}c_2(n)=s_2(N),
\]

where `s_2` is the binary digit sum. The exact convolution identity

\[
c_2*b_2=\delta_1-2\delta_2
\]

gives, for every real `x>=2`,

\[
\boxed{
\sum_{k\le x}c_2(k)B_2(x/k)=-1.
}
\tag{L-23016.1}

Since `c_2(1)=1` and `c_2(2)=0`,

\[
\boxed{
B_2(x)
=-1-
\sum_{3\le k\le x}c_2(k)B_2(x/k).
}
\tag{L-23016.2}

Every nonconstant source on the right lies at scale at most `x/3`.

Normalize

\[
q(t)=e^{-t/2}B_2(e^t).
\]

Then (L-23016.2) becomes

\[
\boxed{
q(t)
=-e^{-t/2}
-
\sum_{k\ge3}
\frac{c_2(k)}{\sqrt k}
q(t-\log k),
}
\tag{L-23016.3}

with causal zero extension.

## 2. Finite prefix and tail

For an integer `R>=3`, define

\[
\mathcal A_R
=I+
\sum_{3\le k<R}
\frac{c_2(k)}{\sqrt k}\tau_{\log k},
\]

and

\[
\mathcal T_R
=
\sum_{k\ge R}
\frac{c_2(k)}{\sqrt k}\tau_{\log k}.
\]

Then

\[
\boxed{
\mathcal A_Rq
=-e^{-t/2}-\mathcal T_Rq.
}
\tag{L-23016.4}

The infinite arithmetic has been isolated in one tail whose first active scale is
`R`.

## 3. Abel summation

For a causal absolutely continuous `f`, put

\[
F_t(x)=x^{-1/2}f(t-\log x).
\]

Then

\[
F_t'(x)
=-x^{-3/2}
\left[
\frac12f(t-\log x)+f'(t-\log x)
\right].
\tag{L-23016.5}

Since

\[
0\le C_2(x)=s_2(\lfloor x\rfloor)
\le1+\frac{\log x}{\log2},
\tag{L-23016.6}

Abel summation gives, pointwise,

\[
\begin{aligned}
|\mathcal T_Rf(t)|
\le{}&
\frac{1+\log R/\log2}{\sqrt R}
|f(t-\log R)|\\
&+
\int_{\log R}^{\infty}
\left(1+\frac u{\log2}\right)e^{-u/2}
\left[
\frac12|f(t-u)|+|f'(t-u)|
\right]du.
\end{aligned}
\tag{L-23016.7}

## 4. Sobolev tail norm

Minkowski's inequality yields, on every cumulative finite horizon and on the
full half-line,

\[
\boxed{
\|\mathcal T_Rf\|_2
\le
\varepsilon_R
\left(\|f\|_2+\|f'\|_2\right),
}
\tag{L-23016.8}

where one explicit choice is

\[
\boxed{
\varepsilon_R
=
\frac{1+\log R/\log2}{\sqrt R}
+
2R^{-1/2}
\left[
1+\frac{\log R+2}{\log2}
\right].
}
\tag{L-23016.9}

In particular,

\[
\boxed{\varepsilon_R=O((\log R)/\sqrt R)\to0.}
\tag{L-23016.10}

Thus the infinite digital recurrence is an arbitrarily small Sobolev
perturbation of a finite delay system.

## 5. Exact remaining finite problem

A full proof from this route would follow from a source-specific finite-prefix
estimate of the form

\[
\|f\|_{H^1(J,J+B)}^2
\le
C_R\|\mathcal A_Rf\|_{L^2(J-O_R(1),J+B)}^2
+
\theta_R\mathcal E_{\le J-\log R}
+
J^{O_R(1)},
\tag{L-23016.11}

with `theta_R<1` after the exact parity/Green boundary correction is included.
For `R` large, (L-23016.8) can then be absorbed. The two-frequency reflected
identity of PR #241 is the exact normal-block adapter for testing
(L-23016.11).

No such finite-prefix Schur reserve is proved here.

## 6. Proof boundary

Closed exactly:

- the strict lower-scale digital recurrence;
- the finite-prefix/tail split;
- the Abel formula;
- the explicit `H1 -> L2` tail bound tending to zero.

Open:

- finite-prefix source-specific coercivity;
- the parity/Green Schur reserve;
- RH.
