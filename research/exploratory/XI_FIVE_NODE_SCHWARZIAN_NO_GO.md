# Why the paired Schwarzian signs stop at four nodes

Status: proposed exact no-go/countermodel; preregistered after one explicitly
disclosed discovery scout and before the held-out panel.
Scope: abstract smooth safe-axis functions. This is not an actual-xi
counterexample and makes no inference about the five-node xi matrix.

Authoring parent: `b7112aa9c8c96aae60e8d0a8ad9fe3b36ffc88ea`.
The exact four-node identity and literal source theorem are in SP/FR.

## 1. Disclosure and fixed design

Before this preregistration, one scratch exact search was run while approval
was in flight. It used x=(1,2,3,4,5), the two-atom function

\[
 p_0(t)=\frac2{t+1}+\frac4{t+4},                    \tag{FN1}
\]

and changed only p(1) to p_0(1)-1/100. It found all proper principal
minors positive and the five-by-five determinant negative. This row is
retained as DISCOVERY, never relabeled as prospective or held out. A second
scratch calculation, also before preregistration, recovered the exact
quadratic determinant along this perturbation. Both are reported in full.

The post-preregistration finite design is now fixed:

1. Rebuild the discovery cell and its exact determinant polynomial by
   permutation and elimination routes.
2. HELDOUT-A: same base/nodes, epsilon=1/1,000,000.
3. HELDOUT-B: x=(1,2,4,6,9), atoms (2,3),(7,5), decrease only p(1) by
   1/100,000. Retain every proper-minor and determinant sign, even failure.
4. HELDOUT-C: same as B, increase only p(16) by 1/100,000. Retain all signs.
5. For both bases and every one-coordinate direction, reconstruct the
   degree-at-most-two determinant polynomial from epsilon=0,1,2 and verify
   it at epsilon=-2,-1,1/10, with no selection by favorable sign.
6. Verify the five-node Schur residual by both inverse-free adjugate and
   full-determinant routes; include singular-anchor and swapped-orientation
   hostile controls.

Only exact rational arithmetic is permitted. No xi evaluation, zeros,
floating-point scan, panel movement or precision escalation is allowed.

## 2. Exact order-five residual

For distinct positive x_i, t_i=x_i^2 and real values p_i, set

\[
 H_{ij}=\frac{x_ip_i+x_jp_j}{x_i+x_j}.               \tag{FN2}
\]

Let M=H[1,2,3,4], h=H[1,2,3,4;5], d=det M, and

\[
 c=(-\operatorname{adj}(M)h,d)^T.                   \tag{FN3}
\]

Without assuming M invertible,

\[
 \boxed{\quad c^THc=d\det H.\quad}                  \tag{FN4}
\]

This follows from M adj(M)=dI by direct block multiplication. If d>0,
the normalized new invariant is the Schur residual

\[
 R_5=H_{55}-h^TM^{-1}h=\det H/d.                    \tag{FN5}
\]

Thus order five adds one exact scalar after a strict four-node anchor.
It is not one of SP's two four-point cross-ratio factors.

Holding all p_j except p_k fixed makes H an affine rank-at-most-two update,
so det H is a polynomial of degree at most two in p_k. This is also clear
by multilinearity: p_k occurs only in row k and column k, with their shared
diagonal counted once. Three exact evaluations reconstruct the polynomial;
additional values are genuinely independent checks.

## 3. The discovery polynomial

For FN1 at x=(1,2,3,4,5), put p_epsilon(1)=p_0(1)-epsilon and leave the
other four sampled values unchanged. Exact expansion gives

\[
 \det H(\epsilon)=
 -\frac{243}{2169288277812500}\epsilon
 -\frac{483}{533978653000000}\epsilon^2.             \tag{FN6}
\]

The other root is -1296/10465. Hence det H(epsilon)<0 for EVERY epsilon>0,
not only for the discovered 1/100. At epsilon=1/100 the exact value is

\[
 -\frac{84039}{69417224890000000000}.                \tag{FN7}
\]

At epsilon=0 the kernel has four real Gram features (two per atom), rank
four, and every proper principal minor is strictly positive. Openness
therefore leaves every proper principal minor positive for all sufficiently
small positive epsilon. FN6 simultaneously makes the full determinant
negative. This already proves a finite-data separation between all
order-at-most-four signs and order five.

### Held-out outcome

The panel fixed in section 1 was then run without alteration. Every proper
principal minor was positive in all three held-out cells. HELDOUT-A gave

\[
 -\frac{777606279}{6941722489000000000000000000}<0,
\]

and the independent atoms/nodes of HELDOUT-B gave

\[
 -\frac{2126823001}{35614488430668169000000000}<0.
\]

HELDOUT-C, the predeclared opposite-coordinate increase, instead gave

\[
 \frac{133394400643}{14003428343249488000000000}>0.
\]

The positive C outcome is retained: the fifth residual is oriented and is
not forced negative by every departure from a rank-four Stieltjes model.
Across both bases, all ten coordinate perturbation determinants were exact
quadratics and all six post-reconstruction evaluations agreed.

## 4. A global smooth paired-Schwarzian countermodel

The finite values can be realized without sacrificing the entire scalar
package that proves order four. For the real two-atom p_0:

- p_0>0 and p_0'<0;
- (t p_0)'>0;
- (1/p_0)''<0 and (t p_0)''<0;
- S p_0>0 and S(t p_0)>0.

The strict assertions follow either directly or from the real-pole
dispersion identities, with two distinct atoms. Choose a C-infinity bump
psi supported in a compact neighborhood of t=1 that contains none of
4,9,16,25, and with psi(1)=1. Put

\[
                    p_\epsilon=p_0-\epsilon\psi.     \tag{FN8}
\]

On the compact support, every displayed strict inequality has a positive
margin after clearing its nonzero derivative denominators. C3-continuity
therefore preserves all of them for every sufficiently small epsilon>0.
Outside the support the function is unchanged. Choose a positive rational
epsilon below this existence threshold. Its five sampled values are exactly
those of FN6, so det H<0, while all matrices of order at most three are PD
by the scalar order-three factorization and every order-four determinant is
positive by the paired-Schwarzian four-point theorem. Consequently every
proper principal minor of this five-node H is positive, yet det H<0.

This proves:

\[
 \boxed{\text{The two positive Schwarzian signs, even with the complete
 lower-order scalar package, do not imply order-five positivity.}}       \tag{FN9}
\]

No explicit numerical bump threshold is needed: FN6 has the required sign
for all positive epsilon, while the preservation claim is the elementary
openness of finitely many strict C3 inequalities on a compact set. The bump
is an abstract countermodel, not a Stieltjes transform, completed xi, or
source-polarized arithmetic kernel.

## 5. Exact next burden and boundaries

For actual xi, FR closes the previously open order-four level. FN4 says the
next exact target is R_5>=0 for every safe five-node packet. FN9 proves that
no argument using only the already established monotonicity, concavity and
paired Schwarzian signs can close it. A new fifth-order source/zero
inequality, or a direct sign theorem for FN4, is necessary.

This packet does not claim that actual xi has a negative five-node packet,
that a sampled positive packet is evidence for RH, or that order five is the
only remaining all-order difficulty. It supplies a sharp logical boundary
and a source-independent residual. No novelty comparison is asserted.
