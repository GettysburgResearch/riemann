# Validation and reproduction

Status: complete component proofs with scoped source review, exact finite arithmetic checks, and non-certified floating moment diagnostics. The full near-linear fourth moment, the 17/24 zero-free boundary, the unbounded moment hierarchy, and RH are not established.

## 1. Mathematical review

The [independent review](INDEPENDENT_MOMENT_REVIEW.md) identifies the exact theorem files, their SHA-256 hashes, who authored or contributed each component, and which parts received a separate review. Review was performed by collaborating AI research agents. It is not human peer review or a proof-assistant certificate.

The reviewed arguments retain the distinctions that matter for these moments:

- Every element row is included, with literal character zeros at nonunits.
- Sixth-power bases may overlap their power-free cores.
- An arbitrary coefficient sieve is distinguished from a bounded-coefficient inner estimate.
- Fixed masks are distinguished from masks for which uniformity is actually proved.
- Smooth separation and signed arithmetic regrouping occur before the relevant norm inequalities.
- Actual portions of the expanded inverse polynomial are distinguished from its unresolved full moment.
- Conditional use of the imported second moment and zero-free theorem is stated locally.
- The arithmetic row cutoff \(H\) is separate from the imaginary height of a zeta zero.

The refined all-row sieve and its overlap consequences use classical character sieves and elementary ideal arithmetic. They do not use the imported quasi-Riemann conclusion. The structured two-Poisson transfer relies on its named imported interfaces and leaves the completed theta extension and the adverse initial scale unresolved. The weaker full moments rely on a common zero-free half-plane and the imported second moment.

No Lean toolchain was run for this packet. The imported Lean dependency closure remains preserved in the preceding source packet; preservation does not certify a kernel build.

## 2. Actual finite diagnostic

[The main program](checks/sextic_moment_probe.py) implements sextic symbols over \(\mathbb Z[\omega]\), with \(N(a+b\omega)=a^2-ab+b^2\), fixed twist \(\nu=1\), and column prime ideals above 2 and 3 omitted.

For a split rational prime it constructs the two prime ideals separately and evaluates Euler's sextic symbol in each residue field. For an inert prime it uses the quadratic residue field. Nonunit values are retained as zeros. Squarefree ideal columns are generated from their distinct prime-ideal factors; the two conjugate prime ideals are distinct factors.

The fixed weight is
\[
W(x)=
\begin{cases}
\exp\!\left(1-\dfrac{1}{1-(4x-3)^2}\right),&1/2<x<1,\\
0,&\text{otherwise}.
\end{cases}
\]

Every nonzero lattice element with \(Nu\le H\) is included. The run uses \(H=\lceil D^{11/10}\rceil\), with the ceiling computed by exact integer comparisons. The program accepts a rational theta, rather than using floating exponentiation for the integer row cutoff. In particular, \(D=1024\) has \(H=2048\), exactly. An earlier development run rounded that cutoff to 2049; the saved final run is corrected. There are no lattice rows of norm 2049, so the correction changes the normalizing denominator at that panel but not its actual row set or raw moment sums.

The symbol exponents and factorizations are exact. The smooth weight, complex sum and moments use ordinary binary64 arithmetic. There is no directed rounding or interval certificate for those moments.

### Saved panels

The table gives \(M_4/(HD^2)\) for the specified weight and fixed twist. Its values are diagnostics at these finite scales, not estimates of an asymptotic exponent or its implied constant.

| \(D\) | Exact \(H\) | Element rows | \(M_4/(HD^2)\), rounded |
|---:|---:|---:|---:|
| 64 | 98 | 360 | 0.01248369545 |
| 128 | 208 | 756 | 0.03745158910 |
| 256 | 446 | 1,626 | 0.02853701278 |
| 512 | 956 | 3,462 | 0.02524651590 |
| 1024 | 2048 | 7,446 | 0.03290693128 |
| 2048 | 4390 | 15,936 | 0.03219113263 |
| 4096 | 9411 | 34,122 | 0.03288757259 |
| 8192 | 20172 | 73,140 | 0.03180119845 |

All moments of orders 2, 4, 6, 8, 10 and 12 are saved in [the full result](results/sextic_moment_probe.json). The largest panel has 1,022 available prime ideals, 1,145 nonzero-weight squarefree columns, and coefficient energy approximately 566.9022043496.

The largest panel's sixth-moment ratio \(M_6/(HD^3)\) is approximately 0.006733335471. Neither its size nor the fourth-moment table proves uniform control as \(D\) tends to infinity. The high moments can also vary substantially between panels; no random-phase model or fitted decay law is asserted.

## 3. Exact checks and their scope

The final run completed the following checks.

| Check | Coverage | Exact predicates |
|---|---|---:|
| Full-residue symbol distribution and multiplicativity | Every residue pair in each included residue field of norm at most 100 | 68,680 |
| Independent signed norm-coefficient identity | Every integer norm from 1 through 8192 | 8,192 |
| Symbol at \(-1\) | All 1,022 prime ideals of norm at most 8192 | 1,022 |
| Sixth powers and their nonunit zero mask | All 49 inputs \(a+b\omega\), \(-3\le a,b\le3\), at all 1,022 prime ideals | 50,078 |
| Inert-field conjugation | The same 49 inputs in each included inert field | 588 |
| Total of the above arithmetic predicates | Scoped identities only | **128,560** |

The norm-coefficient check follows a separate route from the ideal enumeration. It compares the signed ideal counts with the rational Dirichlet convolution
\[
\mu_{\mathbb Z}*(\mu_{\mathbb Z}\chi_{-3}),
\]
then removes integer norms divisible by 2 or 3. This is the coefficient identity from \(\zeta_K(s)=\zeta(s)L(s,\chi_{-3})\). It checks split/inert multiplicities and Möbius signs without using the diagnostic's moment sums.

The [additional checker](checks/check_sextic_probe.py) imports the symbol implementation under test and checks independent algebraic identities. It does not implement every finite-field operation independently. Its result binds both program hashes and records safely bounded int64 arithmetic. It contributes 51,688 of the predicates above. Its acceptance conditions use explicit exceptions, so Python optimization cannot disable them. Normal and optimized runs were both completed and returned byte-identical results.

A separate final check also verified
\[
(H-1)^{10}<D^{11}\le H^{10}
\]
for each of the eight saved panels. These eight comparisons validate the stated cutoff; they are not included in the arithmetic-predicate total.

The main command is deliberately scoped to \(2\le D\le8192\), \(0<\theta\le1/10\) with rational denominator at most 1000, and moments through order twelve. Within that range the vectorized integer residue products fit safely in int64. Larger experiments require a fresh arithmetic and resource review; the program rejects parameters outside this scope.

## 4. Reproduce

Run from this packet directory with Python and NumPy. The recorded environment used Python 3.12.14 and NumPy 2.3.5. Floating results on another platform may differ in their last few digits.

~~~bash
python checks/sextic_moment_probe.py \
  --scales 64,128,256,512,1024,2048,4096,8192 \
  --theta 1/10 \
  --kmax 6 \
  --output results/sextic_moment_probe.json

python checks/check_sextic_probe.py \
  --prime-limit 8192 \
  --output results/sextic_probe_additional_checks.json
~~~

Both commands were run to completion on the final program versions. The additional checker's saved status is PASS_SCOPED_EXACT_SYMBOL_IDENTITIES. The main result's saved status is FINITE_NUMERICAL_DIAGNOSTIC_ONLY.

The final [provenance manifest](PROVENANCE.json) records the exact program, result, proof and review hashes. It also records the parent repository commit and upstream source pins. To inspect integrity without rerunning the floating experiment:

~~~python
from pathlib import Path
import hashlib
import json

root = Path(".")
manifest = json.loads((root / "PROVENANCE.json").read_text())
for entry in manifest["files"]:
    data = (root / entry["path"]).read_bytes()
    assert len(data) == entry["bytes"], entry["path"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"], entry["path"]
~~~

The manifest omits its own hash to avoid self-reference. The commit's Git tree provides its publication identity. No development-only source excerpt, bytecode cache, or unrelated repository file is part of this packet.

## 5. What remains open

A complete fourth-moment proof must handle the long balanced Möbius cores, including nearly coprime factors of size \(D\), at the near-linear row range. Deleting exceptional rows, applying an arbitrary-coefficient short-row sieve, or feeding back only the old pointwise zero-free bound does not close that problem. The proofs identify why each proposed shortcut fails and which exact inputs would still be needed.

The packet provides component proofs, explicit partial ranges, a source-specific correlation estimate, and reproducible finite diagnostics. It establishes no further zero-free improvement beyond the preceding packet's conditional \(139999/160000\), and it makes no height-dependent shrinking-band claim.
