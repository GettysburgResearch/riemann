# Native phase leakage cancels with its full connection, before normal ordering

Status: proposed exact source-path theorem and rational replay; no RH claim.

Scope: the frozen Euler/half-divisor gauge homotopy, with literal input and
output labels retained, homotopy integration in its native Lebesgue measure,
and tau-independent physical observations and masks. This identifies the
missing source connection and core-activation terms in a concrete
selector-amplifying column. It does not equate the complete T-106140 balanced
family with an unprojected Euler homotopy derivative.

Exact sources: the producer authenticates L-102706, L-102746, L-106080,
L-106090, L-106120, L-106121, T-106140, and the frozen Euler-activation,
gauge-connection, and principal-selector notes. The primitive phase and
physical square insertion are inherited, not replaced by a scalar surrogate.

What was actually run: a bounded exact polynomial/beta-integral producer and
regression suite are supplied; the exact-SHA review records execution.

Smallest remaining gap: prove that the native balanced-owner family and its
literal paid diagonal retain the complete connection/core terms in the order
required below, or bound the explicit residual after that projection.

## 1. Exact decomposition of all phase-changing source terms

On a finite labelled physical horizon the frozen source identity is

\[
 H_\tau=G_\tau E_\tau,\qquad G_0=G_1=I,
 \qquad H_\tau'=G_\tau E_\tau'+G_\tau'E_\tau.                 \tag{1}
\]

For the bilateral source use the tensor product of the left and conjugate
right versions. Differentiation uses the product rule on both sides. The two
labelled copies of 67 remain separate; the concrete example below avoids 67.

Let P_alpha be the tau-independent diagonal projection selecting an input
physical record with its canonical least-discrepancy phase data. Let P_beta
select an output phase sector, including fixed owner-class slots if desired.
Physical outputs and common spectator labels remain in these blocks.
Mechanism and derivative-site labels are summand provenance for this
recombined output space, not distinct vector coordinates that could cancel
without being summed. Section 3 separately retains them as literal atoms and
records the nonzero diagonal that then survives.
For alpha != beta define

\[
 X_{\beta\alpha}(\tau)=P_\beta G_\tau P_\alpha E_\tau,
\]
\[
 L^{\rm tr}_{\beta\alpha}=P_\beta G_\tau P_\alpha E_\tau',
 \qquad
 L^{\rm con}_{\beta\alpha}=P_\beta G_\tau'P_\alpha E_\tau.     \tag{2}
\]

The output selector is recomputed on the actual physical output. In
particular (2) does not pretend that a newly common prime leaves the old
selector unchanged.

**PLC-1 (complete off-sector cancellation).** Coefficientwise in each
retained physical output,

\[
 L^{\rm tr}_{\beta\alpha}+L^{\rm con}_{\beta\alpha}
       =X_{\beta\alpha}',\qquad
 \int_0^1(L^{\rm tr}_{\beta\alpha}+L^{\rm con}_{\beta\alpha})d\tau=0.
                                                                  \tag{3}
\]

This holds for any differentiable finite source path E_tau, not just a
special coefficient. Indeed P_beta P_alpha=0 implies X(0)=X(1)=0 by (1), and
the product rule proves (3). It also holds for an individual nonidentity
physical shift inside a diagonal phase block, since that gauge coefficient
vanishes at both endpoints. Finiteness makes every rearrangement literal.

The equality survives any tau-independent linear source observation, fixed
input/output mask, common physical wavelet, or Mellin transform. It survives
the full principal weight when applied to the already cancelled output field:
the weight depends on the fixed output record, not on tau. It does **not**
bound the norms of the two separate summands in (3).

For an absolutely continuous scalar carrier density r(tau), the precise
replacement is

\[
 \int_0^1 r(\tau)(L^{\rm tr}+L^{\rm con})d\tau
       =-\int_0^1r'(\tau)X(\tau)d\tau.                       \tag{4}
\]

The endpoint term is zero. A bounded-variation density has the corresponding
Stieltjes formula. Likewise a tau-dependent projector or primitive phase
contributes its derivative. Thus the theorem never deletes an inherited
carrier measure or silently identifies the Duhamel parameter of L-102746
with this Euler homotopy parameter.

## 2. A source-native selector jump, including every term

Use the clean fixed owners and core labels from the frozen selector packet:

    P=11*13, Q=17*19,
    a=5*A*B, b=3*C*D,
    A=1009, B=1021, C=1201, D=1223.

Initially g=1, ell=5, rho=3. Inserting the native gauge square 3^2 on the left
gives

    a'=3*5*A*B, b'=b, g'=3, c'=5*A*B, d'=C*D,
    ell'=5, rho'=C, N'=9N, M'=M.

The source principal weights are exactly

\[
 w_0=45,\qquad w_1=(135/2)C c_C,\qquad c_C=(C+1)/(C-1).        \tag{5}
\]

Both physical pairs satisfy ratio-eight comparability, but are not in a
single unchanged width-eight shell. This example and the operator statement
use the finite global horizon/direct sum specified in the frozen packet.

Strip only the **common**, tau-independent primitive phase and native input
amplitude z_0=1/sqrt(NM). The selected bilateral Euler coefficient is

\[
 f(\tau)=\tau^4(1-\tau)^6,\qquad
 b(\tau)=-\tau(1-\tau)/12,                                  \tag{6}
\]

where b is the actual 3^2 gauge insertion coefficient. In the one-sided
N^(-it) convention its extra primitive phase is exp(-2i theta_3) and its
Mellin factor is 9^(-it). The conjugated-left convention of L-106120 conjugates
both factors. Whichever orientation is retained, the same factor multiplies
all three terms and is independent of tau; no phase is reset on the output.

There are four owner activations and six core activations in f'. Put

\[
 f'_{\rm own}=4\tau^3(1-\tau)^6,\qquad
 f'_{\rm core}=-6\tau^4(1-\tau)^5.
\]

**PLC-2 (exact three-term cancellation at the amplified output).** Writing
u=1/166320,

\[
 \left(\int_0^1bf'_{\rm own},\quad
       \int_0^1bf'_{\rm core},\quad
       \int_0^1b'f\right)
       =u(-14,15,-1).                                        \tag{7}
\]

Thus the transported full derivative contributes +u, the connection
contributes -u, and the complete observed leakage is zero at exactly the same
physical output. In particular the previous power-sized selector weight is
not a counterexample to the complete integrated connection current.

Proof. The three integrals are respectively

\[
 -\tfrac13 B(5,8)=-1/11880,\qquad
 \tfrac12 B(6,7)=1/11088,\qquad
 -\tfrac1{12}[B(5,7)-2B(6,7)]=-1/166320.
\]

Here B(j,k)=(j-1)!(k-1)!/(j+k-1)!; the producer also differentiates and
integrates the actual rational polynomials independently. Their sum is zero
because bf vanishes at both endpoints.

The cancellation is not stable under silently changing the homotopy measure.
For example the density r(tau)=tau gives the exact nonzero residual

\[
 \int_0^1\tau(bf)'d\tau=-\int_0^1bf\,d\tau
       ={1\over12}B(6,8)={1\over123552}.                      \tag{8}
\]

Equation (8) illustrates the correction in (4); it is not asserted to be a
native carrier choice.

## 3. Common observation and the surviving diagonal

All three entries in (7) have the same output N',M' and therefore the same
Mellin exponential. With the frozen |kappa-hat(t)|^2 measure, their integrated
Gram matrix is

\[
 \Gamma(0)\,w_1|z_0|^2 u^2\, vv^*,\qquad v=(-14,15,-1),       \tag{9}
\]

where Gamma(0)=(2pi)^(-1) integral |kappa-hat(t)|^2 dt. The primitive unit phase
also cancels from (9). The norm of the sum is zero, since sum v=0. The
individual diagonal is not zero.

If homotopy integration occurs first and the two mechanisms
(transported full derivative, connection) are retained as separate atoms,
their diagonal and centered scalar are

\[
 D_2=2u^2,\qquad |u-u|^2-D_2=-2u^2.                           \tag{10}
\]

For the three groups (7) the corresponding values are D_3=422u^2 and
-422u^2. For the four separate owner sites, six separate core sites, and one
connection site, the integrated coefficients in units of u are

    four copies of -7/2, six copies of +5/2, one copy of -1,

so D_11=(175/2)u^2. Each displayed diagonal must be multiplied by
Gamma(0) w_1 |z_0|^2 in the observed principal-weighted form.

These are different explicitly declared atom resolutions. If tau itself is
retained as a continuous primitive label, the diagonal instead integrates
the squared pointwise coefficients before collapsing tau; it is not any of
D_2,D_3,D_11. If all terms are recombined before atoms are declared, the zero
field has zero diagonal. No resolution is silently substituted for
T-106140's literal D_iota.

The exact centered-form correction from a fine partition to a coarse one is
the difference of their diagonals. Consequently a cancellation of the scalar
source field does not license erasing separately normal-ordered source atoms.

## 4. What this says about the actual remaining family gate

The frozen target takes complete Boolean, owner, carrier, shell, marked-67,
endpoint-colour and renewal data inside W_iota before the family square. It
then subtracts the literal D_iota in each character channel. Its phases come
from the actual output least reduced-core primes, as in (2).

At the primitive Euler gauge level, (3) now identifies every omitted
phase-changing connection term and proves its integrated cancellation with
transport. The concrete source column (7) additionally identifies its omitted
core-activation term. It is not left to an unspecified possible complement.

But the complete balanced-owner source in L-106080/T-106140 was obtained after
Boolean row resolution, completion, and transfers controlled in the frozen
unamplified observation. Three operations still need an explicit adapter:

1. Projecting to owner activation alone drops the six core terms in (7).
   Even adding the connection then gives -15u, not zero. Keeping transport
   without the connection gives +u, not zero.
2. A tau-dependent retained weight changes (3) by the explicit term (4).
   All actual carrier/probability/occupation measures must remain visible.
3. Squaring and subtracting a literal diagonal before the cancellation yields
   (10), not the zero recombined field. The native diagonal correction must
   be transported in the same resolution as the complete family.

Thus the selector obstruction and this cancellation are compatible: one rules
out a uniform bound on a source-blind transport column; the other repairs that
specific full source-path column with its required signed complement. Neither
proves a global principal or Kummer moment estimate. The next theorem must
identify the complete balanced-family adapter and its paid diagonal, not
repeat an endpoint identity or discard the connection again.
