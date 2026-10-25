# Independent review of the spectral growth and finite-selector consumers

Date: 2026-10-25.

Reviewer: marked-count agent, independent of the spectral author.

Verdict: PASS for the stated analytic component implications, at the
exact hashes below. No new zero-free region, all-scale spectral lower
bound, or positive-selector existence theorem has been established by
this review.

## 1. Exact reviewed objects

| File in second-pass/spectral | SHA-256 |
| --- | --- |
| SPECTRAL_GROWTH_AND_TIGHT_POSITIVE_SELECTION.md | 4db61773b675f4926731360eee769cd49cb66690a56f2a66cd02f902bf38e083 |
| EVEN_FINITE_SELECTOR_CONSUMER.md | 6c0a67ede84942a31287716661d5fe85644445a0517a296eed36be23c8036e74 |

The complete arithmetic operator and theta-tail estimates were checked
against the local first-pass dependency
standalone/2026-10-24-fresh-zero-free-routes/spectral/THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md,
SHA-256
783c98402482a109d3ebf5743792f3c6cb15cc1d17efe519014e65aa5c98196b,
whose source conventions are pinned to PR #1017 at
450dd8abecf58dfe60b3bc39bda0f792ea82ce95 and PR #1021 at
742e952be4ef7843de86ea12678c0bdd3d3579c3.

This was an analytic review, not a numerical computation of the full
operator's spectrum. No finite eigenvalues or sampled signs were used
to accept an all-scale hypothesis.

## 2. Spectral growth and the Laplace zero detector

The two-translate compression is correct. Two copies of a compact bump
with disjoint supports have identical diagonal form values \(q[g]\)
and orthogonal \(L^2\) coordinates. The smaller matrix eigenvalue is
\(q[g]-|C_g(t)|\). Thus the lower bound at \(a=t/2+R\) supplies the
claimed correlation growth bound, with exponent
\(\eta+\varepsilon/2\). Translation invariance applies to the complete
convolution form, including its pole terms.

With the given Fourier convention,
\[
 z_\rho=(\rho-1/2)/i,\qquad
 iz_\rho=\beta-1/2+i\gamma.
\]
The zero coefficient is
\(G(z_\rho)\overline{G(\overline{z_\rho})}\).
The Laplace denominator is therefore
\(w-(\beta-1/2+i\gamma)\), with the displayed positive residue.
There is no sign error.

Compact smoothness gives rapid decrease in the closed strip
\(|\Im z|\le1/2\). Together with \(N(T)=O(T\log T)\), this justifies
both the original Laplace interchange for \(\Re w>1/2\) and normal
convergence of its meromorphic continuation off the discrete poles.
Distinct zeros give different pole locations. Multiplicity adds
identical residues and cannot cancel them.

A sufficiently concentrated even nonnegative probability bump has both
required Fourier values near one at any prescribed zero. No universal
nonvanishing test or numerical zero list is required. The spectral
growth implication and its stated zero strip are correct; their
load-bearing lower-bound hypothesis remains unproved.

## 3. The even-only Landau argument

For real even \(g\), the symmetric sum of the two translates is even.
Its form is \(2q[g]+2C_g(t)\), so the even spectral bound gives only a
one-sided bound on \(C_g\). The note correctly adds \(Ce^{\delta t}\)
to make a nonnegative function. The added transform is
\(C/(w-\delta)\), with positive sign.

The meromorphic continuation has no real pole above \(\delta\).
The exclusion of real nontrivial zeta zeros is correct: pairing the
alternating series gives a positive numerator, while
\(1-2^{1-s}<0\) for \(0<s<1\).

The included Landau proof is valid. A Taylor disk crossing a finite
real convergence abscissa, expanded from its right, has nonnegative
terms when evaluated to the left. Tonelli forces convergence beyond
the alleged abscissa. Differentiation is justified by the strict
rightward gap. Hence the nonnegative Laplace transform is holomorphic
on \(\Re w>\delta\). A nonzero residue from a chosen zero in that
half-plane is impossible. The even-only inference is sound.

## 4. Finite projection and the unbounded form domain

The infinite convolution construction of a nonnegative compact smooth
bump with Fourier decay \(\exp(-c|t|^{2/3})\) is valid. A block of
\(\asymp |t|^{2/3}\) sinc factors has modulus at most \(1/2\), while
all remaining factors have modulus at most one on the real line.
Fourier inversion gives the smooth density. Rescaling supplies any
needed small support.

For translates inside the period cell, Fourier coefficients are sampled
transform values times phases. At \(N_k=\lceil k^3\rceil\), the
physical cutoff is of order \(k^2\), giving the uniform function and
first-derivative error
\[
                    d_k\ll k^C e^{-c k^{4/3}}.
\]
The possible jump of the zero-extended projection at an endpoint is
handled correctly. The note uses integration by parts to get
\[
 |\widehat r(t)|\ll kd_k\min(1,|t|^{-1}),\qquad
 \int\log(2+|t|)|\widehat r(t)|^2dt\ll k^2d_k^2,
\]
with a harmless equivalent constant near \(t=0\). This controls the
logarithmic archimedean form. The cross term tends to zero by weighted
Cauchy--Schwarz. No false \(H^1\) claim is made for this discontinuous
extension.

The pole operator has norm \(O(e^k)\); the complete finite prime-power
operator has norm \(O(ke^k)\), from summing
\(\Lambda(n)/\sqrt n\) through \(e^{2k}\). Both form errors vanish,
since \(e^{Ck}d_k\to0\). The same decay absorbs the small norm error
multiplied by the assumed spectral growth bound.

Thus the exact finite lower bound applies to projected two-bump tests.
It is never promoted to an infinite-dimensional lower bound. The
resulting finite spectral-growth consumer is correct.

## 5. Theta residual, endpoints, and normalization

Periodization of a probability density has mass one per period.
Fourier truncation retains its constant coefficient exactly. If
\(a_k=(S_k\phi)(k)\), endpoint subtraction changes the mass to
\(1-2ka_k\). The tail estimates give \(ka_k\to0\), so normalization
is legitimate and tends to one.

An even cosine polynomial has derivative zero at both endpoints.
After subtracting its common endpoint value, it also vanishes there.
The zero extension is therefore \(C^1\), belongs to the strong domain
of the logarithmic multiplier, and permits the claimed operator/form
pairing.

For the broad comparator, convolution at scale \(k/2\) gives squared
norm \(O(1/k)\) by Young's inequality. Its Fourier multiplier has
modulus at most one on the real axis, so the same truncation estimates
apply. Endpoint subtraction and normalization are negligible. The
resulting comparator has bounded total variation even if the endpoint
correction produces a small negative part.

For either corrected vector, the global residual bound
\[
              |r_k(x)|+|r'_k(x)|\le B_ke^{-2|x|}
\]
includes normalization error inside the interval and the uncut source
outside. The full operator then has the claimed uniform bounds:

- Both pole terms are at most \(CB_ke^{k/2}\).
- The archimedean bracket is \(O(B_kt)\) for \(0<t\le1\), cancelling
  its \(1/t\) singularity. The remaining integral is \(O(B_k)\).
- Every prime power, including those beyond the compact translation
  range, is bounded using
  \(e^{-2|x\pm\log n|}\le e^{2k}n^{-2}\) and the convergent sum
  \(\sum_{n\ge2}(\log n)n^{-5/2}\).

This gives a full sup-norm residual, not only a form estimate. The
displayed bound for \(B_k\) implies \(k\varepsilon_k\to0\).
The continuum broad comparator similarly satisfies
\(a\varepsilon_a^{\rm broad}\to0\).
These rates were made explicit after a clarity request during review;
the exact hashes above include that correction.

## 6. Tightness, legality, and signed variants

Positive mass-one selectors with uniform tightness put fixed positive
mass in one central compact interval. The narrow theta approximants
are uniformly positive there. In the finite construction their
negative sup norm outside that interval tends to zero, so the global
overlap still has a strictly positive lower bound. No \(L^2\) bound
on the selectors is needed.

The narrow pairing gives
\(c_j=-\kappa_j\langle f_j,v_j\rangle+o(1)\).
For negative shifts, the broad mass-one competitor gives
\(c_j\le\varepsilon_j+C|\kappa_j|/a_j\), forcing \(\kappa_j\to0\).
For nonnegative shifts, unit mass and support give
\(\|w_j\|_2^2\ge1/(2a_j)\); the stronger residual rate above forces
these shifts to zero as well.

For the finite matrices, legality is required only for the exact finite
compression. The inequality \(\lambda_k>\kappa_k\to0\) supplies the
finite spectral-growth premise, which already has its own even-sector
consumer. Infinite-dimensional legality is not inferred.

The signed overlap/variation variant correctly retains the total
variation factor in the residual. Under the alternative exponential
variation bound with exponent \(>1/2\), the arithmetic growth
\((1+|x|)e^{|x|/2}\) of \(K_W*h\) is integrable uniformly against the
selectors. A mass-zero compact test that does not annihilate the weak
mass-one limit exists: otherwise that finite measure would be a
constant multiple of Lebesgue measure. The resolvent equation then
bounds the legal shifts on a cofinal subsequence.

The weighted negative-part inequality is correct by evenness and
\(e^{\alpha|x|}\le2\cosh(\alpha x)\), applied to total variation.
The real-zero canonical-product bound is explicitly an additional
pinned input. Real Fourier zeros are not used to infer physical
positivity.

## 7. Accepted scope

The accepted results are analytic consumers: spectral growth bounds
imply zero strips; the specified positive tight selectors imply RH;
and the prescribed finite even Fourier matrices are an adequate
cofinal discretization for these implications.

The notes do not prove the required all-scale lower bound, construct
the required cofinal positive tight selectors, or infer either from
sampled numerics. No unresolved defect was found at the reviewed
hashes. This review makes no priority claim for the general Weil or
Landau principles.
