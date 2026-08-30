# The source-first Boolean adapter has trivial induced gauge and bounded principal completion

Status: proposed exact source-order and principal-diagonal adapter, with a
bounded authenticated replay. The complete native principal family-square
estimate remains open.

This is the central interpretation of the gauge work in this continuation.
The native Boolean reduction takes the raw squarefree quotient **before**
owner completion. Its induced gauge is the identity. The ambient prime-square
gauge applied to already completed physical indices is another operator;
the earlier selector and masked-inverse obstructions do not obstruct the
correctly ordered quotient gauge. Similarly, the raw mixed-monomial Euler
cancellations do not cancel the canonical completed Boolean source.

Scope: finite labelled raw sources, canonical unordered equal-pair ownership,
the universal Boolean balanced core, clean completed records, and the actual
principal diagonal weight. Both coefficient-recombined and complete
three-factor Boolean-history resolutions are treated. Additional source
labels may be retained as a spectator Hilbert space if their measure and
weights are transported unchanged. No identification of all native carrier,
renewal, endpoint-colour and marked-67 labels with such a spectator space is
silently assumed.

Exact sources: the producer authenticates L-102706, L-102746,
L-102951/L-102952/L-102954/L-102962, L-106080, L-106026 and T-106140, and the
frozen source examples used in the replay. What was actually run is recorded
by the exact-SHA review. The uniform operator bounds below are proved, not
inferred from finite examples.

## 1. The order is present in the native reduction

At the frozen parent, L-102951 identifies the harmonic critical source with
the squarefree Boolean Euler class modulo the squared-activity ideal.
L-102954 then resolves that Boolean source with a frozen Vaughan cutoff and
realizes its balanced core with coefficient b_U(a)/a. L-102952 makes this core
coefficient independent of excluded owner labels, and L-102962 permits the
canonical equal-pair allocation. L-106026 records the resulting finite-shell
physical coefficient and its Mellin transform.

Thus at the algebraic coefficient part of the native route the order is

    raw labelled source -> squarefree Boolean quotient -> Boolean core map
    -> retained owner completion -> physical shell/phase/readout.

This is not an argument that every already-discarded squared-activity field
has a principal family L2 bound. Its historical transfer was at the stated
unamplified observation. The theorem here identifies the quotient source and
its diagonal adapter, not a new norm for that discarded remainder.

## 2. Exact quotient gauge and the commuting diagram

Let I_sq be the ideal spanned by raw labelled monomials having some coordinate
exponent at least two. Let Pi_sf be the corresponding squarefree quotient,
represented by the linear projection onto exponents zero or one. Work at a
finite physical truncation, so the relevant series are finite.

The frozen Euler/half-divisor gauge has

\[
 G_\tau=\prod_p g_\tau(x_p),\quad
 g_\tau(x)=1+O(x^2),\quad g_\tau'(x)=O(x^2).                  \tag{1}
\]

Hence G_tau-I and G_tau' take every raw monomial into I_sq. There are no
negative powers that could lower an exponent. Consequently

\[
 \Pi_{\rm sf}G_\tau=\Pi_{\rm sf},\qquad
 \Pi_{\rm sf}G_\tau'=0.                                      \tag{2}
\]

This statement is coefficientwise in labelled coordinates. The two copies
of 67 are distinct coordinates; physical aliasing is not used in (2).

Define T_U to be the source-first balanced-owner completion map described
explicitly below, including Pi_sf. Then

\[
 \boxed{T_U G_\tau=T_U,\qquad T_U G_\tau'=0.}                 \tag{3}
\]

The commuting diagram has G_tau on the raw source, T_U on both vertical
arrows, and the **identity** on the completed Boolean image. T_U need not be
invertible; its Boolean multiplier is generally not an idempotent projection.
No formula involving an inverse of T_U is used.

Any further tau-independent linear completion observation, shell mask,
canonical phase partition, or retained-label map preserves (3), because it
is applied after that identity. An ambient physical square shift after
completion is not the lower arrow of this diagram.

For H_tau=G_tau E_tau, equations (2)--(3) give the stronger pointwise result

\[
 T_UH_\tau=T_UE_\tau,\qquad T_UH_\tau'=T_UE_\tau'.             \tag{4}
\]

The projected gauge connection is zero. This uses coefficient normal form
in (1). If a carrier is instead expanded into signed words whose linear
coefficients cancel only after recombination, equality of that recombined
operator does not identify a word-counting diagonal. That separate measure
issue remains exactly as stated in NQ.

## 3. The explicit native one-sided coefficient map

Take a physically squarefree labelled support S, with k=|S|>=2. Choose an
unordered pair of distinct owner labels P={p,q} contained in S; put
A=S\P and a=product_(r in A)r. Keep the support and owner labels, so distinct
ancestral columns are not silently collapsed. Restrict to the clean sector;
physical repeated-67 occurrences belong to their separate retained ledger.

In the raw coefficient Hilbert space, the Euler source coefficient is

\[
 {\mu(S)\over\sqrt{Pa}}
 \exp(-i\theta_S),\qquad P=pq,
\]

where theta_S is the sum of the primitive label phases. The map consists of:

1. canonical owner share 1/binom(k,2), as in L-102746/L-102962;
2. Boolean multiplier b_U(A)/mu(A), well-defined since mu(A)=+1 or -1;
3. completion multiplier a^(-1/2) exp(-i theta_A), with physical output
   N=P a^2 and the corresponding translated observation.

Since mu(S)=mu(A), the resulting coefficient is exactly

\[
 {b_U(a)\over\binom{k}{2}\,a\sqrt P}
 \exp(-i\theta_P-2i\theta_A).                                \tag{5}
\]

The principal finite-shell Mellin term is (5) times N^(-it), and the observed
field is (5) times kappa(u-log N). This is precisely the coefficient form
of L-106026.5--6; the canonical owner share is part of the retained source
weight. Character or other fixed coefficient multipliers remain inside the
source term. Conjugating the left member in L-106120 conjugates its phase,
as required, rather than changing the physical output.

For a literal balanced factorization A=A_1 disjoint-union A_2 disjoint-union
A_3, replace b_U(A) in (5) by

\[
 h_U(A_1,A_2,A_3)=a_U(A_1)a_U(A_2)\mu(A_3).                  \tag{6}
\]

Keeping all three-factor histories and summing them later gives b_U exactly.
This is the actual bounded-arity Boolean history resolution, not an arbitrary
Taylor-word atomization. The coefficient and history maps are distinct linear
maps and have separately controlled diagonals below.

## 4. The correct completed derivative is not the mixed-monomial cancellation

The squarefree coefficient of E_tau, or H_tau, on S is (-tau)^k. Therefore
the completed balanced coefficient (5) along either source-first path is

\[
 \tau^k\,{b_U(a)\over\binom{k}{2}\,a\sqrt P}
       \exp(-i\theta_P-2i\theta_A).                           \tag{7}
\]

Its full derivative integrates to (5), which need not vanish. The two raw
owner sites contribute the fraction 2/k of that integral; the k-2 raw core
sites contribute (k-2)/k. They have the same sign, including each literal
Boolean history when (6) is retained.

For the earlier three-prime core example, k=5, b_U=-2 and the canonical share
is 1/10. In units of 1/sqrt(N), (7) is -tau^5/5. Its integrated derivative is
-1/5, with owner and core contributions -2/25 and -3/25. This is the nonzero
native balanced coefficient used in SCB.

By contrast, selecting the already completed monomial x_p x_q product x_r^2
directly in the **raw** Euler homotopy gives the different path
mu(A) tau^2(1-tau)^(k-2). Its full derivative integrates to zero, as EA
correctly proves for that projection. Completion of the raw squarefree
coefficient and selection of that completed monomial are different maps.
The equality of one owner-integrated coefficient in those maps does not
identify their core terms or their full derivative.

This exact ordering distinction is why the EA/PLC cancellations must not be
advertised as cancelling the canonical completed Boolean source.

## 5. Completion pays the actual principal weight

Now take one raw bilateral record with squarefree cores a,b and clean fixed
owners P,Q. Write a=gc,b=gd with coprime c,d>1, and put
ell=least(c),rho=least(d), both odd and distinct. The completion multiplier on
the bilateral amplitude is 1/sqrt(ab). The actual T-106140 principal weight
is w=g^2 ell rho c_ell c_rho. Thus the exact squared norm ratio is

\[
 \boxed{\frac{w}{ab}
 =\frac{\ell\rho c_\ell c_\rho}{cd}
 \le c_\ell c_\rho\le3.}                                    \tag{8}
\]

The last maximum occurs for the two smallest distinct odd primes, 3 and 5.
There is no growing common-core penalty: it cancels against ab. If phase 2
is admitted, the safe constant is 6 instead. The odd clean sector is used
here because it is the native tensor-character sector under discussion.

Ancestral raw support labels remain in the output, so distinct input columns
are disjoint in this record norm. Canonical equal-pair splitting is
contractive: its column squared norm is 1/binom(k,2), at most one. The
bilateral product is contractive as well. Therefore (8) proves an actual
bounded raw-diagonal-to-principal-diagonal completion, not a transported
metric defined merely to make the operator isometric.

## 6. Both Boolean resolutions have uniform subpower diagonal bounds

Put K(H)=max_(n<=H)omega(n), so K(H)=O(log H/log log H). Restrict completed
outputs to N=P a^2<=H, M=Q b^2<=H; hence ab<=H and
omega(a)+omega(b)<=2K(H).

For the coefficient map, the exact identity

\[
 b_U=\mu-2\mu_U+\mu_U\star\mu_U\star\mathbf1
\]

gives |b_U(A)|<=2*3^|A| on nonzero balanced support, where a>U^2 and
mu_U(A)=0; elsewhere b_U is zero. Combining both sides with (8) gives the
safe operator bound

\[
 \|T_U^{\rm coeff}\|\le4\sqrt3\,3^{2K(H)}=H^{o(1)}.          \tag{9}
\]

For the complete literal Boolean factor histories (6), use
|a_U(B)|<=2^|B|. Summing squares over all three-factor allocations gives

\[
 \sum_{A=A_1\sqcup A_2\sqcup A_3}|h_U(A_1,A_2,A_3)|^2
 \le\sum4^{|A_1|+|A_2|}=9^{|A|}.                            \tag{10}
\]

No history is forgotten in (10). Thus the history-labelled map satisfies

\[
 \|T_U^{\rm hist}\|\le\sqrt3\,3^{2K(H)}=H^{o(1)}.            \tag{11}
\]

Both estimates hold pointwise for arbitrary coefficients, and after tensoring
with a Hilbert-valued spectator field whose measure is kept unchanged.
Postcompletion coefficient masks only delete output rows. Primitive unit
phases and Mellin translations do not alter this diagonal norm. Integration
against the actual nonnegative |kappa-hat(t)|^2 dt measure preserves the
bounds.

For the raw finite Euler source, its one-sided coefficient squared norm is
at most sum_(n<=H)1/n<=1+log H when labels are physically distinct. Retaining
the two possible single-67 labels costs at most a factor two without erasing
their ancestry. The bilateral raw diagonal is consequently at most
4(1+log H)^2. Equations (9)--(11) give a direct subpower principal diagonal
for this canonical clean coefficient/Boolean-history source. This recovers
the shape of the already-paid diagonal; it is not a new proof that every
additional gamma label has been transported in the same measure.

## 7. The remaining operation is a family readout, not this completion norm

T-106140 subsequently sums the retained records inside each complete
principal/character member **before** taking its square. That readout is not
the orthogonal record norm in (8)--(11). It couples physical products,
common cores, conductors and all surviving gamma labels. A diagonal bound
does not bound this readout, and the literal Wick diagonal must still be
subtracted in its original resolution.

The source-first adapter therefore settles three concrete points: which
gauge actually acts on the Boolean quotient, why the completed balanced
source remains nonzero, and why physical completion itself has a bounded
principal-weighted diagonal cost. The remaining work is the exact full-gamma
adapter and the signed global additive/Kummer correlation, after the complete
source readout. The ambient postcompletion gauge variations are no longer a
candidate substitute for that problem.
