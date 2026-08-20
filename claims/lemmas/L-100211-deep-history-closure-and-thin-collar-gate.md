# L-100211 — Every deep history is closed; only a subpower activation collar remains

Claim ID: `L-100211`  
Status: **PROVED EXACT REDUCTION; COLLAR ESTIMATE OPEN**  
Created: 2026-08-20  
Depends on: `L-100210`; PR #590 `L-97700--L-97701`  
RH status: **unproved**

The complete small-prime cube has an asymptotic expansion

\[
U_Z(Y)=a_Z+c_ZY^{-1/2}+\varepsilon_Z(Y),
\tag{L-100211.1}
\]

where

\[
a_Z=a_*\prod_{67\le q\le Z}\left(1-\frac1q\right)>0,
\]

\[
c_Z=c_*\prod_{67\le q\le Z}\left(1-\frac1{\sqrt q}\right),
\]

and, once every small-prime divisor is in the fixed deep region,

\[
|\varepsilon_Z(Y)|\le C_ZY^{-2}.
\tag{L-100211.2}
\]

Here \(C_Z=X^{o(1)}\) at the published choice \(Z=(\log X)^{1/4}\).

Substitution in the full rough Euler operator gives the exact decomposition

\[
\boxed{
U_{\rm full}(X)=a_ZA_{1,P}(X)+c_ZX^{-1/2}A_{1/2,P}(X)+\mathcal E_P\varepsilon_Z(X),
}
\tag{L-100211.3}
\]

where

\[
A_{\sigma,P}(X)=\sum_{\substack{A\subseteq P\\p_A\le X}}\frac{(-1)^{|A|}}{p_A^\sigma}.
\tag{L-100211.4}
\]

This retains every activation cutoff.

Choose a deep threshold \(Y_d\) so that (L-100211.2) holds for every endpoint above \(Y_d\). Split the residual history expansion at \(p_A=X/Y_d\).

For the deep part,

\[
\begin{aligned}
\left|\sum_{p_A\le X/Y_d}\frac{(-1)^{|A|}}{p_A}\varepsilon_Z(X/p_A)\right|
&\le C_ZX^{-2}\sum_{p_A\le X/Y_d}p_A\\
&\le C_ZX^{-2}\sum_{n\le X/Y_d}n\\
&\le\boxed{\frac{C_Z}{Y_d^2}}.
\end{aligned}
\tag{L-100211.5}
\]

Thus every deep large-prime history is closed absolutely, with no Type-II cancellation.

The complete remaining residual is confined to

\[
\boxed{X/Y_d<p_A\le X,}
\tag{L-100211.6}
\]

together with the two activation-prefix corrections \(A_{1,P}(X)\) and \(A_{1/2,P}(X)\).

Taking \(Y_d=X^{o(1)}\), as permitted by the fixed-\(P_{61}\) asymptotic and \(Q_Z=X^{o(1)}\), leaves a multiplicative collar of subpower ratio.

Define `RAPC100210` to be the one-sided estimate asserting that the sum of:

1. the inactive constant-mode correction in (L-100210.4);
2. the half-order activation prefix in (L-100210.5);
3. the collar residual from (L-100211.6);

is smaller than the positive full-Euler constant reserve, after the already closed Type-I range is restored.

Then

\[
\boxed{\mathrm{RAPC100210}\Longrightarrow\mathrm{BLPTE67}\Longrightarrow RH.}
\]

The theorem converts the former balanced Type-II range into one thin, source-faithful activation collar. It does not prove `RAPC100210`.