# R-100510 — The complete quadratic Harnack chain does not control critical weighted variation

Claim ID: `R-100510`
Status: **PROVED EXACT ANALYTIC COUNTERMODEL**
Created: 2026-08-20
Depends on: `L-100511`
RH status: **unproved**

The inequalities in `L-100511` are strong but do not, by themselves, imply the
critical downward-variation estimate.

Let

\[
G(u)
=
1+\varepsilon e^{-u/2}\cos u,
\qquad
\varepsilon=\frac1{100},
\qquad
u\ge0.
\]

Then \(G(u)\to1\), and

\[
G(u)\ge1-\varepsilon>0.
\]

The perturbation multiplier for \(G+G'\) is

\[
1+\left(-\frac12+i\right)=\frac12+i,
\]

whose modulus is \(\sqrt5/2\). Hence

\[
G+G'>1-\frac{\sqrt5}{200}>0.
\]

The perturbation multiplier for \(G+3G'+2G''\) is

\[
\left(1-\frac12+i\right)
\left(1+2\left(-\frac12+i\right)\right)
=
-2+i,
\]

whose modulus is \(\sqrt5\). Hence

\[
G+3G'+2G''
>
1-\frac{\sqrt5}{100}>0.
\]

The full complex-disk family imposes, after writing
\(r^2=c^2+d^2\),

\[
\mathcal L_zG
=
G+\frac{6c+r^2}{9}G'
+\frac{2r^2}{9}G''\ge0.
\tag{R-100510.1}
\]

For \(\lambda=-\frac12+i\), the perturbation multiplier is

\[
m_z
=
1+\frac{6c+r^2}{9}\lambda
+\frac{2r^2}{9}\lambda^2.
\]

On the certified disk, \(|c|\le3\) and \(r^2\le9\), so

\[
|m_z|
\le
1+3\frac{\sqrt5}{2}
+2\frac54
<7.
\]

Therefore \(\mathcal L_zG>1-7\varepsilon>0\) simultaneously for every
complex shift in the disk.  In particular, this smooth positive function
satisfies the complete complex quadratic family, every real differential
inequality in (L-100511.5), and has a positive limit.

However,

\[
G'(u)
=
-\varepsilon e^{-u/2}
\left(\frac12\cos u+\sin u\right).
\]

On a fixed positive-length subinterval of every \(2\pi\)-period, the bracket is
at least \(1/2\). Therefore

\[
\boxed{
\int_0^U e^u\,d(-G)_+(u)
\gg
e^{U/2}.
}
\tag{R-100510.2}
\]

The critical weighted downward variation is power-sized despite:

```text
positive G;
positive G+G';
positive G+3G'+2G'';
positive limit;
finite ordinary variation.
```

Hence the quadratic and complex-disk positivity theorems do not replace the
arithmetic cancellation in the activation-free descent.
