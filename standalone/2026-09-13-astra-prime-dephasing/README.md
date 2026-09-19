# PPD26 — remove small-prime cross terms without losing RH detection

**PROPOSED component mathematics; independent review required. No RH proof or
native subpower energy bound is obtained.** Add-only continuation of PR848 at
`99101457b32b6f10f4eda88ca998048404b860ea`.

This pass changes the source family instead of increasing Newton order or
asserting a sign from finite crossing panels. Finite Euler modifications allow
an exact average over small-prime signs. The family is enormous, but its entire
energy can be compared with the original Mobius source WITHOUT a family-size
penalty. This is a loss-controlled family-to-native interface, not a claim that
the resulting mean is already small.

## Main results

For a finite prime bank S, change only those prime signs in mu(n), writing
mu(n)chi_epsilon(n). Let E_epsilon(X) be the integrated Mertens-prefix energy
through X, with the ordinary terminal cancellation and its complete physical
norm retained. Let E_rough,S use only integers prime-to-product(S).

Exactly,

```
mean_epsilon E_epsilon(X)
  = sum_(d|product(S),d<X) E_rough,S(X/d)/d.
```

This eliminates EVERY pair having different squarefree small-prime parts.
The surviving pairs have the same small-prime part and rough cofactors.

For S contained in primes <=4(log X)^2, EVERY signature, even a data-dependent
one, satisfies at sufficiently large X

```
exp[-112 log X/log log X] E_mu(X)
 <= E_epsilon(X)
 <= exp[112 log X/log log X] E_mu(X).
```

The same comparison holds for the rough energy and the family mean. The cost
is subpower, not 2^|S|. Consequently a subpower mean, rough energy, optimal
signature, or the explicitly constructed greedy signature on ANY unbounded
sequence would imply RH. That upper bound is OPEN.

A matching generic-norm theorem identifies a real threshold. Deleting all
primes <=T^a on the actual causal interval (0,T) has operator norm exponent
max(0,1/2-1/a). Thus exponent two is the largest polylogarithmic bank giving
no-power-loss UNIVERSAL norm control. This is not a source-specific impossibility
for larger banks and does not place any zeta zeros.

## Constructive signature selection

A deterministic conditional-expectation algorithm fixes one prime sign at a
time. Each step pairs the entire remaining-label source vectors and subtracts
exactly twice the absolute value of their aggregate inner product:

```
E_greedy = mean energy - 2 sum_j |b_j|.
```

It uses O(|S|X) arithmetic group updates rather than enumerating 2^|S| members.
It retains multiplicative signs, every coefficient and all time cells. It does
not guarantee improvement over the original signature, let alone a subpower
output. At X=16 the tested signing improves native energy; at X=256 it does not.

## A native warning, not a hidden sign claim

In the first rough range u<=y^2, the only surviving squarefree numbers other
than 1 are primes. Its energy is of order y^2/log^2 y. At y=(log X)^2 this forces
the dephased off-diagonal to be EVENTUALLY POSITIVE, although its known initial
cost is only polylogarithmic. This is a different covariance from the old
Newton crossing C_Y; it does not refute the old target.

After paying that explicit prime-only range, the remaining target is the
integrated square of the actual signed rough sum from y^2 to X. Its exact
least-prime recursion is included. No cancellation bound for that tail is
established by this packet.

## Proof and review

Read PROOF.md Sections 2-3 (exact dephasing and causal inverse), Section 4
(sharp generic horizon cost), Section 5 (actual selector), then Sections 6-7
(RH implication and the forced prime-only cost). Classical tools and antecedents
are credited. SOURCE_LOCK.json records latest-branch reconnaissance separately
from mathematical reading; no later research is silently promoted.

The tests cover 30 complete sign ensembles/372 member occurrences, seven larger
collapsed ensembles and 196 exact signing stages. The larger ensembles have
38,046,272 member occurrences; these were NOT enumerated. Both implementations
reconstruct the same compact certificate from full exact rows. See VALIDATION.md.

From this directory, Python 3.10+ and the standard library suffice:

```
python -S -B produce.py --check result.json
python -S -B verify.py result.json --self-test
python -S -O -B produce.py --check result.json
python -S -O -B verify.py result.json --self-test
```

Both programs have the SAME author. Their different reconstructions and
normal/optimized agreement are not independent mathematical acceptance.
No existing source file, canonical status, main, settings or workflow changes.
