# Independent review of the asymmetric coherent far tail

**Verdict: PASS within the explicitly imported Eisenstein framework.**
I independently checked the unequal-cutoff identity, common-puncture
adapter, global capped pointwise estimates, full coherent far-tail
argument, unchanged head argument, and the precise remaining middle
expression. I also checked the separate scalar resource discussion in
Section 6, with its stated limitations.

The new result controls an actual coherent far component. The coherent
middle-band hypothesis remains open. This review does not independently
certify the imported global finite-order cap or original inverse moment,
and it does not claim a new unconditional zero-free region.

## 1. Exact reviewed bytes

Hashes below were computed from the local files after the author added
the explicit full-column/powerful-row derivation requested during review.

| File | Bytes | SHA256 | Git blob SHA1 |
|---|---:|---|---|
| `ASYMMETRIC_HB_TAIL.md` | 20,324 | `8d13f547d0beda762f313b76f428ae6cd94f0e8d0af7fec8d3be64502c770c12` | `863354900bbbbbfaf8e7c7685976441199a18132` |
| `check_asymmetric_hb_tail.py` | 8,432 | `b363213fc727ccaddd30ad2ff550d6ba31ba417fb7ee2437172e53b21ea51903` | `edb3a6a0ab9c4434ea4639b66d00f5a2141140e8` |

The head input is the separately reviewed `INVERSE_POWER_COMPONENT.md`,
SHA256 `46821c4854806910b434c11c7a3560fd2f5a75ef5e52c35414f01e83e86d7437`.
No remote commit is authenticated by this local binding.

## 2. Actual arithmetic inputs and the puncture adapter

I read the original `lem:inverse-amplification` directly in the pinned
[September 30 source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, reported Git blob
`268c4e3206d460c617d3d2129742a72b831b3def`. Its bounded-length native
inverse estimate and fixed polynomial cost for the admitted rowwise test
parameters are the quantities used in (4). No arbitrary-coefficient
moment is substituted.

Equation (5) is the correct local Euler inversion. Removing the primes
of a common puncture multiplies the inverse Dirichlet series by
`prod_(p|Q)(1-psi_u^0(p)(Np)^(-s))^(-1)`. Its coefficients on
`Q`-smooth ideals are `psi_u^0(h)`, with no extra Möbius factor.
The central normalization contributes `(Nh)^(-1/2)`. Original zeros
in `psi_u^0` remain, and the new puncture is common within the row sum.

The geometric scalar mass is a small power of `U` for the prescribed
radical bound. The shorter lengths have no greater inverse exponent,
because `e(b)=max(1,(1+5b)/6)` is nondecreasing. Bounded scales near
length one are covered by a fixed annular rescaling. The row-dependent
primitive phases are bounded scalars inside Minkowski; they do not
create row-selected column coefficients.

The pointwise estimate (6) is valid for both the plain and inverse
factor. For the nonprincipal finite-order family, the global cap makes
`L_orig` and its reciprocal holomorphic on each shifted line to the
right of `7/8`. The Euler-normalized logarithm and three-circles argument
give a subpower conductor/height bound there. Common natural deletion
factors are nonzero and have the admitted polynomial radical bound.
The ordinary factor crosses no pole. Global height scope is used here,
so no buffered-height theorem is extended by assertion.

## 3. The unequal identity and the complete coherent far estimate

For the smooth cutoffs `m_1,m_2`, the factors
`delta_1-m_i*1` start above `y_i`. Their product therefore vanishes
through `y_1 y_2`. Convolution with Möbius proves exactly

\[
             \mu_E=m_1+m_2-m_1*m_2*1
                         \qquad(Nn\le y_1y_2=2D).
\]

Both linear terms vanish on the original annulus for sufficiently large
`U`. In particular `2y_2=4D/U^alpha<D` once `U^alpha>4`.
This threshold is large but fixed. It affects the implied constant and
is not a numerical height verification. Every noncoprime factorization
and repeated-prime term is retained.

The three selectors in (10) sum to one identically. Their common
nonincreasing smooth cutoff gives the stated coherent head, middle and
far expressions; the overlapping transition ranges are part of those
definitions. The far term is not a literal sharp outer cutoff.

On each supported far triple, its dyadic log-lengths satisfy

\[
 a+b+c=r+O(1/\log U),\quad
 a\le\alpha+O(1/\log U),\quad
 a+b\ge1-O(1/\log U),\quad
 b\le r-\alpha+O(1/\log U).
\]

The common product profile separates smoothly. Its normalization is
`sqrt(ABC/D)`, bounded on a nonempty triple. The cutoffs and the far
selector have uniformly bounded logarithmic derivatives, including
when one cutoff argument is much larger or smaller than its transition
range. The separated factors retain one common character, both actual
Möbius coefficients and the ordinary coefficient one.

Using pointwise capped bounds on the first inverse and ordinary factor,
then the original second moment on the second inverse, gives exactly

\[
                   e(b)+\frac34(r-b).
\]

I checked both branches algebraically on the full interval. For `b>=1`,
the gap from `e_0(r)=(1+5r)/6` is `(r-b)/12`. For `b<=1`, it is
`-5/6+r/12+3b/4`, whose minimum over the admitted short branch is
`(r-1-9alpha)/12`. Hence for `r>=1+10alpha` both gaps are at least
`alpha/12`. With `alpha=2/125`, these are exactly

\[
                r\ge\frac{29}{25},\qquad
                \text{saving}=\frac1{750}.
\]

This argument handles every supported far triple, including `R`
comparable to `D`. It is not a selection of favorable triples.
Minkowski over the common Fourier integrals and the logarithmic number
of dyadic triples gives the norm of their coherent sum. Fixed finite
orders absorb all norm frequencies and profile parameters before the
consumer chooses its polynomial height. No extra independence between
the two inverse factors is assumed.

## 4. Head compatibility and the exact residual hypothesis

The head proof uses only the smooth outer fourth-moment envelope and
the ordinary reflected moment. In its two-factor separation,
`w_0(Ax/y)w_0(By/y)` may indeed be replaced by
`w_0(Ax/y_1)w_0(By/y_2)`: both derivative families are uniform and
the logarithmic factor lengths still add to the same outer product
length. The primitive reflection and its normalizers do not require
equal inverse cutoffs. This validates (19) with the same

\[
                 \Gamma_0=83/24-\sqrt{195}/6.
\]

This use retains the printed `.51` floor. The optional adjustable-floor
deduction is unnecessary. The strict head margin from the previous
review still applies throughout the new consumer interval.

The residual middle term has the exact weight

\[
       \chi_0(Nr/U)-\chi_0(Nr/U^{13/20})
\]

in the *unequal*-cutoff convolution. Its support is
`U^(13/20)<Nr<2U`. The new sufficient condition (M) concerns this
single coherent term, not a sum of unrelated absolute component bounds.
It is a different expression from the symmetric tail in the earlier
consumer, and the note does not identify the two pieces.

If (M) is proved, the three-component Hilbert-space triangle inequality
gives the complete native inverse saving `1/1000`; the far saving has
the exact reserve `1/750-1/1000=1/3000`. That full inverse estimate is
the input used by the frozen scalar consumer. Thus the conditional
boundary follows from (M) without changing its scalar certificate.
This implication does not establish (M).

## 5. The separate resource-contact discussion

I checked Section 6 as a scoped statement about the listed estimates,
not an assertion that saturating arithmetic rows exist. At `g=delta/2`,
substituting the stated optimized `R,r` into the two formulas (22)
gives `b_*+c_*=r`, with both individual marked count exponents equal
to `R`. The pointwise product size then reproduces the old inverse
contact. The unit in the first inverse factor is an actual term of the
unequal identity; no cancellation of the complete middle sum is ruled
out by observing that term.

I also verified its placement without relying on decimals. From the
previous exact enclosures
`7497/10000<=kappa_c<=3/4` and
`469/1000<=delta_c<=47/100`, write

\[
 A=5/6-\delta,\qquad
 f=\frac{4-2/(3\kappa)}{2(5-2/(3\kappa))},\qquad
 b_*=1-\frac{Af}{A+\delta f}.
\]

The last expression increases with `delta` and decreases with `kappa`.
Exact endpoint evaluation therefore gives

\[
 \frac{37}{50}<\frac{44837}{60139}
      \le b_*\le\frac{11197019}{15010057}<\frac34.
\]

It lies strictly between `.65` and `1`, and below `r_c-alpha` since
`r_c>29/25`. The cited critical block is therefore inside the actual
middle support with its long inverse cutoff identically one.

The inverse-power comparison is a direct consequence of its envelope
being a supremum of affine functions; Hölder cannot push it below that
same formal affine competitor. The statement remains restricted to
these resource bounds.

During review I requested an explicit source for the final claim about
higher ordinary moments. The accepted bytes now give it: expand a fixed
power of a plain block into its divisor-bounded column coefficients,
use the pinned squarefree-row full-column bound, and split the actual
physical row into a powerful part and squarefree part. The resulting
resource is

\[
              U+U^{1/2}N^q+(UN^q)^{2/3}.
\]

For `s=q log_U N`, its third exponent is no larger than
`max(1,1/2+s)`. The formal class satisfies that resource because
`R_c+delta_c/2<1`. This only checks the named sieve resource for a
fixed higher moment; it is not a lower bound on possible stronger
moments or a proof that the middle band cannot be estimated.

## 6. Checker replay and verification limits

I read and independently ran `check_asymmetric_hb_tail.py` under
`python -O`. It passed 586 unequal-cutoff convolution cases, four
generic affine coefficient identities, 9,393 far-range comparisons,
300 exact resource contacts, and 12,600 individual-resource checks.
The repeated-prime and excessive-saving negative controls were active.
All acceptances use explicit `require` calls.

The universal far-range proof is supplied by the generic affine
identities and monotonicity of the short branch, not by the sampled
rational comparisons. Decimal critical values are diagnostic only;
the independent rational enclosure above certifies the placement used
in this review.

No remaining issue was found in the accepted deductions. Their premises
remain the pinned finite-order cap and moments, and the actual coherent
middle-band second moment remains the open arithmetic task.
