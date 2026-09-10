# Native curvature and a failure-count route

PROPOSED COMPONENT THEOREMS; independent mathematical/code review required.
RH and the new arithmetic counting estimate remain unproved.

This continuation of PR #803 does not enlarge the preceding positive window
or finite verified-height range. It proves new all-scale facts about the SAME
finite prime-power scalar D(m):

1. Its distributional second derivative is explicit, with positive entry/exit
   jumps and a negative center jump for every prime power. On 2<=A<B<=2A,
   total curvature is at most log(4B^2)[32(B-A)/A+3/A^2].
2. Exact Green interpolation now permits square nodes in m, hence fourth-power
   nodes X=k^4 in the original prime scale. Eventual D(k^2)>=0 suffices for RH.
3. A negative value D(z)<=-H, 1<=H<=z, z>=16, forces a neighboring negative
   run of length sqrt(Hz/[256log(16z^2)]).
4. Therefore ONE hypothetical off-line zero of real part beta>1/2 forces
   limsup log(1+N_-(M))/log M >= beta, where N_- counts integer D(j)<0.
   A bound N_-(M)=O_epsilon(M^(1/2+epsilon)) for every epsilon>0 would prove RH.
   NO such upper bound is proved here; only N_-(M)<=M is currently supplied.
5. The exact native divisor renewal and its Mobius inverse are derived.
   The attempted absolute renewal bound is not contractive at the needed scale.

Read PROOF.md, ATTEMPT.md, SOURCES.json and VALIDATION.md. The forward pole
argument is rederived directly from the finite arithmetic scalar. The reverse
RH-to-positive-margin direction imports the pinned annular parent's theorem
at its existing proposed-review scope. Neither the length-one certificate nor
an external finite-height zero verification is used in the new forward work.

The fourth-power Green connection to #805's different odd-Mobius scalar is
credited in SOURCES.json. No transfer of its norm theorem or analytic hypotheses
is inferred from that resemblance, and no external priority is claimed.

Bounded exact checks authenticate both consumed context manuscripts and verify
finite algebra, jump/endpoint bookkeeping, native divisor identities, and a
few actual rational-logarithmic values. They are not machine proofs of the
unbounded statements or evidence for the missing counting upper bound.

Run from this directory in a checkout containing the two parent proof siblings:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

Only this new directory is proposed for the branch. Earlier files are unchanged.
