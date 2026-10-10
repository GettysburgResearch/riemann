# Scoped independent review of the Möbius CRT translation

Status: **ACCEPTED at the stated elementary and conditional scope by the
arithmetic-wave agent**, October 10, 2026. This review certifies neither
an infinite short-row moment estimate nor a new zero-free region.

The following resident source bytes were reviewed in full:

| File | SHA-256 |
|---|---|
| `correlations/MOBIUS_CRT_TRANSLATION.md` | `bde2f3a2c15aa514fdf51a5c0956691170633aa6d79427b7dc3a7f7ff6412710` |
| `correlations/check_mobius_translation.py` | `20f9c6364d9459ac84b96b7ca9c2bc0e7b7e63093ce7bddbf1ff40b0839c5734` |
| `correlations/probe_sextic_cumulants.py` | `e3dec86cc6b07d80bb6bb61aababf460eb8ccd3738852869837b8e1b8c50a1be` |
| PR912 `MELLIN_AND_SPIKES.md` | `f3bdeb168714d838a4b13347cd353675d9644b9629041cdf7def78dc496162e3` |

The PR912 text is pinned at commit
`6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`. Its Section 5 was checked
for the exact uniform reciprocal, polynomial conductor, deleted-factor,
and Mellin-inversion hypotheses used by the conditional translator bound.
Those hypotheses are retained, rather than supplied by this review.

## Analytic contracts

For T-M1, every Eisenstein prime ideal outside the primes over 6 has
residue-field order congruent to one modulo six. Cyclicity makes its
literal sixth-residue character surjective onto the six roots of unity.
A local residue with value -1 exists and is nonzero. Ideal CRT therefore
gives a simultaneous unit t modulo the squarefree product Q. For every
squarefree supported ideal n, multiplicativity gives
chi_n(tu)=(-1)^omega(n)chi_n(u). If any local component of u is zero,
both sides are zero. The unit ideal is also covered.

The same t works for every coefficient profile. Multiplication by this
unit is a permutation of the entire residue ring, so the full joint law,
not merely the separate moments, is preserved. Arbitrary fixed coefficient
characters can be included in the coefficients. No independence assumption
or suppression of nonunit masks enters the argument.

For T-M2, substituting v=tu into a nonuniform complete residue sum moves
the weight to L_H(t^-1 v), with exactly the displayed inverse. It does
not change that weight to its mean. Thus the signed source information
remains in its correlation with the actual translated short lattice
measure; complete-residue moments alone discard that distinction.

For T-M3, a coherent t_D is a unit at every active prime, so every active
coefficient mu_K(n)chi_n(t_D) is +1. For a nonzero nonnegative fixed
smooth W and nu=1, squarefree-ideal counting outside the fixed excluded
primes therefore gives a lower bound c_W D. Under the explicitly assumed
full-family zero-free boundary B<1 and uniform PR912 Section 5 analytic
inputs, the upper bound is C_(P,epsilon)D^(B+epsilon) whenever
N(t_D)<=D^P. Choosing epsilon<(1-B)/2 makes these incompatible for large
D. This proves eventual N(t_D)>D^P for each fixed P, with its own starting
threshold. It gives neither an effective constant nor a new full-family
zero-free result. The weaker statement of zero-freeness with uncontrolled
conductor-dependent constants would not justify this step.

## Exact source and runtime audit

Both source scripts were run in normal and optimized Python, using the
prepared interpreter. All four commands exit zero. Each script's two
JSON outputs are byte-identical. The CRT checker executes 501 exact
guards, finds translator 34 and inverse 83 modulo 91, and includes local
zeros, five simultaneous profiles, moments through order sixteen, and
one nonuniform fourth-moment transport.

The prime-ideal enumeration retains both split ideals, the inert ideal
of norm p^2, and exactly the excluded primes over 6. The column recursion
enumerates each squarefree ideal once, with its literal Möbius sign. The
row-coordinate bound covers the entire norm ball. The residue Euler power
is interpreted in the same sixth-root order for split and inert fields;
the two coordinate bases are related by epsilon=1+omega.

`check_crt_cross_review.py` supplies two further controls independent of
the probe's census and complex-moment formula. Rational prime factorization
counts squarefree ideals at norm p^e with local factors 1,2,1 for split
p and e=0,1,2; for inert p the only factors are 1 at e=0,2. It yields the
complete band counts 19,37,74 at D=128,256,512. In real coordinates
X=a+b/2, Y=sqrt(3)b/2, the fourth cumulant is computed as

    E(X^2+Y^2)^2 - 3E(X^2)^2 - 2E(X^2)E(Y^2)
                     - 3E(Y^2)^2 - 4E(XY)^2,

after centering. This avoids the source's complex-square and summarize
helpers. Both normal and optimized control runs reproduce:

| D=H | Columns | Rows | Exact signed fourth cumulant |
|---|---:|---:|---|
| 128 | 19 | 462 | `348006807/35153041` |
| 256 | 37 | 930 | `6875488331/23088025` |
| 512 | 74 | 1866 | `5440157328645/9354951841` |

All three are strictly positive. T-M4 correctly rejects universal
nonpositive fourth cumulants for this sharp finite source. It draws no
asymptotic lower obstruction or smooth all-scale upper theorem from these
finite examples. No defect was found in the reviewed mathematical or
implementation scopes. `MOBIUS_CRT_REVIEW_EXECUTION.json` binds the replay
and independent-control hashes.
