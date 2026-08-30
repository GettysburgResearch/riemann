# Fixed conductors already have unbounded live source multiplicity

Status: **exploratory exact source-support theorem, finite algebra, and
scoped faithful-carrier rank obstruction; not an integration verdict**.

Scope: the frozen canonical equal-pair Boolean source of L-106120,
L-106131, L-106191 and T-106140, at dyadic horizons. The theorem concerns
admissible source support before the complete signed outer observation. It
does not assert a nonzero value of that observation, admissible freedom of
every coefficient vector, or noncancellation after an unspecified quotient.
RH and GRH remain unproved.

Sources: [manifest](live_fixed_conductor_multiplicity.sources.json). The
finite live-panel predecessor proves duplicate cells but leaves multiplicity
growth open. The source-algebra adapter proves a rank tax conditional on such
growth. The present packet joins those two interfaces. Its sole external
analytic input is the classical prime number theorem in fixed arithmetic
progressions, stated in Section 2; this input is not proved by finite replay.

What was run: two fixed live owner panels, six small rational matrix controls,
twelve primitive source authentications, and ten tests in ordinary and
optimized Python. Smallest remaining gap: exploit complete signed
cross-group coefficients without treating faithful source rank as a lower
bound for every possible trace model or for the analytic target.

## 1. Main theorem and exact meaning of live support

Fix the reduced-core primes

\[
 \ell=5,\qquad \rho=7.
\]

**FCM-1 (unbounded live rectangles at fixed conductors).** For every two
positive integers \(m,n\), there is \(k_0(m,n)\) such that every integer
\(k\ge k_0(m,n)\), with \(U=2^k\) and \(Y=U^6\), admits a common
squarefree core \(g\), left semiprime owners \(P_1,\ldots,P_m\), and right
semiprime owners \(Q_1,\ldots,Q_n\) with these properties:

1. \(U^2/4<g<U^2/3\); both reduced cores are \(c=5,d=7\).
2. Every owner consists of two distinct primes. All \(2m+2n\) owner labels
   are different and avoid the common core, 5, 7 and the labelled prime 67.
3. Every physical product
   \(N_i=P_i(5g)^2\), \(M_j=Q_j(7g)^2\) lies in \((Y,11Y/10)\).
   Each side has one common owner dyadic block and one common physical
   dyadic block. In particular all cross pairs have ratio-eight support.
4. \(P_i\le5g\), \(Q_j\le7g\), all labels are horizon-safe, and
   \(P_i\equiv1\pmod7\), \(Q_j\equiv1\pmod5\).
5. Each full one-sided core has exactly two nonzero ordered Boolean balanced
   histories, both with coefficient \(+1\). Its full occurrence has six
   labels and canonical equal-pair share \(1/15\) per history.

Consequently the same fibre \(\iota=(g,5,7,+1,+1)\) contains at least
\(mn\) different arithmetic pairs in the single raw physical residue cell

\[
 (x,y)=(-7^2Q_j\bmod5,\ 5^2P_i\bmod7)=(1,4),
\tag{1.1}
\]

and at least \(4mn\) literal ordered-history atoms in that cell. The
arithmetic pairs remain distinct after Boolean-history and one-sided
equal-product aggregation.

The conductor pair is fixed across horizons; the common core \(g=g(U)\),
and hence the full fibre label \(\iota\), is not fixed across horizons.

Here “live” has the same source-support meaning as the predecessor:
nonzero Boolean source coefficient, canonical legal owner gauge, clean
labels, exact common-core extraction, the frozen active physical window,
and the declared dyadic and ratio support. It is not a positivity or
nonvanishing theorem for the final Mellin integral. Any additional source
restriction not present in that frozen contract must be checked separately.

## 2. The only prime-distribution input

For every fixed positive integer \(q\) and reduced residue class \(a\),

\[
 \pi(x;q,a)\sim\frac{x}{\varphi(q)\log x}.
\tag{2.1}
\]

We use (2.1) only at \(q=1,5,7\), not at a growing modulus and not under
GRH. A convenient author-provided reference is Kedlaya, *Analytic Number
Theory*, [Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).

A precise consequence used below is this: if \(0<c<C\) and \(\delta>0\)
are fixed, every interval \((A_T,B_T)\subset[cT,CT]\) of length at least
\(\delta T\) contains arbitrarily many primes in a prescribed reduced
class modulo fixed \(q\), as \(T\to\infty\). The assertion is uniform
in the interval endpoints. To see this, the error in (2.1) is
\(o(T/\log T)\) uniformly for \(x\in[cT,CT]\), by the definition of
the asymptotic. Subtraction at the two endpoints gives a positive main term
at least a fixed multiple of \(\delta T/\log T\). Removing any fixed
finite collection of previously used primes does not change the result.

No numerical threshold \(k_0(m,n)\) or growth rate uniform in \(m,n\)
is claimed by FCM-1. The order of its quantifiers is essential. A separately
proved [quantitative sequel](FIXED_CONDUCTOR_POWER_RANK_BARRIER.md) replaces
the fixed owner list by growing proportional intervals and obtains a sharp
order within the fully owner-disjoint rectangle class.

## 3. A small-conductor Boolean core with a middle-sized common part

For all sufficiently large \(U\), choose distinct primes

\[
 \sqrt U<a,b<\frac{21}{20}\sqrt U,
 \qquad \frac U4<h<\frac{3U}{10},
 \qquad g=abh.
\tag{3.1}
\]

The prime number theorem supplies two primes in the first interval and one
in the second. Eventually these intervals are disjoint and avoid every
fixed exceptional label. Then

\[
 \frac{U^2}{4}<g<\frac{1323}{4000}U^2<\frac{U^2}{3}.
\tag{3.2}
\]

For either \(q\in\{5,7\}\), put \(S_q=\{a,b,h,q\}\). Every singleton
in \(S_q\) is at most \(U\), while

\[
 ab>U,\quad hq>U,\quad aq\le U,\quad bq\le U.
\tag{3.3}
\]

Recall the frozen Boolean coefficient

\[
 a_U(S)=-\sum_{D\subseteq S,\ \prod D\le U}(-1)^{|D|}
 \quad(S\ne\varnothing),\qquad a_U(\varnothing)=0.
\]

A singleton therefore has coefficient zero. A two-prime subset has
coefficient 1 precisely when its product exceeds \(U\), and otherwise
has coefficient zero. In an ordered history for
\(b_U=a_U\star a_U\star\mu_{\rm sf}\), both first factors need at
least two labels. On four labels this forces a two-by-two partition and an
empty Möbius remainder. Of the three unordered partitions, only

\[
 \{a,b\}\mid\{h,q\}
\tag{3.4}
\]

has both products above the cutoff: the other partitions contain \(aq\)
or \(bq\). Thus exactly the two orders of (3.4) occur, each with coefficient
1, and \(b_U(gq)=2\).

This construction is deliberately different from a core consisting of two
primes above \(U\). The latter would force \(g>U^2\). The present common
core stays strictly below \(Y^{1/3}=U^2\), so the very-large-common-core
cutoff is not a reason to discard these support witnesses.

## 4. Owner selection with all dyadic constraints retained

Choose \(m+n\) fixed distinct primes \(s_1,\ldots,s_{m+n}\), none equal
to 5, 7 or 67. They will be the first owner labels. For sufficiently large
\(U\), they are smaller than \(a,b,h\).

For \(q=5,7\), define

\[
 L_q=\frac{Y}{q^2g^2},\qquad I_q=(L_q,11L_q/10).
\tag{4.1}
\]

An interval of multiplicative width \(11/10<2\) meets at most two dyadic
blocks. One of the pieces has length at least \(L_q/20\). Its middle
half is an open interval \(J_q\) of length at least \(L_q/40\), contained
strictly inside one owner dyadic block. Because of (3.2), both endpoints
of \(J_q\) are fixed positive multiples of \(U^2\), with constants
bounded independently of the chosen primes \(a,b,h\).

For \(1\le i\le m\), use (2.1) to choose a prime \(t_i\) in
\(J_5/s_i\) with

\[
 t_i\equiv s_i^{-1}\pmod7,
 \qquad P_i=s_it_i.
\tag{4.2}
\]

For \(1\le j\le n\), choose a prime \(v_j\) in \(J_7/s_{m+j}\) with

\[
 v_j\equiv s_{m+j}^{-1}\pmod5,
 \qquad Q_j=s_{m+j}v_j.
\tag{4.3}
\]

Every interval has length a fixed positive multiple of \(U^2\), since
\(m,n\) and the first owner labels are fixed before \(U\) grows.
The endpoint-uniform consequence of (2.1) permits all partner primes to be
chosen distinct. They are eventually larger than \(U\), whereas core
primes and all first owner labels are below \(U\). Hence all cleanliness
and pairwise owner-disjointness conditions hold.

Equations (4.1)--(4.3) give \(Y<N_i,M_j<11Y/10\), common physical
dyadic blocks and all owner congruences. They also give

\[
 \frac{P_i}{5g}<\frac{11U^6}{10\cdot125g^3}
 <\frac{704}{1250}<1,
\tag{4.4}
\]

and the analogous bound with 343 in place of 125 for \(Q_j/(7g)\).
All labels are \(O_{m,n}(U^2)\), hence less than \(4\sqrt Y=4U^3\)
eventually. Both marked incidence conditions hold because all owners and
the common core are coprime to 5 and 7.

The two owners together with four core labels form a six-label occurrence.
The frozen canonical equal-pair theorem allows this owner pair and assigns
it weight \(1/\binom62=1/15\), with no minimum-owner restriction added.
This proves every support statement in FCM-1.

The window can also be tested against an actual frozen one-sided kernel,
not only its support enclosure. At \(X=3Y/2\), every displayed product
\(V\in\{N_i,M_j\}\) satisfies
\(15/11<X/V<3/2\). L-102880 gives
\(K_L(z)=8-4\sqrt z>0\) on this interval. Thus these one-sided kernel
evaluations are simultaneously nonzero. This elementary observation neither
identifies the complete bilinear outer observation with a product of these
values nor proves that its signed integral is nonzero.

Distinct small first factors and distinct large partner factors imply
distinct squarefree owner products. The map \(P\mapsto P(gq)^2\) is
injective; equivalently its squarefree kernel recovers \(P\). Thus neither
one-sided equal-product aggregation nor history aggregation identifies the
\(mn\) arithmetic pairs. Equation (1.1) completes the proof.

## 5. Unbounded source rank is now a live, not ambient, obstruction

**FCM-2.** At the arithmetic-pair resolution, the live residue aggregation
has kernel dimension at least \(mn-1\). At the literal two-history-per-side
resolution, it has kernel dimension at least \(4mn-1\). On the latter
literal-coordinate kernel, the exact literal Wick operator acts as

\[
 -dI,\qquad d=(1-1/5)(1-1/7)=24/35.
\tag{5.1}
\]

This follows from the frozen arbitrary-occupancy identity
\(B_R=R^*SR-dI\). A vector supported on the displayed cell with zero sum
has \(Rz=0\), even if more atoms exist elsewhere in the fibre. It is an
operator statement on certified live support, not a claim that these kernel
vectors are admissible native coefficient inputs.

The atom convention must be preserved when compressing histories. In the
arithmetic amplitudes \(Z_{ij}\), four equal literal histories have energy
\(|Z_{ij}|^2/4\). The original literal scalar restricted to this subspace
is therefore represented by
\(R_{\rm agg}^*SR_{\rm agg}-(d/4)I\), which has eigenvalue \(-d/4\)
on the arithmetic zero-sum space in the ordinary \(Z\)-coordinate norm.
The auxiliary, newly recentered arithmetic-pair Wick form instead has
\(R_{\rm agg}^*SR_{\rm agg}-dI\), and differs by the exact paid-history
correction in Section 7. These two scalar conventions are not identified.

For the literal source algebra \(K^X\), any faithful finite module has
dimension at least \(|X|\): its orthogonal primitive idempotents must act
on nonzero, disjoint summands. FCM-1 therefore implies that no constant rank,
independent of horizon, can faithfully retain every source idempotent even
over the fixed conductor pair \((5,7)\) and after history aggregation.

This does **not** exclude rank-one sheaves upstairs, growing-rank
pushforwards, scalar sufficient statistics, nonlinear encodings, or smaller
principal-specific quotients. It is not a Betti lower bound for an unknown
derived object. It strengthens only the already stated faithful-algebra
carrier boundary.

## 6. Distinct-owner cross terms remain after deleting shared rows and columns

Suppose a separate, source-authorized cleanup deletes interactions sharing
the same left or right arithmetic product. The surviving ordered pairs on
our rectangle have \(i\ne i'\) and \(j\ne j'\); their eight owner labels
are all distinct. Because every physical residue is identical, their
normalized additive kernel is still the constant \(d\).

Thus the residual rectangle operator, **for precisely this deletion**, is

\[
 d(J_m-I_m)\otimes(J_n-I_n).
\tag{6.1}
\]

For \(m,n\ge2\), its eigenvalues divided by \(d\) and multiplicities are

| eigenvalue | multiplicity |
|---|---:|
| \((m-1)(n-1)\) | 1 |
| \(-(m-1)\) | \(n-1\) |
| \(-(n-1)\) | \(m-1\) |
| 1 | \((m-1)(n-1)\) |

It is full rank and indefinite. For the constrained native factorization
\(Z_{ij}=\overline{A_i}B_j\), its scalar is exactly

\[
 d\left(\left|\sum_i A_i\right|^2-\sum_i|A_i|^2\right)
  \left(\left|\sum_j B_j\right|^2-\sum_j|B_j|^2\right).
\tag{6.2}
\]

This is a factorization of an actual source-shaped expression, not an
estimate or a license to vary \(A_i,B_j\) independently in the frozen
native family. Other cleanup maps or signed conductor recombination may
still alter or cancel it. When \(m=1\) or \(n=1\), the operator in (6.1)
is zero, as the deletion rule requires.

## 7. Rank growth does not reopen the paid history correction

At conductors \((5,7)\), the source-dual atomic weights are

\[
 d=24/35,\qquad p=2/35,\qquad k=22/35,
 \qquad d/p=12,\quad k/p=11.
\tag{7.1}
\]

Each arithmetic pair in this construction has four equal Boolean-history
coefficients. Writing \(Z_{ij}\) for their sum, its literal history energy
is \(|Z_{ij}|^2/4\), and the history conversion is
\(\Delta=\tfrac34\sum_{ij}|Z_{ij}|^2\). The signed-history predecessor
still pays its principal-weighted correction. On this fixed conductor
sector, multiplying that nonnegative principal correction by the constants
12 or 11 also bounds the corresponding additive or Kummer history
correction. This statement is limited to that history subledger.

It neither bounds the interactions between different arithmetic pairs nor
contradicts the unbounded amplification ratio when the conductors grow.
The construction therefore separates two concepts: faithful source rank
can grow without producing an unpaid representation-history error. The
remaining useful target is the complete signed cross-group current.

## 8. Replay, scope, and next targets

The accompanying code checks a fixed finite corpus, with exact integer
primality checks, all 81 assignments on each four-label Boolean core,
source inequalities, owner congruences, dyadic blocks, literal shares, and
small exact rational matrix controls. It does not search increasing
horizons or establish (2.1). The all-horizon theorem is the proof above.

| control | common primes | left owners | right owners |
|---|---|---|---|
| \(U=256,Y=2^{48}\) | 17, 19, 59 | (2,16573), (3,11093), (11,3019) | (13,1327), (37,463), (41,421) |
| held-out \(U=1024,Y=2^{60}\) | 37, 41, 223 | (2,210011), (3,140159), (11,38201), (13,32353) | (17,12373), (19,11059), (23,9137) |

These give 9 and 12 arithmetic pairs, respectively, or 36 and 48 literal
ordered-history atoms. They satisfy the sufficient cutoff, source-window,
owner and common-core inequalities directly. They are not claimed to fit
the narrower prime-selection intervals (3.1), which are an asymptotic
existence device. All 21 pairs have the same raw cell (1,4).

The discovery scout examined 5,578 candidate integers in two prescribed
owner-product windows, below its fail-closed 20,000-candidate cap. It is
reproducible with `--scout`; the canonical replay uses the frozen owners and
does not rerun the search. The canonical JSON requires exact recomputation,
LF-normalized hashes of this note, producer, tests and source manifest, and
Git-object authentication of all twelve upstream source files. The tests
also check cutoff equality, owner collisions, false residue congruences,
integer/type caps, the zero-row/column boundary, signed rectangle energies,
and a corrupted source manifest under `python -O`.

The canonical hashes also bind the separate quantitative sequel; its
all-horizon prime-distribution argument is not machine-proved by this replay.

```text
python -B research/riemann-structures/live_fixed_conductor_multiplicity.py --check
python -B -O research/riemann-structures/live_fixed_conductor_multiplicity.py --check
python -B -m unittest tests.test_live_fixed_conductor_multiplicity
python -B -O -m unittest tests.test_live_fixed_conductor_multiplicity
```

The proof has received an independent adversarial reconstruction; source
commit review remains separate from canonical integration. In particular, the
following are not claimed:

- a horizon-uniform multiplicity asymptotic or explicit prime threshold;
- a new result about prime distribution;
- native coefficient-family nonfactorization;
- a lower bound for every possible derived or trace representation;
- complete native signed noncancellation, ONEPLACEWEIL or RELTRACE;
- RH, GRH, or external mathematical priority.

The ranked continuation is: (1) find a smaller source quotient compatible
with the principal pairing rather than every atom idempotent; (2) estimate
the actual signed cross-group current, keeping the complete source weights;
(3) test that quotient against source-aware Adams and the literal diagonal.
