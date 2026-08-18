# L-97911 — An almost root-exponential terminal owner strip is negligible

Claim ID: `L-97911`  
Status: **PROVED UNCONDITIONAL TYPE-I ESTIMATE**  
Created: 2026-08-18  
Depends on: `L-97910`; exact largest-prime Bellman identity in PR #590  
RH status: **not assumed**

Normalize

\[
 U_Z(X)=\frac{\mathcal B_{67,Z}(X)}{\sqrt X}.
\]

Adjoin every active prime larger than `Z` in increasing order. The exact
largest-prime identity is

\[
 U_{\rm full}(X)=U_Z(X)-
 \sum_{Z<p\le X/2}\frac1pU_{<p}(X/p),
\tag{L-97911.1}
\]

where `U_<p` contains every already installed prime below `p`, and every
nonempty large-prime history is owned exactly once by its largest prime.

Let `H=H(X)>=log Z` satisfy

\[
 H=o(\log X)
\]

and define the terminal owner strip

\[
 \mathfrak I_{Z,H}(X)=
 \sum_{Xe^{-H}<p\le X/2}\frac1pU_{<p}(X/p).
\tag{L-97911.2}
\]

Then

\[
 \boxed{
 |\mathfrak I_{Z,H}(X)|\ll\frac{H^2}{\log X}.
 }
\tag{L-97911.3}
\]

Under the cutoff of `L-97910`,

\[
 H^2\log Z=o(\log X)
 \quad\Longrightarrow\quad
 \boxed{\mathfrak I_{Z,H}(X)=o(U_Z(X)).}
\tag{L-97911.4}
\]

Consequently one may take

\[
 \boxed{
 H(X)=\frac{1}{\omega(X)}
 \sqrt{\frac{\log X}{\log Z}},
 \qquad \omega(X)\longrightarrow\infty
 }
\tag{L-97911.5}
\]

provided `H>=log Z`. For example, with

\[
 \omega(X)=\log\log\log X
\]

and fixed `kappa` in `L-97910`, the remaining Type-II owners obey

\[
 p\le X\exp\!\left(
 -\frac{1+o(1)}{\sqrt2\log\log\log X}
 \sqrt{\frac{\log X}{\log\log X}}
 \right),
\tag{L-97911.6}
\]

and every surviving child endpoint is at least the reciprocal exponential
factor in (L-97911.6).

## Proof

The normalized base scalar is globally bounded. Expanding all installed prime
factors and taking absolute values only in this terminal strip gives

\[
 |U_{<p}(Y)|
 \ll\prod_{67\le q\le Y}(1+q^{-1})
 \ll\log(2Y).
\tag{L-97911.7}
\]

This remains source-faithful: the normalized coefficient of a squarefree
history is `1/m`, and inactive factors vanish.

For `p>Xe^{-H}`, one has `2<=Y=X/p<e^H`, so

\[
 |U_{<p}(X/p)|\ll H.
\]

Uniformly for `H=o(log X)`, Mertens' theorem yields

\[
 \sum_{Xe^{-H}<p\le X/2}\frac1p
 \ll\frac H{\log X}.
\tag{L-97911.8}
\]

Multiplication proves (L-97911.3). Since `L-97910` gives
`U_Z(X)\gg1/\log Z`, (L-97911.4) follows.

## Improvement over the preceding split

PR #590 closes only `p>X/Z`. Here `H` may tend almost to
`sqrt(log X/log Z)`, so the closed terminal owner strip is exponentially wider
while preserving exact largest-prime ownership and activation.
