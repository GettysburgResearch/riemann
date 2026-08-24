# Elliptic symmetric fourth as a thin SO(5) slice

This packet takes the exact marked-cubic elliptic trace laws already frozen in
`genus1_cubic_family_laws.json` and pushes them through the fourth symmetric
power.  It does **not** enumerate another field element or curve.  Its purpose
is structural: a degree-five elliptic symmetric-fourth factor has the same
universal reciprocal coefficient shape as the primitive exterior-square
degree-five factor of a genus-two curve, but it occupies a rank-one curve
inside the ambient rank-two SO(5) coefficient space.

The finite input consists of the complete uniform-model trace histograms for
$q=3,5,7,11,13$. The symbolic formulas stated for every odd prime power use the
locked elliptic-stack character theorem, not interpolation from those five
fields.  Uniform marked models give the normalized elliptic-stack measure for
trace observables; they are not the uniform measure on coarse elliptic
isomorphism classes.

## 1. The degree-five weight-four factor

Write

\[
 P_E(T)=1-aT+qT^2=(1-\alpha T)(1-\beta T),
 \qquad \alpha+\beta=a,\quad \alpha\beta=q.
\]

The eigenvalues of \(\operatorname{Sym}^4\) are

\[
 \alpha^4,\quad q\alpha^2,\quad q^2,\quad q\beta^2,\quad \beta^4.
\]

Put $u=a^2-2q$. Pairing reciprocal roots gives the first exact
derivation:

\[
\begin{aligned}
 P_{\mathrm{Sym}^4 E}(T)
  ={}&(1-q^2T)
     \bigl(1-(u^2-2q^2)T+q^4T^2\bigr)\\
    &\mathrel{\phantom{(1-q^2T)}}
     \bigl(1-quT+q^4T^2\bigr).
\end{aligned}
\]

Equivalently, with

\[
 C=a^4-3qa^2+q^2,
 \qquad
 D=q(a^2-2q)\bigl((a^2-2q)^2+q(a^2-2q)-q^2\bigr),
\]

one obtains

\[
 \boxed{
 P_{\mathrm{Sym}^4 E}(T)
 =1-CT+DT^2-q^2DT^3+q^6CT^4-q^{10}T^5.}
 \tag{1}
\]

The producer independently recomputes (1) by Newton recurrence from

\[
 p_n=\alpha^{4n}+q^n(\alpha^{2n}+\beta^{2n})+q^{2n}+\beta^{4n}.
\]

Both derivations and the exact division by $1-q^2T$ are checked on every
source-histogram atom and on algebraic negative controls in the replay test.
The weight matters: $1-qT$ is the wrong proposed middle factor, and the
fixture records a nonzero evaluation at $T=1/q$ for $a=0$ in every frozen
field.

## 2. Exact elimination: the rank-one curve

Set $z=q^2T$. Every factor has the standard normalized SO(5) form

\[
 P_{\mathrm{Sym}^4 E}(z/q^2)
   =1-yz+dz^2-dz^3+yz^4-z^5.                 \tag{2}
\]

If $r=a^2/q$, then

\[
 y=r^2-3r+1=\chi_4,
 \qquad
 d=(r-2)y=\chi_2+\chi_6.                    \tag{3}
\]

Here $\chi_m$ denotes the character of the SU(2) representation
$\operatorname{Sym}^m$. With $w=r-2$, equations (3) become

\[
 y=w^2+w-1,\qquad d=wy.
\]

Eliminating $w$ gives the exact coefficient relation

\[
 \boxed{d^2+yd-y^2-y^3=0.}                  \tag{4}
\]

Thus the symmetric-fourth image is not a generic two-parameter SO(5)
family. Over characteristic zero the reduced curve (4) is rational, with
normalization parameter $w$; its node $(0,0)$ has the two geometric
preimages satisfying $w^2+w-1=0$. Neither preimage is rational: the
discriminant is $5$. Since every arithmetic input has
$r=a^2/q\in\mathbb Q$ and hence $w=r-2\in\mathbb Q$, no elliptic trace input
can hit $(y,d)=(0,0)$. “Rank one” here means one conjugacy or torus parameter,
not a rank-one local system.

Representation-theoretically, $\operatorname{Sym}^4$ maps
$\mathrm{SU}(2)$ into $\mathrm{SO}(5)$, kills the center
$\{\pm I\}$, and factors through the irreducible five-dimensional
representation of SO(3). This is the principal $A_1$ slice in $B_2$ at
the representation level.  Nothing here proves that the arithmetic family
has the largest possible monodromy allowed by that representation.

## 3. The middle eigenline: three levels that must not be conflated

The factor $1-q^2T$ is genuine pointwise, but it is not evidence for a
common Tate sub-local-system.

1. **Ambient representation.** $\operatorname{Sym}^4$ of the standard
   SL(2) representation is irreducible and has no invariant vector.  Ambient
   representation theory therefore forces no common line.
2. **Actual family.**  This packet does not determine the arithmetic or
   geometric monodromy of the marked-cubic family.  A smaller subgroup or a
   special locus could have extra invariant subsystems.
3. **Individual finite-field fiber.** Once a semisimple Frobenius torus is
   diagonalized, the middle monomial $\alpha^2\beta^2=q^2$ spans an actual
   Frobenius-stable line for that procyclic fiber.  Its axis varies with the
   chosen Frobenius torus and is not preserved by the full ambient SL(2).

Consequently the pointwise degree-four quotient is exact, while a compatible
rank-four quotient family, motive, automorphic representation, or Euler
product is not asserted.

## 4. A compact-group certificate for thinness

Clebsch--Gordan gives the multiplicity of the trivial representation in
$V_4^{\otimes n}$, hence the exact SU(2)-$\operatorname{Sym}^4$ trace
moments. A separate $B_2$ Weyl constant-term calculation gives the generic
SO(5) standard trace
moments:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SU(2), trace on $\operatorname{Sym}^4$ | 1 | 0 | 1 | **1** | 5 | 16 | 65 | 260 | 1085 |
| SO(5), standard trace | 1 | 0 | 1 | **0** | 3 | 1 | 15 | 15 | 105 |

The first separation is already cubic.  The principal SO(3) slice has a
cubic invariant in its five-dimensional representation; the SO(5) standard
representation does not.  This is a sharper subgroup detector than merely
observing that both factors have degree five and the same reciprocal shape.

## 5. Symbolic laws for every odd prime power

For the normalized elliptic-stack measure, the locked theorem says

\[
 \mathbb E[\chi_m]
 =-\frac{1+\Theta_{m+2}(q)}{q^{m/2+1}}
 \quad(m>0\text{ even}),
 \qquad \mathbb E[\chi_0]=1.                 \tag{5}
\]

The only nonzero cusp contribution below the degrees used here is
$\Theta_{12}(q)$, the prime-power Frobenius trace on
$S_{12}(\mathrm{SL}_2(\mathbb Z))$; for prime $q=p$, it is
Ramanujan's $\tau(p)$.

Using $y=\chi_4$, $d=\chi_2+\chi_6$, and Clebsch--Gordan, (5) gives

\[
\begin{aligned}
 \mathbb E[y] &= -q^{-3},\\
 \mathbb E[d] &= -q^{-2}-q^{-4},\\
 \mathbb E[y^2] &= 1-q^{-2}-q^{-3}-q^{-4}-q^{-5},\\
 \mathbb E[yd] &= -2q^{-2}-2q^{-3}-2q^{-4}-q^{-5}
                  -(1+\Theta_{12}(q))q^{-6},\\
 \mathbb E[d^2] &= 2-2q^{-2}-4q^{-3}-3q^{-4}-3q^{-5}
                  -(1+\Theta_{12}(q))q^{-6}-q^{-7},\\
 \mathbb E[y^3] &= 1-3q^{-2}-5q^{-3}-4q^{-4}-3q^{-5}
                  -2(1+\Theta_{12}(q))q^{-6}-q^{-7}.
                                                        \tag{6}
\end{aligned}
\]

These are theorem-driven all-$q$ identities. The formulas remain valid for
every odd prime power once the exact value of $\Theta_{12}(q)$ is supplied.
The bundled automatic numeric evaluator is intentionally narrower: it
inherits the locked Ramanujan-tau helper's inclusive characteristic cap
$p\le 1000$. Thus **bounded_exact_coordinate_laws(1009)** refuses explicitly;
this is a producer boundary, not a theorem boundary. For a larger
characteristic, **exact_coordinate_laws_with_theta12(q, theta12)** performs
the exact instantiation from a caller-supplied trace.

The complete frozen histograms reproduce every value in (6) exactly:

| $q$ | marked models | $\operatorname{Sym}^4$ support | exact $\mathbb E[y^3]$ |
|---:|---:|---:|---:|
| 3 | 18 | 4 | \(-601/2187\) |
| 5 | 100 | 5 | \(16739/78125\) |
| 7 | 294 | 6 | \(993999/823543\) |
| 11 | 1210 | 7 | \(7163639/19487171\) |
| 13 | 2028 | 8 | \(76503699/62748517\) |

In particular, a finite value can cross or overshoot its Haar limit.  These
five checks are not used to fit a convergence rate.

## 6. Precise comparison with primitive genus-two exterior square

The locked genus-two packet has

\[
 R(z/q)=1-sz+kz^2-kz^3+sz^4-z^5,
 \qquad
 s=b/q-1,\quad k=(a^2-b)/q.
\]

This is the same universal shape as (2), under $(u,v)=(s,k)$ there and
$(u,v)=(y,d)$ here. The constructions are nevertheless different:

- primitive genus-two exterior square uses
  \(\mathrm{Sp}(4)/\{\pm I\}\to\mathrm{SO}(5)\) and has an ambient
  two-parameter torus;
- elliptic symmetric fourth uses the principal
  \(\mathrm{SU}(2)/\{\pm I\}=\mathrm{SO}(3)\) subgroup and is constrained by
  (4);
- their finite-family measures, actual monodromy groups, motives, and global
  $L$-functions are not identified;
- in the genus-two construction, the canonical polarization line has already
  been removed, and the remaining pointwise normalized unit eigenvalue does
  not prove another common line;
- the symmetric-fourth construction has no pre-existing common line, and its
  pointwise $q^2$ eigenvalue does not prove any common line.

The useful discovery is the exact thin-slice relation and its moment
fingerprint, not a claim that the two families coincide.

## 7. Literature and novelty boundary

The symmetric-fourth transfer from GL(2) to GL(5) is classical.  The primary
reference used for that boundary is Henry H. Kim,
[*Functoriality for the exterior square of GL(4) and the symmetric fourth of
GL(2)*](https://doi.org/10.1090/S0894-0347-02-00410-1), *J. Amer. Math. Soc.*
16 (2003), 139--183.  This packet claims no discovery of the local factor,
its reciprocal form, or automorphy.  Its project-specific contribution is the
locked finite-family pushforward, the exact coefficient-curve elimination,
the selected symbolic all-$q$ stack defects, their bounded exact
instantiations, and the explicit comparison with the
ambient SO(5) genus-two packet.

## 8. Replay and resource boundary

The producer reads two locked JSON fixtures and visits only 55 genus-one
histogram atoms.  It performs no field/curve enumeration, floating-point
calculation, random sampling, database lookup, or interpolation.  A guarded
ledger counts histogram visits, Newton checks, finite coordinate-moment atom
products, and small Laurent-term products under an exclusive 5,000-unit cap.

From the repository root:

```text
python research/l-families/atlas/function_field/elliptic_symmetric_fourth_so5_slice.py --check
python -m unittest tests.test_elliptic_symmetric_fourth_so5_slice
python -O -m unittest tests.test_elliptic_symmetric_fourth_so5_slice
```

To regenerate the deterministic fixture:

```text
python research/l-families/atlas/function_field/elliptic_symmetric_fourth_so5_slice.py --write
```

The source fixture payloads and all producer, note, comparator, and replay-test
files are hash-locked inside the output.
