# Independent review: canonical Koszul analytic parent

Reviewed commit: `4c04db224fedde5d589f05f7183e004a67441a9c`.
Reviewer: independent `recent_landscape` agent, 2026-08-31.
Scope: the seven-file `research/l-families/atlas/generalized/koszul-analytic-parent/`
packet at that commit. No later general-rank or regularization sequel is covered.

Conclusion: no blocking mathematical or replay defect was found in the stated
rank-(2,3), complex-algebra, unitary-input scope. This is a review of the proof
and bounded controls, not a claim that computation proves the infinite theorems
or that the construction has external mathematical priority.

## Evidence and execution boundary

I independently read the complete proof, primitive source contract, producer,
and 23 tests, then read the proof from the exact Git object. The reviewed producer
and test files had no working-tree difference from this freeze. The fixture binds
the proof by normalized SHA-256
`db2ca0196edab3f3c7ef52af3f6c30e61023f3a0080c1285d7fdb6c8844a915c`.

The root agent reports successful Ruff, producer write/check, optimized check,
23 ordinary tests, and 23 optimized tests, followed by the final README binding
regeneration and check. I did not independently execute those jobs: computation
was intentionally serialized by the root because of the shared machine's memory
budget. My independent contribution was source reading, mathematical derivation,
adversarial code inspection, and primary-reference verification.

## Mathematical audit

The algebra is fixed before its scalar character. The two-row contingency-table
exchange argument gives the three-minor presentation of
`R = direct_sum Sym^r(V) tensor Sym^r(W)`. The coordinate-space convention
`P(V*) x P(W*) -> P((V tensor W)*)` is correct in the frozen text.

The quadratic dual relations are the orthogonal complement of the multiplication
kernel in the ordered tensor pairing. Since the kernel contains the alternating
tensors, its orthogonal complement consists of symmetric tensors and therefore
defines odd-generator Lie-superalgebra relations. The construction `B=U(L)` and
the source modules `M_n=L_n*` are compatible. The latter dual is necessary:
`M_1=V tensor W`, rather than its contragredient.

Taking the equivariant Euler characteristic of the Koszul resolution, followed
by super PBW, gives the stated signed determinant product. In particular even
degrees occur in the numerator. The resulting virtual class
`W_n=(-1)^(n+1)[M_n]` agrees with the preceding finite-parent obstruction; an
actual positive module is not silently substituted for a negative virtual grade.

The logarithmic coefficient calculation and Möbius inversion are correct.
For n>1 the constant-four terms cancel and the divisor-one term contributes
`2^n` to `n epsilon_n`. The bound for the remaining proper divisors proves
`epsilon_n ~ 2^n/n`; finite checks are not used to infer the asymptotic.

For unitary inputs the block singular values are exactly `|t|^n`, with
multiplicity `epsilon_n`. This proves the compactness statements and the sharp
Schatten condition `|t|<2^(-1/p)`. At equality the tail is harmonic, so exclusion
of every boundary point is justified. The ordinary Fredholm quotient exists and
is nonzero on the strict trace-class disk. Equality with the scalar series there
follows from the formal coefficient identity and analytic convergence.

The finite-grade logarithmic tail estimate follows from
`epsilon_n <= 3*2^n`. The rational real enclosures are valid because every finite
factor is positive when `|t|<1/2`; the exponential inequalities used are correct.

The Hilbert--Burch control is independent of the infinite parent: the displayed
row syzygies compose to zero, have a nonzero two-by-two minor, and are injective
over the polynomial domain. The already established quotient and Hilbert series
then force the remaining middle homology to vanish. This establishes the
all-endomorphism rational numerator, not merely a generic diagonal identity.

The unitary zero-disk argument is also correct. Equality at radius 1/2 forces
both trace bounds to be sharp, hence both unitary inputs scalar. Substitution
then gives the unique simple boundary zero `t=-1/(2ab)`. The proof correctly
does not call that a zero of a trace-class determinant at its excluded boundary.

## Replay audit

The producer reconstructs all ordered quadratic fibres and the two-sided ideal
through tensor degree three. Sparse exact elimination, odd/odd brackets, and
odd/even brackets recover the low-degree source Lie spaces. The displayed
positive torus weights belong to the dual modules M, as the proof requires.

The equivariant checks compare those source weights against an independent
symmetric-power/Hilbert--Burch calculation. Repeated inputs are allowed, and the
held-out rational unitary input and wrong-dual control are meaningful. The
even-sign counterexample detects the first negative virtual relation. The
finite Euler and rational enclosure checks have appropriately bounded scope.

The primitive JSON contract is checked before payload construction. Canonical
JSON comparison rejects Boolean/integer type confusion. The precursor is bound
by commit, blob, normalized content hash, and working bytes; owned proof/code
hashes are included. The tests cover invalid source ranks, numeric types, caps,
nonunitarity, trace-class boundary inclusion, coarse enclosure refusal, and a
forged fixture. No proof-critical check depends on Python `assert`.

## Primary imports checked independently

- Bjorner--Welker, [Segre and Rees products of posets](https://arxiv.org/abs/math/0312516),
  Corollary 3 and Section 4: the polynomial Segre product is Koszul.
- Galvez--Gorbounov--Shaikh--Tonks,
  [The Berkovits Complex and Semi-free Extensions of Koszul Algebras](https://www.numdam.org/item/10.5802/afst.1497.pdf),
  Definition 2.1, Theorem 2.3, and Section 2.2: the quadratic-dual convention,
  exact Koszul complex, and odd-generator enveloping construction.
- Lofwall, [Hilbert series, Poincare series and homotopy Lie algebras](https://arxiv.org/abs/2103.07735),
  Sections 2.2--2.3, especially formula (2.1): the enveloping quotient and
  PBW's symmetric-even/exterior-odd character product.

These are classical algebraic inputs. No analytic continuation result, prime
family, conductor, gamma factor, global functional equation, or arithmetic RH
consequence is imported or established by this packet. The frozen proof states
those limits explicitly.
