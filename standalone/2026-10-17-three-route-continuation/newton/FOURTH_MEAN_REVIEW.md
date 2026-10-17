# Cross-review: fourth numerator mean and the 49/54 comparison

Status: **No defect found in the reviewed deductions.** This is a scoped
independent mathematical review of PR #966, Theorem A, and of the new
fourth-mean interpolation and comparison bookkeeping. It does not review
#966's new zero detector or Theorem B. It does not independently rebuild the
imported theta/Poisson identities, character adapter, reflection theorem,
large-sieve theorem, or classical approximate functional equation (AFE).
The all-field conclusion remains a proposed composition from those stated
analytic inputs; this review is not an RH proof or an integration decision.

## 1. Exact contents and source checks

Theorem A was fetched independently from PR #966 at commit
`8d94494698ee447711a53dec922986586418e398`, path
`standalone/2026-10-17-selected-fourth-density/PROOF.md`:

- Git blob: `08195836816c1e3718c04e0b966bf89a0b5dad01`.
- Fetched UTF-8 content SHA-256:
  `afda1d2b222a952a3c2f12b255ef9c7f5cf558ef1fd201220ed83b033e7cb790`.
- Local `concurrent/proof966.md` adds one blank final line and has no other
  difference; its SHA-256 is
  `99123c93010f0b4e78e841955c5ef3b33018957dfaea192d62b6c4d08b6dbfed`.

The reviewed local composition and checker hashes are:

| File under `research_work/theta/` | SHA-256 |
|---|---|
| `FOURTH_MEAN_EXTENSION.md` | `ce87e3d482cd0b4fa806c55adf266a2a76a4ef46ea68f9dbd0c319a27a168d95` |
| `verify_fourth.py` | `9c432b418152b55a7a19e05031c5fdac7ec19b6c4788b529c37c992b57be4f42` |
| `FOURTH_CHECKS.json` | `2e5c293c23854661ad6b2f6ab75aaa9760caa7e64c283dc57727bd7ba85e6654` |
| Imported `verify_theta.py` | `d2c77035fd5cfa7ceea2217d3fc51cc99bcec44b74220073efaf1df11a72fc98` |

The corrected prose around equation (1.3) is included in this review. A
later mathematical edit requires an updated review identity.

Primary source consulted directly: Alexandre de Faveri,
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1,
the definitions of the two sieve families, Sections 2.3--2.5, and the AFE
separation in Section 8. The family is indexed by full ideal norm, and the
flat sieve permits sixth-power-free ideals on both sides. Section 2.5.1
gives the conductor as a fixed-S factor times the product of primes whose
index valuations are not divisible by six. Thus for flat rows it is a
fixed-S factor times the radical. Section 2.3.4 explicitly retains the
zero extension at nonunits. These are the conventions needed below.

## 2. Theorem A: full columns, ramification masks and AFE

The deduction of

    sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^4
        << U^(7/6+eta)(2+|t|)^C

from the stated sixth-order sieve is sound for the fixed family and twist.
The following points are load-bearing.

1. A twist unramified outside the fixed S cannot cancel the nontrivial
   tame inertia of a flat row at an outside-S prime. The conductor norm is
   therefore O(Na), rather than an unproved norm comparison. Fixed S and
   finite archimedean types can be subdivided. If the primitive AFE includes
   S-supported columns, they can be separated and summed with their
   convergent norm-to-the-minus-one-half weights; omitting those primes in
   the target L-function changes only fixed local factors. A principal row
   is bounded separately in the central moment and is excluded from the
   later holomorphic-strip interpolation.

2. AFE separation occurs before use of the sieve. Common finite cutoffs
   can be chosen from the largest conductor, the rapid original tails
   retained, and Mellin inversion performed on the truncated sums. The
   small positive Mellin lines introduce arbitrarily small norm losses
   and polynomial height factors. This avoids taking a row-dependent
   supremum over coefficients. Integrable, polynomially weighted kernels
   allow Minkowski. Bounding the original and dual sums separately removes
   the modulus-one root number without deleting any term.

3. Squaring produces ideals b of norm at most V, with coefficients bounded
   by (Nb)^(-1/2+delta) after absorbing the divisor factor. Equality of
   rational norms does not identify different ideal columns. Complete
   multiplicativity remains valid at zero values.

4. The decomposition b=c d^6 is unique, with c flat, and does not require
   coprimality. The factor 1_((a,d)=1) in the displayed character identity
   is necessary. Minkowski first separates the d summands in the row
   l-two norm. For each fixed d, dropping that positive row restriction
   is then legitimate for an upper bound. The sieve coefficients are
   common within that summand. This yields the summable weight
   (Nd)^(-3+O(delta)); columns of length below one are empty.

5. At V<=U^(1+O(delta))(2+|t|)^C, the two mixed sieve terms give the
   exponent 7/6+O(delta). Squaring the l-two bound and integrating the
   separated kernels gives the claimed fourth mean. Conjugation gives
   the same sieve norm, so the dual family requires no unsupported change
   of the full-norm ordering.

This is a classical moment deduction from the imported sieve and AFE.
It is a numerator moment; it provides no bound on reciprocal L-functions
or on the signed physical principal projection.

## 3. Interpolation and exceptional subsets

The finite-vector duality argument in Section 2 is correct. The analytic
dual weights have l-(4/3) norm one on the left and l-one norm one on the
right, and equal the prescribed dual vector at the interior point. The
fixed Gaussian controls polynomial vertical growth. Since p_delta<p,
passing to the larger p decreases the finite-vector norm. Choosing a fixed
delta after the permitted norm loss gives

    ||L(sigma+it)||_(2/(1-sigma))
        << U^((7/12)(1-sigma)+eta)(2+|t|)^C.

Holder on any subset of at most U^nu rows and reflection across the
critical line consequently give exactly

    sum_E |L(y+it)|
        << U^(1/2+nu-y*(5/12+nu/2)+eta)(2+|t|)^C,

for each fixed 0<y<1/2. The conductor factor U^(1/2-y) has been retained.
The inherited imprimitive Euler-product argument applies on these fixed
positive lines. At y=1/2 the exponent is 3nu/4+7/24. The savings over the
second-mean interpolation and individual convexity are, respectively,
y(5/6-nu)/2 and y(nu-1/6)/2. No independence of a subset selected by
denominator zeros is needed.

## 4. Comparison at a=4/9

The new scales and Mellin shift are consistent: h=5/9, theta=2/9,
b=37/54, and b+theta=49/54. The good class is allowed to tie theta at zero
loss because all actual contours use a fixed e>0. The first contour is
2/3+e, so the strict correction-domain inequalities are satisfied.

The middle classes correctly use the lower threshold for counting and
the upper threshold for their zero-free rectangle. Central fourth means
are used below three quarters, reflected fourth interpolation above it,
and convexity only for the last class. This preserves the correction
condition 3x+y>5/2, which would fail if reflection were used too early.
The original DF density is sufficient; no improved detector from #966
enters this composition.

As an independent analytic check on the middle-row saving, write

    d(s)=-144s^2+264s-106,
    n(s)=-216s^2+342s-127,
    g(s)=n(s)/d(s),                 2/3<=s<=11/12.

At zero loss and coincident thresholds the central and reflected gaps
below theta have numerators

    P_c=31104s^3-70560s^2+52572s-12844,
    P_m=18720s^3-41052s^2+29752s-7108,

and denominators 216d and 108d, respectively. On the final DF branch use
d_h=1-24(1-s)^2 and

    P_h=3000s^3-7332s^2+5939s-1589,

with denominator 108d_h. Their cubic Bernstein coefficients are:

| Polynomial | Interval | Bernstein coefficients |
|---|---|---|
| P_c | [2/3,3/4] | 60, 59, 116/3, 17 |
| P_m | [3/4,5/6] | 47/4, 187/36, 10/9, 31/3 |
| P_m | [5/6,11/12] | 31/3, 176/9, 505/12, 355/4 |
| P_h | [11/12,1] | 355/72, 79/12, 373/36, 18 |

Thus the continuous middle gap is at least 1/1458, using d<=15 and
d_h<=1. A grid step 1/6000 loses at most (115/108)/6000, smaller than that
margin: the energy derivatives in the upper threshold, with the counted
exponent fixed, are 1 centrally and (85+30nu)/108 after reflection. This
check is deliberately weaker than the complete finite checker; it verifies
why the middle-row obstruction disappears without the new zero detector.

The other ranges are accounted for correctly in the stated interfaces.
Keeping principal xi on 1+e avoids presupposing the proposed zero-free
conclusion. The small-norm move to z=1/3 is material: it crosses no relevant
pole and gives 20099/108000+e, whereas the old z=2/5 line would exceed the
zero-loss budget with the fixed positive cutoff. The large-norm shift
z=10/e+2 uses its positive e cutoff gap and gives -44/9-e at the first
dyad. The joint Gaussian and Schwartz decay argument retains the nearly
cancelling imaginary directions and uses fixed decay orders after the
polynomial height exponents are known. These tail mechanisms are assessed
as compositions of the stated inherited bounds, not fresh proofs of the
theta kernel's analytic foundations.

The lower limit 49/54 is a limit of the specified balanced good-class
budget: the zero-loss requirement is x-a<=a/2 with x>=2/3. It is not a
universal obstruction to other arguments. The final conclusion uses an
arbitrarily small fixed e for each point strictly to the right of 49/54;
it asserts nothing on the boundary line.

## 5. What was run, and limits of this review

I ran `python3 verify_fourth.py` once and inspected its exact-rational
implementation and imported bookkeeping utilities. It passed all 1642
classes, including the exact minimum middle constant margin
118384121/35223109200. The reported classes are 1 second-mean, 500
fourth-mean, 1140 fourth-interpolated and 1 convexity class. The Bernstein
checks cover the full interval 0<e<=1/1000000; the explicit failure checks
remain active under Python optimization. I did not independently rerun
the mutation suite. The replay verifies finite algebra and contour-domain
bookkeeping, not the imported analytic theorems.

The independent 9081/10000 theorem has not acquired a #966 dependency.
The extra 49/54 claim should retain its separate identity and its exact
new fourth-mean source. No claim about #966's selected-character count,
Theorem B, or its separate 109/120 composition is covered here.

Separately, as requested before freezing, `newton/check_newton.py` now
fails immediately under `python -O` or `python -OO`, before any replay can
run with disabled assertions. One normal replay regenerated `audit.json`
and passed its existing 22 complete finite cases; `python -O` failed as
intended. No larger Newton testing was done. The new checker SHA-256 is
`7194d6f9f7b4410c4df3e5a97d6c9b5adf750c1d1755ebc0e6aed44ae7dcaef9`;
the audit SHA-256 is
`cfb2327aa04ea9c781fd4c24c264a6a1ae6c6dbc3514b5c899388f0a7ac22b46`.
The Newton proof content was unchanged.
