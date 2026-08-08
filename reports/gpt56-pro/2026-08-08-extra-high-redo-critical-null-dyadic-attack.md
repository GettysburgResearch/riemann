# Extra-high redo: critical-mode firewall and a source-complete dyadic attack

Agent: `gpt56-pro-xhigh`  
Date: 2026-08-08  
Base: PR #322 at `72d68a043a008209455375b720cd107a436e7f32`  
Status: **NEW EXACT THEOREMS AND SCOPE CORRECTIONS; RH UNPROVEN**

## 0. Why this redo exists

The previous fast pass after PR #305 was not adequate for the user's request.  In particular, its proposed "Arithmetic Conservation Law Program" was a research sketch, not a proved identity, and it was not a reviewable unconditional RH proposal.  This pass does not preserve that wording as a mathematical result.

The extra-high redo re-entered the live repository, incorporated work through PR #323, reconstructed the load-bearing source modes, proved new exact lemmas, and corrected two normalization errors discovered during its own development before freezing this packet.

The standard applied here is:

```text
reviewers review supplied proofs;
reviewers are not asked to construct a missing theorem;
false statements are marked false only after an exact contradiction;
open RH-bearing estimates remain explicitly UNPROVEN.
```

## 1. Redo of the first preceding pass: the PR #304/#305 boundary programme

The earlier pass correctly found that PR #304's terminal atomic norm cannot be polylogarithmic.  The live repository has since strengthened and independently reproduced that conclusion on PRs #308, #310, #311, #313, and #315.

The constructive descendant PR #316 proves that the **first complete activated boundary**, although linear in the ordinary divisor-source atomic norm, has only logarithmic negative debt in its native paired central-flow coordinate.  Its all-generation `CBVR` recurrence remains open.

PR #317 gives another exact correction: eta-resolvent recombination is the old pure central producer, so a low-frequency eta contraction cannot be promoted to a full RH closure by ignoring zeta-zero modes.

Thus the correct outcome of the first pass is:

```text
atomic boundary termination                  FALSE at the claimed polylog scope;
first coupled boundary                        logarithmic in a correct flow norm;
central/eta all-generation positivity         FALSE / scope-corrected;
cycle-corrected all-generation recurrence     UNPROVEN.
```

There is no unconditional RH proof in that branch family.

## 2. Redo of the second preceding pass: wide-angle / first-principles attack

The previous fast response suggested searching for an abstract conserved quadratic energy.  That was too vague.  The live graph now supplies a much sharper test.

PR #322 proposed a five-adic finite residue automaton.  Two independent source firewalls show why the naive contraction does not close:

1. new `R-32301` proves the raw factor-five critical scaling is **neutral** in the square-root capacity mode, not a factor-`1/5` contraction;
2. concurrent PR #323 proves the nonzero residue states modulo five are Dirichlet-L channels, so a source-free contraction of the complete state is GRH-strength for the mod-five character family.

The exact neutral scalar is PR #277's half-moment

\[
\mathfrak H_X=-\sum_m r_X(m)\sqrt m.
\]

New `L-32301` determines its coefficient signs completely:

\[
\operatorname{sgn} h_{1/2}(n)=(-1)^{\omega(n)}.
\]

Thus the difficult mode is the same coherent prime-parity source already seen in the Möbius-hypercube failures.  It is not a harmless finite-state eigenvector.

## 3. First new theorem: multiplicative finite-difference parity

For `0<theta<1`,

\[
a_\theta(m)=m^\theta-(m-1)^\theta,
\qquad h_\theta=\mu*a_\theta.
\]

`L-32301` proves the exact positive-mixture formula

\[
h_\theta(n)
=\sum_{k\ge1}c_{\theta,k}n^{-(k-\theta)}
 \prod_{p\mid n}(1-p^{k-\theta}),
\qquad c_{\theta,k}>0,
\]

and hence

\[
\boxed{(-1)^{\omega(n)}h_\theta(n)>0\quad(n>1).}
\]

This is a complete all-integer sign theorem, not finite evidence.

## 4. Second new theorem: a critical-mode-null dyadic source

Define

\[
P_\dagger(x)=(1-x)(1-x/2)(1-\sqrt2x),
\qquad x=2^{-s},
\]

and

\[
\Omega_\dagger(s)={P_\dagger(2^{-s})\over\zeta(s)}.
\]

The roots have three exact roles:

```text
x=1          constant floor-tail cancellation;
x=2          affine carry-tail cancellation;
x=1/sqrt2   real square-root critical-mode cancellation.
```

Every hypothetical zeta zero with real part greater than one half remains an uncancelled pole.

`L-32302` proves:

- the complete Dirichlet inverse is coefficientwise positive;
- the generalized-prime sequence is nonnegative;
- the pointwise carry wavelet is supported inside one factor-eight window;
- the averaged carry image vanishes for every row `n>=8`.

The six nonzero averaged rows are exactly

\[
\begin{array}{c|c}
2&-5/6-\sqrt2/3\\
3&-1/2\\
4&11\sqrt2/10\\
5&5\sqrt2/6\\
6&9\sqrt2/14\\
7&\sqrt2/2.
\end{array}
\]

No asymptotic approximation enters this collapse.

## 5. Six-row RH criterion and its normalization correction

Pairing the source against the exact carry inverse gives one six-row scalar `C_dagger(X)`.

During the redo an initial formula incorrectly included the absent carry column `q=1`.  This was caught and fixed before review.  The correct identity is

\[
\mathcal C_\dagger(X)
=\sum_{2\le q\le X}{\omega_\dagger(q)\over\sqrt q}\log(X/q),
\]

with Mellin transform

\[
\boxed{
\int_1^\infty \mathcal C_\dagger(X)X^{-z-1}dX
={1\over z^2}
\left[
{P_\dagger(2^{-z-1/2})\over\zeta(z+1/2)}-1
\right].
}
\]

The `-1` is the unit-source correction and produces the elementary `-log X` real mode.  It does not cancel any off-line pole.

Therefore either a subpower bound or eventual one-sign theorem for this exact six-row scalar would imply RH.  Neither estimate is claimed proved.

## 6. Exact identification with the old bottom charge

The new source is not logically independent of the prior dyadic programme:

\[
\omega_\dagger=(\varepsilon-\sqrt2\delta_2)*\omega_2.
\]

`L-32305` proves

\[
\widetilde{\mathcal R}_\dagger(X)
=\widetilde{\mathcal R}_\omega(X)
 -\widetilde{\mathcal R}_\omega(X/2).
\]

After restoring the missing unit carry column,

\[
\mathcal C_\dagger(X)
=\mathcal R_\omega(X)-\mathcal R_\omega(X/2)-\log(X/2).
\]

If

\[
B(X)=5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X),
\]

then

\[
\boxed{
\mathcal C_\dagger(X)
=-{B(X)-B(X/2)\over6}-\log(X/2).
}
\]

Thus the six-row source is exactly the critical dyadic derivative of the old bottom-charge coordinate.  It is also the scalar channel naturally paired with PR #272's odd-column dyadic commutator.

## 7. A positive critical digital dual

The source admits a new exact positive digital face.

Let

\[
g_{1/2}=\sum_{j\ge0}2^{j/2}\delta_{2^j},
\qquad
d_\dagger=c_2*g_{1/2},
\]

where `c_2=1-v_2` is the binary-digit dual.  Since

\[
g_{1/2}*(\varepsilon-\sqrt2\delta_2)=\varepsilon,
\]

one has

\[
\boxed{
d_\dagger*\omega_\dagger
=\varepsilon-{5\over2}\delta_2+\delta_4.
}
\]

The summatory function is explicitly

\[
\boxed{
D_\dagger(N)
=\sum_{j\le\log_2N}
2^{j/2}s_2(\lfloor N/2^j\rfloor)\ge0.
}
\]

Moreover

\[
D_\dagger(N)=\Theta(\sqrt N).
\]

Hence the normalized causal digital kernel is positive and critical-order.  This is a real theorem, but not a free inverse: its critical nondecay is precisely the arithmetic neutral mode.

## 8. Exact annular physical-to-carry map

`L-32308` proves the critical-null analogue of PR #268's annular isometry.

For the compact physical window associated to `omega_dagger`, every finite coefficient sequence `x` has one integer potential `F_x` with

\[
\|Q_x\|_2^2
=\sum_r{|F_x(r)|^2\over r(r+1)}.
\]

The additive carry split is exactly

\[
(\mathcal S_nF_x)(j)
=\sum_q(\omega_\dagger*x)(q)\chi_{n,q}(j).
\]

For an annular source `M<=m<2M`, choosing `N=32M-1` gives an exact weighted physical/carry isometry on one oversupport row.

Thus there is no unidentified metric or physical-to-carry operator for the RH-sensitive specialization

\[
x=\Lambda_\dagger.
\]

The remaining issue is a quantitative arithmetic estimate inside the one declared carry Hilbert space.

## 9. Polylogarithmic square budget for the lower-scale inverse

The positive inverse satisfies

\[
a_\dagger(2^\nu m)=A_\nu\qquad(m\text{ odd}),
\]

with

\[
A_\nu=O(2^{\nu/2}).
\]

`L-32309` proves

\[
\boxed{
\sum_{n\le N}{a_\dagger(n)^2\over n}
=O(\log^2(2N)).
}
\]

and the exact source-change recurrence

\[
\Lambda_\dagger(n)
=W_\dagger(n)
+\sum_{d\mid n,\,d\ge2}a_\dagger(d)W_\dagger(n/d).
\]

All proper-divisor destinations lie at strict half scale.  The square coefficient budget is polylogarithmic; the old `ell^1` square-root explosion is avoided.  A Hilbert-space recurrence still has to control collisions/cross terms and is not inferred from the coefficient budget alone.

## 10. Five-mode synthesis and closed-strip frame

For compatibility with PR #263's pole/half-pole Green machinery, define the larger filter

\[
P_\Box(x)
=(1-x)(1-x/2)(1-2x)(1-\sqrt2x)^2.
\]

`L-32303` proves a positive compact five-window Green factor and an averaged carry image supported only below row 32.

`L-32304` initially had an odd-Euler normalization error; it was corrected before review.  Relative to PR #263's odd Euler product, the parity pair is

\[
q_+(z)=(1-z)(1-z/2)p(z),
\qquad
q_-(z)=(1+z)(1+z/2)p(-z).
\]

Using PR #263's sharp `45/4` frame gives a uniform closed-strip reserve.  The new pair is related to the old pair by bounded causal filters in both directions, so all previously proved parity synthesis remains available.

The thirty nonzero averaged carry rows have the exact sign blocks

```text
2..3     negative
4..7     positive
8..15    negative
16..31   positive
>=32     zero.
```

This finite bank is useful for transition diagnostics; the triple source is better conditioned for lower-scale inverse recombination because it avoids the supercritical `2^nu` inverse factor.

## 11. Strategic conclusion after the live PR #323 update

Concurrent PR #323 proves that odd-prime residue automata contain nonprincipal Dirichlet-L modes.  Radix two is character-free.  The preferred route is therefore:

```text
principal inverse-zeta source
-> critical real-mode dyadic high-pass
-> exact compact annular physical/carry isometry
-> finite current carry bank
-> positive generalized Selberg forcing
-> complete strict-divisor lower-scale family with polylog coefficient-square budget
-> source-complete odd-column dyadic commutator
-> strict lower-scale recurrence
-> RH.
```

The last strict recurrence is **UNPROVEN**.  Nothing in this report relabels it as a routine lemma.

## 12. Exact status

```text
previous vague conservation-law sketch            WITHDRAWN AS A PROOF CLAIM
PR #304 terminal atomic closure                   FALSE
five-adic 1/5 scaling reserve                     FALSE AS A SCALING CONSEQUENCE
five-adic residue automaton                       arithmetic / character channels remain
multiplicative half-moment parity sign             PROPOSED COMPLETE
critical-null triple source                        PROPOSED COMPLETE
six-row carry collapse                             PROPOSED COMPLETE
six-row Mellin criterion                           PROPOSED COMPLETE CONDITIONAL
critical digital dual                              PROPOSED COMPLETE
critical-null annular physical/carry isometry      PROPOSED COMPLETE
positive-inverse square budget                     PROPOSED COMPLETE
five-mode parity frame                             PROPOSED COMPLETE
strict source-complete recurrence                  UNPROVEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```

This packet is intended for adversarial review of the supplied exact mathematics.  It is not presented as an unconditional proof of RH because the final source-complete recurrence has not been proved.
