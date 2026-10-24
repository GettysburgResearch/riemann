# Third pass: a full Möbius cubic moment with a power saving

24 October 2026. **Status: proposed source-dependent mathematics.**
The full structured moment below improves a cubic large-sieve term.
The inherited numerical zero-free boundary is unchanged. This directory
is additive; the two earlier frozen passes remain unchanged.

## 1. The main result

Work over the Eisenstein field with primary ideals and the pinned source's
cubic symbol, extended by zero. Write \(G(b)\) for its normalized cubic
Gauss coefficient and \(\theta=\Theta_\ell\nu\), where the angular order
\(\ell\) and finite ray character \(\nu\) are fixed. Initial excluded
primes are fixed. Let \(W\) be a nonnegative smooth radial annular weight
and \(V\) a smooth norm-annular weight. Set \(X=AB\).

Assume **ZF_beta**: the relevant finite twists of this fixed angular type
have a common zero-free half-plane \(\Re s>\beta\), for a fixed
\(1/2<\beta<1\), with a possible principal pole permitted. Then for some
\(\eta_{\rm full}>0\), every \(\epsilon>0\), and all \(A\ge B\ge2\),

\[
\boxed{
\sum_{a\equiv1\ (3)}W(a/\sqrt A)
\left|\sum_b\frac{\mu(b)\theta(b)G(b)}{\sqrt{Nb}}
          \overline{\chi_b(a)}V(Nb/B)\right|^2
\ll X^\epsilon\left[A+X^{2/3-\eta_{\rm full}}\right].
}
\]

The row sum includes nonsquarefree rows. The proof retains every Poisson
frequency, the original Möbius coefficient, common divisors and all
internally generated zero masks. It makes no arbitrary-coefficient
operator claim and no assertion for an arbitrary growing initial puncture.

The generic cubic large sieve gives \(A+X^{2/3}\) in this range.
For example, at \(A=B=T\) the new bound is
\(T+T^{4/3-2\eta_{\rm full}}\), up to the stated small losses.
The positive exponent \(\eta_{\rm full}\) is not numerically specified.

The complete proof is [FULL_MOBIUS_CUBIC_MOMENT.md](FULL_MOBIUS_CUBIC_MOMENT.md).
Its zero-free premise is explicit. The proposed all-unitary result in
PR #1012 supplies it, if that source-dependent result is adopted, for
\(\beta>B_\flat\). The present packet does not independently certify
that input or the upstream analytic theorems.

## 2. What makes the improvement possible

The exceptional ordinary cubic character estimates in the source require
a prime-convolution coefficient. The actual Möbius coefficient has an
exact alternative decomposition. With \(m=\mu\,1_{N\le\sqrt{Y_0}}\),

\[
\mu=2m-m*m*1\qquad(Nn\le Y_0),
\]

where the stars denote ideal Dirichlet convolution. This produces at
most three character polynomials; the two Möbius factors are short and
the third is a full smooth ideal sum. That is enough for the source's
functional-equation, large-value and Gram argument. The decomposition
retains small primes and all natural zeros.

[MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md](MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md)
proves this coefficient adapter.
[QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md](QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md)
gives the explicit exceptional-mean bound

\[
\sum_{p,q}|A(p,q)|^2\ll Y^{7/3-10^{-6}},
\]

in neighborhoods of radius \(10^{-9}\) of the two source exponent
configurations \((1,0)\) and \((1/3,1/3)\). The coefficient in
\(A(p,q)\) is the actual Möbius coefficient with a fixed angular/ray
twist. This exceptional estimate uses no zero-free premise.
Its numerical saving is **not** asserted for the full Gauss moment.

The full-moment assembly then uses ZF_beta to control every small
primitive-conductor frequency, including the principal ones. In the
remaining frequencies the new adapter completes the source's estimates.
For the entire short dual range, the proof also establishes

\[
|\mathcal M-\mathcal D|\ll X^\epsilon B^{2\beta+1},
\qquad H=B^2/A,
\]

in the unnormalized convention of the main note. When
\(H\le B^{2-2\beta}\), this is at most the diagonal scale \(AB\).
This includes subunit frequency ranges with their actual Schwartz decay.

## 3. New repository work taken into account

The repository was checked again before this pass was frozen. `main`
remained at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The following
branch work is relevant; none is silently treated as an integrated theorem.

| Pinned work | What was used or learned |
| --- | --- |
| [PR #1019](https://github.com/GettysburgResearch/riemann/pull/1019), head `3bcc1daaeb51c71cb2785b9744cde0d641f68f4c` | Its natural-length squarefree-label theorem bounds the projection of the actual Möbius inverse vector and saves a power. Its projection theorem explicitly leaves the orthogonal complement open. The new cubic moment has different row characters and coefficients, so there is no automatic transfer to that complement. |
| PR #1019, `PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md` at the same head | This already addresses the physical quartic numerator `k^3`. Its annular consumer retains the factor `D^(2 delta)`; its stated best bound in the binding range is `D^(17/12)`. The ordinary-numerator improvement from our second pass does not remove this cost. |
| [PR #1012](https://github.com/GettysburgResearch/riemann/pull/1012), head `64cb43c038d1828a478cb97cbc32e435e111d2d2` | Its proposed full-unitary boundary supplies the exact fixed-angular zero-free orbit needed here. A finite-order-only premise would not suffice for an angular coefficient. |
| [OpenAI mathematical source](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a), commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` | Its cubic dispersion and exceptional-character proofs are the imported analytic inputs. The new contributions are the Möbius adapter, its quantitative finite exponent argument, and the complete all-row assembly with principal frequencies retained. |

Exact file paths and content hashes are recorded in
[SOURCES.json](SOURCES.json).

## 4. The physical orientation and the remaining global gap

A proposed cubic-character shortcut was checked at the finite Fourier
level. The actual first-Poisson column is

\[
\mu(c)\gamma_2(c)\overline{\chi_{3,c}(k)}.
\]

Its sextic Gauss realization has numerator **\(k^4\)**. The proposed
square-index realization has the opposite cubic character. Whole
conjugation preserves the fourth-power requirement. The local primitive
system also retains the fourth-power branch under the stated geometric
functional equation.

[CUBIC_FOURTH_POWER_ORIENTATION.md](CUBIC_FOURTH_POWER_ORIENTATION.md)
proves this check. The resulting natural scale is `K^4/D`; the tempting
`K^2/D` recursion and its proposed `5/6` consequence are withdrawn.

The new full moment applies when the row length is at least the column
length. The physical cubic inverse in the desired range can have the
opposite ordering. The original sextic inverse additionally has different
characters and completion factors. A bound for its complete signed
nonsquare contribution, or a coefficient-preserving consumer of the new
cubic moment, remains necessary.

Accordingly the source-qualified benchmark
\(B_\flat=0.874886647039964\ldots\) from
[Liu, arXiv:2610.26835v1, Theorem 17.1](https://arxiv.org/html/2610.26835v1)
is unchanged. No new zero-free half-plane or proof of RH is claimed.

## 5. Finite validation and review boundary

[check_cubic_arithmetic.py](check_cubic_arithmetic.py) uses only the Python
standard library and exact integer arithmetic. It checks:

- the short Möbius convolution identity on a finite ideal monoid, including
  repeated prime factors, two distinct primes of the same norm, angular
  phases and independent natural-zero/puncture masks;
- Gauss norms, zero frequencies and the Hasse-Davenport coefficient
  conversion in the exact fields `Q(zeta_6,zeta_p)` for
  `p=13,37,61,73`;
- the actual cubic Fourier orientation and the fourth-power embedding,
  rejecting the square substitution in both nontrivial cubic classes.

The saved [cubic_arithmetic_report.json](cubic_arithmetic_report.json)
records **943 finite checks**. Normal and optimized isolated executions
produce the same report. These checks authenticate only their finite
arithmetic predicates. The analytic moment, asymptotic margins and
zero-free input require mathematical review.

The exact remote mathematical commit and independent review verdicts
are to be recorded in a separate review-only followup. Agent review is
not external peer review or a formal proof certificate.
