# L-9515 — Balanced critical Farey correlation

Claim ID: `L-9515`  
Title: Möbius-weighted local-to-Bohr dispersion at the critical Farey scale  
Status: **OPEN PROPOSED LEMMA / PROOF ATTEMPT — load-bearing step not established**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9512`, `L-9513`, `T-9506`; comparison with `L-23002`  
Scope: the complete analytic-totient packet, including the nonperiodic tail

## 1. Proof-facing statement

Let
\[
f(u)=\{u\}^{2}-\frac13
\]
and let
\[
c_k=\frac{i}{2\pi k}+\frac{1}{2\pi^2k^2}\qquad(k\ne0)
\]
be its Fourier coefficients. For a smooth fixed cutoff
\(W\in C_c^\infty((1/2,3))\), put
\[
\mathcal J_D(\alpha)
=\int_{\mathbb R}W(x/D)e^{2\pi i\alpha x}\,dx.
\]

After the exact nonperiodic Bernoulli/Mertens tail of `L-9512` is retained,
the unresolved dyadic correlation is
\[
\mathcal N_D
=
\sum_{d,e\asymp D}\mu(d)\mu(e)
\sum_{k,\ell\ne0}
c_k\overline{c_\ell}\,
\mathcal J_D\!\left(\frac{k}{d}-\frac{\ell}{e}\right).
\]

The proposed critical estimate is
\[
\boxed{\mathcal N_D\ll_{\varepsilon,W}D^{2+\varepsilon}.}
\tag{L-9515.1}
\]

The statement must be applied to the complete packet. Deleting the exact tail,
separating the Bernoulli channels, or taking entrywise absolute values changes
the problem.

## 2. Parts already closed

### Exact resonances

The locus
\[
\frac{k}{d}=\frac{\ell}{e}
\]
is grouped by the reduced rational frequency. `L-9513` proves the exact
Jordan-totient square factorization
\[
\begin{aligned}
\mathcal B_D={}&
\frac1{12}\sum_{q\le D}J_2(q)
\left(\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}d\right)^2\\
&+\frac1{180}\sum_{q\le D}J_4(q)
\left(\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}{d^2}\right)^2,
\end{aligned}
\]
and consequently the resonant contribution has the required size
\(O(D^{2})\) on an interval of length \(D\).

### Fourier tails

Because \(c_k=O(1/|k|)\), with an additional \(O(1/k^2)\) channel after the
complete endpoint correction is assembled, standard dyadic truncation reduces
the proof to finitely many harmonic blocks. The discarded part is bounded at
\(D^{2+\varepsilon}\) after the exact endpoint/tail cancellation is retained.

### Separated frequencies

For
\[
\left|\frac{k}{d}-\frac{\ell}{e}\right|
\ge D^{-1+\eta},
\]
repeated integration by parts in \(\mathcal J_D\), followed by divisor counting,
gives the required estimate. This is the ordinary large-sieve/far-frequency
region.

Thus only the critical cluster
\[
0<
\left|\frac{k}{d}-\frac{\ell}{e}\right|
\lesssim D^{-1+\eta}
\tag{L-9515.2}
\]
remains.

## 3. Determinant parameterization

Write
\[
d=ga,\qquad e=gb,\qquad(a,b)=1,
\]
and set
\[
h=kb-\ell a.
\]
Then
\[
\frac{k}{d}-\frac{\ell}{e}
=\frac{h}{gab}.
\]

The exact resonance is \(h=0\). The unresolved part has \(h\ne0\) and
\[
|h|\lesssim \frac{gab}{D^{1-\eta}}.
\]

For fixed \(a,b,h\), all integer solutions are
\[
k=k_0+at,\qquad \ell=\ell_0+bt.
\]
The decay of \(c_kc_\ell\) makes the \(t\)-sum convergent. The remaining
arithmetic object is a signed bilinear form in
\[
\mu(ga)\mu(gb)
\]
over balanced coprime pairs.

## 4. Proposed dispersion closure

The attempted proof is:

1. apply a finite Heath–Brown/Vaughan-type convolution identity to both
   Möbius factors before taking absolute values;
2. split the resulting variables into Type-I and balanced Type-II ranges;
3. apply Poisson summation in the long variables while retaining the determinant
   equation \(kb-\ell a=h\);
4. identify the zero dual frequency with the already extracted \(h=0\)
   Jordan square;
5. bound every nonzero dual frequency by Weil/Kuznetsov estimates and the
   spectral large sieve;
6. sum over \(h\), the divisor parameter \(g\), harmonic blocks, and dyadic
   partitions.

If Step 5 were uniform at the transition where the modulus, determinant and
dual frequency share large gcd, the resulting total would be
\(D^{2+\varepsilon}\), proving (L-9515.1).

## 5. Exact point at which the proof attempt remains incomplete

The required uniform Type-II estimate at Step 5 has not been proved.

At the critical length, one zero/major-arc contribution remains after the
formal Poisson transform. In denominator coordinates it is a smooth dyadic
Möbius block; in prime coordinates it is the balanced signed-semiprime cell of
PR #222; in transport coordinates it is the reserve-minus-curvature margin of
PR #218.

A phase-blind large sieve bounds this contribution by \(D^{3+\varepsilon}\).
The missing square-root gain is exactly the arithmetic content of RH. It cannot
be obtained by:

- taking absolute values of the cells;
- treating each prime filter as a contraction;
- using the complete-period Bohr mean in place of the physical interval;
- replacing the complete tail by an independent bound;
- a finite positive computation or a density-one support statement.

## 6. Relation to the repository-wide common gate

With the source normalizations matched, (L-9515.1) is the analytic-totient
version of `L-23002`:

- dyadic screw transport;
- balanced semiprime Type-II energy;
- vertical prime Hardy energy;
- analytic-totient local second moment.

A proof of any one complete version closes the corresponding chain to RH.

## 7. Status boundary

This file records a serious proof attempt, not a proved lemma. The unresolved
uniform nonzero-dual/major-arc estimate is the single load-bearing gap. Reviewers
should begin there rather than rechecking the already closed exact-resonance or
far-frequency pieces.
