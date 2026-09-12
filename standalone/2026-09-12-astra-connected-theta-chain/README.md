# CTC26 — an infinite connected theta-calibrated Ising chain

**Proposed component proofs; independent review required. RH is not proved.**
This packet follows #863 at `0640c9c59be0bf20c18258460a7517fb09728e82`.
It does not replace or reclassify its finite degree-fourteen result.

The construction changes scale: one countably infinite nearest-neighbour Ising
chain, all couplings `(1/2)log(3/2)>0`, and a positive square-summable observable.
For n>=32 its weights are

    a_n=1/(2n)+[7/(8log(3/5))] log(n)/n^2.

The first31 weights have a prescribed sum and two parameters. Complete
interval bounds and an intermediate-value argument choose those parameters
so that the infinite law matches the exact theta second and fourth moments.
It does NOT match the sixth moment: its standardized excess is between .005
and .05 (the retained enclosure is approximately .0221714 to .0229276).

## Proved components supplied for review

1. Every finite restriction is a connected ferromagnet. The full observable
   exists in L2 and has an entire characteristic function with only real zeros.
   An explicit O_R(1/N) bound controls the whole complex-disk cutoff error.
   A separate real-frequency estimate gives an analytic probability density.
2. Positive two-by-two transfer matrices admit a bounded-error Perron-product
   comparison with an error uniform in chain length AND positive real field.
3. The complete log-MGF has the three-term asymptotic

       (h/2)log h -[(1+log(2pi))/2]h +(7/4)log h+O(1).

   These are exactly the three corresponding theta coefficients. The ratio
   of the two MGFs is therefore bounded above and below on the real field
   axis, but this is NOT a complex ratio estimate or an identification with Xi.
4. A full infinite-tail certificate proves exact variance/fourth-moment
   matching and a nonzero sixth-moment discrepancy. No future segment is
   treated as independent of the prefix or silently removed.

Start with [PROOF.md](PROOF.md), then [INVERSE_PROGRAMME.md](INVERSE_PROGRAMME.md).
The latter names the still-open all-order identification, and explains why this
construction is not a claimed RH proof or a finite moment-order improvement.
[VALIDATION.md](VALIDATION.md) records executed checks, scopes and preliminary
failures. [SOURCES.json](SOURCES.json) identifies source and literature inputs.

## Replay

Run from this directory (standard-library Python):

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py --part 1
    python -I -S -B test_rejections.py --part 2
    python -I -S -B -O test_rejections.py --part 1
    python -I -S -B -O test_rejections.py --part 2

`--emit` is producer-only. The numerical routines are adapted from #863, not
an independent second transcendental backend. Finite execution checks the
stated enclosures; it does not machine-prove Lee--Yang or the analytic limits.
