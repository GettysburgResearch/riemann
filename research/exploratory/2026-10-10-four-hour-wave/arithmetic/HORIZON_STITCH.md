# Global SHARP positivity from a finite-horizon/tail stitch

Status: **PROPOSED theorem, with executed directed Arb certificates.**
Scope: the literal labelled beta source and every real endpoint and power
in the indicated ranges. The critical power one and RH remain open.
This improves the sufficient threshold in `POWER_THRESHOLD.md`; it does
not replace the source or assert that a finite endpoint scan is a proof.

Write

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),\qquad
 T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},\qquad
 H_m(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^m.
\]

**Proposed theorem A-HS1.** For every real \(x\ge1\) and every real
\(m\ge1.7725\), one has \(H_m(x)>0\).

The proof consists of two analytic uniform bounds and five finite strict
inequalities. The coefficient at 67 is handled as two distinct labels.

## 1. Removal on a bounded endpoint interval

For a prime label q and \(x\ge q\), define

\[
 r_q(m,x)=q^{-1/2}
   \left(\frac{4\sqrt{x/q}-3}{4\sqrt x-3}\right)^m,
 \qquad r_q(m,x)=0\quad(x<q).
 \tag{H1}
\]

For fixed \(m>0\), this is nondecreasing in x, including the positive
activation jump at x=q. Indeed, writing \(v=\sqrt x\), the derivative of
the ratio inside the parentheses is

\[
 \frac{12(1-q^{-1/2})}{(4v-3)^2}>0.
\]

That ratio lies strictly between zero and one on the active domain, so
\(r_q(m,x)\) is nonincreasing in m.

Let

\[
 R_m(X)=\sum_{p\le X}r_p(m,X)+\mathbf1_{67\le X}r_{67}(m,X).
 \tag{H2}
\]

**Lemma A-HS2.** If \(R_{m_0}(X)<1\), then
\(H_m(x)>0\) for every real \(1\le x\le X\) and every real \(m\ge m_0\).

To prove this, use the finite active labelled subsets and level masses
\(M_k\) from the complete proof of A-SP1. If an active A is obtained by
adding label q to B, put \(y=x/n_B\). Then \(q\le y\le x\le X\), and

\[
 \frac{w_m(A)}{w_m(B)}=r_q(m,y)\le r_q(m_0,X).
\]

Summing over all k removals from each active k-subset gives

\[
 kM_k\le R_{m_0}(X)M_{k-1},\qquad k\ge1.
 \tag{H3}
\]

The non-strict inequality also holds at empty levels. Since \(M_0>0\)
and \(R_{m_0}(X)<1\), every even/odd pair is nonnegative and the first
pair is strictly positive. The finite alternating sum is positive. This
argument bounds the entire real interval, including every activation
point; it does not infer positivity between sampled endpoint values.

## 2. A sharper uniform tail bound

For \(1<m<2\), put \(a=(m+1)/2\),

\[
 B(a)=\frac{1-67^{-a}}{\zeta(a)},\qquad
 E_*(m)=\frac{68}{67}
       \left[\frac{3m}{2(2-m)}+\frac2{m-1}\right]+2.
 \tag{H4}
\]

**Lemma A-HS3.** For every real \(x\ge1\),

\[
 H_m(x)\ge4^m\left[B(a)x^{m/2}-E_*(m)\sqrt x\right].
 \tag{H5}
\]

The exact majorant \(|\beta(n)|\le1+\mathbf1_{67\mid n}\) improves
the earlier constant \(|\beta(n)|\le2\). For \(b=m/2\in(0,1)\), the
decreasing-integral estimate gives

\[
 \sum_{n\le x}|\beta(n)|n^{-b}
 \le\frac{68}{67}\frac{x^{1-b}}{1-b}.
 \tag{H6}
\]

The second progression is \(67^{-b}\sum_{k\le x/67}k^{-b}\);
it is zero if x/67<1 and obeys the same bound otherwise. Similarly the
uniform tail estimate \(\sum_{n>y}n^{-a}\le y^{-a}+y^{1-a}/(a-1)\),
valid also for \(0<y<1\), gives

\[
 \sum_{n>x}|\beta(n)|n^{-a}
 \le2x^{-a}+\frac{68}{67}\frac{x^{1-a}}{a-1}.
 \tag{H7}
\]

Use the absolutely convergent beta series \(\sum\beta(n)n^{-a}=B(a)\).
On n<=x, write the kernel as
\(4^m(x/n)^{m/2}(1-3\sqrt{n/x}/4)^m\).
The real-power Bernoulli bound \(0\le1-(1-z)^m\le mz\) for
\(0\le z\le3/4\) bounds the kernel modification by
\((3m/(4\sqrt x))\sum_{n\le x}|\beta(n)|n^{-m/2}\).
Multiply this error and (H7) by \(4^m x^{m/2}\), and use
\(2x^{-1/2}\le2\sqrt x\). Equations (H6) and (H7) then give exactly
(H5).

On \([3/2,2)\), E_* is increasing because

\[
 E_*'(m)=\frac{68}{67}
       \left[\frac3{(2-m)^2}-\frac2{(m-1)^2}\right]>0.
 \tag{H8}
\]

B(a) is positive and increasing on a>1: both its numerator and
\(1/\zeta(a)=\prod_p(1-p^{-a})\) increase there. The latter
monotonicity also follows termwise from its positive Euler product.
Thus, for a slab \([m_0,m_1]\subset[3/2,2)\), the strict inequality

\[
 B((m_0+1)/2)X^{(m_0-1)/2}>E_*(m_1)
 \tag{H9}
\]

implies H_m(x)>0 simultaneously for every \(m\in[m_0,m_1]\) and
every real x>=X. Combining (H9) with A-HS2 covers all real x>=1.

## 3. Executed finite certificate and interval coverage

`verify_horizon_stitch.py` evaluates (H2) and (H9) in Arb directed balls
at 192-bit precision, with exact rational slab endpoints and coefficients.
It enumerates all primes through 40000 with a complete Eratosthenes sieve
(4203 primes, last prime 39989), includes one additional 67 term, and
requires the *entire* ball to satisfy each strict comparison. It checks
all ratio domains and the absence of gaps between the power slabs.

| Power slab | X | Certified 1-R_m0(X), lower-scale decimal | Certified margin in (H9), lower-scale decimal |
|---|---:|---:|---:|
| [1.7725, 1.773] | 29200 | 0.000089800787164 | 0.0484568309370 |
| [1.773, 1.774] | 30000 | 0.000221961617428 | 0.218304338064 |
| [1.774, 1.778] | 32000 | 0.000387931034537 | 0.520726649617 |
| [1.775, 1.79] | 35000 | 0.000321717003117 | 0.500771316106 |
| [1.78, 1.81] | 40000 | 0.003230018000459 | 0.608011169142 |

The retained JSON balls, rather than the rounded table, are the finite
certificate. The five intervals cover [1.7725,1.81]; overlaps are
intentional. A-SP1 and its independent exact rational certificate cover
every m>=1.80206853774. Since 1.80206853774<1.81, their union covers
every m>=1.7725 and proves A-HS1 subject to review of the analytic lemmas.

Normal and optimized Python runs are retained separately and must be
byte-identical. The checker uses explicit guards, never Python assertions.
It does not certify any bound at m=1, any zeta zero census, or RH. The
infinite tail and all-real monotonicity arguments are mathematical proofs
above, not machine formalizations.
