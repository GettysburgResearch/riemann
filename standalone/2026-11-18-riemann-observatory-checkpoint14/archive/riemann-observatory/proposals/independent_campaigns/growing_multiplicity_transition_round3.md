# Exact growing-multiplicity transition in the polynomial model

Proposer: director.2026-11-17. Status: ordinary algebra/analysis proof supplied, independently reviewed by corpus and semantic_skeptic; director adjudicated. This is a consequence of the previously reconstructed exact finite-model formula, not a zeta theorem or novelty claim.

Let integersN>=1,m>=1, L=N+m, and letE_(N,m) be the optimal squared H2 error approximating1 by(1−z)^m A(z),degA<=N. The established exact formula is

E_(N,m)=1−product_(j=0..m−1)(L−j)/(L+1+j).

SetC=L+1/2, r=(m−1/2)/C<1, A=m²/C and

B=m²(2m²−1)/[12C³(1−r²)].

Then

1−exp(−A)<=E_(N,m)<=1−exp(−A−B),

0<=E_(N,m)−[1−exp(−A)]<=exp(−A)B.             (1)

Indeed log[(C−x)/(C+x)]=−2artanh(x/C). For0<=u<=r<1,

u<=artanh u<=u+u³/[3(1−r²)].

Apply this to x=j+1/2. The exact sums are sumx=m²/2 and sumx³=m²(2m²−1)/8. This proves A<=−log(1−E)<=A+B and(1), using1−exp(−B)<=B. All estimates are uniform inN,m; no unspecified fixed-m constant occurs.

AsN→infinity withm=m(N):

- Ifm²/N→lambda in[0,infinity), thenm/N→0,A→lambda,B→0, henceE→1−exp(−lambda).
- Ifm²/N→infinity, thenA=m²/(N+m+1/2)→infinity: for m<=N useA>=m²/(3N), while for m>N useA>=m/3. ThereforeE→1.
- E is asymptotic tom²/N if and only ifm²/N→0. Sufficiency follows from(1),A/(m²/N)→1,B/A→0 andA→0. For necessity, any subsequence withm²/N→lambda>0 finite has ratio→(1−exp(−lambda))/lambda<1; a further subsequence with m²/N tending to infinity has ratio<=N/m²→0. Ifm²/N does not tend0, extract one of these subsequences.

Thus the exact threshold for the familiar fixed-m leading term is m=o(sqrt N). Atm∼c sqrt N the approximation error has the nontrivial transition1−exp(−c²), and for larger multiplicity the error saturates at1.

An explicit absolute remainder for comparison withm²/N is

|E−m²/N|<=m²(m+1/2)/(NC)+A²/2+B,

from0<=A−(1−exp(−A))<=A²/2. This bound is deliberately simple rather than sharp.

The meaningful next problem is not to reprove this one-cluster formula, but to extend a comparable transition theorem to several growing confluent clusters. Existing fixed-m Hilbert-matrix constants deteriorate rapidly and do not settle that problem. The dimensionN here is polynomial degree; it is not automatically log of a Dirichlet-polynomial cutoff. Any arithmetic transfer must specify its own scaling map.
