# Review of the finite-horizon necklace representation

**Reviewer:** /root/native_structural_attack, a separate agent in the same
model session.

**Verdict:** the displayed representation, convergence and polynomial
majorant claims pass the reconstruction below at the exact frozen
manuscript hash. The open signed trace bound remains open. This is
internal mathematical review, not external human review or formal
verification.

**Reviewed manuscript:** HORIZON_NECKLACE_FACTORIZATION.md in
standalone/2026-10-13-sextic-structural-strike/.

**Exact SHA256:**
a6aa7ab8925eac3f1f514b6e4138baa87735e3902fa3c5a78679480c7cf925ab.

**Bytes:** 20252.

**Independence disclosure:** the root agent supplied the necklace idea and
authored this manuscript. Before it was frozen, I independently checked
the physical-horizon mechanism and suggested the smooth plateau variant
now in Section 6. I also authored the finite checker described below.
Thus this review reconstructs the full written proof using separate
derivations, but it is not independent of every part of its development.
The parenthetical fixed-character correction in Section 6 is included in
the reviewed hash. Earlier hashes do not identify this review target.

## 1. Actual source and classical identity checked

I read the full frozen manuscript, the source SC1–SC7 short-polynomial
transport, and P8/P14–P15 of the prime-slot source physically included in
the packet from PR #911, commit
2f8b6a3898a722d0602a91dea73bac344a3bb7dd. The source uses exact squarefree
incidence allocations, all physical column tests, independent Mellin
frequencies, and literal zeros. It does not authorize equality between
partial frequency-region integrals in two different representations.

I personally opened Pieter Moree, *The formal series Witt transform*,
arXiv:math/0311194v2, Section 2. Equations (1)–(3), and the denominator
identity immediately following them, are exactly the classical
multivariate coefficients and formal identity used here. The manuscript
correctly credits that algebra. Its new proposed application is the
simultaneous physical truncation of all retained factors, not the
invention of the Witt identity.

I also checked the integrated CURRENT_RESULTS.md Section 9 and Section 11:
the repository already separately records a causal Euler/Dickman
completion and the scalar formal identity for \(1-x/2\).
The new note does not need their analytic theorems. They motivate the
connection; they are not unproved dependencies smuggled into this proof.

## 2. Fresh reconstruction of the local algebra

For content \(\alpha\), let \(A_\alpha=|\alpha|!/\prod_i\alpha_i!\) count
linear words. Every linear word has a unique least period; a primitive
cyclic word of content \(\alpha/d\), repeated \(d\) times, has
\(|\alpha|/d\) distinct linear rotations. Consequently

\[
A_\alpha=\sum_{d\mid\gcd\alpha} (|\alpha|/d)\,w_{\alpha/d}.
\]

Ordinary divisor inversion gives exactly (2.1).
This proves both integrality and nonnegativity without an appeal to
analytic roots or an infinite fractional-power convention.

Independently, the coefficient of \(\mathbf z^\beta\) in the logarithm
of the proposed product is

\[
-\sum_{d\mid\gcd\beta}\frac{w_{\beta/d}}{d}
=-\frac{A_\beta}{|\beta|},
\]

by the displayed counting identity. This is the coefficient of
\(\log(1-\sum_i z_i)\). The constant terms on both sides are one.
Formal exponentiation proves (2.2), since each coefficient uses finitely
many factors.

In particular, \(w_{e_i}=1\), \(w_{e_i+e_j}=1\),
\(w_{2e_i+e_j}=1\) for unequal slots, and
\(w_{e_i+e_j+e_\ell}=2\) for distinct slots. A repeated word in a single
letter is imprimitive, so \(w_{me_i}=0\) for \(m>1\).
The correct triple multiplicity is material: replacing it by one changes
the cubic cancellation.

The rational function \(R_{J,p}\) is analytic on the entire open unit
polydisk: every denominator is \(1-\mathbf z^\alpha\), with
\(|\mathbf z^\alpha|<1\). Its numerator can vanish, and the proof never
takes its reciprocal. Its Taylor series uses only nonnegative coordinate
exponents. The formal identity proves the vanishing of every
nonconstant coefficient through total degree \(J\).

## 3. Absolute coefficient convergence: where the estimate is taken

One must take absolute values after the exact local degree cancellation.
An absolute product formed before that cancellation could reintroduce
first- or second-degree divergence. The reviewed argument has the order
right.

More explicitly, write the local Taylor coefficients \(r_e\). Choose a
fixed polyradius \(\rho<1\) on which their absolute sum is finite.
For \(0<t\le\rho/2\),

\[
\sum_{e\ne0}|r_e|t^{|e|}
=\sum_{|e|\ge J+1}|r_e|t^{|e|}
\le (t/\rho)^{J+1}\sum_e |r_e|\rho^{|e|}.
\]

The constant depends only on \(r,J,\rho\). At a prime, substitute
\(t=(Np)^{-\sigma_*}\); bounded slot values can only decrease this
coefficient majorant. Fixed-field ideal counting implies convergence of
\(\sum_p (Np)^{-(J+1)\sigma_*}\) when
\((J+1)\sigma_*>1\). No prime ideal asymptotic is needed.

The finitely many primes with \(t>\rho/2\) each have a convergent
geometric denominator expansion because \(\sigma_*>0\).
Their uniform finite majorants cover every row and every independent
frequency. Removing a prime by \(SQ\), or setting any slot value to
zero, cannot increase that chosen positive majorant. The product of
local absolute majorants is therefore finite, yielding (3.5).
The same estimate on a real-part neighborhood proves local normal
convergence.

This proof establishes absolute convergence of the multivariate ideal
Dirichlet series itself, which is stronger than merely bounding the
numerical Euler product. Equal-norm ideals are distinct in that series.
It evaluates no infinite reciprocal \(L\)-function and sends neither
\(J\) nor the number of slots to infinity.

## 4. Physical-horizon preservation: a downset argument

Fix actual upper horizons \(Y_i\ge1\), not merely dyadic scale labels.
For the source allocation these are \(bD/Nc_i\).
An allocation with \(Nc_i>bD\) contributes nothing and need not enter
this argument.

The set of exponent arrays satisfying every coordinate norm bound
\(Nn_i\le Y_i\) is a multiplicative downset. If an exponent array is
outside it, adding any nonnegative array leaves it outside.
Every factor used in (4.7), including each inverse-denominator expansion
inside the remainder, has nonnegative exponents.

For one retained necklace multiindex \(\alpha\), an ideal term \(n\)
places \(n^{\alpha_i}\) in column \(i\).
The exact eligibility condition is

\[
(Nn)^{\alpha_i}\le Y_i\quad\text{for every }\alpha_i>0,
\]

equivalently \(Nn\le X_\alpha\).
Thus discarding a term with \(Nn>X_\alpha\) cannot affect any retained
coefficient. This remains true when the factor occurs \(w_\alpha>1\)
times: every copy can be truncated separately, and the product is still
tested by the complete original column windows.

The argument does not assert that the truncated-factor product itself
has support contained in the rectangle. Oversized products can survive
inside that product; complete Mellin inversion subsequently removes
them. This distinction is explicitly preserved by the manuscript.

Since \(X_\alpha\le Y_*=\max_iY_i\), every ideal retained by the short
factor is supported on prime ideals of norm at most \(Y_*\).
Conversely, adding the infinitely many larger primes to the remainder
does not change a retained coefficient: any nonconstant term at such a
prime already exceeds at least one horizon. This proves Theorem 4.1
coefficientwise in ideals, without a norm-collision identification.

Every character is multiplied literally. In particular, if a prime
divides the row, a balanced left/right pair has value zero. Reducing its
formal exponent modulo six and declaring the pair principal with value
one would change the represented coefficients. The reviewed formula
does not do that. Likewise, the same-side pair retains the complete
fixed \(\nu^2\) twist in addition to the cubic sextic-symbol part.

## 5. Smooth plateau and all-frequency Mellin transport

A fixed bounded smooth \(\rho\) equal to one on \([0,1]\) and supported
in \([0,2]\) can replace the sharp factor indicator by
\(\rho(Nn/X_\alpha)\). Every coefficient that changes lies strictly
outside at least one physical coordinate horizon. New primes that occur
in this longer finite polynomial are also harmless for the same reason.
All extra exponents are nonnegative. The coefficient rectangle therefore
remains exactly the same.

For each fixed set of horizons the remaining factors are finite
polynomials and the remainder has an absolutely convergent Dirichlet
series. Multiplying their positive absolute bounds gives an integrable
dominating function after including the fixed smooth Mellin transforms.
Termwise full Mellin inversion is valid on every prescribed contour
with \((J+1)\sigma_*>1\).

The subsequent element-row summation is over the Eisenstein lattice,
whose real dimension is two. Its fixed Schwartz weight has total
absolute mass \(O_\Phi(H)\) under \(u/\sqrt H\), for \(H\ge1\).
The revised field-scope paragraph is therefore essential and correct:
the ideal identities hold over a fixed general number field; that
particular row scaling and \(H\) mass statement are native Eisenstein
statements.

No equality of partial Mellin tube integrals follows from the complete
coefficient identity. The manuscript correctly refuses to transfer
SC7 automatically to this new integrand.

## 6. Polynomial stability and the still-unpaid arithmetic saving

For \(\lambda>0\), fixed-field ideal counting and partial summation give

\[
\sum_{Nn\le X}(Nn)^{-\lambda}\ll
\begin{cases}
X^{1-\lambda},&\lambda<1,\\
\log(2X),&\lambda=1,\\
1,&\lambda>1.
\end{cases}
\]

All retained characters have modulus at most one. Applying this estimate
separately to every short factor, and the uniform remainder bound,
proves (5.2). The row mass estimate proves (5.3). The constants may
depend on the fixed field, slot number, degree cutoff and contour.
The construction gives no uniform control as these parameters tend to
an endpoint.

At \(\sigma_i=1/2,J=2\), singleton factors cost \(Y_i^{1/2}\), and pair
factors cost \(\log(2\min(Y_i,Y_j))\). The remainder is uniformly bounded
because \(3\sigma_*=3/2>1\). Hence the literal new integrand has the
stated all-frequency polynomial majorant. This excludes the specific
superpolynomial resonances of the previous unfiltered Euler and
single-only-shortened representations.

At balanced horizons \(Y_i\asymp D\), the absolute singleton estimate
still costs \(D^k\) in the integrand, followed by \(D^k\) from the Mellin
scale prefactors. The resulting moment power is the trivial
\(HD^{2k}\), up to logarithms. Algebraic stability alone is not a new
moment estimate.

For orientation, suppose the already-used native smooth second moment
and pointwise exponent \(\beta\) are supplied in their actual uniform
moving-mask class. At real part one-half, dyadic summation of plateau
singleton polynomials then gives second-moment size
\(HD^\epsilon\), and pointwise size
\(D^{\beta-1/2+\epsilon}\), with polynomial frequency costs.
Cauchy on two singleton factors, the pointwise estimate on the other
\(2k-2\), and absolute bounds on all pair factors and the remainder
give at best

\[
HD^{(2k-2)(\beta-1/2)+\epsilon}
\]

for the balanced trace. Restoring the \(D^k\) Mellin scales gives exactly

\[
HD^{1+2(k-1)\beta+\epsilon}.
\]

This is the existing interpolation exponent. The calculation is an
accounting statement under those named inputs, not a new theorem for
arbitrary sharp cutoff coefficients or arbitrary twists.
The plateau formulation is useful because it can use the actual smooth
native inputs.

The further signed trace target (7.1) is consequently substantive.
If it held uniformly for the original incidence allocations, its
\(D^k\prod_i(Nc_i)^{-1/2}\) Mellin price would be

\[
D^k\prod_I(Nq_I)^{-|I|/2}.
\]

Pair-incidence sums are harmonic and higher-incidence sums converge.
At fixed slot count their logarithmic factors can be absorbed in
\(D^\epsilon\). This reproduces the stated conditional implication
to the diagonal moment. It proves no converse, no new zero-free region,
and no RH consequence.

The repair keeps all prime and composite degrees within the literal
short Möbius factors. It therefore avoids the known prime-selection
counterexample at the level of coefficient class. It does not prove
that (7.1) is true, or that another obstruction cannot exist.

## 7. Exact finite diagnostic and reproducibility

The owned checker is pass3_check_witt_horizon.py, exact SHA256

97d5c362cb7c8ccbff19e0aaff7415a3c3b9852406c3dd05a609c7c8db19e628.

It uses only Python standard-library integers and rational arithmetic.
No floating-point cutoff, numerical ideal count or inferred asymptotic
enters a pass condition. Failed conditions raise RuntimeError and are
not disabled by optimized Python.

Independent coverage:

- 16 local remainder checks, for 2–5 slots and cutoffs 1–4;
  421 multiindices and 487 primitive factor copies.
- Direct enumeration of 1,183 primitive cyclic word orbits,
  covering 319 multiindices for 2–4 letters and lengths 1–6.
  This enumeration does not obtain its counts from the formula being
  checked.
- Seven finite ideal-norm rectangles at cutoffs 2 or 3.
  Factors use squarefree products of individually labeled formal prime
  ideals. Cases include distinct ideals of the same norm, separate
  labels of norms \(7,7,13\), unequal horizons, a horizon equal to one,
  literal row-zero masks, more general slot zeros and signed phases.
- Negative controls detect an overly small physical cap, the incorrect
  multiplicity one for three distinct letters, an imprimitive repeated
  singleton factor, and restoration of a principal nonunit zero.

Within each finite rectangle the script constructs the original
prime-slot polynomial, the exact geometric inverse of the retained
necklace product, and every independently truncated squarefree factor.
It checks equality of every retained ideal coefficient after reunion.
The finite ring is truncated by exact integer products
\(\prod_p(Np)^{e_{p,i}}\le Y_i\), separately for each column.
Its correctness as a downset follows from the monotonicity proved above.

I ran ordinary Python and Python with -O against the exact reviewed
proof, using the optional --proof argument. The JSON reports are
byte-identical and PASS. The normal report is
pass3_witt_horizon_report.json, 5576 bytes, SHA256

9f8a8b6352c85a956bd6ea74fd66f9a1da866135296bb7edfbbe51cb5c62ce10.

The report records the manuscript hash and 20252-byte length.
The finite principal-zero negative witness is local; it is not a
statistical test of a sextic family. The smooth plateau extension and
infinite normal convergence are proved in Sections 3–5 of this review,
not inferred from the finite diagnostic.

## 8. Review boundary and smallest remaining gap

No load-bearing gap was found in Lemma 2.1, Lemma 3.1, Theorem 4.1,
Corollary 4.2 or Theorem 5.1 under their written hypotheses.
The field-specific row normalization and the fixed-character pair
description are both correct at the reviewed hash.

The native diagonal moment still requires the signed all-frequency
trace saving (7.1), or a weaker complete filtered estimate that gives
the same incidence-weighted result. Neither local necklace algebra,
ordinary absolute convergence, nor the finite checker supplies it.
The full native composite singleton sector remains unresolved.

The review does not independently prove all imported native smooth M2
or pointwise results; they are mentioned only to expose the unchanged
interpolation price. It does not claim originality of the classical
necklace identity, does not transfer old tube estimates, and does not
turn a finite successful check into a global arithmetic theorem.

