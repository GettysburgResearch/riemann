# Theta order 26, incremental root construction, and a weighted all-order criterion

This directory contains proposed native mathematical components and directed
finite certificates for the actual Xi function. The principal finite result
is exact Taylor matching through orders **22, 24, and 26** by explicit entire
functions whose zeros are all real. A subsequent construction gives a two-step
numerical extension chain with separately certified endpoints:

\[
       (22,64)\ \longrightarrow\ (24,84)\ \longrightarrow\ (26,104),
\]

where each pair records `(matched Taylor order, number of quadratic factors)`.
Each extension appends 20 new factors. Its endpoint exists by complete-source
directed interval arithmetic; the numerical path between endpoints is not
certified.

The strongest all-order component is
[WEIGHTED_CANONICAL.md](WEIGHTED_CANONICAL.md). It proves that positive weighted
power-sum feasibility at unbounded orders would imply RH. The consumer needs
neither integer multiplicities, a positive Gaussian reserve, a positive inverse
Fourier density, nor a common bound on node support. The missing unbounded-order
positivity/construction is stated explicitly. This packet establishes **no new
zeta zero-free boundary and no proof of RH**.

## The finite certificates

All models take the form

\[
 P(z)=e^{-az^2}\prod_{j=1}^{N}(1-b_jz^2),
 \qquad a>0,\quad b_j>0,\quad a+\sum_jb_j=\tfrac12.
\]

They agree with the variance-one theta function
`H(z)=xi(1/2+iz/sqrt(v_theta))/xi(1/2)` through the stated Taylor order and
obey `|P(z)| <= exp(|z|^2/2)` everywhere. All zeros are the real numbers
`+/-1/sqrt(b_j)`, with their multiplicities. The physical Xi approximant is
`P(sqrt(v_theta) z)`. Matched order 26 is distinct from polynomial degree.

| Construction | Matched Taylor order | Factors | Polynomial degree | Upper contraction bound |
|---|---:|---:|---:|---:|
| Direct positive-node fit | 22 | 64 | 128 | `2.320e-38` |
| Direct positive-node fit | 24 | 128 | 256 | `5.857e-37` |
| Direct positive-node fit | 26 | 128 | 256 | `8.859e-35` |
| First incremental endpoint | 24 | 84 | 168 | `1.749e-36` |
| Second incremental endpoint | 26 | 104 | 208 | `9.236e-35` |

Every certificate uses a full active-coordinate cube of rational radius
`10^-50`. The checker includes every term of every finite sum and every
Jacobian entry. Its source is reconstructed from the complete positive theta
kernel, including time, index, and Taylor tails; a zeta-zero table is not a
proof input. The interval backend is inherited and authenticated, while the
new source integrals are recomputed through order 26.

The new finite models are entire-function constructions. A positive
probability-law representation is not asserted or needed for their zero
locations, coefficient matching, or entire bounds.

## Read the mathematical argument

| File | Content |
|---|---|
| [SOURCE26.md](SOURCE26.md) | Complete theta-kernel identity, normalization, quadrature, and every analytic remainder |
| [PROOF_GAUSSIAN.md](PROOF_GAUSSIAN.md) | Direct 22/24/26 finite existence theorems, whole-cube contraction, and canonical-factor compactness |
| [PROOF_INCREMENTAL.md](PROOF_INCREMENTAL.md) | Certified 84/24 and 104/26 endpoints, including their exactly fixed 20-fold new clouds |
| [WEIGHTED_CANONICAL.md](WEIGHTED_CANONICAL.md) | Positive weighted all-order criterion, correct half-plane domains, and an imaginary-axis identification argument |
| [extension/POWER_SUM_EXTENSION.md](extension/POWER_SUM_EXTENSION.md) | Exact moving-root identities, quantitative safe intervals, collision coordinates, and controlled complex-pair compactness |
| [extension/PROOF_EXTENSION.md](extension/PROOF_EXTENSION.md) | Reference-variance trapping and exact interacting graph perturbations |
| [EXPERIMENTS.md](EXPERIMENTS.md) | Selected completed searches, failures, and the reason for changing construction class |

Independent mathematical reviews and hash-bound replay reports are in the
sibling `audit/` directory. The reviews retain the proposed component status
and the explicit missing all-order hypothesis.

## Reproduce the proofs

From this directory in the repository:

```sh
python -O check_gaussian.py --rebuild-source
python -O check_incremental.py
python -S extension/check_power_extension.py
python -S extension/check_extension.py
```

The first command reconstructs the complete source and checks the three
direct models. The second checks both incremental endpoints. The last two
check exact finite algebra behind the extension identities. Python `-O`
cannot remove the explicit acceptance guards; the extension checkers also
run with `-S`, without third-party packages.

The default source location is the sibling earlier packet:

```text
standalone/2026-10-18-theta20-and-native-cancellation/theta/
```

It is pinned to commit `c93ca65a510b6acaf167f929b9bf7e67d742b05a` and includes
the authenticated arithmetic primitive with Git blob
`c32015f110d10186538ffabcb4689ba5bbc060d0`. In another staging layout, supply
`--source /path/to/pinned/theta` to the two Gaussian checkers. The complete
source can be rebuilt once and then authenticated by its recorded digest on
subsequent endpoint replays.

The decisive receipts are `gaussian_certificate.json` and
`incremental_certificate.json`. Their code, primitive, source, and exact
parameter hashes are recorded inside them. Replaying the same interval
backend is reproducibility, not an independent arithmetic implementation;
the separate mathematical reviews address that distinction.

## Reproduce the numerical producers

The directed checkers need the Python standard library and the pinned
primitive. The exploratory producers additionally use NumPy and SciPy.
Regenerate the exact rational input files from the curated chosen centers,
without overwriting the checked copies:

```sh
python produce_gaussian_certificate.py --output /tmp/gaussian_parameters.json
python produce_incremental_certificate.py --output /tmp/incremental_parameters.json
```

The recorded local replays produced byte-for-byte identical parameter files.
Different QR libraries may select different valid active columns; only a
successful directed check of the resulting cube establishes its theorem.

The direct search itself is short to replay:

```sh
python search_gaussian_polynomial.py --degree 22 --nodes 64 --without-density --output /tmp/theta22_search.json
python search_gaussian_polynomial.py --degree 24 --nodes 128 --without-density --output /tmp/theta24_search.json
python search_gaussian_polynomial.py --degree 26 --nodes 128 --without-density --output /tmp/theta26_search.json
```

All three recorded replays reproduced every chosen center, target, damping
step, and Newton history exactly. `gaussian_candidates.json` retains those
three complete histories and provenance hashes. Optional inverse-density
diagnostics were excluded from the curated data because they are outside
the theorem.

`initial_zero_guesses.json` identifies the primary Odlyzko table used to
initialize the optimizer. Those numerical entries are seeds only: changing
them affects search convenience, and the directed checker never loads them.
The root-flow producer and exact endpoint provenance are in `extension/`;
its curated candidate files retain the selected complete endpoint parameters
without the large intermediate diagnostic histories.

## The next mathematical task

With
`Q_r=(-1)^(r+1) r kappa_(2r)/(2r)!`, the weighted consumer needs finite positive
nodes and weights satisfying

\[
           \sum_j\lambda_jb_j^r=Q_r,
                         \qquad 2\le r\le M,
\]

for unbounded M. Equivalently, the positive atomic measure
`nu=sum_j lambda_j b_j^2 delta_(b_j)` must realize the available moments
`Q_2,...,Q_M`. Existing finite successes verify initial instances. They do
not prove all-order positivity of the actual theta cumulants.

The moving-root construction gives a concrete incremental mechanism and two
successful finite steps. Its complete continuation still depends on target
gap signs, affordable root motion, and collision handling. The weighted
half-plane theorem supplies a second route that can use general positive
moment measures. Both routes now have fewer unnecessary constraints, while
retaining the exact ordinary-zeta target.
