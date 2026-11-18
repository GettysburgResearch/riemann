# Independent check: two roots separated on the 1/N scale

Reviewer: li_advocate, 2026-11-17. Independently derived after receiving only the equivalence agent's claim, without reading its proof or code. This is an elementary finite polynomial model; no novelty is claimed.

Take P(z)=(1−z)(1−qz), |q|=1,q≠1. Its reciprocal coefficients are a_n=(1−q^(n+1))/(1−q). For N≥1 use BCF's W_N=∑_(n=0)^N(1−n/N)a_n z^n. Direct convolution gives residual coefficients

c_0=0; c_k=(1+q^k)/N for1≤k≤N; c_(N+1)=−q(1−q^N)/[N(1−q)]; c_(N+2)=0.

Therefore its exact squared circle norm is

2/N + (2/N²) Re∑_(k=1)^N q^k + |1−q^N|²/[N²|1−q|²].

Let q=exp(ic/N) for fixed real c≠0. The first two terms tend to0; the last tends [sin(c/2)/(c/2)]². Thus this triangular window's error generally does not tend to0 even though, for each N with distinct roots, the corresponding fixed-polynomial BCF simple-root hypothesis is met. This illustrates a lack of uniformity when the polynomial itself depends on N; it is no contradiction to the published fixed-polynomial theorem. At c=2πj,j a nonzero integer, the boundary term and geometric sum vanish for all sufficiently large N, giving exactly2/N and hence no such obstruction at these resonances. At c=0 the double-root calculation gives exactly1+4/N, consistent with the continuous limit.

For the optimum over degree≤N polynomials, put L=N+2,M=L+1 and S=∑_(k=0)^L exp(ikc/N). The residual is exactly constrained by R(1)=R(q^(−1))=1. The two-row coefficient Gram matrix has diagonal M and conjugate off-diagonals S,bar S. Since the rows are independent, inversion yields the exact optimal squared norm

2(M−Re S)/(M²−|S|²).

As N→∞ with c fixed and nonzero, S/N→exp(ic/2)sinc(c/2), hence the optimum is asymptotic to F(c)/N, where

F(c)=2[1−sinc(c/2)cos(c/2)]/[1−sinc²(c/2)], sinc(x)=sin x/x.

For c≠0 the denominator is strictly positive. F(c)→4 as c→0 by Taylor expansion, and F(c)→2 as |c|→∞. This matches the confluent double-root constant4 and two separated simple-root constant2, respectively. The displayed expression does not itself prove uniform asymptotics for a variable c=c_N; that requires additional estimates, especially near c=0.

Classification: independently checked with no issue in the inspected polynomial claim. The unchanged triangular window fails for generic fixed c because a boundary coefficient remains of order1; the optimum still has error of order1/N. This is a precise computational stress test for any claim that a fixed-polynomial theorem is uniform over shrinking root gaps. It supplies no theorem about actual ζ zero gaps, simplicity, or arithmetic residue sums.
