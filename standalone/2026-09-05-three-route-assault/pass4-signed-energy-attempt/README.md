# Fourth pass: direct signed-energy attempt, not an RH completion

Status: proposed complete component proofs, independent review required.
RH: NOT PROVED. The requested end-to-end completion was not obtained.
Target branch: research/astra/20260905-three-route-assault, PR #793.
Exact base: bfb66e07f7e38306dbcb916911332a591efce917.
Publication: local packet and add-only patch only; no remote update this pass.

Read PROOF.md. The change is confined to the new pass4 directory; no earlier
proof, manifest, canonical registry or formal-library source is modified.

The attack uses the latest heat-Hankel cross-branch source budget, then works
on the literal Mobius Laguerre energy rather than enlarging a positivity
certificate ladder. The outcomes are:

1. An exact extended norm identity expresses the complete signed energy
   through derivatives of reciprocal zeta at safe real points:

       (1-r) sum |a_n|^2 r^n
        =sum [2sqrt(r)/(1-r)]^(2j) |D^(j)(s_r)/j!|^2,
       s_r=(3+r)/[2(1-r)].

   This includes the case where both sides are infinite. A finite
   meromorphic circle integral across an interior pole is not this norm.

2. A proved bounded convergence region:

       E(r)<infinity for 0<r<=317/325.

   An elementary rational certificate for 0<H<1/40 and the source budget
   for a whole hypothetical conjugate invariant pair give this region.
   No zero list is used. This is a coarse classical-source consequence,
   not a new verified-height or asymptotic zero-free record.

3. An exact leading asymptotic for the full literal diagonal:

       sum_(n=0)^N Delta_n ~ [1+201/(68pi^2)](N+1).

   The proof also supplies Abel error at most 10sqrt(1-r). The atom k=1 is
   essential to the leading constant. Ordinary squarefree counting, not
   PNT or RH, pays the arithmetic density error.

The remaining statement is still finiteness of the signed norm for EVERY
r<1. The completed diagonal does not imply it: replacing mu_67 by mu_67^2
preserves the diagonal at every degree but creates coefficient root growth
3. Routes 1 and 3 retain their all-order sign gaps; they have not been
silently declared closed or dropped.

Validation: 706 finite exact rational/Gaussian-rational controls and ten
unit/rejection tests pass normally and under -O. The independent elementary
source-H enclosure is freshly recomputed as well. No zero scan, actual
large-degree energy evaluation, Lean build, remote CI run or independent
referee acceptance is claimed. The code does not machine-prove the analytic
arguments. SOURCES_AND_REVIEW.md gives the proof and execution boundaries.

Replay from this directory:

    python verify.py
    python -O verify.py
    python verify.py --tests
    python -O verify.py --tests
    sha256sum -c SHA256SUMS

There is no dependency on the predecessor's Python implementation.
