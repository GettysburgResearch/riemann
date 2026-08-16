# L-95100 — Every root-completed policy flow has one terminal coordinate and an exact monotone cutoff controller

Claim ID: `L-95100`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #538 `L-95040`; PR #474 `L-93021`; PR #247 `L-23815`  
Scope: exact finite source-specific flow algebra; no cofinal positivity theorem and no RH conclusion

## 1. Root-completed source

Fix an endpoint `X`. Let `t_X^circ` be the minimally root-completed critical carry target of `L-93021`: its columns `q>=3` equal

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

and its column two is chosen so that the dyadic root functional vanishes. Let
`r_X^circ` be its exact node divergence. The signed-span theorem `L-95040`
gives

\[
r_X^circ(1)=0,
\qquad
\sum_{n=2}^X n r_X^circ(n)=0.
\tag{L-95100.1}
\]

## 2. A descending policy flow

For every parent `n>=4`, let `pi_n` be a probability law on quarter-balanced
splits `n=j+(n-j)` with both children at least two. Define the occupation
recursively from the top:

\[
D_X^\pi(n)
=r_X^\circ(n)
+\sum_{m>n}D_X^\pi(m)P_\pi(m,n),
\qquad n>=4,
\tag{L-95100.2}
\]

where `P_pi(m,n)` is the total coefficient with which the two children of a
policy split at `m` equal `n`. Put the split coefficient

\[
d_{m,j}=D_X^\pi(m)\pi_m(j).
\tag{L-95100.3}
\]

Then the divergence agrees with `r_X^circ` on every node `n>=4`. The only
unmatched coordinates are

\[
E_2^\pi=r_X^\circ(2)+\operatorname{in}_\pi(2),
\qquad
E_3^\pi=r_X^\circ(3)+\operatorname{in}_\pi(3).
\tag{L-95100.4}
\]

Every split preserves size, so (L-95100.1) gives

\[
\boxed{2E_2^\pi+3E_3^\pi=0.}
\tag{L-95100.5}
\]

Consequently the complete terminal defect is one dimensional:

\[
\boxed{(E_2^\pi,E_3^\pi)=(-3\tau_\pi,2\tau_\pi).}
\tag{L-95100.6}
\]

A policy may therefore have a strictly positive occupation at every internal
node and still fail CRCTP only by one terminal ratio.

## 3. The cutoff control bank

Define the terminal-minimizing split

\[
j_-(n)=\max(2,2\lfloor n/4\rfloor).
\tag{L-95100.7}
\]

Its two children terminate, under repeated use of the same rule, with the
minimum possible number

\[
b_-(n)=n\pmod 2
\tag{L-95100.8}
\]

of leaves of size three.

For parents above a cutoff use the mixed law

\[
\pi^{\rm mix}_n
={31\over32}\delta_{\max(2,\lfloor n/3\rfloor)}
+{1\over32}\delta_{\lfloor n/2\rfloor}.
\tag{L-95100.9}
\]

For an integer `K>=4`, the cutoff policy `pi^(K)` uses `j_-` at `n<=K` and
`pi^mix` at `n>K`.

## 4. Exact one-parent switch formula

Let

\[
\delta_n
={31\over32}
 [b_-(\max(2,\lfloor n/3\rfloor))+b_-(n-\max(2,\lfloor n/3\rfloor))]
+{1\over32}[b_-(\lfloor n/2\rfloor)+b_-(n-\lfloor n/2\rfloor)]
-b_-(n).
\tag{L-95100.10}
\]

Then `delta_n>=0`, and it has the closed residue table

\[
\boxed{
\delta_n=0\quad(n\text{ odd}),
}
\]

while for even `n`, according to `n mod 12`,

\[
\boxed{
\begin{array}{c|rrrrrr}
n\bmod12&0&2&4&6&8&10\\ \hline
\delta_n&0&1/16&31/16&1/16&0&2.
\end{array}}
\tag{L-95100.11}
\]

Increasing the cutoff from `K-1` to `K` changes only the split at parent `K`.
The occupation at `K` is unchanged because it depends only on larger parents.
Therefore

\[
\boxed{
E_3^{(K)}=E_3^{(K-1)}-\delta_KD_X^{(K-1)}(K),
}
\tag{L-95100.12}
\]

and

\[
\boxed{
E_2^{(K)}=E_2^{(K-1)}+{3\over2}\delta_KD_X^{(K-1)}(K).
}
\tag{L-95100.13}
\]

Thus the terminal-three defect is monotonically nonincreasing along every
interval of cutoffs on which the switched occupations are nonnegative. The
controller is not an arbitrary LP search: it has a fixed mod-12 drop schedule.

## 5. Proof boundary

Established exactly:

1. one-dimensional terminal residual for every root-completed policy flow;
2. the cutoff-bank construction;
3. the exact one-parent switch formula;
4. the nonnegative mod-12 control schedule;
5. terminal monotonicity under nonnegative occupation.

Open:

1. cofinal nonnegativity of the relevant policy occupations;
2. cofinal bracketing of zero by a fixed or controlled cutoff bank;
3. CRCTP and the root-scalar estimate;
4. RH.
