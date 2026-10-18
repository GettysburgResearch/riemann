# Independent review of the quadratic-family estimates and native frequency tail

## Verdict and scope

**Pass for the stated component deductions.** The reviewer did not author
the arithmetic proofs or checker. The review read the complete proofs,
rederived their exponent balances and analytic consumers, checked the named
primary large-sieve and subconvexity inputs, and replayed the exact finite
checker in normal and optimized Python. No blocking gap was found in the
claims listed below.

This is a mathematical review of deductions from named inputs, not a new
proof or formal verification of those external theorems. The finite checker
verifies finite identities and exponent arithmetic. It does not certify an
analytic continuation argument, an asymptotic family estimate, or a zeta
zero-free region. The manuscript remains a proposed research component.

The reviewed files are bound by SHA-256:

| File | SHA-256 |
|---|---|
| `arithmetic/PROOF.md` | `aecac636f02150fbf03e37ae1945605b5f128d7820226596da77eab83a44cc82` |
| `arithmetic/NATIVE_FREQUENCY_TAIL.md` | `5020e35082d9e4e67a6919744c5b84692c264eb2e271e0b07d443b826b72cb07` |
| `arithmetic/README.md` | `b43f124141719b1fee2eb9b7f147b4c65b9bd075a9e8b7946483aa522da84ff3` |
| `arithmetic/check_arithmetic.py` | `c8abdcd0cb7eb6cfcfa183c216aa3fd62e6faaaf48c7444f82624f9354d09373` |
| `arithmetic/check_report.json` | `7beff1b4a6fd3654ebc17b95a327ee37f6c8f8ef0c1745809123ed4a0d0aa20a` |

## 1. Actual quadratic family and the full dual sum

The family has primitive odd characters of discriminants `-8u`, with `u`
odd and squarefree in `(Q,2Q]`. The elementary character average and its
ramification probabilities are inherited from frozen PR #1001, with their
scope restated. A fixed local sign or zero condition expands into a finite
polynomial in those local characters and has positive limiting density.
Its error constants are allowed to depend on the fixed condition.

The quadratic large-sieve contract was checked in Soundararajan--Young,
JEMS 12 (2010), Theorem 2.4, which states the unconditional Heath-Brown
inequality used here. Its squarefree columns are not all integer columns.
The manuscript's conversion retains the full unique decomposition
`n=a*b^2`, with `a` squarefree and **no** extra `(a,b)=1` restriction.
For each fixed `b`, the row mask `1_(u,b)=1` is retained before positively
enlarging the row sum. Binary partial-sum decomposition and Abel summation
legitimately handle the row-dependent weights. The square-root norm summed
over `b` costs `sum 1/b`, a logarithm that is included.

The exact flat-cutoff functional equation has the correct sign, conductor
factor `(q/pi)^(1/2-s)`, dual variable `pi*n*K/q`, and gamma quotient for an
odd primitive character. The contour crosses the cutoff transform's pole
at zero, and no pole of an actual nonprincipal L-function. The dual weight
is bounded at zero and rapidly decreasing at infinity, including the
variation needed by Abel summation. Every dual dyad and the separate unit
term are included.

For `h=Re(s)-1/2>0`, splitting the dual at `Q/K` produces the claimed
`Q^epsilon K^(-h)` root norm, including the region above conductor size.
The sharp-cutoff replacement has the same bound. Squaring gives the
actual full-L tail estimate on every fixed compact subset of
`1/2<Re(s)<1`, without deleting exceptional rows. Constants are not claimed
uniform at the critical line or for growing heights. The complex-compact
supremum variant follows by a fixed submean cover; the slight enlargement
of the real-part range is paid using `K<=Q` after choosing the requested
epsilon.

## 2. Complete residual transfer and local optimization

The random series tail retains every square alias `nm=square`; the Euler
product is the same Hilbert-space-valued analytic function, first identified
in absolute convergence and then by the identity theorem. Fixed local
conditioning is paid by its positive probability.

For an arbitrary finite character polynomial, replacing both full L-values
by their initial segments costs the actual coefficient mass `B`, and
expanding the complete finite residual costs the weighted mass `D`.
The estimate compares the full expression `zLA-1`; it never divides by
`zeta(s)` or an actual L-value. The square-root comparison uses
`abs(sqrt(a)-sqrt(b))<=sqrt(abs(a-b))` correctly. The squared comparison
accounts explicitly for the squared tail error. Uniform actual full-L
second moments are obtained first from the root comparison with `A=1`,
so their later use is not circular.

The two growing-horizon balances were rederived. At real part `3/4`, they
allow exponents below `1/4` for the root-residual comparison and below
`1/6` for absolute squared-residual asymptotics. At `5/6`, the respective
thresholds are `2/5` and `3/10`. These are mollifier-length exponents, not
zero-free boundaries.

The finite-local optimizer follows from an exact variance decomposition
after writing `A=L_(<=y) N`. The tail is independent and its mean is an
explicit nonzero absolutely convergent product on `Re(s)>1/2`. All local
state functions are covered, and uniqueness is correctly restricted to
`z!=0`. Its variance tends to zero with `y`; the minimum keeps the rational
bias `abs(z*m-1)^2`.

The transfer for `y=(log Q)^nu` pays the actual Euler coefficient masses.
It does not assume that a primorial is shorter than a power of `Q`.
The strict condition `nu<1/(5/4-sigma_0)` makes both masses subpower, and
the logarithm of the support is also affordable. The actual normalized
auxiliary residual therefore tends to zero. With the common zeta factor,
the limit remains `abs(zeta(s) M_Z(s)-1)^2`; it is identically one at a
hypothetical ordinary zeta zero. No principal-member conclusion was added.

## 3. Native frequency tail and its physical consumer

The Fourier normalization was checked directly from
`f(u)=exp(u/2) R(exp(u))`. Each translated term contributes
`z_Y(d) d^(-1/2-it)`, so the exact multiplier is
`zeta(1/2+it) G_Y(1/2+it)^2/(-1/2+it)` with the stated Fourier sign.
All convolution products remain present, including those beyond the
physical output point.

The finite Dirichlet-polynomial moment bound follows from the full Gram
matrix, a Schur row estimate, and `d_j(n)^2<=d_(j*j)(n)`. The latter local
inequality follows by counting integer matrices with prescribed row and
column compositions. All losses are logarithmic and are paid.

Bourgain's primary PDF, arXiv:1408.5794v2, Theorem 5, explicitly gives
the pointwise exponent `13/84`. The indexed arXiv abstract retains an older
exponent; the reviewed deduction uses the theorem in the revised PDF.
Dyadic summation therefore gives
`H(Y,T) << (YT)^epsilon T^(-71/42)(T+Y^2)` and the cutoff `Y^(84/71)`.
The independent twelfth-moment interpolation exponents `1/2` and `1/3`
are correct. Its optional recent input is isolated and is not needed for
the stronger pointwise-based cutoff.

The passage to the strict native square step first projects the complete
Mellin input in frequency, and then applies the physical indicator. The
indicator is an L2 contraction. The proof does not interchange the two
operators or claim that the restricted low-frequency part remains
bandlimited. The reverse triangle inequality pays all mixed terms in a
root-norm comparison. The endpoint `(Y+1)^2` is excluded, and the native
crossing bound makes the smooth component have bounded squared norm.

The retained low-frequency norm is still unbounded by a subquadratic power
of the old native energy. The displayed compact-frequency estimate costs
its square. The reviewed manuscript explicitly leaves this as the missing
arithmetic step; the frequency cutoff is not interpreted as a zeta boundary.

## 4. Reproduction and primary inputs

The following runs both returned PASS and produced the same receipt as
`arithmetic/check_report.json`, byte for byte:

```bash
python arithmetic/check_arithmetic.py --report audit/arithmetic_replay.json
python -O arithmetic/check_arithmetic.py --report audit/arithmetic_optimized_replay.json
```

No Python assertion is an acceptance gate. This replay is independent of
the authoring agent, using the same checker implementation.

Primary references checked for the load-bearing imported estimates:

- K. Soundararajan and M. P. Young, *The second moment of quadratic twists
  of modular L-functions*, Theorem 2.4:
  https://ems.press/content/serial-article-files/31734
- D. R. Heath-Brown, *A mean value estimate for real character sums*:
  https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums
- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
  revised PDF, Theorem 5:
  https://arxiv.org/pdf/1408.5794

The squarefree character-average proof and native crossing identity are
inherited from the exact source commits cited in the manuscripts. Neither
their integrated status nor any global zero-free claim is changed here.
