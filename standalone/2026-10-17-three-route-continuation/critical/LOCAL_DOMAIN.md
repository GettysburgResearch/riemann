# Exact ramified Euler factors and an enlarged correction domain

Status: proposed source-level structural component with a full written proof. This sharpens the analytic domain and row-norm bound for the ACTUAL correction factor in the CT/OpenAI Poisson identity. It does not by itself justify a new global contour shift or prove a new zero-free region.

Scope: fixed field F containing mu_12, fixed S and source local choices, fixed PRINCIPAL target character, and every actual sixth-power-free Poisson row u, including its finite S-unit classes. Every exterior valuation j=0,...,5 and the original zero extensions are retained. Angular phases are retained and are not treated as finite-order Hecke twists.

Exact primary source: OpenAI/math commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`, blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`. This file was fetched at the exact commit. The load-bearing source formulas are `eq:exact-Euler-factor`, `eq:C-local-values`, `eq:Euler-good-exact`, and the definition of H immediately following it. CT v2 Section 11 imports this finite local calculation for its fixed data. The fixed target called eta in that source is specialized to 1 here; the angular phase is denoted Phi, avoiding that notation collision.

The gain comes from evaluating the bad-prime sums exactly. The older bounds used the universal estimate |C_(t,1)|<=Q^(t+1/2) even in boundary cases where the two nontrivial Gauss sums give the smaller exact size Q^t. They also treated the l and m sums without fully using their valuation coupling. The exact calculation removes two previously imposed inequalities.

## 1. Variables and native local conventions

At an exterior prime p of norm Q, let

    j=v_p(u),  alpha=chi_p(u/p^j) in mu_6,
    Phi=vartheta(p),  gamma=gamma_2(p),
    r=Q^(-1),  D=Q^(-xi),  P=Q^(-w),  V=Q^(-6z),
    A=Phi^6 Q^4 D^6,  E=A V.                              (1)

Here |Phi|=|gamma|=|alpha|=1. Write tau_v for the source Gauss sum, with indices modulo six. The source normalizations give

    tau_0=-1,  |tau_v|=sqrt(Q) for v=1,...,5,
    tau_1 tau_5=Q,  gamma Phi tau_1=-sqrt(Q).               (2)

The last identity uses the PRINCIPAL target character; it does not set the angular phase Phi to one. The first identity retains the zeroth-power character's unit mask on a nontrivial residue ring.

For e0=0,1 and l,k,m>=0 put t=e0+3l and J=j+6m. The exact local factor is

    F_(u,p)=sum_(e0,l,k,m)
      gamma^e0 Phi^t alpha^(k-t) C_(t,k)(J)
      Q^(-e0(1/2+xi)-l(1+3xi)-k w-6m z).                 (3)

For t=0,

    C_(0,0)(J)=1,  C_(0,k)(J)=1_(J=0) for k>0.

For t>0,

    C_(t,0)(J)=1_(J>=t-1) Q^(t-1) T_t(p^(J-t+1)),
    C_(t,1)(J)=1_(J>=t) tau_1 Q^(t-1) T_(t-1)(p^(J-t)),
    C_(t,k)(J)=0 for k>=2,                                (4)

where

    T_v(1)=tau_v,
    T_v(0)=Q-1 if v=0 mod6, and 0 otherwise.               (5)

In (4), a positive power of p is interpreted as zero in the residue field. The source's absent modulus at exponent zero is a different convention from its masked zeroth-power character. Equations (3)--(5) retain this distinction throughout.

At a good prime j=0, the extracted variables are

    D1=alpha^(-1)D,  W=alpha P.

Consequently D1 W=DP=Q^(-xi-w) for EVERY row u. This is the reason the common leading factor below is a zeta function, despite the two conjugate row characters.

At a bad prime j>=1, the extracted reciprocal and numerator Euler variables are BOTH zero, by the original nonunit extensions. Thus

    H_(u,p)=(1-V)F_(u,p)                  if j>=1,
    H_(u,p)=(1-V)(1-W)F_(u,p)/(1-D1)      if j=0.          (6)

The unit alpha still occurs inside the exact bad-prime sum (3); it is not confused with these two extracted zero values.

## 2. The exact table for all six valuations

For j=0 the source formula is

    F_0=1/(1-V)+W/(1-W)
        + E/(1-E)[(1-r)/(1-V)+W]
        - D1/(1-E)[1+(Q-1)WV/(1-V)].                      (7)

For j=1,...,5 define delta_1=1 and delta_j=0 for j>=2, and the following finite numerators:

| j | T_j |
|---|---|
| 1 | D P |
| 2 | Phi^3 alpha^3 tau_3 Q D^3 |
| 3 | gamma Phi^4 alpha^2 tau_4 Q^(3/2)D^4 + Phi^3 alpha^4 tau_1 tau_2 Q D^3 P |
| 4 | gamma Phi^4 alpha^3 tau_1 tau_3 Q^(3/2)D^4 P |
| 5 | -r A |

**Lemma 1: exact bad-prime formula.** For each j=1,...,5,

    F_j=1/(1-V)+(1-r)E/[(1-E)(1-V)]
        -(Q-1)DP V^(delta_j)/[(1-E)(1-V)]
        +T_j/(1-E),                                      (8)

and hence

    H_j=[1-rE-(Q-1)DP V^(delta_j)+(1-V)T_j]/(1-E).        (9)

For j=1 this simplifies further to

    H_1=[1-rE+(1-QV)DP]/(1-E).                            (10)

The subscript H_1 in (10) denotes LOCAL valuation j=1; it does not denote the global principal row.

### Proof by complete support enumeration

The t=0,k=0 terms give 1/(1-V) for every j. The t=0,k>0 terms occur only for j=0,m=0 and sum to W/(1-W). They are absent for every bad prime.

For positive t, the allowed residues are t=0,1,3,4 mod6, because t=e0+3l. The k=0 term has two possible types:

- INTERIOR: J>=t, requiring t=0 mod6 by (5). Write t=6d, d>=1. For every j, m>=d. Its double geometric sum is `(1-r)E/[(1-E)(1-V)]`.
- BOUNDARY: J=t-1. The possible pairs (t mod6,j) are (0,5), (1,0), (3,2), (4,3). Their first nonzero terms, before the common 1/(1-E) factor, are respectively `-rA`, `-D1`, `Phi^3 alpha^3 tau_3 QD^3`, and `gamma Phi^4 alpha^2 tau_4 Q^(3/2)D^4`.

For k=1 there are also two types:

- INTERIOR: J>t, requiring t=1 mod6 by (5). Write t=6d+1, d>=0. The source phase identity in (2) makes its leading coefficient `-(Q-1)DP`. The condition J>t is m>=d+1 for j=0,1 and m>=d for j=2,3,4,5. This gives the common third summand of (8), or its V-weighted counterpart for j=0.
- BOUNDARY: J=t. The possible pairs (t mod6,j) are (0,0), (1,1), (3,3), (4,4). The corresponding first terms are `E W`, `DP`, `Phi^3 alpha^4 tau_1 tau_2 QD^3P`, and `gamma Phi^4 alpha^3 tau_1 tau_3 Q^(3/2)D^4P`.

In the (0,0) case d starts at one, since t=0 was already treated. Every other boundary sequence starts at d=0 except the k=0 (0,5) sequence, which starts at d=1 and has m=d-1. These initial indices explain the `E W` and `-rA` entries.

All other terms vanish by (4)--(5); k>=2 contributes nothing for positive t. Within every surviving boundary sequence, increasing t by six, l by two and m by one multiplies its term by exactly

    Phi^6 Q^(6-2) D^6 V alpha^(-6)=E.

The Gauss index stays unchanged modulo six. The same ratio governs the d progression of each interior sum, while its extra m progression has ratio V. Thus the displayed geometric summations account for all terms, not just a finite truncation. They converge absolutely when |V|<1 and |E|<1, and |W|<1 for the good-prime t=0 tail.

The good-prime boundary terms and interior sums recover (7), using (2). For j>=1, combining the appropriate boundary terms gives exactly T_j, hence (8). Multiplication by 1-V proves (9). Finally, for j=1, combine the DP terms as `(1-V)-(Q-1)V=1-QV`, proving (10). QED.

## 3. Removing two old inequalities in the full correction domain

Write x=Re xi, y=Re w and z_r=Re z. Define the open domain D by

    x>1/2, y>0, z_r>0;
    6z_r+y>1, x+6z_r>1, x+y>1;
    x+y+6z_r>2, 6x+6z_r>5.                              (11)

The notation z_r distinguishes a real part from the complex variable z. This is the former displayed correction domain with ONLY the two additional restrictions `3x>2` and `3x+y>5/2` removed.

**Theorem 1: enlarged full-family correction domain.** The exact correction

    H_u(xi,w,z)=product_(p notin S) H_(u,p)(xi,w,z)

is holomorphic on D for every original sixth-free row. On each fixed-margin closed subdomain of D, for every eta>0,

    |H_u(xi,w,z)| <<_eta (N u)^eta.                       (12)

The bound is uniform in all imaginary parts and in the actual row and its fixed finite local classes. Its constants may depend on F, S, the source local choices, eta, and the real-part margins. It is a bound for H, not for the reciprocal L-function. No nonvanishing of H_u is claimed.

### Proof for good primes

Let x,y,z_r belong to a fixed-margin subdomain of D. The denominators in (7) and (6) are uniformly nonzero: |D1|<1, |W|<1, |V|<1 and

    |E|=Q^(4-6x-6z_r)<Q^(-1).

The exact subtraction already present in the source, or expansion of (7), gives

    |H_(u,p)-1|
       << Q^(-6z_r-y)+Q^(-6z_r-x)+Q^(-x-y)
             +Q^(1-x-y-6z_r)+Q^(4-6x-6z_r).              (13)

All five prime-ideal series converge by (11). The constants are uniform in alpha and all vertical phases. The product over the good primes is therefore normally convergent and uniformly bounded, independently of which primes divide u.

### Proof for bad primes

The exact sizes of the table entries are

    |T_1|=Q^(-x-y),
    |T_2|=Q^(3/2-3x),
    |T_3|<=Q^(2-4x)+Q^(2-3x-y),
    |T_4|=Q^(5/2-4x-y),
    |T_5|=Q^(3-6x).                                     (14)

The two terms in T_3 are kept separately; no cancellation between them is used. All exponents are negative on D. In particular,

    3x+y-2=(2x-1)+(x+y-1)>0,
    4x+y-5/2=(3x-3/2)+(x+y-1)>0.                          (15)

Thus the old stronger inequalities are not needed for either mixed term. From (9), or (10) when j=1,

    |H_j-1| << |E|+Q^(1-x-y)+|T_j|.                      (16)

On every fixed-margin subdomain this is O(Q^(-delta)) for some delta>0 uniform in j=1,...,5. Every local denominator 1-E is nonzero, including at the smallest exterior prime.

The product over bad primes is finite. For any eta>0, choose a norm cutoff large enough that `1+C Q^(-delta)<=Q^eta` above it. The finite collection of smaller prime ideals contributes a fixed constant. Since the product of the distinct bad norms is at most N u, this proves (12). This argument does not require the literal product of bad-prime majorants over all primes to converge.

Normal convergence of the good product and holomorphy of the finitely many exact bad factors prove holomorphy of H_u. The formulas agree with the source on the initial absolutely convergent region, so they give the continuation of the original correction, not a replacement coefficient system. QED.

At a fixed z=2/5 or z=1/2, the domain simplifies to

    x>1/2, y>0, x+y>1.                                   (17)

All other inequalities in (11) then hold automatically. This removes the particular local-domain restriction behind the earlier good-class scale threshold. It does not establish that every other part of a global comparison can be shifted accordingly.

## 4. The common diagonal factor, with a quantified cost across it

Define the larger open domain D_star by

    x>1/2, y>0, z_r>0;
    6z_r+y>1, x+6z_r>1;
    x+y+6z_r>2, 6x+6z_r>5.                              (18)

Thus (18) also removes the inequality x+y>1. Set

    K_(u,p)=(1-Q^(-xi-w)) H_(u,p),
    K_u=product_(p notin S) K_(u,p).

**Theorem 2: common-pole factorization and powerful-row cost.** K_u is holomorphic on D_star, and on each fixed-margin subdomain,

    |K_u(xi,w,z)|
       <<_eta (N u)^((1-x-y)_+/2+eta),                    (19)

where r_+=max(r,0). There is the exact meromorphic identity

    H_u(xi,w,z)=zeta_F^S(xi+w) K_u(xi,w,z).                (20)

It holds initially by Euler multiplication and then by continuation. No nonvanishing of K_u is asserted. On the diagonal x+y=1 the bound in (19) is `(N u)^eta`; the same is true of every fixed-order transverse derivative on the complex diagonal w=1-xi, as specified below.

### Good-prime product after extraction

At j=0, put H_p^0=1+D1 W/(1-D1). Since D1W=Q^(-xi-w), the exact leading cancellation is

    (1-D1W)H_p^0-1 = D1^2 W(1-W)/(1-D1).                 (21)

The remainder H_p-H_p^0 has the four V/E bounds in (13), with the Q^(-x-y) term removed. Thus

    |K_(u,p)-1|
       << Q^(-2x-y)+Q^(-6z_r-y)+Q^(-6z_r-x)
             +Q^(1-x-y-6z_r)+Q^(4-6x-6z_r).              (22)

Every series converges on D_star. In particular 2x+y>1 follows from x>1/2 and y>0. The proof is uniform in alpha. The good-prime product is therefore holomorphic and uniformly bounded.

### The cost occurs only at valuations at least two

For j=1, (10) shows H_1 is bounded on every fixed-margin subdomain of D_star. The factor QV multiplying DP is also bounded there, because `x+y+6z_r>2` implies `Q^(1-x-y-6z_r)` decays. The factors E and 1-E are controlled as before.

For j=2,...,5, (14)--(15) give the uniform bound

    |H_j| << Q^((1-x-y)_+).                               (23)

Indeed T_2, the first term in T_3, and T_5 are bounded because x>1/2. The two mixed terms satisfy

    2-3x-y=(1-x-y)+(1-2x),
    5/2-4x-y=(1-x-y)+(3/2-3x),

so neither exceeds the common possible loss. Multiplication by `1-Q^(-xi-w)` costs at most two since x+y>0.

Only primes with j>=2 carry the power in (23). Therefore

    product_(p: v_p(u)>=2) Q^((1-x-y)_+)
       <= (N u)^((1-x-y)_+/2).

The remaining uniform constants per prime are absorbed into `(N u)^eta` by the elementary finite-small-prime argument. This proves (19) and the product's holomorphy. Equation (20) follows as in Theorem 1.

The factor 1/2 in this bound has a precise local origin. If x>1/2, y>0 and x+y<1 are fixed within D_star, then the j=2 formula has leading size `Q^(1-x-y)` as Q grows; its other displayed terms are smaller. A row u=p^2 has norm Q^2. Thus this local pointwise estimate cannot simply replace the cost by zero across the diagonal. This is a local observation, not a lower bound for the full product over all primes.

### Fixed-order transverse derivatives on the diagonal

Let a fixed-margin closed subdomain of D_star be intersected with the complex diagonal w=1-xi. In particular 1/2<x<1, and the real-part margins keep y=1-x bounded away from zero. Fix an integer k>=0. Then for every eta>0,

    |partial_w^k K_u(xi,1-xi,z)| <<_(k,eta) (N u)^eta.     (24)

To prove this, choose a positive r0 small enough that every disk `|w-(1-xi)|<=r0` stays inside a slightly larger fixed-margin subdomain of D_star. Apply (19) with loss eta/2 on the circle of radius

    r_u=min(r0, 1/log(2+N u)).

Its exponent `(1-x-Re w)_+/2` is at most r_u/2, so the extra norm power is at most exp(1/2). Cauchy's derivative bound contributes `k! r_u^(-k)`, which is at most a fixed multiple of `1+log(2+N u)^k`. This is absorbed into the remaining eta/2 power. The disk shrinks with the row norm only AFTER a common analytic neighborhood has been established; no unproved fixed-radius derivative bound is assumed.

## 5. What this result changes, and the remaining gap

Theorem 1 replaces a sufficient correction domain by a strictly larger one for the same actual Euler factors. It does not remove any Euler factor, change a shared-prime zero, replace full-norm ordering by conductor ordering, or enlarge the character family. The old inequalities are recovered if desired, so prior arguments remain valid on their original domains.

Theorem 2 identifies the exact common zeta factor at the functional-equation diagonal for every row. It also states the cost of moving across that diagonal and keeps the powerful-prime support responsible for that cost. The fixed-order derivative estimate concerns K_u, whose common pole has been extracted; it is NOT a bound for the original principal reciprocal detector or for a renormalized finite part of the full physical theta integral.

For the principal row and z=1/2, `DIAGONAL_FINITE_PART.md` separately proves the needed nonvanishing and identifies the renormalized first finite part with the native logarithmic derivative. Those principal nonvanishing claims are not generalized to arbitrary u here. Taking a full physical diagonal projection, controlling its signed finite part, and handling its Mellin weights and tails remain open.

A new zero-free comparison based on this enlarged domain must separately recheck every contour segment, residue, density class, physical scale, numerator mean, and tail. No such global extension is asserted in this component.

## 6. Verification boundary

`verify_local_domain.py` checks the exact source coefficients of all surviving branch types, the common geometric ratio, the assembled j=0,...,5 numerators, and negative controls for the unit mask and bad-prime common term. Its polynomial arithmetic is exact, uses explicit failing checks under normal and optimized Python, and reports file hashes. The written support enumeration proves that the branch list is complete and the geometric sums are infinite identities. The checker does not authenticate the full metaplectic construction, global Poisson identity, or a future contour comparison.
