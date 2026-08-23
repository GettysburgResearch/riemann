# L-105222 — Weighted local extinction and the exact combined correction budget

Claim ID: `L-105222`  
Status: **PROPOSED EXACT EXTINCTION LEMMA AND CORRECTION IDENTITY; independent review pending**  
Created: 2026-08-23  
Depends on: `L-105220--L-105221`  
RH status: **not assumed**

## 1. A weighted integrality threshold

Let `c` range over real simple critical points and let

\[
w_c=\Omega_a(c)>0,
\qquad
\rho_c=\frac{p(c)}{p''(c)}.
\]

Define

\[
N=\sum_cw_c,
\qquad
A=-\sum_cw_c\rho_c,
\qquad
B=\sum_cw_c\rho_c^2.
\tag{L-105222.1}
\]

Assume `A>0`. Let

\[
W_+=\sum_{\rho_c>0}w_c
\]

be the weighted mass of wrong extrema. If `G=N-W_+` is the good-extremum
weight, then

\[
A
\le
\sum_{\rho_c<0}w_c|\rho_c|
\le
\sqrt{GB}.
\]

Therefore

\[
\boxed{
W_+
\le
N-\frac{A^2}{B}
=
\frac{NB-A^2}{B}.
}
\tag{L-105222.2}
\]

For `|x-a|<=1`, the positive localizer satisfies

\[
\Omega_a(x)\ge\Omega_a(a+1)=\frac9{25}.
\tag{L-105222.3}
\]

Consequently

\[
\boxed{
\frac{NB-A^2}{B}<\frac9{25}
\quad\Longrightarrow\quad
\text{there is no wrong extremum in }[a-1,a+1].
}
\tag{L-105222.4}
\]

This is an integrality-scale criterion: a subunit weighted defect, rather than
a merely asymptotic coherence statement, eliminates the last adverse event.

## 2. Exact real/nonreal/debt algebra

Let the complete boundary carriers of `L-105221` be denoted

\[
\mathcal N,\qquad\mathcal A,\qquad\mathcal B.
\]

For a finite polynomial, define the conjugate-paired corrections

\[
C_0
=
\sum_{\substack{p'(c)=0\\c\notin\mathbb R}}\Omega_a(c),
\]

\[
C_1
=
\sum_{\substack{p'(c)=0\\c\notin\mathbb R}}
\Omega_a(c)\rho_c,
\]

\[
C_2
=
\sum_{\substack{p'(c)=0\\c\notin\mathbb R}}
\Omega_a(c)\rho_c^2,
\]

and

\[
D_2
=
\sum_{p''(d)=0}\Omega_a(d)\tau_d.
\tag{L-105222.5}
\]

Then exactly

\[
\mathcal N=N+C_0,
\qquad
\mathcal A=A-C_1,
\qquad
\mathcal B=B+C_2+D_2.
\tag{L-105222.6}
\]

Solving for `N,A,B` and expanding gives

\[
\boxed{
\begin{aligned}
NB-A^2
={}&
\mathcal N\mathcal B-\mathcal A^2
-\mathcal N(C_2+D_2)
-C_0\mathcal B\\
&+C_0(C_2+D_2)
-2\mathcal A C_1-C_1^2.
\end{aligned}
}
\tag{L-105222.7}
\]

This is the precise correction interface. Separate absolute estimates for
`C_0,C_1,C_2,D_2` are sufficient but not necessary: only the displayed signed
combination must be controlled.

## 3. A conclusion-facing moving-centre gate

For the Xi derivative level `k`, suppose an entire-function passage produces
the exact analogues of (L-105222.6) on a sequence `|a|->infinity`. Assume

\[
B_k(a)
=
\frac{D}{\ell(a)^3}(1+o(1))
\tag{L-105222.8}
\]

and that the signed combined correction in the second line of
(L-105222.7) is

\[
o\bigl(\ell(a)^{-3}\bigr).
\tag{L-105222.9}
\]

The safe-line defect from `L-105221` is `O(ell^-4)`, so

\[
\frac{N_kB_k-A_k^2}{B_k}=o(1).
\]

Eventually it is below `9/25`; hence no wrong extremum lies in
`[a-1,a+1]`.

Since the unit intervals cover both tails of the real axis, a uniform version
of (L-105222.8)--(L-105222.9) at every sufficiently large centre removes all
high-ordinate wrong extrema at that derivative level. Only a compact
finite-height residue/winding ledger remains.

## 4. Scope

The extinction lemma and correction algebra are exact. The Xi correction
estimate (L-105222.9) is not proved. The theorem identifies a potentially
strictly weaker target than bounding every correction separately, because
nonreal-critical and adjacent-derivative terms may cancel in the exact signed
combination.
