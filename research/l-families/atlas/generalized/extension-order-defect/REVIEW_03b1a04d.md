# Independent review of source normalization and invariant-base generators

Reviewed freeze: `03b1a04df3427a09781cdf4d43a9326671a2e566`.
Reviewer: `/root/recent_landscape`, separate from the author.
Conclusion: **no blocker found in the stated algebraic and finite-replay scope**.

I read the complete proof, preregistration, producer and28 tests during
candidate review, then reread the final proof and replay statement and
inspected the frozen artifact/source bindings. The six reviewed files
have no diff from this freeze:

| file | Git blob |
|---|---|
| `NORMALIZATION_AND_INFINITE_BASE.md` | `156320b9961aa65e8e4270e5a3ba5d263c6f2205` |
| `NORMALIZATION_PREREGISTRATION.md` | `b9d4171b377d5de77fcdb2c88ec68db46aa7711c` |
| `NORMALIZATION_REPLAY.md` | `a6ec10da0934630f3889552c8e6853603ffcbfa6` |
| `normalization_replay.py` | `17e2a906d7f3efddedb66c8e73a9d4f0d8844531` |
| `normalization.verification.json` | `5cfb111228d67b470929bfc65b3b3084d2258172` |
| `tests/test_extension_order_normalization.py` | `6ef4c3bde28a011d78285cee4659f3c261ed4979` |

The proof-object digest is
`276d29dc00e8a530d23f0e7192e7426759227b6459e4bd51c0f2a321913a9777`.
All five owned LF-normalized hashes were independently compared with the
unchanged source files and match. The six exact predecessor bindings
include the actual C6 module and the existing Lie source artifact.

Normality, integrality and the independent faithful cyclic actions prove
that C is the integral closure of the prescribed B' in the prescribed
cubic field. The field and embedding are necessary input. This is not
uniqueness from Euler or Hilbert data and does not defeat the earlier
generization counterexample outside that category.

The chart z=a^2, s=z^3, x=zp, y=z^2q has the correct character weights
and equations `x^3=su, xy=sv, y^3=s^2w`. It identifies an actual etale
pullback of the source cover with the A2 quotient. The origin fibre has
basis1,p,q,p^2,q^2 and length5, distinct from generic rank3 and the
full homogeneous-vertex minimal quotient of dimension33. The geometric
fixed loci have codimensions3 and2; this justifies absence of a branch
divisor without asserting flatness at the codimension-two stratum or
reducedness of the fixed-point scheme.

For the locally finite infinite polynomial source, the finite-module
criterion correctly concerns only nontrivial character directions.
Arbitrary trivial variables can be separated. The exact quotient
`Pbar1=S1+Sym^2(S2), Pbar2=S2+Sym^2(S1)` follows from invariant monomial
divisors, including same-charge cubes and opposite-charge pairs. It
proves both the finiteness obstruction and the full minimal-generator
series, rather than only a linear lower bound. The normal/integral
argument still works with infinitely many variables because any one
equation has finite support; it makes no Noetherian or infinite-CM claim.

For the actual even Lie ladder, the exact series is
`1+(6t^2+2t^4)(2C(t)+C(t)^2+C(t^2))`. The convolution proof uses an
epsilon split with fixed endpoint segments; it does not manufacture
a uniform remainder from an asymptotic equivalence. The shift factor
`6/4+2/16` gives the stated leading constant13/144 on even degrees.

The producer authenticates all six source objects before helper execution
or artifact use. It independently reconstructs sixteen PBW source rows;
the older Lie producer is not executed. Literal chart, fibre, covariant
monomial and33-generator controls are separate from the compressed
cutoffs2,4,8,12,16. Complete typed canonical replay and duplicate/nonfinite
rejection preserve the exact acceptance scope. The finite tests do not
stand in for the infinite finiteness, normality or asymptotic proofs.

The coordinator reports Ruff, write/check/optimized-check and28 tests in
each mode passed, followed by the final replay-note rebind. This reviewer
performed no scientific execution. The standalone later finite-cutoff
homological corollary is not one of the six files certified by this report.
