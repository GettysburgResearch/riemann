# A refined all-row sextic sieve and improved higher-moment overlap ranges

Status: proposed proved deduction from classical squarefree character large sieves and elementary ideal counting. No quasi-Riemann zero-free theorem, new higher-moment premise, or numerical zero input is used.

Scope: every nonzero element row over K=Q(sqrt(-3)), arbitrary complex coefficients on squarefree ideal columns, the literal nonunit zero extensions, and exact incidence pieces of the Möbius moments. This strengthens the H^(1/2)L term in the preceding all-row estimate to H^(1/6)L. It improves some higher-moment common-gcd ranges. It does not prove the full fourth moment or a new zero-free half-plane.

Primary inputs: Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*, Theorem 1.3, [arXiv:1112.1650v1](https://arxiv.org/html/1112.1650v1), used for orders 3 and 6; the quadratic large sieve over this field, in the exact form recorded in OpenAI October 5 `paper2.tex`, label `lem:quadratic` (lines 1883–1905), citing Goldmakher–Louvel; and the planar additive large sieve in September 30 `lem:planar-additive-sieve`. The sextic specialization is also the September 30 `lem:sextic-large-sieve`. Both imported manuscripts are pinned at OpenAI commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

The BGL theorem was checked at its primary-source Theorem 1.3 and its Section 2 convention: it uses the underlying primitive character for a power index. Our proof does not discard zeros from sixth-power factors. It freezes those factors into the column coefficient before applying a squarefree-row theorem.

## 1. The squarefree input for each nontrivial power

Let S be the fixed excluded column primes, containing those above 2 and 3. For j=1,...,5 and arbitrary coefficients z_n on squarefree ideals n outside S with Nn<=L, we use

\[
\sum_{\substack{Na\le M\\a\ {\mathrm{squarefree}}\\(a,S)=1}}
\left|\sum_n z_n\chi_n(a)^j\right|^2
\ll_{S,\epsilon}(ML)^\epsilon
\left(M+L+(ML)^{2/3}\right)\sum_n|z_n|^2.                 \tag{1.1}
\]

For j=1,5 this is the sextic sieve, with conjugation of coefficients if necessary. For j=2,4 the symbols have order three, giving the cubic sieve and its conjugate. For j=3 the quadratic sieve gives the stronger factor M+L, which implies (1.1).

Only fixed ray-class splittings are involved in passing from the primary-generator residue-symbol convention to those theorems. On squarefree indices, raising a local sextic character to powers j=1,...,5 leaves a nontrivial local character at every good column prime. Thus its conductor retains that prime and its zero on nonunits. Conjugation also preserves zeros. No factor with exponent divisible by six is included in the varying squarefree row of (1.1).

## 2. Exact valuation decomposition of every row

Choose generators multiplicatively for ideals, including the finitely many bad primes. Every nonzero element u is uniquely represented by a unit epsilon, an arbitrary ideal v, and pairwise-coprime squarefree ideals a_1,...,a_5 such that

\[
u=\varepsilon\,v^6 a_1 a_2^2 a_3^3 a_4^4 a_5^5.           \tag{2.1}
\]

Here and below the expression uses the chosen generators. For a prime valuation e, divide e=6q+r with 0<=r<=5: put its q-th power into v and, if r>0, one copy into a_r. This proves uniqueness. **There is no condition that v be coprime to the a_j.** Such overlap occurs whenever a valuation is at least seven and has nonzero remainder modulo six.

The exact symbol identity is

\[
\chi_n(u)=\chi_n(\varepsilon)\,
\mathbf1_{(n,v)=1}\prod_{j=1}^5\chi_n(a_j)^j.             \tag{2.2}
\]

This includes all original zeros. In particular chi_n(v^6) is the displayed indicator, not the constant function one.

Take dyadic norm blocks

\[
A_j\le Na_j<2A_j,\qquad V\le Nv<2V,
\qquad A_j,V\ge1.
\]

A block meeting Nu<=H satisfies

\[
P:=V^6A_1A_2^2A_3^3A_4^4A_5^5\le H.                      \tag{2.3}
\]

Set B=V product_j A_j and M=max_j A_j. Choose one index j attaining M. Freeze epsilon, v, and all a_i with i!=j. The coefficient

\[
z_n\chi_n(\varepsilon)\mathbf1_{(n,v)=1}
\prod_{i\ne j}\chi_n(a_i)^i
\]

is independent of the remaining a_j and its squared mass is at most sum_n|z_n|^2. The coprimality restrictions between the varying a_j and the other a_i can be discarded in the nonnegative row square-sum. No mask on the column is removed.

If a_j contains primes of S, fix their squarefree product q_j first. There are only finitely many choices depending on S. Its character factor is absorbed into the coefficient, and the remaining a_j is squarefree outside S. The norm scale changes by the fixed factor Nq_j, which only changes the implied constant. The same treatment applies for any selected j and any unit. This justifies (1.1) for the required varying component.

There are O_K(B/M) choices of the frozen ideal labels, by elementary ideal counting. Applying (1.1) with row scale 2M, and bounding each frozen coefficient norm by the original one, proves the block bound

\[
\ll_{S,\epsilon}(HL)^\epsilon
\left(B+\frac{BL}{M}+\frac{BL^{2/3}}{M^{1/3}}\right)
\sum_n|z_n|^2.                                           \tag{2.4}
\]

There is no sixth-power exception left outside this bound. If every a_j is the unit ideal, then M=1, B=V and the same bound simply counts the available v labels while keeping their masks.

## 3. Two exact monomial inequalities

The loss from all the frozen labels can be optimized without a numerical linear program. Since every A_j,V>=1,

\[
B\le P\le H.
\]

Moreover

\[
\frac{(B/M)^3}{P}
=\frac{A_1^2A_2}{M^3V^3A_4A_5^2}\le1,                  \tag{3.1}
\]

because A_1,A_2<=M. Similarly

\[
\frac{(B/M^{1/3})^3}{P^2}
=\frac{A_1}{M V^9A_2A_3^3A_4^5A_5^7}\le1.               \tag{3.2}
\]

Consequently

\[
\boxed{B/M\le H^{1/3},\qquad
B/M^{1/3}\le H^{2/3}.}                                   \tag{3.3}
\]

These inequalities are literal for every admissible block; no independence of its norm labels is assumed.

### Proposition 3.1: an intermediate all-row sieve

For H,L>=1 and arbitrary complex coefficients z_n on squarefree columns outside S with Nn<=L,

\[
\boxed{\sum_{\substack{u\in\mathcal O_K\\0<Nu\le H}}
\left|\sum_n z_n\chi_n(u)\right|^2
\ll_{S,\epsilon}(HL)^\epsilon
\left(H+H^{1/3}L+(HL)^{2/3}\right)\sum_n|z_n|^2.}         \tag{3.4}
\]

**Proof.** Insert (3.3) into (2.4). There are O(log(2H)^6) dyadic blocks for the six labels v,a_1,...,a_5, six units, and finitely many bad-prime patterns. Summing their bounds proves (3.4), by assigning a smaller preliminary exponent loss to (1.1) and absorbing the fixed logarithmic power into the requested (HL)^epsilon. Bounded H,L are covered by changing the constant. \(\square\)

This is an elementary consequence of the stated classical sieves, not a claimed improvement to their squarefree-row theorem. The intermediate estimate improves the earlier all-row factor H^(1/2)L. The next argument improves it further.

### Limits of this particular optimization

The cross term (HL)^(2/3) still comes from squarefree rows: the block A_1=H, all other labels one, has that exact sieve term. Thus this refinement alone still reaches diagonal size H sum|z_n|^2 only when L<=H^(1/2).

The exponent 1/3 in the L-term cannot be reduced by optimizing (2.4) alone: take A_1=A_2=H^(1/3), the other labels one. Then P=H and B/M=H^(1/3). In this block the quadratic coordinate is trivial, so retaining its stronger estimate does not remove the example when L>=H. These observations are barriers for this scalar upper-bound optimization, not lower bounds on actual character sums. An additional ordinary-character sieve supplies the missing alternative.

### Lemma 3.2: ordinary primitive-character large sieve

For coefficients z_n supported on the chosen primary ideal generators of norm at most L, and all primitive finite-order Hecke characters with conductor norm at most Q,

\[
\sum_{N\mathfrak q\le Q}\sum_{\chi\ {\rm primitive}\bmod\mathfrak q}
\left|\sum_nz_n\chi(n)\right|^2
\ll_K (L+Q^2)\sum_n|z_n|^2.                              \tag{3.5}
\]

A fixed finite collection of ray or unit corrections changes only the implied constant.

**Proof.** Work first with primitive multiplicative characters of the finite residue group modulo each ideal q; the Hecke characters in (3.5) are a subset, satisfying the required unit invariance. Since K is a PID, choose one generator for each q. The primitive Gauss expansion expresses chi(n), including its zero at nonunits, as

\[
\frac1{\tau(\overline\chi)}
\sum_{a\bmod\mathfrak q}^{*}\overline\chi(a)
e_K(an/q),\qquad |\tau(\overline\chi)|=\sqrt{N\mathfrak q}.
\]

Fixed trace-dual-lattice normalizations have no effect on the following inequalities. Character orthogonality (or Bessel's inequality for the subset of primitive characters) bounds the sum over chi of the squared transform by

\[
\frac{\varphi(\mathfrak q)}{N\mathfrak q}
\sum_{a\bmod\mathfrak q}^{*}
\left|\sum_nz_n e_K(an/q)\right|^2
\le\sum_{a\bmod\mathfrak q}^{*}
\left|\sum_nz_n e_K(an/q)\right|^2.
\]

Distinct reduced fractions a/q with Nq<=Q are separated by at least c_K/Q in the fixed two-dimensional trace torus: a nonzero difference has numerator a nonzero algebraic integer and denominator the product of two generators, of absolute value at most Q. Reduced fractions from distinct denominator ideals cannot coincide. The planar additive large sieve therefore gives L+Q^2 for points n in the norm disk Nn<=L. Our chosen primary generators form a subset of that lattice disk, so coefficients may simply be extended by zero to the other lattice points. This proves (3.5). No large-sieve bound for general Hecke characters is imported without this reduction. \(\square\)

### Lemma 3.3: an alternative bound on each valuation block

Write P_0=product_j A_j, so B=VP_0. For the same block as Section 2,

\[
\text{block energy}\ll_S V(L+P_0^2)\sum_n|z_n|^2.         \tag{3.6}
\]

**Proof.** Fix v, the unit, and the finitely many bad-prime parts. Absorb the exact indicator (n,v)=1 and the fixed phases into z_n. Reciprocity turns the varying sixth-free core product_j a_j^j into a finite-order character in n. Its conductor outside S is exactly product_j a_j: at each good prime the exponent j lies in {1,...,5}, so the local sextic character to that power is nontrivial. Its total conductor divides a fixed ray modulus times this squarefree core, and hence has norm O_S(P_0) on the block.

The map from the five pairwise-coprime squarefree ideals a_j to this character has bounded multiplicity depending only on the fixed data. Indeed restriction to the residue group at any good conductor prime determines which of the five distinct nontrivial powers of its sextic character occurs; this recovers j and therefore all the a_j outside S. Fixed local corrections, unit choices, and the finitely many possibilities at S account for only a bounded multiplicity. One may equivalently partition into the fixed ray classes before applying reciprocity.

Every resulting character retains its zero at the good core primes because its local component there is nontrivial and primitive. The v-prime zeros, including primes that overlap the core, were separately retained in the fixed coefficient mask. The residue-character convention at powers divisible by six is therefore never used to drop a zero. At the fixed bad primes, any imprimitive zeros are already in the fixed column exclusion S.

Apply Lemma 3.2 to this subset of characters with Q=O_S(P_0), using its bounded multiplicity. There are O_K(V) possible v in the dyadic block and each coefficient mask is a contraction. Summing proves (3.6). \(\square\)

### Theorem 3.4: final refined all-row sieve

For the full range and exact coefficients of Proposition 3.1,

\[
\boxed{\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)\right|^2
\ll_{S,\epsilon}(HL)^\epsilon
\left(H+(HL)^{2/3}+H^{1/6}L\right)\sum_n|z_n|^2.}         \tag{3.7}
\]

**Proof.** In the notation of a fixed block, put

\[
T_1=\frac{BL}{M},\qquad T_2=VP_0^2.
\]

The block has both bounds (2.4) and (3.6). By (3.2), the first is at most a subpower times [H+(HL)^(2/3)+T_1] times the coefficient mass. The second is at most [VL+T_2] times that mass. Further,

\[
\frac{T_1^2T_2}{P^2L^2}
=\frac{V^3P_0^4}{M^2P^2}
=\frac{A_1^2}{M^2V^9A_3^2A_4^4A_5^6}\le1.              \tag{3.8}
\]

Since P<=H,

\[
\min(T_1,T_2)\le(T_1^2T_2)^{1/3}\le(HL)^{2/3}.
\]

Also V<=H^(1/6). Use the elementary inequality
min(a+x,b+y)<=a+b+min(x,y) for nonnegative a,b,x,y, and absorb the subpower factor into both candidate bounds before taking their minimum. The block energy is consequently at most a subpower times [H+(HL)^(2/3)+H^(1/6)L] times the coefficient mass. Sum the same logarithmic number of blocks as before. This proves (3.7). \(\square\)

This improved bound still reaches diagonal size for L<=H^(1/2). The squarefree-row cross term has not improved. The H^(1/6)L term retains the scale of the sixth-power row copies rather than suppressing them.

## 4. Improved bounds for the squarefree moment cores

Use the exact incidence notation from `GENERAL_MOMENT_ATTACK.md`, or Section 9 of `FOURTH_MOMENT_ATTACK.md`. For fixed k, shared ideals c_I have |I|>=2, all are squarefree and pairwise coprime, and

\[
X_i=D\Big/\prod_{I\ni i}Nc_I,
\qquad P(\mathbf c)=\prod_iX_i
=D^k\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]

The squarefree balanced core has exact coefficients mu_K(r)nu(r) times its k-factor divisor weight and the mask (r,CS)=1. Its coefficient mass is O(D^epsilon P(c)), uniformly in the moving mask, by the fixed-order ideal divisor bound and counting the supported factor tuples. Applying (3.7), with column scale a fixed multiple of P(c), gives

\[
\boxed{\|B_{C,\cdot}(\boldsymbol X)\|_2^2
\ll D^\epsilon\left(HP+H^{1/6}P^2+H^{2/3}P^{5/3}\right).} \tag{4.1}
\]

All constants may depend on fixed k,W,nu,S and a polynomial bound H<=D^(C_0). Nonempty bounded factor scales below one are covered by a fixed support-dependent constant. No quasi-Riemann theorem is used.

For the fourth-moment core P=X^2 this becomes

\[
\sum_{0<Nu\le H}|B_{c,u}(X)|^2
\ll (HX)^\epsilon\left(HX^2+H^{1/6}X^4+H^{2/3}X^{10/3}\right).
                                                                    \tag{4.2}
\]

The resulting common-gcd tail obeys

\[
\|T_{\ge C}\|_2^2\ll(DH)^\epsilon
\left(HD^2+H^{1/6}D^4C^{-2}
+H^{2/3}D^{10/3}C^{-4/3}\right).                          \tag{4.3}
\]

The same Minkowski proof as the prior tail theorem applies. Its target-size cutoff remains C>=D H^(-1/4), because the last term is now the limiting one. The improvement in the middle term is nevertheless real away from that cutoff.

## 5. A strictly larger controlled common-gcd range for higher moments

Let G_(>=C)^(k) be the exact portion of A_u(D)^k whose original tuple has N gcd(n_1,...,n_k)>=C. In the incidence decomposition this is precisely the condition Nc_[k]>=C.

### Theorem 5.1

For fixed k>=2, C>=1 and the preceding parameter ranges,

\[
\boxed{\|G_{\ge C}^{(k)}\|_2^2\ll D^\epsilon
\left(HD^k+H^{1/6}D^{2k}C^{2-2k}
+H^{2/3}D^{5k/3}C^{2-5k/3}\right).}                      \tag{5.1}
\]

Hence this entire contribution has energy O(D^(k+epsilon)H) if

\[
\boxed{C\ge\max\left\{1,
\left(\frac{D^k}{H^{5/6}}\right)^{1/(2k-2)},
\left(\frac{D^{2k}}H\right)^{1/(5k-6)}\right\}.}          \tag{5.2}
\]

**Proof.** The exterior character in the exact incidence decomposition is a contraction in the row norm, including all repeated-prime zeros. Take square roots in (4.1) and apply Minkowski over the shared ideals. The three terms before summation are sqrt(H)P^(1/2), H^(1/12)P, and H^(1/3)P^(5/6).

For the first, the shared ideals with |I|=2 cost harmonic logarithms and those with |I|>=3 have convergent sums. It is therefore O(D^epsilon sqrt(H)D^(k/2)). For the second, every other shared-ideal sum has exponent |I|>1, while the designated full-common-gcd tail satisfies

\[
\sum_{Nc\ge C}(Nc)^{-k}\ll C^{1-k}.
\]

Its contribution is O(D^epsilon H^(1/12)D^k C^(1-k)). For the third, all exponents 5|I|/6 exceed one; the designated tail is O(C^(1-5k/6)). Its contribution is O(D^epsilon H^(1/3)D^(5k/6)C^(1-5k/6)). Drop only nonnegative coprimality/support restrictions in these majorants. Squaring the sum of these three norm bounds proves (5.1). Comparing its last two terms to HD^k gives exactly (5.2). \(\square\)

At H=D^(1+theta), 0<theta<=1/10, k=3 gives the explicit threshold

\[
\boxed{C\ge D^{(5-\theta)/9}}.                            \tag{5.3}
\]

The other condition in (5.2) is C>=D^(13/24-5theta/24), which is weaker for every theta>=0. The previous all-row argument required C>=D^((5-theta)/8). Thus a strictly larger part of the actual sixth moment is now controlled, with the cutoff exponent lowered by (5-theta)/72. For k=2, (5.2) still gives C>=D^(3/4-theta/4).

This is a partial moment theorem on a specified summand of the exact expanded polynomial. It does not imply the full sixth moment, and it does not establish the amplitude exponent 23/36 or 17/24. The balanced small-overlap remainder, including c=1 in the fourth moment, remains outside the proved diagonal range.
