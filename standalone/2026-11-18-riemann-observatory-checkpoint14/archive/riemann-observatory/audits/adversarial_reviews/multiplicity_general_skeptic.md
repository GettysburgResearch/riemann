# Independent skeptic review: exact optimal window for one repeated root

Reviewer: equivalences agent. Date2026-11-17. The reviewer received the claimed coefficient and norm formulas, derived the argument below **before opening** the advocate proof, and did not rely on its numerical checks. This is independent mathematical reconstruction, not formal proof-assistant validation. No novelty claim.

## Statement reviewed

For integers m>=1,N>=0,L=N+m and D=(L+1)(L+2)...(L+m), put

a_n=binom(n+m-1,m-1)(L-n)(L-n-1)...(L-n-m+1)/D, 0<=n<=N.

Claim: A=sum a_n z^n is the unique minimizer of ||1-(1-z)^m A||² on degree<=N polynomials in H²(S¹), and the minimum equals

1-L(L-1)...(L-m+1)/D.

## Independent reconstruction

Define the polynomial extension

f(x)=[(x+1)...(x+m-1)/(m-1)!]*[(L-x)...(L-x-m+1)/D].

For m=1 the first product is empty and equals1. It has degree2m-1, agrees with a_n on0..N, and vanishes at integer points -1,..,-(m-1) and N+1,..,L. Furthermore

f(-m)=(-1)^(m-1).

Indeed the first product gives(-1)^(m-1) and the second numerator is (L+m)...(L+1)=D.

Let c_k be the residual coefficient of1-(1-z)^m A, for0<=k<=L. The backward difference nabla^m f(k)=sum_{j=0}^m(-1)^j binom(m,j)f(k-j) uses values of f only between -m and L. All values outside0..N in that range vanish except f(-m), which occurs only when k=0,j=m. Its contribution is(-1)^m(-1)^(m-1)=-1. Therefore

c_k=-nabla^m f(k), 0<=k<=L.

As an mth difference of a degree2m-1 polynomial, c_k is the restriction of a polynomial in k of degree at most m-1. Hence its mth forward difference vanishes. In the unit-circle coefficient inner product,

<R,z^j(1-z)^m>=sum_{s=0}^m(-1)^s binom(m,s)c_(j+s)=0,

for every0<=j<=N. All coefficient indices are within0..L. Thus R is orthogonal to the full admissible approximation space. Since1=R+(1-z)^m A, this establishes the projection minimizer. Multiplication by the nonzero polynomial (1-z)^m is injective, giving uniqueness. Finally

||R||²=<R,1>=c_0=1-a_0=1-(L)_falling_m/D.

The coefficients are real, so conjugation conventions do not affect the displayed normal equations. This proves the stated theorem independently.

## Boundary and asymptotic checks

- m=1: a_n=(L-n)/(L+1), error=1/(L+1), the elementary single evaluation constraint.
- m=2: recovers the independently checked exact double-root coefficients and error2(2L+1)/((L+1)(L+2)).
- N=0: a_0=1/binom(2m,m), precisely the best scalar projection onto(1-z)^m, because its squared coefficient norm is binom(2m,m).
- Error lies strictly between0 and1 for all stated parameters: each factor(L-j)/(L+j+1) lies in(0,1).
- For **fixed m**, the ratio product equals1-m²/L+O_m(L^-2); hence error~m²/N asN→infinity. No uniformity for growing m follows from this expansion.

## Classification

Independently checked with no issue found in the inspected statement and proof reconstructed above. The result is an elementary exact approximation theorem; it is not a new consequence about zeta zeros. Burnol's multiplicity-squared asymptotic is consistent but is not itself the provenance of this exact finite formula.

## Comparison with advocate file

Pending at the time this independent reconstruction was written; recorded below after opening that file.

After the reconstruction above, the reviewer opened proposals/independent_campaigns/multiplicity_general.md. The advocate uses the same finite-difference extension mechanism, with the same exceptional value at-m and boundary zero sets. All formula ranges, degree bounds, and normal equations agree. No discrepancy found. The all-m proof does not rely on finite testing or external source hypotheses. Its asserted asymptotic explicitly fixes m, as required. Verdict: verified within ordinary mathematical review of this self-contained exercise; historical novelty unassessed.
