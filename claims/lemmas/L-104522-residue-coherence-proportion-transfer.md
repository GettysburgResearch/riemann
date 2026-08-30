# L-104522 — Genuine residue-coherence transfer of real-zero proportions

Claim ID: `L-104522`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Depends on: `L-104500`, `L-104502`  
RH status: **not assumed**

## 1. Purpose

This theorem corrects the scope defect in the earlier high-derivative-band
statement.  Here the hypothesis that the derivative has many real zeros is a
load-bearing premise.  No real-rootedness of the parent is independently
proved.

Let `f` be real analytic on a neighbourhood of `[a,b]`. Assume:

1. `f(a)f(b) != 0`;
2. every zero of `f'` in `(a,b)` is simple;
3. `f` and `f'` have no common zero in `[a,b]`.

Write the real zeros of `f'` as

\[
a<c_1<\cdots<c_R<b.
\]

At each critical point define the derivative-ratio residue

\[
\boxed{
\rho_j={f(c_j)\over f''(c_j)}.
}
\tag{L-104522.1}
\]

By `L-104502`, `rho_j>0` exactly at a wrong extremum and `rho_j<0` exactly at a
Rolle-generating extremum.

Put

\[
A=-\sum_{j=1}^R\rho_j,
\qquad
B=\sum_{j=1}^R\rho_j^2,
\]

and, when `R B>0`, define the residue coherence

\[
\boxed{
\mathfrak C(f;(a,b))
={A_+^2\over R B},
\qquad A_+=\max(A,0).
}
\tag{L-104522.2}
\]

By Cauchy--Schwarz, `0<=mathfrak C<=1`.

## 2. Coherence bounds the number of good extrema

Let

\[
G=\#\{j:\rho_j<0\},
\qquad
E=\#\{j:\rho_j>0\},
\qquad R=G+E.
\]

Write

\[
S_- =\sum_{\rho_j<0}|\rho_j|,
\qquad
S_+ =\sum_{\rho_j>0}\rho_j.
\]

Since `A=S_--S_+`, one has `S_->=A_+`.  Therefore

\[
A_+^2
\le S_-^2
\le G\sum_{\rho_j<0}\rho_j^2
\le G B.
\]

Hence

\[
\boxed{
G\ge {A_+^2\over B}=R\,\mathfrak C(f;(a,b)).
}
\tag{L-104522.3}
\]

## 3. Exact proportion transfer on one interval

The exact reverse-Rolle identity `L-104500.3` gives

\[
N_\mathbb R(f;(a,b))
=2G-R+1-B_--B_+,
\]

with `B_-,B_+ in {0,1}`. Combining with (L-104522.3),

\[
\boxed{
N_\mathbb R(f;(a,b))
\ge
\bigl(2\mathfrak C(f;(a,b))-1\bigr)R-1.
}
\tag{L-104522.4}
\]

In particular, if

\[
\mathfrak C(f;(a,b))\ge {1+c\over2}
\qquad(0<c<1),
\]

then

\[
\boxed{
N_\mathbb R(f;(a,b))\ge c\,N_\mathbb R(f';(a,b))-1.
}
\tag{L-104522.5}
\]

This is a genuine converse-Rolle proportion theorem: if the derivative has no
real zero, the right side supplies no positive count; if it has proportion `p`,
that `p` is multiplied by the independently measured coherence factor.

## 4. Mean/variance form

Assume the average residue is negative. Write

\[
\mu=-{1\over R}\sum_j\rho_j>0,
\qquad
m_2={1\over R}\sum_j\rho_j^2,
\]

and define the squared coefficient of variation about the negative carrier

\[
v^2={m_2-\mu^2\over\mu^2}.
\]

Then

\[
\mathfrak C={\mu^2\over m_2}={1\over1+v^2}.
\]

Thus `v<1` gives the explicit transfer constant

\[
\boxed{
c(v)={1-v^2\over1+v^2}>0,
}
\tag{L-104522.6}
\]

and

\[
\boxed{
N_\mathbb R(f;(a,b))
\ge
c(v)N_\mathbb R(f';(a,b))-1.
}
\tag{L-104522.7}
\]

The monochromatic cosine model has `v=0` and `c=1`.  The quartic firewall
`x^4-2x^2+2` has coherence below `1/2`, so the theorem correctly gives no
positive transfer.

## 5. Xi proportion form

Let

\[
F_k(t)=\Xi^{(k)}(t).
\]

For a regular interval `I_T=(-T,T)`, let

\[
R_k(T)=N_\mathbb R(F_k;I_T),
\]

and let `Z_k(T)` be the complete zero count in the corresponding symmetric
rectangle.  Suppose, along a sequence of regular heights,

\[
{R_k(T)\over Z_k(T)}\ge p+o(1),
\qquad
{Z_k(T)\over Z_{k-1}(T)}=1+o(1),
\]

and

\[
\mathfrak C(F_{k-1};I_T)\ge {1+c\over2}+o(1).
\]

Then (L-104522.4) gives

\[
\boxed{
\liminf_{T\to\infty}{R_{k-1}(T)\over Z_{k-1}(T)}
\ge c p.
}
\tag{L-104522.8}
\]

Unlike the earlier high-band statement, the antecedent line proportion `p` is
not re-proved inside this theorem.  If `p` is improved, the conclusion improves
linearly.

## 6. Scope

The theorem does not assert the Xi residue-coherence bound.  It identifies a
concrete two-moment estimate which is sufficient for a nontrivial downward
percentage transfer.  That arithmetic/analytic mean-value problem is isolated
as `RCMV104530` in `T-104530`.
