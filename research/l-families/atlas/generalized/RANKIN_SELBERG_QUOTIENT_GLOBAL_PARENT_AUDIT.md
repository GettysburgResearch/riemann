# Rankin--Selberg quotient: independent frozen-source audit

Status: PASS in the stated meromorphic quotient scope.
RH and GRH remain unsolved. This is a research-branch audit, not a canonical
repository integration verdict or an external novelty certification.

## Exact object reviewed

Scientific source: b62dfc6348661992bca659c99de226a1b6b22e14.
Authoring parent: 246434f343029cc821aa236081c4d12080f571f2.
Programme import: f55df306d95ccf50959f715e030ae8eacdc457dd.

The five scientific files are unchanged by this review. Their frozen Git
blobs are:

| File | Git blob |
|---|---|
| [Proof](RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md) | 4a3f9f0b6644bffdc94214e6fb2b60dfafdd93ca |
| [Producer](rankin_selberg_quotient_global_parent.py) | 524c8ce891d79d751a324f70528e95e12bd5bc00 |
| [Fixture](rankin_selberg_quotient_global_parent.json) | f44fe4d65225601e04d86c58e6d6d296c51126c7 |
| [Manifest](rankin_selberg_quotient_global_parent.sources.json) | 5fc1c031e34a879496165407f6c500d9abfeac5a |
| [Tests](../../../../tests/test_rankin_selberg_quotient_global_parent.py) | 479567d07bb4f553bcd9b00bcbe515ac53ad0b24 |

Fixture LF-normalized SHA-256:
ff9c5e7cc43db1d9c63f317cd842e4337066ec30c30a2f8be6f45958648ce856.

Both the root reviewer and a separate reviewer read all five files. The
separate reviewer did not author the object or coordinate its acceptance
with the author. The root independently checked the frozen file bytes
against the working copies and reproduced every fixture artifact digest.

The single pinned context source is the published programme checkpoint at
the authoring parent, blob 3047f87a0a6e01c4ff6c6455e056a0aecb7e6cad.
It is context, not a surrogate proof of modularity or analytic continuation.

## Mathematical review

### 1. Source and flag

The source is the actual weight-24 cusp-form space, not a fitted
Dirichlet sequence. The standard modular-form facts imply
S24 = Delta M12 and give the basis f0=Delta E4^3, f1=Delta^2.
The scalar is tied to the specified cusp coordinate and normalized
functional ell(f)=[q]f. Its kernel is the line spanned by f1.

The q-coefficient and T2 calculations agree. The two Hecke eigenlines
are classical calibration; generic non-eigenform coefficients fail the
displayed coprime multiplicativity test. This is not claimed as a new
automorphic representation.

### 2. Completion and reflected endpoint

For the stated Eisenstein normalization, the root checked the completed
series and period formulas against the primary sources, including visual
inspection of Zagier's printed pages 276--278. The completed Eisenstein
series has poles at both zero and one, with residues -1/2 and +1/2.
Cusp decay justifies the meromorphic period and unfolding.

The common factor is exactly

    A(s)=pi^(-s) Gamma(s) (4pi)^(-s-23) Gamma(s+23).

Consequently I=A zeta(2s)D and I(s)=I(1-s). A functional equation for D
alone is not asserted. The statement in Miller--Schmid's introduction that
mentions only s=1 cannot be used literally for their completed E_s:
the reflected pole at zero must be retained.

### 3. Canonical quotient and divisor

For Q=det I/I11 and F=D00-D01 D10/D11, one has
Q=A zeta(2s)F. Constant flag changes f0 -> f0+t f1, f1 -> c f1
act by Hermitian congruence; both the numerator determinant and denominator
entry acquire |c|^2. This proves flag invariance also for complex t,c.

For real sigma>1 the period is positive definite and Q is its strictly
positive minimum over ell(f)=1. This is a real variational interpretation,
not a holomorphic minimum operation at complex s.

With G the Petersson Gram, the residues of Q are
+det(G)/(2G11) at one and -det(G)/(2G11) at zero.
Away from these endpoints, additional poles can occur at zeros of I11.
In the real coefficient basis their exact local pole order is
max(ord(I11)-2ord(I01),0). The proof does not establish existence or
cancellation of additional poles.

Removing A does not add poles because 1/A is entire; subsequently
dividing by zeta(2s) may add poles. The completed quotient, L_Q and F
must not be assigned the same pole set without a separate cancellation
argument.

### 4. Genuine fixed-basis coupling

If a fixed invertible basis diagonalized the entire period family,
uniqueness of the coefficient Dirichlet series would force each Fourier
coefficient direction into one of two independent kernel lines.
The directions at n=1,2,3 are pairwise nonproportional, with minors
1, -48 and -195660. This rules out such a constant congruence.

It does not rule out parameter-dependent diagonalization, rational
expression in classical Rankin--Selberg entries, or every representation
of the resulting scalar.

### 5. Absolute fractional-frequency mechanism

The shear g=f0-696 f1 gives c2=0, c3=195660, while b1=0 and b2=1.
Thus the inverse denominator starts with 2^w, w=s+23; replacing D11
by a series beginning with one would change the answer.

The cusp coefficient bound, dominated convergence and geometric inverse
give an absolutely convergent generalized Dirichlet series on a genuine
right half-plane. Correction words have frequencies

    (nm/2) product_j (ell_j/2),  n,m,ell_j >=3.

Their minimum at inverse depth r is (9/2)(3/2)^r. This both proves local
finiteness of the infinite support and validates the bounded prefix
coverage. At 9/2 there is exactly one ordered word, with coefficient

    -(-48*195660)^2 = -88203653222400.

All smaller frequencies are integers. Multiplication by
zeta(2s)=sum_d d^46 (d^2)^(-w) leaves this coefficient unchanged.
Ordinary Dirichlet-series uniqueness therefore excludes an absolutely
convergent integer-indexed series for either F or L_Q on any right
half-plane. The ordinary-prime Euler-product exclusion requires normalized
local power series and an absolutely convergent expansion.

No generalized-prime, formal-product or conditional-product exclusion
is proved. No claim is made that arbitrary multiplication preserves the
same object or obstruction.

## Independent finite reproduction

The root replay passed:

- 30 tests in normal Python, 1.091 seconds;
- the same 30 under -O, 1.083 seconds;
- both producer checks;
- Ruff lint and formatting checks, and Git whitespace checks.

A separate implementation formed Delta=(E4^3-E6^2)/1728, rather than
using the producer's product/recurrence, through q order 40. It reproduced
all 24 fixture q rows and checked both T2 coefficient equations through
n=20 (40 equations). An independent recursive enumeration of ordered
frequency words reproduced the complete F and L_Q maps at twelve cutoffs:

    9/2, 5, 11/2, 6, 27/4, 7, 8, 9, 10, 81/8, 11, 12.

The separate reviewer also reconstructed all 24 rows without importing
producer mathematics and reproduced the four fixture cutoff maps, with
1, 3, 14 and 27 correction words. Its additional 24 in-memory
artifact/digest/source/type/cap tampering checks failed closed.
Its 30 normal/-O tests and both producer checks passed.

The producer reports 12,373 of 200,000 allowed work units. Its accounting
covers the declared bounded loop operations, not every interpreter
instruction. Public primitive caps, internal rational caps, container
sizes, and pre-expansion workload checks are explicit. Canonical JSON
comparison distinguishes booleans, integers, floats and string rationals;
duplicate keys and nonfinite JSON are rejected.

These computations check finite algebra and pinned context. They do not
machine-prove modularity, continuation, global series convergence, or the
analytic uniqueness argument. Remote primary-paper bytes are not bound by
the fixture.

## Primary-source boundary and disposition

The root inspected Miller--Schmid's introductory formulas (1.7)--(1.14),
Zagier's Eisenstein section 1(a)--(c), and the relevant modular-form
ring, Fourier, discriminant and Hecke pages. The PDF-reading workflow
was used to check obscured normalization and sign information, including
Zagier's discriminant identity. The separate reviewer independently
checked the cited primary formulas as well.

References remain at their exact locations in the
[proof note](RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md): the
[Miller--Schmid paper](https://arxiv.org/pdf/math/0605783),
[Zagier Eisenstein paper](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf),
and [Zagier modular-form chapter](https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf).
Schur and shorted-form constructions are classical; the quotient identities
here have a direct proof and do not depend on an uninspected operator theorem.

Accept this exact source as a meromorphic, source-specified global quotient
with an explicit loss of ordinary integer frequencies. Keep its frozen
PROPOSED header as historical evidence; this audit supplies the acceptance
disposition for the research branch. Further pole control, extensions to
other cusp flags, and any claims of external originality require new work
and, for new mathematics, a new identity and review.
