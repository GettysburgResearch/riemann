# Chain-level continuation of the Segre--Chow synthesis

```text
Status: proposed theorem synthesis plus exact finite replays;
        independent mathematical/code review required.
Branch: research/gpt56-pro/20260831-segre-chow-equivariant-synthesis
Parent packet: PR #782, initial head 552fe0b78fd96b02fe5836269e6795a992c935be
Source heads retained:
  PR #766  17c7624a0bd56c5356d00278b2a846d2efdbdccc
  PR #769  f36576faf7853a56bd1f64edd29c4df662cae849
  PR #781  ea282c4e73ecd2d8cad44587da5ffa135df67e98
RH status: RH and GRH remain unproved; nothing here addresses either.
```

This continuation attacks the three principal targets deposited in the first
PR #782 packet. It does not modify any source branch or replace the exact
atlases that those branches proved.

## 1. Chain-level Segre--Chow result

For the ternary cube

\[
 V=\mathbf Q^3,\qquad W=\operatorname{Sym}^3V,\qquad
 E=V^{\otimes3}=W\oplus C,
\]

let

\[
 B_q=\operatorname{Tor}^{\operatorname{Sym}W}_q(R,\mathbf Q),
 \qquad
 R_r=(\operatorname{Sym}^rV)^{\otimes3}.
\]

The change-of-rings spectral sequence from `THEOREM_I.md` is the spectral
sequence of the literal two-block Koszul bicomplex

\[
 \Lambda^p C\otimes\Lambda^qW\otimes R.
\]

The new exact calculation proves

\[
 C\otimes B_{1,2}\longrightarrow B_{1,3}
\]

is surjective and that the first higher transgression

\[
 \boxed{
 d^2_{2,1,4}:E^2_{2,1,4}\longrightarrow E^2_{0,2,4}=B_{2,4}
 }
\]

has rank 65 and is surjective. Thus the complete 65-dimensional
Chow-base strand

\[
 B_{2,4}=[552]\otimes(\mathbf1+\sigma)
          +([642]+[543])\otimes\varepsilon
\]

does **not** survive to ambient Segre Tor. In particular the spectral
sequence does not degenerate at its `E2` page. This is the requested
chain-level no-go theorem against multiplying Chow Tor termwise by
\(\Lambda^\bullet C\).

The same page reconstructs the first two ambient dimensions from canonical
subquotients:

\[
 142+20=162
\]

ambient quadratic equations, and

\[
 1445+275=1720
\]

ambient cubic linear syzygies. These agree with the independently built
27-generator ambient maps in PR #766. The theorem and proof are in
`CHAIN_LEVEL_TERNARY_TRANSGRESSION.md`.

The replay constructs the orbit-sum inclusion, every displayed W-Koszul map,
the complement action, the horizontal homology and the zig-zag transgression
from scratch. It obtains the same rank profile modulo 65521 and 65537:

- `ternary_change_of_rings_replay.py`
- `ternary_change_of_rings_replay.json`

A nonzero modular minor is an exact certificate that the corresponding
integer minor is nonzero over \(\mathbf Q\). Characteristic-zero upper bounds
come from PR #769's already proved complete Chow-base Tor table; matching the
upper bound upgrades each certified lower bound to equality.

## 2. Full Frobenius/cycle-index alternant theorem

For a permutation \(\tau\in S_m\) with cycle lengths
\(\ell_1,\ldots,\ell_a\), the twisted trace is

\[
 \operatorname{Tr}\!\left((A,\tau)\mid
 (\operatorname{Sym}^rV)^{\otimes m}\right)
 =\prod_{\nu=1}^a h_r(A^{\ell_\nu}).
\]

Combining this tensor-cycle identity with the partial-fraction alternant of
T-108522 gives a closed numerator for **every conjugacy class**, and hence
by Frobenius characteristic and character orthogonality reconstructs the
full \(GL(V)\times S_m\) alternating Chow-Tor character.

This closes the all-\((d,m)\) theorem proposed in `THEOREM_II.md`; the exact
formula and proof are now in `FROBENIUS_CYCLE_INDEX_ALTERNANT.md`.

At \((d,m)=(3,3)\), an independent exact replay checks:

1. all three cycle numerators at four diagonal panels, including repeated
   and signed eigenvalues;
2. every coefficient against PR #769's complete
   \(GL_3\times S_3\) Tor table;
3. character inversion against the trivial, sign and standard isotypic
   Euler polynomials separately;
4. the explicit cycle alternant for all three conjugacy classes at the
   generic panel \((2,3,5)\).

Files:

- `cycle_index_alternant_replay.py`
- `cycle_index_alternant_replay.json`

The ordinary alternant remains only the identity-class trace. The twisted
cycle numerators are essential; no natural \(S_m\)-representation is inferred
from a scalar reciprocal factorization.

## 3. All-depth stable correction-head theorem

Let \(\operatorname{corr}_j\) be the stable weight-\(2j\) correction between
the square-defect coefficient and the Gauss-sign exterior-square term. The
new theorem gives the entire part containing an elementary factor of index
strictly larger than \(j\) by one generating identity:

\[
 \sum_{k=0}^{j-1}H_{j,k}t^k
 \equiv
 H_X(-t)\left(
 N_{2,X}(t^2)+(-1)^{j(j+1)/2}D_{\wedge^2X}(t^2)
 \right)\pmod{t^j}.
\]

Here

\[
 \operatorname{corr}_j
 =\sum_{k=0}^{j-1}e_{2j-k}H_{j,k}
  +\text{terms with every elementary index at most }j.
\]

Consequently the coefficient of \(e_{2j}\) is

\[
 1+(-1)^{j(j+1)/2}.
\]

The linear head therefore has period four:

- present for \(j\equiv0,3\pmod4\);
- absent for \(j\equiv1,2\pmod4\).

The disappearances at depths 5 and 6 are real, but they are not permanent:
the linear head provably returns at depths 7 and 8. Thus any extrapolation
that the linear layer has structurally terminated forever is false.

`STABLE_LAYER_HEAD_THEOREM.md` proves the formula by infinitesimal
linearization of the elementary/power-sum relation and the plethystic power
sums of \(\operatorname{Sym}^2X\) and \(\Lambda^2X\).
`stable_layer_head_replay.py` verifies the resulting head term-by-term against
the committed depth-3,4,5,6 dictionaries and records the exact depth-7,8
predictions.

## 4. Canonical top relation: exact endpoint and remaining finite comparison

The first packet proved that the degree-seven quotient class is the unique
\([777]\otimes\mathbf1\) top Tor line and that the invariant top differential
is dual to the ternary-cubic Hessian component. The continuation makes the
canonicalization procedure completely explicit:

\[
 L_{\mathrm{can}}=
 \ker D_2\cap K_{(7,7,7)}
 \cap\ker E_{12}\cap\ker E_{21}
 \cap\ker E_{23}\cap\ker E_{32}
 \cap K^{S_3}.
\]

This line is one-dimensional. Its saturated integral lattice has a unique
primitive generator up to sign; a descriptor-order sign convention makes it
literal. Any accepted marked witness decomposes uniquely as

\[
 w=\alpha w_{\mathrm{can}}+w_{\mathrm{old}},\qquad \alpha\ne0.
\]

The theorem and an exact comparison contract are in
`CANONICAL_TOP_PROJECTION.md`.

This pass does **not** claim that the published 379-term vector is already the
primitive canonical generator. Performing that last coefficientwise
projection requires the marked Lie-action matrices on the degree-seven
source coordinates. The branch currently authenticates the kernel vector,
old-space obstruction and quotient class, but does not contain those action
matrices in an accepted executable contract.

## 5. Corrections and scope

- The change-of-rings spectral sequence is now proved nondegenerate at `E2`
  in the ternary cube.
- The scalar alternant is insufficient for factor-permutation types; the
  cycle-index refinement is the exact repair.
- The depth-5/6 failure of the simple correction law is not permanent
  termination; the large-part head is period four.
- The 379-term quotient class is canonical, while its literal marked lift
  still requires the explicit projection comparison.
- No additive Euler character is promoted to a superdeterminant.
- No local rationality or finite syzygy geometry is promoted to automorphy,
  analytic continuation, RH or GRH.

## 6. Ranked continuation after this pass

1. Compute the full ternary change-of-rings spectral sequence by internal
   degree, beginning with the transgression into \(B_{3,5}\) and the incoming
   differential controlling \(E^2_{1,1,4}\).
2. Decompose the rank-65 transgression representation-equivariantly, not only
   by total rank; the target table predicts its exact three isotypic pieces.
3. Add the marked \(\mathfrak{sl}_3\) and factor-permutation actions to the
   top-witness artifact and execute the canonical projection contract.
4. Expand the stable-head generating identity beyond `k=4`; it is recursive
   in shallower square-defect coefficients and should expose the complete
   partition-lattice law.
5. Extend the cycle-index replay to \(m=4\) and use all five conjugacy classes
   to predict the first uncomputed \(GL(V)\times S_4\) Chow-Tor character.
