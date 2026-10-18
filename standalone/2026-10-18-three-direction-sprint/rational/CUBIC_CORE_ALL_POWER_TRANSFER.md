# Bilinear transfer of the low-cubic-core estimate to every original input power

**PROPOSED complete source-qualified sector theorem, pending internal
review.** The high-cubic-core signed complement remains OPEN. This note
supplies the missing outer cross-component argument explicitly; it does
not invoke Minkowski on a signed dual-sector projection.

Use the exact original all-power mixed vector, row family and profiles
of `SQUAREFREE_COLUMN_ADAPTER.md`. Its outer indices are denoted g,h;
the primitive Poisson frequency below is denoted kappa. The primary
quadratic/cubic sieve and Poisson pins are exactly those specified in
`CUBIC_CORE_DUAL_SECTOR.md`.

## 1. The complete original sector and the claimed estimate

Let D,N be the ORIGINAL lengths, L=DN, and put

    C0=D+N+L^(2/3),
    H0=D^(1/3)+N^(1/3)+L^(1/6).

For every original expanded coefficient pair, apply primitive Poisson
to its actual pair character, retaining its zero-only mask and the
exact sixth-free row sieve. For every nonzero primitive dual frequency
write uniquely

    kappa=j^3 v,    v cubefree.

Let P_original,<=V denote the COMPLETE signed contribution with Nv<=V,
summed over all original d1,n1,d2,n2, all source input powers, physical
rows, shared primes, sieve indices, local classes and dual profile tails.
The true primitive-principal contribution is treated separately by
the complete O(U^(1+epsilon)) bound already proved for the original
source in `ACTUAL_SIXTHFREE_SECTOR.md`.

We claim, for polynomially bounded V>=1,

    |P_original,<=V| <<_epsilon (UDNV)^epsilon
      [ U^(2/3)V^(2/3)+U^(3/4)C0^(1/4)V^(3/4)
                              +U^(5/6)H0 V^(5/6) ].     (1)

All common smooth height costs and fixed input/row masks have the
same qualified uniformity as in the squarefree-column theorem. At the
synchronized corner D=U,N=sqrt(U), (1) gives

    |P_original,<=V| << U^(2/3+epsilon)V^(2/3+epsilon)
             +U^(1+epsilon)V^(3/4+epsilon)
             +U^(7/6+epsilon)V^(5/6+epsilon).            (2)

Thus V=U^(1/25) pays this COMPLETE original dual sector at
U^(6/5+epsilon). Neither the complementary Nv>V sector nor the full
mean has been bounded. The long-inverse edge of the full witness polygon
still needs its own complete estimate; (2) alone is not its consumer.

## 2. Exact all-power cross terms add a cubic row twist

The column adapter is the finite coefficient identity

    M_u(D)S_u(N)=sum_(g squarefree,h)
       mu(g)nu((gh)^2)chi_((gh)^2)(u)/(Ng Nh)
               B_u(D/Ng,N/(Ng(Nh)^2);g).               (3)

Every prime shared by h and the inner inputs is allowed. The input mask
of B is retained. For a component i put

    w_i=g_i h_i,
    D_i=D/Ng_i, N_i=N/[Ng_i(Nh_i)^2],
    L_i=D_i N_i=L/(Nw_i)^2.

Only nonempty polynomially bounded component scales occur. Opening
the original square gives ALL cross-component pairs i=1,2, with outside
absolute weight `1/(Nw_1 Nw_2)`. Their extra row factor is

    chi_((w_1)^2)(u) conjugate(chi_((w_2)^2)(u)).

Its primitive inducing character has order dividing three. Let its
squarefree good conductor be C_lambda, of norm Lambda. At each of its
primes its exponent is two or four modulo six. Original zeros at
EVERY prime of w1 w2 remain as an additional row mask, even where the
primitive character becomes unramified. Denote all such zero-only and
other original row masks by B0.

This is why one cannot simply apply the untwisted quadratic-form
theorem to each diagonal component and then use a triangle inequality
for a signed dual projection. The bilinear estimate below includes
the actual extra primitive character and these masks.

## 3. Local primes of the cubic twist

Both inner product columns A_i are squarefree. Partition their
divisors r_i=(A_i,C_lambda), including every r_i|C_lambda. At a prime
of C_lambda, the primitive exponent is the original even exponent
two or four plus `1_(p|A1)-1_(p|A2)`. The four possibilities are
NEVER zero modulo six. Hence the primitive pair conductor contains
ALL of C_lambda in every partition.

Allocate each prime of r_i to its unique original inverse or plain
input factor. This extracts exactly `1/sqrt(Nr_i)` from its central
normalization and shortens those two lengths. There are only
divisor-many allocations. The remaining columns are coprime to
C_lambda. Their gcd R and coprime remainders x,y are taken outside it.
The full primitive conductor is now C_lambda*x*y.

The local Gauss factor at C_lambda depends on the two fixed r_i
patterns and has modulus one. Its CRT interactions with x,y are
separated multiplicative column twists. The remaining x,y factor is
the same gamma_1(x) times conjugate(gamma_1(y)) as before. Any fixed
ray interaction is separated by the original finite ray subdivision.
The dual character at C_lambda is an outside row multiplier of modulus
at most one; it is retained until Cauchy and the positive bounds.
It may have odd exponent after this partition. That causes no problem:
it is a row multiplier, not a replacement column family.

The sum over r1,r2 and their input allocations costs only a prescribed
subpower: even the complete absolute resource
`sum_(r1,r2|C_lambda)1/sqrt(Nr1 Nr2)` is divisor-bounded. The shortened
lengths are no larger than D_i,N_i. It therefore suffices to prove
the next bilinear bound with columns coprime to C_lambda, then multiply
its explicit subpower mask losses.

## 4. Unequal component lengths: the complete bilinear hybrid

Here use the possibly shortened D_i,N_i and L_i. Put
`L_bar=sqrt(L1 L2)`. On a fixed common gcd R, the original column
lengths are `M_i=L_i/NR`. Their ratio need not be bounded. After the
EXACT coprimality Mobius projector k, each coefficient length is
`M_i/Nk`. The full Fourier kernel still uses the ORIGINAL x,y norms;
each of its separately normalized ratios Nx/M1,Ny/M2 stays in a fixed
compact annulus. Its norm/angle Fourier seminorm resource is therefore
uniform at both shortened coefficient lengths, just as in the
squarefree theorem. No primitive kernel for an artificial pair is used.

After the sixth-free index d and row-mask divisor b, the prefactor
and dual scale are

    P=U/[Lambda^(1/2)(Nd)^6 Nb sqrt(M1 M2)],
    H=M1 M2 Lambda (Nd)^6 Nb/U,
    J=(H/Nv)^(1/3).                                    (4)

All original masks are included; factors with a nonunit character
value vanish literally. The coefficient resources for each side are

    A_i << (NR Nk)^(-1+epsilon),
    B_i << (NR Nk)^(-1+epsilon) C_i(Rk),
    C_i(n)=sum_(n_a n_b=n,n_a<=C D_i,n_b<=C N_i)
          [D_i/Nn_a+N_i/Nn_b+(L_i/Nn)^(2/3)].           (5)

These are the same square-mass and uniform factorized Gauss-projection
bounds as in the squarefree theorem, at the ACTUAL lengths of that side.
Twists from C_lambda, b,k,v and all zero masks stay as bounded
multiplicative input coefficients.

For kappa=j^3v, split every j=t^2 r with r squarefree. The t,r may
share primes. The column character in r is quadratic, and the original
input mask (column,t)=1 remains. The complete individual hybrid bound is

    E_i(J) << J A_i+sqrt((M_i/Nk) J A_i B_i).            (6)

Apply Cauchy to the two coefficient polynomials on the SAME j set;
the bilinear row sum is at most sqrt(E_1 E_2). With the common bound
`A=(NR Nk)^(-1+epsilon)` this is at most A times

    J
     +J^(3/4)[((M1/Nk)C1)^(1/4)+((M2/Nk)C2)^(1/4)]
     +J^(1/2)[M1 M2 C1 C2/(Nk)^2]^(1/4).               (7)

This is the essential unequal-length step. Replacing both M_i by their
maximum would introduce an unnecessary product-length ratio loss.

## 5. Summation: every apparent length ratio cancels

Multiplying the first term of (7) by (4) gives

    U^(2/3)L_bar^(-1/3)Lambda^(-1/6)
       (Nd)^(-4)(Nb)^(-2/3)(NR)^(-2/3)(Nk)^(-1)(Nv)^(-1/3).

Both columns force `N(Rk)<=C min(L1,L2)`. Thus the R,k resource is at
most `min(L1,L2)^(1/3+epsilon)`, which cancels L_bar^(-1/3) with a
factor at most a constant. Summing all d,b,v gives

    << U^(2/3)Lambda^(-1/6)V^(2/3)(UDNV)^epsilon.        (8)

One mixed term has resource

    U^(3/4)Lambda^(-1/4)L1^(-1/4)
       (Nd)^(-9/2)(Nb)^(-3/4)(NR)^(-3/4)(Nk)^(-5/4)
                                     (Nv)^(-1/4)C2(Rk)^(1/4).

Put n=Rk. Its divisor weight is `(Nn)^(-3/4)(Nk)^(-1/2)`.
Use `C2(n)<<C0 (Nn)^epsilon` and the ACTUAL bound `Nn<=C L1`.
The complete n sum costs `C0^(1/4)L1^(1/4+epsilon)`, canceling
the displayed inverse L1 power. The other mixed term is identical
with sides exchanged. Their total is

    << U^(3/4)Lambda^(-1/4)C0^(1/4)V^(3/4)(UDNV)^epsilon. (9)

For the last term of (7) the resource is

    U^(5/6)L_bar^(-1/6)Lambda^(-1/3)
       (Nd)^(-5)(Nb)^(-5/6)(NR)^(-5/6)(Nk)^(-3/2)
                                (Nv)^(-1/6)(C1(Rk)C2(Rk))^(1/4).

Again n=Rk gives a summable divisor factor. Cauchy in the complete
n sum bounds the arithmetic part by sqrt(S1 S2), where the allocation
proof of the squarefree theorem gives

    S_i=sum_n (Nn)^(-5/6)C_i(n)^(1/2)
       << (D_i N_i)^epsilon L_i^(1/6) H_i,
    H_i=D_i^(1/3)+N_i^(1/3)+L_i^(1/6).

The factor L_bar^(-1/6) cancels EXACTLY against
`(L1 L2)^(1/12)`. Summing all d,b,v leaves

    << U^(5/6)Lambda^(-1/3)sqrt(H1 H2)V^(5/6)(UDNV)^epsilon. (10)

All d series converge. Every original b divisor is included, and its
negative power gives only the original mask subpower. The nonzero
Fourier tails and the H/Nv<1 regime have the same rapid-decay treatment
as in the squarefree theorem. Fixed dual-lattice denominators are
cleared at fixed cost. The bad-S cubefree part v_S has finitely many
patterns; the full S-smooth j_S part is retained as a bounded column
twist and the scale replacement J/Nj_S. The three row powers
J,J^(3/4),J^(1/2) in (7) have convergent finite-prime geometric
resources over ALL j_S. Thus these are complete frequency estimates,
including bad-prime powers, rather than good-frequency truncations.
If Lambda=1, subtract the formal x=y=1
nonzero-frequency contribution as there; it is absorbed in (8). If
Lambda>1, that pair is genuinely nonprincipal and remains included.

Equations (8)--(10) prove the full bilinear bound. Since Lambda>=1
and every shortened H_i<=C H0, its right side is uniformly bounded
by the bracket in (1), times a prescribed subpower.

## 6. Reassembling ALL original powers

Multiply the absolute bilinear bound by the exact outside coefficient
`1/(Ng1 Nh1 Ng2 Nh2)` from (3), and sum EVERY nonempty original
component. Their lengths and masks are polynomially bounded. The two
ideal harmonic sums on each side cost only fixed logarithmic powers;
the divisor-many local C_lambda partitions and all mask losses were
already assigned arbitrarily small powers. Choosing those powers
before the prescribed final epsilon pays every component and cross
term, proving (1).

This is a bilinear sum of the actual signed Poisson sectors, with an
absolute estimate applied only after their correct local kernels and
collisions have been identified. It is not an application of a norm
triangle inequality to an indefinite sector. The original all-power
zero extensions, shared inputs, sixth-free rows, and every primitive
dual frequency with cubefree core through V are present. The ENTIRE
remaining high-core sector remains unbounded here; none of this proves
the complete U^(6/5) mixed mean or its conditional zeta conclusion.
