# Balanced `USp(4)` control in the frozen quintic families

**Status:** exact bounded exploration, with separately locked all-`q` and
compact-group inputs.

**Scope:** every monic squarefree quintic over `F_q` for exactly
`q=3,5,7`.  No field above `7` is evaluated.  The largest field has
`7^5=16807<20000` monic candidates.

**Exact sources or dependencies:** `genus2_q_scan.py` for finite-field
coefficient arithmetic, `genus2_affine_orbits.py` for the exact affine
action, `GENUS2_MOMENT_IDENTITY.md` and its checker for the all-`q` first
moment, and `USP_COEFFICIENT_MINOR_RANK_SCAN.md` and its checker for the
exact `USp(4)` Haar law.  All are content-hash locked in the JSON artifact.

**What was actually run:** exhaustive squarefreeness and character-sum
coefficient reconstruction for all `3^5+5^5+7^5=20175` candidates, with a
per-field cap of `20000`; exact joint, support, sign, moment, affine-orbit,
and endpoint aggregation; and an exact `C_2` virtual-character reduction of
the third moment.  No roots, random samples, larger fields, or floating-point
quantities enter the artifact.

**Smallest remaining gap:** evaluate one explicit weight-six virtual
character average `mean(R6)` for general odd prime powers.  Three frozen
values do not establish such a formula.

## 1. Normalization and the exact Haar control

Write

\[
 L_D(u)=1+a_Du+b_Du^2+q a_Du^3+q^2u^4
\]

and define

\[
 B_D=\frac{2a_D^2}{q}-\frac{b_D^2}{q^2}
     =\frac{J_D}{q^2},
 \qquad J_D=2q a_D^2-b_D^2.
\]

For the compact group, with `e_1=Tr(U)` and `e_2` the second exterior
character,

\[
 B=2e_1^2-e_2^2=\chi_{2,0}-\chi_{0,2}
   =-(x_1^2+x_1^{-2})(x_2^2+x_2^{-2}).
\]

The locked `C_2` calculation proves that its Haar law is symmetric and
continuous on `[-4,4]`, with

\[
 \Pr(B<0)=\Pr(B>0)=\frac12,\qquad \Pr(B=0)=0,
\]

every odd moment zero, and

\[
 \operatorname{Haar}(B^{2r})
 =\frac{1}{r+1}\binom{2r}{r}^{2}.
\]

Thus the first six Haar moments are

\[
 0,\ 2,\ 0,\ 12,\ 0,\ 100.
\]

These are compact-group theorems, not conclusions drawn from the three
finite fields.

## 2. The proved all-`q` mean

The existing squarefree-family moment proof gives, for every odd prime
power `q`,

\[
 \langle\chi_{2,0}\rangle_q=q^{-3}-q^{-4},\qquad
 \langle\chi_{0,2}\rangle_q=-q^{-1}-q^{-5}.
\]

Consequently

\[
 \boxed{\langle B_D\rangle_q
 =q^{-1}+q^{-3}-q^{-4}+q^{-5}.}
\]

This is the only all-`q` finite-family moment asserted here.  It is a
consequence of the locked proof, not a fit.  Its frozen specializations are
`88/243`, `646/3125`, and `2444/16807`.

## 3. Exhaustive frozen laws

The scan visits all `q^5` monic quintics, rejects the nonsquarefree ones by
an exact polynomial gcd, and reconstructs `(a_D,b_D)` from character sums
over `F_q` and `F_(q^2)`.  The exact family sizes are `q^5-q^4`.

| `q` | members | joint `(a,b)` atoms | `B` atoms | negative | zero | positive | `min B` | `max B` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 162 | 32 | 14 | 48 | 12 | 102 | `-19/9` | `29/9` |
| 5 | 2500 | 81 | 33 | 986 | 50 | 1464 | `-4` | `96/25` |
| 7 | 14406 | 138 | 55 | 6258 | 336 | 7812 | `-4` | `181/49` |

Every frozen support lies in the exact Haar support `[-4,4]`.  The member
sign fractions are respectively

\[
 (8/27,2/27,17/27),\quad
 (493/1250,1/50,366/625),\quad
 (1043/2401,8/343,1302/2401)
\]

in `(negative,zero,positive)` order.  They are exact finite facts.  In
particular, the visible drift toward `(1/2,0,1/2)` is not promoted to a
monotonicity or convergence theorem.

The six exact normalized member moments are:

| order | Haar | `q=3` | `q=5` | `q=7` |
|---:|---:|---:|---:|---:|
| 1 | 0 | `88/243` | `646/3125` | `2444/16807` |
| 2 | 2 | `3560/2187` | `141284/78125` | `1536800/823543` |
| 3 | 0 | `42136/19683` | `2362156/1953125` | `34798640/40353607` |
| 4 | 12 | `1531592/177147` | `514468844/48828125` | `21877044944/1977326743` |
| 5 | 0 | `28210648/1594323` | `14061597676/1220703125` | `648054364784/96889010407` |
| 6 | 100 | `889288040/14348907` | `2745781777004/30517578125` | `442530198951440/4747561509943` |

The JSON retains the complete joint `(a_D,b_D)` law, complete `J_D`
histogram, exact probabilities, raw `sum J_D^m`, and exact differences from
the Haar moments.

## 4. Newly source-locked raw aggregates

The same bounded loop independently recomputes the three raw sums which the
earlier high-weight packet had only recorded as frozen controls:

| `q` | `sum b_D^3` | `sum a_D^2 b_D^2` | `sum b_D^4` |
|---:|---:|---:|---:|
| 3 | 8256 | 8352 | 45552 |
| 5 | 788080 | 857040 | 8278480 |
| 7 | 14205744 | 16117248 | 221057088 |

The artifact binds these sums to a deterministic member-coefficient ledger
digest, the producer, its tests, and the coefficient-arithmetic source.  It
does not read or hash the earlier high-weight artifact; the dependency is
deliberately one-way so that the high-weight packet can consume this scan as
its independent provenance source.

With `t=a_D/sqrt(q)` and `e=b_D/q`, the exact triangular identities

\[
\begin{aligned}
 \chi_{0,3}&=e^3-e^2-2et^2-e+3t^2,\\
 \chi_{0,3}+\chi_{2,2}
 &=e^2t^2-3et^2-t^4+5t^2-1,\\
 \chi_{0,4}+3\chi_{2,2}+4\chi_{0,3}
 &=e^4-5et^2-2t^4+14t^2-3e^2-2
\end{aligned}
\]

therefore recover the three frozen high-weight channel means from this
enumeration.  Agreement with the prior packet is a regression check, not a
circular source for the raw totals.

## 5. Affine orbits and endpoint concentration

For

\[
 (D\mid(\alpha,\beta))(T)=\alpha^{-5}D(\alpha T+\beta),
\]

the exact coefficient laws give `a -> chi(alpha)*a` and `b -> b`; hence
`B_D` is orbit-invariant.  Repartitioning the scanned members gives `29`,
`132`, and `349` affine orbits.  The sign counts under uniform *orbit*
weight are

\[
 (10,2,17),\quad(52,4,76),\quad(155,8,186),
\]

again in `(negative,zero,positive)` order.  These differ from member weights
when stabilizers are nontrivial; the JSON keeps both measures separate.

The endpoints are unusually concrete:

- at `q=3`, `J=-19` and `J=29` each comprise one free orbit of six members;
- at `q=5`, the lower Haar endpoint `B=-4` has six members split into
  orbits of sizes `5` and `1`, while `J=96` has twenty members in two orbits
  of size `10`;
- at `q=7`, `B=-4` has forty-two members in two size-`21` orbits, while
  `J=181` has forty-two members in one free orbit.

The artifact reports the exact shares of absolute moments `2,4,6` carried
by the absolute extreme and by the two endpoints.  These are finite support
concentrations only; they are not a limiting tail law.

## 6. Exact reduction of the first unresolved odd moment

The first moment is proved for all odd prime powers, but the third
finite-family moment has no all-`q` evaluation in the locked sources.  The
raw identity is

\[
 B_D^3=\frac{8a_D^6}{q^3}
 -\frac{12a_D^4b_D^2}{q^4}
 +\frac{6a_D^2b_D^4}{q^5}
 -\frac{b_D^6}{q^6}.
\]

An independent exact `C_2` decomposition sharpens this to

\[
\begin{aligned}
B^3={}&6\chi_{2,0}-6\chi_{0,2}-2\chi_{0,3}+2\chi_{2,3}
 +3\chi_{6,0}-3\chi_{4,2}+\chi_{2,4}-\chi_{0,6}\\
={}&6B-2\chi_{0,3}+R_6,
\end{aligned}
\]

where

\[
 R_6=2\chi_{2,3}+3\chi_{6,0}-3\chi_{4,2}
     +\chi_{2,4}-\chi_{0,6}.
\]

The new `sum b_D^3` lock makes `mean(chi_(0,3))` exact in each frozen
field.  Thus

\[
 \boxed{\langle B_D^3\rangle_q
 =6(q^{-1}+q^{-3}-q^{-4}+q^{-5})
 -2\langle\chi_{0,3}\rangle_q+\langle R_6\rangle_q.}
\]

The remaining frozen `mean(R6)` values are

\[
 \frac{3364}{19683},\qquad
 \frac{93156}{1953125},\qquad
 \frac{1227172}{40353607}.
\]

This is an exact pointwise reduction, not an all-`q` average formula.  The
smallest honest next calculation is the squarefree-family average of this
single explicit virtual weight-six channel.

## 7. Firewall

The mean formula in Section 2 is proved for every odd prime power by a
separate locked argument.  The Haar symmetry and moment formula in Section
1 are exact compact-group facts.  Everything else numerical in this packet
is exhaustive only at `q=3,5,7`.  No interpolation, higher-field search,
equidistribution theorem, detector claim, or RH implication is made.
