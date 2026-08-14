# Handoff — two-channel Cycle Debt and direct complete-endpoint Q4 PIG

Status: **PROPOSED PACKET / EXACT-SHA REVIEW REQUESTED**  
Cutoff UTC: `2026-08-14T17:13:53Z`  
Frozen base: `main@9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Intended branch: `agent/91701-q4-cycle-debt-control`  
RH: **unproved**


Live movement: PR #470 appeared during construction at
`a05584ac5c5227d56e9c2eb45c6530b68987cbb0`, continuing the native-root
lane. It does not overlap the claims in this packet. `main` remained frozen at
the SHA above.

## Contributions

### Route A — Cycle Debt

`L-93010` proves that the full signed Cycle-Debt LP is exactly a two-colour
positive Markov-control problem:

\[
 s=M^+(I-P^+)-M^-(I-P^-),
\]

with only the negative channel charged by the exact capacity drift.

`L-93011` gives the normalized Bellman interval

\[
 \max_eP_ef\le f(n)\le\min_e(P_ef+c_e)
\]

and the exact optimality conditions

```text
positive support -> zero dual defect;
negative support -> full-capacity dual defect.
```

The resulting tuple is a finite solver-independent certificate for the exact
Cycle-Debt optimum.

### Route B — Q4/PIG

`T-93010` defines the complete continuous-position endpoint energy

\[
 \mathscr P_\circ(N)=N^{-2}\sum_j|R_N(j)|^2
\]

and proves the exact decomposition

\[
 \mathscr P_\circ(N)
 =|M_\circ(N)|^2/N
 +N^{-3}\sum_{a<b}|R_N(a)-R_N(b)|^2.
\]

The zero-safe mean has its direct Mellin pole consumer. Therefore complete
endpoint PIG is RH-equivalent without `L-90419`'s withdrawn unconditional
Selberg input and without the disputed global QIDR recurrence. A zero with real
part \(\beta>1/2\) forces energy above every exponent below \(N^{2\beta-1}\).

## Replays

```bash
cd experiments/X-91701-cycle-debt-two-channel
python3 verify.py
sha256sum -c SHA256SUMS

cd ../X-91702-q4-completed-pig
python3 verify.py
sha256sum -c SHA256SUMS

cd ../..
sha256sum -c integration/gpt56-pro-91701-content-sha256.txt
```

Expected verdicts:

```text
PASS_X_91701_CYCLE_DEBT_TWO_CHANNEL_MARKOV_CONTROL
PASS_X_91702_Q4_COMPLETED_ENDPOINT_PIG
```

## Exact source locks

See `integration/gpt56-pro-91701-source-lock.tsv`. The principal mathematical
sources are frozen PR #272, #335, #362, #383, and #386 heads; the independent
route reviews are frozen PR #369 and #371 heads.

## Independent review requests

### Cycle reviewer

Please reconstruct:

1. both directions of the signed-flow/two-channel equivalence;
2. overlap cancellation and equality of minima;
3. normalized dual signs;
4. Bellman-envelope equivalence;
5. pointwise complementary slackness;
6. existence of the certificate from finite LP strong duality.

### Q4 reviewer

Please reconstruct:

1. actual compact source normalization;
2. cell indexing `N-j-1`;
3. mean-source identity;
4. normalization of the variance decomposition;
5. Mellin kernel and multiplier;
6. zero safety, including multiplicity as residue rather than pole order;
7. integer-to-real interpolation;
8. both directions of the RH criterion;
9. the quantitative off-line-zero exponent.

## Smallest remaining gaps

```text
Cycle Debt:
construct critical two-channel certificates with X^{o(1)} negative cost.

Q4:
prove the complete endpoint energy is polylogarithmic, equivalently close the
source-specific low-frequency / weighted-Goldbach estimate.
```

Neither remaining theorem is proved by this packet. RH remains unproved.
