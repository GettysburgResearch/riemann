# O-15301 — July 2026 positive-path convergence audit

Claim ID: `O-15301`  
Title: The radical-tail ratio is closed; the low packet must be split by certified zero evaluations  
Status: `LITERATURE_AND_REPOSITORY_AUDIT`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31

## Located primary sources

1. Alain Connes and Caterina Consani, *Spectral Triples and Zeta-Cycles*,
   arXiv:2106.01715; L'Enseignement Mathématique 69 (2023), 93--148.
2. Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta Spectral
   Triples*, arXiv:2511.22755 (2025).
3. Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
   arXiv:2606.09096 (June 2026).
4. Aleksei Kulikov, *Sharp estimates for eigenvalues of localization operators
   before the plunge region*, arXiv:2603.07407 (March 2026).
5. Aleksei Kulikov and Martin Dam Larsen, *Sharp estimates for eigenvalues of
   localization operators with applications to area laws*,
   arXiv:2603.23832 (March 2026).
6. Ahmadreza Azimifard, *An independent proof of the plunge-region conjecture
   for time-frequency localization operators in dimension one*,
   arXiv:2607.23016 (July 2026).

Every reference above was located directly. No unlocated citation is used in
this audit.

## Independent mathematical convergence inside the repository

During this pass, three conclusions were derived independently on separate
branches and then found to agree:

1. the finite prolate source needs both `f(0)=0` and `integral f=0`, so two
   distinct finite modes cannot in general supply an exact radical source;
2. three modes give the exact cross-product repair;
3. locally uniform real-zero convergence to

   ```text
   zeta(1/2-iz) * Phi(z)
   ```

   is sufficient for RH whenever the product is not identically zero; `Phi`
   need not be zero-free.

The base PR now contains the stronger detailed versions of these results. This
branch withdraws its duplicate claim cards and retains only the genuinely
additional low-block analysis.

## Newly closed component

The current PR #152 stack now contains an explicit self-Fourier Gaussian/Hermite
source satisfying both source constraints, a term-by-term Gaussian bound on the
localized radical-tail cross form, and a complete finite multiband packet whose
Hardy complement floor loses only a polynomial support factor.

Consequently the ratios

\[
 \mathfrak T_\lambda/h_\lambda\to0,
 \qquad
 \mathfrak T_\lambda^2/(h_\lambda\|k_\lambda\|^2)\to0
\]

are no longer the missing positive-path theorem. The exterior radical tail is
not the current blocker.

## Claim-registry defect found

The active base branch presently assigns the same IDs to distinct files:

```text
L-14312  two claims
L-14313  two claims
T-14303  two claims
X-14307  two experiments.
```

This is a process blocker, not a mathematical refutation. The claims should be
renumbered and every dependency, schema, report, and integration patch updated
before merge.

## Correction to the remaining low-block program

The newest base audit correctly isolates the growing finite low-symbol packet.
However, asking the **entire** packet to approach small-tail radical
truncations is too strong.

Exact global radical transforms vanish at every actual zeta zero. If
`r=k+t`, then at each certified centered zero

\[
 \widehat k(z_\rho)=-\widehat t(z_\rho).
\]

Thus small radical tails force small certified-zero evaluations. `L-15304`
proves a finite singular-value obstruction: any packet subspace with a positive
zero-evaluation singular floor stays a positive distance from all such radical
truncations.

The correct finite decomposition is therefore

```text
complete low packet
    = radical-like zero-evaluation near-kernel
      + evaluation-visible residual block.
```

Only the near-kernel should be fitted by exact radical sources. The visible
block needs its own finite lower certificate.

## Role of the latest localization literature

The 2026 pre-plunge and plunge-count estimates improve packet scheduling:

- pre-plunge modes can have exponentially small Fourier leakage;
- the transition packet has explicit logarithmic-size estimates in standard
  one-dimensional localization models.

They do not identify the arithmetic zero-evaluation near-kernel, certify the
visible low block, or prove the complete Weil lower floor.

## Revised critical path

1. repair the duplicate base IDs;
2. construct the complete first low-symbol packet;
3. evaluate it at proof-grade critical-line zeros;
4. certify a rational near-kernel/visible-block split;
5. approximate only the near-kernel by exact Gaussian/Hermite radical targets;
6. directly lower-bound the visible block and all cross maps;
7. compose the finite matrix with the ambient complement through `L-14308`;
8. prove a symbolic cofinal floor `>=-epsilon(lambda)`, `epsilon(lambda)->0`;
9. invoke `T-14302`.

## Honest conclusion

The source normalization, external-tail numerator, complement denominator, and
their cofinal ratio now have coherent proposed solutions. The growing low block
remains open, and its first proposed full-packet approximation must be refined
by the zero-evaluation obstruction. No proof of RH is claimed.