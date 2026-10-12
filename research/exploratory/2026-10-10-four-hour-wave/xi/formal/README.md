# Compiled arithmetic adapters for the enlarged kappa interval

Status: COMPILED REAL-ARITHMETIC ADAPTER; analytic binding remains separate.
Scope: real logarithmic lengths in the plain fourth-moment reflection argument.
What was actually run: the genuine Lean 4.33.0-rc2 compiler produced `.olean`
and `.ilean` artifacts; all 15 candidate theorems were checked, with warnings
treated as errors and their complete axiom lists printed and audited.
Smallest remaining gap: proving and binding the underlying analytic reflection,
masking, coefficient, fourth-moment and transport interfaces on the enlarged
parameter interval. These arithmetic adapters do not discharge those inputs.

## Source and normalization

The September-30 OpenAI manuscript was read at the frozen source hash
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
Its comparison stage around `old-eq:3.11` and
`eq:comparison-uncentered-margin` gives the source inequalities below.
The same source is credited by PR #910 at
`670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`.
The current wave's written adapter is
`../../literature/KAPPA_EXTENSION_CONDITIONAL.md`, Section 2.2.
Its mathematical owner confirmed the normalized variables before formalization.

Here \(\kappa\) is the plain-moment parameter, \(M\) is the logarithmic
row width including its declared moving twist-radical contribution,
\(z\) is the logarithmic length of the live prime slots, and
\(A=n_1+n_2+z\) is the total plain-and-slot length. All lengths use the
same \(\log_Z\) convention. \(A_{\rm comp}\) is the reflected comparison's
total length, retaining those same live slots. Its capacity is

\[
A_{\rm comp}+(6\kappa-1)z
 =n_{1,\rm comp}+n_{2,\rm comp}+6\kappa z.
\]

The support/reflection error is \(\xi\). The source's analytic kappa
interval also has \(\kappa\le1\). The compiled comparison implications
need its lower bound only; `coefficient_range` records both endpoints when
the affine-ledger upper coefficient five is needed.

## Exact compiled implications

[LowKappaCapacity.lean](LowKappaCapacity.lean) explicitly assumes

\[
z\ge0,\quad\kappa\ge13/18,\quad
A\ge5M/6,\quad A+(6\kappa-1)z\le M,
\]

and, for the reflected bounds,

\[
A_{\rm comp}\le3M/2-A+2z+\xi.
\]

It proves

\[
z\le M/20,\qquad A_{\rm comp}\le23M/30+\xi,\qquad
A_{\rm comp}+(6\kappa-1)z\le14M/15+\xi.
\]

The zero-error corollary sets \(\xi=0\), giving exactly the requested
three upper bounds. Strict \(A>5M/6\) gives \(z<M/20\).
When \(\xi\le M/30\), the two actual admissibility boundaries retain
margin \(M/30\):

\[
A_{\rm comp}+M/30\le5M/6,\qquad
A_{\rm comp}+(6\kappa-1)z+M/30\le M.
\]

Positive \(M\) gives strict admissibility. The separate terminal adapter
uses \(A\ge z\) in place of the high-length condition and proves
\(z\le3M/13\) and \(\kappa z\le M/6\).

The clipped deleted-column theorem explicitly assumes

\[
\begin{gathered}
M\ge0,\quad \text{short}\le M/4,\quad0\le z\le\ell\le M/20,\\
\kappa\ge13/18,\quad(6\kappa-1)\ell\le M/6,\quad\xi\ge0,\\
\text{short}+\max(0,\text{along})+z>5M/6,\\
\text{reflected}\le\max(0,M-\text{along}+\xi).
\end{gathered}
\]

It handles both branches of the reflected maximum and proves

\[
\text{reflected}+\text{short}+z\le23M/30+\xi,\qquad
\text{reflected}+\text{short}+6\kappa z\le14M/15+\xi.
\]

The source also has nonnegative short and reflected lengths; the compiled
upper-bound implication does not need those extra lower bounds. The retained
\(z\ge0\) condition is a physical source hypothesis and is explicitly
marked unused in the clipped algebra proof.

## Explicit nonvacuity and boundary controls

The same Lean file proves existential real witnesses:

| Control | \(M,A,z,\kappa,A_{\rm comp},\xi\) |
| --- | --- |
| Strict positive comparison | \((60,51,2,13/18,43,0)\) |
| Positive support error and retained margins | \((60,51,2,13/18,44,1)\) |
| Simultaneous equality in all three upper bounds | \((60,50,3,13/18,46,0)\) |
| Below-threshold failure of all three bounds | \((60,50,25/8,7/10,185/4,0)\) |

Thus the compiled real-parameter hypotheses are inhabited, including the new
range \(13/18\le\kappa<3/4\). These examples do not instantiate the full
analytic fourth-moment theorem. A further positive witness covers the clipped
reflection hypotheses.

## Reproduction and trust boundary

From the checkout root run

```bash
python research/exploratory/2026-10-10-four-hour-wave/xi/formal/compile_low_kappa.py
```

The runner activates the installed tools, runs Lean through the repository's
`formal/` Lake environment, and writes ignored compiled artifacts under
`.build/`. [low-kappa-compilation.json](low-kappa-compilation.json) records
the actual compiler version, mathlib revision, hashes, full compiler arguments
and every theorem's axiom list. [compiler-output.txt](compiler-output.txt)
retains the compiler evidence. The candidate imports Mathlib directly and
is outside the trusted project imports.

The successful build uses mathlib
`51e6992efd06126df61a496bebf8f49482a4e129`. Every theorem's complete printed
axiom set is contained in `propext`, `Classical.choice`, `Quot.sound`.
No admitted proof or extra source axiom appears. The runner uses explicit
exceptions for its acceptance predicates.

The result certifies the stated real arithmetic. It does not certify the
enlarged analytic moment theorem, any actual-xi input, a zero-free conclusion,
or RH.
