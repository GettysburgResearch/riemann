# Native moments: Liouville transfer and finite-ray rigidity

**Status: proposed component mathematics; full generalized moments and RH
remain open.** This is a focused continuation of PR #933, not another claim
of an improved zero-free exponent. No independent mathematical review has
been performed in this session.

Read [MATHEMATICS.md](MATHEMATICS.md). The two directions are complementary:
change higher prime-power coefficients in a controlled way, but retain the
very rigid signed data at the primes.

## What is proved in the note

1. **Reversible transfer at the same moment order and same physical height.**
   The original Mobius polynomial and the completely multiplicative
   Liouville polynomial are related by exact square-ideal convolutions.
   Their scale-maximal L^(2k) envelopes at weight X^(-1/2) differ by at most
   C log(2+D) in either direction. At weight X^(-1/2-delta), the cost is at
   most zeta_K(1+2delta), independently of D. Every nonunit zero and original
   exclusion is retained; no new gcd exclusion appears. The classical
   square-divisor identity itself is expressly credited.

2. **The complete tensor becomes one structured polynomial.**
   A product of k Liouville sums regroups exactly into the coefficients
   lambda_K(n) nu(n) d_{W,X}(n), where d_{W,X} is the actual ordered divisor
   profile. No pairwise coprimality is needed. The full moment is its physical
   row second moment. A prime-power rooting identity retains the whole
   composite companion without introducing the prime-dependent exclusion
   in the earlier Mobius rooting.

3. **A finite-ray coefficient rigidity theorem.**
   For a fixed finite ray quotient G and |a(g)|<=1, suppose the squarefree
   coefficients with prime value a(g(p)) satisfy diagonal native moments
   for all twists in the dual of G, at one fixed order and 0<h<6k/5.
   Then a is identically zero or exactly -eta for one character eta of G.
   An illegal Fourier coefficient forces a twist's moment to have upper
   limiting power at least 2k+h/6. This extends #933's scalar deformation
   mechanism using finite Fourier integrality and Parseval. It is a
   necessary classification, NOT a proof of the surviving native case.

## What did not close

The structured second moment of lambda_K(n) d_{k,W,X}(n), at length X^k and
near-linear physical row height, is still unbounded at the target scale.
The proposed transfer requires all smaller column scales at the SAME row
height; data only on H=X^h do not suffice automatically. Generic large
sieve norms forget the exact coefficient structure and do not solve this.

**No new fourth-moment power saving, sixth-moment power saving, 17/24 bound,
cofinal moment hierarchy, or RH proof is claimed.** The payoff is an exact,
prime-preserving simplification of the full target and a rigorous
classification of a class of inadmissible coefficient changes.

## Validation actually performed

Run with Python 3 and no third-party packages:

```sh
python verify.py > replay.json
python -O verify.py > replay.optimized.json
cmp replay.json results.json
cmp replay.optimized.json results.json
```

Both runs in the authoring environment passed and produced byte-identical
reports. The checker covers 36,208 forward/inverse coefficient pairs, with
31 actual Eisenstein element rows and four masks on a four-prime semigroup
(norms 7,7,13,25). It includes conjugate ideals of equal norm, a split and an
inert rational prime, repeated powers, units, and literal zeros. Twelve
finite tensor comparisons and exhaustive finite Fourier classifications on
C2, C3, C6 are also checked. Three deliberately false substitutions are
rejected: adding coprimality, replacing a nonunit sixth power by one, and
unsigned inversion.

The Fourier enumeration is on a finite alphabet {0} union mu_6; it is NOT
an enumeration of all Hecke characters. The prime semigroup is not all
Eisenstein ideals. The all-parameter theorems rest on the written proofs,
not on these finite checks. Both proof and code have the same author.

No remote CI, full-repository validator, proof assistant, external peer
review, or independent reconstruction of the standard Hecke theorems was
run. Direct container git access was unavailable; publication uses the
connected GitHub API. Only the new standalone packet is to be added, with
PR #933's exact head as parent; earlier work and integrated status are not
changed. MANIFEST.json binds the local files other than itself.

## Source and scope record

Base: PR #933, `8685591132bc6f283f670d252121c1629df3a208`.
Its PRIME_DEGREE_COHERENCE.md was read, including the scalar singularity,
sixth-power copying, and prime-rooting arguments. These mechanisms are
credited rather than relabeled as discoveries here. PR #916's same-height
warning and PR #356's historical Liouville use were read at description
level. Recent #930/#932/#934 descriptions supplied a scope cross-check,
not analytic inputs. See the note for the precise reading boundaries.

The finite-ray theorem uses the classical prime ideal theorem and Hecke
facts at s=1; the square-convolution and tensor results are elementary.
No imported quasi-Riemann/theta theorem or October 2026 large sieve is
needed. The classical Liouville identity is documented at
https://dlmf.nist.gov/27.6 . No global novelty claim is made.
