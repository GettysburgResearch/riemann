# The native quadratic variation tail has a fixed atomic leading term

Status: **Proposed quantitative component lemmas C-V1--C-V3, pending
independent review.** The literal source is retained. The asymptotic
comparison states its Mertens hypothesis explicitly. No new zero-free line
or critical positivity result is claimed.

Scope: beta(n)=mu(n)-1_(67|n)mu(n/67),
T(y)=(4sqrt(y)-3)1_(y>=1),
F(x)=sum_(n<=x)beta(n)n^(-1/2)T(x/n),
H_2(x)=sum_(n<=x)beta(n)n^(-1/2)T(x/n)^2, and
J(u)=e^(-u)H_2(e^u), u>=0. Variation tails exclude the atom at u=log Y
itself. All infinite sums and measures below retain every activation.

Exact dependencies: `NEGATIVE_MASS.md` A-NM2, A-NM3 and the exact descent
identity (A11); `ZERO_FREE_MERTENS.md` supplies a source-qualified adapter
to a Mertens hypothesis. The elementary squarefree count is reconstructed
below. The already known BV/critical-mass distinction is inherited from
the earlier negative-mass packet; the contribution here is its explicit
atomic asymptotic and the corresponding negative ac-tail pole constant.

What was actually run: exact finite coefficient and rational pole-constant
controls in `test_variation_tail.py`. These are finite source controls,
not a numerical certification of a Mertens hypothesis or an infinite
asymptotic. The execution receipt records both Python modes.

## C-V1. The complete atomic variation tail

The exact local coefficient identity is

    |beta(n)|=mu(n)^2+1_(67|n)mu(n/67)^2.                 (C-V1)

To check it, if a prime other than67 occurs twice, both sides vanish.
Otherwise the exponent of67 is0,1,2 or at least3, and the absolute beta
coefficient is respectively1,2,1 or0, exactly as on the right.

The elementary squarefree count follows from mu(n)^2=sum_(d^2|n)mu(d):

    sum_(n<=x)mu(n)^2
      =sum_(d<=sqrt(x))mu(d) floor(x/d^2)
      =x/zeta(2)+O(sqrt(x)), x>=1.                       (C-V2)

There are O(sqrt(x)) floor errors; the absolutely convergent omitted tail
of sum mu(d)/d^2 is O(x^(-1/2)). Consequently

    S_beta(x):=sum_(n<=x)|beta(n)|
      =r_beta x+O(sqrt(x)),
    r_beta=(1+1/67)/zeta(2)=(6/pi^2)(1+1/67).           (C-V3)

For x/67<1 its vanishing count differs from its proposed main term by
O(sqrt(x)), so this is uniform for all x>=1.

At u=log n the exact J derivative measure has atom beta(n)n^(-3/2).
Its total atomic variation on (log Y,infinity) is therefore

    V_at(Y)=sum_(n>Y)|beta(n)|n^(-3/2)
       =(12/pi^2)(1+1/67)Y^(-1/2)+O(Y^(-1)).             (C-V4)

Indeed Abel summation, with the inclusive S_beta(Y), gives

    V_at(Y)=-Y^(-3/2)S_beta(Y)
            +(3/2)integral_Y^infinity S_beta(x)x^(-5/2)dx.

The main terms combine to2r_beta Y^(-1/2). Both error terms are
O(Y^(-1)). The proof covers arbitrary real Y>=1 and the strict endpoint
semantics at every integer activation.

## C-V2. Source cancellation improves only the ac part of that tail

The exact absolutely continuous derivative is

    J'_ac(u)=3e^(-u)F(e^u).

Hence its positive, negative and total variations satisfy

    V_ac,-(Y)=3 integral_Y^infinity F_-(x) dx/x^2,
    V_ac(Y)=3 integral_Y^infinity |F(x)| dx/x^2,
    V_J(Y):=|dJ|((log Y,infinity))=V_at(Y)+V_ac(Y).       (C-V5)

The atomic and ac measures are mutually singular; taking absolute
variation cannot cancel them against one another.

Assume 1/2<=theta<1 and M(x)=O_epsilon(x^(theta+epsilon)) for every
epsilon>0. A-NM2 gives |F(x)|=O_epsilon(x^(theta-1/2+epsilon)).
Choose 0<epsilon<1-theta. Integration in (C-V5) gives

    V_ac(Y)=O_epsilon(Y^(theta-3/2+epsilon)),
    V_J(Y)=(12/pi^2)(1+1/67)Y^(-1/2)
              +O(Y^(-1))+O_epsilon(Y^(theta-3/2+epsilon)). (C-V6)

In particular the full variation tail has the same strictly positive
atomic leading constant for every theta<1. A stronger Mertens exponent,
including theta=1/2 if assumed, does not alter this leading term. This is
a quantitative obstruction to reading the critical source cancellation
rate from the full variation norm; it is not an obstruction to estimating
the negative absolutely continuous variation itself.

## C-V3. A rightmost pole forces an explicit negative ac-tail constant

Use exactly the assumptions of A-NM3: c>0, F is absolutely Mellin
integrable in every Re(s)>c, its continued Mellin transform is holomorphic
near the real point c, and it has a pole of order r>=1 at c+i tau,
tau!=0, with leading coefficient A as in (A8). For this source a
nontrivial zero gives c<1/2, so in particular c<1.

Then

    limsup_(Y->infinity) V_ac,-(Y)/[Y^(c-1)(log Y)^(r-1)]
          >=3|A|/[2(1-c)(r-1)!].                       (C-V7)

This is a complementary tail form of A-NM3. It retains the actual pole
multiplicity and requires no isolated-pole or inverse-Mellin assumption.

Proof: put R(Y)=integral_Y^infinity F_-(x)dx/x^2. It is finite by
the elementary F(x)=O(sqrt(x)log(2x)) bound. The triangle argument
already written in A-NM3 gives, for M_-(sigma)=integral_1^infinity
F_-(x)x^(-sigma)dx/x,

    liminf_(sigma downarrow c)(sigma-c)^r M_-(sigma)>=|A|/2.

If K=limsup R(Y)/[Y^(c-1)(log Y)^(r-1)] is infinite, the claim follows.
Otherwise R(Y)<=(K+eta)Y^(c-1)(log Y)^(r-1) for all sufficiently large Y.
For c<sigma<1 integration by parts gives

    M_-(sigma)=R(1)+(1-sigma)integral_1^infinity R(x)x^(-sigma)dx.

The boundary at infinity vanishes under the preceding bound; R is an ac
tail, so there is no hidden activation atom. After putting x=e^u, the
gamma integral is (r-1)!/(sigma-c)^r. The finite initial segment
contributes zero after multiplication by(sigma-c)^r. Thus

    limsup_(sigma downarrow c)(sigma-c)^r M_-(sigma)
        <=(1-c)(K+eta)(r-1)!.

Comparison and eta downarrow0 give K>=|A|/[2(1-c)(r-1)!]. Finally
V_ac,-=3R by(C-V5), proving(C-V7).

The constant depends on an actual hypothetical off-line zero and its zeta
derivative. The packet neither finds such a zero nor supplies a certified
numerical enclosure of A. Full variation(C-V6) is larger for reasons
that are independent of this oscillatory pole information.
