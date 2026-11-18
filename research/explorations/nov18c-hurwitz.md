# The cost of approximating a zeta zero by a zero-free Euler source

**Proposed analytic theorem.** Suppose $\rho=\beta+i\gamma$ is an actual zero with $\beta>1/2$. Fix $1/2\le a<\beta$ and $0<c<\beta-a$. There are a compact disk $K\subset\{\Re s>a\}$ and a constant $P_1$ with the following property. Let $P\ge P_1$, and let
\[
    Z_P(s)=\sum b_P(n)n^{-s},\qquad b_P(n)=1\quad(n\le P).
\]
Assume uniform absolute majorants $\sum |b_P(n)|n^{-1-\epsilon}\le C_\epsilon$ for every $\epsilon>0$, and that $f_P(s)=(s-1)Z_P(s)$ continues to a holomorphic zero-free function on $\Re s>a$. Then
\[
                         \sup_{s\in K}|f_P(s)|\ge \exp(P^c).           \tag{1}
\]
The disk and threshold can depend on the fixed zero, $a,c$ and the majorants. The result also applies when $f_P$ is known to be zero-free only on a neighborhood of the disk chosen in the proof. It quantifies the failure of passing from the [zero-free comparison Euler products](nov18c-goldbach.md) to ordinary zeta by normal families. Those products have $|b_P(n)|\le d(n)$ and can be chosen to match every coefficient through $P$.

**Proof.** Put $f(s)=(s-1)\zeta(s)$. For fixed $b>1$ and $0<\kappa<b-1$, the two Dirichlet series and their first derivatives differ by $O(P^{-\kappa})$ on $\Re s\ge b$. This follows by extracting the power $P^{-\kappa}$ from their tails and absorbing $\log n$ with any smaller part of the remaining convergence margin. On a fixed compact subset of this half-plane the same bound holds for $f_P-f$ and its derivative. The actual $f$ is bounded away from zero on such a compact set.

Choose a real center coordinate $R>b$ and put $w=R+i\gamma$. Choose small $\varepsilon>0$ and set
\[
 r_0=R-b,\qquad r_1=R-\beta+\varepsilon,\qquad
 r_2=R-a-2\varepsilon,\qquad r_3=R-a-\varepsilon,
\]
where $r_0<r_1<r_2<r_3$. Work on the closed disk $K$ centered at $w$ of radius $r_3$; write $M=\sup_K|f_P|$. The holomorphic function
\[
                   U=f'-(f_P'/f_P)f
\]
has supremum $O(P^{-\kappa})$ on the concentric $r_0$ disk. Choose the logarithm of $f_P$ to be bounded at $w$, possible uniformly by its convergence there to $f(w)\ne0$. On the $r_3$ disk its real part is at most $\log M$. Borel–Carathéodory on an intermediate radius between $r_2,r_3$ and the Cauchy derivative bound on $r_2$ give $\sup_{r_2}|U|\ll 1+\log^+ M$. All disk-dependent factors are fixed before $P$ varies.

Choose a circle of radius less than $\varepsilon$ about $\rho$ on which $f$ does not vanish. The normalized contour integral of $U/f=f'/f-f_P'/f_P$ counts the zeros of $f$ inside that circle, with positive multiplicity. It follows that $\sup_{r_1}|U|$ has a fixed positive lower bound. Hadamard's three-circles theorem gives
\[
 1\ll P^{-\kappa\theta}(1+\log^+M)^{1-\theta},\qquad
 \frac{\theta}{1-\theta}=\frac{\log(r_2/r_1)}{\log(r_1/r_0)} .
\]
For fixed $b,\varepsilon$, this ratio tends to $(\beta-a-3\varepsilon)/(b-\beta+\varepsilon)$ as $R\to\infty$. With $\varepsilon$ small, $b$ large, $\kappa$ close to $b-1$, and finally $R$ sufficiently large, we obtain $\kappa\theta/(1-\theta)>c$. Absorb the fixed constant by enlarging $P_1$. This proves (1).

In particular, if one constructed such approximants throughout $\Re s>1/2$ and proved $\log^+\sup_K |f_P|=P^{o(1)}$ on every compact disk there along a common unbounded sequence of $P$, this would prove RH. Agreement of a long list of exact Euler coefficients alone does not supply that growth estimate.

## The sharp exponent among positive Euler approximants

Assume $\Theta<9/10$ and fix $1/2\le a<1$. Consider families as above that also come from positive integral Euler products with $0\le b_P(n)\le d(n)$. Define $\kappa(a)$ as the infimum of $d\ge0$ for which such a family, with $f_P$ holomorphic and zero-free in $\Re s>a$, satisfies for each compact $K\subset\{\Re s>a\}$ and each $\epsilon>0$
\[
                \log^+\sup_K |f_P|\ll_{K,\epsilon} P^{d+\epsilon}.
\]
Then
\[
                          \kappa(a)=\max(\Theta-a,0).
\]
The preceding lower bound applies separately to every ordinary zero to the right of $a$. If $\Theta\le a$ then ordinary zeta itself is an admissible constant family. To prove the remaining upper bound it suffices, by the infimum, to produce a family for each fixed $\Theta<b<9/10$ with exponent $b-a$.

Use the [simultaneous removal construction](nov18c-goldbach.md) on all off-line zeros with initial cutoff $P_0=2P$. Its $Z_+$ agrees with every ordinary coefficient through $P$ and removes all zeros in $\Re s>1/2$. Fix the jet order $J\ge1$, the delay exponent $A$ and the other construction parameters independently of $P$. The following bounds make the dependence on $P_0$ explicit.

* The smooth density is $O(t^{b-1})$ uniformly in $P_0$. Up to any $x\ge P_0$ the absolute value of the discrepancy between its integral and the signed *expected* prime mass is $O(x^{b-2/5})$ because only the final incomplete block enters, since both sources vanish before $P_0$. Bernstein's dyadic union bound in the construction can be required on **every** dyadic scale at least $P_0/2$. The summed failure probability is $O(P_0^{-2})$ with a fixed concentration constant. The two Markov cost bounds can have joint probability at least $3/4$ with fixed constants. Choose an outcome satisfying all these requirements for each sufficiently large $P_0$. The cumulative signed prime rounding error is then $O(x^{b/2}(1+\log x)^2)$ uniformly in both $x\ge P_0$ and $P_0$.
* For the calibration in centered derivative coordinates at $Y=P_0$, the initial residual norm is $O_J(P_0^{b-1}(1+\log P_0)^{2J})$ by the same uniform Markov bound. The inverse Vandermonde bound and number of fractional entries both depend only on $J$ and the fixed bands. They give $O_J(P_0^b(1+\log P_0)^{2J})$ correction primes in $[P_0,2P_0]$, then $O_J(1)$ per stage $[4^jP_0,2\cdot4^jP_0]$. The supply of fresh primes is uniform in $P_0$ by the ordinary prime number theorem and the uniformly small harmonic mass of the original marks.
* Write $H_P=-(Z_P/\zeta)'/(Z_P/\zeta)$. On each compact path in $\Re s\ge a'>a$ avoiding the selected zeros, its explicit density transform is $O(1+P_0^{\Theta-a'})$. In the normally convergent residue sum, factor $P_0^{\Re\rho-\Re s}$ out of each delayed Mellin term and bound it by $\max(1,P_0^{\Theta-a'})$. The remaining ordinate factors are polynomial and the fixed smooth Mellin factor decays faster than every power, uniformly on the path. The block and rounding errors cost $O(1)$ there by partial summation since $\max(b-2/5,b/2)<1/2<a'$. All higher prime powers also cost $O_{a'}(1)$ by absolute convergence of $\sum_p(\log p)p^{-2a'}$ and $|e_p|\le1$. The calibrated prime terms cost $O_J((1+P_0^{b-a'})(1+\log P_0)^{2J+1})$ by the stage counts.

To transfer these bounds from the logarithmic derivative to $f_P$, enclose the given compact in a fixed rectangle with closure in $\Re s\ge a'>a$, choosing its boundary free of selected zeros, and include a fixed real point $w>1$ on its right edge. At $w$ the logarithm of the positive ratio $Z_P(w)/\zeta(w)$ is uniformly bounded by the absolutely convergent Euler products, since $|e_p|\le1$. Integrate the real part of $-H_P(s)\,ds$ along the boundary to bound $\log|Z_P/\zeta|$ there, with constants independent of $P$. Multiplying by the fixed holomorphic $(s-1)\zeta(s)$ and applying the maximum modulus principle to $f_P$ fills the rectangle, including its removed zeros. This yields $\log^+\sup_K|f_P|\ll_{K,\epsilon}P^{b-a+\epsilon}$ as claimed.
