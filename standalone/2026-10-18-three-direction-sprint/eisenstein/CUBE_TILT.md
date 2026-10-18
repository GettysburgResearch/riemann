# Damping only the cubes: exact target preservation and the full transform price

Status: **PROPOSED arithmetic deformation and analytic component estimates.**
No new zeta zero-free boundary is proved. The deformation is defined as a
complete arithmetic sum and, equivalently, an absolutely convergent
convolution of legal original theta sums. It is not declared to be one
unchanged spherical theta vector.

Fix one CT-admissible cyclotomic field, for example F=Q(zeta_12), with its
actual S, generator conventions, vartheta and zero extensions. Use the
complete native Gaussian B_m(Z) of `eq:B`. For a real v>=0 define

    B_(m,v)(Z)=sum_(c squarefree,n)
       gamma_2(c) vartheta(c n^3) chi_(c n^3)(m)
       /(sqrt(Nc) (Nn)^(1+v)) P_G(Nc (Nn)^3/Z).          (1)

The extra factor damps only n. Every squarefree c, unrestricted n, shared
c,n prime and nonunit zero remains. Absolute Gaussian convergence holds
for every fixed m,Z,v.

## 1. Exact local Poisson calculation

Besides CT's pinned `eq:principal-factor`, the full local calculation was
checked in OpenAIPrimitive at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, file
[05-poisson.tex](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex),
`eq:exact-Euler-factor`, `eq:C-local-values` and `eq:Euler-good-exact`.
This is a finite Fourier calculation with its common-prime unit masks.

Write l=v_P(n), e0=v_P(c) in {0,1}, t=e0+3l, and J=6j in the principal
frequency row. The finite local sums vanish unless t=0 or t=6d or 6d+1.
For t=6d and 6d+1 the cube exponent is EXACTLY l=2d. Consequently (1)
replaces, throughout the principal local geometric series,

    E= vartheta(P)^6 Q^(4-6xi-6z)
    by E_v= vartheta(P)^6 Q^(4-6xi-6z-2v).               (2)

The t=0 term and the first squarefree t=1 term are unchanged. In particular
the reciprocal target coefficient remains -Q^(-xi). With
V=Q^(-6z), W=Q^(-w), D=Q^(-xi), the exact local expression is

    F_v=1/(1-V)+W/(1-W)
        +E_v/(1-E_v)[(1-Q^(-1))/(1-V)+W]
        -D/(1-E_v)[1+(Q-1)WV/(1-V)].                   (3)

At the double residue w=1,z=1/6 its correction is therefore

    H_(v,P)(s)=(1-Q^(-2))
       [1-(1-Q^(-1))Q^(-s)-vartheta(P)^6 Q^(2-6s-2v)]
       /[(1-vartheta(P)^6 Q^(3-6s-2v))(1-Q^(-s))].     (4)

The scalar c0 and the squarefree target 1/zeta_F^S(s) are unchanged. This
is not inferred from changing a bare-vector asymptotic: (2)--(4) come from
the full native Poisson shell calculation.

For EVERY v>=1/2, the complete product H_v is holomorphic and nowhere zero
on Re s>1/2. Local nonvanishing follows as in H_FACTOR.md from

    (1-Q^(-1))Q^(-sigma)+Q^(2-6sigma-2v)<1.

Its difference from one is
O(Q^(-2)+Q^(-1-sigma)+Q^(3-6sigma-2v)), summable for sigma>1/2,v>=1/2.
Thus the modified PRINCIPAL arithmetic detector retains every hypothetical
nontrivial target zero. A physical upper bound strong enough to exploit
that detector is a separate task.

More generally H_v=L(6s-3+2v,vartheta^6)R_v, with R_v holomorphic and
nonzero for Re s>1/2 and v>=0. At a fixed target zero rho in that region,
some finite v-derivative of H_v(rho) at v=0 is nonzero: the angular
L-function is entire and not identically zero and its zero has finite
order. These derivatives act on H, not on 1/zeta. The actual arithmetic
probes insert (-log Nn)^j in (1). Their complete analytic norms still have
to be paid; a finite order cannot be assumed uniformly without proof.

There is also a complete inverse resource, rather than just pointwise
nonvanishing. The Dirichlet-algebra proof in H_FACTOR.md with its sixth
coefficient multiplied by Q^(-2v) gives

    ||R_v||_sigma+||R_v^(-1)||_sigma
        <=C_(F,S) zeta_F^S(6sigma-2+2v).

For v>=1/2 and sigma>=1/2 this last zeta argument is >=2. The remaining
shifted L-factor and its Euler inverse have absolute norms at most
zeta_F^S(6sigma-3+2v). Consequently, uniformly for v>=1/2 and
1/2<sigma<=3/4,

    ||H_v||_sigma+||H_v^(-1)||_sigma
       <=C'_(F,S) zeta_F^S(6sigma-2)
       <=C''_(F,S)/(sigma-1/2).                         (4a)

These are full coefficient norms, so they give bounded causal inverse
operators on every weighted past Lp horizon just as in H_FACTOR.md (9).
This step does not assume any Hecke zero-free theorem inside its critical
strip: the shifted L here is in absolute convergence.

## 2. An exact full convolution in the original legal sums

Put b_m(P)=vartheta(P)^3 chi_P(m)^3/Q. The zero value when P divides m is
retained. Write A_m for the c-sum in (1) with n=1. Then

    B_m(Z)=sum_n b_m(n) A_m(Z/(Nn)^3),
    B_(m,v)(Z)=sum_n b_m(n)(Nn)^(-v) A_m(Z/(Nn)^3).

The b_m(n) are completely multiplicative, including their zero values.
Dirichlet convolution gives the exact relation

    B_(m,v)(Z)=sum_n c_v(n) chi_n(m)^3 B_m(Z/(Nn)^3),    (5)

where c_v(1)=1 and at each exterior prime

    c_v(P^j)=-(1-Q^(-v)) vartheta(P)^(3j)
                              Q^(-j-(j-1)v), j>=1.    (6)

Its local operator is the resolvent

    (1-b_m(P) T_(Q^3))/(1-Q^(-v)b_m(P) T_(Q^3)),
    T_a A(Z)=A(Z/a).                                   (7)

All sums in (5) are absolutely convergent for fixed m,Z by Gaussian
flatness and polynomial ideal counting. The inverse has local coefficient
(1-Q^(-v))vartheta(P)^(3j)Q^(-j) for j>=1. In particular

    |c_v(n)|<=1/Nn,                                    (8)

uniformly in v>=0, and both full operators preserve all nonunit masks.

For every positive sigma, every 1<=p<=infinity and every past horizon T,
the forward and inverse operators in (5) obey

    ||C_v^(+/-1) A||_(sigma,p,T)
        <=zeta_F^S(1+3sigma)||A||_(sigma,p,T).            (9)

This also holds with an arbitrary fixed row l^2 space inside the norm.
Proof: put u=Q^(-1-3sigma), r=Q^(-v). The local absolute masses are
1+(1-r)u/(1-ru) and 1+(1-r)u/(1-u), respectively; both are at most
(1-u)^(-1). Multiplication by chi_n(m)^3 contracts the row norm. Causal
dilation, Minkowski and the complete Euler product prove (9). No cutoff
or inverse reciprocal-L bound occurs.

## 3. Why this is not a free theta/profile substitution

Every unramified local vector in the original fixed finite-level theta
realization is spherical. Its pure-cube ratio W_P(a(P^3))/W_P(1)=Q^(-1)
is fixed by the representation. Damping n=P changes that ratio to
Q^(-1-v) at EVERY exterior prime. A change at finitely many local vectors
cannot make that all-prime change. Spherical Hecke operators act by scalars
on the one-dimensional spherical line and do not change this ratio.

Nor is it just a new fixed archimedean norm profile. In F=Q(zeta_12), at a
completely split rational prime p there are at least three distinct prime
ideals P1,P2,P3 of norm p. The theta indices P1^3 and P1P2P3 have the same
norm p^3, but their required cube weights are p^(-v) and 1. A single function
of the total norm cannot make both changes. This is an exact obstruction
for that claimed profile architecture, not for an infinite convolution
treated with its actual analytic cost.

Most importantly, (9) uses a POSITIVE Z-weight. The reflected physical
gain is Z^(-1/2). On that scale a dilation by (Nn)^3 costs (Nn)^(3/2),
so its prime coefficient of size Q^(-1) costs Q^(1/2). The resulting
absolute Euler resource diverges. In particular (9) does not transfer
the original CT moment with the same exponent.

HYBRID_MOMENT.md derives a weaker but complete signed quadratic-sieve
bound for (5). It retains the nonzero-frequency phases and pays all tails.
The remaining loss is explicit; the new zero-safe principal correction
alone does not yield a new zero-free boundary.

## 4. Finite-prime cube filters cannot remove the global numerator zeros

Let P0 be any finite set of exterior primes. Tilt cubes only at those
primes and leave the others unchanged. Its exact principal correction is

    H_(v,P0)(s)=H_0(s) product_(P in P0) H_(v,P)(s)/H_(0,P)(s). (10)

Each displayed LOCAL ratio is holomorphic and nowhere zero for Re s>1/2,
by the local bounds already proved. Thus every zero of H_0 in that region
is still a zero of H_(v,P0), with the same multiplicity. Every finite linear
combination of these probes also contains H_0 as a common factor.
Differentiating finitely many tilted local factors does not change that
conclusion: its principal response is H_0 times a holomorphic function.

Therefore a finite-prime calculation cannot establish the all-prime
noncancellation in (4). A growing prime cutoff needs a COMPLETE cofinal
physical-source approximation and a uniform norm/tail estimate. Convergence
of the ratios in (10) cannot be locally uniform around a zero of H_0 if
the proposed limit is H_v/H_0 with H_v nonzero there. This is an exact
finite-architecture obstruction, not an impossibility of the full filter.

## 5. The exact correlated analytic object left by the filter

Put psi=vartheta^3 and let xi_m=chi_bullet(m)^3 be the quadratic character,
retaining its additional conductor-prime omissions. The full filter has
the Dirichlet series

    sum_n c_v(n)chi_n(m)^3 (Nn)^(-s)
              =L^S(1+s+v,psi xi_m)/L^S(1+s,psi xi_m).   (11)

The scale operator in (5) uses (Nn)^3, so its Mellin-Z multiplier is

    C_v(w;m)=L^S(1+3w+v,psi xi_m)/L^S(1+3w,psi xi_m).  (12)

Its denominator is not an arbitrary new row: it is precisely the cube
completion in the original transform

    Mellin B_m(w)=e^(w^2) A_m(w)L^S(1+3w,psi xi_m),      (13)

where A_m is the uncompleted squarefree Gauss Dirichlet series, initially
in absolute convergence. Controlling (12) jointly with the actual
completed theta vector is the remaining correlated problem.

There is a tempting but invalid shortcut. At Re w=-1/2 and v=1/2, the
Hecke functional equations turn (12), after the actual primitive/omitted
local factors are restored, into a ratio involving L(1-3it) and L(3/2-3it),
with a favorable conductor factor conductor^(-1/2) and smoothing gamma
quotient. That boundary multiplier alone is not the original CAUSAL
filter. Its denominator has zeros at

    w=(rho-1)/3,

for zeros rho of the quadratic-Hecke family, between the initial absolute
line and -1/2. Moving a Mellin contour must retain all their residues.
The fact that the completed B_m transform is entire does not imply that
it vanishes at these points: the uncompleted A_m can have exactly those
completion-denominator poles. No such cancellation is assumed here.

The clean reflected sector h=f=1 has column vector gamma_2(c)/vartheta(c),
up to fixed ray factors. The filter on squarefree n has coefficients
mu_F(n)vartheta(n)^3 product_(P|n)(1-(NP)^(-v))/Nn. Thus (12)--(13) specify
the arithmetic vectors that a better dispersion estimate must exploit.
Replacing them by arbitrary independent vectors reproduces the loss in
HYBRID_MOMENT.md. For example independent fourth-moment Cauchy gives

    sqrt[(D+N^2)(D+C^2)]/N >= D/N+C,

since the squared difference is D(N-C)^2/N^2. It cannot improve the
general collapsed quadratic-sieve bound just by increasing moment order.

## 6. An exact ordinary consumer for the corrected physical principal term

Fix F=Q(zeta_12) and v>=1/2. Let E_F be the pure ideal-Mobius Gaussian in
LEGAL_FIELD.md and let E_(F,v)=H_v*E_F, where multiplication of Dirichlet
series means the complete causal ideal-norm convolution. Its transform is

    Mellin E_(F,v)(s)=exp[tau(s-c)^2] H_v(s)/zeta_F^S(s). (14)

This is the actual form of the tilted principal physical residue after
undoing its fixed scalar and D-power shift. No correction factor has been
silently dropped. The three period-12 character operators of LEGAL_FIELD
give exactly

    T_1 T_2 T_3 E_(F,v)=H_v*R,                         (15)

where R is the ordinary rational Mobius source with the same omitted
finite rational primes. For any sigma0>1, H_v has finite coefficient norm
there; hence E_(F,v) has the same source-specific all-order Gaussian
Cauchy bound as E_F, with that explicitly finite additional norm. The
three Euler--Maclaurin compressors therefore approximate (15) cofinally
with O_A((log T)^3) rational/normalized-jet probes and complete T^(-A)
weighted-past error, exactly as in LEGAL_FIELD.md.

Finally apply the COMPLETE H_v inverse from (4a). For each sigma>1/2 its
weighted Lp cost is O((sigma-1/2)^(-1)), independent of horizon. This
recovers R, including every ordinary-zeta zero and without requiring any
of the three auxiliary quadratic L-functions to be zero free in their
critical strips. The inverse is an absolutely controlled infinite Euler
operator; its cost is not counted as O(log^3 T) extra finite probes.

If the source's S is larger, first enlarge it to a fixed rationally
saturated set and use the corresponding fixed-period characters as in
LEGAL_FIELD.md section 5. All finite factors remain explicit and have
zeros only on Re s=0.

Thus the ordinary principal target can be made fully concrete in ONE
legal field, with both the arithmetic L-factor deflation and the physical
H correction paid. What remains open is a strong enough bound for this
WHOLE correlated observable and the complete nonprincipal Poisson
comparison. The current hybrid estimate gives only the exponent budget
in HYBRID_MOMENT.md, whose optimistic zero-free boundary exceeds one.
