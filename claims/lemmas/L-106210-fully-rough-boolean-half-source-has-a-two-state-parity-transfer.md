# L-106210 — The fully rough Boolean half-source has a two-state parity transfer

Claim ID: `L-106210`  
Programme aliases: `LFAM1.ROUGH_HALF_SOURCE_TRANSFER`, `LFAM2.BOOLEAN_WITT_PARITY`, `STRESS.FINITE_DEPTH_ROUGH_CORE`  
Status: **PROVED EXACT BOOLEAN HALF-SOURCE FACTORIZATION**  
Created: 2026-08-26  
Depends on: `L-106133`, `T-106150`, the Boolean cutoff definitions  
Programme issues: #743, #736, #737  
RH status: **not assumed**

On the squarefree Boolean algebra let

\[
h(S)=\left(-\frac12\right)^{|S|},
\qquad
f_U=a_U\star h,
\qquad
b_U=f_U\star f_U=\mu_{\rm sf}\text{-balanced row}.
\]

Let \(g,c\) be coprime squarefree integers, let every prime divisor of \(c\)
exceed \(U\), and put \(k=\omega(c)\).

## 1. Exact two-state transfer

No truncated Möbius divisor can contain a prime of \(c\). Splitting the
Boolean convolution according to which rough labels enter the \(a_U\)-factor
gives

\[
\boxed{
f_U(gc)
=
2^{-k}
\left[
f_U(g)-\bigl(1-(-1)^k\bigr)h(g)
\right].
}
\tag{L-106210.1}
\]

Equivalently, adjoining one new \(U\)-rough prime acts on the state
\((f_U,h)\) by

\[
\boxed{
\begin{pmatrix}f_U(gp)\\ h(gp)\end{pmatrix}
=
\begin{pmatrix}
\frac12&-1\\[1mm]
0&-\frac12
\end{pmatrix}
\begin{pmatrix}f_U(g)\\ h(g)\end{pmatrix}.
}
\tag{L-106210.2}
\]

The eigenvalues are \(+1/2\) and \(-1/2\). Thus arbitrary Boolean
factorization history in a completely rough tail collapses to a
two-dimensional parity state.

For \(g=1\),

\[
\boxed{
f_U(c)=
\begin{cases}
0,&k\ \text{even},\\[1mm]
-2^{1-k},&k\ \text{odd}.
\end{cases}
}
\tag{L-106210.3}
\]

## 2. Balanced coefficient

The Boolean Vaughan identity also gives

\[
b_U
=
\mu_{\rm sf}-2\mu_U+\mu_U\star\mu_U\star\mathbf1_{\rm sf}.
\]

Put

\[
H_U(g)
=
(\mu_U\star\mu_U\star\mathbf1_{\rm sf})(g).
\]

Since \(c>1\) is \(U\)-rough,

\[
\boxed{
b_U(gc)=H_U(g)+\mu(g)\mu(c).
}
\tag{L-106210.4}
\]

Hence two \(U\)-rough reduced cores attached to one common core satisfy

\[
\boxed{
b_U(gc)b_U(gd)
=
\bigl(H_U(g)+\mu(g)\mu(c)\bigr)
\bigl(H_U(g)+\mu(g)\mu(d)\bigr).
}
\tag{L-106210.5}
\]

The rough balanced coefficient is therefore rank two in the variables
\(1\) and \(\mu\).

## 3. Cofinal finite depth

On a dyadic physical horizon \(Y\), every reduced core in the compact
observation is at most \(C\sqrt Y\) for one absolute \(C\), while

\[
U=\lfloor Y^{1/6}\rfloor.
\]

For sufficiently large \(Y\), four distinct primes larger than \(U\) have
product \(>U^4>C\sqrt Y\). Therefore

\[
\boxed{
P^-(c)>U
\quad\Longrightarrow\quad
1\le\omega(c)\le3
}
\tag{L-106210.6}
\]

cofinally, and likewise for the opposite reduced core.

Thus the fully rough part of the live half-source consists only of
prime-, semiprime-, and triple-prime cores, with the exact two-state
coefficients above.

## Scope

This theorem removes Boolean factorization complexity in the fully rough
sector. It does not estimate its physical reflection/Kummer trace, prove
`REFSIG106150`, `BCI102990`, or RH.
