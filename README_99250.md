# T-99250 packet — scalar SHARP Harnack and exact kernel-source repair

**RH remains unproved.**

This packet is a collision-free successor to PR #642. It introduces one
conclusion-facing idea:

> factor every row through the single SHARP state, then apply the factor-67
> Harnack operator to that scalar before doing any common-parent composition.

Define

\[
\Psi(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}(4\sqrt{x/n}-3)
\]

and

\[
\mathfrak H_{67}(x)=\Psi(x)-67^{-1/2}\Psi(x/67).
\]

The packet proves:

1. PR #642's positive kernel has the exact child Radon–Nikodym map
   `1_(t<=Z) T(Z/t)/T(Y/t)`;
2. the same formula proves normalized Hall profile monotonicity and one-parent
   random-key ownership;
3. the factor-67 defect has local coefficient `(1,-2,1)` at 67;
4. a directed all-real scan proves `mathfrak H_67>0` for
   `1<=x<100,000,001`, with minimum lower bound greater than `1.2834`;
5. global nonnegativity of this one scalar implies RH directly by its Mellin
   transform and Landau.

The exact remaining line is

```text
mathfrak H_67(x) >= 0 for every x >= 100000001    OPEN / RH-BEARING
```

## Replay

```bash
cd experiments/X-99250-sharp-harnack
python3 verify.py
./replay.sh --full
```

Expected fast verdict:

```text
PASS_T99250_SHARP_KERNEL_RN_AND_H67_REDUCTION
```

## Reading order

1. `claims/lemmas/L-99250-sharp-kernel-radon-nikodym-common-parent.md`
2. `claims/lemmas/L-99251-factor67-sharp-harnack-descent-and-consumer.md`
3. `claims/lemmas/L-99252-local-square-and-100m-sharp-certificate.md`
4. `claims/theorems/T-99250-single-scalar-sharp-harnack-rh-candidate.md`
5. `standalone/2026-08-19-sharp-harnack/PROOF.md`
6. `audit/author_hostile_t99250_review.md`
