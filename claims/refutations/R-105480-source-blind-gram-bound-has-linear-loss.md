# R-105480 — A source-blind Gram/Bessel bound has an unavoidable linear loss

Claim ID: `R-105480`

Status: **PROVED EXPLICIT COUNTEREXAMPLE; BINDING PHYSICAL-COLLAPSE FIREWALL**

Let `M` be a positive multiple of `4`, and put

\[
I_N=\{M,M+1,\ldots,5M/4-1\},
\qquad N=|I_N|=M/4.
\]

Define

\[
a_n=
\begin{cases}
N^{-1/2},&n\in I_N,\\
0,&\text{otherwise}.
\end{cases}
\tag{R-105480.1}
\]

Then

\[
\sum_n|a_n|^2=1.
\tag{R-105480.2}
\]

Moreover the critical coefficients `a_n sqrt(n)` stay between `2` and
`sqrt(5)`.

For every

\[
3M/2\le m<7M/4
\]

and every `n in I_N`,

\[
\frac65<\frac mn<\frac74<2.
\]

Only the first branch of `K_L` is used, and

\[
K_L(m/n)
=8-4\sqrt{m/n}
\ge\kappa,
\qquad
\kappa=8-4\sqrt{7/4}>0.
\tag{R-105480.3}
\]

Therefore

\[
H(m+)=\sum_na_nK_L(m/n)
\ge\kappa\sqrt N.
\]

Since there are `N` such integers `m`, and `m<7M/4`,

\[
\boxed{
\sum_{m=M}^{2M}\frac{|H(m+)|^2}{16m}
\ge\frac{\kappa^2}{448}M.
}
\tag{R-105480.4}
\]

The left side is exactly the Gram energy of `delta_m=H(m+)/4`.

## Binding consequence

No inequality of the form

\[
\sum_m\frac{|\delta_m|^2}{m}
\le M^{o(1)}\sum_n|a_n|^2
\]

can hold for arbitrary physical coefficient packets, even when the
coefficients have the natural critical size `a_n=O(n^{-1/2})`.

Therefore none of the following closes `F1GRAM105480`:

```text
source-blind Schur testing;
a universal Bessel/frame bound for physical dilates;
diagonal coefficient energy alone;
positivity of the prime-box Hodge form before physical collapse;
zero logarithmic mean of K_L without arithmetic source cancellation.
```

The counterexample does not apply to the signed Boolean source itself.  It
proves that a successful argument must use its least-prime cutoff differences,
Möbius signs, connected Kummer incidence, or an equivalent source-specific
arithmetic mechanism.
