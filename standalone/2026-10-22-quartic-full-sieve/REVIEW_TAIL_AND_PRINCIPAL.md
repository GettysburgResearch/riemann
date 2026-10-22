# Independent internal review of the quartic tail and principal target

Date: 2026-10-22.

Reviewer: the separate research agent `alternative_major`.

This is an internal mathematical proof check. It is not external peer review,
and it does not certify a new zero-free region. I read the complete arguments,
re-derived the local exponents and amplifier identity, and checked the actual
row and profile scopes. No numerical experiment is used as proof.

## Reviewed versions

| File | SHA-256 of reviewed content |
|---|---|
| `QUARTIC_PRIMITIVE_SIEVE_TAIL.md` | `7500879e7fd62776ab4c06c55f3de2777fac9c8983e3acd62a6ef75943a8ee64` |
| `DIRECT_PRINCIPAL_TARGET.md` | `5f87538ea5dbc9c858ae867969ee9170ccdc303e384fecaa1cee7aa8bf3a63cb` |

Both files were read from `work/round4_full_inverse/`. The hashes were
computed from the local bytes after the changes described below.

## 1. Quartic primitive-sieve tail

**Review outcome:** the stated tail bound has a complete valid proof within
its stated scope:

\[
 \sum_{0<Nk\le K}|T_R(k,D)|^2
 \ll_{\epsilon,W}(KD)^\epsilon
       \left(\frac K R+\frac{D^2}{R^4}\right).
\]

The following are the substantive checks.

1. **Local support.** If the exponent \(e\ge2\) of a prime in the
   modulus is not divisible by four, the local character is induced from a
   nontrivial character modulo that prime. The Gauss sum vanishes unless
   the row has valuation exactly \(e-1\), and its modulus after division
   by the modulus norm is \(q^{-1/2}\). If \(4\mid e\), the exact
   normalized Ramanujan sum is
   \(1_{p^e\mid k}-q^{-1}1_{p^{e-1}\mid k}\). Both branches are needed;
   the proof retains them.
2. **CRT phases.** In the unique factorization of a modulus as a coprime
   squarefree part times a powerful part, the CRT factors are fixed column
   phases. After extracting the required row divisor from the powerful
   part, its remaining Gauss factor is a common row factor of modulus at
   most one. It does not become an extra coefficient depending jointly on
   the squarefree column and the varying row. Thus its removal in the norm
   is justified.
3. **Large-sieve scope.** The proof uses the complete multiplicative large
   sieve with bound \(X+M^2\), obtained by finite Gauss inversion and the
   two-dimensional additive large sieve. This includes every nonzero
   Gaussian row. The selected quartic character at an odd squarefree
   modulus is primitive at every prime in that modulus; the conductor-one
   term is harmless. No squarefree-row large-sieve theorem is substituted
   for the required complete-row estimate.
4. **Column normalization.** For a fixed powerful part, the remaining
   columns lie in a fixed annulus and their squared coefficient sum is
   \(O_W(1)\), including the case in which the annulus contains the unit
   ideal. The resulting branch bound has exactly the two terms displayed
   in equation (14) of the note.
5. **Summation over powerful parts.** For a fixed nonzero row, every
   supported powerful modulus has each prime exponent at most one more
   than the row valuation. The number of local branches is divisor
   bounded. Cauchy can therefore be applied in each physical row with only
   a subpower loss. Applying Minkowski across all powerful parts would not
   justify the same bound; the proof does not do that.
6. **Euler exponents.** The local costs for the row-volume term and the
   column term are respectively
   \(q^{-2}(1+O(q^{-1}))\) and
   \(q^{-5}(1+O(q^{-2}))\). Summing by the squarefree radical above
   \(R\) gives \(R^{-1+\epsilon}\) and \(R^{-4+\epsilon}\), exactly
   as claimed.
7. **Endpoint scope.** The row zero is explicitly excluded. The exact
   empty ranges \(R\ge\sqrt{bD}\) and \(R\ge K\) follow from the
   strict cutoff \(Nd>R\), the column support, and the forced divisibility
   \(d\mid k\). No statement for the zero Fourier coefficient is
   implicitly included.

The local identities were independently compared with the primary
prime-power and CRT formulas in
[DDHL, arXiv:2306.11875v4, Section 3](https://arxiv.org/html/2306.11875v4).
The proof note cites an earlier version of the same paper; the identities
used in this review agree with the current inspected version.

**What this does not establish.** The Cauchy cross term requires an
independently established \(O(K)\) bound for the vector to which the tail
is attached. The inequality above does not prove that bound, a centered
main-term formula for the truncated sieve, uniform automorphic level
dependence, or a raw inverse moment below the existing range. The final
section of the reviewed note retains these qualifications.

## 2. Direct principal sixth-power target

**Review outcome:** the conditional implication is correct after the two
precision edits listed below. If the stated full physical-row hypothesis
holds for \(H\ge D^a\), with the smooth-profile uniformity now written in
the statement, then

\[
 \zeta(s)\ne0\qquad
 \left(\Re s>\frac12+\frac{5a}{12}\right).
\]

The exact deletion identity has the displayed minus sign:

\[
 M_1(D;W)=M_{p^6}(D;W)
          -(Np)^{-1/2}M_{p^6}(D/Np;W).
\]

It follows from the terms divisible by \(p\) and the literal zero of the
character at a nonunit; it does not discard those terms or assign them an
unrestricted character value. Distinct amplifier primes yield distinct
sixth-power rows. A fixed annulus of primes of size
\(A\asymp H^{1/6}\) therefore gives the factor \(A^{1-o(1)}\), while
the complete-row hypothesis controls the sum of their squared inverse
polynomials.

The moving shorter length is handled legitimately by

\[
 F_p(t)=M_{p^6}(D/(At);W),\qquad
 t\partial_tF_p(t)=M_{p^6}(D/(At);xW'(x)).
\]

At each fixed \(t\), the column length is common to every amplifier row.
The assumed bound thus applies before integrating the one-dimensional
Sobolev inequality. The annulus parameter is bounded above and below, and
the shorter length is admissible with the same row scale, up to the stated
fixed enlargement. The weighted shorter term has an additional factor
\(A^{-1}\). Hence the normalized principal estimate is
\(|M_1(D;W)|^2\ll D^\epsilon H/A\), with the claimed exponent.

Normal convergence of the smoothed dyadic reciprocal series follows from
that estimate and the stated uniformity for the profiles
\(x^{1/2}W(x)\) and \(x^{-s}W(x)\) on compact subsets. The omitted
Euler factors are finite, holomorphic, and nonzero in \(\Re s>0\), so the
passage from the incomplete Dedekind zeta function to the complete one is
valid. Finally \(\zeta_E=\zeta L(\cdot,\chi_{-3})\), with the second
factor holomorphic in the relevant half-plane, justifies the Riemann-zeta
conclusion.

**Edits requested and verified in the hashed version.**

- The statement now explicitly requires the estimate for every fixed smooth
  annular profile, with finite-seminorm and common compact-family
  uniformity. This is needed by the dyadic holomorphic continuation, in
  addition to the one fixed Euler derivative used in the amplifier.
- The proof now continues \(1/\zeta_E^S\), and writes
  \(\zeta_E^S(s)=\zeta_E(s)\prod_{p\in S}(1-(Np)^{-s})\), instead of
  identifying a sum over good ideals directly with the complete reciprocal.

**Limit of the conclusion.** The full raw moment hypothesis is not proved
for any new \(a<1\) in the reviewed note. In particular the target
\(a=21/25\), corresponding to the half-plane \(\Re s>17/20\), is a
conditional calibration. It is not a new zero-free theorem.

## 3. Overall publication status

The quartic tail is a proved estimate for the exact omitted portion of a
squarefree-modulus projector. The principal target is a correct conditional
reduction that retains all physical rows, natural zeros, shorter lengths,
and required profiles. Both are suitable for inclusion in a clearly marked
research packet. Neither changes the source-qualified zero-free boundary.

## 4. Confirmation against the frozen published source

After the mathematical source was frozen, I retrieved the committed blobs
with `git show` from the local repository, using the full commit identifier
below rather than a moving branch name:

- Source commit: `193c3d79f0522f08f62afc5c24c29f139d889080`.
- Source tree: `1e71897b46a6b7b75fe8694c48b7d08911260276`.
- Parent commit: `e87c5f669f81fe6371af926917d1c5b21023bce8`.
- Packet directory: `standalone/2026-10-22-quartic-full-sieve/`.

The committed `QUARTIC_PRIMITIVE_SIEVE_TAIL.md` is 11,067 bytes and has
SHA-256
`7500879e7fd62776ab4c06c55f3de2777fac9c8983e3acd62a6ef75943a8ee64`.
The committed `DIRECT_PRINCIPAL_TARGET.md` is 4,600 bytes and has SHA-256
`5f87538ea5dbc9c858ae867969ee9170ccdc303e384fecaa1cee7aa8bf3a63cb`.
Both hashes exactly match the versions reviewed in Sections 1 and 2 above.

I also read the packet's `README.md` at that exact commit. Its scope is
consistent with this review: it explicitly says that no new zero-free
boundary has been proved, retains the inherited source-qualified benchmark,
identifies the quartic centered low-divisor estimate as open, and labels the
\(17/20\) consumer as conditional on an unproved full inverse moment. It
also distinguishes internal scoped checks from external peer review and
formal verification. This README scope check is not an independent audit of
the packet's other mathematical notes.

This confirmation is an **internal independent-agent check** of the two
named proofs and their exact published versions. It does not assert an
achieved boundary improvement. No mathematical source file was changed in
performing this confirmation; only this review report was extended.
