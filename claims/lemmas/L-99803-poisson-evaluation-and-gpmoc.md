# L-99803 — Poisson evaluation isolates one off-diagonal theorem

For each \(L\), define the fixed-order packet

\[
f_L(y)=(\mathcal F_Lh)(y)
\]

for every \(y\ge1\), using the same \(M_L\) even below the \(L\)-th block.
Write

\[
f_L(y)=\sum_n c_{L,y}(n),
\qquad
\tau_L=\frac1{\log(L+e)}.
\]

Set

\[
D_{L,y}(\gamma)=\sum_n c_{L,y}(n)n^{\tau_L-i\gamma},
\]

\[
Q_L(y)=
\int_{\mathbb R}|D_{L,y}(\gamma)|^2
P_{\tau_L}(\gamma)\,d\gamma.
\]

For

\[
E_{L,y}(z)=\sum_n c_{L,y}(n)n^{\tau_L-z},
\]

we have \(E_{L,y}(\tau_L)=f_L(y)\). The Poisson inequality in the right
half-plane gives

\[
\boxed{|f_L(y)|^2\le Q_L(y).}
\]

Let

\[
b_{L,k}=\binom{M_L+k-1}{k}.
\]

The exact positive inverse is

\[
(\mathcal Kh)(x)
=\sum_{k=0}^{L+1}b_{L,k}f_L(x/2^k),
\qquad 2^L\le x<2^{L+1}.
\]

Define `GPMOC99800` by

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\sqrt{Q_L(y)}\,\frac{dy}{y}
=2^{o(L)}.
}
\]

Then \(\mathcal Kh\) has subpower logarithmic negative mass. Since \(K(s)\) is
zero-safe in the open translated strip, PR #653's Landau theorem yields RH.

The diagonal contribution is already subpower and L-99801 supplies local
coercivity. The signed off-diagonal squarefree-core packing in the display is
the sole remaining theorem. It is not implied by a diagonal large sieve or by
the finite \(10^8\) certificate.
