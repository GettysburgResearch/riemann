# An infinite pole-clearing source can lose the disks of every finite stage

Status: proposed source-specific theorem, awaiting frozen-commit independent review.
Scope: the actual S3 coherent source over F7 and its extension to F49; ordinary
constructible sheaves in each finite grade, a formal graded limit, and explicitly
specified Hilbert direct sums. No number-field or RH conclusion is asserted.

The source is frozen at PR769 commit
`7b320b3a9a55a16e73d99dd9bbab5bf592d50c93`. The imported sheaf construction,
source characters and arithmetic pole statements are in
`../koszul-analytic-parent/CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md`,
`FINITE_RESONANT_COHERENT_POLES.md` and `S3_WEIGHT_CIRCLE_POLE_DIVISOR.md`.
This note does not modify those reviewed sources.

## 1. An actual degreewise limiting algebra

Keep the source notation A_n=R_n tensor chi^n and let M_n be its untwisted
Koszul Lie dual. Write

    M_n = A_n^triv copies of 1 + B_n copies of sign + C_n copies of Std,
    T_n = B_n sign + C_n Std,   n even.

The multiplicity symbol A_n^triv in this display is not the coherent grade A_n.
The nontrivial summand T_n is defined by the finite-group averaging idempotent.
For even N>=2 the existing construction is

    B^(N) = (direct-sum_j j_*A_j)
            tensor Sym(direct-sum_(even 2<=n<=N) j_*T_n [grade n]).

Here every j_* is ordinary and every displayed grade is finite dimensional.
Use the unit in new symmetric generators for the inclusion B^(N)->B^(N+2).
In a fixed total grade m only n<=m and finitely many weighted partitions of m
contribute. Consequently these inclusions stabilize in each grade and define
an actual graded algebra B^(infinity), with each grade constructible. This is
not one finite-rank constructible sheaf and no topology is hidden in the notation.

The full place-Hilbert Euler series is well defined formally: a coefficient
of z^m uses only closed points of degree at most m and finite stalk grades.
It therefore commutes with this degreewise stabilization. If H_N is the full
Euler function of B^(N), there is a unique formal H_infinity with integer
coefficients and H_N congruent to H_infinity modulo z^(N+2).
This statement alone says nothing about analytic convergence on a common disk.

## 2. A sharper source multiplicity formula

Put a_n=B_n+C_n. A transposition s acts by -1 on sign and has one negative
eigenvalue on Std. Thus a_n=dim(M_n)^(-), the actual transposition anti-invariant
dimension. It is not the anti-invariant dimension of the original Segre algebra.

The frozen equivariant PBW formula is

    tr(g|M_n)=(-1)^(n+1)/n sum_(d|n) mu(d) b_(n/d)(g^d),

where b_r(e)=4-(-2)^r and b_r(s) is 4 for even r and 0 for odd r.
For even n, subtract the s-character from the identity character. Every even
divisor d cancels because s^d=e. For odd d, n/d is even, and
b_(n/d)(e)-b_(n/d)(s)=-2^(n/d). Hence

    a_n = 1/(2n) sum_(d|n, d odd) mu(d) 2^(n/d),       n even.       (2.1)

In particular a_2,a_4,a_6,a_8,a_10,a_12 are 1,2,5,16,51,170.
Writing n=2j gives

    b_j:=a_(2j)=4^j/(4j)+e_j,
    |e_j| <= (4^(floor(j/3)+1)-4)/(12j).                            (2.2)

Indeed every proper odd divisor is at least three, and the distinct integers
j/d lie between 1 and floor(j/3). Bound their powers by the full geometric
sum. This proves the exponential remainder without extrapolating a finite table.

## 3. The two arithmetic sources and an exact base-change identity

Use the already constructed curves

    E: y^2=x^3+x,     D: v^2=-4-27u^4

over F7. Both are genus-one smooth proper curves with eight rational points;
the quartic D has two rational points at infinity. Thus both polynomials are

    P_7(T)=1+7T^2.

An independent complete enumeration of seven residue classes checks these
point counts. The source geometry and genus are imported, not inferred merely
from seven point counts. Squaring the Frobenius roots gives trace -14 over F49,
so both polynomials become P_49(T)=(1+7T)^2. No F49 enumeration is used.

Remove the already present degree-two multiplier and define the pure ladders

    K_(7,N)(z)=product_(even 4<=n<=N) (1+7z^(2n))^a_n,
    K_(49,N)(z)=product_(even 4<=n<=N) (1+7z^n)^(2a_n).              (3.1)

Then H_N=H_2 K_N in each field, and exactly for every finite even N,

    K_(49,N)(z^2)=K_(7,N)(z)^2.                                    (3.2)

The grading substitution is essential. Equation (3.2) is compatible with
constant-field extension; differing scalar radii are not a failure of sheaf
base change. The same identity holds for the formal limits.

## 4. Sharp scalar radius and a fractional singularity

Introduce x=z^4 for F7 and x=z^2 for F49. Both cases reduce to

    K_r(x)=product_(j>=2) (1+7x^j)^(r b_j),   r=1 or 2.             (4.1)

The product converges normally and is nonzero for |x|<1/4. In that disk use
the logarithm defined at zero. With beta=7r/4, equations (2.2) give

    log K_r(x) = -beta log(1-4x) + R_r(x),
    R_r(x) = -7r x + 7r sum_(j>=2) e_j x^j
        + r sum_(j>=2) b_j [log(1+7x^j)-7x^j].                    (4.2)

The remainder R_r is holomorphic on |x|<1/3. To verify this, on every compact
disk |x|<=rho<1/3, the error series from e_j converges by (2.2). Also
|7x^j|<=7rho^2<1 for j>=2 and

    |log(1+u)-u| <= |u|^2/[2(1-|u|)].

The remaining series is dominated by a constant times sum 4^j rho^(2j)/j.
Every logarithm here uses its convergent power series; no branch is chosen
after a zero has been crossed. Consequently

    K_r(x)=(1-4x)^(-beta) A_r(x),   A_r=exp R_r,                    (4.3)

where A_r is holomorphic and nonzero on |x|<1/3 and A_r(1/4)>0.
Since beta is 7/4 or 7/2, the point x=1/4 is a non-meromorphic branch
singularity. Thus the exact Taylor radii of the limiting K functions are

    radius K_7 = 1/sqrt(2),     radius K_49 = 1/2.                  (4.4)

These are consequences of (4.2), not fits to finite coefficient growth.
The formal limit and the normally convergent product agree on their common
disk because each coefficient stabilizes.

## 5. The full source limit loses the finite-stage disks

For F7 the imported nonresonant source theorem gives H_2 Taylor radius
7^(-1/8)>1/sqrt(2). For F49 the source is fully resonant and H_2 is holomorphic
on |z|<1. In both cases H_2(0)=1, so it is not identically zero.

At a positive point of (4.4), H_2 is holomorphic and has a finite integer zero
order, possibly zero. Multiplication by it cannot remove the noninteger exponent
in (4.3). Therefore the full formal source H_infinity has the same exact radius
as K_infinity. In particular

    limsup |[z^m]H_(infinity,7)|^(1/m)=sqrt(2),
    limsup |[z^m]H_(infinity,49)|^(1/m)=2.                           (5.1)

Every finite H_N has the inherited meromorphic continuation and natural boundary
at |z|=1. Its guaranteed holomorphic disk is |z|<Q^(-1/[2(N+2)]), and in the
fully resonant case every finite H_N is holomorphic on the unit disk. The disks
approach one while the degreewise limiting source has the smaller radii (5.1).
This is an explicit source-defined failure of the inference from finite pole
clearing to analytic convergence of an infinite completion.

## 6. Finite critical products and the fixed-factor warning

At x=1/4, for J=floor(N/2),

    log K_(r,N)(1/4) = r sum_(j=2..J) b_j log(1+7*4^(-j))
                      = beta sum_(j=2..J) 1/j + c_r + o(1).        (6.1)

The error series converges absolutely: (2.2) controls the linear error and
the logarithm estimate in Section 4 controls the quadratic error. Since the
harmonic sum minus log J has a finite limit, there is C_r>0 such that

    K_(r,N)(1/4) ~ C_r N^beta.                                    (6.2)

These are critical values in x; substitute z=1/sqrt(2) or 1/2 respectively.
The statement concerns the pure multiplier. The raw H_N value at that point
can remain zero if its fixed H_2 factor vanishes there. Such a finite zero
does not remove the branch or restore local normal convergence.

## 7. The actual operator has a different domain

On the actual H^1(P1,j_*T_n), dimension 2a_n, Frobenius has eigenvalues of
absolute value sqrt(Q). Use the same orthonormal eigenbasis norm on every copy
of each of the two fixed elliptic Frobenius spaces. Define

    D_Q(z)=direct-sum_(even n>=4) z^n Frob_Q | H^1(P1,j_*T_n).

For every finite p>=1 its Schatten p-sum is exactly

    Q^(p/2) sum_(even n>=4) 2a_n |z|^(pn).

Equation (2.2) proves membership precisely for |z|<2^(-1/p); at equality the
positive harmonic tail diverges. The operator is compact precisely for |z|<1.
For |z|<1/2 the ordinary Fredholm determinant det(1-D_Q(z)) equals K_Q(z),
with equality of the source block determinants. Over F7 the scalar determinant
continues to |z|<1/sqrt(2), but this does not enlarge the trace-class domain.

The determinant, the formal source limit, the finite-stage functions and the
meromorphic continuation of each finite stage are thus distinct constructions
with explicitly compared domains. No topology has been chosen to force an
ordinary determinant to exist beyond its actual ideal domain.

## 8. Verification and limits

The replay authenticates frozen source blobs, compares independent source
character formulas, enumerates only F7, checks Frobenius squaring, compares two
formal coefficient algorithms, tests stabilization and the exact substitution,
and gives rational logarithm intervals for finite critical products. Tests do
not establish normal convergence, branch singularities, asymptotics or operator
ideal membership; those are proved above and require independent proof review.

No infinite-rank constructible sheaf, canonical choice-free topology,
archimedean completion, number-field transfer or RH implication is claimed.
