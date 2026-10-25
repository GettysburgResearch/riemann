# Independent review of the projected affine operator calculation

Reviewer: native_gain agent. Author: two_sign_hlc agent.

**Verdict: pass at the stated finite-operator and local-obstruction
scope.** The fixed-projector variance identity is exact. The conditioned
fixed-line incidence is an isometry and has the stated compressed norm
lower bounds. The explicit test pair and the varying-projector error
inequality are correct. The source-specific Fock interpretation is
properly restricted to an existing recorded coordinate.

This review does not certify a lower bound for the full HLC dirty sum,
an actual Möbius counterexample, the complete external HLC proof, or a
new native inverse estimate. In particular, the source's major-arc
comparison is not identified with a constant projection without the
additional comparison estimate required in equation (2).

## Exact reviewed bytes and source checks

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `PROJECTED_AFFINE_OPERATOR.md` | 13,149 | `1ab0c4c72f203921a63714c59f15f49b26839b93ff0f1962fedef9294e94d2ad` | `963ae27dec0f02d3df011fed12ea29e49eea6126` |
| `check_projected_affine_operator.py` | 6,662 | `0c2ed2324da70591db54af16a9a176c6805310a3e325699a88c4e87d51a96749` | `f0d9d5abfcd197bda5c35cd5b22d07c6dd009d63` |

These are local byte authentications, not remote-publication claims.
The final accepted text explicitly uses p at least 3 for the local
mean-zero isometry statement. For p=2 the target has only one point,
so that mean-zero subspace is zero-dimensional. The HLC application
uses large primes and is unaffected by the qualification.

I independently read the source's Section 4.4, including its state
measure and transfer rules on pp. 26--27, the parametrization (4.40),
and the dirty equation (4.47) and its subsequent selection argument
on pp. 30--31. The local PDF of
[Lü--Wang--Wu, arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242)
has 734,761 bytes and SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.

For the supplementary twisted-sum input I verified the statement of
Theorem 4 in Keith Conrad's author-hosted
[On Weil's proof of the bound for Kloosterman sums](https://kconrad.math.uconn.edu/articles/kloosterman.pdf).
It gives the stated bound for nontrivial multiplicative twists; the
ordinary Kloosterman bound covers the trivial twist. The Gauss and
geometric degeneracies used in the note were checked separately below.
This external character-sum theorem is an imported input for the
supplementary example, not for the finite identities (1)--(8).

## 1. Fixed projectors and correct centering

Multiplication by an indicator is self-adjoint. Hence

\[
 \langle f,P(U_{q,h}-J)Qg\rangle
       =\langle\Pi Pf,U_{q,h}\Pi Qg\rangle.
\]

Let u and v denote these two mean-zero vectors. For uniform affine
parameters, the pair \((qx+h,qy+h)\) is uniform over all ordered
distinct field points whenever x differs from y. Consequently

\[
 \mathbb E[ v(qx+h)\overline{v(qy+h)}]
 =\begin{cases}
   \|v\|_2^2,&x=y,\\
   -\|v\|_2^2/(p-1),&x\ne y.
  \end{cases}
\]

Expanding the pairing with normalized counting measure proves exactly
\(\|u\|_2^2\|v\|_2^2/(p-1)\). This also checks the complex-valued
case, beyond the checker's real rational examples.

The omitted uncentered term is exactly
\(|\mathbb E(Pf)|^2|\mathbb E(Qg)|^2\). Mean-zero f or g need not
remain mean zero after projection. The note correctly retains P J Q
and does not use that observation to reject the centered identity.

Conditioning on another label is valid only if the affine law remains
uniform and both projected vectors are fixed after that conditioning.
A density bounded by C gives the stated C multiplier for the squared
upper bound. None of these hypotheses follows from the dirty-edge
record alone. The comparison-error inequality (2) is ordinary
Minkowski followed by the operator-norm estimate, with the projectors
kept inside the difference operator.

## 2. The actual local dirty condition and its normalization

The source records an incoming pair \((p,\ell)\). Its raw determinant
is \(P_{\rm full}-DpZT_f\), so it equals the nonzero
\(P_{\rm full}\) modulo p. The target remains on the recorded line.
For fixed complete outgoing labels this gives exactly the condition
used in the note, with c fixed and nonzero.

Writing \(z'=tv\) forces \(t=c/\det(z,v)\). Each nonzero t has
exactly p source preimages, since the determinant with v is a nonzero
linear functional. There are p(p-1) source points and p-1 target
points. Therefore pullback preserves both the mean and the normalized
L2 norm. On the nonzero mean-zero target space it has norm one;
subtracting the constant operator changes nothing on that subspace.

These are probability normalizations for the local channel. They are
not the state measure of the entire integer operator. The note
explicitly retains that distinction and does not derive a full
arithmetic lower bound from the local norm.

## 3. Compressed incidence with arbitrary endpoint indicators

For a retained source set A, the fraction of the p-point fibre over
y that remains is r_y. The normalized adjoint gives

\[
             T^*PT=\operatorname{diag}(r_y),
       \qquad (PTQ)^*(PTQ)=Q\operatorname{diag}(r_y)Q.
\]

The squared norm is consequently the largest r_y over the retained
target set B. Moreover the sum of all missing fibre fractions is
\((p-1)\delta_X\), so their average over B is at most
\(\delta_X/\alpha_Y\). This proves equation (7).

If B contains at least two points, the difference of the two largest
fibre indicators is mean zero and supported in B. Its Rayleigh
quotient is the average of those two r_y values, which is at least
the average on B. The same lower bound therefore holds for the
restricted centered operator in (8).

No factorization assumption about the original integer good-state
projector is introduced by this argument. Nor can an unconditional
exceptional measure be used as the conditional delta_X or delta_Y
without a separate argument. The note states both limits.

## 4. Fock weights do not supply a new line draw at this transfer

I checked the source's measure \(\lambda_i(p,\ell)=\nu_i(p)\),
the factorial weight on recorded tuples, and its rule that an incoming
recorded pair must have been present before the edge operation.
Moving that fixed coordinate into an active list does not introduce
a second independently averaged line. The earlier line-selection
factor cannot be charged again at every such transfer.

This leaves the actual source coefficients, including its 1/V_i
transfer factor, damping, list symmetrization, prime measures,
archimedean restrictions and coherent raw-minus-comparison sum.
They are not replaced by one in the note's conclusion. In particular,
the local lower bound is not a lower bound for the whole weighted
dirty operator, and does not conflict with the source's separate
good-state/list-selection estimate.

## 5. The explicit test pair and its cancellation scope

For k nonzero modulo p, the additive phase has mean
\(-1/(p-1)\) over the nonzero residues. The chosen affine
correction therefore makes g mean zero. Direct expansion gives

\[
                    \|g\|_2^2=1-2/p,\qquad |g|\le1.
\]

The pullback f has the same properties. The projected uncentered
pairing is an average of
\(1_A(z)1_B(\phi(z))|f(z)|^2\). Its lost mass is at most
\(\delta_X+\delta_Y\). The two remaining means are bounded by
\(\delta_X\) and \(\delta_Y\), so the centered correction costs
at most their product. This proves equation (10), including its
sign and its last term.

For the reciprocal phase, additive completion reduces every Fourier
coefficient to a twisted Kloosterman sum, with a Gauss sum or a
bounded degenerate sum when its linear coefficient is zero. The
interval Fourier L1 cost is O(log p). For the target additive phase,
nonprincipal twists are Gauss sums after completion; the principal
twist is a geometric progression. The choice
\(k=\lfloor\sqrt p\rfloor\) gives the stated O(sqrt(p)) geometric
bound. The constant correction contributes at most one.

For an ordinary Dirichlet character modulo q below p/(2k), splitting
an interval into q progressions is legitimate. The target progression
has phase increment kq/p, between zero and one half, so each sum is
O(p/(kq)) and all q classes cost O(p/k). Completing the reciprocal
phase in each progression gives O(sqrt(p) log p) per class, because
q is invertible modulo p. Summing gives the stated
O(q sqrt(p) log p), and hence O(p^(5/8) log p) for q at most p^(1/8).

These are finite-array, single-scale cancellation properties. They
are not uniform prefix estimates at every smaller scale, a global
multiplicative sequence, or a Möbius example. The note does not use
them as such. Their role is to show that these particular
one-variable tests coexist with a constant-size fixed-incidence
pairing.

## 6. Varying projectors and the actual remaining input

For each uniformly distributed affine parameter, the decomposition
in Section 5 of the note is exact. The first error pairing is at
most \(2d_P\|f\|_\infty\|g\|_\infty\), because
\(\|KQg\|_\infty\le2\|g\|_\infty\). For the second,
move the permutation to the first vector; its permutation and
constant parts each cost at most
\(d_Q\|f\|_\infty\|g\|_\infty\).

Taking the root mean square and adding the correctly centered
unprojected variance proves (12). The error is an explicit
exceptional-mass term, not permission to drop the projectors.

The remaining HLC application would need a conditional averaging
law and its true comparison error after the complete labels are
fixed, or cancellation in the coherent sum of labels and arithmetic
coefficients. The local deterministic channel does not provide
that law. Neither this review nor the note supplies the additional
estimate.

## 7. Checker replay and verdict limits

I ran the checker with `python -O`. It passed:

- 80 exact fixed-projector affine identities;
- 334 varying-projector error cases;
- 2,988 dirty determinant and line constraints;
- 504 compressed Gram cases;
- 480 mean-zero compressed lower bounds;
- the negative control that omits the centered comparison.

The rational examples exercise the normalizations and finite
identities. They do not prove a theorem for all primes by exhaustive
computation. The general arguments above supply that reasoning;
the supplementary Kloosterman bound remains an external theorem.
No full HLC dirty-edge estimate, Möbius correlation, or zero-free
improvement is certified here.
