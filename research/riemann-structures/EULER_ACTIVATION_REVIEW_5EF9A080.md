# Independent review of the native Euler activation adapter

Scientific checkpoint: `5ef9a0800e7d0f03bfef1ad4ba467f8843a90058`.

Reviewed files: `EULER_ACTIVATION_SOURCE_ADAPTER.md`, `euler_activation_source_adapter.py`, its JSON certificate, and `tests/test_euler_activation_source_adapter.py`. The checkpoint adds these four files. This review concerns this frozen packet, not a subsequent gauge-derivative extension.

## Finding

No unresolved mathematical or implementation blocker was found in the stated scope. The result identifies the complete Boolean equal-pair coefficient with an owner-activation projection of the declared native Euler homotopy. It also proves the compensating core activation at the same labelled physical monomial. It does not identify that projection with the full retained-carrier current, and it does not supply a new bound for the existing paid diagonal.

## Independent mathematical checks

I read the proof and implementation, and inspected the relevant frozen Euler-path, carrier, and equal-pair source definitions. For the local path `e_t=1-t*x-(1-t)*x^2`, the mixed labelled coefficient is `mu(a)*t^2*(1-t)^k`. Differentiating the two owner sites gives `2*mu(a)*t*(1-t)^k`; differentiating the core sites gives `-k*mu(a)*t^2*(1-t)^(k-1)`. Their integrals are respectively `mu(a)/binom(k+2,2)` and its negative. The full endpoint coefficient vanishes for `k>=1`, while the `k=0` semiprime endpoint remains nonzero.

The raw carrier argument uses the absence of a degree-one local term in `R*S`, so `-R*S*L` cannot provide both distinct odd owner labels. This is an argument about the specified labelled monomial, not every physical integer that can be represented by different label allocations.

The source completion is appropriately limited. In the frozen subcritical examples the full Vaughan row is `+1-2=-1`, whereas the previously isolated balanced row was `-2`. Thus the completed full owner amplitude is half the balanced amplitude. The four fixed-core bilateral activation pairings are `J/4,-J/4,-J/4,J/4`, and cancel at the common physical observation. This is not a statement about cross terms between independently selected core packets or arbitrary retained masks.

The three diagonal formulas correspond to genuinely different measures or aggregation stages: derivative site with Lebesgue parameter measure, integrated individual sites, and two aggregated activation sectors. Their values are respectively

`4/((2k-1)(2k+1)(2k+3)N)`,

`2/(k(k+1)^2(k+2)N)`, and

`8/((k+1)^2(k+2)^2 N)`.

The packet correctly avoids identifying these with the frozen native paid diagonal. Even when the uncentered field cancels, a centered expression retains its declared diagonal correction.

## Corrected issue found during review

The source has two distinct labels associated with the physical prime 67. A physical integer involving `67^2` can therefore also arise from two linear labels, even though the selected squared-label monomial has zero endpoint coefficient. I raised this aliasing issue; the frozen proof now explicitly restricts the zero statement to the labelled sector, excludes 67 from the subcritical fixture, and includes a regression distinguishing the four-linear-label coefficient from the mixed squared-label coefficient. This repair affects the scope of the statement and prevents an incorrect promotion to an unrestricted physical-integer quotient.

## Independent code review

I read the bounded exact polynomial integration, literal product-rule densities, all three diagonal calculations, raw-carrier coefficient checks, frozen subcritical-panel authentication, and complete Boolean allocation reconstruction. The implementation uses exact rational arithmetic and explicit validation rather than floating-point evidence for the identities. The ten tests include endpoint cancellation and nonfactorization, the surviving `k=0` sector, diagonal normalization, the complete Vaughan row, duplicate-label aliasing, integration, type/cap checks, and source/certificate rejection controls.

## Execution evidence and limits

I did not run tests or the producer. The coordinating agent reports that Ruff, producer write/check, optimized check, ten ordinary tests, and ten optimized tests all passed. The reported proof-object hash is `e9e95f790e92502bc0adb264f51272e186d7b53d5de2b0c004a8308270c0c6e0`. Those execution results are distinct from my independent source, proof, and code reading.

The elementary homotopy and beta-integral identities are classical. The useful contribution is the explicit source binding, complementary activation, and normalization boundary. Arbitrary carrier masks, gauge transport, source-dual weights, and the full retained-current estimate remain separate questions.
