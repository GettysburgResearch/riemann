# L-100210 — Largest-prime Euler telescoping and the exact activation-tail correction

Claim ID: `L-100210`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-20  
Sibling input: PR #590 at `d42817f4de15b97d37f760578d64d067a77be5c5`  
RH status: **not assumed**

Let

\[
Z=(\log X)^{1/4}
\]

and let \(p_1<\cdots<p_k\) be the active rough primes larger than \(Z\). Put

\[
(\mathcal R_pf)(Y)=\frac1p f(Y/p),
\qquad
\mathcal E_P=\prod_{i=1}^k(I-\mathcal R_{p_i}).
\]

The full normalized rough scalar is

\[
U_{\rm full}(X)=\mathcal E_PU_Z(X).
\]

## Full constant mode

For a literal constant on the whole positive half-line,

\[
\boxed{
\mathcal E_P c=c\prod_{i=1}^k\left(1-\frac1{p_i}\right).
}
\tag{L-100210.1}
\]

Equivalently, with

\[
e_i=\prod_{h\le i}\left(1-\frac1{p_h}\right),\qquad e_0=1,
\]

the largest-prime decrement telescopes:

\[
\boxed{
\sum_{i=1}^k\frac{e_{i-1}}{p_i}=1-e_k.
}
\tag{L-100210.2}
\]

Thus the constant asymptotic mode of the Type-II source requires no bilinear estimate.

## Physical activation correction

The arithmetic carrier is zero below its endpoint support. For

\[
c_+(Y)=c\,\mathbf1_{Y\ge1},
\]

one instead has

\[
\boxed{
\mathcal E_Pc_+(X)=c\sum_{\substack{A\subseteq P\\p_A\le X}}\frac{(-1)^{|A|}}{p_A}.
}
\tag{L-100210.3}
\]

Hence

\[
\boxed{
\mathcal E_Pc_+(X)=c\prod_{p\in P}\left(1-\frac1p\right)-c\sum_{\substack{A\subseteq P\\p_A>X}}\frac{(-1)^{|A|}}{p_A}.
}
\tag{L-100210.4}
\]

The second term is the exact inactive-subset correction. Omitting it is the constant-mode version of the historical unrestricted-reservoir error.

Likewise,

\[
\boxed{
\mathcal E_P\left(Y^{-1/2}\mathbf1_{Y\ge1}\right)(X)=X^{-1/2}\sum_{\substack{A\subseteq P\\p_A\le X}}\frac{(-1)^{|A|}}{\sqrt{p_A}}.
}
\tag{L-100210.5}
\]

Thus both asymptotic modes telescope completely away from activation, while their only obstruction is one explicit truncated Euler prefix.