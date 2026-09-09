# Critical signed kernel: exact zero-mode resolution

**PROPOSED component theorems. Independent review pending. RH is not proved.**
This Riemann-repository continuation attacks the complete signed Mobius quadratic,
not another diagonal majorant. Read [PROOF.md](PROOF.md).

## What was found

Let Z(s)=(1-2^-s)zeta(s), F(s)=(s-1)Z(s)/s, and retain PR805's exact regularized
hyperbola kernel K(u,v)=R(1/(uv)). Introduce the endpoint-corrected Mellin mode

    nu_s=s(1-s)u^(s-1)du+s delta_1.

Its complete complex BILINEAR pairing is

    B(nu_s,nu_t)=st [F(t)-F(s)]/(s-t),
    B(nu_s,nu_s)=-s^2 F'(s).

The domain, boundary atom, pole removals and integrability at zero are proved
explicitly. The formula is not a Hermitian positivity claim.

At distinct zeta zeros the cross terms vanish. At a simple zero alpha the
matched term is alpha(1-alpha)Z'(alpha), exactly the reciprocal of the
coefficient of x^alpha in the Mellin pole expansion of Q(x). Multiple zeros
have explicit nonsingular antidiagonal jet blocks. A conjugate pair of
multiplicity m produces a real form of signature (m,m), not a positive form.

## The attempted completion has an exact limitation

For ANY finite selection S of zeros, include the double pole at zero of
-1/[s^2 F(s)] and form its finite residue model q_S(Y). The corresponding
source functional L_(S,Y) obeys EXACTLY

    B(L_(S,Y),L_(S,Y))=q_S(Y^2)-2q_S(Y).

This retains the logarithmic background and the full linear correction,
not merely the leading power. No simplicity assumption is needed.

Thus the square-scale identity itself is compatible with any hypothetical
off-critical zero. This does NOT assert that one exists, or that the finite
spectral models have the actual integer Mobius coefficients. It rules out
treating mode orthogonality or this nonlinear identity as a critical-line
selection mechanism without another actual-source estimate.

## Compact realization, without hiding a divergent boundary

The cutoff measure

    nu_(s,e)=s(1-s)u^(s-1)1_(e<u<1)du+s delta_1-s e^s delta_e

has exact harmonic balance. A complete weighted-variation bound controls the
omitted interval and proves convergence of its kernel pairings. The log-mode
cutoff has total coefficient mass log(1/e), which diverges. Convergent compact
kernel pairings therefore do not establish a bounded critical source norm.
These are continuous/atomic controls, not substituted Mobius data.

## Prior work and publication

The previous unpublished proof and checker are preserved BYTE-FOR-BYTE under
[prior/](prior/PROOF.md). The old 99,962-byte canonical report is not copied
into this new directory. `prior/check.py --write /tmp/prior-results.json
--self-test` reconstructs it exactly; its byte hash, semantic hash, and prior
ZIP provenance are in [SOURCES.json](SOURCES.json). The prior report was
reconstructed and compared byte-for-byte during this continuation. Its former
README/validation receipts remain in the previously supplied original bundle;
they are not silently rewritten to claim earlier publication.

## Claims and evidence

| Local ID | Scope |
|---|---|
| KSC-1 | Complete elementary kernel remainder and Mellin continuation. |
| KSC-2 | Exact all-domain bilinear divided difference, with endpoint atom. |
| KSC-3 | Multiple-zero jet orthogonality and real signature. |
| KSC-4 | Exact finite-spectrum square-scale identity, including the zero pole. |
| KSC-5 | Compact balanced cutoffs with complete omitted-boundary estimate. |
| OPEN | Subpower E(X) for the literal Mobius source; no improvement to that bound proved. |

Finite checks include native integer Mobius identities, piecewise exact kernel
integrals, synthetic polynomial-root/multiplicity models, and directed rational
remainder samples. Synthetic roots are NEVER declared to be zeta zeros. See
[VALIDATION.md](VALIDATION.md) for exact commands, counts, and omissions.

```bash
python -B standalone/2026-09-09-astra-kernel-spectral-continuation/check.py \
  --check standalone/2026-09-09-astra-kernel-spectral-continuation/results.json --self-test
```

Everything is exploratory and addition-only. No canonical result, formal
library, main branch, other research packet, or workflow is changed.
