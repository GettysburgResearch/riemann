# The global grading has a source-forced natural boundary

This companion concerns the global cohomological completion Lcal(z,T)
of the preceding note. It quantifies its finite-cutoff functional
equation, explains the Hilbert-space cost of restoring duality, and
proves a meromorphic natural boundary in the grading variable z. The
last result uses point counts on the actual genus-three S3 Galois
closure, not a chosen sequence of positive coefficients.

The natural-boundary assertion below is for fixed real 0<T<1/Q only.
It is not asserted for every complex T, and it is not a claim about
the boundary of the T-plane. The mechanisms are classical operator and
graded-product mechanisms; external priority is not claimed.

## 1. The complete finite-cutoff functional equation

Write L_n(t)=Z(P^1,t)^a_n P_D(t)^b_n P_E(t)^c_n, and put

    kappa_n=b_n+c_n-a_n=(d_n-r_n)/3-t_n,

where d_n=(n+1)binom(n+2,2), t_n=n/2+1 for even n and zero otherwise,
and r_n=1 if 3 divides n and zero otherwise. In particular kappa_0=-1.
The source curve functional equations give exactly

    L_n(t)=Q^kappa_n t^(2kappa_n) L_n(1/(Qt)).              (1.1)

Let Lcal_N be the product of grades 0 through N. Set

    K_N=sum_(n=0)^N kappa_n,
    W_N=sum_(n=0)^N n kappa_n.

Then, wherever the finite expressions are defined, the meromorphic
identity is

    Lcal_N(z,T)=Q^K_N T^(2K_N) z^(2W_N)
                         Lcal_N(1/z,1/(QT)).              (1.2)

The grade-zero source is included. Omitting it changes K_N by one.
For exact formulas put E=floor(N/2), J=floor(N/3), and
S_j(M)=sum_(n=0)^M n^j for j>=1. Directly summing the source character
formula gives

    K_N=[S_3(N)+4S_2(N)+5S_1(N)+2(N+1)]/6
                 -(J+1)/3-(E+1)(E+2)/2,

    W_N=[S_4(N)+4S_3(N)+5S_2(N)+2S_1(N)]/6
                 -S_1(J)-2[S_2(E)+S_1(E)].                (1.3)

Thus K_N~N^4/24 and W_N~N^5/30. These divergent native exponents
are explicit, rather than an unspecified correction to an infinite
functional equation. Formula (1.2) also transforms |z|<1 to |1/z|>1,
outside the source trace-class domain. Neither defect is repaired by
formally retaining (1.2) at N=infinity.

## 2. Compactness and perfect pure-weight duality cannot coexist

The following elementary obstruction applies to any infinite-dimensional
complex Hilbert space. Suppose a bounded perfect bilinear pairing is
represented by a bounded isomorphism J:H -> H', and a bounded operator
K satisfies

    K' J K = Q J,          Q!=0.                           (2.1)

Then K is not compact. Indeed Q^(-1)J^(-1)K'J is a bounded left inverse,
so compactness of K would make the identity operator compact. This
argument does not assume positivity or a Hermitian pairing.

For the actual source H^1 family, the undamped direct sum of the finite
Frobenius modules carries the source Poincare pairing with multiplier Q.
Use the real source tensor pairings on its multiplicity spaces and the
same fixed finite curve pairings in each copy. They are uniformly bounded
and perfect under the previously fixed norms. The undamped Frobenius is
bounded and invertible, but not compact. Grading makes its operator
trace class; it cannot simultaneously retain (2.1) on the same infinite
Hilbert space with any bounded perfect pairing.

There is a precise, limited way to retain duality. Let H_a be the source
H^1 direct sum with norm

    ||v||_a^2=sum_n exp(2an)||v_n||^2,        a real.

The source pairing identifies H_a with the continuous dual of H_(-a).
For z=exp(-s), s>0, the actual damped Frobenius K_s=exp(-sN)F gives a
bounded isomorphism H_a -> H_(a+s). Its oppositely damped partner
K_(-s)=exp(sN)F is a bounded isomorphism H_(-a) -> H_(-a-s), and

    B(K_s v,K_(-s)w)=Q B(v,w).                            (2.2)

This follows grade by grade and extends by continuity. The inclusion
H_(a+s) -> H_a has singular values exp(-sn) with polynomial source
multiplicities, hence lies in every Schatten class. Composing it with
K_s gives the compact endomorphism used in the global completion.
The inverse damping is unbounded as an endomorphism of H_a. The scale
of spaces restores a coherent duality between different spaces, but
does not supply a second ordinary Fredholm determinant on the same
space or remove the divergent finite prefactor (1.3).

## 3. The actual Galois closure controls the leading singularity

Let Z be the smooth genus-three S3 Galois closure supplied by the
geometric companion. It has affine equations

    y^2=x^3+Ax+B,       v^2=-3x^2-4A,

and source cohomology H^1(Z)=H^1(D) direct_sum H^1(E)^2. Write
Z_m=#Z(F_(Q^m)), e_D(m)=tr(F_D^m), and e_E(m)=tr(F_E^m). Then

    Z_m=1+Q^m-e_D(m)-2e_E(m).                              (3.1)

Substituting the three rational source sectors into log Lcal gives

    log Lcal(z,T)=sum_(m>=1) T^m/m *
       [alpha_m F_e(z^m)+beta_m F_s(z^m)+gamma_m F_c(z^m)],

    alpha_m=Z_m/6,
    beta_m=(1+Q^m+e_D(m))/2,
    gamma_m=(1+Q^m-e_D(m)+e_E(m))/3.                        (3.2)

This logarithm is the one equal to zero at T=0 in the initial domain;
for fixed real 0<T<1/Q it is a single holomorphic logarithm on |z|<1.
All its individual determinant factors are nonzero there.

The alpha_m are actual source counts divided by six. They are not
assumed to be strictly positive at every small m. The two infinity
points of Z are defined over an extension of degree at most two,
because their residue condition is the square root of -3. Therefore

    Z_(2h)>=2 for every h>=1.                              (3.3)

Also the degree-six source map Z -> P^1 gives Z_m<=6(Q^m+1).
These direct geometric facts already suffice for convergence and strict
positivity of the constant below; the stronger Weil bounds are not
needed for its sign.

## 4. A dense family of source-forced singularities

Fix real 0<T<1/Q and a root of unity zeta of exact order h. Then

    limit_(r increases to 1) (1-r)^4 log Lcal(r zeta,T)
        = C_h(T)
        = 1/2 sum_(h divides m) Z_m T^m/m^5 > 0.           (4.1)

Proof. For each fixed m,

    (1-r)^4 F_e((r zeta)^m) -> 3/m^4 if h divides m,
                              0 otherwise.

The scaled F_s and F_c terms tend to zero, even when their order-two
and order-one denominators resonate. For uniform domination use
|1-r^m zeta^m|>=1-r^m>=1-r. Thus the scaled absolute values of
F_e,F_s,F_c are bounded respectively by 3,1,1. Their coefficients grow
at most by a constant times Q^m, and sum (QT)^m/m converges. Dominated
convergence in (3.2) proves (4.1). Every summand in its final constant
is nonnegative; the m=2h term is positive by (3.3). In particular

    C_h(T) >= T^(2h)/(2h)^5.                              (4.2)

Taking real parts in (4.1) shows that |Lcal(r zeta,T)| grows like the
exponential of a positive constant times (1-r)^(-4), at the level of
this logarithmic asymptotic. Such growth is faster than any finite pole.
Consequently Lcal has no meromorphic continuation through zeta.
Roots of unity are dense on |z|=1, so this circle is a meromorphic
natural boundary in z for the stated fixed real T.

This directly obstructs continuing the source grading to 1/z across
any arc in this parameter range. It strengthens the earlier failure
of a fixed-z finite functional equation. It does not rule out a
different object, different topology, infinite completion factors, or
special complex T outside the hypotheses. In particular T=0 gives
Lcal=1 and is deliberately excluded.

## 5. Bounded exact controls

The replay checks (1.3) against the exact source multiplicities and
checks (1.2) as a rational identity for bounded finite cutoffs, using
the actual geometric P_E and P_D. It retains kappa_0=-1 and the source
parity and mod3 corrections.

For the boundary it computes Z_m from the frozen source Frobenius
modules, with the first two degrees independently checked against
complete primitive point counts. The series for C_h is enclosed by
truncating at m=M; the omitted positive tail is at most

    4 (QT)^(M+1)/[(M+1)^5(1-QT)].                         (5.1)

This follows from Z_m<=6(Q^m+1)<=8Q^m for Q>=5. A conservative bound
for the tail of the scaled logarithm in (4.1) is

    8 (QT)^(M+1)/[(M+1)(1-QT)].                           (5.2)

One may use the source curve bounds or the already established Weil
bounds to obtain the coefficient estimate in (3.2) needed for (5.2).
The replay evaluates its finite part in Q(omega), omega^2+omega+1=0,
at roots of unity of orders 1,2,3 and rational r. It checks the real
part using Re(a+b omega)=a-b/2. No approximate roots, floating-point
logarithms, or fitted singularity constants are used.

The finite calculations are controls of the proved formulas. Density
of roots of unity, the all-h positivity argument, compactness
obstruction, and meromorphic natural-boundary theorem are not inferred
from a finite list of examples.
