# L-106411 — Reflected Xi endpoint channel and the complete four-channel budget

Claim ID: `L-106411`  
Status: **PROVED EXACT FOR THE TRUNCATED TWO-BOUNDARY XI SOURCE**  
Created: 2026-08-24  
Depends on: `L-105260`, `L-106410`  
RH status: **not assumed**

Retain the notation of `L-106410`, and write the real truncated Xi source as
the sum of its positive- and negative-frequency halves.  The two-boundary
Paley--Wiener polarization has two same-sign Hankel channels and two reflected
Toeplitz orientations.

Let \(u,v\in[0,L]\), put \(c=\lambda L<1\), and consider one reflected
orientation.  The positive denominator source density is

\[
\begin{aligned}
a_\times(u,v)={}&
 (1-\lambda u)v^2(1-\lambda v)\\
&+(1+\lambda v)u^2(1+\lambda u),
\end{aligned}
\tag{L-106411.1}

while the absolute endpoint-Turán density is

\[
r_\times(u,v)=2\lambda(u+v)^2|u-v|.
\tag{L-106411.2}

These are the cross-frequency terms in

\[
-(\Xi+i\lambda\Xi')(\Xi''-i\lambda\Xi''')
\]

and

\[
(\Xi-i\lambda\Xi')(\Xi''+i\lambda\Xi''')
 -(\Xi+i\lambda\Xi')(\Xi''-i\lambda\Xi'''),
\]

respectively.

## 1. Reflected-channel bound

Since \(0\le\lambda u,\lambda v\le c\),

\[
a_\times(u,v)
\ge(1-c)^2(u^2+v^2).
\tag{L-106411.3}

Moreover,

\[
(u+v)^2\le2(u^2+v^2),
\qquad |u-v|\le L,
\]

so

\[
r_\times(u,v)
\le4c(u^2+v^2).
\tag{L-106411.4}

Therefore

\[
\boxed{
0\le r_\times(u,v)
\le\frac{4c}{(1-c)^2}a_\times(u,v).
}
\tag{L-106411.5

The sign of the reflected Turán density is fixed on each orientation
\(u-v>0\) or \(u-v<0\).  Integration along the corresponding difference line
therefore preserves (L-106411.5) for the physical Toeplitz kernel.

At \(c=1/200\),

\[
\boxed{
\left(\frac{4c}{(1-c)^2}\right)^2
 =\left(\frac{800}{39601}\right)^2
 =\frac{640000}{1568239201}
 <\frac1{2400}.
}
\tag{L-106411.6

## 2. Complete two-boundary budget

`L-106410` gives the squared same-sign ratio

\[
\left(\frac8{199}\right)^2=\frac{64}{39601}<\frac1{600}.
\]

Paying both same-sign orientations and both reflected orientations
conservatively gives

\[
\boxed{
2\frac{64}{39601}
+2\frac{640000}{1568239201}
=\frac{6348928}{1568239201}
<\frac1{200}.
}
\tag{L-106411.7

Thus, at the source-normalized finite-section Hilbert--Schmidt level, the
complete endpoint-Turán four-channel packet consumes less than one half of one
percent of the corresponding positive endpoint-denominator bank.

## 3. Scope

The estimate is exact after:

```text
positive/negative Xi Fourier splitting;
truncation to [0,L];
two-boundary Toeplitz--Hankel polarization;
source normalization by the positive endpoint-denominator bank.
```

It does not itself prove that the cofinal Xi endpoint frame has this bank as
its reference Gram, nor that the Fourier tail, endpoint and confluent ledgers
are `o(d_T)`.  That final bank-identification interface is isolated in
`T-106410`.
