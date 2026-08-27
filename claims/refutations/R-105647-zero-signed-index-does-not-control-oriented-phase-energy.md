# R-105647 — Zero signed index does not control oriented phase energy

Claim ID: `R-105647`  
Status: **PROVED EXACT ONE-PAIR COUNTERFAMILY**  
Created: 2026-08-25  
Depends on: `L-105647--L-105649`; sibling `L-106512--L-106514`  
RH status: **not assumed**

The logarithmic midline charge recovers the signed all-pass index exactly.  It
does not recover the degree-zero canonical-correlation defect.

## 1. Equal-degree quotient

For `a,b>0`, put

\[
A(z)={z-ia\over z+ia},
\qquad
B(z)={z-ib\over z+ib},
\qquad
U={A\over B}.
\]

Both numerator and denominator have degree one, so

\[
\boxed{-\operatorname{wind}U=0.}
\tag{R-105647.1}

For every

\[
0<y<\min(a,b),
\]

`L-105647` gives

\[
\boxed{
\mathfrak J_y(U)=1-1=0.
}
\tag{R-105647.2}

Thus the complete small-scale logarithmic signed index vanishes identically.

## 2. The oriented Hankel charge remains positive

The normalized model vectors are

\[
e_a(\xi)=\sqrt{2a}e^{-a\xi},
\qquad
e_b(\xi)=\sqrt{2b}e^{-b\xi}.
\]

Their squared overlap is

\[
\left|\langle e_a,e_b\rangle\right|^2
={4ab\over(a+b)^2}.
\]

The exact oriented overlap formula of `L-106512` therefore gives

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=1-{4ab\over(a+b)^2}
={ (a-b)^2\over(a+b)^2}.
}
\tag{R-105647.3}

This is strictly positive whenever `a!=b`.  For the explicit fixture

\[
a=1,
\qquad b=2,
\]

one has

\[
\boxed{
-\operatorname{wind}U=0,
\qquad
\mathfrak J_y(U)=0\ (0<y<1),
\qquad
\|H_U\|_{\mathcal S_2}^2={1\over9}.
}
\tag{R-105647.4}

Equivalently, the denominator phase-angle integral of `L-106514` is positive
even though the signed index and its sufficiently fine logarithmic
regularization are both zero.

## 3. Exact missing quantity

For a general finite reduced quotient

\[
U={B_+\over B_-},
\]

one has

\[
\begin{aligned}
\|H_U\|_{\mathcal S_2}^2
&=m_- -\operatorname{tr}(P_-P_+)\\
&=(m_--m_+)
 +\bigl(m_+-\operatorname{tr}(P_-P_+)\bigr).
\end{aligned}
\]

Hence

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=
\lim_{y\downarrow0}\mathfrak J_y(U)
+
\|H_{U^{-1}}\|_{\mathcal S_2}^2.
}
\tag{R-105647.5}

The first term is the signed integer flow.  The second is the degree-zero
reverse-oriented phase energy.  It is exactly the null energy discarded by a
raw negative-Hardy or adverse-only estimate.

## 4. Consequence for the Xi programme

`L-105647--L-105649` close the dictionary between soft current charge,
adaptive bandwidth and signed index.  They do **not** prove the remaining
physical phase-angle theorem.  That theorem must control the reverse-oriented
canonical-correlation defect using actual Xi parent/derivative geometry or the
positive Turan/current hierarchy.

Thus a valid final attack must retain both:

```text
signed logarithmic index flow;
degree-zero oriented phase-overlap defect.
```

Deleting the second term would repeat the raw-shell and absolute-energy errors
already refuted elsewhere in the repository.  RH remains unproved.
