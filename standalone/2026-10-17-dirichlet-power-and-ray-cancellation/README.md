# Dirichlet power cancellation and native angular-ray cancellation

**Status: proposed component mathematics, with complete written proofs and
finite checks. RH remains unproved.** The Fourier theorem is a deduction
from an explicit common Dirichlet zero-free-strip input, supplied by the
reported OpenAI 7/8 theorem. The angular-ray theorem is elementary and
unconditional, and does not use that input. Neither is integrated as
accepted mathematics or independently certified by a proof assistant.

This packet continues #962 at
`b2032c663736ecd1e3872559d160ce069664ea06`. The live #963--#969 work was
read at the scopes recorded in LATEST_REVIEW.md before choosing these
two different attacks. It adds no numerical Dedekind zero-free exponent.

## 1. A true additive power saving for the complete norm source

For any fixed finite list of Dirichlet characters xi_1,...,xi_r, put

    a=(mu xi_1)*...*(mu xi_r).

If ALL primitive Dirichlet L-functions have no zeros in Re(s)>theta,
with 2/3<=theta<1, then for every epsilon>0,

    sup_(alpha real) |sum_(n<=X) a(n)e(alpha n)|
           << X^((1+theta)/2+epsilon).

There is no loss depending on the fixed convolution order r in this
exponent. The proof first derives conductor-uniform reciprocal estimates
from the common strip, keeps the square-root oscillatory Mellin cost in
the major arcs, and uses a finite inverse identity plus bilinear estimates
on the remaining frequencies. Every prime-power cofactor and original
Dirichlet-character zero is retained.

For K=Q(sqrt(-3)), the actual full norm coefficient is

    a_K(n)=sum_(NI=n)mu_K(I)=mu*(mu chi_{-3})(n).

It has a_K(p)=-2 at split primes: it is not a one-bounded multiplicative
function. At the reported common theta=7/8, the result gives

    sup_alpha |sum_(n<=X) a_K(n)e(alpha n)|
                   << X^(15/16+epsilon).

This replaces a logarithmic saving by a positive power, uniformly in
additive frequency, for this complete source. At alpha=0 the imported
strip already gives the stronger exponent 7/8+epsilon. The new conclusion
is uniformity over all additive frequencies; it cannot improve its own
zero-free input by evaluating alpha at zero.

The elementary completion adapter retains asymmetric fixed ideal
exclusions, the native/coupled/two-channel/geometric families, every
original column cap, and full Gaussian tests. For any FIXED k it gives
the complete capped norm tensor exponent

    1-1/(16k)+epsilon.

Degrees m>=2 and bounded powerful-prime profiles are uniform in the
stated coefficient norm; conductor, k and fixed norm twists are not
silently allowed to grow. Endpoint-maximal growing-shift covariances
also acquire a power saving in the explicit long-shift range.

Read DIRECT_FOURIER.md, STRIP_AND_MAJOR_ARCS.md, and
COMPLETION_AND_COVARIANCE.md for the complete statements and proofs.
The rational mu case and major-arc mechanism are classical
Baker--Harman theory. No worldwide priority is asserted for the
fixed-product adapter or its consequences.

## 2. An angular second mean with the radial parameter fixed

Fix K=Q(sqrt(-3)) and a fixed excluded set consisting of all prime ideals
above the rational primes dividing a squarefree Q with 6|Q. For
psi_l((alpha))=(alpha/|alpha|)^(6l), define the actual native sum

    A_(t,l)(X)=sum_(X/2<NI<=X, (I,S)=1) mu_K(I)(NI)^(it)psi_l(I).

For normalized discrete Gaussian weights p_R of width R>=1, every
integer center l0, and every real t,

    sum_l p_R(l-l0)|A_(t,l)(X)|^2
               <<_Q (1+|t|)^2 X(1+X/R).

The underlying rational-ray diagonal has order X for every fixed t.
Thus R>=X gives the correct second-moment order with **no radial
averaging**. The full logarithmic Gaussian column, including every tail
and cross term, has angular-only critical energy O(log D) at R=D and
t=0. This is a new source-specific component relative to #963's
coefficient-uniform geometric argument.

The arithmetic reason is the unique decomposition I=(a)J into a positive
rational content and a primitive ideal. For squarefree I,

    mu_K((a)J)=mu_K(J)mu(a)^2 chi_{-3}(a),
    (a,Q NJ)=1.

Squarefree inversion and the cancellation of this fixed periodic
character give square-root cancellation along each rational ray, with
a cofactor weight whose mean stays bounded. The proof uses those actual
signs before taking an angular norm. It does not replace the source with
arbitrary coefficients or a random prime model.

Read NATIVE_ANGULAR_RAY_MOMENT.md. Its saturated-S condition differs
from the more flexible S in the Fourier result and is not relaxed by
combining the two theorems. The moving-angle control in
ANGULAR_HULL_OBSTRUCTION.md explains why the remaining angular
average cannot be removed by a bound uniform in its center.

## 3. The precise remaining task

The Fourier result has exponent 15/16, not 1/2. The angular result has
a probability average over infinite-order angular characters, not a
bound for its principal member l=0. Positivity alone extracts that
member at a factor proportional to the angular width. These results
therefore do not prove the fixed-principal critical energy estimate.

The useful change in strategy is concrete: there is now proved signed
cancellation along the actual rational rays, and a separate uniform
additive power estimate for the complete norm coefficients. Any proposed
composition must identify how it estimates the remaining cross-ray
coherence at the fixed principal angular character. That step is open.
Further exponent tuning of the already used positive theta estimate
does not supply it.

## Reading and reproduction

- LATEST_REVIEW.md: the current repo and new external-paper audit.
- SOURCES.md: exact imported scopes and primary-source locators.
- REVIEW.md: parallel proof reviews, corrections, and review obligations.
- VALIDATION.md: what each finite checker does and does not authenticate.
- SHA256SUMS: a byte manifest, not a mathematical certificate.

Run `python replay.py` from this directory to reproduce the archived
finite reports in ordinary and optimized Python. No Lean build, zero
census, numerical L-value experiment, full-repository validator, or
remote CI result is implied by those checks.
