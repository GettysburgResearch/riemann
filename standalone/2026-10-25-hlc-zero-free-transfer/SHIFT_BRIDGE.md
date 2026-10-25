# Shifted-prime cancellation and a quantitative bridge to zero-free half-planes

Research note for the review of Guangshi Lü, Zhiwei Wang and Jie Wu,
*On the Hardy–Littlewood–Chowla conjecture*, arXiv:2610.20242v1,
14 October 2026. Prepared 25 October 2026.

**Status.** The transport identity and its conditional zero-free consequence
below are proved here. The required power bound for the full averaged
correlation is not proved here and is not supplied by Theorem 1 of the paper.
There is no new unconditional zero-free boundary in this note. No claim of
literature novelty is made for this elementary smoothing argument.

## 1. What is actually available from the new paper

Theorem 1, p. 3, claims

\[
 \sum_{p\le x}\mu(p+2)=o(\pi(x)),
 \qquad \sum_{n\le x}\Lambda(n)\mu(n+2)=o(x).
\]

The statement concerns the fixed shift 2. Its main intermediate Type II sum,
(4.2), pp. 14–15, is

\[
 \sum_{m,n}\alpha_m\beta_n\mu(mn+2)W(mn+2),
 \quad \alpha_m=\mu(m)R_Z(m)m^{iv}.
\]

The determinant equation after Cauchy is
\(bmn-ars=2(a-b)\), (4.8), p. 16. Proposition 4.2 removes minor arcs with
arbitrary logarithmic precision. Proposition 5.3, p. 42, estimates the major
arcs using the special Möbius coefficient. Equation (5.17), p. 45, gives
logarithmic precision for the auxiliary-weighted sums.

These are not fixed power savings. In particular, the final unweighting,
(5.18)–(5.19), pp. 45–46, first fixes an integer b, lets x tend to infinity,
and then lets b tend to infinity. The result is o(x), without a stated
uniform rate when b, the shift, or the number of prime bands grows with x.
The auxiliary prime scales are subpolynomial:
\(Y=\exp(O_K((\log x)^{0.2}))\).

The paper's claimed theorem is a potential major advance on additive parity
correlations. It is not, by its stated strength, a power-saving theorem for
the Mertens function or a theorem about an Euler product whose denominator
is zeta. The independent audit of the paper is a separate task; none of
the arguments below assumes that every lemma of the paper has been validated.

## 2. A transport theorem with two explicit summatory inputs

Define

\[
 M(t)=\sum_{n\le t}\mu(n),\qquad
 E(t)=\psi(t)-t=\sum_{m\le t}\Lambda(m)-t,
\]

and extend both functions by zero at t=0. Let
\(\beta_M,\beta_P\ge0\), and suppose explicitly that

\[
 |M(t)|\le C_M(1+t)^{\beta_M},\qquad
 |E(t)|\le C_P(1+t)^{\beta_P}.
 \tag{2.1}
\]

These are premises. A numerical boundary copied from another research
packet is not silently substituted for them.

Let \(W\in C_c^1((1,2))\), \(K\in C_c^2((1,2))\), and
\(\kappa=\int_1^2 K(v)\,dv\ne0\). Let \(1\le H\le X/4\). Define

\[
 C_h(X;W)=\sum_{n\ge1}\mu(n)\Lambda(n-h)W(n/X),
\]

where \(\Lambda(m)=0\) for nonpositive m, and define the signed average

\[
 S_H(X;W,K)=\sum_{h\in\mathbb Z}K(h/H)C_h(X;W).
 \tag{2.2}
\]

Only \(H<h<2H\) occurs. This is a signed sum of correlations, not the sum
of their absolute values. Put \(M_W(X)=\sum_n\mu(n)W(n/X)\).

### Theorem 2.1: exact centered remainder and power transfer

Under (2.1),

\[
 \frac{S_H(X;W,K)}{\kappa H}
 =M_W(X)+O_{W,K,C_M,C_P,\beta_M,\beta_P}
 \left(
 \frac{X^{\beta_M+\beta_P}}{H}
 +\frac{X^{\beta_M+\beta_P+1}}{H^2}
 \right).
 \tag{2.3}
\]

The remainder before division by \(\kappa H\) has the exact representation

\[
\begin{split}
 R_H&:=S_H-\kappa H M_W\\
 &=-\int_0^\infty\!\int_0^\infty
 M(u)E(t)\left[
 \frac{W'(u/X)}{XH}K'\!\left(\frac{u-t}{H}\right)
 +\frac{W(u/X)}{H^2}K''\!\left(\frac{u-t}{H}\right)
 \right]dt\,du.
 \tag{2.4}
\end{split}
\]

**Proof.** Reorder the finite sums in (2.2):

\[
 S_H=\sum_n\mu(n)W(n/X)
       \int_0^\infty K((n-t)/H)\,d\psi(t).
\]

Write \(d\psi(t)=dt+dE(t)\). Since \(n>X>2H\), the continuous term is
exactly \(H\kappa\). Integration by parts in t gives

\[
 R_H=\frac1H\int_0^\infty E(t)
      \sum_n\mu(n)W(n/X)K'((n-t)/H)\,dt.
\]

For each t, integrate the inner sum against dM(u) by parts. All boundary
terms vanish because of the cutoffs, and the result is (2.4).
On the support, \(u\asymp X\), \(t\asymp X\); for each u the t interval
has length H. The term containing W' is
\(O(X^{\beta_M+\beta_P})\), and the term containing K'' is
\(O(X^{\beta_M+\beta_P+1}/H)\). Division by \(\kappa H\) proves (2.3).
\(\square\)

The same proof works with powers enlarged by arbitrarily small epsilon.
It also works for complex W and K.

## 3. Do not allow a Mellin weight to hide a zeta zero

A power bound for one arbitrary compactly supported W does not automatically
exclude every zeta zero: \(\widehat W(s)\) may vanish at a zero of zeta.
There are two complete ways to avoid this gap.

### 3.1 Compact test family

Fix a nonnegative nonzero \(W\in C_c^1((1,2))\), and use
\(W_\tau(u)=W(u)u^{-i\tau}\) for every fixed real \(\tau\). Constants may
depend on \(\tau\). If the correlation bound

\[
 S_H(X;W_\tau,K)/H\ll_{\varepsilon,\tau} X^{\alpha+\varepsilon}
 \tag{3.1}
\]

holds for every fixed \(\tau\), then (2.3), with \(H=X^\theta\), gives

\[
 M_{W_\tau}(X)\ll_{\varepsilon,\tau}X^{\gamma+\varepsilon},
 \quad
 \gamma=\max\{\alpha,\beta_M+\beta_P+1-2\theta\}.
 \tag{3.2}
\]

For \(\Re s>1\), absolute convergence gives

\[
 \int_0^\infty M_{W_\tau}(X)X^{-s-1}\,dX
 =\frac{\widehat W(s-i\tau)}{\zeta(s)},
 \quad \widehat W(z)=\int_0^\infty W(u)u^{z-1}\,du.
 \tag{3.3}
\]

The left side is holomorphic for \(\Re s>\gamma\). At a hypothetical
zero \(\rho=\beta+i\tau\) with \(\beta>\gamma\), the numerator is
\(\widehat W(\beta)>0\). Therefore it cannot cancel the reciprocal-zeta
pole. This contradicts holomorphy. Consequently zeta is zero-free in
\(\Re s>\gamma\).

No uniformity in \(\tau\) is needed for this zero exclusion: a given zero
has a fixed imaginary part. Uniformity would be needed for quantitative
conductor or height bounds, which are not claimed.

### 3.2 One explicitly nonvanishing Mellin weight

Alternatively take

\[
 W(u)=\exp[-(\log u)^2],\qquad
 \widehat W(s)=\sqrt\pi\exp(s^2/4)\ne0.
 \tag{3.4}
\]

For fixed \(0<\theta<1\) and \(H=X^\theta\), the compact-support
restriction in Theorem 2.1 may be removed. Weighted derivative moments
\(\int_0^\infty u^B|W(u)|du\) and
\(\int_0^\infty u^B|W'(u)|du\) are finite for every real B. Thus the same
two remainder estimates hold. There is now a boundary correction from
\(n\le2H\), bounded after division by H by

\[
 O\left(H\exp[-\log^2(X/(2H))]\right)=O_A(X^{-A})
 \tag{3.5}
\]

for each fixed A. The Mellin argument (3.3) then needs only this one W.
The small-X endpoint of its Mellin integral is harmless: the sum has
faster-than-any-power decay there. This version trades a noncompact n
weight for an everywhere nonzero transform. It is not an additional
consequence of the paper's compactly supported estimates without tail control.

## 4. Numerical targets and a conditional bootstrap

Suppose, as explicit analytic input, both exponents in (2.1) can be taken
arbitrarily close to a common \(\beta<1\). The remainder exponent is

\[
 r(\beta,\theta)=2\beta+1-2\theta.
 \tag{4.1}
\]

Taking the repository's source-qualified number
\(\beta_0=0.874886647039964\ldots\) **as a conditional example**, not as
an independently certified premise here, gives:

| Shift scale | Remainder exponent | Additional full-correlation input | Result of one transfer |
|---|---:|---:|---:|
| \(H=X^{0.98}\) | 0.789773294079928… | \(S_H/H\ll X^{0.8+\varepsilon}\) | zero-free for \(\Re s>0.8\) |
| \(H=X^{0.9999}\) | 0.749973294079928… | \(S_H/H\ll X^{0.75+\varepsilon}\) | zero-free for \(\Re s>0.75\) |
| \(H=cX\), fixed \(0<c\le1/4\), compact family | 0.749773294079928… | \(S_H/H\ll X^{0.75+\varepsilon}\) | zero-free for \(\Re s>0.75\) |

For a first improvement over beta, this elementary transport bound requires

\[
 \theta>(1+\beta)/2.
 \tag{4.2}
\]

At beta_0 this means \(\theta>0.937443323519982\ldots\). Thus these are
polynomially shorter than X, but still very long shifts; a claim that the
bridge already works with logarithmic shifts would be false.

There is a further conditional consequence. The standard analytic
equivalences identify, for \(1/2\le b<1\), a zero-free half-plane
\(\Re s>b\) with the bounds
\(M(x),\psi(x)-x\ll_\varepsilon x^{b+\varepsilon}\). A brief justification
is included below. Therefore a fixed input (3.1), if valid independently
of the current b, allows the recurrence

\[
 b_{j+1}=\max\{\alpha,2b_j+1-2\theta\}.
 \tag{4.3}
\]

If \(1/2\le\alpha<b_0<2\theta-1\), the values strictly decrease until
alpha is reached.
Indeed, before clipping at alpha,

\[
 b_j=(2\theta-1)-2^j[(2\theta-1)-b_0].
\]

For theta=0.98 and the sample beta_0, the unclipped exponents are

\[
 0.8748866470\ldots\to0.7897732941\ldots
 \to0.6195465882\ldots\to0.2790931763\ldots.
\]

A hypothetical bound (3.1) with alpha=1/2 would clip the last value at
1/2 and imply RH in three transfers. The value below 1/2 is not an asserted
Mertens bound; it only shows that the residual has become smaller than the
assumed correlation input. The input itself is completely open here.

An exact rational example avoids any dependence on the particular decimal
boundary. **Assume** the summatory inputs hold with
\(\beta_M=\beta_P=7/8+\varepsilon\), and **assume** the same full
correlation input with \(\alpha=1/2\) and \(\theta=49/50\). The
unclipped recurrence is exactly

\[
 \frac78\longmapsto\frac{79}{100}
 \longmapsto\frac{31}{50}\longmapsto\frac7{25}.
 \tag{4.4}
\]

Clipping at \(\alpha=1/2\) gives RH after three transfers. This is an
illustration of the conditional theorem, not an achieved sequence of
zero-free regions. In particular, the square-root averaged-correlation
input is not established by the supplied paper or by this note.

**Analytic equivalence used for iteration.** The easy direction follows
from the Mellin integral of M or psi. For the converse, suppose zeta has
no zeros in \(\Re s>b\), with b<1. On a disk centered at \(2+it\) whose
left edge stays to the right of b, an analytic branch of log zeta exists
for large t. Polynomial growth of zeta and Borel–Carathéodory give
\(|\log\zeta|\ll\log t\) on a slightly smaller disk. On a concentric
disk lying in \(\Re s>1\), log zeta is bounded. Hadamard three-circles
therefore gives \(|\log\zeta(\sigma+it)|\ll(\log t)^a\), a<1, for each
fixed \(\sigma>b\). Thus \(1/\zeta(\sigma+it)\ll_\eta t^\eta\) for
every eta>0; Cauchy also controls the logarithmic derivative. A truncated
Perron contour, shifted to \(\sigma=b+\varepsilon/2\) and truncated at
a sufficiently large fixed power of x, proves both summatory estimates,
with the pole at 1 contributing x to psi. This is a standard contour
argument, not an extra arithmetic theorem attributed to the new paper.

## 5. What this bridge rules out

### 5.1 Centering away the main term destroys the signal

The centered correlation

\[
 S_H-\kappa H M_W
\]

already satisfies (2.3) under the current summatory inputs. An argument
which only improves this remainder has not bounded \(M_W\). The precise
unresolved object is the **full** signed average S_H. Near zero additive
frequency, its prime factor contributes its mean density and leaves the
Möbius mean exposed. A determinant or major-arc treatment must retain and
control this term; it must not label it as a removable resonance and then
claim the full average is small.

### 5.2 A Cauchy/short-interval variance argument does not bootstrap by itself

For an unsmoothed version, let
\(P_H(n)=\psi(n-H)-\psi(n-2H)\) and
\(J=\sum_{n\asymp X}|P_H(n)-H|^2\). Direct Cauchy gives

\[
 \left|\sum_{n\asymp X}\mu(n)[P_H(n)-H]\right|/H
 \ll \sqrt{XJ}/H.
\]

To make this \(O(X^\alpha)\) requires
\(J\ll H^2X^{2\alpha-1}\). A fixed power-strength prime-variance estimate
of this sort cannot be silently inferred from an almost-all short-interval
PNT with an o(1) relative error. It already entails strong information
about zeta zeros. Double partial summation uses existing cancellation
on both sides and yields the explicit different tradeoff (2.3).

### 5.3 Symmetric kernels and vanishing moments are not a free exponent gain

The second term in (2.4) has normalized operator scale \(H^{-2}\).
An even K or a finite collection of vanishing moments may suppress some
very low frequencies, but a wavelength comparable to H survives for every
nonzero K. To see the obstruction from the premises alone, take smooth
model cumulative functions on a block of length X,

\[
 M_*(u)=X^{\beta_M}\chi(u/X)\cos(cu/H),\quad
 E_*(u)=X^{\beta_P}\chi(u/X)\cos(cu/H),
\]

with a phase adjustment if needed, choosing c such that the Fourier
transform of K is nonzero at c. Inserting these into (2.4) has size
\(X^{\beta_M+\beta_P+1}/H^2\) after division by H. When
\(H\gg X^{\max(\beta_M,\beta_P)}\), the derivative amplitudes are
bounded; the model is compatible with bounded coefficients and, on the
prime side, a positive base density 1 plus a small oscillation. It is not
a counterexample about actual primes or actual Möbius values. It shows
why the stated summatory estimates alone cannot improve the exponent.

If \(\kappa=0\), the Mertens main term vanishes identically; then a strong
bound for S_H is a bound for a centered remainder and gives no zero
exclusion via (3.3). Repeated smoothing at fixed H changes constants or
effective support, not this logical issue.

### 5.4 Even an ideal power upgrade of the paper's one-sign estimate does not contract beta

There is a second, distinct obstruction to a direct upgrade of the
particular proof chain in the paper. Let \(X=MN\), and grant the stronger
uniform input

\[
 \sup_{\chi,t}|M_\alpha(t)|
 =\sup_{\chi,t}\left|\frac1M
   \sum_{m\asymp M}\mu(m)R_Z(m)\chi(m)m^{it}\right|
 \ll_\varepsilon M^{\beta-1}X^\varepsilon
 \tag{5.1}
\]

over every character and frequency required in Proposition 5.3. This
is an explicitly granted idealized input. Zero-freeness for zeta alone
does not automatically give it for nonprincipal characters and a moving
roughness cutoff \(R_Z\). Also grant sufficiently strong power versions
of the small-prime-polynomial exceptional-set estimates, minor-arc bound,
and unweighting, so that none is the bottleneck.

On the large-prime-polynomial set in the proof of (5.16), the estimate
uses the square of the supremum in (5.1). Thus its normalized energy is

\[
 \mathcal E=\int|P_s(t)M_\alpha(t)N_\beta(t)|^2dt
 \ll_\varepsilon M^{2\beta-2}X^\varepsilon.
\]

Grant the same estimate for the complementary set. The Cauchy estimate
between the two energy factors in Section 5.2 then gives

\[
 |Q_Y^{\rm maj}|\ll_\varepsilon XY M^{2\beta-2}X^\varepsilon.
\]

Combining this with the first Cauchy estimate (4.4),
\(|T_Y|^2\ll(X/Y)Q_Y\), yields only

\[
 |T_Y|\ll_\varepsilon X M^{\beta-1}X^\varepsilon.
 \tag{5.2}
\]

Write \(M=X^m\), \(0<m\le1\). The output exponent in (5.2) is

\[
 1-m(1-\beta)\ \ge\ \beta,
\]

strictly greater than beta when m<1 and beta<1. For example, at
beta=7/8 the balanced block m=1/2 gives 15/16; even m=4/5 gives 9/10.
The original balanced Type II range has both variables of positive
power length, so m stays away from 1.

Consequently, replacing logarithmic estimates by ideal power estimates
within this particular chain still does not automatically give an
input-to-output improvement of the zero-free exponent. The first Cauchy
step has discarded the second Möbius sign, \(\mu(h)\), from
\(mn+2=ah\). A genuine contraction through this route needs additional
joint cancellation, or a different extraction that retains that sign;
solving only the power-scale minor arcs would not suffice. This is a
limitation of the stated estimate chain, not an impossibility theorem
for all modifications of the paper's approach.

## 6. Connection with positive squarefree marks

The finite-prime mark \(\rho^{\omega_i(n)-1}\omega_i(n)\) in the paper
suggests differentiating a generating function. This is a real connection
to the repository's \(\mu^2(n)\omega(n)\) route, but it has a specific
analytic limitation.

For \(\Re s>1\), set

\[
 F(z,s)=\sum_n\frac{\mu^2(n)z^{\omega(n)}}{n^s}
       =\prod_p(1+zp^{-s}).
\]

Then

\[
 F(1,s)=\frac{\zeta(s)}{\zeta(2s)},\qquad
 F(-1,s)=\frac1{\zeta(s)},
\]

and

\[
 \partial_zF(1,s)=\frac{\zeta(s)}{\zeta(2s)}
                    \sum_p\frac1{p^s+1}.
 \tag{6.1}
\]

In a simply connected zero-free subdomain of \(\Re s>1/2\),

\[
 \sum_p\frac1{p^s+1}=\log\zeta(s)+A(s),
 \tag{6.2}
\]

where A is holomorphic in \(\Re s>1/2\): subtract the first prime-power
term locally and all remaining prime sums are absolutely convergent there.
At a zero rho of zeta of multiplicity m, (6.1) has a local term proportional
to \((s-\rho)^m\log(s-\rho)\). Although it tends to zero, this is not
holomorphic across rho. This explains why a sufficiently strong,
correctly centered error bound for the positive count
\(\sum\mu^2(n)\omega(n)W(n/X)\) can detect zeros, while the unmarked
squarefree count does not.

It also explains the missing step in a tempting parameter interpolation:
an error estimate only at z=1 cannot be differentiated in z without a
uniform estimate in a neighborhood. Formally
\(F(z,s)=\zeta(s)^z G(z,s)\), with the higher prime powers absorbed in G.
The noninteger power of zeta itself develops a branch at a zeta zero.
Assuming the desired uniform continuation to justify the differentiation
would supply the zero-free information one is trying to prove.

For a fixed finite prime set P, the positive marked Dirichlet series is
instead a finite Euler-factor modification of
\(\zeta(s)/\zeta(2s)\); it remains holomorphic at zeta zeros in
\(\Re s>1/2\). The global branch mechanism arises only after taking a
controlled infinite-prime limit. The new paper's finitely many moving
subpolynomial prime bands do not by themselves justify that limit with a
fixed power error. The shift by 2 additionally removes the simple Euler
product representation altogether.

For comparison, finite negative marks satisfy, for a finite P,

\[
 \sum_n\frac{\mu(n)\rho^{\omega_P(n)}}{n^s}
 =\frac1{\zeta(s)}\prod_{p\in P}
      \frac{1-\rho p^{-s}}{1-p^{-s}}.
\]

For 0<rho<1 and Re s>0, the finite factor is nonzero. Power cancellation
for this *unshifted* marked Möbius sum would directly exclude zeta zeros;
the paper proves a different, prime-shifted statement with only little-o
unweighting. These two statements must not be interchanged.

## 7. A quantitative limitation of the paper's unweighting architecture

In the CRT model for primes used by Proposition 2.3, each prime band Pi
has harmonic mass asymptotic to log 2. The probability that \(p+2\) has
no divisor from Pi tends to 1/2. A product of K factors
\(\rho^{\omega_i-1}\omega_i\) vanishes unless every one of the K bands
is hit, so its support probability tends to \(2^{-K}\). For a normalized
nonnegative mark of mean 1, Cauchy gives second moment at least \(2^K\),
and variance at least \(2^K-1\). For b independent, disjoint-band marks,
the normalized average therefore has variance at least
\((2^K-1+o(1))/b\) in that CRT model.

At a finite x, pairwise disjoint intervals of the particular form
\((\exp(L^a),\exp(2L^a)]\), a in (0.1,0.2), can number only
\(O(\log L)\): disjoint successive bands require their values \(L^a\)
to increase by at least a factor 2. Thus one cannot choose
\(b\asymp X^{2\delta}\) in the stated fixed-band averaging scheme to
turn its RMS error into \(X^{-\delta}\). This is a limitation of that
specific quantitative unweighting mechanism, not a theorem that all
possible refinements of the paper are incapable of power savings.

## 8. Reproducible algebra check

`verify_shift_bridge.py` checks (2.4) using actual Möbius and von Mangoldt
values and piecewise polynomial quadrature. It uses
\(W(u)=(u-1)^2(2-u)^2\) on [1,2], and
\(K(v)=140(v-1)^3(2-v)^3\) on [1,2], so \(\int K=1\).
Both vanish with the derivatives needed for integration by parts.

For (X,H)=(40,5), (80,10), (120,12), direct finite summation and the
double-Stieltjes formula agree to absolute errors below
\(4\cdot10^{-12}\). The calculation checks the sign and the two powers
of H, and does not establish any asymptotic correlation bound or RH.

## 9. Concrete research target

The most specific new target obtained here is:

> For H=X^0.98, prove
> \(\sum_h K(h/H)\sum_n\mu(n)\Lambda(n-h)W_\tau(n/X)
>   \ll_{\varepsilon,\tau}H X^{0.8+\varepsilon}\)
> for every fixed real tau, with W nonnegative, compact and nonzero,
> while retaining the principal additive-frequency contribution.

Combined with the explicit summatory premises at beta_0, this would prove
a zero-free half-plane Re s>0.8. A square-root version would iterate to RH.
The current paper's fixed shift 2, subpolynomial auxiliary scales,
logarithmic estimates, and final nonuniform little-o limit do not prove
this statement. A successful transfer of its determinant machinery would
need a uniform large-shift treatment and, crucially, a new bound for the
principal Möbius mean, rather than another estimate for the centered
determinant residual.
