# Degree24 source-faithful connected ferromagnetic realization

**Status: PROPOSED computer-assisted finite theorem.** A fresh directed
certificate passes for the original complete standardized theta moments
through degree24. This improves the degree22 finite achievement in
PROOF22.md. Cofinal feasibility, an unbounded-order construction, RH and
any improved global zeta zero-free boundary remain unproved.

## 1. The graph and its legal change of architecture

Use exactly the hub-and-dimer model and the original theta law defined in
PROOF22.md. The complete multiplicity list is now

```text
[2,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,127].
```

Thus there are2 single observed spins,152 dimers,306 observed spins, one
zero-observable-weight hub, and307 vertices altogether. There are154 hub
edges and152 internal dimer edges, hence306 edges: the graph is a
connected tree. Every observed spin has a strictly positive observable
weight, and every edge has a finite strictly positive ferromagnetic
coupling.

The useful new move replaces254 of the old256 independent fair spins by
127 equal-weight dimers. At internal alignment probability `p=1/2`,
one such dimer has coordinates `(A,B)=(2a,0)` and characteristic function

\[
 \frac{1+\cos(2az)}2=\cos(az)^2.
\]

It is exactly two independent fair spins of weight`a`, at every order.
Turning their common coupling positive opens an additional legal direction
without adding vertices. A lower-degree moment continuation was used only
to find a candidate; the existence proof below does not trust the
continuation or any saved solver residual.

In the original model notation the physical weights of dimer type`i` are
`(A_i+B_i)/2` and `(A_i-B_i)/2`, and its internal edge bias is
`q_i=2p_i-1`. Every root is attached to the hub with bias
`eta=10^(-10)`. The exact rational center and the whole active cube are
given in parameters24_bulk_preconditioned.json. The twelve active
coordinates are

```text
[6,51,15,21,3,27,48,9,12,5,18,53].
```

Every other coordinate is fixed. The cube radius is `10^(-30)`.

## 2. Complete moment equations and source

Condition on the hub spin being positive. Each fair block has raw moment
`A_0^n` for even`n` and `eta A_0^n` for odd`n`; each dimer has

\[
 [p_iA_i^n+(1-p_i)B_i^n]
 \begin{cases}1&n\text{ even},\\ \eta&n\text{ odd}.\end{cases}
\]

Independent conditional blocks add cumulants with their full
multiplicities. Convert the total conditional cumulants back to moments
and symmetrize over the fair hub, which sets odd raw moments to zero.
Finally convert to unconditional cumulants. These finite polynomial
operations are implemented in the unchanged model.py.

The target is the actual standardized theta law, with normalization and
variance reconstructed from the complete original theta density. The
fresh computation uses the same pinned320-bit outward-integer backend,
six explicit theta indices,98 cells and Taylor degree120 as PROOF22.md,
with all even source orders0,...,24. Every cell error, each full time
tail and all omitted indices are retained using the explicit bounds in
that proof. Extending the finite moment list does not truncate any source
tail; source_extended.py records each complete remainder separately.

Let `F:C->R^12` be the twelve normalized cumulant residuals, for orders
2,4,...,24, against this exact standardized theta source. Their vanishing
is equivalent to matching all raw moments through24 by the triangular
moment/cumulant identities and symmetry.

## 3. A fixed rational preconditioner is sufficient

The certificate contains a fixed rational12-by12 matrix`R`, selected by a
non-directed decimal producer. Its selection is not an acceptance premise.
The checker evaluates, with outward intervals,

\[
 \beta=\|R F(c)\|_\infty,
 \qquad L=\sup_{x\in C}\|I-R DF(x)\|_\infty.
\]

It proves

\[
 \beta<3.439\cdot10^{-35},\qquad
 L<2.109\cdot10^{-6},\qquad
 r=10^{-30},\qquad \beta+Lr<r.
\]

No floating inverse and no asserted equality `R=DF(c)^(-1)` is used in
these bounds. In fact `L<1` implies `R DF(c)` is invertible by the Neumann
series. Since the matrices are square, `R` itself is therefore invertible.
This independently checks the needed invertibility using the same whole
cube interval computation.

The map `T(x)=x-R F(x)` maps the cube strictly into itself and has
Lipschitz constant at most`L<1`. Banach's theorem supplies its unique fixed
point in the cube. At that point `R F(x)=0`; invertibility of`R` then gives
`F(x)=0`. This proves existence of an exact root for the complete original
theta target, rather than merely an approximate match to source
midpoints.

Whole-cube checks prove `A_i>|B_i|`, `1/2<p_i<1`, every edge bias in
`(10^(-11),1-10^(-9))`, and total observable support less than12. Hence
every point of the cube, including the exact fixed point, defines the
stated connected positive ferromagnet. The standard finite weighted
Lee--Yang theorem then gives real Fourier zeros, with the zero-weight hub
handled by the positive-weight approximation/Hurwitz argument from
PROOF22.md. This imports precisely the same classical theorem, with no
new claim of spectral identification with zeta zeros.

## 4. Executed certificate

```text
python standalone/2026-10-18-three-direction-sprint/theta/certify_tree_preconditioned.py --parameters standalone/2026-10-18-three-direction-sprint/theta/parameters24_bulk_preconditioned.json --emit standalone/2026-10-18-three-direction-sprint/theta/certificate24_bulk_preconditioned.json
```

The run completed successfully in44.8201 seconds with

```text
beta = 3.4380552475739557e-35
L    = 2.1082887951034925e-6
canonical JSON with one LF newline SHA256 = d1e8d8d1a0e0ff36d91289be9f9bb70d28e76776c13ed69f478a2343c9b054e5
```

The actual Windows CRLF file-byte SHA256 is
`3884ea2879f60da2f72cd5c93a67842e240f3e23ff696e20ed2e076c82be185f`.
The two identities describe serialization conventions, not different
certificate contents. All `input_hashes` inside the certificate hash actual
input file bytes.

Replace `--emit` by `--check` with the same certificate path to reconstruct
the entire source and cube bounds afresh and require exact JSON equality.
The verifier uses only the Python standard library. Its finite
preconditioner is exact decimal/rational data; SciPy, floating arithmetic,
saved targets and old certificates are not proof dependencies.

finite_tree_controls.py separately compares all raw orders0,...,24
between the cumulant assembly and direct multiplication of complete
conditional raw exponential generating series, checks an independently
enumerated128-configuration miniature graph, and verifies the exact
bulk-promotion boundary identity. Those assembly checks complement the
root certificate; they do not replace it.
