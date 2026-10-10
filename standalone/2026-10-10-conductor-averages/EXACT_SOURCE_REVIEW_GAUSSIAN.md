# Exact-source review receipt: Gaussian sampled moments

**Reviewer:** /root/joint_spectral_attack.
**Review date:** 2026-10-10.
**Role:** independent mathematical reviewer of the Gaussian note.
The reviewer did not author GAUSSIAN_SAMPLED_MOMENTS.md. This is an
AI-agent review, not human external acceptance or formal verification.

## 1. Frozen repository identity

The reviewed repository object is:

| Item | Exact identity |
|---|---|
| Repository | GettysburgResearch/riemann |
| Source commit | 38ee7069e23ae24fd693e70149dc817900c3caa4 |
| Source tree | 6df69e2b5674372695530860f9528b8db7aee9ff |
| Parent commit | 506e3808d2f1e86a31a6d1f70cc7da58367c9918 |
| Packet | standalone/2026-10-10-conductor-averages |

I independently resolved the commit, tree, and parent in Git, then
read the complete committed Gaussian source and both committed
Gaussian content reviews with git show against this source commit.
The identities below were calculated from those committed bytes,
not inferred from filenames or from the working-tree versions.

### Mathematical source

[GAUSSIAN_SAMPLED_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/38ee7069e23ae24fd693e70149dc817900c3caa4/standalone/2026-10-10-conductor-averages/GAUSSIAN_SAMPLED_MOMENTS.md)

| Item | Value |
|---|---|
| Git blob SHA | 31c446ef6dce84a38cdf5d7024b75da56d1e9af2 |
| SHA-256 | 53625b2fc8da8162792bb40cbb329cd609ddf152d362f05fad32ac7b841d41d4 |
| Bytes | 22,774 |

### First independent content review

[REVIEW_GAUSSIAN_SAMPLED_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/38ee7069e23ae24fd693e70149dc817900c3caa4/standalone/2026-10-10-conductor-averages/REVIEW_GAUSSIAN_SAMPLED_MOMENTS.md)

| Item | Value |
|---|---|
| Reviewer | Root research agent |
| Git blob SHA | 35c2598ea6f40174906208fcb389eaeab04e6b42 |
| SHA-256 | 783afecb330858a3ea2bd306359e64fe21a6c785cea4fdf61fabf9ea1a0d5a85 |
| Bytes | 5,638 |

### This reviewer's independent content reconstruction

[REVIEW_GAUSSIAN_SECOND.md](https://github.com/GettysburgResearch/riemann/blob/38ee7069e23ae24fd693e70149dc817900c3caa4/standalone/2026-10-10-conductor-averages/REVIEW_GAUSSIAN_SECOND.md)

| Item | Value |
|---|---|
| Reviewer | /root/joint_spectral_attack |
| Git blob SHA | f8890c781b37a2153850523199bfe3f4e8f80077 |
| SHA-256 | 15cc6cac6fab6271cad75bb1cd2340281fc392fd0ebec61af8873eeb9d812feb |
| Bytes | 7,830 |

Both content reviews identify the same source SHA-256 recorded
above. My earlier independently reconstructed source is identical
to the now-committed mathematical source.

## 2. Mathematical verdict on the committed source

**Accept at the exact source identity above.** The deterministic
Gaussian sampling, maximal recovery, finite-truncation, and causal
inversion arguments are valid. The moment-to-zero implication is
valid with its stated arithmetic moment premise and fixed primitive
Hecke-character framework.

This verdict follows from independent reconstruction of the
arguments, followed by complete rereading of the committed source
and confirmation of its identity. It is not a verdict obtained
solely by comparing hashes or adopting the other review.

The decisive checks are:

1. The ideal count and Stieltjes integral give a uniform
   \(O(D)\) Gaussian count for every \(D>0\). The complex Gaussian
   has the exact modulus used in the entire-family bound.
   Cauchy's formula at radius \(\sqrt m\) gives the required
   all-order factor \(m^{-m/2}\), and the detector Mellin transform
   is exactly the nonvanishing function \(e^{s^2/2}\).

2. The arbitrary measurable aperture supplies separated
   interpolation nodes after Chebyshev. The factorial denominator
   products control the Lagrange basis. The divided-difference
   integral remainder applies to complex functions. The fixed
   grid has an exponential observation cost, with no unrecorded
   derivative-order constant.

3. Observations in \([X,2X]\) include every row \(Nu\le X^h\),
   while all target row sets in \([X/2,X]\) are contained in it.
   The rowwise supremum and \(\ell^p\) triangle inequality
   therefore give the claimed maximal moment. The prescribed
   \(n_X\) has \(n_X\log n_X/(2\log X)\to4\), so the
   remainder is \(X^{-3+o(1)}\) before the row count and the
   allowed observation multiplier is \(X^{o(1)}\).

4. The finite Gaussian window has uniform value error
   \(O(D^{-A})\). Its row norm error is
   \(O(D^{h/p-A})\), which does not change the stated targets
   for \(b\ge0\). Only the full entire family is interpolated;
   the moving truncations are not differentiated.

5. The sixth-power replica identity keeps every literal zero
   and permits \((r,v)\ne1\). Absolute convergence justifies
   its Euler regrouping. In the moving average, the exact
   coefficient is \(J(Y/N\operatorname{rad}d)/J(Y)\).
   The dilation norm is at most \((Nd)^{-\sigma}\).
   Both the limiting Euler operator and its inverse converge
   in the required coefficient norm. The error is small on
   functions supported above a sufficiently large fixed scale,
   uniformly on finite upper truncations. Separating the
   integrable low part before taking that upper endpoint to
   infinity avoids circular use of the desired conclusion.

6. Distinct selected replicas have count of order \(D^{h/6}\)
   for fixed \(r\). Jensen leaves exactly
   \(k+5h/6+e\) in the exponent. Weighted Hölder and the
   rapid low-scale tail justify Mellin continuation for
   \[
   \Re s>\frac12+\frac{5h}{12k}+\frac{e}{2k}.
   \]
   The finite Euler corrections are nonzero at positive real
   parts, so the identity theorem gives the claimed zero
   exclusion under the moment premise. A principal \(L\)-pole
   causes a zero of its reciprocal and creates no exception.

The detailed independent reconstruction remains in the exact
second review identified in Section 1. This receipt supplies
the committed-source binding that that review intentionally
deferred.

## 3. Open arithmetic and scope boundaries

The arithmetic sampled upper bound (4.4) or (4.5) for the actual
Gaussian-weighted signed Möbius sums remains **unproved**.
The sampling and interpolation lemmas supply no estimate for
those observed arithmetic values.

Every sufficiently large dyadic scale is still required.
Having finitely many observations at each scale is not a finite
verification of the infinite assertion. The finite-truncation
theorem concerns approximation of those values, not their
arithmetic cancellation.

The full fourth moment, the full generalized \(2k\)-th moment
hierarchy, an unconditional improvement of the zero-free region,
and RH remain **open**. Approaching the conditional boundary
\(1/2\) still requires the stated arithmetic hierarchy and
character coverage. No numerical experiment, finite zero census,
or exponent diagnostic replaces those requirements.

This receipt independently reviews the Gaussian source only.
The reviewer is an author of JOINT_CONTINUATION.md; that
authorship supplies no independent review of the joint note.
Its separate reviewer and exact-source receipt must carry that
independent assessment.

No frozen source or content-review file was changed in preparing
this receipt. It binds the source commit above and makes no claim
to approve later mathematical modifications.
