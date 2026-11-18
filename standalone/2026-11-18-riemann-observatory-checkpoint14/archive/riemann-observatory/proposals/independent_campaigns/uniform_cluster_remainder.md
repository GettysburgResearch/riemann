# A uniform remainder for two coalescing unit-circle roots

Author: equivalences research agent. Date2026-11-17. Status: self-contained elementary proof; independent advocate/skeptic and director adjudication complete for the stated scope. No claim of novelty, publication priority, or direct progress on RH. The sources motivating this exercise are Burnol math/0103058v2 §2 and BCF1211.5191v1 Theorem2. Neither is being cited as proving the finite-N bound below.

## Theorem E-UNIFORM-001

Let N>=0, L=N+2, and define the **actual** approximation optimum

E_N(theta)=inf_{deg A<=N}(1/(2pi))integral_0^(2pi)|1-(1-z)(1-exp(-i theta)z)A(z)|² dt,

where z=exp(it). Let

F(c)=(2-2 sin(c)/c)/(1-(2sin(c/2)/c)²), c!=0,

and F(0)=4. For every real C>=0, put B=12+C². Then, simultaneously for every integer N>=0 and every real |c|<=C,

|L E_N(c/L)-F(c)| <= 38 B²/L.

A considerably smaller bound applies once L>=6B:

|L E_N(c/L)-F(c)| <= (2B²+5B)/L.

The constants are explicit and coarse, not optimized. The statement includes c=0. For finitely many small L, the interval |c|<=C may contain aliases c=2pi*j*L, j!=0; at those parameters the actual polynomial has one double root. The first displayed theorem uses that genuine optimum, not the singular two-distinct-evaluations quotient. The large-L proof excludes aliases automatically via its positive stable Gram determinant.

## Stable divided-difference formulation

For0<=x<=1 define

g_c(x)=(exp(icx)-1)/(ic) when c!=0, and g_0(x)=x.

This is continuous jointly in(c,x). Its x derivative has modulus1, and |g_c(x)|<=x. Define the continuous moments

b=integral_0^1 g_c(x)dx, a=integral_0^1 |g_c(x)|²dx, v=a-|b|²,

and the normalized discrete moments at x_k=k/L,0<=k<=L,

b_L=(1/(L+1))sum g_c(x_k), a_L=(1/(L+1))sum |g_c(x_k)|², v_L=a_L-|b_L|².

These are Gram moments in the divided-difference basis(1,g_c); they retain the derivative direction as c→0, unlike the two nearly parallel raw evaluation vectors.

For c!=0 put J(c)=integral_0^1 exp(icx)dx. Then

a=(2-2ReJ)/c², v=(1-|J|²)/c², and a/v=F(c).

At c=0 these extend to a=1/3,b=1/2,v=1/12 and a/v=4.

Whenever c/L is not a nonzero root-collision alias, the residual constraints R(1)=R(exp(ic/L))=1 are equivalent to sum r_k=1 and sum r_k g_c(k/L)=0. At c=0 the second constraint becomes sum k r_k=0, exactly the double-root derivative condition. The minimum-norm coefficient problem therefore gives

E_N(c/L)=a_L/((L+1)v_L)

whenever v_L>0, including c=0. This follows by inverting the stable2x2 Gram matrix with entries1,b_L,conjugate b_L,a_L, or by the orthogonal projection of the constant vector against the centered divided difference. No estimate on the inverse of the nearly singular raw evaluation Gram matrix is used.

## Elementary uniform determinant bound

For every real x,

(sin x/x)² <= 1/(1+x²/3),

with continuous value1 at0. Here is a self-contained proof. Put u=x². If0<=u<=3/2, the alternating cosine series gives

sin²x <= u-u²/3+2u³/45.

The tail after this cubic has the required sign: in the expansion of1-cos(2x), the omitted terms alternate with decreasing modulus when4u<=6. Moreover

(1-u/3+2u²/45)(1+u/3)=1-u²/15+2u³/135<=1

for0<=u<=3/2. Dividing byu and1+u/3 proves the claim in this range, with continuity at0. If u>=3/2, sin²x<=1<=u/(1+u/3), proving the remaining range.

Apply this with x=c/2. Since |J(c)|=|sin(c/2)/(c/2)|, it follows that

v(c)=(1-|J(c)|²)/c² >= 1/(12+c²) >=1/B,

also atc=0 by continuity. This bound is polynomial in C and avoids selecting a small separation-dependent interval.

## Uniform quadrature estimates

If f:[0,1]→C is K-Lipschitz, its normalized endpoint sample mean obeys

|(1/(L+1))sum_(k=0)^L f(k/L)-integral_0^1 f(x)dx| <= K/(L+1).

Indeed write the sample mean as L/(L+1) times the left rectangle mean plus f(1)/(L+1). The rectangle error is at most K/(2L), while |f(1)-integral f|<=K/2; multiplying and adding gives K/(L+1).

Since g_c is1-Lipschitz and |g_c|² is2-Lipschitz, uniformly in c,

|b_L-b|<=1/(L+1), |a_L-a|<=2/(L+1).

Also |b|,|b_L|<=1/2, because |g_c(x)|<=x. Hence

|v_L-v| <= |a_L-a|+|b_L-b|(|b_L|+|b|) <=3/(L+1).

Finally a<=1/3 and a_L<1/2 for L>=2.

## Proof for large L

Assume L>=6B. The previous estimates imply v_L>=1/B-3/(L+1)>=1/(2B)>0. Thus the stable Gram formula is valid, and there can be no nonzero alias in this regime. Using a<=1/3,

|a_L/v_L-a/v| <= |a_L-a|/v_L + a|v_L-v|/(v_L v)
                  <= (4B+2B²)/(L+1).

Moreover a_L/v_L<=B. Recalling L/(L+1)=1-1/(L+1),

|L E_N(c/L)-F(c)| <= (4B+2B²)/(L+1) + B/(L+1)
                      <= (2B²+5B)/L.

All estimates include c=0 without division by c and are uniform over |c|<=C.

## Proof for all remaining L

For2<=L<6B, choose A=0 to get0<=E_N(theta)<=1 for every theta, including aliases. Also0<=F(c)=a/v<=B/3. Consequently

L|L E_N(c/L)-F(c)| <=L²+(B/3)L <36B²+2B²=38B².

For L>=6B the stronger large-L constant satisfies2B²+5B<=38B² because B>=12. This proves the all-L bound.

## Scope and next steps

This is a genuine uniform O_C(1/N) remainder, rather than a fixed-c convergence assertion. It controls the coalescing derivative direction explicitly. It does not supply a useful infinite-zero arithmetic estimate: constants must still be tracked as the cluster size or scaled diameter grows, and root-dependent optimal coefficients need not become usable Dirichlet-polynomial coefficients.

Next precise problem: for a fixed m-root cluster with scaled positions c_j in a compact set, construct a confluent divided-difference Gram basis, prove a uniform lower bound through all collisions, and quantify its dependence on m and the cluster diameter. Before transferring anything to zeta, establish bounds for grouped rational principal parts with the same constants.

Exact rational-circle checks in the earlier cluster campaign and the explicitly unvalidated float stress test in experiments/code/uniform_cluster_remainder.py are supplemental, not the proof. The source of truth for this theorem is the argument above. Historical novelty remains unassessed.

## Independent review

The advocate independently checked the determinant inequality and derived the stronger18B² all-L constant by direct1-cos kernel quadrature. The parent independently obtained the same alternate kernel estimate. This note retains the conservative38B² constant proved above. See the independent review in audits/adversarial_reviews/uniform_cluster_skeptic.md (or the filename recorded in the merged audit manifest if renamed). No formal proof-assistant validation or novelty search is claimed.
