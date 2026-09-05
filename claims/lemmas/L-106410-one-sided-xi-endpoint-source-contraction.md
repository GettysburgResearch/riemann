# L-106410 — One-sided Xi endpoint source is a strict Hankel contraction

Claim ID: `L-106410`  
Status: **PROVED EXACT FOR THE TRUNCATED POSITIVE XI HALF-SOURCE**  
Created: 2026-08-24  
Strengthened: 2026-08-24  
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

and, using the endpoint identity of `L-106400` and symmetrizing under
\(u\leftrightarrow v\),

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

## 2. Sharp symmetric relative bound

The domain and the weight \(\Phi(u)\Phi(v)\) are symmetric.  Therefore

\[
\widehat A_L(\xi)
=\frac12\int
\Bigl[(1-\lambda u)v^2(1+\lambda v)
 +(1-\lambda v)u^2(1+\lambda u)\Bigr]
\Phi(u)\Phi(v)\,du.
\]

Each coefficient product is at least \(1-c\), so

\[
\widehat A_L(\xi)
\ge\frac{1-c}{2}
\int(u^2+v^2)\Phi(u)\Phi(v)\,du.
\tag{L-106410.3}

Since \((u-v)^2\le u^2+v^2\) and \(\lambda\xi\le2c\),

\[
\widehat R_L(\xi)
\le2c\int(u^2+v^2)\Phi(u)\Phi(v)\,du.
\tag{L-106410.4}

Combining (L-106410.3)--(L-106410.4) gives

\[
\boxed{
0\le\widehat R_L(\xi)
\le\frac{4c}{1-c}\widehat A_L(\xi)
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
\left(\frac{4c}{1-c}\right)^2
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
\left(\frac{4c}{1-c}\right)^2
 =\left(\frac4{199}\right)^2
 =\frac{16}{39601}
 <\frac1{2400}.
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
