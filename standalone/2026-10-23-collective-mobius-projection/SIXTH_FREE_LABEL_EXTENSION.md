# Sixth-power-free labels and the optimized residue reference scale

23 October 2026. Proposed extension, independent review pending. The
squarefree-label proof `SHORT_LABEL_RESIDUE_VECTOR.md`, SHA256
`a003b982e012b3659329bc325b3b7d1f3db8aa7cd85f81b8120876e3c18c329f`,
is preserved unchanged. This note extends its V4 and V3 to all good
sixth-power-free labels, and improves its full-residue bound away from
the shortest-label range. All source and coefficient restrictions remain.

## 1. The local replacement for V5--V11

Let R be sixth-power-free. Split off from R the factor h consisting of
its primes that occur in the full modulus c, and write R=h R0. Thus
(h,R0)=1 and R0 is sixth-power-free. Write n=e g m, where g consists
of primes in both n and h, and e of primes in n and c but outside R.
Then c=e^2 l c0, with l supported on h and c0 squarefree. The m and R0
factors may share primes; both are coprime to e*h. Put H=Nh and L=Nl.

At p|h, let a=v_p(R) in {1,...,5}, epsilon=1_{p|n}, and j=v_p(c).
For 6 not dividing j, the only nonzero branch is j=a+epsilon+1,
with local squared scalar

    omega=(Np)^(-1-epsilon).

Here omega includes the n-normalization at p. The principal branches
are as follows; the last nonprincipal branch is also listed to avoid
omitting the case v_p(nR)=6.

| a | epsilon | j | omega upper bound |
|---|---|---|---|
| 4 | 1 | 6 | q^-3 |
| 5 | 0 | 6 | q^-2 |
| 5 | 1 | 6 | q^-1 |
| 5 | 1 | 7 | q^-2 |

These are the exact Ramanujan branches or their magnitude bounds.
At j=6,v=6 the factor is 1-q^-1 before the n-normalization. No local
zero is removed. The free m and R0 characters are both the j-th
power of the inverse local sextic character, including the principal
zero mask when j=6.

Aggregate e into the same unique sixth-power-free sieve column
r=e^2c0 as in V8. For fixed h,g,l and an e-dyad, the corresponding
positive row norm is bounded by

    omega(h,g,l)*(L/U)*Delta6(K/H,U/L)*I(CU,D/(gE);Q).

All coprimality masks needed in the m-sum are already enforced by the
inverse row or by the fixed puncture Qh. The row phase from l is
outside the R0-sum. The map r -> r*l remains injective even when l
has exponent six or seven. The inherited all-row inverse estimate
therefore applies. The sixth-free sieve itself is applied to r and
R0, not to l*r.

For each R there are only divisor-many choices of h and local branch;
Cauchy costs K^epsilon. The four positive sums to be bounded are

    sum omega,
    sum omega*L/H,
    sum omega*L^(2/3)*H^(-5/6),
    sum omega*L^(1/6)*H^(-1/3),

over H<=K. For a nonprincipal prime branch their local weights are

    q^(-1-epsilon), 1,
    q^(-1/3-a/6-epsilon/3),
    q^(-5/6-a/6-5epsilon/6).

The four principal entries in the table are no worse for the following
Rankin bounds. In the third sum the unique leading threshold is the
a=1,epsilon=0 weight q^-1/2; at Rankin exponent1/2+epsilon all prime
terms are summable. In the first and fourth sums the leading weights
are q^-1 and cost a subpower. The second sum has bounded local weights
and costs K^(1+epsilon). Thus the four cumulative bounds are

    K^epsilon, K^(1+epsilon), K^(1/2+epsilon), K^epsilon.

They reproduce V11 exactly. Consequently V4 holds for all good
sixth-power-free labels. V12--V14 are unchanged. In the primitive
density expansion, (d,R)=1 ensures dR is still sixth-power-free,
so V15--V16 are unchanged too. We obtain

\[
 \sum_{\substack{NR\le K\\R\ \text{sixth-power-free}}}
 (|P_R^{\rm full}(D)|^2+|P_R^{\rm prim}(D)|^2)
 \ll(DKNQ)^\epsilon D^{2/3},\qquad K\le D^{1/7}.       \tag{S1}
\]

## 2. Optimize the full-residue reference scale

Retain a free reference Y instead of setting Y=D. The original
completed finite vector V13 and the sum of the reflected scalar L13
give

\[
 \sum_R|P_R^{\rm full}(D)|^2\ll(YDKNQ)^\epsilon
 [Y^{2/3}+D^{5/6}Y^{-1/6}+K^2Y^{-1/3}
 +D^{5/6}K^{7/6}Y^{-1/3}
 +DK^2Y^{-4/3}+DK^{7/6}Y^{-1/2}].                    \tag{S2}
\]

For K<=D choose

    Y=max(D,D^(5/6)K^(7/6)).

If K<=D^(1/7), the earlier choice Y=D applies. Otherwise substitution
shows each term in S2 is bounded by D^(5/9)K^(7/9). In particular
K^2Y^-1/3 is smaller because K<=D, and the reflected nonvolume term
is smaller because K>=D^(1/7). Therefore

\[
 \sum_{R\ \text{sixth-power-free},\,NR\le K}
 |P_R^{\rm full}(D)|^2
 \ll(DKNQ)^\epsilon\{D^{2/3}+D^{5/9}K^{7/9}\},\quad K\le D.
                                                               \tag{S3}
\]

No optimized primitive analogue beyond S1 is claimed here.

Full-theta sixth-power periodicity at the residue, with the fixed
section scope of paper8, also gives the unrestricted-label consequence

\[
 \sum_{NR\le K}|P_R^{\rm full}(D)|^2
 \ll(DKNQ)^\epsilon
       \{D^{2/3}K^{1/6}+D^{5/9}K^{7/9}\},\quad K\le D. \tag{S4}
\]

Indeed write R=R0*b^6 uniquely and use rho_full(nR)=rho_full(nR0).
The first constant term is repeated O(K^(1/6)) times; the second sums
with b^(-14/3). This multiplicity is retained, not discarded.

## 3. Coherent full-series remainder mean

There is also a direct continuation consequence. Let R_R(U) denote
the raw full-series contour scalar L19. For K<=D^(1/7) and
U>=sqrt(D*K^7),

\[
 \sum_{R\ \text{sixth-power-free},\,NR\le K}|R_R(U)|^2
       \ll(UDKNQ)^\epsilon D^{11/12}K^{7/12}.          \tag{S5}
\]

To verify it, use exact reciprocal completion, retain every scale
U/a^6, and split at A=U^(1/6)D^(-1/12)K^(-7/12)>=1. The reflected
vector bound is DK^2/Y+DK^(7/6)Y^(-1/6), obtained by summing L13.
The original completed finite norm is V13, and S1 supplies its pole
vector. After summing a, the two nonvolume head/tail costs are both
D^(11/12)K^(7/12). The volume costs are at most D^(1/2)K^(7/2),
which is smaller for K<=D^(1/7). The original finite plateau costs
K^2+D^(5/6)K^(7/6) only logarithms: its finite part vanishes once
U/a^6 is below the first modulus. These costs and the full subunit
pole tail are also smaller in the stated range. The pole tail cost
is D^(5/6)K^(7/6). No divergent a^-1 tail of a nonzero plateau is used.

S5 is a full-series statement. It is not the moving-coprimality
primitive continuation or an estimate for the complete inverse norm.
