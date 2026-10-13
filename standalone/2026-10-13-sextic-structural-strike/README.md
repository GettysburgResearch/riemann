# Sextic structural strike: false trace targets, a finite-horizon repair, and a conductor theorem

**Status: proposed standalone research, with complete proofs and scoped
same-team reviews.** The full native fourth moment, the generalized
\(2k\)-th moment hierarchy, and RH remain open. This packet changes no
integrated theorem and claims no new numerical zero-free boundary.

This pass stepped back from the repeated completion arguments and checked
what the proposed analytic targets actually ask for. It found two
asymptotic counterexamples to the unfiltered traces in PR #911. It then
constructed a different exact representation which removes that specific
instability, using the classical primitive-necklace identity. A separate
conjugate-pair argument gives a sharp conductor mean for the fully sextic
local type and a larger controlled native moment sector.

The new representation and the new conductor estimate are constructive
results. Neither supplies the still-missing signed cancellation among
the longest singleton products.

## 1. What the accumulated work was missing

The native object is the Eisenstein sextic family

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad
M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D)|^{2k},
\tag{1.1}
\]

with every character zero at a nonunit retained. The desired hierarchy
has diagonal size

\[
                          M_{2k}(D,D^h)\ll D^{h+k+\epsilon}
\tag{1.2: OPEN}
\]

for every required fixed \(k\), twist, smooth test, exclusion and smaller
scale, with \(h>1\) close to one.

The source audit separated four distinct difficulties.

| Route already explored | What survives | Where it stops |
|---|---|---|
| Signed auxiliary and A2 reunion, including #927 | Exact cancellation of artificial completion terms and stronger controlled tails | Complete inversion returns the native covariance; it does not supply its missing sign estimate |
| Incidence, graph and conductor sectors in #925–#929 | Additional complete signed sectors and positive conductor bounds with their stated selectors | Nearly coprime long singleton products remain outside the diagonal region |
| Prime-slot finite Euler traces in #911 | Exact identities after all physical column tests; its local pair algebra and tube bounds retain their own scope | The stronger unfiltered contracts P13 and CT1 are false |
| Independent-prime or coefficient-insensitive models | The abstract residue model has diagonal moments | Actual sixth-power rows preserve coherent spikes, and exact Möbius parity matters |

The failure of P13 and CT1 is particularly actionable. Removing the
column norm constraints creates coefficients far beyond the physical
moment's range. They can accumulate exponentially in the unfiltered
integrand even though the complete Mellin operation later deletes them.
An exact integral representation does not license a polynomial estimate
for every value of that integrand.

## 2. Two actual source-contract refutations

The sources being refuted are preserved byte-for-byte in
[sources/pr911](sources/pr911), at commit
`2f8b6a3898a722d0602a91dea73bac344a3bb7dd`. They were explicitly open
sufficient contracts, not accepted proofs of the moment. Their conditional
implications remain logically correct; their hypotheses cannot hold with
the stated uniformity.

### 2.1 The original Euler trace fails even on its common conjugate slice

Let \(\mathcal C\) be the original finite source polynomial and
\(Y=bD,\ H=D^h\), and take the permitted trivial datum \(\nu=1\).
For every fixed \(k\ge1\), and every fixed
\(0<\sigma_0<1\), [EULER_TRACE_RESONANCE.md](EULER_TRACE_RESONANCE.md)
constructs one fixed legal cross-pair incidence mask and the deterministic
frequency vector

\[
\mathbf t_Y=(\underbrace{\pi/\log Y,\ldots,\pi/\log Y}_{k},
             \underbrace{-\pi/\log Y,\ldots,-\pi/\log Y}_{k})
\]

such that the **complete original row trace** is real, nonnegative, and

\[
\sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
          \mathcal C_{2k,Y,Q,u}(\sigma_0+i\mathbf t_Y)
\ge \exp\!\left(c\frac{Y^{1-\sigma_0}}{\log Y}\right)
\tag{2.1}
\]

for every sufficiently large \(Y\). At \(\sigma_0=1/2\), this refutes
P13 even with any additional fixed power of \(D\).

The proof removes finitely many small primes by an actual permitted
cross-pair mask. Every remaining paired local numerator is positive on
every row. On the retained row \(u=1\), the top primes have negative
cosine and give a positive first-order logarithmic contribution.
The classical prime ideal theorem makes that contribution dominate all
smaller primes. Positivity of every other row justifies the unit-row
lower bound; no signed row sum is incorrectly replaced by a selected
positive part.

### 2.2 Shortening only the single Euler factors does not repair it

For the same permitted datum \(\nu=1\), every fixed \(k\ge2\), and
\(1/3<\sigma<1/2\),
[RESONANT_SHORT_TRACE.md](RESONANT_SHORT_TRACE.md) gives a second
counterexample for the literal CT1 integrand
\(Q_{\rm coll}\prod_iT_{i,Y}\):

\[
\sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
       Q_{{\rm coll},Y,u}(\sigma+i\mathbf t_Y)
       \prod_iT_{i,Y,u}(\sigma+it_{i,Y})
\ge \exp\!\left(c\frac{Y^{1-2\sigma}}{\log Y}\right).
\tag{2.2}
\]

The frequencies have two left clusters separated by \(\pi/\log Y\),
with conjugate right clusters. They lie outside the exact WT1 tube.
The degree-two collision coefficient is negative at the opposite
clusters, so the positive collision ratio grows exponentially.

The actual short Möbius factors might vanish at an individual frequency.
[SHORT_FACTOR_NONSMALLNESS.md](SHORT_FACTOR_NONSMALLNESS.md) handles
that issue for their product at once: a predetermined
\(O_k(\log Y)\) grid contains a point where the product is at least
\(\exp[-C\log Y\log\log Y]\). This follows from its nonzero anchor at
real part four and explicit complex interpolation. That loss is too
small to cancel (2.2) at every grid point.

Both refutations retain the original Möbius coefficients, all row
nonunit zeros, the literal exterior incidence mask, and all rows.
The fixed mask's norm can be enormous; it is fixed before
\(Y\to\infty\), and the source permits it once \(Y\) exceeds that norm.
No effective small numerical threshold is claimed.

**What remains valid:** the exact complete norm-filtered identity SC4,
the P14–P15 conditional implications, the earlier common-tube suppression
for its exact representation, and the possibility of the original
native moment bound. Neither lower bound is transferred to a signed
full-dimensional Mellin integral.

## 3. A repair connecting the necklace and causal-horizon strands

[HORIZON_NECKLACE_FACTORIZATION.md](HORIZON_NECKLACE_FACTORIZATION.md)
uses the classical multivariate Witt identity

\[
1-\sum_i z_i
 =\prod_{\alpha\ne0}(1-\mathbf z^\alpha)^{w_\alpha},
\qquad
w_\alpha=\frac1{|\alpha|}
\sum_{d\mid\gcd\alpha}\mu_{\mathbb Z}(d)
\frac{(|\alpha|/d)!}{\prod_i(\alpha_i/d)!}.
\tag{3.1}
\]

The integer \(w_\alpha\) counts primitive cyclic words with that slot
content. The identity is credited to the classical literature and
proved elementarily in the note; it is not claimed as a newly discovered
combinatorial theorem.

Retain all factors of degree at most a fixed \(J\). The remainder has
no nonconstant terms through degree \(J\), so its absolute coefficient
Euler product is uniformly bounded whenever

\[
                          \min_i\Re s_i>1/(J+1).
\tag{3.2}
\]

For the actual column horizons \(Y_i=bD/Nc_i\), truncate **every**
retained factor at

\[
                          X_\alpha=\min_{\alpha_i>0}Y_i^{1/\alpha_i}.
\tag{3.3}
\]

A removed ideal \(n\) would already put \(n^{\alpha_i}\) past at
least one column horizon. All other exponents are nonnegative, so
later multiplication cannot bring it back. The new integrand therefore
preserves every physical ideal coefficient exactly. Equal-norm distinct
prime ideals remain distinct.

At the critical line, \(J=2\) suffices. The representation becomes

\[
\mathcal I_{2,u}
=\mathcal R_{2,u}
 \prod_iT_{i,Y_i,u}(s_i)
 \prod_{i<j}T_{ij,\min(Y_i,Y_j),u}(s_i+s_j).
\tag{3.4}
\]

The pair factors are now short Möbius polynomials at real part one;
the complete same-side character retains its fixed \(\nu^2\) twist,
and cross-side factors retain the principal nonunit masks. The
remainder is uniformly bounded. Thus, for **all independent frequencies**,

\[
|\mathcal I_{2,u}|
\ll
\prod_iY_i^{1/2}
\prod_{i<j}\log(2\min(Y_i,Y_j)).
\tag{3.5}
\]

The source row trace costs at most \(H\) times (3.5). More generally,
a finite \(J\) gives an explicit polynomial bound at every fixed
positive contour. No prime ideal theorem or zero-free premise is needed
for this representation theorem.

This fixes the specific superpolynomial defect. It does not give the
desired \(HD^\epsilon\) signed trace bound. At balanced horizons, the
trivial bound still gives \(HD^{2k+\epsilon}\) after Mellin scaling.
The smooth plateau version is compatible with the existing native
second-moment inputs; applying ordinary Cauchy and the old pointwise
estimate recovers the old higher-moment exponent, with no automatic
bootstrap. The earlier tube estimates are not transferred between
representations without a new proof.

## 4. A constructive conductor theorem in every fixed order

[CONJUGATE_PAIR_CONDUCTOR_SIEVE.md](CONJUGATE_PAIR_CONDUCTOR_SIEVE.md)
extends the two-sign mechanism in the cubic conductor argument to the
family \(a b^{n-1}\), for every fixed \(n\ge3\) over a fixed number
field containing \(\mu_n\), with its fixed standard residue-character
family. With
\(M=\min(A,B)\), \(N_0=\max(A,B)\), it proves

\[
\begin{aligned}
&\sum_{a\sim A,b\sim B}
\left|\sum_{q\sim Q}^{\rm squarefree}
\lambda_q\chi_q(a)\overline{\chi_q(b)}\right|^2\\
&\quad\ll (ABQ)^\epsilon\|\lambda\|_2^2
\left[
AB+M^{1/n}N_0^{1-1/n}Q^{2/n}
+M^{1-1/n}N_0^{1/n}Q
+M^{2/n}N_0^{1-2/n}Q^{3/n}
\right].
\end{aligned}
\tag{4.1}
\]

The source input is de Faveri's fixed-order sieve, primitive-character
Poisson formula and squarefree root-number factorization. The new
composition keeps the two conjugate character factors together:
after reflection their orientations agree, giving \(\chi_q(ae)\).
The source's higher-power mixed root-number factors are absent in this
squarefree residual pair. Two coefficient vectors from Mellin
separation are handled explicitly by Cauchy before nonnegative norms
are used.

For the native sextic family the required pair is \(a b^5\).
With a primitive moving background of conductor norm \(R\), the
central second mean is bounded by

\[
\begin{aligned}
&(RAB)^\epsilon(2+|t|)^C AB\\
&\quad\times
\left[1+R^{1/6}M^{-2/3}
+R^{1/2}(M/N_0)^{1/3}
+R^{1/4}M^{-5/12}N_0^{-1/12}\right].
\end{aligned}
\tag{4.2}
\]

In particular, fixed background gives conductor-size cost.
[CONDUCTOR_COROLLARIES.md](CONDUCTOR_COROLLARIES.md) sums dyads to get

\[
\sum_{\substack{ab\ {\rm squarefree}\\N(ab)\le X}}
\left|L\!\left(\tfrac12+it,
       (\psi\chi_{ab^5})^{\rm prim}\right)\right|^2
\ll X^{1+\epsilon}(2+|t|)^C.
\tag{4.3}
\]

This covers the standard family with exact local order six at every
ramified good prime, because its primitive local exponents are precisely
\(1,5\). Characters with local orders two or three are not all covered.
No claim of external novelty or priority is made.

### A strict native sector gain

The theorem averages both singleton signs against the moving background.
Writing their norm sizes as \(X,Y\), \(L=XY\),
\(M=\min(X,Y)\), \(N_0=\max(X,Y)\), and letting \(G\) be the
multiplicity-two nonprincipal conductor norm, the absolute native
accounting cost at every fixed moment order is

\[
D^{k+\epsilon}H^{1/2}L^{1/2}
\left[
1+G^{1/12}M^{-1/3}
+G^{1/4}(M/N_0)^{1/6}
+G^{1/8}M^{-5/24}N_0^{-1/24}
\right].
\tag{4.4}
\]

All higher multiplicities and principal masks have been paid. Arbitrary
tuple selectors are allowed here because (4.4) bounds a positive
absolute accounting quantity.

For the exact feasible fourth-tuple pattern in Section 6 of the proof,
at

\[
H=D^{21/20},\quad L=D^{19/20},\quad
M=D^{1/8},\quad N_0=D^{33/40},\quad G=D^{1/2},
\]

the new bound gives

\[
                          \mathcal Q^\Phi\ll HD^{2-1/24+\epsilon}.
\tag{4.5}
\]

The specified earlier one-sign positive profile leaves an excess
\(D^{1/480}\) on this same feasible pattern. The improvement is relative
to the explicitly compared positive profiles, not a claim to dominate
every previous signed bound on a different complete block.

For the longest singleton core, \(L\asymp D^{2k}\), even the first
term of (4.4) is \(H^{1/2}D^{2k+\epsilon}\). A perfect absolute
conductor mean would still leave that cost. This is why the new conductor
theorem does not finish (1.2).

## 5. Why the exact Möbius prime/composite completion matters

[PRIME_DEGREE_COHERENCE.md](PRIME_DEGREE_COHERENCE.md) proves a finite
Hermitian collision-subtraction inequality. For \(|b_j|\le1\),
\(B=\sum_jb_j\), \(V=\sum_j|b_j|^2\), let \(Q_k(b)\) sum the
ordered Hermitian \(2k\)-tuples with every index distinct. For every
fixed \(k\ge1\) and \(0<\delta<1\),

\[
Q_k(b)\ge(1-\delta)|B|^{2k}
 -[((2k)!-1)^k\delta^{1-k}](1+V)^k.
\tag{5.1}
\]

The proof uses the exact partition-lattice Möbius coefficients.
Applying it to the native coefficients on prime columns, with
\(\nu=1\) and a fixed nonzero smooth \(0\le W\le1\) of compact support
inside \((0,\infty)\), gives, for \(0<h<6k/5\),

\[
\mathcal S^{\rm prime}_{2k}(D,D^h)
\gg \frac{D^{2k+h/6}}{(\log D)^{2k+1}}.
\tag{5.2}
\]

This is a lower bound for the **whole signed all-distinct prime-column
row sum**, not merely for selected positive rows. Literal sixth-power
rows produce the coherent spike; the row-summed collision correction
has smaller order.

Primality is an additional arithmetic column selector. Therefore (5.2)
does not refute the full composite native singleton core. It proves
that a theorem stable under every such selector would be false.
Cancellation between the prime part and the complete composite Möbius
part must remain available.

An additional local Mellin argument makes the same issue precise for
small prime-degree perturbations:
\(\mu_K(n)^2z^{\omega_K(n)}\), with \(z\) close to but different from
\(-1\), has Dirichlet series
\(\zeta_K(s)^z E_z(s)\). Its noninteger local order at one recreates a
principal-row obstruction. Sixth-power replicas carry it to a moment
limsup of at least \(2k+h/6\). The tangent
\(\mu_K(n)\omega_K(n)\) also has a logarithmic singularity.
These are exact obstructions to coefficient-insensitive extensions.

The note retains an exact prime-rooting identity, including the full
composite companion and all exclusions, as a possible interface for a
future signed dispersion argument. The identity supplies no moment
estimate by itself.

## 6. Other attacks tested and priced

The conductor addendum combines the new sextic pair estimate, the old
cubic pair estimate, the quadratic estimate and the single-label
estimates for the complete five-exponent family. In the balanced box
\(Q_1=\cdots=Q_5=X\), every displayed branch still permits \(X^{13/2}\).
Consequently minimizing or interpolating those upper bounds cannot
improve the source's universal weighted exponent \(11/8\).
A matching elementary upper calculation proves the exact limit of
that list. The initial floating-point search is not the proof.

Independently reflecting more conductor groups introduces larger dual
volumes if they are then bounded separately. The present work provides
no three-group signed estimate that pays those volumes.

Sparse scale sampling and rough-replica refinements in #914, #926 and
#929 remain useful at their source scopes. They do not supply the
arithmetic moment premise. This packet uses the interpolation idea for
a rigorous lower-bound obstruction rather than treating denser sampling
as evidence for the open upper bound.

## 7. Validation and review boundaries

[VALIDATION.md](VALIDATION.md) records exact commands, proof hashes,
review scopes, corrections and reproducible diagnostics.
[PROVENANCE.json](PROVENANCE.json) pins the external repository sources;
[MANIFEST.json](MANIFEST.json) binds the packet's files.

The three finite diagnostics use exact integer or rational arithmetic.
They check residue identities and masks, partition identities, primitive
necklaces, coefficient rectangles, and exponent bookkeeping. Normal
Python and `python -O` produce byte-identical reports. They do not
verify an infinite analytic estimate, the imported sieve, or RH.

Separate agents reconstructed the load-bearing proofs, with author
overlap disclosed. Their reviews caught and repaired scope issues
before publication. Same-team agreement is not formal verification,
external expert certification or integration into the accepted record.
The frozen mathematical content is separately bound to its Git commit
in the publication receipts.

## 8. The remaining target after this pass

The full generalized moment is still unproved. The new state is more
specific:

1. The original unfiltered contracts P13 and CT1 should not be used as
   viable sufficient targets with their stated quantifiers.
2. The necklace representation retains the physical horizons and has
   a proved polynomial bound at all frequencies. Its stronger signed
   trace estimate remains open.
3. The conjugate-pair conductor theorem improves the moving-background
   accounting and settles the absolute mean for the fully sextic local
   type. The long singleton term remains too large after absolute values.
4. The signed prime/composite Möbius completion must be preserved.
   Removing repeated columns or importing a coefficient-insensitive
   random model does not provide that cancellation.

If a bound \(M_{2k}\ll HD^{k+a_k+\epsilon}\) were eventually proved with
the source's full uniformity, the inherited extraction would price it at
\(\Re s>1/2+5h/(12k)+a_k/(2k)\). Approaching \(1/2\) requires the
remaining loss to be sublinear in \(k\). This packet does not prove that
premise or claim a new extraction boundary.
