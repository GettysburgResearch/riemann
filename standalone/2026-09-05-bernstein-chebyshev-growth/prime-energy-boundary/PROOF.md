# The actual-prime diagonal and the signed Christoffel--Darboux energy

Status: PROPOSED complete analytic proofs; independent review required.
The prime-only subexponential estimate and RH are NOT proved.
Scope: the literal primes and weights log p; all positive integer degrees.
A separate countermodel changes the weights on the same primes, not zeta.
Exact parent: PR #792 at 3b1bb5b81b36f742b6d5840088bf79a8e1519084.
What was run: the finite exact checker described in VALIDATION.md.
Smallest remaining gap: the source-specific polynomial energy bound (18).
Local labels PE-1 through PE-4 are confined to this directory.

## 1. Preserve the actual prime-only observable

Throughout, p denotes an ordinary prime, log is the natural logarithm, and

    F_n(t)=L_n^(-1)(t)=L_n(t)-L_(n-1)(t),              n>=1,
    F_0(t)=1,
    theta(x)=sum_(p<=x) log p,
    s(w)=(2-w)/(1+w).

The polynomial definition, valid also at parameter -1, is

    F_n(t)=sum_(j=1)^n (-1)^j binom(n-1,j-1) t^j/j!.

Keep exactly the parent's prime-only coefficient:

    Pcal_n=(-1)^n sum_p (log p)p^-2 F_n(3log p)
                  -3*2^(n-1)+2/3,                  n>=1.     (1)

Each prime series converges absolutely at each fixed degree. The parent
proves, using the complete higher-power source and archimedean terms,

    d_n=-(3/8)Pcal_n+r_n,       r in l^2,                      (2)
    sum_(n>=0) d_n w^n=d_0/2+(3/8)(xi'/xi)(s(w))             (3)

initially near zero; (3) then defines its meromorphic continuation on the
disk. The return to the original observable is unchanged:

    |c_n(2)| <= (8/9)sqrt(2n+1) max_(0<=j<=n)|d_j|.          (4)

The parent also gives RH iff Pcal has all-epsilon subexponential growth.
No statement in this packet assumes the conclusion of that equivalence.

It is useful to express (1) as an exact signed measure. Set

    dnu(x)=dtheta(x)-dx+dx/(2sqrt(x)),          x>=1.

Finite integration gives

    integral_1^infinity x^-2 F_n(3log x)dx=(-1)^n3*2^(n-1),
    (1/2)integral_1^infinity x^(-5/2)F_n(3log x)dx
                                                   =(2/3)(-1)^n.

Consequently

    Pcal_n=(-1)^n integral_[1,infinity) x^-2 F_n(3log x)dnu(x).
                                                               (5)

All continuous terms in (5) are part of the original correction, not
arbitrary centering. The primitive theta(x)-x+sqrt(x) is zero at x=1.

## 2. PE-1: actual-prime diagonal asymptotic

Define the positive prime diagonal

    Delta_n=sum_p (log p)^2 p^-4 F_n(3log p)^2.                (6)

**Theorem PE-1.** Unconditionally, as n tends to infinity,

    Delta_n=(2/3)n+O(sqrt(n) log(n+2)).                       (7)

Thus its complete degree-weighted diagonal satisfies

    D_N:=sum_(n=1)^N n Delta_n
       =N(N+1)(2N+1)/9+O(N^(5/2)log(N+2)).                  (8)

In particular D_N~(2/9)N^3. The constants in these asymptotic estimates
are not numerically certified here. The proof uses the classical
quantitative PNT, not RH, a zero prefix, or a prime scan.

### 2.1 Exact Laguerre identities

Ordinary Laguerre orthogonality and its three-term recurrence give

    integral_0^infinity e^-t L_j(t)L_k(t)dt=1_(j=k),
    tL_k=(2k+1)L_k-(k+1)L_(k+1)-kL_(k-1).

For k=0 the last term is zero. Since F_n=L_n-L_(n-1) and
F_n'=-L_(n-1), it follows exactly that

    integral e^-t F_n^2=2,
    integral t e^-t F_n^2=6n,
    integral t e^-t (F_n')^2=2n-1.                            (9)

For the middle identity the cross moment is
integral t e^-t L_n L_(n-1)=-n. All integrals in (9) run from zero to
infinity. No orthogonality measure at alpha=-1 is being imported at its
singular endpoint; only the ordinary alpha=0 identities are used.

### 2.2 The continuous diagonal is exactly 2n/3

Let

    g_n(x)=(log x)x^-4 F_n(3log x)^2.

Then Delta_n=integral g_n dtheta. The substitution t=3log x gives

    integral_1^infinity g_n(x)dx
       =(1/9)integral_0^infinity t e^-t F_n(t)^2dt
       =(2/3)n.                                             (10)

To replace dx by the ACTUAL prime measure dtheta requires a uniform
estimate in n; ordinary pointwise PNT is not silently interchanged with
this moving polynomial.

Put R(x)=theta(x)-x. Integration by parts yields

    Delta_n-(2/3)n=-integral_1^infinity R(x)g_n'(x)dx.         (11)

Both endpoints vanish: g_n(1)=0, while R(x)=O(x) suffices at infinity
for every fixed n. The same bound follows from PNT and a finite initial
interval, or from an elementary Chebyshev bound.

In the t coordinate the variation appearing in (11) is bounded by

    integral_1^infinity x|g_n'(x)|dx
     <=(1/3)integral_0^infinity e^-t
          [(1+4t/3)F_n^2+2t|F_n F_n'|]dt
     <=(1/3)[2+8n+2sqrt(6n(2n-1))]=O(n).                    (12)

The Cauchy--Schwarz step uses exactly (9).

The stronger localized estimate, for any T>=1, is

    integral_1^(exp(T/3)) x|g_n'(x)|dx
     <=(1/3)[2+(8/3)T+2sqrt(2T(2n-1))].                     (13)

Indeed integral_0^T t e^-t F_n^2<=2T; the other derivative integral may
be bounded by its full value 2n-1. This avoids any pointwise or
large-degree asymptotic formula for Laguerre polynomials.

### 2.3 Uniform PNT transfer

The classical de la Vallee Poussin estimate gives constants C,c>0 with

    |R(x)|/x <= C exp(-c sqrt(log x)),             x>=2.      (14)

Changing C covers the finite initial interval. Also |R(x)|/x<=B globally
for a fixed finite B. Let a=c/sqrt(3) and split (11) at x=exp(T/3).
Equations (12)--(14) give

    |Delta_n-(2/3)n|
       <=C_1(1+T+sqrt(nT))+C_2 n exp(-a sqrt T).             (15)

Choose T=max(1,4a^-2 log^2(n+2)). The second term is O(1), while the
first is O(sqrt(n)log(n+2)). This proves (7). Summing n times (7) proves
(8). This is a proof for the infinite actual-prime diagonal, not an
extrapolation from the exact finite checker.

## 3. PE-2: the complete signed energy has an explicit kernel

Define

    E_N=sum_(n=1)^N n |Pcal_n|^2.

**Theorem PE-2.** For every positive integer N,

    E_N=double_integral (xy)^-2 K_N(3log x,3log y)dnu(x)dnu(y),
    K_N(t,u)=sum_(n=1)^N n F_n(t)F_n(u)
      =N(N+1)[F_N(t)F_(N+1)(u)-F_(N+1)(t)F_N(u)]/(t-u).    (16)

At t=u the last quotient means its continuous value

    K_N(t,t)=N(N+1)[F_(N+1)(t)F_N'(t)-F_N(t)F_(N+1)'(t)].

The double integral covers [1,infinity)^2 and is absolutely convergent
at each fixed N with respect to the total variation measures, because
only finitely many logarithmic powers occur with x^-2 y^-2. It retains
all distinct-prime terms, both continuous corrections, and every cross
term. Its diagonal PRIME-PRIME part is exactly D_N in (8).

Proof. Insert (5), square, and sum the finite degree range. To verify
the displayed Christoffel--Darboux identity without using an endpoint
orthogonality theorem, apply the polynomial recurrence

    tF_n=2nF_n-(n+1)F_(n+1)-(n-1)F_(n-1),       n>=1.

Multiply the t and u versions by nF_n(u) and nF_n(t), subtract, and sum.
The interior terms telescope; the n=1 lower term is zero. The upper
boundary is N(N+1) times the numerator in (16). The diagonal limit follows
by differentiation. This is the classical CD mechanism in the specified
normalization, not a new general orthogonal-polynomial theorem.

## 4. PE-3: a polynomial energy bound would close the original target

The following is an exact endpoint, not a proved prime estimate:

    RH <=> E_N=O(N^2)
       <=> E_N is bounded by some fixed polynomial in N.     (17)

For the nontrivial forward implication from a polynomial bound, if
E_N<=C N^B, then |Pcal_N|^2<=E_N/N<=C N^(B-1). This is subexponential,
so the parent's endpoint gives RH. Conversely RH gives bounded d_N,
and r in l^2 is bounded, so (2) gives bounded Pcal_N and E_N=O(N^2).

PE-1 therefore supplies the correct unconditional normalization for a
source-specific diagonal-comparison attempt:

    E_N <= C N^A D_N,       all N>=N0,                        (18)

for any fixed finite A>=0 and C,N0. This would imply RH. Under RH it
holds already with A=0 (after adjusting constants at finitely many N).
The harmless polynomial gap between N^3 and N^2 is NOT an obstruction
to the original subexponential target. It would be incorrect to argue
that a cubic diagonal alone prevents a proof: a polynomial-loss upper
comparison with that diagonal would suffice. No such comparison for
the actual signed source has been proved here.

For scale calibration there is also an exact conditional asymptotic.
Under RH, let gamma run over DISTINCT positive zero ordinates, m_gamma
be their multiplicities, and

    k_gamma=(9/4)/(gamma^2+9/4),
    omega_gamma=2 arctan(2gamma/3),             0<omega_gamma<pi.

The centered genus-zero product gives an absolutely and uniformly
convergent Fourier series in the integer variable n:

    d_n=sum_gamma m_gamma k_gamma cos(n omega_gamma).

Finite trigonometric sums have zero mean for nonzero frequencies; different
positive ordinates give different frequencies and no sum is 2pi. Absolute
summability permits uniform finite truncation before taking the mean.
Thus the Cesaro mean of |d_n|^2 is
(1/2)sum_gamma m_gamma^2 k_gamma^2. Partial summation gives its n-weighted
mean. The l^2 remainder in (2) has vanishing n-weighted mean-square divided
by N^2, and its cross term vanishes by Cauchy--Schwarz. Consequently

    lim_(N->infinity) E_N/N^2
       =(16/9) sum_gamma m_gamma^2 k_gamma^2 >0       [RH].  (19)

Multiplicity is squared only AFTER grouping equal ordinates. No simplicity,
linear-independence, or zero-spacing assumption is made.

### Why an arbitrary-coefficient large sieve cannot supply (18)

For any M distinct primes and fixed N, form the nonzero column vectors

    v_p=(sqrt(n) p^-2 F_n(3log p))_(1<=n<=N).

They are nonzero because F_1(3log p)=-3log p. Normalize each column to
unit norm. The normalized Gram matrix is positive semidefinite, has trace
M, and has rank at most N. Its largest eigenvalue is therefore at least
M/N. An upper comparison with the diagonal valid for EVERY coefficient
vector must pay at least M/N. Taking primes in [exp(N),2exp(N)] makes
this exponential by PNT. This does not refute the special vector and
continuous cancellation in (18); it proves that a generic arbitrary-vector
bound is the wrong assertion. The literal source restrictions must matter.

## 5. PE-4: even exact prime support and the same diagonal are insufficient

This test changes the weights, not the primes. It is NOT actual zeta and
is NOT a counterexample to RH.

Let

    a_p=(log p)[1+(1/2)p^(-1/4)cos(log p)],
    theta_a(x)=sum_(p<=x) a_p.

The weights are positive, lie between (log p)/2 and 3(log p)/2, and
satisfy a_p/log p ->1. Chebyshev's bound and partial summation give

    theta_a(x)=theta(x)+O(x^(3/4)) ~ x.

In fact the same classical PNT error class (14), with possibly smaller c,
holds for theta_a-x, because x^(3/4) is absorbed in that error.
The diagonal using a_p^2 has the SAME leading asymptotic:

    Delta_(a,n):=sum_p a_p^2 p^-4 F_n(3log p)^2 ~ (2/3)n.    (20)

To justify the last assertion uniformly in n, let
vartheta_2(x)=sum_(p<=x) a_p^2/(log p). Then
vartheta_2(x)=theta(x)+O(x^(3/4)). Moreover
Delta_(a,n)=integral g_n d vartheta_2. The proof of PE-1 therefore applies
verbatim, even giving the same O(sqrt(n)log(n+2)) error class. No assertion
about the new coefficients follows from that diagonal asymptotic.

Define Pcal_(a,n) by (1) with log p replaced ONLY in the prime sum by a_p.
Then

    limsup |Pcal_(a,n)|^(1/n) >= sqrt(65/41)>1.               (21)

### Proof of the noncancelling pole

For Re s>1, put P(s)=sum_p (log p)p^-s. The exact continuation

    P(s)=-zeta'(s)/zeta(s)-sum_p sum_(r>=2)(log p)p^(-rs)

is meromorphic on Re s>1/2; the higher-power series is holomorphic there.
Its pole at 1 has residue +1, while its residue at a zeta zero of
multiplicity m in this half-plane is -m. The zero-free line Re s=1 is
the classical PNT input, not RH.

For rho=3/4+i, the weighted prime series is, initially on its convergence
half-plane and then meromorphically,

    P_a(s)=P(s)+(1/4)[P(s+1/4-i)+P(s+1/4+i)].                (22)

At s=rho the first shifted term has residue 1/4. The second is regular
because its argument is 1+2i. The unshifted term has residue -m, where m
is the multiplicity of an actual zeta zero at rho, or m=0 if there is none.
Thus the total residue is 1/4-m, which CANNOT vanish for any integer m>=0.
This argument does not assume a zero-free low prefix.

The meromorphic function

    A_a(s)=P_a(s)-1/(s-1)+1/(2s-1)

has the same pole. Both correction terms are regular at rho. Its Cayley
pullback has the nonremovable pole

    w_rho=(2-rho)/(1+rho),       |w_rho|^2=41/65<1.

Its nonconstant Taylor coefficients are exactly Pcal_(a,n). By the identity
theorem and Cauchy--Hadamard their root-limsup is at least sqrt(65/41).
If another singularity lies closer to zero, the rate is larger, not smaller;
no exact equality is claimed. This proves (21).

Consequently no theorem using ONLY exact prime support, positive log-p-like
weights, the PNT error class, and the diagonal asymptotic can establish
(18): the modified source satisfies all of them and violates every
polynomial energy bound. Any successful proof must use a property lost
in (22), such as the literal log-p weights tied to the original completed
Euler product. This is a targeted counterexample to a proposed generic
estimate, not a prohibition on source-specific arithmetic methods.

## 6. Actual attempt and disposition

The proposed completion was: pay the higher powers using HP-1, pay the
prime diagonal using PE-1, identify the full positive energy using PE-2,
and apply a polynomial-loss large-sieve comparison to get (18), then (17)
and the original inequality. The fourth arrow is not justified.
The generic arbitrary-vector version incurs exponential dimension cost;
the positive-prime-support/PNT version is refuted by PE-4. Neither result
refutes the special literal-source inequality (18), but neither proves it.

A second attempted completion via fractional radial norms is analyzed in
BOUNDARY.md. Those norms can in fact be bounded unconditionally for the
actual meromorphic source, but do not exclude interior poles. A weighted
area norm correctly distinguishes boundary and interior poles; its needed
finiteness estimate remains open.

This pass supplies an actual-prime asymptotic, an exact signed kernel, a
conditional normalization, and two precisely scoped obstructions. It does
not supply a new signed prime cancellation estimate, an unconditional
proof of (18), a new zero-free region, or a proof of RH.

## 7. Classical inputs and prior-art boundary

The new source calculations are offered without any external novelty or
priority claim. The CD mechanism, Hardy/Bergman facts in BOUNDARY.md,
logarithmic-derivative residues, and classical PNT are standard tools.

- NIST DLMF 18.3, Table 18.3.1, ordinary Laguerre orthogonality:
  https://dlmf.nist.gov/18.3
- NIST DLMF 18.9, the recurrence and formulas 18.9.13 and 18.9.23:
  https://dlmf.nist.gov/18.9
- Kiran S. Kedlaya, Notes on Analytic Number Theory, Chapter 8,
  Theorem 8.7 and the theta/psi comparison in Section 8.1:
  https://kskedlaya.org/ant/chapter-8.html
- The same notes, Theorem 8.6, gives N(T)=O(T log T), used in BOUNDARY.md.
- The existence of a critical-line zero is classical and is used only for
  the divergent p>=1 radial norms, never for the diagonal or CD theorem.
- Exact repository imports: GROWTH.md at 81e336a6d62d0963216ae05f809ec4df05447eb8;
  arithmetic-laguerre/PROOF.md at a895f734fc4243dbe81e1a0c5a17cf978a744962;
  higher-prime-powers/PROOF.md at 3b1bb5b81b36f742b6d5840088bf79a8e1519084.

The exact paths and blob identities are in SOURCE_LOCK.json. The finite
checker authenticates those parent bytes, but does not confer independent
review status on the parent's analytic arguments.
