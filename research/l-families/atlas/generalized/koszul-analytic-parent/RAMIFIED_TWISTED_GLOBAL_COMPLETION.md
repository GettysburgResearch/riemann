# A ramified twist of the genuine graded global source

This companion forms the actual finite sheaf R_n tensor chi_u **after**
forming the Segre source R_n. It proves an entire cohomological determinant
in the arithmetic variable and a meromorphic natural boundary in the
grading variable. The latter argument uses signed counts of a genus-nine
source; the positive untwisted count argument does not transfer.

The source hypotheses remain those of the frozen
[S3 family](S3_RAMIFICATION_AND_GRADED_FAMILY.md): characteristic p>3,
A nonzero, -4A^3-27B^2 nonzero, and

    E: y^2=f(x)=x^3+Ax+B,       u=y,
    d(u)=-4A^3-27(B-u^2)^2,    g(x)=-3x^2-4A.

Write Q for the constant field size and use characteristic-zero etale
coefficients. All geometric cohomology and finite-cover trace formulas
are the classical inputs already used in the
[global completion](GLOBAL_COHOMOLOGICAL_COMPLETION.md). No new RH
mechanism, priority claim, or number-field Euler product is asserted.

## 1. The actual twist and its three primitive sources

Let chi=chi_u be the rank-one quadratic sheaf of w^2=u, extended by
its zero inertia stalks at 0 and infinity. It is geometrically nontrivial.
The S3 closure is unramified at 0, whereas chi ramifies there; thus the
two covers are geometrically disjoint and their joint geometric group
is S3 times C2. This gives the source-defined sheaves

    T_n = R_n tensor chi,
    R_n = Sym^n(std_2) tensor Sym^n(perm_3).

Use the already proved multiplicities

    R_n = a_n 1 + b_n sign + c_n std,
    d_n=(n+1)^2(n+2)/2,
    t_n=n/2+1 for even n, and 0 otherwise,
    r_n=1 if 3 divides n, and 0 otherwise,
    a_n=(d_n+3t_n+2r_n)/6,
    b_n=(d_n-3t_n+2r_n)/6,
    c_n=(d_n-r_n)/3.                                    (1.1)

The three twisted sources are as follows.

* L(chi,T)=1: the cover P1_w -> P1_u has both source and target of
  genus zero, so its anti-invariant H^1 is zero, and its anti-invariant
  H^0 and H^2 are zero.
* The sign tensor chi source is the smooth genus-two curve
  D_chi: s^2=u d(u). The polynomial has five distinct roots: d has
  four simple roots and d(0) is nonzero. Its sixth branch point is
  infinity. Write P_Dchi for its degree-four H^1 polynomial.
* The std tensor chi source is the already constructed anti-invariant
  cohomology of C:w^4=f(x) over E, via y=w^2. Its rank is four.
  Write P_P=P_C/P_E for this actual Prym cohomology polynomial.
  No choice of a principally polarized Prym model is needed.

Consequently the complete finite-grade identity, including all bad
places, is

    L(T_n,T)=P_Dchi(T)^{b_n} P_P(T)^{c_n}.               (1.2)

H^0 and H^2 vanish; H^1 has dimension
4(b_n+c_n)=2(d_n-t_n). Both primitive rank-four Frobenius polynomials
have weight one and determinant Q^2, by the actual proper smooth
sources and their direct summands.

For clarity about extension and ramification, at each of the four old
C2 branch points chi is unramified. The old inertia-invariant space
has dimension a_n+c_n, and its residual Frobenius is multiplied by
chi(u_v). At 0 the new C2 acts as minus the identity on every T_n.
At infinity the joint inertia C6 contains the same central minus
identity. Thus both new stalks are zero. Elsewhere the local factor
is the original factor with T^{deg v} replaced by
chi(u_v) T^{deg v}. The conductor is

    4*(d_n-t_n)/2 + 2*d_n = 4d_n-2t_n;

Euler-Poincare gives H^1 dimension (4d_n-2t_n)-2d_n, as above.

This operation is not twisting one input before taking symmetric
powers. The latter gives R_n tensor chi^n. At n=2 it is untwisted,
and hence has H^0 and H^2 of dimension a_2=4 and H^1 dimension 16.
The actual T_2 has no H^0 or H^2 and H^1 dimension 32. At an
unramified identity Frobenius with chi=-1 its grade-two trace is -18,
whereas the input-twist shortcut gives +18. Grade one alone cannot
detect this error.

## 2. The regular-source double cover and signed point counts

Let Z be the frozen genus-three S3 Galois closure

    Z: y^2=f(x), v^2=g(x).

Its normalization after adjoining w^2=y is

    Z_tilde: w^4=f(x), v^2=g(x).                         (2.1)

The double cover Z_tilde -> Z ramifies at the six geometric points
over u=0 and the two points over infinity. At the former u has simple
zeros, since the S3 cover is unramified there; at the latter u has
pole order three. There are no other odd valuations. Riemann-Hurwitz
gives 2g(Z_tilde)-2=2*(2*3-2)+8=16, hence genus nine.

The anti-invariant cohomology is

    H^1(Z_tilde)^- = H^1(D_chi) + 2 H^1(P),

an equality of Frobenius modules, of rank twelve. Indeed the regular
S3 representation is 1+sign+2std, and its chi-twist has the three
primitive cohomology sources from section 1. Thus, if u_m and v_m
are the H^1 traces of D_chi and P,

    Delta_m = #Z_tilde(F_{Q^m}) - #Z(F_{Q^m})
            = -u_m-2v_m.                               (2.2)

These are actual signed integers with |Delta_m|<=12 Q^{m/2}.
They need not be positive or even nonzero. When Q is 3 modulo 4,
the square and fourth-power maps have identical fibre-count
functions in every odd-degree extension. Equation (2.1) then gives
Delta_m=0 for every odd m. This is an explicit obstruction to simply
reusing the positive Z-count argument.

For the bounded replay, affine counts in (2.1) are obtained directly
as sum_x fourths(f(x))*squares(g(x)), and the two possible infinity
points contribute 1+chi_field(-3), just as for Z. Each ramified
infinity point of the double cover has unchanged residue field.
The sign-twist count is 1+sum_u squares(u*d(u)). These equations are
specified before their cohomological polynomials are reconstructed.

## 3. An entire global determinant from the actual finite sources

Use the genuine multiplicity spaces B_n=Hom_S3(sign,R_n) and
C_n=Hom_S3(std,R_n), with dimensions b_n,c_n. Choose a complex
realization and fixed finite-dimensional Hermitian norms on the two
rank-four Frobenius sources, exactly as in the frozen untwisted
completion. Then form the Hilbert direct sum

    H_chi = direct_sum_n (B_n tensor H_Dchi)
                         + (C_n tensor H_P),
    K_chi(z)|_n = z^n Frob.

For every p>0, K_chi(z) is in S_p exactly when |z|<1; this follows
from the polynomial multiplicities and the fixed invertible finite
blocks. At |z|=1 it is bounded and noncompact; for |z|>1 it is
unbounded. This is the polynomial-growth R_n cohomology operator,
not the exponential-growth Koszul Lie operator.

The ordinary Fredholm determinant is

    L_chi(z,T)=det(1-T K_chi(z))
      = product_n P_Dchi(Tz^n)^{b_n} P_P(Tz^n)^{c_n}.    (3.1)

It is jointly holomorphic for |z|<1 and all complex T, with
L_chi(0,T)=L_chi(z,0)=1. For |T|<1/Q its logarithm is the actual
closed-point Euler logarithm, with grade weight z^{n deg v} and
the ramified stalks of section 1. Equivalently,

    log L_chi = -sum_{m>=1} T^m/m
                  [B(z^m)u_m + C(z^m)v_m],             (3.2)

where B=(F_e-3F_s+2F_c)/6, C=(F_e-F_c)/3 and

    F_e(z)=(1+2z)/(1-z)^4,
    F_s(z)=1/(1-z^2)^2, F_c(z)=1/(1-z^3).

All zeros lie on the grade-dependent circles
|T|=Q^{-1/2}|z|^{-n}; there are no poles. For every fixed 0<|z|<1
there are infinitely many zeros with unbounded modulus. Therefore
no identity with a nonzero rational T-prefactor can equate this
function with its value at 1/(QT): the reciprocal zeros would
accumulate at T=0, where (3.1) equals one. This rules out only that
finite-prefactor, fixed-z functional equation, not every possible
infinite completion or paired-scale construction.

## 4. A signed source natural boundary, without exceptional real T

Fix a real 0<T<1/Q. For any root of unity zeta of exact order h,
the same dominated-convergence argument as in the frozen untwisted
boundary proof gives

    lim_{r->1-}(1-r)^4 log L_chi(r*zeta,T)
      = C_h^chi = (1/2) sum_{h divides m} Delta_m T^m/m^5. (4.1)

Indeed the F_e coefficient in (3.2) is Delta_m/6, whereas the F_s
and F_c coefficients are u_m/2 and (v_m-u_m)/3. Their pole orders
are smaller than four. The resonant F_e term has scaled limit
3/m^4. Uniform bounds |F_g(r*zeta)|<=F_e(r), together with the
finite weight bounds, provide a summable majorant. Formula (4.1)
is real but can have either sign, and can vanish at some orders.

Nevertheless it is nonzero at a dense collection of roots, for
**every** fixed real T in the stated interval. First, Delta_h is
nonzero for infinitely many h. Otherwise the power traces of the
invertible rank-twelve anti-invariant Frobenius would eventually
vanish. Its characteristic recurrence has nonzero constant term,
so backward recurrence would force the zeroth power trace, twelve,
to vanish, a contradiction.

For any h with Delta_h nonzero, write

    C_h^chi = T^h/(2h^5) * [Delta_h + E_h].

The integrality |Delta_h|>=1 and the weight bound give

    |E_h| <= 12 (QT)^h/[1-(sqrt(Q)T)^h] -> 0.           (4.2)

To verify (4.2), bound the j>=2 contribution
sum_j Delta_{hj} T^{h(j-1)}/j^5 by dropping j^5 and summing its
geometric majorant. Thus all sufficiently large h with Delta_h
nonzero have C_h^chi nonzero, of the same sign.

Primitive h-th roots are dense along any unbounded sequence of
orders. Here is an elementary quantitative justification, so the
claim does not presuppose prime orders. In a fixed angular interval
of positive normalized length ell, inclusion-exclusion gives
ell*phi(h)+O(2^{omega(h)}) primitive exponents. The bounds
phi(h)>=sqrt(h/2) and 2^{omega(h)}<=64 h^{1/4} make the error
smaller than the main term for all sufficiently large h. The latter
bound separates the six primes below 16; each remaining prime
factor satisfies 2<=p^{1/4}. The former follows multiplicatively
from phi(p^a)^2/p^a>=1 except the single factor p^a=2, which
contributes 1/2.

At a root with C_h^chi>0, the modulus grows faster than any pole;
at a root with C_h^chi<0, it decays faster than any finite-order
zero. Either behavior contradicts a nonzero meromorphic extension
there, since a meromorphic germ is a finite integral power times
a holomorphic nonvanishing factor. These roots are dense, proving
that |z|=1 is a meromorphic natural boundary of L_chi(z,T).

This theorem does not assert nonzero constants at every root, does
not assert positivity, and does not cover arbitrary complex T.
The source-defined signed genus-nine trace sequence is essential
to its proof.

## 5. Bounded replay and analytic error bounds

The replay counts the equations over F_5, F_7 and their extensions
through degree three only. For each rank-four primitive source the
first two complete counts determine coefficients c_1,c_2 by Newton
identities; the proved weight-one duality supplies coefficients
Q*c_1 and Q^2. Degree three is held out. This is a reconstruction
using source duality, not four independent extension counts.

At finite u the replay multiplies the full inertia-invariant graded
trace by chi(u). It checks zero stalks at 0 and infinity, all-grade
rational trace identities, and the wrong chi^n grade-two control.
The genus-nine counts independently check the regular-source
decomposition (2.2) in all three small extensions.

For positive z=r<1 and real T>=0 with QTr<1, put h=QTr and
C_r=(F_e(r)-1)/r. Since b_n+c_n<=d_n/2, the absolute trace of
the twisted H^1 grade is bounded by 2d_n Q^m. Thus the power-log
tail after degree M is bounded by

    2 C_r h^{M+1}/[(M+1)(1-h)].                         (5.1)

The grade-product logarithm tail after N is bounded by

    2QT [F_e(r)-sum_{n=0}^N d_n r^n]
          /[1-QT r^{N+1}].                             (5.2)

These deliberately conservative bounds also permit replay at
T=1/2,z=1/10, beyond the initial Euler-product T disk. Exact
rational atanh enclosures are applied to the finite positive
quartic determinant values before rounding. The two independently
bounded constructions must overlap. Finite probes do not prove
the infinite nonzero-trace or primitive-root density arguments.
