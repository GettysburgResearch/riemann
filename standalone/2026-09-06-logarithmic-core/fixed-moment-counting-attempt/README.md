# The failure-count upper bound was not proved

Status: failed direct counting attempt with proposed component proofs.
Independent mathematical review required. RH and the requested estimate remain open.

The exact target is N_-(M)=O_eps(M^(1/2+eps)) for every eps>0, for the
unchanged actual annular scalar. No nontrivial unconditional count upper bound
is supplied in this packet. The elementary eps>=1/2 case is not the missing part.

The attack takes an exact moment majorant for the threshold R_j>1/4, where
R_j=1/4-D(j), and keeps all prime-power correlations. Its retained results are:

* The exact centered Gram expansion and a uniform summable lattice correction:
  |sum R_j^2-sum T_j^2|<5.
* The full centered diagonal is asymptotic to
  [455/3072-log(2)/36] M log M, using only the ordinary PNT.
* Under RH, every fixed even moment of R has a strictly positive logarithmic
  mean. Consequently its unweighted sum is not O(M^theta) for any theta<1.
  This rules out the proposed fixed-raw-moment proof of the counting bound,
  even in the case where all the inequalities being counted are positive.

The obstruction is conditional on RH and the exact source expansion; it is
not a counterexample to RH or to the requested count bound. It does not rule
out threshold-sensitive or increasing-order moment methods. The paper states
precisely the increasing-order estimate that would suffice and does NOT prove it.

Read PROOF_ATTEMPT.md, SOURCES.json, and VALIDATION.md. Bounded exact checks
cover algebra only. They do not establish PNT, the actual zero expansion,
the conditional infinite moment limits, or the requested upper bound.

Replay:

    python -I -S -B verify.py --manifest --check result.json
    python -I -S -B -O verify.py --manifest --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

Parent research, reviews, main, formal sources, and workflows are unchanged.
No new positive range, numerical zero record, or external priority is claimed.
