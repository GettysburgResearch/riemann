# L-100724 — Reciprocal-level pairing makes every endpoint interval below the exponent `e` positive

Claim ID: `L-100724`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC INTERVAL THEOREM**  
Created: 2026-08-21  
Depends on: `L-100721`; Tao's semigroup bound; Mertens' prime-reciprocal theorem  
RH status: **not assumed**

Let `p<q` be endpoint primes and let `P` be the complete set of primes strictly
between them. Put

\[
S_{p,q}=\sum_{p<\ell<q}{1\over\ell},
\qquad
a=p^{-1/2},
\qquad b=q^{-1/2}.
\]

Then

\[
\boxed{
S_{p,q}+a+b<1
\quad\Longrightarrow\quad
H_{p,q;\mathcal P}(t)\ge0
\quad(t\ge0).
}
\tag{L-100724.1}
\]

## 1. A quantitative lower bound for every rough reciprocal prefix

For `x>=1`, write

\[
A_{\mathcal P}(x)=\sum_{k\ge0}(-1)^kM_k(x),
\]

where

\[
M_k(x)=
\sum_{\substack{A\subseteq\mathcal P,\ |A|=k\\
                  \prod_{\ell\in A}\ell\le x}}
 {1\over\prod_{\ell\in A}\ell}.
\]

Double-counting a selected prime gives

\[
\begin{aligned}
kM_k(x)
&=\sum_{\ell\in\mathcal P}{1\over\ell}
  \sum_{\substack{|B|=k-1,\ \ell\notin B\\
                    \ell\prod_{r\in B}r\le x}}
  {1\over\prod_{r\in B}r}\\
&\le S_{p,q}M_{k-1}(x).
\end{aligned}
\tag{L-100724.2}
\]

If `S_(p,q)<1`, every odd level is smaller than the preceding even level.
Pairing levels yields

\[
\boxed{
1-S_{p,q}\le A_{\mathcal P}(x)\le1
\qquad(x\ge1).
}
\tag{L-100724.3}
\]

The upper bound is also a special case of Tao's theorem.  For `x<1`, the
prefix is zero by convention.

## 2. Positivity of the compensated prefix

Use the exact four-term prefix from `L-100721`:

\[
\mathcal B(x)
=A(x)-aA(x/p)-bA(x/q)+abA(x/(pq)).
\]

For `x<1`, it is zero. For `x>=1`, (L-100724.3), the upper bound `A<=1`, and
the nonnegativity of the last term give

\[
\boxed{
\mathcal B(x)
\ge1-S_{p,q}-a-b.
}
\tag{L-100724.4}
\]

Thus the hypothesis in (L-100724.1) implies

\[
\mathcal B(x)>0
\qquad(x\ge1).
\]

The coarea formula `L-100721.5` now gives

\[
H'_{p,q;\mathcal P}(t)\ge0.
\]

Since `H(0)=0`, the complete interval is nonnegative at every scale.

## 3. Asymptotic prime-power width

Fix any real

\[
1<A<e.
\]

Mertens' theorem gives, uniformly for primes `p<q<=p^A`,

\[
S_{p,q}
\le\log{\log q\over\log p}+o_{p\to\infty}(1)
\le\log A+o(1).
\]

Because `log A<1` and `p^-1/2+q^-1/2=o(1)`, there is `p_0(A)` such that

\[
S_{p,q}+p^{-1/2}+q^{-1/2}<1
\]

whenever `p>=p_0(A)` and `q<=p^A`. Therefore

\[
\boxed{
q\le p^A,\quad A<e,\quad p\ge p_0(A)
\Longrightarrow
H_{p,q;\mathcal P}(t)\ge0
\quad(t\ge0).
}
\tag{L-100724.5}

This strictly enlarges the previous asymptotic region `A<exp(3/4)` from
`L-100615`.

## 4. Updated matrix frontier

After deleting finitely many low-prime rows and columns, only intervals with

\[
\boxed{
\log q\ge(e-o(1))\log p
}
\tag{L-100724.6}
\]

can contribute negatively to the joint min--max cubic matrix.

The theorem is pointwise and source-faithful. It does not estimate the
remaining supercritical intervals.
