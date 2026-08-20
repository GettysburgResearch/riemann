# L-101000 — Critical variation dominates the activation-zero envelope deficit

Claim ID: `L-101000`  
Status: **PROVED EXACT POSITIVE-OPERATOR IMPLICATION**  
Created: 2026-08-20  
Frozen inputs: PR #673, PR #687, PR #690  
RH status: **not assumed**

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

\[
L_-(X)
=
\sum_{n\le X}\frac{\beta(n)}{\sqrt n}
4(\sqrt{X/n}-1),
\]

and let the activation-zero quadratic envelope be

\[
\mathcal E_-(X)
=
16\frac{1-67^{-3/2}}{\zeta(3/2)}X-Q_-(X).
\]

The atom-free descent gives

\[
\boxed{
\mathcal E_-(X)
=
4X\int_X^\infty L_-(t)\frac{dt}{t^2}.
}
\tag{L-101000.1}
\]

Define

\[
V(Y)=\int_1^Y (L_-(t))_-\frac{dt}{t},
\]

\[
D(Y)=\int_1^Y (\mathcal E_-(X))_-\frac{dX}{X}.
\]

Assume

\[
V(Y)=Y^{o(1)}.
\tag{L-101000.2}
\]

Then

\[
\boxed{
D(Y)=Y^{o(1)}.
}
\tag{L-101000.3}
\]

## Proof

From the positivity of the Hardy kernel,

\[
(\mathcal E_-(X))_-
\le
4X\int_X^\infty (L_-(t))_-\frac{dt}{t^2}.
\]

Therefore

\[
\begin{aligned}
D(Y)
&\le
4\int_1^Y\int_X^\infty
(L_-(t))_-\frac{dt}{t^2}\,dX\\
&=
4\int_1^Y
(L_-(t))_-\frac{t-1}{t^2}\,dt
+
4(Y-1)\int_Y^\infty
(L_-(t))_-\frac{dt}{t^2}.
\end{aligned}
\]

The first term is at most \(4V(Y)\).

For the tail, split into dyadic blocks.  If
\(2^kY\le t<2^{k+1}Y\), then \(Y/t\le2^{-k}\), hence

\[
Y\int_Y^\infty
(L_-(t))_-\frac{dt}{t^2}
\le
\sum_{k\ge0}
2^{-k}
\int_{2^kY}^{2^{k+1}Y}
(L_-(t))_-\frac{dt}{t}.
\]

For every fixed \(0<\varepsilon<1\), (L-101000.2) gives

\[
\int_{2^kY}^{2^{k+1}Y}
(L_-(t))_-\frac{dt}{t}
\ll_\varepsilon
(2^{k+1}Y)^\varepsilon.
\]

The geometric sum

\[
\sum_{k\ge0}2^{-k(1-\varepsilon)}
\]

converges.  Thus \(D(Y)\ll_\varepsilon Y^\varepsilon\) for every
\(\varepsilon>0\).

## Matrix consequence

The activation-zero envelope criterion is a positive smoothing of the critical
variation criterion:

\[
\boxed{
\mathrm{AFCD}
\Longrightarrow
\mathrm{ACAD}
\Longrightarrow
\mathrm{RH}.
}
\]

The first implication is structural and unconditional.  Its converse is not
claimed.  This contracts two apparently separate routes into one directed
middle-estimate chain.
