# Whole-problem attempt and the exact point not completed

This pass tries to turn a good native seed into a sequence with increasingly
long exact arithmetic prefixes. The target is a full residual estimate, not
a graph spectrum. RH and that estimate remain unproved.

## Attempt 1: multiply or accelerate one residual

For a seed p with F=1-zeta p, F^m has Dirichlet support beginning atQ^m.
The prefix therefore grows exactly. More generally P_m(F) has that delay
when its first m Taylor coefficients vanish. P_m(1)=1 retains the necessary
interpolation at every possible zeta zero. This is attractive because a small
seed E(p) might suggest quickly decreasing higher powers.

The inference is false. Every fixed finite balanced p has its OWN zeros
arbitrarily close to Re s=1 at large heights. Every P_m with P_m(1)=1 sees
those zeros too. The complete output norm must have at least orderQ^(m-o(m))
in the logarithmic-growth sense of NM1, or be infinite. This rejects scalar
polynomial acceleration regardless of coefficient tuning. It is not a claim
that the original optimized native minima are large.

A non-directed exploratory script expanded truncated Dirichlet convolutions
through2^20. Some higher powers had very small partial integrals because their
onsets were moving toward the cutoff. Those are NOT norm upper bounds. For the
normalized prefix-two seed, the truncated second/third-power energies already
increased as the cutoff grew. No scout value is used by acceptance or promoted
to a complete fourth/sixth moment, a tail estimate, or an asymptotic.

## Attempt 2: prevent artificial common zeros by multiple native seeds

NM2 constructs three arbitrarily close finite seeds with no common auxiliary
zero after the pole cancellation at1. The concrete support16/24/81 bank retains
all native normalizations and has E<0.02 for EACH member, with a complete tail.
NM3 supplies an actual bounded compact signed filter from the unchanged
factorial source to each seed. Their joint real-translation-generated space
is exactly the original factorial-source space. No accidental extra inner
factor remains. This repairs the qualitative fixed-generator defect rather
than ignoring it.

The equality concerns ALL real causal translations in ordinary L2(dt).
It is not a proof of the analogous statement for a restricted integer-dilation
algebra or for finite Dirichlet feedback. It is also not proof that the common
space is all L2: the common zeta Blaschke factor is retained explicitly.

## Attempt 3: a bounded analytic inverse and cheap polynomial feedback

No bounded analytic Bezout controller exists for ANY fixed normalized finite
bank, even when there is no common zero. Simultaneous prime-phase recurrence
makes every bank entry arbitrarily small at the SAME safe point1+iT. This is
an actual-frequency calculation, not the independent-prime surrogate already
rejected in the earlier entropy work.

For multivariate feedback P_m of degree D_m and coefficient l1 mass A_m,
NM4 supplies the quantitative necessary cost

    E_m >= c_bank Q^m/(1+A_m D_m)^[4(d-1)].

Thus subexponential coefficient/degree cost cannot close this proposed loop.
A successful E_m=exp(o(m)) would need at least exponential growth of A_m D_m.
This does NOT preclude such a construction: large coefficients may cancel in
the physical output. The missing task is a complete norm estimate paying that
cancellation and every frequency, not another no-common-zero argument.

The polynomial iterates can have infinite Dirichlet support and are not
assumed to be L2. Introducing a smoothing filter changes their interpolation
values and requires a new full delay/evaluation estimate. No unannounced
filter is inserted here to manufacture finiteness.

## Exact sufficient ending, and the unproved estimate

Choose polynomial feedback on the specified triple, with total-degree delay
m, P_m(1,1,1)=1, and prove E_m=exp(o(m)). At any hypothetical off-line zero
rho, the three F_j equal1, so the exact delayed Mellin inequality gives

    E_m >= (2Re rho-1)Q^[m(2Re rho-1)]/|rho|^2.

This contradicts the requested upper bound and, by the functional equation,
proves RH. The upper bound is NOT supplied. It is not assigned to reviewers
as a routine missing step. No new bound on the alternative finite-support
affine minima is claimed.

## Relationship to the other live work

The live #834/#835 PR descriptions were read as orientation only: they pursue
actual-theta spectral/global-Laguerre signs and explicitly retain their missing
reality/Fourier-positivity steps. Their new proofs and numeric campaigns were
NOT reviewed or imported in this pass. The #803 compression remains a separate
finite-support approach, not implied by this bank's continuous-shift cyclicity.

The new manuscript is a direct continuation from #833. It incorporates and
freshly replays one seed from the previously LOCAL NJP26 normalization package.
It does not upload all eleven NJP26 files or claim their six-cutoff campaign was
rerun. The old package and its remaining work remain separately identifiable.

The useful result here is a small explicit native generating bank and its exact
source factorization, with the next controller burden stated quantitatively.
It is not an unconditional RH proof or evidence that the remaining step is easy.
