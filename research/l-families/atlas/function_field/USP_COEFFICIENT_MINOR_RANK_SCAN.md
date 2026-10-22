# Reciprocal coefficient minors across symplectic ranks

**Status:** DRAFT exact compact-group exploration; not independently reviewed.

**Scope:** characters and Haar moments on `USp(2g)`. The all-rank identities are
algebraic. The checked rank audit is only `g=1,2,3`, with moments through order
four (and through order six for one `USp(4)` virtual control).

**Exact sources or dependencies:** elementary/exterior characters, the
two-by-two dual Jacobi--Trudi identity, the Weyl character formula, the Weyl
constant-term formula, and the all-`q` character means proved in
`GENUS2_MOMENT_IDENTITY.md`. The small-rank checker implements the character
and constant-term audits directly with integer/rational arithmetic; no
external computer algebra is trusted. The finite-family bridge imports only
the two displayed exact channel means from the existing proof packet.

**What was actually run:**

```text
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --write
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
```

**Smallest remaining gap:** evaluate the balanced virtual control in actual
hyperelliptic families. Its odd Haar moments vanish identically, so any finite
odd bias is arithmetic rather than a built-in compact-group sign.

## Project-facing takeaways

1. The existing genus-two alternating-moment theorem is a shadow of
   `H_g=-s_(2^g)`, not a genus-two-only phenomenon. Its sign should be treated
   as a representation-theoretic baseline, not as arithmetic evidence.
2. The literal probe `e_1^2-e_2^2` remains negative-honest in every rank
   `g>=2`; varying the genus does not remove that built-in sign.
3. The virtual control `B=2e_1^2-e_2^2` cancels the generic odd Haar
   background exactly, yet its finite genus-two mean is a proved positive
   `q^-1+O(q^-3)`. It is the cleanest next target for family-specific bias.
4. These are compact-group/coefficient statements, not a canonical analytic
   detector, an equidistribution theorem, or an RH implication.

## 1. Normalization

Let `V` be the standard `2g`-dimensional representation and write

\[
 e_k(U)=\operatorname{Tr}(U\mid\Lambda^kV).
\]

On a maximal torus this is the elementary symmetric polynomial in
`x_1,x_1^{-1},...,x_g,x_g^{-1}`. Symplectic reciprocity gives

\[
e_{2g-k}=e_k.
\]

These are normalized compact-group coefficients. Relating them to a concrete
family still requires the family's Frobenius normalization and an
equidistribution or direct character-sum theorem.

## 2. The genus-two sign identity is an all-rank Schur identity

Define the reciprocal-centre Hankel minor

\[
H_g=e_{g-1}e_{g+1}-e_g^2=e_{g-1}^2-e_g^2.
\]

For the rectangular partition `(2^g)`, dual Jacobi--Trudi is the two-by-two
determinant

\[
s_{(2^g)}=\det\!\begin{pmatrix}e_g&e_{g+1}\\e_{g-1}&e_g\end{pmatrix}
=e_g^2-e_{g-1}e_{g+1}.
\]

Therefore, for every `g>=1`,

\[
\boxed{H_g=-s_{(2^g)}.}
\]

This is stronger and simpler than a rank-by-rank character decomposition:
`s_(2^g)` is the character of the honest Schur functor `S_(2^g)(V)`. Hence

\[
(-1)^m\int_{USp(2g)}H_g(U)^m\,dU
=\dim\left(S_{(2^g)}(V)^{\otimes m}\right)^{USp(2g)}\in\mathbb Z_{\ge0}.
\]

Every positive even moment is strict: the restricted representation is
nonzero and self-dual, so its tensor square has an invariant. Odd moments can
vanish.

The exact low-rank audit gives:

| group | restriction of `s_(2^g)` | Haar moments of `H_g`, orders 1--4 |
|---|---|---|
| `USp(2)` | `chi_(2 omega_1)` | `0, 1, -1, 3` |
| `USp(4)` | `1 + chi_(omega_2) + chi_(2 omega_2)` | `-1, 3, -11, 56` |
| `USp(6)` | `chi_(2 omega_1) + chi_(omega_1+omega_3) + chi_(2 omega_3)` | `0, 3, -15, 377` |

Thus genus two is special only in the **strict first moment**: its rectangle
contains a trivial constituent, while the adjacent odd ranks `g=1,3` do not.
The alternating weak sign itself is forced in every rank before any arithmetic
family is introduced.

## 3. Keeping the literal genus-two formula in higher rank

Now keep the fixed-depth probe

\[
F_g=e_1^2-e_2^2
\]

rather than moving it to the reciprocal centre. For `g>=3`, another dual
Jacobi--Trudi identity gives

\[
e_2^2-e_1^2
=s_{(2,2)}+e_1(e_3-e_1).
\]

Here `e_3-e_1=chi_(omega_3)` is the primitive third-exterior character. At
`g=2`, reciprocity gives `e_3=e_1`, so the second term disappears and
`e_2^2-e_1^2=s_(2,2)`. Consequently `-F_g` is honest for every `g>=2`.

It contains exactly one trivial summand: `e_1=chi_(omega_1)` has Haar norm one,
whereas `e_2=1+chi_(omega_2)` has Haar norm squared two. Thus

\[
\int(e_2^2-e_1^2)=2-1=1.
\]

It follows that

\[
\boxed{(-1)^m\operatorname{Haar}(F_g^m)>0\quad(g\ge2,m\ge0).}
\]

The rank-one boundary reverses orientation:
`F_1=e_1^2-1=s_(2)` is itself honest, with moments `0,1,1,3` through order
four. This is an exact warning against extrapolating the genus-two sign rule
downward without checking the exterior-power boundary.

For reference, at rank three the honest character `-F_3` decomposes as

\[
1+2\chi_{\omega_2}+\chi_{\omega_1+\omega_3}+\chi_{2\omega_2},
\]

and the original `F_3` moments through order four are
`-1,7,-87,2051`.

## 4. A whole `USp(4)` cone has the same forced sign

Consider the integer pencil

\[
Q_{\alpha,\beta}=\alpha e_1^2-\beta e_2^2,
\qquad \alpha,\beta\in\mathbb Z_{\ge0}.
\]

Using the four `C_2` irreducibles visible in the two squares,

\[
-Q_{\alpha,\beta}
=(2\beta-\alpha)(1+\chi_{\omega_2})
+(\beta-\alpha)\chi_{2\omega_1}
+\beta\chi_{2\omega_2}.
\]

Therefore `-Q_(alpha,beta)` is an honest character exactly on the cone
`alpha<=beta`. The original point `(1,1)` is merely the boundary ray on which
the `chi_(2 omega_1)` coefficient cancels. An infinite collection of nearby
coefficient probes consequently has the same representation-forced
alternating moment pattern.

This matters for detector design: observing that pattern does not by itself
distinguish arithmetic structure, symplectic monodromy, or an especially
successful choice of minor.

## 5. A balanced virtual control with an exact symmetric Haar law

The first especially clean line outside that honest cone is

\[
B=2e_1^2-e_2^2
=\chi_{2\omega_1}-\chi_{2\omega_2}.
\]

On the `C_2` torus it factorizes:

\[
B=-(x_1^2+x_1^{-2})(x_2^2+x_2^{-2}).
\]

This virtual character has **every odd Haar moment equal to zero** and

\[
\boxed{\operatorname{Haar}(B^{2r})
=\frac{1}{r+1}\binom{2r}{r}^{\!2}\qquad(r\ge0).}
\]

There is an exact probabilistic form of the same result. Let `A` have the
arcsine density

\[
\frac{1}{\pi\sqrt{4-x^2}}\,1_{|x|<2}
\]

and let `S`, independently, have the Wigner semicircle density

\[
\frac{\sqrt{4-x^2}}{2\pi}\,1_{|x|<2}.
\]

Their even moments are `binom(2r,r)` and
`binom(2r,r)/(r+1)`, respectively, and their odd moments vanish. Hence `AS`
has exactly the displayed moments of `B`. Both laws have support in `[-4,4]`,
so compact moment determinacy gives

\[
\boxed{B\ \overset{d}{=}\ A S.}
\]

In particular, the Haar pushforward is genuinely symmetric and continuous:

\[
\Pr_{USp(4)}(B<0)=\Pr_{USp(4)}(B>0)=\frac12,
\qquad \Pr(B=0)=0.
\]

Here is a direct constant-term proof. In an odd power, both torus exponents
are `2 mod 4`. The `C_2` Weyl density has coordinate support at most four and
has zero coefficient at each `(+-2,+-2)`, so no constant term survives. In
power `2r`, only density exponents

\[
(0,0),\quad(\pm4,0),\quad(0,\pm4)
\]

contribute; their coefficients are respectively `8` and `-2` at each of the
four nonzero points. If `C=binom(2r,r)` and
`D=binom(2r,r-1)=Cr/(r+1)`, division by the Weyl order eight gives

\[
\frac{8C^2-8CD}{8}=C(C-D)=\frac{C^2}{r+1}.
\]

The frozen direct checks are

\[
0,2,0,12,0,100
\]

through order six.

This control already has a nonzero arithmetic answer in the quintic
hyperelliptic family. Under the atlas normalization,

\[
B_D=\frac{2a_D^2}{q}-\frac{b_D^2}{q^2}
=\chi_{2,0}-\chi_{0,2}.
\]

The existing all-`q` proof gives

\[
\langle\chi_{2,0}\rangle_q=q^{-3}-q^{-4},\qquad
\langle\chi_{0,2}\rangle_q=-q^{-1}-q^{-5},
\]

and therefore

\[
\boxed{\langle B_D\rangle_q
=q^{-1}+q^{-3}-q^{-4}+q^{-5}.}
\]

The values at `q=3,5,7` are respectively

\[
\frac{88}{243},\qquad\frac{646}{3125},\qquad
\frac{2444}{16807}.
\]

Thus the zero Haar mean is approached with an explicitly positive leading
`q^-1` bias. This is not a trend fit: it is a formal consequence of two
proved all-`q` character averages. It isolates a family-specific correction
that the sign-coherent original minor obscures.

Unlike the original minor, `B` has no built-in odd Haar bias. It is therefore
a sharper compact-group control: an odd finite-family moment of normalized
`2e_1^2-e_2^2` measures arithmetic deviation from Haar directly. A plausible
next exact calculation is to run the existing squarefree-sieve machinery on
its first and third finite-family moments before attempting any larger field.

## 6. What this does and does not say

What is established here:

- the all-rank Schur explanation of the reciprocal-centre minor;
- an all-rank honest-character explanation of the fixed-depth probe for
  `g>=2`;
- exact `C_1`, `C_2`, and `C_3` restriction audits;
- an exact `USp(4)` honest cone; and
- the balanced virtual control's all-order Haar moments.

What is not established:

- convergence of any finite L-function family to these Haar laws;
- a source-faithful analytic `XD`, `HCNC`, Pick, or Loewner detector;
- novelty in the representation-theory literature (the identities are
  classical in mechanism, although they were not previously recorded in this
  project); or
- any implication for RH.

The design lesson is concrete: first decompose a coefficient detector in the
representation ring. Schur-positive or negative-Schur-positive directions
come with predetermined Haar moment signs. To expose family-specific
arithmetic, compare exact finite character averages or use virtual directions,
such as `B`, whose generic odd background cancels.
