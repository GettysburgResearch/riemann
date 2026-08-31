# The conditional xi zero-feature form and its domain obstruction

Status: proposed analytic successor; preregistered before finite controls.
Scope: the same literal completed-xi normalization and exponential core as
SP. The zero-feature factorization is conditional on RH. Its nonclosability
is a domain theorem, not evidence for or against RH.

Authoring parent: `13c236591b144dd69502e831874c0505b6d8267d`.
The load-bearing operator theorem is SP at
`e5e43625b157ecc5f602532e16a1197679594824`.

## 1. Exact statement

Let H=L2(0,infinity), e_x(t)=exp(-xt), x>1/2, and D be the finite
complex span of these exponentials. Put

\[
 Y(x)=\xi_R(1/2+x),\quad F=Y'/Y,\qquad T_0e_x=F(x)e_x.
\]

SP proves, with no assumption of this note, that

\[
 \mathrm{RH}\iff T_0\text{ is closable}
 \iff T_0\text{ is accretive on }D.                  \tag{ZF1}
\]

The present theorem describes the POSITIVE QUADRATIC FORM when RH is
assumed. For the distinct positive critical ordinates gamma, retaining
multiplicity m_gamma, let

\[
 \mathcal K=\bigoplus_{\gamma>0}\mathbb C^2,
\]

and define on D

\[
 (Vg)_{\gamma,0}=\sqrt{2m_\gamma}\int_0^\infty
          g(t)\cos(\gamma t)dt,
\quad
 (Vg)_{\gamma,1}=\sqrt{2m_\gamma}\int_0^\infty
          g(t)\sin(\gamma t)dt.                     \tag{ZF2}
\]

Under RH, V is a well-defined minimal Kolmogorov factor and

\[
 \boxed{\quad 2\operatorname{Re}\langle g,T_0g\rangle
                 =\|Vg\|_{\mathcal K}^2\quad(g\in D).\quad}       \tag{ZF3}
\]

Nevertheless,

\[
 \boxed{\quad D(V^*)=\{0\};\quad V\text{ is not closable}.\quad}  \tag{ZF4}
\]

Consequently ZF3 is not an operator identity T_0+T_0^*=V^*V, and the
positive form on D is not closable. Every other minimal Hilbert-space
factor of the same kernel is unitarily equivalent to V and has the same
obstruction. This is compatible with ZF1: an accretive closable operator
need not have a closable real-part form when it is not sectorial.

Unconditionally, SP's source polarization gives an exact INDEFINITE
quadratic representation. A positive source-local Hilbert factor on all
of D would make T_0 accretive and hence prove RH by ZF1. Requiring that
factor to be closable is stronger and, by ZF4, is impossible even under
RH. Thus neither positivity nor domains can be silently supplied by the
formal prime-shift expression.

## 2. The conditional Gram identity

All inner products are conjugate-linear in the first argument. Under RH,
SP's locally uniform product formula is

\[
 F(z)=\sum_{\gamma>0}m_\gamma
 \left(\frac1{z-i\gamma}+\frac1{z+i\gamma}\right),
 \qquad \sum_\gamma\frac{m_\gamma}{\gamma^2}<\infty.              \tag{ZF5}
\]

For a core vector g=sum_j c_j e_(x_j), elementary Laplace integration
gives

\[
 (Vg)_{\gamma,0}=\sqrt{2m_\gamma}
       \sum_jc_j\frac{x_j}{x_j^2+\gamma^2},\qquad
 (Vg)_{\gamma,1}=\sqrt{2m_\gamma}
       \sum_jc_j\frac{\gamma}{x_j^2+\gamma^2}.                   \tag{ZF6}
\]

The square sum converges by ZF5. Its polarized kernel is

\[
 \langle Ve_x,Ve_y\rangle
 =\sum_{\gamma>0}2m_\gamma
 \frac{xy+\gamma^2}{(x^2+\gamma^2)(y^2+\gamma^2)}
 =\frac{F(x)+F(y)}{x+y}.                                      \tag{ZF7}
\]

Together with SP12, this proves ZF3 with every factor 2 and multiplicity
fixed. It is a form identity on D only.

## 3. Minimality

Suppose a=(a_gamma,b_gamma) in K is orthogonal to every Ve_x,
x>1/2. Cauchy--Schwarz and sum m_gamma/gamma^2<infinity make

\[
 R(z)=\sum_{\gamma>0}\sqrt{2m_\gamma}
       \frac{a_\gamma z+b_\gamma\gamma}{z^2+\gamma^2}           \tag{ZF8}
\]

locally normally convergent away from its discrete boundary poles.
It vanishes on the real interval x>1/2 and hence in Re z>0. At i gamma
and -i gamma its two residues are constant nonzero multiples of
a_gamma-i b_gamma and a_gamma+i b_gamma. Both vanish, so a_gamma=b_gamma=0.
Thus the closed span of {Ve_x:x>1/2} is all of K. Equal-height
multiplicity is one weight in one coordinate pair; it is not duplicated.

The same residue argument establishes the standard uniqueness statement:
two minimal factors of ZF7 are related by a unique unitary, initially
defined on finite linear combinations of their kernel vectors.

## 4. The adjoint domain is zero

Let a=(a_gamma,b_gamma) lie in D(V*). By definition there is u in H
such that

\[
 \langle Ve_x,a\rangle_K=\langle e_x,u\rangle_H
     =(Lu)(x)\qquad(x>1/2).                                  \tag{ZF9}
\]

The left side is ZF8 (up to harmless conjugation of its coefficients).
The right side extends to an H2 function in Re z>0. The identity theorem
makes the two analytic functions equal there.

A right-half-plane H2 function cannot have a nonzero simple boundary pole.
Indeed, a term c/(z-i gamma) contributes a constant times |c|^2/sigma
to

\[
 \sup_{\sigma>0}\frac1{2\pi}\int_{\mathbb R}
          |h(\sigma+it)|^2dt,
\]

while the locally analytic remainder is bounded in a fixed neighborhood;
the reverse triangle inequality on a shrinking neighborhood preserves
the divergence. The locally normal convergence in section 3 makes that
remainder legitimate at each isolated ordinate.

Therefore both boundary residues of ZF8 vanish for every gamma. Section
3's two equations give a_gamma=b_gamma=0. Hence D(V*)={0}. Since D is
dense but D(V*) is not dense in nonzero K, the standard adjoint criterion
shows that V is not closable. This proof does not call boundary evaluation
a bounded L2 functional; its unboundedness is exactly the obstruction.

If the form q(g)=||Vg||^2 were closable, its closed-form representation
would supply a closed factor W with the same kernel on D. Restrict to the
minimal closed span and use the unitary uniqueness above; V would then be
closable, a contradiction. Thus q itself is not closable.

## 5. Exact source equality and the prime boundary

SP gives an unconditional Hilbert--Schmidt source kernel A_Phi with

\[
 B_X(ix,iy)=Y(x)Y(y)\frac{F(x)+F(y)}{x+y}.
\]

For g=sum c_j e_(x_j), set

\[
 q_g(a)=\sum_j\frac{c_j}{Y(x_j)}e^{-x_j a}.
\]

The decay proved in SP makes all integrals absolute, and its Fourier
identity gives

\[
 2\operatorname{Re}\langle g,T_0g\rangle
 =\iint_{\mathbb R^2}\overline{q_g(a)}A_\Phi(a,b)q_g(b)\,da\,db. \tag{ZF10}
\]

Under RH this equals ||Vg||^2. Without RH, ZF10 remains true but its
source quadratic form need not be positive. Pointwise positivity of pieces
of A_Phi is irrelevant; SP's fixed-r two-node coefficient has negative
determinant.

SP also gives on D the exact Euler/prime formula involving the left shift
exp(-log(n)A_0). It is an algebraic identity after the Gamma, pole and
prime terms have been combined. The separate term (A_0-1/2)^(-1)|D is
nonclosable, and A_0=-d/dt on its maximal domain has right-half-plane
point spectrum. Hence ordinary self-adjoint functional calculus, separate
operator adjoints, or termwise V*V constructions are invalid.

A legitimate unconditional positive source factor of ZF10 would imply
the PSD of every safe matrix ZF7, so SP13 would imply RH. Even conditionally,
ZF4 shows that it cannot be promoted to a closable factor of this core
form. A useful source theorem must therefore either remain a quadratic
identity with its exact nonclosable domain, change the ambient topology,
or introduce a genuinely renormalized/sectorial form. Calling any of
these changes harmless would conceal the central burden.

## 6. Preregistered finite controls and scope

Before arithmetic, the finite controls are fixed:

- exact rational verification of ZF7 for three fixed positive spectral
  measures, three safe-node panels, and every principal subpacket;
- two independent exact determinant routes and the explicit rank cap
  two times the number of distinct ordinates;
- exact residue matrices at plus/minus i gamma for four fixed ordinates,
  including multiplicity weights and a same-height aggregation control;
- finite minimality controls using a fixed six-by-six feature matrix;
- hostile failures for a missing sine channel, a duplicated multiplicity
  coordinate, a sign-swapped pole, and an asserted V*V operator scope;
- strict typed JSON, rational, source and artifact seals.

These finite checks authenticate only algebra and schema. They do not
prove RH, the infinite H2 pole argument, source positivity, or closability.
No new xi values, zeros, prime sums or numerical thresholds are computed.

The theorem adds a domain-correct Kolmogorov description and an obstruction;
it does not duplicate SP's closability equivalence. It proves no order-five
matrix result, no positive A_Phi factor, and no prime-source square root.
External novelty is not asserted.
