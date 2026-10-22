# The radical reduction in Liu's actual field and unit conventions

22 October 2026. **Source-dependent arithmetic and amplification
reduction. The matching-field high-conductor estimate remains
unproved.** This is a separate extension of RADICAL_STRATIFICATION.md;
it does not alter that frozen Eisenstein-field statement.

The result applies, in particular, to F=Q(zeta_12), the field required
by the conditional scalar comparison. It also applies to any fixed
number field containing mu_12 with the source conventions below.
The field is fixed throughout every estimate.

## 1. Exact source interface, not a count of raw field elements

Use Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1),
Section 3, especially Lemma 3.3 and equations (3.5)--(3.9),
printed pages 22--24; Section 10.2, equation (10.3);
Theorem 10.4; and Lemma 10.6, equations (10.15)--(10.16),
printed pages 56--58. For noncyclotomic F containing mu_12, the
same setup is explicitly retained in Lemma 18.1 and Theorem 18.2.
Only the allowed-generator and unit setup, ideal counting, and
the exact amplification identity are used from this interface.
No theta reflection or asserted new numerical boundary is needed
for the deduction below.

Choose the source's admissible fixed S, including the archimedean
places, primes above 6, fixed coefficient conductors, and enough
finite places that R=O_(F,S) is principal. An **exterior ideal**
means an integral ideal prime to the finite part S_f. Put

\[
 U_S=R^\times,\qquad \Gamma=U_S^6,\qquad
 \mathcal U_6=U_S/U_S^6.
 \tag{1}
\]

The group mathcal U_6 is finite. Source Lemma 3.3 supplies an
allowed generator for each exterior fractional ideal, unique
modulo Gamma, and their products are multiplicative modulo Gamma.
Every nonzero row in R/Gamma has a unique presentation

\[
                  u=\varepsilon a_u\pmod\Gamma,
            \qquad \varepsilon\in\mathcal U_6,
 \tag{2}
\]

where a_u is allowed and generates the exterior ideal of u.
The source row length is q_u=N((u)_S), the exterior-ideal norm.
It is not a count of all elements of a given full field norm:
the infinite S-unit repetitions have already been divided by Gamma.

The finite unit character
xi_epsilon(n)=chi_n(epsilon) is a fixed finite-order Hecke
character ramified only in S. At each unit sector it is absorbed
into the fixed coefficient character, exactly as in source (10.3).
Its zero extensions are unchanged. A fixed bounded row weight or
finite sector selector is harmless for the nonnegative estimates
below; no signed unit projector is deleted.

This setup avoids a class-number-one assumption on O_F. The
principalization of O_(F,S), the quotient by sixth powers of its
units, and multiplicativity modulo Gamma are the specific imported
source structure.

## 2. Exact decomposition, conductors, and counting

Every exterior integral ideal factors uniquely as v a^6 with
v sixth-power-free. Multiplicativity of allowed generators modulo
Gamma gives the unique row decomposition

\[
                  u=\varepsilon v a^6\pmod\Gamma .
 \tag{3}
\]

There is no condition (v,a)=1. The unit representative epsilon
belongs to the sixth-power-free row. Define

\[
                       \mathscr R(u)=N\operatorname{rad}(v),
 \tag{4}
\]

where the radical is over exterior primes only. Multiplication by
any allowed a^6 preserves both mathscr R and the finite unit sector.
The map (u,a)->u a^6 is injective when u is sixth-power-free and
a is an exterior ideal: the exterior prime valuations recover the
remainder and quotient modulo six, and (2) recovers the unit class.
This is exactly the injection used in source Lemma 10.6.

At every exterior prime, the residue characteristic is prime to
six and the field contains mu_6. A nonzero valuation j modulo six
gives a nontrivial tame Kummer character and hence conductor exponent
one. A zero valuation modulo six contributes no primitive conductor
there, but its original unit indicator remains if the prime divides u.
The finite unit characters and fixed coefficient character are
ramified only in S, so they cannot cancel any of the exterior
nontrivial characters. The primitive conductor outside S is therefore
exactly rad(v). At S the row classes lie in the fixed finite group
F_S^times/F_S^(times 6), so their local conductors have a fixed bound.

For H,C>=1,

\[
 \#\{u\in(R\setminus\{0\})/\Gamma:
                 q_u\le H,\ \mathscr R(u)\le C\}
       \ll_{F,S,\epsilon}H^{1/6}C^{5/6+\epsilon}.
 \tag{5}
\]

Indeed exterior ideals of norm at most X number O_F(X). At fixed v,
the choices of a in (3) number O_F((H/q_v)^(1/6)), times the fixed
finite number of unit classes. For a squarefree exterior ideal r,

\[
 \sum_{\operatorname{rad}(v)=r}q_v^{-1/6}
   =\prod_{\mathfrak p\mid r}\sum_{j=1}^{5}q_{\mathfrak p}^{-j/6}
   \le 5^{\omega(r)}q_r^{-1/6}.
 \tag{6}
\]

The ideal divisor bound and partial summation give (5).
In particular no extra power depending on [F:Q] or the S-unit rank
enters the exponent. Those data affect constants and the finite
sector multiplicity only.

## 3. Uniform reciprocal input and the low-conductor theorem

Let nu be a fixed finite-order Hecke coefficient character with
conductor supported in S, and let Q be a puncture exterior ideal,
fixed during the row sum. Define

\[
 M_{u,Q}(D;W)=
  \sum_{(n,Q)=1}\frac{\mu_F(n)\nu(n)\overline{\chi_n(u)}}{\sqrt{q_n}}
                  W(q_n/D).
 \tag{7}
\]

The sum is over exterior ideals; W is smooth, supported in a fixed
compact subinterval of (0,infinity). Source Lemma 10.6 instead
uses D^(-1/2) W_src(q_n/D). The exact normalization conversion is
W(y)=sqrt(y) W_src(y), which preserves every fixed finite seminorm
condition. Both common character orientations are allowed.

Assume a common finite-order Hecke zero-free half-plane Re(s)>beta
for this fixed F, where 1/2<beta<1. The precise reciprocal input is

\[
 L_F(\sigma+it,\psi)^{-1}
   \ll_{F,\delta,\epsilon}
       \{N\mathfrak f_\psi(3+|t|)^{[F:\mathbb Q]}\}^{\epsilon},
       \qquad \sigma\ge\beta+\delta.
 \tag{8}
\]

This is the same uniform reciprocal consequence isolated in the
frozen source packet's UNIFORM_INVERSE_AND_STRIPPING.md, Proposition 1:
common zero-freeness and the Hecke functional equation, with the
principal pole removed before applying a zero-free logarithm.
Deleting additional Euler factors costs the corresponding radical
norm to an arbitrary small power. Estimate (8), rather than an
unqualified pointwise bound with a character-dependent constant,
is the quantitative input used here.

Reciprocity and the unit-sector identity express (7) as the smooth
inverse of a primitive finite-order character, with all omitted
Euler factors retained. Its primitive conductor has norm
O_(F,S,nu)(mathscr R(u)), and its additional deleted primes divide uQ.
Mellin shifting to Re(s)=beta+delta consequently gives

\[
 |M_{u,Q}(D;W)|
   \ll \mathcal S(W)(Dq_uq_Q)^\epsilon D^{\beta-1/2}.
 \tag{9}
\]

The argument is identical in each of the finitely many unit sectors.
No angular infinite-type character is generated. Norm twists are
vertical translations and have the usual polynomial profile cost.
Combining (9) with (5), and redistributing epsilon, proves

\[
 \boxed{\quad
 \sum_{\substack{q_u\le H\\\mathscr R(u)\le C}}
       |M_{u,Q}(D;W)|^2
  \ll \mathcal S(W)^2(HDCq_Q)^\epsilon
                H^{1/6}C^{5/6}D^{2\beta-1}.
 \quad}                                                     \tag{10}
\]

All row sums are the literal source orbits with their finite unit
classes. The removal identity is exactly

\[
 \sum_{\substack{q_u\le H\\\mathscr R(u)\le C}}|M_{u,Q}(D;W)|^2
  =\sum_{\varepsilon\in\mathcal U_6}
    \sum_{\substack{v\ {\rm sixth\!-\!power\!-\!free}\\
                        N\operatorname{rad}(v)\le C}}
       \ \sum_{q_vq_a^6\le H}|M_{\varepsilon v,Qa}(D;W)|^2.
 \tag{11}
\]

Shared primes between v and a, all powers in a, and the original
unit character are retained. This proves the matching-field
low-conductor estimate; it is not merely a dimensional analogy.

## 4. Matching-field HC implies the actual amplified inverse exponent

Put kappa=2beta-1, rho=(11-12beta)/5 and choose

\[
       \eta,\tau>0,\qquad c=\rho-\eta-\tau>0.
 \tag{12}
\]

Assume the following **unproved** estimate in this same fixed F,
with its admissible S, fixed finite coefficient families, source
unit sectors, common fixed-seminorm uniformity, and polynomially
bounded growing punctures:

\[
 \sum_{\substack{q_u\le H\\\mathscr R(u)>D^c}}
       |M_{u,Q}(D;W)|^2
   \ll \mathcal S(W)^2(HDq_Q)^\epsilon H,
                   \qquad H\ge D^{1-\eta}.                 \tag{13}
\]

Equation (10) bounds its complement by
H D^(-5tau/6) times the allowed small powers, so (13) implies the
full raw H-bound at every H>=D^(1-eta).

The source amplification then yields, for sixth-power-free rows,

\[
 \boxed{\quad
 \sum_{q_u\le U}^{(6)}|M_{u,Q}(D;W)|^2
   \ll \mathcal S_1(W)^2(UDq_Q)^\epsilon
           U^{1/6}\max\{U,D^{1-\eta}\}^{5/6}.
 \quad}                                                     \tag{14}
\]

Here is a complete matching-convention proof of this step. For every
exterior ideal a, Euler multiplication gives

\[
 M_{u,Q}(D;W)
  =\sum_{d\mid\operatorname{rad}(a)}
       \frac{\mu_F(d)\nu(d)\overline{\chi_d(u)}
                       \mathbf1_{(d,Q)=1}}{\sqrt{q_d}}\,
                    M_{u a^6,Q}(D/q_d;W).
 \tag{15}
\]

This is source (10.16) with the exact extra puncture. At a prime
dividing either u or Q the relevant Euler factor is already one,
so the identity remains valid even when a meets u or Q. There is
no need to remove such amplifier ideals. Its absolute divisor mass
is product_(p|a)(1+q_p^(-1/2))<<q_a^epsilon.

Choose H0 equal to max(2U,D^(1-eta)) times a small buffering power
of max(2,U,D,q_Q), and average over all exterior ideals
q_a<=A=(H0/U)^(1/6). Their number is gg_(F,S) A for large A,
as in source Lemma 10.6. The finitely bounded case is absorbed
directly. The injection following (4) sends these pairs to rows
q_(u a^6)<=H0. Cauchy on (15), then the scale Sobolev argument,
gives

\[
 A\sum_{q_u\le U}^{(6)}|M_{u,Q}(D;W)|^2
  \ll (UDH0q_Q)^\epsilon
        \sum_{q_k\le H0}\sup_{T_0\le T\le D}|M_{k,Q}(T;W)|^2
  \ll (UDH0q_Q)^\epsilon\mathcal S_1(W)^2H0 .
 \tag{16}
\]

For the last inequality, dyadically cover T between a fixed positive
T0 and D and apply one-dimensional Sobolev on each scale interval.
The derivative profile is -yW'(y); both fixed profiles satisfy the
full raw bound already proved. This costs O(log(2D)) and a fixed
number of extra seminorms, absorbed in the small power. At bounded
nonempty subunit scales there are only O_(F,S,W)(1) exterior ideals;
smaller scales are empty. Since H0>=D^(1-eta), every shorter scale
is in the licensed range. Dividing by A and allocating the buffer
inside the final epsilon proves (14).

The all-row version follows from (11) without its conductor cutoff:
the row-scale terms sum against q_a^(-6), and the amplified terms
against q_a^(-1) up to q_a<=U^(1/6). They cost a constant and a
logarithm, respectively; their extra puncture Qa has the displayed
small-power cost. Thus the same bound is available with all the
source rows if a consumer needs it.

## 5. Exact conditional field conclusion

Taking beta=7/8, eta=tau=1/100 and c=2/25 gives precisely

\[
 \sum_{\mathscr R(u)\le D^{2/25},\ q_u\le H}|M_{u,Q}(D;W)|^2
        \ll (HDq_Q)^\epsilon\mathcal S(W)^2 H D^{-1/120},
        \qquad H\ge D^{99/100}.
 \tag{17}
\]

The complementary matching-field premise (13) would therefore
give the scalar comparison's inverse resource

\[
                        e(r)=\max\{1,\;1/6+33r/40\}.
 \tag{18}
\]

In particular (17)--(18) are valid as this conditional reduction
over F=Q(zeta_12). **An assumption about high-conductor rows only
over the Eisenstein field does not imply (13) over F.** The latter
must be the stated analytic hypothesis of the scalar certificate.
This note closes the arithmetic field-interface issue; it does
not prove that remaining moment or a new zero-free boundary.

For a conclusion over the full finite-order Hecke family of one
fixed F, premise (13) is required for every admissible fixed S
and every fixed finite coefficient family used as the target
varies. Its constants may depend on F,S and that fixed family,
as in Liu's source theorems; the exponents eta=1/100 and c=2/25
remain the same. An estimate for a single unrelated coefficient
character or a single chosen target does not meet this quantifier.

For a conclusion simultaneously over all number fields one would
need the matching high-conductor premise over every extension
F=K(zeta_12) required by Liu's descent, with the rest of that
source's analytic hypotheses. No such family premise is established
here. The complete-rectangle cubic result is a separate Eisenstein
component and is not used to justify (13).
