# Independent review of conductor uniformity and signed stripping

Date: 2026-10-20. Reviewer: Type-I subagent, independently of the author.

Reviewed file: ../uniform/UNIFORM_INVERSE_AND_STRIPPING.md.
Initial reviewed SHA256:
636c5c83cbee19290d506c66e5812e08cfc23da394a46f934f8850cb050a7c16.

**Verdict:** both propositions follow from their stated common zero-free
premise and ordinary uniform Hecke functional equations. One local
wording repair in the polynomial growth input was requested and applied.
The repaired file was reread and has SHA256
fcee7547018c62c5a54c273501b7f2032a93b3633b5b04b3cdce90fdc1015c12.
No outstanding issue was found. No zero-free premise is proved by this
review.

## Applied local repair

The phrase “on each fixed bounded real strip \(I\)” in (5) is too broad.
For a pure norm character the function (6) has an artificial pole at
\(-1+i\tau\), owing to its denominator. Thus (5) is false on strips
containing \(-1\). The repaired version restricts it to compact real
intervals \(I\subset(-1,\infty)\).
All disks in the proof lie strictly to the right of \(\beta\), so this
repair changes neither proposition nor any exponent.

## Reciprocal estimate

The pole removal in (6) is otherwise correct: it is holomorphic and
nonzero on \(\Re s>\beta\), and at \(1+i\tau\) its value is the nonzero
residue divided by 2. On \(\Re s\ge3/2\), the logarithm of its rational
factor is bounded uniformly in the translated height; the Euler
logarithm has the same property.

The functional-equation gamma ratios have equal exponential decay
factors and polynomial size in the stated analytic conductor, uniformly
in nonnegative angular shifts. Only a polynomial upper bound is used.
On the disks centered at \(2+it\), all shifted local parameters differ
by bounded amounts, so their conductors are uniformly comparable.
Borel--Caratheodory controls the full logarithm on radius \(R\), and
three circles between \(1/2\) and \(R\) gives the exponent
\(\log(2r)/\log(2R)<1\). This applies throughout the smaller disk, not
just its leftmost point. Exponentiation gives every positive conductor
power, and the factor \((s-1-i\tau)/(s+1-i\tau)\) has modulus at most one
for positive real part. Cauchy's formula at half the zero-free gap
therefore gives (3), including derivatives.

This is a uniform consequence of the *common location* of the zero-free
boundary. It does not require uniform constants in the argument that
established that location.

## Sharp cutoff and omitted Euler factors

The coefficient bound \(|a_\chi(m)|\le d_n(m)\) is valid: at each rational
prime, the ideal Euler factor has at most \(n\) prime-ideal factors,
with residue degrees at least one. The half-integer Perron point
preserves the original integer cutoff and avoids a near-integer error.
With \(T=x^2\), the usual truncated Perron error is smaller than the
stated \(O(x^\eta)\), uniformly in \(\chi\).

On the shifted line, the conductor inequality contributes at most
\((1+|t|)^{\epsilon/8}\). Integrating to \(x^2\) costs
\(x^{\epsilon/4}\), which gives exactly the displayed
\(x^{\beta+3\epsilon/4}\) before absorbing logarithms. Horizontal
segments have the additional \(T^{-1}\) and are smaller. There are no
residues: \(1/L\) vanishes rather than having a pole at a translated
principal pole.

Deleting primes multiplies the reciprocal by
\(\prod_{\mathfrak p\in S}(1-\chi(\mathfrak p)N\mathfrak p^{-s})^{-1}\).
At any fixed positive real-part gap its absolute value is bounded by
an arbitrary positive power of \(N\prod_{\mathfrak p\in S}\mathfrak p\),
with a fixed constant. The sharp-cutoff argument remains valid after
extending the coefficients by zero at those primes.

## Signed dilation

Differentiating \(t^{3-6c}f(Z/t^6)\) gives (13) exactly. The Stieltjes
formula includes the norm-one atom, since \(A(t)\) is zero below 1.
The large-\(t\) boundary vanishes under the stated small-argument
assumption. The two pieces have powers
\[
 Z^{b-c}\int_1^{Z^{1/6}}t^{\beta+2-6b+\eta}\,dt,
 \qquad
 Z^L\int_{Z^{1/6}}^\infty t^{\beta+2-6c-6L+\eta}\,dt.
\]
These give respectively the maximum exponent in (12) and
\((3+\beta)/6-c+\eta/6\). The threshold \((3+\beta)/6\) is consequently
correct. Above it, choose the Möbius exponent smaller than both the
desired conductor exponent and \(6b-3-\beta\); then the exponent
\(b-c\) is preserved without a \(Z^\epsilon\) loss.

The differentiability and derivative estimate on the actual Mellin
profile are essential hypotheses. The note keeps them explicit and
does not infer a new target zero-free boundary from the stripping
operator alone.
