# The complete beta energy has an exact assembled Perron--Fourier bridge

Status: **exact source reindexing, exact one-variable assembled wavelet, and
exact absolutely convergent Perron--Fourier formula; the boundary-contour
estimate, the assembled cancellation, RH, and GRH remain open**

Bounded exact replay:
[`ffps_assembled_beta_perron_fourier_bridge.py`](ffps_assembled_beta_perron_fourier_bridge.py).

Frozen sources:

1. the compact boundary-field near-correlation criterion at
   `b870366141fe8d5f43d5b81f6e50a67d2a888070`;
2. the primitive rho/wavelet packet at that same release head.

The replay pins all imported blobs. It uses no zeta zero, prime interval,
curve, point count, or floating-point inference.

## 0. Outcome

Put

\[
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
 \qquad
 (c_0,c_1,c_2)=(1,-2,1).
\tag{0.1}
\]

If `67` does not divide the squarefree integer `u`, then

\[
 \beta(67^i u)=c_i\mu(u)\quad(0\le i\le2),
 \qquad
 \beta(67^i u)=0\quad(i\ge3).
\tag{0.2}
\]

Let \(\mathcal R\) be the compact even autocorrelation from the
boundary-field packet and

\[
 \mathcal E(X)=
 \sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right).
\tag{0.3}
\]

The predecessor proves

\[
 \boxed{\mathrm{RH}\Longleftrightarrow\mathcal E(X)=X^{o(1)}.}
\tag{0.4}
\]

Every nonzero source pair has a unique representation

\[
 m=67^i g a,
 \qquad
 n=67^j g b,
 \qquad 0\le i,j\le2,
\tag{0.5}
\]

where `g,a,b` are squarefree, pairwise coprime, and prime to `67`. Put
\(N=ab\). For squarefree `67`-free \(N\), define

\[
 H_N(Y)=
 \sum_{\substack{g\le Y,\ g\ {\rm squarefree}\\
                   (g,67N)=1}}{1\over g}
\tag{0.6}
\]

and the complete assembled divisor wavelet

\[
\begin{aligned}
 \mathscr W_X(N)
 ={}&\sum_{i,j=0}^2{c_ic_j\over67^{(i+j)/2}}
 \sum_{a\mid N}
 \mathcal R\!\left(
   \log{67^{i-j}a^2\over N}
 \right)\\
 &\qquad\qquad\times
 H_N\!\left(
 {X\over\max(67^ia,67^jN/a)}
 \right).
\end{aligned}
\tag{0.7}
\]

Then the complete positive prefix energy, including its diagonal, is exactly

\[
 \boxed{
 \mathcal E(X)=
 \sum_{\substack{N\ {\rm squarefree}\\67\nmid N}}
 {\mu(N)\over\sqrt N}\,\mathscr W_X(N).}
\tag{0.8}
\]

The sum is finite because (0.6) vanishes when its argument is below one.
Consequently the source-assembled one-variable statement

\[
 \boxed{
 \left|
 \sum_N{\mu(N)\over\sqrt N}\mathscr W_X(N)
 \right|=X^{o(1)}}
\tag{0.9}
\]

is **equivalent to RH**, not merely sufficient for it. Equation (0.9) is a
coordinate identity, not an estimate proved in this packet. Its advantage
over channelwise `PRIMCAR` is that the three exceptional orientations, the
common-factor cutoff, all divisor orientations, and all height endpoints
remain assembled before any square or triangle inequality.

The ratio support is at most 16, whereas the exceptional prime is 67.
It follows that the \(N=1\) wavelet is exactly the complete diagonal:

\[
 \boxed{
 \mathscr W_X(1)=\mathcal R(0)
 \sum_{i=0}^2{c_i^2\over67^i}H_1(X/67^i).}
\tag{0.9a}
\]

Every \(N>1\) term is off-diagonal. Thus (0.8) does not merely compress the
energy: it separates the known logarithmic diagonal from one explicit
one-variable signed off-diagonal without a further projection.

There is also a clean analytic bridge. Write

\[
 B_\beta(w)=\sum_{n\ge1}{\beta(n)\over n^w}
 ={1-67^{-w}\over\zeta(w)}
 \qquad(\Re w>1).
\tag{0.10}
\]

For \(W\in C_c^\infty((0,\infty))\), put

\[
 \mathcal E_W(X)=
 \sum_{m,n\ge1}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right)
 W\!\left({\max(m,n)\over X}\right).
\tag{0.11}
\]

Let

\[
 \widetilde W(z)=\int_0^\infty W(y)y^{z-1}\,dy,
 \quad
 s={1+z\over2},
 \quad
 \mathcal R_z(x)=\mathcal R(x)e^{-z|x|/2},
\tag{0.12}
\]

and use the Fourier convention

\[
 \widehat{\mathcal R_z}(t)
 =\int_{\mathbb R}\mathcal R_z(x)e^{-itx}\,dx.
\]

For every vertical line \(\Re(z)=c>1\), absolute convergence and
Mellin--Fourier inversion give

\[
 \boxed{
 \mathcal E_W(X)
 ={1\over2\pi i}\int_{(c)}\widetilde W(z)X^z
 \left\{
 {1\over2\pi}\int_{\mathbb R}
 \widehat{\mathcal R_z}(t)
 B_\beta(s-it)B_\beta(s+it)\,dt
 \right\}dz.}
\tag{0.13}
\]

There is no unnamed correction Euler product in (0.13). Keeping the source
assembled makes it collapse exactly to the two literal beta Dirichlet
multipliers.

For arbitrary annular \(W\in C_c^\infty((0,\infty))\), the smoothed max
correlation (0.11) is an analytic coordinate, not asserted to be a positive
Gram or an RH criterion for one fixed \(W\). There is, however, an exact
positive subclass. If \(W\) is smooth and nonincreasing on
\([0,\infty)\), equals one near zero, and has compact support, then

\[
 \boxed{
 \mathcal E_W(X)=\int_0^\infty -W'(v)\,\mathcal E(vX)\,dv\ge0.}
\tag{0.13a}
\]

This follows by integrating the sharp prefix indicator and makes the smooth
object a positive mixture of literal Gram energies. It does **not** recover
a sharp endpoint without an additional argument. The exact RH-equivalent
object in this packet remains the sharp prefix identity (0.8).

## 1. Exact primitive reindexing

Suppose \(\beta(m)\beta(n)\) is nonzero. Remove the `67`-adic exponents
\(i,j\). The remaining parts are squarefree. If their gcd is \(g\), write
them as \(ga,gb\). Squarefreeness makes \(g,a,b\) pairwise coprime.
Conversely every tuple in (0.5) gives one nonzero ordered source pair, so
this is a bijection.

The source sign becomes

\[
 \beta(m)\beta(n)
 =c_ic_j\mu(ga)\mu(gb)
 =c_ic_j\mu(a)\mu(b).
\tag{1.1}
\]

Since \(a,b\) are coprime and squarefree,

\[
 \mu(a)\mu(b)=\mu(ab)=\mu(N),
 \qquad
 {1\over\sqrt{mn}}
 ={1\over67^{(i+j)/2}g\sqrt N}.
\tag{1.2}
\]

For fixed \(i,j,N,a\), the two prefix inequalities are equivalent to

\[
 g\le {X\over\max(67^ia,67^jN/a)}.
\tag{1.3}
\]

Summing \(g\) gives (0.6), and then summing \(a\mid N\), \(i,j\), and \(N\)
proves (0.8). When \(N=1\), the support bound kills \(i\ne j\), giving
(0.9a); equality \(m=n\) is impossible for \(N>1\). No limiting argument,
density replacement, or positivity estimate enters the proof.

The bounded replay checks this bijection and coefficient normalization on
2,209 ordered source pairs with a toy exceptional prime `5`, including its
square exceptional layer. Independently, it evaluates the literal
\(N\)-, divisor-, and \(H_N\)-sums in (0.6)--(0.8): 430 primitive products
and 1,271 nonzero orientations reproduce the same exact 522-dimensional
square-root vector and digest. The toy prime changes only the finite replay
size;
the proof above is for `67`.

## 2. Why the local Euler product closes exactly

The primitive decomposition has four states at every prime \(p\ne67\):

| state | local factor |
|---|---:|
| absent | `1` |
| in the common squarefree factor \(g\) | \(p^{-2s}\) |
| in the left primitive core | \(-p^{-s+it}\) |
| in the right primitive core | \(-p^{-s-it}\) |

Their sum factors:

\[
 \boxed{
 1+p^{-2s}-p^{-s+it}-p^{-s-it}
 =(1-p^{-s+it})(1-p^{-s-it}).}
\tag{2.1}
\]

This is the exact Fourier--hyperbola cancellation that disappears if the
common-factor state, the two orientations, or their signs are estimated
separately.

At `67`, the one-variable source polynomial is

\[
 1-2x+x^2=(1-x)^2.
\tag{2.2}
\]

Hence the exceptional pair factor is

\[
 (1-67^{-s+it})^2(1-67^{-s-it})^2.
\tag{2.3}
\]

Combining (2.1) over \(p\ne67\) with (2.3) gives precisely

\[
 B_\beta(s-it)B_\beta(s+it).
\tag{2.4}
\]

Thus the initially plausible correction factor \(H_{d,t}(z)\) is
identically one for the complete source. Correction products arise only
after source states or incidence modes are separated.

## 3. Proof of the Perron--Fourier formula

Mellin inversion in (0.11) contributes

\[
 X^z\max(m,n)^{-z}.
\]

For \(x=\log(m/n)\), one has

\[
 \max(m,n)=\sqrt{mn}\,e^{|x|/2},
\]

and therefore

\[
 {\max(m,n)^{-z}\over\sqrt{mn}}
 =(mn)^{-s}e^{-z|x|/2}.
\tag{3.1}
\]

Fourier inversion of \(\mathcal R_z\) changes the remaining ratio factor
into \(m^{it}n^{-it}\). Since \(\Re(s)>1\), the two source sums are
absolutely convergent and separate:

\[
 \sum_{m,n\ge1}
 {\beta(m)\beta(n)\over m^{s-it}n^{s+it}}
 =B_\beta(s-it)B_\beta(s+it).
\tag{3.2}
\]

Compact support alone would not justify absolute Fourier inversion. Here
one uses the stronger imported BV regularity. Writing
\(\widetilde K(x)=K(-x)\), the distributional second derivative of
the autocorrelation is a finite measure:

\[
 D^2\mathcal R=(DK_{\rm bd})*(D\widetilde K_{\rm bd}).
\]

Multiplication by the compact piecewise-\(C^2\) function
\(e^{-z|x|/2}\) preserves that property. Hence
\(\widehat{\mathcal R_z}(t)=O_z((1+|t|)^{-2})\), so its Fourier transform is
integrable. Together with rapid vertical decay of the Mellin transform and
absolute Dirichlet convergence, this justifies Fubini. Equations
(3.1)--(3.2) prove (0.13).

The formula is initially asserted only on \(\Re(z)>1\). Moving it toward
\(\Re(z)=0\) is the arithmetic problem, not a formal consequence of RH. On
the boundary, the two beta multipliers contain reciprocal zeta factors on
the critical line. Taking their absolute values would demand negative
moments and zero-derivative information substantially stronger than the
source-equivalent criterion. Any viable contour argument must retain the
signed \(t\) integral, its residues, and the exceptional-channel assembly.

## 4. A high-pass notch does not automatically survive the max tilt

Let \(K\) be a compact boundary kernel and, for fixed \(\varepsilon>0\), let

\[
 K_r=\Delta_\varepsilon^r K.
\]

If \(\mathcal R_r\) is its autocorrelation, then on the
translation-invariant Fourier line

\[
 \widehat{\mathcal R_r}(t)
 ={|1-e^{-i\varepsilon t}|^{2r}\over\varepsilon^{2r}}
 |\widehat K(t)|^2.
\tag{4.1}
\]

Thus \(\mathcal R_r\) has a zero of order \(2r\) at \(t=0\). In the Perron
formula, however, the actual kernel is

\[
 \mathcal R_{r,z}(x)=\mathcal R_r(x)e^{-z|x|/2}.
\tag{4.2}
\]

The nonconstant even tilt in (4.2) does not commute with the Fourier notch.
Although

\[
 \widehat{\mathcal R_r}(0)=\int\mathcal R_r(x)\,dx=0,
\]

one generally has

\[
 \widehat{\mathcal R_{r,z}}(0)\ne0
 \qquad(z\ne0).
\tag{4.3}
\]

The replay proves this exact algebraic firewall for difference orders
\(r=1,2,3\): the untwisted autocorrelation has \(2r\) vanishing signed
moments, while multiplication by the rational toy tilt \(2^{-|x|}\) refills
the zero mode in every row.

This does not refute the band-pass route. The leakage tends to zero with
\(z\), and a contour such as \(\Re(z)\asymp1/\log X\) may still convert it
into a subpower cost. It proves that the phrase “the notch kills \(t=0\)”
is insufficient once the physical max cutoff is restored. The near-zero
Perron leakage must be estimated explicitly.

## 5. The first unresolved analytic statement

Name the signed boundary-contour problem `ASMPERRON`:

> Move the source-assembled formula (0.13) to a contour approaching
> \(\Re(z)=0\), paying only \(X^{o(1)}\), while retaining the signed \(t\)
> integral, all beta local states, all critical-line residues, and the
> endpoint limit.

An `ASMPERRON` theorem strong enough to recover the sharp prefix energy
would prove (0.9), hence RH. No such estimate is proved here. The exact
formula does identify where a proof must act:

1. the complete local algebra is already closed;
2. there is no missing correction Euler product;
3. the remaining difficulty is boundary control of a signed product of two
   reciprocal-zeta sources;
4. channelwise or modewise absolute values discard the cancellation that
   produced (2.1).

A next attack should compare three coordinates without separating them:

```text
sharp assembled wavelet (0.8)
  <-> source-assembled Perron--Fourier integral (0.13)
  <-> band-pass/reflection field before the max tilt.
```

## 6. Proof and scope ledger

| statement | grade |
|---|---|
| complete beta `67`-adic coefficients `(1,-2,1)` | **PROVED EXACT** |
| unique `(i,j,g,a,b)` primitive reindexing | **PROVED EXACT** |
| one-variable assembled wavelet identity (0.8) | **PROVED EXACT** |
| assembled-wavelet RH equivalence (0.9) | **PROVED FROM THE FROZEN PREFIX-ENERGY EQUIVALENCE** |
| full diagonal equals the \(N=1\) wavelet (0.9a) | **PROVED EXACT** |
| positive smooth-prefix mixture (0.13a) | **PROVED EXACT** |
| generic four-state local factorization (2.1) | **PROVED EXACT** |
| exceptional square factorization (2.2)--(2.3) | **PROVED EXACT** |
| smoothed Perron--Fourier identity (0.13) on \(\Re(z)>1\) | **PROVED BY ABSOLUTE CONVERGENCE AND BV FOURIER DECAY** |
| exact \(t=0\) notch before the max tilt | **PROVED FOR FIXED DIFFERENCES** |
| automatic preservation of that notch under the Perron max tilt | **FALSE IN ABSTRACT; EXACT TOY FIREWALL** |
| `ASMPERRON`, a boundary-contour estimate, or an RH proof | **OPEN / NOT PROVED** |

No external novelty claim is made without a dedicated comparison.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py --check
python -B -O research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py --check
python -B -m unittest tests.test_ffps_assembled_beta_perron_fourier_bridge
python -B -O -m unittest tests.test_ffps_assembled_beta_perron_fourier_bridge
```

The replay checks:

- all frozen source blobs;
- the generic four-state factorization;
- the exceptional beta square;
- 2,209 exact ordered-pair reindexings;
- a second, literal \(N\)-divisor-\(H_N\) replay over 430 primitive products;
- equality in a 522-dimensional square-root basis;
- \(2r\) vanishing autocorrelation moments for \(r=1,2,3\);
- exact refilling of the toy zero mode by a nonconstant max tilt;
- canonical JSON and explicit resource caps.
