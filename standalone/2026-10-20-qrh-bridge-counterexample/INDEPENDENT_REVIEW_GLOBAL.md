# Independent exact-head review of the QRH bridge counterexample

20 October 2026. This review binds commit
`8101ee2e304e4e001e42ab4c1718c77bff814e9f` and these files:

| File | SHA256 |
|---|---|
| README.md | `7b11e946eb0020884af4e062dd7592976c977038cc65413850326422bdd072d9` |
| verify_counterexample.py | `f0ebe8c9a47a23506656e271e71c9ac92b06cfebf5940aa240d53c488ca4df2b` |

The reviewer independently checked the source, arithmetic and proof,
and did not discover or author the counterexample.

## Source and actual use

I opened the primary
[arXiv:2210.03121v9 source](https://arxiv.org/html/2210.03121v9)
directly. Equation (3) defines the functions used in Lemma 1.
Dividing that lemma's first inequality by its positive exponential
factor gives exactly the inequality tested in the note.

Lemma 5 specifies `U>=exp(10/z0)` and `J=2 floor(z0 log U+2)`.
The final proof uses the same prescription and invokes the first
inequality of Lemma 1 in the first step of equation (45). Thus the
failed bound is used in the final contradiction, not merely stated
as an unused auxiliary result.

The finite example `z0 log U=11,J=26` satisfies that displayed
prescription and lower bound. The infinite family supplies arbitrarily
large parameters, so the issue cannot be removed merely by increasing
the fixed large-`V` or height thresholds elsewhere in the proof.
The finite example alone is not claimed to meet every other auxiliary
threshold for every choice of the paper's remaining parameters.

## Independent arithmetic and infinite-family check

Using a separate exact `Fraction` calculation from the primitive
factorial sum, I obtained

`3791459973096443589997/9495690262216704000000 > 0`

for the asserted left-minus-right difference after removing the
positive exponential factor. This is the opposite sign to the
lemma's requirement.

I also independently checked the integral-remainder argument. For
even `J=2n+4`, the remainder of the degree-`J-1` Taylor polynomial
of `exp(-n)` is positive and equals

`n a_n integral_0^1 exp(-nt)(1-t)^(J-1) dt`,

where `a_n=n^(J-1)/(J-1)!`. Bounding the integrand by
`exp(-(n+J-1)t)` and enlarging the integral to the positive half-line
gives a remainder strictly below `a_n/3`. The tested difference is
therefore strictly greater than `-1+a_n/6`.

The exact initial inequality `a_11>6` checks. The displayed formula
for `a_(n+1)/a_n` is exact. The first three binomial terms are
`5+8/n+3/n^2`, and multiplying them by `(n+1)^2` and subtracting
`(2n+5)(2n+4)` gives exactly `n^2+4+14/n+3/n^2>0`.
Thus `a_n` strictly increases for positive integer `n`; the claimed
failure for every integer `n>=11` follows. This is a readable proof
of the infinite family, not an extrapolation from a numerical list.

## Isolated replay and scope

I created and extracted a fresh `git archive` of the reviewed directory
at the exact commit. Both `python -I -S -B` and
`python -I -S -B -O` passed the checker. Their stdout was byte-identical,
their stderr empty, and all archived files remained byte-identical
after replay. The checker contains no Python `assert` acceptance
statements. Its finite rational examples and primitive-value checks
are distinct from the infinite integral/binomial proof above.

No defect was found in this counterexample or its stated scope.
It invalidates the cited proof step as written. It does not disprove
RH, disprove the abstract QRH-to-RH implication, or exclude a different
proof. It does not certify the rest of the external paper. This is
agent review, not a claim of human review or global mathematical
certification. The earlier boundary-iteration packet is unaffected.
