# L-106410 — One-sided Xi endpoint source is a strict Hankel contraction

Claim ID: `L-106410`  
Status: **PROVED EXACT FOR THE TRUNCATED POSITIVE XI HALF-SOURCE**  
Created: 2026-08-24  
Depends on: `L-106400`, `L-106401`; the positive Xi Fourier kernel  
RH status: **not assumed**

Let \(\Phi(u)\ge0\) be the positive even Xi Fourier density.  For \(L>0\), set

\[
F_L(t)=\int_0^L\Phi(u)e^{itu}\,du.
\]

Fix \(\lambda>0\) with

\[
c:=\lambda L<1.
\]

Define the one-sided endpoint companions

\[
N_L=(F_L-i\lambda F_L')(F_L''+i\lambda F_L'''),
\]

\[
D_L=(F_L+i\lambda F_L')(F_L''-i\lambda F_L''').
\]

Both Fourier transforms are supported on \([0,2L]\).  Put

\[
A_L=-D_L,\qquad R_L=N_L-D_L.
\]

## 1. Positive source densities

For \(0\le\xi\le2L\), write \(v=\xi-u\) and integrate only where
\(0\le u,v\le L\).  Direct differentiation gives

\[
\boxed{
\widehat A_L(\xi)
 =\int
 (1-\lambda u)v^2(1+\lambda v)
 \Phi(u)\Phi(v)\,du
 \ge0,
}
\tag{L-106410.1}

and, using the endpoint identity of `L-106400`,

\[
\boxed{
\widehat R_L(\xi)
 =\lambda\xi\int
 (u-v)^2\Phi(u)\Phi(v)\,du
 \ge0.
}
\tag{L-106410.2}

The factors in (L-106410.1) are nonnegative because
\(\lambda u\le c<1\).

## 2. Uniform relative bound

Let

\[
I_0(\xi)=\int\Phi(u)\Phi(v)\,du.
\]

Since \(|u-v|\le u+v=\xi\),

\[
\widehat R_L(\xi)\le\lambda\xi^3I_0(\xi).
\tag{L-106410.3}

On the other hand, \(1-\lambda u\ge1-c\) and \(1+\lambda v\ge1\), so

\[
\widehat A_L(\xi)\ge(1-c)\int v^2\Phi(u)\Phi(v)\,du.
\]

The integration domain and weight are symmetric under \(u\leftrightarrow v\).
Therefore

\[
\int v^2\Phi(u)\Phi(v)\,du
 =\frac12\int(u^2+v^2)\Phi(u)\Phi(v)\,du
 \ge\frac{\xi^2}{4}I_0(\xi).
\tag{L-106410.4}

Combining (L-106410.3)--(L-106410.4), and using \(\xi\le2L\), gives

\[
\boxed{
0\le\widehat R_L(\xi)
\le\frac{8c}{1-c}\widehat A_L(\xi)
\qquad(0\le\xi\le2L).
}
\tag{L-106410.5}

## 3. Exact Hankel-energy consequence

For a positive-frequency symbol \(g\), the Hilbert--Schmidt norm of the
reflected Hankel operator is, up to the fixed Fourier normalization,

\[
\|H_{\overline g}\|_{\mathcal S_2}^2
 =\int_0^\infty\xi|\widehat g(\xi)|^2\,d\xi.
\]

Thus (L-106410.5) gives

\[
\boxed{
\|H_{\overline{R_L}}\|_{\mathcal S_2}^2
\le
\left(\frac{8c}{1-c}\right)^2
\|H_{\overline{A_L}}\|_{\mathcal S_2}^2.
}
\tag{L-106410.6}

At the explicit shift

\[
\boxed{c=\lambda L=\frac1{200},}
\]

one has

\[
\boxed{
\left(\frac{8c}{1-c}\right)^2
 =\left(\frac8{199}\right)^2
 =\frac{64}{39601}
 <\frac1{600}
 <\frac1{200}.
}
\tag{L-106410.7}

The companion winding is independent of \(\lambda>0\), so this small shift does
not weaken the exact zero-count index.

## 4. Scope and remaining adapter

The theorem closes the **same-sign positive half-source** ratio with an exact
constant.  The full real Xi observation also contains:

```text
reflected Toeplitz channels;
the conjugate same-sign channel;
Fourier tails beyond L;
finite-window endpoint and confluent terms;
the normalization of the denominator bank.
```

The classical superexponential decay of \(\Phi\) makes the discarded Fourier
tail harmless for any cofinal \(L\to\infty\), but the exact two-boundary bank
adapter and its normalized denominator trace must still be supplied.  They are
not asserted by this lemma.
