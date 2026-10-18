# Degree26 exact original-theta realization on a connected tree

**Status: PROPOSED computer-assisted finite theorem.** A complete directed
contraction certificate proves a307-vertex,306-edge, strictly positive
ferromagnetic tree matching the original standardized theta moments
through degree26. This is separate from the root track's307-edge cycle
realization at the same degree. Neither finite result supplies a
growth-controlled cofinal construction, a new zeta zero-free region or RH.

## 1. The graph and complete conditional formula

Start with the degree24 multiplicities, weights and notation in
PROOF24.md. Keep counts `[2,10]+[1]*15+[127]`, giving306 observed spins
and one zero-weight hub. Select the root spins of the unique dimers of
types2 and3. Remove type3's edge to the hub and connect its root directly
to type2's root by a positive edge of bias r. The graph remains connected
and has306 edges, so it is a tree. Every other hub edge has bias
eta=10^(-10), and all internal dimer biases are 2p_i-1.

For the selected dimer i define the zero-hub conditional vectors

\[
 M_i(n)=1_{n\text{ even}}[p_iA_i^n+(1-p_i)B_i^n],\qquad
 T_i(n)=1_{n\text{ odd}}[p_iA_i^n+(1-p_i)B_i^n].
\]

The n=0 entries are M_i(0)=1,T_i(0)=0. Write raw convolution
`(U*V)(n)=sum_(k=0)^n binom(n,k)U(k)V(n-k)`. For the root-root merge,
the complete cluster moments conditional on a positive hub are

\[
 \mu_{23}(n)=
 \begin{cases}
 (M_2*M_3)(n)+r(T_2*T_3)(n),&n\text{ even},\\
 \eta[(T_2*M_3)(n)+r(M_2*T_3)(n)],&n\text{ odd}.
 \end{cases} \tag{1}
\]

This comes directly from the complete selected-cluster spin factor
`(1+eta sigma_(root2))(1+r sigma_(root2)sigma_(root3))`, together
with both internal dimer factors. Its total mass is exactly one;
no cyclic partition quotient or approximation is used. merge_model.py
also implements root-child and child-child choices, checked separately
on miniature graphs, but the theorem uses only (1).

Convert (1) to conditional cumulants; replace the two old component
cumulants by this cluster cumulant and retain every other multiplicity.
Convert the resulting total cumulants to conditional raw moments,
symmetrize the hub by setting odd moments to zero, then convert to
unconditional cumulants. The target equations are the thirteen even
cumulant ratios through26 of the complete original standardized theta law.
These equations are triangularly equivalent to all raw moment equalities
through26, since the zeroth moment is1 and all odd moments are zero.

## 2. Full-source, whole-cube existence proof

parameters26_merge.json gives the exact finite decimal/rational center,
the fixed rational13-by13 preconditioner R, and radius10^(-30).
The active coordinates are

```text
[6,51,15,21,3,27,48,9,12,5,18,53,54].
```

The center merge bias is
`r=0.06364023671573725472484278221667431505213872194482276738756...`.
These displayed digits are descriptive; the complete finite rational
value in the parameter file is used.

certify_merge.py independently reconstructs the target from the pinned
320-bit outward integer backend, six explicit theta indices, every
selected time cell and the full Taylor/time/omitted-index remainders.
No saved target midpoint, numerical zero or solver residual is trusted.
For F=the complete model-minus-actual-target equations, it proves

\[
 \beta=\|RF(c)\|_\infty<6.171\cdot10^{-33},\qquad
 L=\sup_C\|I-RDF\|_\infty<0.000513,
\]
\[
 r_C=10^{-30},\qquad \beta+Lr_C<0.01r_C<r_C. \tag{2}
\]

The checker uses the stricter explicit guards L<.001, beta<r_C/100
and r_C-beta-Lr_C>.99r_C. The fixed map x -> x-RF(x) is consequently
a strict contraction of the whole closed cube into itself. Since
`||I-RDF(c)||<1`, the square matrix RDF(c) is invertible, which also
proves R invertible. Banach therefore gives an exact root of F, not
merely a root of preconditioned equations or a midpoint approximation.

All physical observable weights `(A_i+B_i)/2,(A_i-B_i)/2` remain strictly
positive throughout the cube. Every edge bias stays in
`(10^(-11),1-10^(-9))`, and total support is below12. Thus the exact
root is a finite positive ferromagnet of the claimed graph. The standard
finite weighted Lee--Yang theorem gives real Fourier zeros. Its
zero-weight hub is treated by positive-weight approximation and Hurwitz,
exactly as in PROOF22.md.

## 3. Executed replay and independent assembly controls

```text
python -O standalone/2026-10-18-three-direction-sprint/theta/certify_merge.py --parameters standalone/2026-10-18-three-direction-sprint/theta/parameters26_merge.json --check standalone/2026-10-18-three-direction-sprint/theta/certificate26_merge.json
```

Fresh optimized replay passed in9.0 seconds, recomputing the full source
and cube, with

```text
beta = 6.170153825140304e-33
L    = 0.0005124538802249338
canonical JSON-LF SHA256 = e7c6ca12f4cf203385290dd4c88edea9431de2cadabbd4a657f60d0c928c1b8f
actual Windows file-byte SHA256 = 084008bca3ca2b45e2ab24d6a2e8333fdfffd276196598d71a488efcb50ac8bf
```

The initial emission had already passed. File input hashes inside the
certificate always refer to actual input bytes; the two displayed output
hash conventions are explicitly distinguished.

merge_controls.py independently enumerates eight complete six-vertex
miniatures,64 spin configurations each, checking all raw orders0..26,
every explicit graph derivative against AD, both different-type and
same-type-copy merges, and all root/child endpoint choices.

merge_integer_controls.py separately reconstructs **all307 vertices**
with exact scaled-integer raw exponential-generating-series multiplication.
It explicitly enumerates the selected cluster's physical spins and edge
factors, removes the right hub attachment, verifies normalization exactly,
and compares every even raw order0..26 against the directed model interval.
It uses neither the conditional cumulant recurrence nor the merged formula
(1) as its reference assembly. Its optimized run passed in1.657 seconds;
receipt canonical SHA256
`c573e2dfad4515526aaa8bf22e687ecb8e941ac9d178fd106b692393cf0ade89`.

The root track's cyclic26 witness was independently replayed and checked
with cycle_independent_controls.py and cycle_parameter_controls.py;
those receipts concern the distinct307-edge graph, not this tree.

The initial merged-edge tangent search was exploratory. Its candidate
selection does not enter the existence proof. On the user's later
instruction, all higher-order finite fitting was stopped in favor of
the cofinal construction, compactness and obstruction results in this
directory.
