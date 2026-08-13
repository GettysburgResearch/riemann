# PR #431 verification and canonical-regeneration repair

Date: 2026-08-13  
Review PR frozen head: `78a622e32ef36e587099bb95cb791461b75d26bf`  
Live proposal branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
RH status: **unproved**

## Review verification

The three exact objections are correct against the submitted `T-91304` route.

1. Historical `L-91350.2` drops the causal parent cutoff. At `(t,p,y)=(79,83,1)`, the positive sources `85,86,87` are counted formally but are outside `d<=py`.
2. A pure-reserve mode-dependent branch has target/score `(2r,r^2)`, while an `r`-scaled canonical child has `(2r,r)`.
3. A source restriction of mass `1/2` may retain all positive packet loss; source mass is not a scalar loss coefficient.

The reviewed noninherited-row statement also lacked a complete ledger. Later local all-row results are separate repairs.

## Exact new identity

Let `h_j^X,h_j^Y` be the two mode branch coefficients and let `s_inf^X,s_inf^Y` be survival coefficients. Put

```text
alpha_j = min(h_j^X,h_j^Y),
Theta   = sum_j alpha_j.
```

After extracting `alpha_j` times the canonical packet from every branch, sum all branch excesses together with survival. The two mode coefficients are both exactly `1-Theta`. Therefore

\[
Q_\infty Iu+\sum_j(H_j-\alpha_jI_4)Iu=(1-\Theta)Iu,
\]

and

\[
Iu=(1-\Theta)Iu+\sum_j\alpha_jIu.
\]

This is pointwise in the source measure. The aggregate remainder is a canonical physical packet, not a noncanonical hidden residue.

For the pure-reserve review control, the correct child coefficient is `r^2`; the current packet has coefficient `1-r^2`. The apparent mode mismatch is absorbed exactly into the current canonical packet.

## Repaired global architecture

1. Enter the canonical positive packet cone once through the fixed finite small-prime producer.
2. Keep the prime-tail index as part of every packet state.
3. Apply the exact aggregate regeneration identity pointwise.
4. Handle the canonical current restriction locally in the positive packet cone.
5. Pass the actual canonical child restrictions to endpoints `X/p`; their total positive mass is at most the parent mass.
6. Recurse on actual packets using the packet-envelope deficit, never a scalar copy of a native packet.
7. Sum all physical child/current packets before the finite quantizer, collar, omission and endpoint port are charged.

The resulting proposed recurrence is

\[
\Delta_X(P)\le C_{\rm fin}m(P)+\sum_j\Delta_{X/p_j}(P_j),
\qquad
m(P_{\rm current})+\sum_jm(P_j)=m(P).
\]

The packet envelope then gives `O(log X)` normalized loss and would feed the resident endpoint-score RH criterion.

## Exact boundary

```text
PR #431 exact counterexamples                  VERIFIED
historical T-91304 composition                 REJECTED
packet deficit homogeneity/subadditivity        PROVED
aggregate canonical regeneration               PROVED
prime-tail index retention                     PROVED
packet-envelope tree estimate                  PROVED ABSTRACTLY
finite positive entry/local debt               REVIEW REQUIRED
one-use affine physical assembly               REVIEW REQUIRED
endpoint-score RH consumer                      REVIEW REQUIRED
Riemann Hypothesis                             UNPROVED
```

The proposed repaired theorem is `T-91404`. It must be reviewed independently at one frozen commit before any RH claim is made.
