# Independent review of logarithmic transport, field variation, and finite sextic arithmetic

Reviewer: the spectral research agent, separate from the authors of the two
family notes and the sextic experiment. Date: 2026-10-24.

**Disposition:** accepted at the explicitly stated scope. The transport and
representation identities are exact; their analytic uses remain conditional.
The sextic computations are exact finite experiments. None of these items
establishes a smaller zero-free half-plane.

## Frozen objects

Paths are relative to the containing research packet. SHA-256 binds this
review to the following bytes.

| Object | SHA-256 |
|---|---|
| `family/COHERENT_LOG_TRANSPORT.md` | `2d86f119b744f99cbad8b8f1098b37809429a1f07626d6be7d8cf2be3b065220` |
| `family/FIELD_TOWERS_AND_HORIZONTAL_TRANSPORT.md` | `264521afaef4aa3c6426fcc1bb224b3e6edb749815d54f849af44bda634b5d20` |
| `family/check_log_transport.py` | `44f8018a39b8feaf1d9f58443e512d54240c92d8c35d5e2278090734f7b493ac` |
| `family/check_log_transport_results.json` | `d3e56fb1ebb874f95a12aa2c5432a4278e5a291bb22a2025b3a837d489d81ade` |
| `sextic_interpolation_experiment.py` | `b4c34f39b8f0982734f98ad9403b6e3d5fd605169ce97596c2b13b95a58cde73` |
| `sextic_interpolation_report.json` | `fbe6523ddd7c670b5549b3a58a828818be9f2a0cf4e74145d43edc184f34d614` |
| `reviews/independent_sextic_checks.py` | `826bb8ae635300b9bb3f05fa67d4187c6c38031ee6070dcd7517db5f0e53b3b1` |
| `reviews/independent_sextic_checks.json` | `a8ed7397e8b2b1babab6c0d9da520e896271e73179d3a99f14d5f74f80e31a5f` |

## 1. Coherent logarithmic transport

I independently reconstructed the derivation of
\(\mu_F\log N=-\mu_F*\Lambda_F\). Substituting
\(H=D/(N\mathfrak p)^j\) and
\(V_D(x)=\log D\,V(x)/\log(Dx)\) gives the displayed transport formula
with exactly its minus sign, its factor \((N\mathfrak p)^{-j/2}\), and no
remaining logarithmic error. The prime-power sum is finite by support. The
zero-extended multiplicativity identity remains valid when one or both
factors are nonunits.

The higher-prime-power estimate is valid for \(a>1/2\), because its constant
\(\sum_{\mathfrak p,j\ge2}\log N\mathfrak p/(N\mathfrak p)^{ja}\)
converges. Absorption uses the specified half-maximum of the common envelope
and a sufficiently large \(\log D\). It is not a bound showing absorption
at every detector scale. The dyadic prime-block deduction keeps the prime
logarithm weight and pays for the number of dyadic blocks; its displayed
size follows from those factors.

For the proposed use of M1, the replacement inverse length is \(r-z\) and
the combined prime length is \(z+z_0\). The supplied conditions become

\[
 r+z+2z_0<1,\qquad 2r+6z+8z_0<3.
\]

I checked the original M1 coordinates directly against equation (13.2) of
[Liu, arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1).
The first condition fails when \(r>1\). This closes that particular
application of the supplied separate moment; it does not rule out a new
signed joint estimate. Liu's Section 15.2 also explicitly identifies
relations among the detected cutoffs as additional information beyond
the existing min--max argument.

The higher-logarithm identities and the surviving one-large-prime term are
correct. The rough splitting includes its entire \(\mathfrak d=1\)
residual. Its Euler correction has the stated upper majorant
\(\exp(CY^{1-\sigma}/\log(2Y))\). Thus the supplied majorant is
\(D^{o(1)}\) at \(Y=(\log D)^A\) if \(A(1-\sigma)\le1\), whereas
it is superpolynomial at a fixed power cutoff. This is a failure of that
absolute estimate to produce the desired result, not a lower bound for
the actual correction. The local Laurent calculation is also consistent
with a hypothetical zero.

The final version incorporates three scope clarifications requested in this
review: the presentation is unitary with \(|\psi|\le1\); the sums are
defined for every \(H>0\), including the short scales in the transport;
and the Euler product uses exactly the same omitted primes and nonunit zeros
as the coefficient sums. No further correction is requested.

The standard-library checker was independently replayed in ordinary and
optimized isolated Python. It reproduces 1,536 logarithmic coefficient
checks, 2,560 rough-splitting checks, and 3,280 character products, including
918 nonunit products. All eight deliberately incomplete prime-only
identities are rejected. These checks support the finite algebra only;
the infinite estimate was reviewed separately as above.

## 2. Field towers and horizontal transport

Frobenius reciprocity gives trivial multiplicity exactly one in
\(\operatorname{Ind}_H^G1\) for a connected field extension. The
resulting Artin factorization therefore forces one copy of the base zeta
function, regardless of the extension degree. The restriction to abelian
extensions when asserting unconditional zero persistence through an entire
complement is valid. The note does not infer global Artin holomorphy for a
general extension.

For genuine representations, the invariant-space multiplicity is at most
the degree; products and tensor constructions retain that cost. The caution
about negative virtual coefficients is appropriate. The unitary norm twist
has sign \(L(s,\eta N^{it})=L(s-it,\eta)\), so it changes height only.
The proposed mean-zero-count implication for full abelian-extension zeta
functions follows from their common factor. A theorem about the quotients
would not by itself count the removed base zeros.

These deductions reject a free gain from the specified representation
algebra. They do not exclude field variation supplied with new correlation
or analytic information. The imported numerical boundary remains explicitly
source-qualified; this review does not verify Liu's full analytic proof.

## 3. Sextic arithmetic and independent replay

I reran all nine declared rectangles using the primary Python runtime with
NumPy. The output is byte-for-byte identical to the author's JSON and has
the same SHA-256 as `sextic_interpolation_report.json` above. This includes the largest rectangle
\((U,D)=(2500,125000)\), with 762 physical rows, 35,284 squarefree
columns, and maximum column prime-factor count five.

The implemented ring is \(\mathbb Z[\omega]\), with
\(\omega^2+\omega+1=0\) and norm \(a^2-ab+b^2\). Its root list is
the positive ordering \((1+\omega)^k=e^{k\pi i/3}\). The prime-local
calculation agrees with the positive sextic convention
\((u/\mathfrak p)_6\equiv u^{(N\mathfrak p-1)/6}\pmod{\mathfrak p}\),
as in the sextic-symbol definition in
[Liu's version-pinned source](https://arxiv.org/html/2610.26835v1).
The split and inert formulas, the unique primary generators, and the
squarefree/sixth-power-free filters are consistent. Character values on
collisions are zero, and remain zero through composite-column products;
they do not become principal values when phases cancel.

The additional saved checker reconstructs expectations independently in
\(\mathbb Z[X]/(X^2+X+1)\), with arbitrary-precision modular polynomial
powering and an adjugate divisibility test. It does not use the author's
root table, local powering formulas, factor routine, or energy contraction
to obtain expected values. It imports the author's ideal/prime enumeration
and actual outputs being compared; norm counts are separately checked by
the divisor-sum formula for \(\zeta_{\mathbb Q(\sqrt{-3})}\), after
excluding primes above 2 and 3.

The saved receipt records:

- 300 ideal norm-count comparisons;
- 9,971 local residue comparisons at 59 prime ideals, including 179 natural
  nonunit cases and 6,548 nonreal values sensitive to orientation;
- a separately factored and accumulated \((64,128)\) rectangle, checked
  with exact rational arithmetic at \(z=-1,1/4,1/2,3/4,1,2\).

The resulting unnormalized energies are, respectively,
\(888,6823/256,1851/16,78039/256,664,6324\). They exactly match
the author's energy polynomial. The saved checker reproduces the original
independent receipt byte-for-byte.

The quadratic form \(A^2-AB+B^2\), its diagonal subtraction, and the
real-variable interpolation identity are correct. The fixed-width
arithmetic remains within its bounds on the declared cases. At \(z=-1\),
the squarefree column weight is exactly Möbius; at \(z=1\) it is the
unmarked squarefree weight. No Gauss factor has been inserted.

This is the explicitly defined untwisted \((u/n)_6\) experiment with
sharp annuli. The review does not transfer it to all ray presentations,
smooth profiles, heights, moving punctures, or growing parameters in an
analytic consumer. Finite exactness and bounded moment displays do not
establish the uniform asymptotic hypothesis needed for a new region.

## Reproducing the extra independent checker

From the packet directory, in a Python environment containing NumPy:

```bash
python3 -I -B reviews/independent_sextic_checks.py --output /tmp/independent-sextic.json
python3 -I -B sextic_interpolation_experiment.py --output /tmp/sextic-replay.json
```

The first output should have SHA-256
`a8ed7397e8b2b1babab6c0d9da520e896271e73179d3a99f14d5f74f80e31a5f`;
the second should have SHA-256
`fbe6523ddd7c670b5549b3a58a828818be9f2a0cf4e74145d43edc184f34d614`.
The second command is a complete rerun of the nine cases, not an input
receipt check.
