# The coherent quadratic graded algebra and the fixed-twist module

There are two different, valid source constructions:

    M_n=R_n tensor chi,          A_n=R_n tensor chi^n.

The preceding fixed-twist packets target M_n. Their grade-two
chi-versus-chi-squared tests reject substituting A_n for M_n; they do
not assert that A_n is an invalid generalized object. This companion
constructs A as an actual graded algebra on the joint cover, proves
its analytic completion, and compares its principal poles and positive
scalar-resonance boundary with the signed boundary of M.

All covers and hypotheses are those of the
[quadratic signed theorem](QUADRATIC_SIGNED_SOURCE_BOUNDARY.md).
In particular the joint cover Z_tilde -> P1 has constant group
G times C2, the quadratic cover is geometrically disjoint from Z,
and identity is the only g in G scalar on both original inputs V,W.
The S4 specialization uses V=std_3, W=perm_4 and chi=chi_u.
Classical finite-cover cohomology and curve duality remain imported
results; no new arithmetic RH theorem or priority claim is made.

## 1. Multiplication before cohomology

The Segre algebra R=direct_sum_n Sym^n(V) tensor Sym^n(W) has its
native multiplication R_n tensor R_m -> R_{n+m}. The quadratic
cover supplies the algebra 1 plus chi, with the multiplication
chi tensor chi -> 1 coming from its deck action. On the common
unramified open set, form the actual two-colour algebra

    B=R tensor (1 plus chi),
    B_{n,epsilon}=R_n tensor chi^epsilon,
    (n,epsilon)*(m,eta)=(n+m,epsilon+eta modulo 2).

The epsilon=0 part is R itself. The epsilon=1 part is the fixed
twist M, a graded R-module, but is not closed under its own
multiplication: the product of two odd-colour elements lands in
epsilon=0. The diagonal epsilon=n modulo 2 part is the unital
graded subalgebra A, with

    A_n tensor A_m -> A_{n+m}.

Equivalently it is the Segre construction on the actual joint-cover
inputs V'=V tensor chi and W'=W. The central deck involution acts
as degree parity. No multiplication was recovered by fitting a
Hilbert series.

Extending by j_* preserves the given multiplication maps via the
usual lax monoidal map j_*F tensor j_*H -> j_*(F tensor H).
This does not claim that j_* is strongly monoidal. At a ramified
point the full invariant source and its multiplication must still
be used; replacing them by tensor products of invariant inputs is
the obstruction already exhibited in the S3 ramification packet.

## 2. Distinct finite sources and their ordinary completions

The exact finite-grade L-functions are

    L(A_n,T)=L(R_n,T) for n even,
             L(R_n tensor chi,T) for n odd.             (2.1)

Consequently their cohomology is the untwisted source in the even
grades and the fixed-twist source in the odd grades. Using the actual
finite multiplicity spaces and fixed finite Frobenius realizations,
the Hilbert sum again has polynomial grade growth. The ordinary
cohomological Fredholm ratio is

    L_A(z,T)=product_{n even} L(R_n,Tz^n)
                     product_{n odd} L(R_n tensor chi,Tz^n).    (2.2)

It is jointly meromorphic for |z|<1 and all T, and equals the actual
closed-point Euler product in |T|<1/Q, with weight z^{n deg v}.
It is not the same operator or function as the entire fixed-twist
determinant L_M. Grade zero in (2.2) is Z(P1,T), whereas grade zero
in L_M is L(chi,T). For the actual chi_u cover of P1 used by the
S3 and S4 sources this last factor is one; a general quadratic cover
of positive genus can have a nontrivial grade-zero H^1 polynomial.

For S4, write a_n=m_{1,n}, and let h_n^0,h_n^chi be the previously
proved untwisted and fixed-twist H^1 dimensions. Then

    H^0(A_n)=H^2(A_n) have dimension a_n for n even,
                                           and zero for n odd;
    dim H^1(A_n)=h_n^0 for n even, h_n^chi for n odd.     (2.3)

Thus the principal poles occur only at the even grades. For fixed
0<|z|<Q^{-1/2}, the zero radii Q^{-1/2}|z|^{-n} cannot cancel
the even-grade pole radii |z|^{-2k} and Q^{-1}|z|^{-2k}.
There are infinitely many such poles, preventing a fixed-z
reciprocal functional equation with a nonzero rational T-prefactor.
This is a scoped statement about finite prefactors, not an exclusion
of every alternative regularization or infinite completion.

On the S4 source a_n grows polynomially and is positive along all
sufficiently large even grades. Hence its H^0 and H^2 block operators
are in every S_p exactly for |z|<1, bounded noncompact at |z|=1,
and unbounded outside. The other blocks obey the same strict disk.
These are the R_n cohomology operators, not the exponential Lie parent.

## 3. The two scalar resonances are actual nonnegative counts

In G times C2 the only elements scalar on both inputs V',W' are
(1,+1) and (1,-1), with scalar products +1 and -1 respectively.
Therefore the full unsigned scalar-resonance theorem applies, even
though the inflated permutation input W' is not faithful on the
joint group. The signed theorem's identity-only shortcut must not
be applied to this algebra.

Let Z_m=#Z(F_{Q^m}) and Ztilde_m=#Z_tilde(F_{Q^m}). The complete
local coset weights at the two scalar elements are

    w_m(1,+1)=Ztilde_m/(2|G|),
    w_m(1,-1)=(2Z_m-Ztilde_m)/(2|G|).                  (3.1)

The first is the regular joint-cover identity coefficient. Their
sum is Z_m/|G|, obtained from the inflated G-regular representation,
which proves the second. Both are nonnegative. Geometrically,
Z_tilde -> Z has at most two rational points above each rational
point, so 0<=Ztilde_m<=2Z_m even at ramified points.

For any root of unity zeta and fixed real 0<T<1/Q, the leading
radial constant is therefore

    lim_{r->1-}(1-r)^D log L_A(r*zeta,T)
      = C/(2|G|) sum_{m>=1} T^m/m^{D+1}
          [ Ztilde_m * 1_{zeta^m=1}
            +(2Z_m-Ztilde_m) * 1_{zeta^m=-1} ].         (3.2)

Here D=r+s-1 and C=binom(D-1,r-1). Every term is nonnegative.
A closed point of Z_tilde gives a strictly positive identity term
at an extension degree divisible by both its degree and the order
of zeta. Consequently the constant is positive at every root of
unity, and |z|=1 is a meromorphic natural boundary of L_A(z,T).

This differs from the fixed-twist module: its leading constants
use the signed sequence Delta_m=Ztilde_m-Z_m, can vanish at some
orders, and require the nonzero-trace/integrality argument. The
algebra's extra scalar term does not obstruct the proof; it restores
the full positive source average appropriate to this construction.

For the S4 source D=6, C=10 and |G|=24, so the coefficient in
(3.2) is 5/24. At zeta=1 only Ztilde occurs. At zeta=-1 it is
Ztilde_m for even m and 2Z_m-Ztilde_m for odd m. Omitting the
nonidentity scalar would delete the odd terms in this latter case.

## 4. The minus-grading source is a constant quadratic twist

Let eta be the quadratic character of the constant field, taking
Frobenius to -1. Replacing chi by chi tensor eta in the input gives
R_n tensor chi^n tensor eta^n. At the m-th Frobenius power the
additional factor is (-1)^{nm}. Hence its completed function is
exactly L_A(-z,T).

The corresponding actual quadratic cover Z_tilde^eta -> Z is the
constant quadratic twist of Z_tilde. In the odd-characteristic Kummer
model this multiplies the radicand by a nonsquare constant. Its point counts are

    #Z_tilde^eta(F_{Q^m})=Ztilde_m for m even,
                           2Z_m-Ztilde_m for m odd.     (4.1)

At ramified points both double covers have the same single point;
over unramified rational points the two quadratic splitting types
are exchanged in odd extensions and agree in even extensions.
Thus the positive constant at zeta=-1 is itself the ordinary
identity-count constant of a genuine constant-twisted source.
This provides an arithmetic meaning for the sign change of the
grading parameter, and requires the extension-degree parity.

## 5. Ramification and finite duality preserve grade parity

At S4 infinity the even grades in A use the old untwisted inertia
invariants, while the odd grades use the diagonal twisted inertia
from the preceding packet. Thus for q=3 modulo 4 an odd-grade
first trace can vanish without its local denominator disappearing.
The actual second Frobenius power still detects the invariant space.
At u=0 the odd grades have zero stalks, whereas the even grades
retain their untwisted source stalks.

Set kappa_n=h_n^0/2-a_n in even grades and kappa_n=h_n^chi/2 in
odd grades. The actual finite-cutoff source functional equation is

    L_{A,N}(z,T)=Q^{K_N}T^{2K_N}z^{2W_N}
                              L_{A,N}(1/z,1/(QT)),
    K_N=sum_{n<=N} kappa_n, W_N=sum_{n<=N} n*kappa_n.   (5.1)

For S4, d_n~n^5/12 and the even and odd leading coefficients of
kappa_n are 3d_n/4 and 5d_n/4 respectively. Summing the two parity
subsequences gives

    K_N~N^6/72,            W_N~N^7/84.                 (5.2)

Equivalently this is the unsigned joint-cover average
(g(Z_tilde)-1)/|G times C2|=(49-1)/48=1 multiplying d_n.
Grade zero contributes -1, as it does for the untwisted principal
factor. The divergent exponents remain a precise barrier to taking
an ordinary infinite limit of the finite duality prefactor.

## 6. Replay boundaries

The replay should use the same frozen S4 and quadratic-cover sources
as the preceding analytic adapter, rather than produce a third
independent polynomial reconstruction. It checks the even/odd
cohomology assignments, actual multiplication parity, full infinity
factors, the nonnegative counts (3.1), and the constant-twist parity
formula (4.1). A grade-two comparison must say which source is
being tested; agreement in grade one does not identify the algebra
with the fixed-twist module.

The analytic boundary statements follow from the full source proofs.
Finite point counts, parity tables and interval probes do not replace
the all-root argument or the classical purity and duality inputs.

For explicit cohomological assembly write A_rho(z) for the original
S4 multiplicity series and set

    E_rho(z)=(A_rho(z)+A_rho(-z))/2,
    O_rho(z)=(A_rho(z)-A_rho(-z))/2.

If ell_rho^0(m) and ell_rho^chi(m) are the complete untwisted and
fixed-twist local trace sums over F_{Q^m}, then

    log L_A(z,T)=sum_m T^m/m sum_rho
       [E_rho(z^m)ell_rho^0(m)+O_rho(z^m)ell_rho^chi(m)]. (6.1)

The parity projection is performed at the grade level before taking
Frobenius powers. In particular A_rho(-z^m), as it appears here, is
not interchangeable with A_rho((-z)^m) when m is even.

For the S4 scalar constants at zeta=1 or -1, a conservative tail
after m=M is

    20(QT)^{M+1}/[(M+1)^7(1-QT)].                      (6.2)

The corresponding sixth-order scaled radial logarithm at z=r or -r
has tail at most

    20(QT)^{M+1}/[(M+1)(1-QT)].                        (6.3)

Indeed each selected scalar count is at most 48(Q^m+1), the
coefficient is 5/24, and (1-r)^6 F_e(r)<=10. The full local trace
averaging mass is Q^m+1, so the radial estimate also follows
directly from the actual joint-cover source, without signs or
absolute values of separate cohomological constituents.

For the independent determinant-logarithm check, the positive-grade
total cohomology dimension is at most 6d_n: the even untwisted
constituents satisfy this bound including H^0 and H^2, and the odd
fixed-twist constituents have H^1/dimension ratios at most six.
Purity bounds each Frobenius eigenvalue by Q in absolute value, so
the m-th power trace is bounded by the dimension times Q^m,
independently of the chosen fixed Hermitian norms. Thus the preceding
packet's two positive-grade tail bounds remain
valid unchanged with coefficient six. The grade-zero Z(P1,T) factor
is kept as a separate exact rational number; its sign is not absorbed
into a real logarithm beyond the initial arithmetic Euler disk.
