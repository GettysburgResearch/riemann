# The surviving marked Kummer line has no finite partial-Frobenius closure

Status: **generic function-field obstruction, with an exact principal-trace
model of the complete marked owner pushforward**.

Scope: finite Kummer covers and finite Kummer--Tate orbit repairs of the
specified degree-bounded polynomial source. This is not an impossibility
theorem for all correspondence, derived, infinite-dimensional, or full
integer-source parents. In particular, a virtual source may cancel the
coupled component; a genuine constituent cannot be inferred from its name.

Frozen source: COMPLETE_MARKED_OWNER_PUSHFORWARD.md and its producer at
faf74a47dac33927d081a890f2b5a7ead48b869b. That packet retains ordered rational
owner roots with weight1/4. Its integral parent has trace16J, rather than
identifying split owners with rational points of an unordered quotient.

## 1. The generic domain and the crossed orbit

Let K=F_5(lambda,rho). The field embeddings

\[
 \sigma:\lambda\mapsto\lambda^5,\quad\rho\mapsto\rho,
 \qquad
 \tau:\rho\mapsto\rho^5,\quad\lambda\mapsto\lambda
\]

fix the constants. Work at the generic point. A partial map need not preserve
the original open complement of the diagonal: its pullbacks introduce new
punctures. We do not assert a self-map of that unchanged open set.

For every integer r define

\[
 f_r=\begin{cases}
       \rho-\lambda^{5^r},&r\ge0,\\
       \rho^{5^{-r}}-\lambda,&r<0,
      \end{cases}
 \qquad a_r=[f_r]\in K^*/K^{*2}.                 \tag{1}
\]

The associated quadratic Kummer line is denoted L_r. These are characteristic
zero coefficient lines, with coefficient prime different from5. The odd power
5 does not change a square class. Consequently

\[
 \sigma^*a_r=a_{r+1},\qquad\tau^*a_r=a_{r-1},
 \qquad(\sigma\tau)^*a_r=a_r.                    \tag{2}
\]

For example, sigma(f_-1)=(rho-lambda)^5. Thus total Frobenius preserves every
line in the orbit while the two marked maps translate it in opposite
directions. This explains why a total-Frobenius control does not provide
independent marked descent.

## 2. MKO-1: independent divisors and exponential cover degree

For any finite set I of integers, the classes {a_r:r in I} are linearly
independent over F_2. Hence

\[
 [K(\sqrt{f_r}:r\in I):K]=2^{|I|}.              \tag{3}
\]

Proof. Each f_r is irreducible in F_5[lambda,rho]: it has degree one in rho
when r>=0 and degree one in lambda when r<0. The corresponding prime divisors
D_r are distinct. If r!=s, f_s is not divisible by f_r. Therefore

\[
 v_{D_r}(f_s)=\delta_{r,s}.
\]

Any nonempty product of distinct f_s has an odd valuation at at least one
D_r, and cannot be a square. This proves independence. To prove (3) without
assuming it as a slogan, induct on |I|. In a multiquadratic extension with its
sign-change Galois group, an element whose square belongs to K is a common
eigenvector for that group; its character eigenspace is the K-line generated
by a product of the already adjoined square roots. A new independent class
therefore cannot become a square in that extension, so each step has degree2.
This also proves that any finite extension trivializing these |I| lines has
degree at least2^|I|. Purely inseparable extension does not remove this
obstruction, because a nontrivial quadratic extension is separable.

There is no finite algebraic extension E/K containing sqrt(f_0) and admitting
a field embedding tilde_sigma:E->E restricting to sigma on K. Indeed its
iterates would put sqrt(f_r) in E for every r>=0, contradicting (3). This is a
no-go for a finite generic cover that both trivializes the crossed Kummer
line and lifts the left partial Frobenius. It is stronger than a single
failure at a finite-field point, but it does not exclude an infinite cover.

## 3. MKO-2: the finite-rank constituent obstruction

Pullback by sigma is an exact equivalence on finite-dimensional continuous
generic etale representations. The image field F_5(lambda^5,rho) is identified
with K by sigma, and K is purely inseparable over that image. The resulting
equivalence is the topological invariance of the etale site; see
[Stacks, Section59.45](https://stacks.math.columbia.edu/tag/04DY).

If a finite-dimensional representation V has sigma^*V isomorphic to V, it
cannot have L_0 as a Jordan--Holder constituent. Otherwise exact pullback puts
every L_r, r>=0, among the constituents of V. The lines are pairwise
nonisomorphic by Section2, contradicting finite length.

The same proof applies to L_0 tensored with a sigma-fixed rank-one external
character or Tate twist. The hypothesis is an actual nonzero constituent.
This statement cannot simply be applied to an arbitrary virtual difference,
where matching constituents in opposite signs may cancel.

## 4. The source principal observable in the Kummer--Tate ring

Keep the four fixed omitted marks0,1,2,3 of the frozen complete owner model.
Let r_i and l_i denote the Kummer classes of rho-i and lambda-i. Write

\[
 R=\sum_{i=0}^3 r_i,\quad S=\sum_{i=0}^3 l_i,
 \quad W=-1-\sum_{i=0}^3r_il_i,
 \quad a=a_0,\quad n=\mathbb L-6,                 \tag{4}
\]

where the Tate class L has trace q over F_q. All r_i,l_i are fixed by both
partial pullbacks, as are Tate twists. Their squares, and a^2, equal1.
The fixed marks are rational over F_5; chi_q(-1)=1 on every extension.

Use the following polynomial in these actual character classes:

\[
 \begin{aligned}
  \alpha&=-a-R,&\beta&=-a-S,&\omega&=W,\\
  A&=n(n-1)(n-2)(n-3),\\
  B&=(n-2)(n-3)(\alpha^2-n),\\
  C&=(n-2)(n-3)(\beta^2-n),\\
  T&=\alpha^2\beta^2-(n-4)(\alpha^2+\beta^2)
       -4\omega\alpha\beta+n^2+2\omega^2-6n,\\
  Q&=81(A^2+B^2+C^2+T^2)-36A.                    \tag{5}
 \end{aligned}
\]

At every clean extension-field point, the trace of Q is **4J** of the frozen
complete owner principal Wick observable. This follows directly from its
all-q moment formula, not from a fitted list of traces. The ordered source
integral parent has trace16J; thus 4Q is an integral Kummer--Tate trace model
for that parent. We claim equality of the specified trace functions. No
unproved equality of derived compact-pushforward objects is used.

Reduce (5) using a^2=1. There are unique external polynomials Q_0,Q_1 with

\[
 Q=Q_0+aQ_1.                                    \tag{6}
\]

The coefficient Q_1 is nonzero. To check this explicitly, specialize the
external sign rows to the actual F_25 witness of the source packet, where
R=0, S=-2, W=1. Formula (5) gives

\[
 \begin{aligned}
 B&=(n-2)(n-3)(1-n),\\
 C&=(n-2)(n-3)(5-n-4a),\\
 T&=(n-3)(n-9)+4(n-3)a,\\
 Q_1&=648(n-3)^2\big((n-2)^2(n-5)+(n-9)\big).
 \end{aligned}                                  \tag{7}
\]

This is nonzero, and strictly positive for n>=19. Changing a from1 to-1
changes J by -Q_1/2, exactly the cofinal negative defect already proved in
the source packet. Thus the surviving crossed line is not an arbitrary
decoration added after the owner sum: its coefficient in the exact principal
trace model is nonzero.

## 5. MKO-3: finite Kummer--Tate orbit repairs cannot be invariant

The eight external coordinate classes r_i,l_i and any finite collection of
the a_r are independent square classes. Use their distinct coordinate and
graph divisors just as in Section2. In particular, external coefficients
are unramified at the new graph divisors and cannot turn one a_r into another.
With characteristic zero coefficients, their distinct rank-one characters
are linearly independent in the representation Grothendieck group. Tate
powers are also distinct arithmetic characters (their Frobenius eigenvalues
are distinct powers of5); they do not create a relation between these finite
quadratic characters.

Let A_ext be the rational Kummer--Tate ring generated by the eight external
characters and the Tate class. Consider the ring with finite sums only,

\[
 \mathcal R=A_{\rm ext}
  \left[\bigoplus_{r\in\mathbb Z}\mathbb Z/2\mathbb Z\right]. \tag{8}
\]

A basis monomial in its crossed variables is the product of a_r over a
finite subset I of Z. Pullback sigma translates I to I+1. Every nonempty
finite I has an infinite translation orbit: its minimum increases under
each positive translate. A finite sum invariant under this translation
must consequently have zero coefficient on every nonempty I. Therefore

\[
 \mathcal R^{\sigma^*}=A_{\rm ext}.              \tag{9}
\]

This includes repairs involving products of several crossed lines, not just
linear sums of their individual orbits. Formula (6), with Q_1 nonzero, is not
in the invariant subring. No addition of only finitely many orbit terms can
make it invariant while retaining any nonzero crossed component. Such a
finite repair must cancel the complete crossed component, hence cannot
preserve the varying principal observable proved in the source packet.

The no-go is exact for this declared finite Kummer--Tate class model. It does
not say that every possible geometric parent belongs to (8). In particular,
an infinite orbit, a correspondence retaining coupled transport, a changed
observable, or cancellation by the remaining original source are not ruled
out. A virtual source outside the declared ring requires a separate binding
and constituent argument.

## 6. Replay and the next source gate

The companion bounded replay authenticates the frozen owner note, producer,
and artifact directly from their Git blobs. It expands (5) in the finite
external/sign group ring with exact integer coefficients, separates its
crossed parity, and checks (7) against direct evaluations and the frozen
principal count. Finite graph-index controls verify the pullback polynomial
identities in characteristic5 and the divisor labels. These controls do not
prove the infinite statements; Sections2,3,5 contain their proofs.

The complete original integer source has not been identified with this
polynomial coefficient projection. Its carrier transport, sums over other
common cores and degrees, and signed complements may change or cancel the
class. The next serious gate is that source binding, not another search for
a finite list of partial-Frobenius labels.
