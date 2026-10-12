# A squarefree tail improvement: global SHARP positivity above 1.737

Status: **PROPOSED theorem, with directed finite certificates; independent
analytic review requested.** This packet preserves the literal beta source
and kernel. The theorem covers all real endpoints and all real powers in
its stated range. It does not prove the critical power one or RH.

Use the definitions of beta, T and H_m in `HORIZON_STITCH.md`. Put
\(d=1/\zeta(2)\) and \(K=68/67\).

**Proposed theorem A-SF1.** For every real \(x\ge1\) and every real
\(m\ge1.737\), one has \(H_m(x)>0\).

The finite-horizon argument is A-HS2. The new ingredient is a rigorous
squarefree prefix asymptotic, including its favorable constant. Uniform
tail positivity is established with an explicit derivative guard.

## 1. Elementary squarefree counting with an explicit error

Let \(Q(x)=\sum_{n\le x}\mu(n)^2\). For all real x>=1,

\[
 |Q(x)-dx|\le2\sqrt x.
 \tag{S1}
\]

Indeed, \(\mu(n)^2=\sum_{h^2\mid n}\mu(h)\), so, with
\(D=\lfloor\sqrt x\rfloor\),

\[
 Q(x)=\sum_{h\le D}\mu(h)\lfloor x/h^2\rfloor,
 \qquad d=\sum_{h\ge1}\mu(h)/h^2.
\]

The error from replacing the floors is at most D. By convexity of
\(t^{-2}\) on each interval \([h-1/2,h+1/2]\),

\[
 \sum_{h>D}h^{-2}\le\int_{D+1/2}^\infty t^{-2}\,dt
             =\frac1{D+1/2}.
\]

Writing y=sqrt(x) in [D,D+1), the total bound is
\(D+y^2/(D+1/2)\le2y\), since its difference from 2y is
\((y-D-1/2)^2/(D+1/2)-1/2\le0\). This proves (S1).

Partial summation consequently gives, for a>1 and x>=1,

\[
 \sum_{n>x}\mu(n)^2n^{-a}
 \le\frac d{a-1}x^{1-a}
       +2\left(1+\frac a{a-1/2}\right)x^{1/2-a}.
 \tag{S2}
\]

To check the constant, write the tail as
\(-Q(x)x^{-a}+a\int_x^\infty Q(t)t^{-a-1}dt\).
The main terms combine to d x^(1-a)/(a-1); bounding the endpoint and
integral errors with (S1) gives exactly (S2). This holds at integers too,
with the tail n>x excluding the atom already counted in Q(x).

## 2. The weighted squarefree prefix and its negative constant

For \(1/2<b<1\), define

\[
 C_b(Y)=1+\frac{1+Y^{-1/2}}{1-b}
       +|\zeta(b)|\left[\frac1{2b-1}+Y^{-1/2}\right],\qquad Y\ge1.
 \tag{S3}
\]

**Lemma A-SF2.** For every real x>=Y>=1,

\[
 \left|\sum_{n\le x}\mu(n)^2 n^{-b}
       -\frac d{1-b}x^{1-b}-\frac{\zeta(b)}{\zeta(2b)}\right|
 \le C_b(Y)x^{1/2-b}.
 \tag{S4}
\]

Here the constant \(\zeta(b)/\zeta(2b)\) is negative. The denominator
is positive by its Euler product; the numerator is negative from
\(\zeta(b)=\eta(b)/(1-2^{1-b})\), where the alternating eta series is
positive for every b>0.

For completeness, the elementary counting continuation identity yields,
for every real z>=1,

\[
 \sum_{k\le z}k^{-b}=\frac{z^{1-b}}{1-b}+\zeta(b)+R_b(z),
 \quad R_b(z)=-\{z\}z^{-b}
            +b\int_z^\infty\{t\}t^{-b-1}dt,
 \quad |R_b(z)|\le z^{-b}.
 \tag{S5}
\]

This is the same counting continuation used in `ZERO_FREE_MERTENS.md`,
and its integral converges for b>0. Insert (S5) into the exact identity

\[
 \sum_{n\le x}\mu(n)^2n^{-b}
  =\sum_{h\le\sqrt x}\mu(h)h^{-2b}
                   \sum_{k\le x/h^2}k^{-b}.
\]

The sum of the R_b errors is at most
\(\lfloor\sqrt x\rfloor x^{-b}\le x^{1/2-b}\).
Complete the other two h-sums to the absolutely convergent Euler sums
\(\sum\mu(h)h^{-2}=d\) and \(\sum\mu(h)h^{-2b}=1/\zeta(2b)\).
The uniform decreasing-integral tail bounds at y=sqrt(x) give

\[
 \sum_{h>\sqrt x}h^{-2}\le x^{-1}+x^{-1/2},\qquad
 \sum_{h>\sqrt x}h^{-2b}
       \le x^{-b}+\frac{x^{1/2-b}}{2b-1}.
\]

Their contributions, divided by x^(1/2-b), are at most
\((1+x^{-1/2})/(1-b)\) and
\(|\zeta(b)|[x^{-1/2}+1/(2b-1)]\), respectively. Since x>=Y,
these three bounds prove (S4). No Mertens estimate or RH input is used.

## 3. A tail inequality retaining the favorable constant

Fix 1<m<2, put b=m/2, a=(m+1)/2, and fix X>=67. For every real x>=X,
the exact bound \(|\beta(n)|\le\mu(n)^2+
\mathbf1_{67\mid n}\mu(n/67)^2\) and (S4) imply

\[
 \sum_{n\le x}|\beta(n)|n^{-b}
 \le\frac{dK}{1-b}x^{1-b}
     +(1+67^{-b})\frac{\zeta(b)}{\zeta(2b)}
     +(1+67^{-1/2})C_b(X/67)x^{1/2-b}.
 \tag{S6}
\]

Apply (S4) separately at x and x/67, both >=X/67>=1; rescaling gives
the three factors K, 1+67^-b and 1+67^-1/2 exactly. Although the middle
term is negative, (S6) remains an upper bound: (S4) gives an upper bound
for each nonnegative squarefree prefix before they are added.

The same absolute beta majorant and (S2) give

\[
 \sum_{n>x}|\beta(n)|n^{-a}
 \le\frac{dK}{a-1}x^{1-a}
   +2\left(1+\frac a{a-1/2}\right)(1+67^{-1/2})x^{1/2-a}.
 \tag{S7}
\]

Define

\[
 E_0(m)=K\left[\frac{3m}{2(2-m)}+\frac2{m-1}\right],
 \quad L(m)=-\frac{3m}{4}(1+67^{-b})\frac{\zeta(b)}{\zeta(2b)}>0,
\]
\[
 C(m,X)=(1+67^{-1/2})
          \left[\frac{3m}{4}C_b(X/67)+4+\frac2m\right].
 \tag{S8}
\]

Exactly the Bernoulli kernel-modification bound in A-HS3, now using
(S6) and (S7), yields

\[
 \frac{H_m(x)}{4^m\sqrt x}
 \ge B(a)x^{(m-1)/2}-dE_0(m)
       +L(m)x^{(m-2)/2}-\frac{C(m,X)}{\sqrt x},\qquad x\ge X.
 \tag{S9}
\]

The last tail coefficient simplifies because
\(2(1+a/(a-1/2))=4+2/m\). This accounts for every error term.

## 4. Uniform exponent slabs and the derivative guard

Take \([m_0,m_1]\subset[3/2,2)\), and set b0=m0/2 and
\(B_0=B((m_0+1)/2)>0\). Certified constants satisfying

\[
 0<L_0\le\inf_{m\in[m_0,m_1]}L(m),\qquad
 C_1\ge\sup_{m\in[m_0,m_1]}C(m,X)
 \tag{S10}
\]

give a uniform lower function

\[
 g(x)=B_0x^{(m_0-1)/2}-dE_0(m_1)
            +L_0x^{b_0-1}-C_1x^{-1/2}.
 \tag{S11}
\]

Indeed B increases and E_0 increases on this domain, as shown in (H8);
also x>=1 and L_0>0 ensure that the favorable term in (S9) is at least
L_0 x^(b0-1). The constants C_1 are held fixed for the whole tail x>=X.

Require the two strict conditions

\[
 g(X)>0,\qquad
 B_0\frac{m_0-1}{2}\sqrt X>L_0(1-b_0).
 \tag{S12}
\]

Then g is increasing for every x>=X. Differentiating (S11) and dropping
its positive last derivative bounds g' below by

\[
 x^{b_0-2}\left[B_0\frac{m_0-1}{2}\sqrt x-L_0(1-b_0)\right]>0.
\]

Thus (S12) proves positive H_m for every real tail endpoint and every
power in the slab. This derivative check is necessary here: the favorable
constant in (S9) decays with x, so a positive value of its right side at
one horizon alone would not establish the entire tail.

## 5. Executed directed certificate

`verify_squarefree_stitch.py` uses python-flint 0.9.0 and Arb at 192 bits.
For each exact rational slab it encloses the entire m interval, computes
L_0 as the directed lower endpoint of the L enclosure, and bounds C_b
over the entire b interval. Its C_1 uses the upper endpoint of C_b,
m<=m1, and 2/m<=2/m0, followed by a directed upper endpoint. Those
endpoints are exact dyadic Arb numbers; their exactness and signs are
explicit guards. Every comparison must hold for the entire resulting
ball. The checker also verifies R_m0(X)<1 by a complete prime sieve with
the additional 67 label, using the A-HS2 implementation.

| Power slab | X | Certified 1-R_m0(X), scale decimal | Certified g(X), scale decimal | Derivative-guard margin, scale decimal |
|---|---:|---:|---:|---:|
| [1.737, 1.7372] | 4640 | 0.000241615313243 | 0.000705034911762 | 6.92061337935 |
| [1.7372, 1.738] | 4680 | 0.000206556896530 | 0.00855767414401 | 6.95771461621 |
| [1.738, 1.7395] | 4700 | 0.000768806442532 | 0.0170509758141 | 6.98933252203 |
| [1.7395, 1.742] | 5000 | 0.000603240222741 | 0.185008510806 | 7.25773678140 |
| [1.742, 1.747] | 5500 | 0.000576638383920 | 0.427932841044 | 7.69510156852 |
| [1.747, 1.756] | 6500 | 0.00123564386085 | 0.918652224081 | 8.53232782725 |
| [1.756, 1.773] | 8500 | 0.00359700962195 | 1.78471140503 | 10.0805443185 |

The retained JSON balls are the certificates; the rounded table is only
for reading. The seven closed slabs cover [1.737,1.773], and A-HS1 covers
all m>=1.7725. A-HS2 covers the entire bounded endpoint interval for each
slab, while (S12) covers its whole tail. This proves A-SF1 subject to
independent review of the displayed analytic contracts.

Independent finite controls check (S1) at all integer endpoints through
1000 (608 squarefree integers), and compare (S4) with direct squarefree
weighted sums in nine cases: b=3/5,4/5,9/10 and x=67,100,1000. These
controls do not replace the infinite analytic proof. Normal and optimized
Python receipts are required to agree byte for byte; assertions are never
used as guards. RH and critical-power-one flags remain false.
