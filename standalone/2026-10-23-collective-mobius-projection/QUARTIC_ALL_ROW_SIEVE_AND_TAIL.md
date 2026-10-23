# A quartic all-row sieve and a smaller primitive-sieve tail

Status: new derived component, 23 October 2026. This is not a centered inverse-moment theorem or a zero-free boundary. The estimates below follow from the squarefree quartic sieve and the complete multiplicative sieve; no priority claim is made. All ramified moduli in this note are fixed.

## 1. Inputs and conventions

Work over the Gaussian integers, omit the prime above 2, and choose primary generators. All norms below are ideal norms. Characters vanish at nonunits. Fixed ray restrictions, fixed angular phases in the column coefficients, and fixed column coprimality masks are allowed. Constants may depend on the fixed ray modulus. No column coefficient may depend arbitrarily on the unfrozen row.

The squarefree input is Blomer--Goldmakher--Louvel, [*L-functions with n-th order twists*, Theorem 1.3](https://arxiv.org/pdf/1112.1650), with n=4:

\[
 \sum_{Na\le A}^{\rm sf}\left|\sum_{Nm\le M}^{\rm sf}b_m(a/m)_4\right|^2
 \ll_\epsilon(AM)^\epsilon[A+M+(AM)^{2/3}]\sum_m|b_m|^2. \tag{Q1}
\]

Its finite reciprocity classes give the native Gaussian residue-symbol convention. Both orientations and complex conjugation have the same bound. The theorem permits arbitrary complex squarefree column coefficients.

We also use the complete multiplicative sieve

\[
 \sum_{N\mathfrak q\le Q}\sum_{\chi\bmod\mathfrak q}^{\rm primitive}
 \left|\sum_{Nm\le M}b_m\chi(m)\right|^2
 \ll (M+Q^2)\sum_m|b_m|^2. \tag{Q2}
\]

A harmless fixed-modulus factor is allowed. Here (Q2) is an inequality for the full primitive character family, not just one character per conductor. For completeness, primitive Gaussian fractions x/q with Nq<=Q are separated by a constant times Q^-1 on the two-dimensional torus: a nonzero difference has nonzero Gaussian numerator and denominator of modulus at most Q. The additive large sieve on a lattice disk of radius sqrt(M) has constant O(M+Q^2). Primitive Gauss inversion, followed by orthogonality over all characters modulo q, gives the usual Nq/phi(q) weight, which is at least one. This proves (Q2). Primary-generator and ray restrictions can be imposed by zero extension on the additive lattice and finitely many bad-place characters. The conductor-one character is bounded directly by O(M) times the coefficient norm. This is the same complete-sieve reduction recorded in PR1016, `QUARTIC_PRIMITIVE_SIEVE_TAIL.md`, section 5, at commit `7ea66551190f291101b0dd44fb1fc9b3331c560d`.

## 2. The all-row estimate

For X,M>=1 and arbitrary squarefree column coefficients,

\[
 \boxed{\sum_{0<Nr\le X}\left|\sum_{Nm\le M}^{\rm sf}b_m(r/m)_4\right|^2
 \ll_\epsilon(XM)^\epsilon
 [X+(XM)^{2/3}+MX^{1/4}]\sum_m|b_m|^2.} \tag{Q3}
\]

Every physical row is retained. Equivalently, the bilinear form with arbitrary complex row coefficients a_r is bounded by the square root of the bracket times ||a||_2 ||b||_2. The Hilbert-space dual has the same norm. The result is also valid with conjugated symbols.

Write uniquely

\[
 r=a b^2c^3d^4, \qquad a,b,c\text{ squarefree and pairwise coprime}. \tag{Q4}
\]

The variable d is arbitrary and may share primes with a,b,c. Freeze d and split a,b,c into dyads A,B,C. Put X_d=X/(Nd)^4, so AB^2C^3 is at most a fixed multiple of X_d. The factor (d^4/m)_4 is precisely the column mask 1_(m,d)=1, including its zeros. Thus its removal never replaces a zero by a unit phase.

For fixed b,c, absorb (b^2c^3/m)_4 and the d mask into the columns and apply (Q1) in a. Dropping the pairwise-coprimality restrictions enlarges the positive row sum. Since there are O(BC) pairs (b,c), this gives

\[
 [ABC+MBC+BC(AM)^{2/3}](XM)^\epsilon\|b\|_2^2. \tag{Q5}
\]

There is a second bound for the same dyad. After finitely many reciprocity sectors, the function m -> (ab^2c^3/m)_4 is a primitive character with good conductor abc. Its local exponents are respectively 1,2,3. In particular a quadratic local factor at a prime of b is still nonprincipal and primitive. The conductor and its nonzero local exponents determine the disjoint triple (a,b,c) uniquely. Thus this dyad injects, up to a fixed bad-place multiplicity, into the complete primitive family of conductor norm O(ABC). The d mask is a common column coefficient after d is frozen. Formula (Q2) gives

\[
 [M+(ABC)^2](XM)^\epsilon\|b\|_2^2. \tag{Q6}
\]

Set P=ABC, U=MBC, V=(ABC)^2 and Z=BC(AM)^(2/3). Then

\[
 \min(P+U+Z,M+V)\le P+Z+M+\min(U,V),
\]
\[
 P\ll X_d,\quad Z\ll(X_dM)^{2/3},\quad
 \min(U,V)\le U^{2/3}V^{1/3}
 =A^{2/3}B^{4/3}C^{4/3}M^{2/3}
 \ll(X_dM)^{2/3}. \tag{Q7}
\]

This proves the fixed-d bound X_d+(X_dM)^(2/3)+M. Summing d is a sum of positive row norms, not a Cauchy inequality between duplicate rows: (Q4) is unique. The first two d series have exponents 4 and 8/3 and converge; there are O(X^(1/4)) possible d. Dyadic factors are absorbed into epsilon. This proves (Q3). If rows at the fixed ramified prime are desired, split their valuations and absorb the finitely many corresponding column phases; the same geometric summation preserves (Q3).

The last term cannot in general be discarded: fourth-power rows repeatedly sample the principal column sum. No claim of a squarefree-row bound for all rows is being made.

## 3. Consequence for the exact squarefree-sieve tail

Use exactly the tail in PR1016:

\[
 T_R(k,D)=\sum_c {\xi(c)g_4(k,c)\over Nc}W(Nc/D)
       \sum_{d^2\mid c,\ Nd>R}\mu(d), \tag{Q8}
\]

where |xi|<=1 is any fixed function of c, W is bounded on a fixed annulus [a,b], and K,D,R>=1. Then

\[
 \boxed{\sum_{0<Nk\le K}|T_R(k,D)|^2
 \ll_\epsilon(KD)^\epsilon
 \left[{K\over R}+{(KD)^{2/3}\over R^2}
              +{DK^{1/4}\over R^{9/4}}\right].} \tag{Q9}
\]

One may take the minimum with the inherited bound K/R+D^2/R^4. The tail is exactly empty if R>sqrt(bD) or R>K. The zero row is excluded and has to be treated separately in an automorphic application.

Here are the local weights and summation, to make clear that no powerful row is omitted. Write c=mq with m squarefree, (m,q)=1, and q powerful. The sieve coefficient is

\[
 B_R(q)=\sum_{d\mid\operatorname{rad}q,\ Nd>R}\mu(d),
\]

which vanishes unless Nrad(q)>R and is divisor-bounded. If p=Npi and e>=2, the local normalized Gauss factor has these branches:

| Local exponent | Required row divisor rho | Absolute branch weight w |
|---|---|---|
| 4 does not divide e | pi^(e-1), with exact valuation | p^(-1/2) |
| e=4j, first Ramanujan term | pi^e | 1 |
| e=4j, second Ramanujan term | pi^(e-1) | p^(-1) |

The last two are the exact identity g_4(k,pi^e)/p^e=1_(pi^e divides k)-p^-1 1_(pi^(e-1) divides k). These are the local identities used in the pinned PR1016 proof; the primary source is [David--Dunn--Hamieh--Lin, section 3](https://arxiv.org/html/2306.11875v4).

For a fixed global q branch, put k=rho r. CRT and the squarefree Gauss identity turn its m sum into

\[
 w\,u(r)\sum_m b_{q,\mathrm{branch}}(m)\overline{(r/m)_4},
 \qquad |u(r)|\le1,
\]

with Nm bounded by a fixed multiple of D/Nq and coefficient squared norm O_W(1). All CRT phases, xi(mq), column zeros, and the fixed character of rho are in b. If Nq>bD or Nrho>K the branch is empty. Apply (Q3), with harmless constants when D/Nq is between fixed positive constants and 1, to get

\[
 w^2\left[{K\over N\rho}
 +\left({KD\over N\rho Nq}\right)^{2/3}
 +{D\over Nq}\left({K\over N\rho}\right)^{1/4}\right](KD)^\epsilon. \tag{Q10}
\]

At each nonzero k, the number of supported (q,branch) is bounded by a fixed power of tau(k): every prime of q divides k and e<=v_pi(k)+1. Cauchy is applied inside each physical row over only these supported terms. Its cost and |B_R(q)|^2 are absorbed into (KD)^epsilon. This is not a Minkowski sum over all q.

The three resulting Euler masses, with a prime p required to occur, have leading terms

\[
 \sum_{e,\mathrm{branch}}{w^2\over N\rho}=p^{-2}(1+O(p^{-1})),
\]
\[
 \sum_{e,\mathrm{branch}}{w^2\over(N\rho Nq)^{2/3}}
       =p^{-3}(1+O(p^{-2/3})),
\]
\[
 \sum_{e,\mathrm{branch}}{w^2\over Nq(N\rho)^{1/4}}
       =p^{-13/4}(1+O(p^{-1})). \tag{Q11}
\]

For example the nonprincipal branch exponents are e, (4e+1)/3, and (5e+3)/4, whose minima at e=2 are 2,3,13/4. The e=4j first branch exponents are 4j,16j/3,5j; the second are 4j+1,(16j+4)/3,(20j+7)/4. Thus all omitted terms decay faster. Fixing the squarefree radical a bounds these masses by Na^(-2+epsilon), Na^(-3+epsilon), and Na^(-13/4+epsilon). Summing Na>R gives R^-1, R^-2, R^-9/4, respectively, with epsilon loss. This proves (Q9).

## 4. Exact application budget, not a closure claim

Suppose a separate result controls the relevant full vector S by ||S||_2^2 << (KD)^epsilon K. Cauchy with (Q9), K=D^2/H, and the inverse-Poisson prefactor H/D gives a cross-term bound

\[
 (KD)^\epsilon\left[D R^{-1/2}
       +D H^{1/6}R^{-1}
       +D^{3/4}H^{3/8}R^{-9/8}\right]. \tag{Q12}
\]

The tail squared must also be included in the exact norm difference. It is smaller when each term in (Q12) is <=H and 1<=H<=D. Write H=D^alpha, R=D^r, 0<alpha<=1. A sufficient and exact maximum of the three cross-term constraints is

\[
 r\ge\max\{2-2\alpha,\ 1-5\alpha/6\}; \tag{Q13}
\]

the remaining constraint r>=2/3-5alpha/9 is weaker. At the quartic target alpha=14/15 this permits r=2/9, versus the inherited generic tail's r=4/15.

For comparison with the open low-divisor problem, if its centered error is separately bounded by H^(2-u)D^(u-1)R^gamma, then alpha=14/15 and r=2/9 require gamma<=(3/10)(1-u), with strict slack for epsilon losses. This improves the allowable level cost from (1/4)(1-u). Neither a per-level R^(2-2u) bound nor R^(1-u) suffices. Thus the remaining task is genuine signed/aggregate level cancellation; (Q9) does not prove it, nor does it furnish the premise on S in (Q12).
