# Independent negative literal-profile signed witness review

Status: ACCEPTED at the fixed finite source scope of NP1–NP3. The stated
negative full critical remainder and negative leading face are realized
by a nonnegative smooth literal norm profile. No negative full moment,
asymptotic saving, or RH result is inferred.

Reviewer: `/root/final_height_review/collision_review`, 2026-10-10.
What was actually run: proof/checker/receipt reads and SHA-256 binding.
No checker execution, new native integration or independent primitive
replay by this reviewer. Earlier review files remain unchanged.

Frozen continuation `literature/` heads:

* `NEGATIVE_PROFILE_SIGNED_WITNESS.md`:
  `9c5c7b2dac0b2fe3a41f03e5f08cd1a66f433bf198164ba13060c04504ce7663`.
* `check_negative_profile_signed.py`:
  `083b6ab601216364dd2068378d33dadae7e10a066db01ef31a638e83b3b1dd52`.
* `negative-profile-signed-certificate.json`:
  `eb3e1e356b44dcd4eb66c2f6dc429b0775fd6d031d641d8082cd8e1b85e28cd3`.

The imported full-source proof is
`1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca`,
its checker is
`ace0ec9a10deef974d3cae842590bc46c2d048e65dfa5b14b659cbc7c380dc50`,
and its independent review is
`5084650971b3af4d5dbb30ed169ecc5f30a4ce463f064edb6bcca3d5ce13d008`.
Both imported full native receipt modes have SHA-256
`46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93`.
The leading proof and its imported receipt are respectively
`480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120`
and `fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8`.
Their source and perturbation interfaces were physically read for the
preceding `SIGNED_SECTOR_KERNEL_INERTIA_REVIEW.md` in this directory.

At D=30, two disjoint nonnegative compact smooth bumps at 7/30 and
19/30 can equal one at those samples and vanish at all other
integer-norm samples. Thus only the two actual primes over each of 7
and 19 survive, with trivial nu and column Möbius coefficients -1.
All four-column tuple weights are +1. This is a fixed literal norm
profile, not an independent choice of weights on ordered-pair space.

I independently checked the combinatorial census. Among the 4^4=256
ordered tuples, only multiplicity types 2+1+1 and 1+1+1+1 are critical.
In type 2+1+1 the two singleton norms have product at least 49>H=40.
In type 3+1 the singleton norm is at most 19 and g2=1, so the tuple
is not critical; types 2+2 and 4 have no singleton. Therefore there are
`4*binom(3,2)*12+24=168` critical tuples and 24 leading tuples.

The complete character/mask grouping has six four-distinct groups,
24 same-side-double groups and 24 balanced-double mask groups. Their
multiplicities are respectively 4, 2 and 4, giving 54 groups and
24+48+96=168 tuples. The literal unit charges are 1 for norm 7 and
3 for norm 19. Four of the six leading groups are neutral. None of
the same-side-double groups is neutral. Eight balanced-double groups
are neutral because their two singleton primes have equal norm charge.
Thus exactly 12 groups and 48 tuples survive the radial unit projector.
This preserves every principal mask and distinguishes equal norms
from equal prime ideals.

A record in the imported full receipt stores the trace of one residual
character/mask group before multiplication by its old tuple count.
Changing the norm profile changes only the integer multiplicities;
the trace retains the same H, radial test, Poisson normalization and
nonunit mask. Every new group is a subset of the old tuple census.
The checker explicitly rebuilds all old groups, validates their original
record multiplicities and the exact neutral/killed partition, and then
applies the newly enumerated counts. Skipping absent records is safe
because precisely the nonneutral groups are absent and their complete
radial traces vanish exactly.

The printed complex directed balls are parsed into exact rational
midpoint/radius intervals, multiplied by nonnegative integer counts
and summed. No floating-point approximation enters acceptance. The
new imaginary intervals contain zero. The recorded real intervals
enclose full critical form approximately -473.9436589264844 and
leading form approximately -3.05128649834139. These are imported
directed trace aggregations, not fresh primitive integrations.

The original full Schwartz budget is a tuplewise absolute triangle
bound, not merely a bound on cancellation in its total signed form.
Removing tuples with all retained weights one can therefore only
decrease that bound. The same holds for the sum of the leading
conductor budgets. Using the inherited full bound
`72126747/206640625<.35` and leading bound below .001 gives the
strict genuine Schwartz conclusions

    full critical R2 < -473.5,       leading face < -3.

The coefficient profile, the compact-Fourier test and its genuine
Schwartz companion remain fixed in this finite example. The negative
signs show that even literal nonnegative factorable source norm
profiles do not transfer full-moment positivity to these selected
sectors. They do not imply a negative fourth moment or a violation
of a uniform absolute or upper moment estimate.

The auxiliary control reconstructs the four actual prime fields and
all 150 nonzero spatial-disk rows with norm at most 40. Its forms
are full critical -504, leading +24, and full fourth moment 2916.
These belong to that different compact spatial cutoff and are not
substituted for the Fourier-compact or Schwartz forms. No execution
of this control is claimed here. The checker and certificate clearly
separate imported complete traces, derived interval aggregation,
auxiliary disk arithmetic and the unproved asymptotic estimates.
