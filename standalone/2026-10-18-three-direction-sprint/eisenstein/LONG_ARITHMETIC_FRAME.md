# An exact long arithmetic frame for the squarefree physical rows

**PROPOSED source-qualified component theorem.** The finite frame and its
inverse below are proved. The stated principal-coordinate synthesis bound
uses the exact matched base section of `../rational/UNRESTRICTED_POLAR_ENERGY.md`.
Neither result bounds the entire continuous remainder or the complete
mixed moment. Physical rows here are SQUAREFREE. Numerator labels are
UNRESTRICTED. These are different restrictions.

The field is E=Q(omega), with the original good primary convention, fixed
excluded primes S, and the fixed finite ray data of the original physical
source. The exact adjoint identity is [rStation paper 10/v2, Section 7]
(https://rstation.ai/problems/riemann_hypothesis/papers/10), source SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.
The full residue periodicity and primitive cusp weights are the base-section
inputs explicitly pinned in `RESIDUE_VALUATIONS.md`. The annular-head
reciprocal and norm-comparison inputs are those in
`../rational/ANNULAR_PROFILE_DEBIAS.md`; they do not follow from the frame.

## 1. The row weight must belong to the target, not the frame

Fix 0<c<C. Let J_U be ALL good squarefree primary rows u in the finite
annulus cU<=Nu<=CU, or their fixed legal ray slice. There are O(U) rows.
Let h be a fixed smooth function supported in the interior of this
annulus. For the arithmetic mixed value f(u), set

    F(u)=h(Nu/U) f(u).                                      (1)

For an original smooth nonnegative row weight w, choose a smooth h with
|h|^2>=w and slightly enlarged compact annular support. Then the original
weighted squarefree-row mean is at most ||F||_2^2. Such an h exists by
taking a smooth cutoff equal to a sufficiently large constant on supp w.

There is NO row factor h, sqrt(h), or sqrt(w) in the frame defined next.
Consequently its inverse does not require a lower bound for h near its
support boundary. Putting sqrt(w) into both target and frame would instead
produce w^2 in a complete-label Parseval calculation; that would not
uniformly control the original w mean.

Fix a nonzero nonnegative smooth label profile W supported on a compact
annulus of (0,infinity). Let R run over EVERY good primary ideal, with no
power-free restriction, and define the finite matrix

    Psi_(u,R)=U^(-1/2) gamma_1(u) bar chi_u(R)
                                      sqrt(W(NR/K)).        (2)

Every nonunit zero in chi_u(R) is retained. On squarefree good u,
|gamma_1(u)|=1. A finite division into original ray classes is permitted;
fixed phases do not change any bound below. Labels can be summed over the
full finite set of good primary classes, so no new congruence assumption
is introduced.

## 2. The row-frame operator is invertible for long labels

Put S_K=Psi Psi*. For u=v, smooth lattice counting with the complete mask
(R,u)=1 gives

    (S_K)_(u,u)=c_(S,W) K/U prod_(p|u)(1-1/Np)
                          +O_epsilon(sqrt(K)/U (UK)^epsilon), (3)

with c_(S,W)>0 (and a different positive fixed scalar after a fixed label
ray restriction). One proof expands the squarefree mask divisor b|u.
The ideal count at length K/Nb has main c K/Nb and error O(sqrt(K/Nb));
sum_(b|u)(Nb)^(-1/2) is a prescribed subpower. The Euler product in (3)
is at least c_epsilon U^(-epsilon).

For distinct squarefree u,v, the character chi_u bar chi_v in R has a
nonprincipal primitive good part. At a prime in the symmetric difference
of u and v its tame exponent is 1 or -1 modulo six. It therefore remains
ramified there; an S-supported character cannot make it principal.
Its good conductor C_(u,v) divides uv/(u,v)^2, and NC_(u,v)<<U^2.
At primes common to u,v the quotient's unit phase may be principal, but
the original zero mask remains. Expand that mask by its divisors before
estimating the sum.

For completeness, primitive planar character Poisson with a smooth
annular norm profile gives

    |sum_a theta(a) V(Na/X)| << (NC X)^epsilon sqrt(NC)       (4)

for a nonprincipal finite-order character of good conductor C. The
prefactor is X/NC, the complete primitive Fourier coefficient has modulus
sqrt(NC), and the rapidly decreasing dual transform has lattice mass
O(NC/X) if X<=NC. If X>=NC, the zero frequency is absent and Fourier
decay gives the same bound. A fixed ray restriction is a finite expansion
by S-supported characters; none cancels the good ramification. Additional
zero-mask divisors change X and cost only a divisor subpower. Thus (4)
applies to the exact masked sum in S_K, including all shared primes.
It follows that

    |(S_K)_(u,v)| << (UK)^epsilon, u!=v,
    ||S_K-diag(S_K)|| <= O_epsilon(U (UK)^epsilon).          (5)

The row count O(U) and the Schur bound prove the second inequality.

Fix eta>0 and put K=U^(2+eta). Choose each internal epsilon sufficiently
small in terms of eta. The errors in (3) and (5) are then smaller than
half the diagonal lower bound for large U. In particular

    S_K >= c_(eta,epsilon) (K/U) U^(-epsilon) I,
    ||S_K^(-1)|| <<_(eta,epsilon) (U/K) U^epsilon.           (6)

The same conclusion holds for K in a fixed polynomial range with
K>=U^(2+eta). This is an actual proved ROW-frame lower bound. It does not
assume the small-label column-Gram hypothesis in paper 10 Section 8.
It uses unrestricted labels, so their sixth-power replicas and common
prime zeros must be included when bounding any coordinate family.

## 3. Exact reconstruction from the complete adjoint data

Define a=Psi*F. Since S_K is invertible, the exact finite-dimensional
identity is

    F=S_K^(-1) Psi a.                                      (7)

Let a=m+t+e be ANY exact decomposition of these coordinates. Define

    F_main=S_K^(-1)Psi m,
    F_rem=S_K^(-1)Psi(t+e).

Then F=F_main+F_rem. Moreover

    ||F_main||_2^2 <= ||S_K^(-1)|| ||m||_2^2,
    ||F_rem||_2^2 <= ||S_K^(-1)|| ||t+e||_2^2.              (8)

Indeed the squared norm of the left inverse S_K^(-1)Psi is
||S_K^(-1)Psi Psi* S_K^(-1)||=||S_K^(-1)||. No claim that m lies in
range Psi* is needed. Formula (7), rather than an adjoint relation alone,
is the justification for this forward decomposition.

Here is the precise source interpretation. Write the full arithmetic
vector on the squarefree rows as f(u)=sum_A c_A chi_A(u), retaining every
product power and original zero mask. In each common separated norm mode,
the relevant product length is L=DN. The pinned paper 10 identity, with
its row profile replaced by the smooth h of (1), is

    B_R(A)=U^(-1/2)sum_u h(Nu/U) bar chi_A(u)
                                      gamma_1(u) bar chi_u(R)
          =U^(1/6) hhat(2/3) rho_(prim,nu_[A])(AR)
                                                    +E_(U,R)(A). (9)

Reciprocity supplies exactly the fixed character nu_[A] from the source.
The source proof is linear in h; the contour identity is valid for a
smooth complex h too. On the finite row set containing its support,

    a_R=sqrt(W(NR/K)) sum_A c_A overline(B_R(A))             (10)

for real h, with the evident conjugate profile if h is complex. Thus
conjugation/orientation must be retained when matching the primitive
residue; taking absolute values before that matching is not permitted.
Equation (9) is on unrestricted good A, even when AR has square factors.

There are TWO distinct unpaid vectors in the application considered here:

* m_R is the Type-I MAINTERM in the matched fixed-section pairing of the
  primitive residue in (9) with the annular-debiased mixed coefficient.
* t_R is the ENTIRE residue pairing minus this specified m_R. It includes
  the complete nonconstant Type-I error and EVERY principal contribution
  of any other section not included in the matched mainterm.
* e_R is the pairing with the separate adjoint contour E_(U,R)(A).

These definitions, including the sqrt(W) label factor and the fixed
Mellin scalars, give an exact a=m+t+e even for the original full vector.
They do not discard either unpaid vector. If the input is restricted to
the matched base-compatible section, t is just its nonconstant Type-I
error; otherwise it also contains all unmatched principal sections.
Each other finite section requires its own exact residue match before
the mainterm bound in the next section can be used for it.

## 4. The true-weight principal contribution has a paid synthesis bound

For the matched base section, use
`../rational/UNRESTRICTED_POLAR_ENERGY.md`, source SHA256
`5c88ae67d837a78c2d6c655d1fd0ce463ccbfee944baf3eb060bd7421c2f3531`.
Its exact local formula, before taking absolute values, gives

    m_R=C U^(1/6)L^(1/3) sqrt(W(NR/K))
                    (N R_red)^(-1/6) v(rad R) L_R,         (11)

with the conjugation fixed in (10). In particular conjugating the complete
coordinate conjugates its ENTIRE coefficient and common profile along
with rho, not only rho. The Mobius head remains arithmetically the same,
the norm height kappa changes sign, and the calibration solution changes
to its conjugate because its original response matrix is real. Therefore
the annular comparison and response bounds apply with the same constants.
If ord_p R=6k+r, 0<=r<=5,
then R_red has exponent r at p. The primitive factor v(rad R) includes
primes of positive exponent SIX even when absent from R_red. Its local
Boolean response is 1/v_p-1 for residues zero through four, and q/v_p-1
for residue five. These are part of (11), not removed by periodicity.

The complete unrestricted-label energy proved there is

    ||m||_2^2 << (UDGK)^epsilon U^(1/3)L^(2/3)K^(2/3)
                                      D^(2beta-2)G^(-2beta-2). (12)

This includes all sixth-power replicas. Their weighted count is K^(2/3),
not the sixth-free count with an incorrectly unchanged R^(-1/3) weight.
Combining (6), (8), and (12) proves the genuine synthesis estimate

    ||F_main||_2^2 << (UDGK)^epsilon U^(4/3)L^(2/3)K^(-1/3)
                                      D^(2beta-2)G^(-2beta-2). (13)

All original common-profile Fourier integrals can be restored before the
norm by Minkowski: the fixed polynomial height costs in the source inputs
are absorbed by their rapidly decreasing densities. This does not
replace the original zero detector by a new pointwise mollifier.

For example, beta=7/8, D=U, N=sqrt(U), L=U^(3/2), K=U^(2+eta):

* G=D^(1/5) has complete norm-comparison cost U^(1+epsilon), and (13)
  is U^(2/3-eta/3+epsilon).
* G=U^(4/25)D^(1/5) has comparison cost U^(6/5+epsilon), and (13)
  is U^(1/15-eta/3+epsilon).

These are bounds for the specified principal synthesis contribution,
not for the original whole vector. In particular the comparison cost
must still be added when returning from a calibrated vector to the
original source.

## 5. Why this does not close the continuous term

The exact reconstruction eliminates a completeness ambiguity but gives
no automatic saving in the errors. Paper 10 Corollary 5 supplies only

    sum_(A~L)|E_(U,R)(A)|^2 << (ULNR)^epsilon L(NR)^(1/2).

If sum_A|c_A|^2 is subpower, coefficient Cauchy and summing all labels give
||e||^2 << L K^(3/2) times subpowers. Equation (8) then gives merely

    ||S_K^(-1)Psi e||^2 << U L K^(1/2) times subpowers,      (14)

which at the corner and K=U^(2+eta) is U^(7/2+eta/2+epsilon).
This is much larger than the desired U^(6/5). If a calibrated coefficient
has a larger arithmetic ell2 norm, that factor must also be paid.
The distinct nonconstant Type-I vector t has not been bounded here.
Neither t nor e is assumed independent or orthogonal to the mainterm.

There is also a useful check on interpretation. For a positive smooth h,
one can choose a smooth unit-modulus radial phase a(x) on its support
with integral h(x)a(x)x^(-1/3)dx=0, by mapping its normalized cumulative
mass to exp(2pi i times that cumulative mass). Multiplying each row of
the frame by this phase preserves its Gram spectrum and puts
ha in the adjoint profile. The raw residue coefficient hhat(2/3) then
vanishes for ALL labels R, while the original arithmetic vector and its
norm are unchanged. Thus eliminating raw pole coordinates by itself
cannot prove a bound for the whole vector; their mass can move into the
continuous coordinates of the new profile. In the convention of (9),
multiply the frame rows by a to put ha in B_R; their analysis coordinates
then conjugate this factor as in (10). Conjugating a instead gives h*bar a,
whose same moment also vanishes. This observation was supplied by the
rational-source agent and checked independently in this frame convention.
Estimate (13) is a correctly
normalized component bound, not a pole-removal proof of the full norm.

Finally, squarefree physical rows are a proper subset of the original
sixth-free row set. An extension through u=e*z, z powerful, needs its own
primitive-character/root-number and row-profile adapter. The frame does
not silently supply that adapter. The complete nonconstant/continuous
estimate on the actual arithmetic vector, including the other physical
row powers, remains open. No unconditional improved zeta boundary follows.
