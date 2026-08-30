# Independent review of the Xi near-adapted-scale scout

Reviewed source: **939a24962a4c6a449c0b56e3b20f78b936f35f6c**.
Reviewer: codex-two-programmes / root, independent of the author.
Verdict: **PASS for the exact scalar and raw-Hardy statements;
the Xi-specific narrowing retains its stated L-106502 dependency.**

The review read the complete new note and producer, and the literal
L-106710 and L-106502 source statements. The companion replay authenticated
all six frozen source blobs at scientific head
81d52e569cc8bb566e54043fd692fd6157406aab.

## Mathematical reconstruction

With s=xi/2, x=d/xi, the odd sum and difference are
2s^K P_K(x^2) and 2s^K x Q_K(x^2). Dividing by the current
d(v^K-u^K) gives exactly

\[
p=\tfrac12\mathbb E_\mu R_K(d/\xi),\qquad
g=\tfrac{\xi^2}{2}\mathbb E_\mu[R_K(d/\xi)/d^2].
\]

The half-convolution and variable-change factors cancel. The two binomial
coefficient inequalities establish 1/K <= R_K <= K. Cauchy--Schwarz
then yields the stated inverse-variance lower bound on g. A positive
current excludes a measure supported only at d=0; the inverse moment is
finite by the original Schwartz integral.

Inserting the literal mismatch identity gives
rho(eta)=g/eta+(p-g)eta. For g>p, monotonicity and solving the two
quadratics give the exact accepted interval and width M/(g-p).
The M=0 case is a singleton, and the g<=p exception is correctly retained.

The proposed positive even Gaussian source really does induce an
unweighted N(0,nu) law for x at the fixed frequency. The extra current
weight is x^2 Q_K(x^2), not an unweighted Gaussian probability.
Its moment ratios give g~1/(2K nu), p~1/(2K), and
rho(1+c nu+o(nu)) -> (1-2c)/(2K). This is a source-varying
counterfamily, not a counterexample for the actual Xi kernel.

Conditional on the original positive-moment concentration, the g lower
bound suffices for the necessary exponentially narrow mismatch window.
No upper inverse-moment bound is assumed. The conversion from relative
scale width to physical frequency width first obtains an o(1)
carrier displacement and only then replaces xi by the carrier in the
exponential; that order is legitimate.

The raw Hardy-node mass bound follows by maximizing
2y exp(-2y A), with optimum y=1/(2A). The sharper interval-mass
maximum in the note also agrees with direct differentiation.
This has no implication for arbitrary collective, confluent, source-weighted,
or outer-normalized vectors.

## Reproduction

At the exact source worktree:

- producer check passed in normal and optimized Python;
- all 23 tests passed in normal Python and all 23 under -O;
- Ruff passed;
- the worktree remained clean.

No numerical Fourier transform, Xi zero computation, contour computation,
or source-Pick determinant was performed. Rational Gaussian-moment and
phase controls are finite regressions, not proofs of the analytic limits.

## Retained boundary

The pointwise density ratio is not a Pick congruence and not the physical
outer-normalized companion quotient. The actual denominator-kernel metric,
signed off-band compensation, collective localization, and free-energy
estimate remain open. The source's independent constant-review request
for L-106502 is not discharged by this audit.

The smallest invalidating source-level change would be replacing the
current-weighted conditional measure by an unweighted product measure,
or applying the scalar ratio after an unjustified outer-factor division.
Neither change occurs in the reviewed packet.

There is no ninety-percent, density-one, RH, GRH, or novelty conclusion.
