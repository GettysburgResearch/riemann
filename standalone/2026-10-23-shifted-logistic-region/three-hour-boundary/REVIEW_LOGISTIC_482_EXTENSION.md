# Review of the separate R=4.82 extension

2026-10-21. Boundary_attack independently reviewed the new real-axis
archimedean bound, scalar implementations and global composition.
I authored the two-prime lemma; its independence is supplied instead
by the separate type_i_gain and global_route reviews. This receipt
does not present self-review as independent review.

Exact reviewed SHA256 values:

- Global extension wrapper:
  `ec4805cc633a03e9f489dd2def61efd5ef95519357c804df7bd1536d29bdb175`.
- `LOGISTIC_NEGATIVE_ARCHIMEDEAN.md`:
  `88d8dba1316e61aa3cd67e2bb81a2c04d1ac114985593ecde9082aeae766182f`.
- Directed extension code:
  `662d90cd10e659a11a419df845f7fa9c5ff7e0803095cdf009c2579124d80e6c`.
- Directed JSON:
  `aee690cd4b54e7be1929bdd30385a9e3894cac7fb7f4f4ac42ef59bb9c495da9`.
- Fraction extension code:
  `b2c09c2b4c9af34a2e460bb4bbec6360044d798892ad3471cd0e18c5c40db425`.
- Fraction JSON:
  `fb6f0752051047df05c42ec6ebedc0ee36c11f3e1a92fcc46c0916baa6ff92cf`.

The E_f inequality has the correct sign and integration order. In
particular the negative integrand is first replaced by the smaller
positive tanh integral with exponent 3, and only then is tanh bounded
below by its cubic polynomial. The latter polynomial may be negative
at large u; no false pointwise comparison of exponential weights is
made there. Both geometric moment sums and the positive Taylor error
have the stated constants. This proves E_f(sigma)<=-.31eta uniformly.

The prime lower bound and the negative E_f bound are distinct terms
and both add favorably to the sufficient master margin. Their sum is
exactly 1.4547eta-2775eta^3. The extension keeps the original full
1e-7 error budget, which is conservative after removing the old tiny
positive E_f allowance.

The enlarged parameter rectangle still has eta<.0075, sigma>.99,
alpha>.98, A<.21, l>=28. The baseline's direct Lehman tail and gamma,
pole and high-frequency E bounds remain valid at l=82. The finite
minimum-zero proof requires no new initial zero-free constant.

`replay_logistic_extension_review.py` independently recomputed all
44 directed and 70 Fraction accepted boxes without changing their
JSONs. It verified exact producer hashes, containment, nonoverlapping
interiors and total area 2700/241. All lower bounds were positive.
Thus the two finite scalar obligations pass for the entire closed
[0,50/241] x [28,82] rectangle.

No unresolved defect was found in this composition. The frozen
wrapper still describes the independent Fraction replay as an
obligation; the replay above supplies it, rather than altering that
wrapper. Imported finite RH, Littlewood and explicit-formula/zero-count
inputs retain the scope described in REVIEW_LOGISTIC_BASELINE.md.
The proposed conclusion is only the classical logarithmic R=4.82
region; neither B_flat nor RH is asserted to improve.
