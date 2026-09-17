# 02. Reciprocal-sum hierarchies, natural families, and the reverse direction

**Status:** classical inputs plus explicit derived arguments. The nested Golomb density and direct multi-residue dispute remain OPEN. References are keyed in [SOURCES](SOURCES.md).

## 1. Counting, harmonic mass, and the scale of a family

For a locally finite positive family A, counted with its stated multiplicities, write
\[
A(x)=\#\{a\in A:a\le x\},\qquad H_A(x)=\sum_{a\le x}a^{-1}.
\]
For subsets of the positive integers, partial summation gives
\[
H_A(x)=A(x)/x+\int_1^x A(t)t^{-2}\,dt.
\]
Hence, for fixed k,
\[
A(x)\sim\frac{x}{\log x\log_2x\cdots\log_kx}
\quad\Longrightarrow\quad H_A(x)\sim\log_{k+1}x.
\]
The corresponding nth element obeys \(a_n\sim n\log n\cdots\log_kn\). These statements assume the counting asymptotic; a harmonic asymptotic alone does not imply it. Large gaps and clustering can survive harmonic averaging.

The local spacing heuristic for a smooth target F is
\[
\Delta a\simeq\frac1{aF'(a)},\qquad dn/da\simeq aF'(a).
\]
It is an average-density calculation, not a theorem about individual gaps and not an answer to the request for independently natural families.

The prime-density sieve heuristic uses
\(\prod_{p\le y}(1-1/p)\sim e^{-\gamma}/\log y\).
Independent survival all the way to \(\sqrt x\) does not give the exact prime-density constant. This warning becomes more important for recursive sieves.

## 2. Golomb primes: a natural third-log family

Start G at 3. Select the least larger prime p for which no earlier selected g divides p-1:
\[
G=\{3,5,17,23,29,53,83,\ldots\}.
\]
Erdős's theorem [E61] supplies
\[
G(x)\sim\frac{x}{\log x\log_2x},\qquad
V_G(x):=\prod_{g\le x}\left(1-\frac1{g-1}\right)\sim\frac1{\log_2x}.
\]
Define the absolutely convergent correction
\[
D_G=\sum_{g\in G}\left[-\log\left(1-\frac1{g-1}\right)-\frac1g\right].
\]
Taking logarithms of V_G gives
\[
H_G(x)=\log_3x-D_G+o(1).
\]
The handoff reported \(D_G\approx0.45966185\). This number is preserved as historical, not as a newly certified constant with a tail enclosure.

### Exact recursive source

Set g(p)=1 if p belongs to G, with g(2)=0, and
\[
a_G(n)=\prod_{q\mid n}(1-g(q)).
\]
For odd primes,
\[
g(p)=a_G(p-1).
\]
All prime divisors of p-1 are smaller than p, so this is genuinely recursive. It connects multiplicative restrictions with shifted-prime evaluation, rather than ordinary multiplication of Golomb primes into primes.

## 3. Direct multiple residues versus nested sieving

For a direct greedy rule forbidding r fixed nonzero classes modulo each selected prime, the simple survival model is
\[
V(x)\approx Ce^{-rH(x)},\qquad
H'(x)\approx\frac{Ce^{-rH(x)}}{x\log x}.
\]
It predicts
\[
H(x)\approx\frac1r\log_3x+O(1),\qquad
B(x)\approx\frac{x}{r\log x\log_2x}.
\]
The supplied handoff reports that an extension printed at the end of [E61] instead has an iterated-log denominator depending on r. Earlier chat claimed an argument against that printed formula using small-modulus sieves, Brun–Titchmarsh and two-linear-form bounds. A complete such argument was not supplied in this conversation. **This packet does not declare the printed extension disproved.** Reconcile the exact rule, exceptional primes, hypotheses, and uniform sieve remainders before choosing a theorem statement. Meijer [M74] is a relevant primary source, not an automatic resolution.

### The proposed nested construction

Inside G, start R at 5 and select p if p avoids 2 modulo every earlier r in R. The handoff listed
\[
R=\{5,23,29,53,83,113,149,173,269,293,\ldots\}.
\]
Starting at 3 fails: every later G-prime is 2 modulo 3. The repair at 5 removes that immediate obstruction, but does not itself prove infinitude.

Writing b_R(n) for the indicator of integers without a prime divisor in R,
\[
r(p)=1_{p\ge5}g(p)b_R(p-2).
\]
The base G already forbids 0 and 1 modulo r. Conditional equidistribution across the remaining r-2 classes suggests survival factors
\[
V_R(z)=\prod_{r\le z}\left(1-\frac1{r-2}\right)
\]
and the model
\[
H_R'(x)\approx\frac{Ce^{-H_R(x)}}{x\log x\log_2x}.
\]
It predicts \(H_R(x)\sim\log_4x\) and \(R(x)\sim x/(\log x\log_2x\log_3x)\). These are **heuristic targets**.

A sufficient analytic package would estimate the number U_G(x,z) of G-primes surviving the R restrictions up to z by \(G(x)V_R(z)(1+o(1))\), bound the large-modulus exclusions E_G(x,z) by \(o(G(x)V_R(z))\), and show \(H_R(x)-H_R(z)=o(1)\). The anticipated local factor for a squarefree d supported on R is \(\prod_{r\mid d}(r-2)^{-1}\), but one needs useful weighted control uniformly over growing d. Ordinary prime equidistribution alone is not that theorem.

## 4. A complete digit-selection tower

Fix integer base b>=2; let \(d_b(n)=\lfloor\log_b n\rfloor+1\). Define
\[
S_0=\mathbb N,\quad S_{k+1}=\{p\text{ prime}:d_b(p)\in S_k\}.
\]
Then S_1 is the ordinary primes; S_2 is the primes with a prime number of digits (decimal example [OEIS]). The sets are nested.

For an m-digit prime block, classical PNT with its exponential error and partial summation give
\[
\sum_{b^{m-1}\le p<b^m}\frac1p
=\log\frac m{m-1}+O_b(e^{-c_b\sqrt m})
=\frac1m+O_b(m^{-2}+e^{-c_b\sqrt m}).
\]
The m=1 endpoint contributes only a constant. The errors are summable, and a partial last block costs O(1/m). Thus for any fixed set A of positive digit lengths,
\[
H_{T_b(A)}(x)=H_A(d_b(x))+C_{A,b}+o(1),\quad
T_b(A)=\{p:d_b(p)\in A\}.
\]
Induction gives, for fixed k>=1,
\[
H_{S_k}(x)=\log_{k+1}x+C_{k,b}+o(1).
\]
One can start instead from G: primes whose digit count is a Golomb prime have harmonic growth \(\log_4x\).

This tower is unconditional given classical PNT. It is base-dependent and highly clustered: entire prime digit blocks are retained or discarded. It does not imply a smooth ordinary count \(x/(\log x\cdots\log_kx)\). Using \(\lfloor\log p\rfloor\) is a related logarithmic-block construction, not a new base-independent arithmetic theorem.

## 5. Fractional and other scales

Integers representable as a sum of two squares, counted once, obey the Landau–Ramanujan law \(B(x)\sim Kx/\sqrt{\log x}\), hence
\[
H_B(x)\sim2K\sqrt{\log x}.
\]
This is a natural fractional level. The continuously parameterized weights \(d_\alpha\) give another, algebraically more useful family:
\[
\sum_{n\le x}d_\alpha(n)/n\sim(\log x)^\alpha/\Gamma(1+\alpha),\quad\alpha>0.
\]
See Chapter 04. Families sharing this exponent need not share analytic continuation.

Prime-indexed primes satisfy \(p_{p_n}\sim n(\log n)^2\), so their reciprocals converge: they are not a third-log family. Fixed k-almost-prime sums have generating function
\[
\sum_{k\ge0}P_k(s)z^k=\prod_p(1-zp^{-s})^{-1}
=\exp\left(\sum_{m\ge1}\frac{z^mP(ms)}m\right).
\]
For example \(P_2(s)=(P(s)^2+P(2s))/2\). This exact hierarchy produces powers of logarithms, not successive logarithms.

## 6. Reverse scales: definitions matter

A subset of positive integers obeys \(H_A(x)\le\log x+O(1)\). Larger growth requires a different object. Complex reciprocal sums may cancel and have no ordered notion of positive growth; sizes such as |z| must be specified.

- The distinct pronic integers n(n+1) satisfy \(\sum1/[n(n+1)]=1\): a finite-limit branch.
- The real sequence \(a_n=\sqrt{2n}\) has \(H_A(y)\sim y\).
- The recurrence \(a_{n+1}-a_n=1/a_n\) telescopes exactly: \(\sum_{n\le N}1/a_n=a_{N+1}-a_1\), with \(a_n\sim\sqrt{2n}\).
- Counting each lattice point z in \(\mathbb Z^2\setminus\{0\}\) by its radius, \(\sum_{|z|\le y}|z|^{-1}=2\pi y+O(\log y)\). Counting distinct radii would be a different family. Summing 1/z on a symmetric complex lattice cancels instead.

The tailored recurrence \(F(a_{n+1})-F(a_n)=1/a_n\) realizes a desired F, but is not an independently motivated discovery. For F(y)=e^y, the smooth count is \((y-1)e^y+C\) and the inverse involves \(1+W(n/e)\). For F(y)=e^{e^y}, the asymptotic inverse is
\[
a_n=\log_2n-\frac{\log_3n}{\log n}+o\left(\frac{\log_3n}{\log n}\right).
\]
These are inverse-density models, not preferred canonical sequences.

### Logarithmic zeta-zero heights

Count positive ordinates gamma of ALL nontrivial zeros with multiplicity, without assuming RH. The Riemann–von Mangoldt formula gives
\[
N(T)=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right)+O(\log T).
\]
Assign size \(a_\gamma=\log(\gamma/(2\pi))\), removing finitely many nonpositive sizes. Then the size count is \(e^y(y-1)+O(y)\), so partial summation gives
\[
\sum_{a_\gamma\le y}a_\gamma^{-1}\sim e^y.
\]
Before this change of coordinate, \(\sum_{0<\gamma\le T}1/\gamma=(4\pi)^{-1}\log^2(T/(2\pi))+C+o(1)\); see [BPT]. Neither law determines the zeros' real parts.

### Divisor marking links the forward and backward towers exactly

For A subset of integers >=2, let
\[
c_A(n)=\#\{a\in A:a\mid n\}.
\]
This counts an integer together with a distinguished A-divisor. Exactly,
\[
\sum_{n\le X}c_A(n)=\sum_{a\le X}\lfloor X/a\rfloor
=XH_A(X)+O(A(X)),
\quad
\sum_n c_A(n)n^{-s}=\zeta(s)D_A(s).
\]
If \(H_A(X)\sim\log_kX\), partial summation gives
\[
\sum_{n_0\le n\le X}\frac{c_A(n)}{\log_kn}\sim X.
\]
In size coordinate \(a=\log_kn\), with multiplicity c_A(n), the reciprocal sum through y is therefore \(\sim\exp_k y\).

For A=all nonunit integers, c_A=d(n)-1 and k=1; for A=primes, c_A=omega(n) and k=2; for A=G, c_A=omega_G(n) and k=3. The multiplicities are intrinsic divisor counts, while the size coordinate is an explicit choice and is not claimed uniquely canonical.

For exponential-size families the ordinary Dirichlet series in that size can diverge for every s. A Laplace transform may replace it; e.g. \(\sum(d(n)-1)e^{-s\log n}=\zeta(s)(\zeta(s)-1)\). At double-exponential density even a usual Laplace kernel can be insufficient.

## 7. Historical numerical panel

The handoff reported counts through 10^7:

| Family | Count | Reciprocal sum |
|---|---:|---:|
| G, seed 3 | 142724 | 0.9983782461 |
| Direct avoid 1 and 2, seed 5 | 111122 | 0.7169315505 |
| Nested avoid 2 inside G, seed 5 | 73300 | 0.4701347012 |

These are **HISTORICAL-UNREPLAYED**: no generator/output for this panel was supplied. Ratios normalized by \(x/(\log x\log_2x)\) were reportedly about 0.6395, 0.4979 and 0.3284. Even the established G-law is far from its limiting ratio at that range. These values do not distinguish iterated logarithmic asymptotics reliably and are not used as proof dependencies.
