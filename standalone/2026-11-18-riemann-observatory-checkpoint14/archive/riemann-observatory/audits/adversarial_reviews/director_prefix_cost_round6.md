# Closed finite-prefix cost: independent adjudication

This is a finite polynomial theorem, independent of the unverified arithmetic prefix lower bound in rStation48 §8.1. The starting matrix is source(80), not its later arithmetic application. The director read both independent derivations, checked the kernel signs and parity, differentiated the variational maximum, and separately derived the endpoint Laplace constant. Source priority for the simplification is unassessed. No RH premise is needed.

Let m≥1,0≤b<1, δ=1−b,a=(1+b)/δ. Let M_ij=∫_b^1t^(i+j)dt and v_j=−1_{j=0}+m∫_0^bt^jdt for0≤i,j<m. Define c_m(b)=m²b+v^T M^(-1)v. M is positive definite because a nonzero polynomial cannot vanish on an interval. With the Legendre normalization P_n(1)=1,

    c_m(b)=m²+2∫_1^a[P′_(m−1)(x)]²dx.             (A)

## Proof from the Gram problem

On real polynomials of degree<m in L²[b,1], let p_b represent the functional ℓ_b(q)=−q(0)+m∫_0^bq. Thus its coefficients are M^(-1)v and

    c_m(b)=max_p {m²b+2ℓ_b(p)−∫_b^1p²}.

The maximizer depends smoothly on b. Differentiating at stationarity gives c′_m(b)=(m+p_b(b))². This also follows directly from M′=−dd^T,v′=md,d_j=b^j.

Use the orthogonal basis P_k(x(t)), x(t)=(2t−1−b)/δ. Its squared norms are δ/(2k+1). Parity shows that the functional coordinates are (−1)^k D_k, where

    D_k=−P_k(a)+(mδ/2)∫_1^aP_k(x)dx.

Multiplying by P_k(x(b))=P_k(−1)=(−1)^k cancels that sign. Consequently δp_b(b)=Σ_{k<m}(2k+1)D_k. The two elementary Legendre identities

    Σ_{k<m}(2k+1)P_k=P′_m+P′_(m−1),
    (x+1)(P′_m−P′_(m−1))=m(P_m+P_(m−1))

give

    δp_b(b)=−(P′_m+P′_(m−1))(a)
       +(mδ/2)[P_m(a)+P_(m−1)(a)−2],
    p_b(b)+m=−2P′_(m−1)(a)/δ.

For the second identity, substitute (x²−1)P′_n=n(xP_n−P_(n−1)) and the three-term recurrence; it also holds for m=1 directly. Since da/db=2/δ², dc_m/da=2[P′_(m−1)(a)]². At b=0 the kernel evaluation norm is Σ_{k<m}(2k+1)=m². Integrating proves(A).

The second independent proof expands the Christoffel–Darboux endpoint kernel and obtains the positive polynomial

    G_m(s)=m(m−1)Σ_{j=0}^{m−2}
       binom(m−2,j)binom(m+j,j)s^j/(j+1)
      =2P′_(m−1)(1+2s),
    c_m(b)=m²+∫_0^{b/(1−b)}G_m(s)²ds.

Its coefficient arithmetic and the variational differentiation agree. This supplies an independent check of the normalizations and sign of p_b(b).

## Exact consequences and separate asymptotic regimes

c_1=1,c_2=4/(1−b), and

    c_3=3(b³+9b²+3b+3)/(1−b)³.

For m≥2 all Taylor coefficients of P′_(m−1)(1+z) are positive, so c_m is strictly increasing in b and c_m(b)>m² for b>0. Keeping only its constant coefficient yields

    c_m(b)≥m²+m²(m−1)² b/(1−b),

with equality for m=1,2 and strict inequality for m>2,b>0. For fixed m≥2, the highest polynomial coefficient in(A) gives

    c_m(b) ~ 4(2m−3)binom(2m−4,m−2)²(1−b)^(-(2m−3))

as b→1. A naive power2m−1 is wrong: the leading highest-mode contribution cancels in the functional D_(m−1). For m=3,b=1/2 the exact cost165 also refutes both naive estimates m²/(1−b)=18 and the proposed upper bound m²/(1−b)^(2m−3)=72.

For fixed b∈(0,1), put R=a+sqrt(a²−1)=(1+sqrt b)/(1−sqrt b). As m→∞,

    c_m(b) ~ (1−b)² R^(2m−1)/(8πb).              (B)

An independent director derivation uses n=m−1,A(x)=sqrt(x²−1). Uniformly on a compact subinterval of(1,∞), the positive Laplace integral for P_n gives P_n(x)~R(x)^(n+1/2)/sqrt(2πn A(x)). The differentiation recurrence then gives P′_n~nP_n/A(x). Therefore [P′_n]²~nR(x)^(2n+1)/(2π A(x)³). Endpoint Laplace integration of2∫_1^a leaves R(a)^(2n+1)/(2π A(a)²), since(logR)′=1/A. The part below any fixed x0<a is exponentially smaller; monotone positive Taylor coefficients bound it by(x0−1)[P′_n(x0)]². Since A(a)²=4b/(1−b)², this is(B). The independent advocate instead sums the terminal Legendre modes with a geometric dominating bound and obtains the same prefactor.

These limits keep m or b fixed respectively. Neither yields uniformity in a joint limit or an asymptotic for a moving arithmetic prefix b(N). Even positive increasing functions F_N(b)=c_m(b)(1+b^N) converge to c_m(b) for every fixed b<1, while their ratio along b=1−1/N tends to1+e^(-1). Thus a separate uniform arithmetic estimate is necessary.

## Evidence and next questions

Independent proofs: [prefix_skeptic62.md](../prefix_skeptic62.md), [prefix_formula62_finite_cost.md](../prefix_formula62_finite_cost.md). Both independently implemented exact rational matrix solves and closed-form controls passed72 inputs, m1–12 and six rational prefixes. Their agreement is finite corroboration; the variational and Legendre proofs establish the full statement. See scripts/prefix_skeptic62.py and experiments/code/prefix_formula62_exact.py and their retained results.

Next precise questions: obtain a uniform transition asymptotic as m√b stays bounded (the b→0 edge is absent from(B)); characterize sharp joint b→1,m→∞ bounds; only after separately verifying the arithmetic prefix theorem ask whether its proof errors can be made uniform for b=b(N). Exact formula(A) alone cannot supply that arithmetic uniformity.
