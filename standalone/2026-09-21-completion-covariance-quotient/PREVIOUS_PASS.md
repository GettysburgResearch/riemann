# Source-completion covariance: preceding chat pass

Status: proposed component mathematics, not independent acceptance. RH and the complete native covariance estimate remain open. This document preserves the mathematical content of the preceding chat pass; it is not a verbatim transcript or a claim to recover its original executable files.

## Publication check, 21 September 2026

The user reported that another agent had published the preceding work and requested verification, publication if absent, then continuation. Searches of completion-related branches and reservoir-related issues, the default-branch code index, the live recent-PR collection, and the changed-file inventories of #903, #904 and #905 did not locate this specific three-point / square-reservoir / graph-energy packet. They DID locate the separate MCB31 executable restoration on #904 at aaea3f9605a430600bea0189397d93ca315b5f98. This is a scoped negative search, not proof that no copy exists anywhere. The present additive branch starts at that #904 head; main and all predecessor files are preserved.

Preceding reading pins: #904 5cd394d5dfe49d153be49e9eaab02e83efdce3f1; #905 98cf588261473724178231c667595fc09cc216fe; #903 530cc8f706b1f1e3dc7aff77efdced82e4ac73ad. Current continuation additionally inspected DCN26 at #903 f80aa1346bbc457d5726977c0b720162c05bb70e.

## 1. Motivation and inherited source

The question was whether changing the completed short source, without changing its exact Newton reconstruction, could remove the troublesome composite covariance. This is distinct from assuming favorable signs of its independently selected spectral components.

Let mu be the Mobius function, m(k)=sum_(n<=k) mu(n)/n, and F_Y=sum_(k<=Y)m(k)^2. A finite real source c retains c(n)=mu(n) for n<=Y and satisfies sum c(n)/n=0. Put

    m_c(k)=sum_(n<=k)c(n)/n,
    J(c)=sum_(k>=1)m_c(k)^2,
    U_d(c)=sum_(d|n)c(n)/n,
    B_q(c)=sum_(q|n)(c*c)(n)/n.

All convolutions are ordinary Dirichlet convolutions. The inherited cap-three greedy completion uses only the known prefix, has |c(n)|<=3 and support L0<=Y+ceil(Y/2)<=2Y, and satisfies J(c)<=2F_Y. Its proof uses |m(Y)|<=1 and charges its reciprocal tail to the previous half-prefix. At each later n, add an opposite-sign coefficient of magnitude min(3,n times the current absolute reciprocal residual).

For v_c=2c-1*c*c, the exact inverse identity is

    mu-v_c = mu*(delta-1*c)*(delta-1*c).

Consequently v_c(n)=mu(n) for n<(Y+1)^2. This short-prefix Newton identity is inherited; classical antecedents include Huxley--Watt, Mertens Sums requiring Fewer Values of the Mobius function, arXiv:1807.05890.

The complete harmonic output is

    Q_c(k)=sum_n (c*c)(n)/n H_floor(k/n)
          =sum_(q>=2) B_q(c) Z_q(k),

where H_0=0 and Z_q is the sum of the fully centered harmonic Fourier tails over the reduced fractions with denominator q. Both reciprocal and logarithmic moments of c*c vanish, so this full harmonic formula retains all centering constants. On the native range Q_c(k)=2m_c(k)-m(k).

For any balanced h supported strictly after Y, therefore,

    Q_(c+h)(k)-Q_c(k)=2m_h(k),  k<(Y+1)^2.             (P1)

This identity concerns the COMPLETE output, not an arbitrary denominator projection or its whole future beyond the native endpoint.

## 2. Optimal three-point cancellation

Assume Y>=7 and let P_Y be the primes 3(Y+1)/4<p<=Y. For each p in P_Y, add the triple

    h(2p-1)=-(2p-1)/(2p),
    h(2p)=2,
    h(2p+1)=-(2p+1)/(2p).                             (P2)

Each triple is reciprocal-balanced. Their supports are disjoint and lie beyond L0. The new source c_tilde=c+h is supported through 2Y+1 and still has coefficient cap three. The only indices divisible by a protected p are p and 2p, whose reciprocal masses are -1/p and 1/p. Hence

    U_p(c_tilde)=0,
    B_p(c_tilde)=B_(p^2)(c_tilde)=B_(pr)(c_tilde)=0

for distinct protected p,r. More strongly, every odd q divisible by a protected prime has B_q(c_tilde)=0. Group source masses by odd part: the whole odd-part p fibre has sum zero, and the odd neighbors in (P2) have no protected prime factor. Dirichlet convolution preserves this pushforward cancellation.

The primitive of one triple is -1/(2p) at 2p-1, +1/(2p) at 2p, and zero elsewhere. Thus

    J(h)=J(c_tilde)-J(c)=1/2 sum_(p in P_Y) 1/p^2 <=1/Y,
    J(c_tilde)<=2F_Y+1/Y.                             (P3)

For the inequality one can bound the number of terms by Y and use p>3(Y+1)/4. By (P1),

    sum_(k=Y+1)^((Y+1)^2-1) |Q_(c_tilde)(k)-Q_c(k)|^2
        =2 sum_p 1/p^2 <=4/Y.                        (P4)

The complete outputs are IDENTICAL on 2Y+1<=k<(Y+1)^2.

This perturbation is energy-minimizing among balanced perturbations supported in Y<n<=2Y+1 that cancel all selected U_p. Indeed cancellation forces h(2p)=2. Writing r=m_h gives r(2p)-r(2p-1)=1/p, whence r(2p)^2+r(2p-1)^2>=1/(2p^2). The involved pairs of coordinates are disjoint, and (P2) attains equality simultaneously.

## 3. The replacement modes were not discarded

For distinct protected primes,

    B_(pr)=0, B_(2pr)=-2/(pr), B_(4pr)=2/(pr).         (P5)

Let C_Y=2 sum_(p<r in P_Y)1/(pr). On Y<k<=floor(5Y/4), the original selected semiprime function is C_Y(H_k-2). After (P2), its replacement within the denominator family containing pr is

    C_Y[H_k-2H_floor(k/2)+H_floor(k/4)-2].             (P6)

The harmonic second difference is O(1/k), removing the logarithmically growing term but not the constant -2. Using the classical PNT, the old selected energy is asymptotic to log(4/3)^4 Y/[4(log Y)^2], whereas (P6) has energy asymptotic to log(4/3)^4 Y/(log Y)^4. This is a two-logarithm improvement for a specified family, NOT a bound for the full native covariance. The continuation examines the additional source-attributed divisor terms necessary to close that family; those are not automatically the whole actual B_2 or B_(2p) amplitudes.

The prior conclusion was that the ATC29 obstruction is valid for its chosen source and partition but is not invariant under completion. Neither its disappearance at q=pr nor (P6) proves that the full arithmetic difficulty disappears.

## 4. Square-reservoir cancellation of all pure large-prime denominators

Set R=ceil(sqrt(2Y)) and L=R^2. Starting from the cap-three completion, construct a balanced perturbation h supported in Y<n<=L such that

    U_p(c+h)=0 for every prime p>R,
    J(h)<=64 (L-Y)(2R-1)^2/Y^2 <=3072,
    J(c+h)<=2J(c)+2J(h)<=4F_Y+6144.                  (P7)

For R<p<=Y put t=floor(Y/p). Because p^2>2Y, the native contribution to p U_p is -m(t), of magnitude at most one. The completion contributes at most three more in absolute value, so |p U_p(c)|<=4. Assign coefficients of a common appropriate sign, each of magnitude at most eight, at p(t+1),...,p(2t), until their reciprocal masses cancel U_p. Capacity is sufficient since 8 sum_(k=t+1)^(2t)1/k>=4. For p>Y, cancel any original completion coefficient at p. These assigned indices are <=2Y, and different protected primes cannot share an index there.

Pair each assigned coefficient a_n at n with -q(n)a_n/n at q(n)=ceil(sqrt(n))^2. Assigned n is nonsquare; its large prime divisor could not divide the square root. Every reservoir square has root <=R and hence no prime factor >R. Thus these reservoir masses restore balance without undoing any protected U_p cancellation.

Between consecutive squares at most 2R-1 assigned terms remain uncanceled in the primitive, each of reciprocal magnitude at most 8/Y. Squaring this bound and summing at most L-Y positions proves (P7). The last numerical constant follows, for Y>=2, from R<sqrt(2Y)+1, L-Y<4Y, and (2R-1)^2<12Y.

All source indices are <=R^2, so each contains at most one prime >R and only to the first power. Their products can have pure large-prime divisor types only p, p^2, or pr. Balance gives B_p=-U_p^2, and absence of a source index divisible by pr gives B_(p^2)=U_p^2 and B_(pr)=2U_pU_r. Therefore

    B_q(c+h)=0 whenever every prime factor of q is >R. (P8)

Every surviving denominator has a prime factor <=R. The result does NOT cancel the mixed small/large-prime conditional amplitudes U_(pd).

Tradeoffs: coefficients can accumulate to O(sqrt(Y)) at reservoir squares, and squarefree support is not preserved. It is invalid to import old cap-three constants or SFC30's cubefree-support conclusions unchanged. MCB31's coefficient-cap-free microscopic theorem is compatible with the new source, subject to its actual support and localized energy hypotheses; its energy exponent remains quadratic.

## 5. General minimum-energy completion

For h supported in Y<n<=L with total reciprocal sum zero, let r(k)=m_h(k), r(Y)=r(L)=0. Then

    h(n)=n[r(n)-r(n-1)],
    J(h)=sum_(k=Y+1)^(L-1)r(k)^2,
    U_d(h)=sum_(k=Y+1)^(L-1)r(k)[1_(d|k)-1_(d|k+1)].

For a finite target set D, write A_(d,k)=1_(d|k)-1_(d|k+1) and u_d=U_d(c). The cancellation problem is Ar=-u. If and ONLY if u is in the range of A it is feasible; when feasible,

    min J(h)=u^T(AA^T)^+u,
    r_star=-A^T(AA^T)^+u.                             (P9)

These are ordinary minimum-norm linear algebra identities, not a new general pseudoinverse theorem. Coefficient caps add linear inequalities on successive differences; (P9) need not then give the constrained optimizer.

If D consists of primes >sqrt(L), each integer is labeled by its selected prime divisor or by zero. Columns of A are the incidence vectors of transitions between adjacent labels. AA^T is a grounded graph Laplacian, with zero as ground. The objective is exactly an electrical dissipation. In the three-point case AA^T=2I. Minimizing this source energy does not automatically minimize the remaining full covariance.

## 6. Historical computational statements and limitations

The preceding chat reported 62,068 exact coefficient comparisons, 31,034 primitive-output cells, largest full prefix 16,383, and 222 protected-prime constraints for the square construction. Its displayed square-reservoir panels were Y=31,63,127,255, with rounded J(h) values 0.152663, 0.166461, 0.091886, 0.095852, and maximum source coefficients 6.593998, 10.229307, 11.412913, 15.968554. Those original executable artifacts and receipts are not available in this session; these figures are preserved as HISTORICAL CHAT REPORTS, not newly authenticated results. The fresh continuation checker has its own independently declared panel sizes, implementation and counts.

The preceding pass did not run the full repository validator, supply a formal proof, obtain independent mathematical review, or prove an RH-bearing native gain. Its suggested next step was to exploit the completion constraints inside the microscopic kernel while paying the full replacement covariance. The continuation must test that suggestion rather than treat it as a theorem.
