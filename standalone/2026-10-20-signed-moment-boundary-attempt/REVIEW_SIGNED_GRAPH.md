# Independent review of the exact sixth-power graph

Reviewer role: beyond_boundary. Author of the reviewed graph note:
repo_routes_audit. Review date: 20 October 2026.

Reviewed file: work3/SIGNED_SIXTH_POWER_GRAPH.md

Reviewed SHA-256:

    0459e0b5ccb98ebe2fcbe3618117c864e5e3baa4d181b2d076882ed5d5a5348e

The source comparison was against Liu, arXiv:2610.26835v1,
Lemmas 12.9–12.10 and §§12.7.1–12.7.3, using PDF SHA-256

    5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5

## Findings

No mathematical correction is required in the reviewed version.

1. The full Gauss coefficients satisfy the stated sixth-power
   invariance when the pool prime is coprime to both columns. This
   includes imprimitive powers and the natural Gauss zeros.
2. The residue-ring substitution in (2) is exact. With the source's
   allowed generators and compatible additive character, multiplication
   by \(p^6\) sends the residue variable modulo \(m\) to the
   \(p^6\)-divisible classes modulo \(mp^6\). The additive phase reduces
   to the original one modulo \(m\). The statement is valid over the
   number field; it does not require replacing the field residue rings
   by integer residue rings.
3. The enlarged row norm scale and enlarged modulus norm have the same
   factor \((Np)^6\). Therefore both the Poisson prefactor and the
   transformed norm argument in (3) agree with those of the
   unamplified sum. Retaining the graph retains its nontrivial Fourier
   aliases.
4. Formula (4) has the correct normalization for a pool with smooth
   positive prime weights and row-dependent admissibility. It keeps
   \(A(h)=\sum_p w_p a_p(h)\) inside the exact change of variables.
   It does not substitute a constant pool cardinality. The formula
   applies to the invariant part of the summand; column-divisibility
   errors must remain separately accounted for.
5. For the single fixed-prime mask \(1_{p\nmid h}\), the graph is
   \(v_p(k)=6\). The modulus \(mp^7\), compared with the original
   masked modulus \(mp\), is correct. The note correctly refrains from
   assigning that period to a general coefficient containing
   \(1/A(h)\).

An average over pool primes is still an exact identity. Neither a
smooth positive weight nor an admissibility normalization deletes the
aliases. Estimating cancellation between aliases from distinct primes
is a possible additional analytic argument, which this review does
not rule out or supply.

## Scope

This review covers the exact identities, their normalization, and the
stated limitation on the direct source inference. It is not a proof
of a higher product moment, an impossibility theorem for signed
amplification, or a numerical zero-free improvement. The separate
signed-origin note is this reviewer's author contribution, not an
independent review of that note.
