# The exact Ramanujan threshold and the rate of recurrence

Assume RH. Write $y=\log n$, $t=\log y$, $E(y)=1/(\sqrt y\,t)$, and $B(n)=\log(\sigma(n)/(e^{\gamma_E}n\log\log n))$. Put
$$
 \beta=\sum_\rho |\rho|^{-2}=2+\gamma_E-\log(4\pi),\quad
 b_*=2\sqrt2-2-\beta,\quad
 F(t)=\sum_\rho e^{i\gamma t}/|\rho|^2,\quad D(t)=\beta-F(t)\ge0.
$$
Zeros are counted with signs and multiplicities. At this particular tolerance the primary census profile vanishes. Define
$$
 W_2(t)=-\sum_\rho e^{i\gamma t}/(1-\rho)^2,\quad
 \kappa=\sqrt2(2+\log2)-2,\quad C=\kappa+W_2(0).
$$
Then $1.8547590<C<1.8548767$, and the exact second-scale extremal statement is
$$
 \limsup_{n\to\infty}t\big(B(n)/E(y)+b_*\big)
 = C-\liminf_{t\to\infty}tD(t)
 \tag{1}
$$
in the extended reals. Thus a lower limit strictly below $C$ gives infinitely many strict exceedances of $-b_*E(y)$. A lower limit strictly above $C$ excludes all sufficiently large exceedances and equalities. Equality at $C$ requires finer information. In particular positivity of the secondary coefficient relative to the varying profile $F(t)$ alone gives neither conclusion about the global threshold.

Ramanujan's oscillatory upper bound and Nicolas's effective estimates are earlier results. Nicolas obtains a positive secondary lower coefficient at colossally abundant integers and an effective upper bound at all integers. Axler reviews these bounds and proves other explicit inequalities. Crim's November 2026 preprint gives $\kappa+W_2$ at colossally abundant integers and a further term. We include an independent asymptotic derivation needed for the integer count and the recurrence interpretation. [Nicolas](https://doi.org/10.1007/s11139-021-00491-y) · [Axler](https://doi.org/10.1007/s11139-022-00683-0) · [Crim, Theorem 1 and Corollary 4](https://hexagonmath.org/pdf/2611.00182v1)

## The tangent optimum to second order

Use a real tangent parameter $y\to\infty$, $s=1/(y\log y)$, and select the integer $m_y$ maximizing $\log(\sigma(m)/m)-s\log m$, choosing all equal-efficiency marginal factors at ties. This is the colossally abundant optimizer. The [tangent identity](robin-tangent-nov18.md) supplies baseline $-K(y)-R(y)$ before exponent deficits, where $R(y)=O(1/y)$ and $K$ uses $\vartheta$. Let $P(y)$ be the smallest possible total deficit, attained at $m_y$.

For $p\le y$ and positive exponent $j$, the exact local deficit is $(j-1)s\log p-\log(1-p^{-j-1})$. The absent prime costs $-\log(1-1/p)-s\log p$. For $p>y$ exponent zero is optimal. On $p\le y^{2/5}$ the candidate $j=\lfloor\log y/\log p\rfloor$ costs $O(1/y)$ per prime, hence these primes contribute $O(y^{-3/5})$. On $y^{2/5}<p\le y-1$ the first increment of log abundancy is at least $1/(p+1)\ge1/y\ge s\log p$ and a third increment is at most $p^{-3}<s\log p$. The optimum cost is therefore $\min(p^{-2},s\log p)+O(p^{-3})$. The at most two remaining integers near $y$ have cost $O(1/y^2)$ by taking exponent one. Restoring the discarded small primes in the min sum costs $O(y^{-3/5})$. Extending the inverse-square tail past $y$ costs $O(1/y)$. Thus, with $q^2\log q=y\log y$,
$$
 P(y)=s\vartheta(q)+\sum_{p>q}p^{-2}+O(y^{-3/5}).
$$
Here $q=\sqrt{2y}(1-\log2/(2t)+O(t^{-2}))$. The RH prime number theorem permits replacing the tail by $\int_q^\infty du/(u^2\log u)$ with error $O(q^{-3/2}\log^2 q)$. Partial integration gives $(q\log q)^{-1}(1-1/\log q+O(1/\log^2q))$. Consequently
$$
 P(y)/E(y)=2\sqrt2-\sqrt2(2+\log2)/t+O(t^{-2}).
$$

The [integrated explicit formula](robin-finite-horizon-nov18.md) for the $\psi$ analogue $J$ gives $-J(y)/E(y)=F(t)+W_2(t)/t+O(t^{-2})$. Indeed, with $a=1-\rho$, integrate $\int_t^\infty e^{-av}(v^{-1}+v^{-2})dv$ by parts twice. The first two coefficients after dividing by $\rho$ and normalizing are $1/(\rho a)$ and $(1-1/a)/(\rho a)=-1/a^2$. The remainder is $O(t^{-2}/(|\rho||a|))$ uniformly on RH because $\Re a=1/2$, $|a|>14$. The archimedean contribution is negligible here. Also $\psi(u)-\vartheta(u)=\sqrt u+O(u^{1/3}\log^2u)$ by the prime-power identity and RH. Integrating the square term gives $(J(y)-K(y))/E(y)=2-2/t+O(t^{-2})$. Thus the optimum baseline equals
$$
 (-K(y)-R(y)-P(y))/E(y)
   =-2\sqrt2+2+F(t)+(\kappa+W_2(t))/t+O(t^{-2}).
 \tag{2}
$$
This derivation uses neither Crim's numerical residual certification nor an assumption on zero spacings.

For every $n$ with $y=\log n$, (2) bounds $B(n)/E(y)$ above. Conversely $\log m_y=y+O(\sqrt y\log^2y)$. The first-prime cutoff is within one of $y$, and all additional increments satisfy $p^j\le 2y\log y$ by the marginal bound $p^{-j}$. Summing $\log p$ over those powers and using RH for $\vartheta(y)$ proves the claim. The tangent remainder at $\log m_y$ is $O(y^{-1}\log^3 y)$, negligible to either displayed order. Replacing $y$ in the normalization and in the oscillatory arguments by $\log m_y$ has negligible cost: both series have modulus of continuity $O(|h|\log^2(2/|h|))$ for $0<|h|<1/2$ by splitting their absolute sums at $1/|h|$ and using the Riemann–von Mangoldt count. Hence equality in (2) to its indicated order is realized at a CA number for each prescribed real center.

Finally $|W_2(t)-W_2(0)|\le\sqrt{2\beta D(t)}$ by weighted Cauchy–Schwarz, since the coefficient moduli of $W_2$ are $|\rho|^{-2}$. Pairing conjugates gives $W_2(0)=\beta-\tfrac12\sum_\rho|\rho|^{-4}$. Since $|\gamma|>14$, this gives the numerical enclosure above. Any subsequence with bounded $tD(t)$ has $W_2(t)=W_2(0)+o(1)$; unbounded $tD(t)$ cannot raise the upper limit. The upper and realized lower bounds in (2) prove (1).

## Secondary census and a Diophantine obstruction

In the slab $|\log n-y|\le y^{3/4}\log y$ let $V_*(y)$ count $B(n)\ge-b_*E(\log n)$. Then
$$
 \frac{t^{3/2}}{y^{3/4}}\log(1+V_*(y))
 =\pi\sqrt{2/3}\,\sqrt{[C-tD(t)]_+}+o(1).
 \tag{3}
$$
The same formula holds in $[e^y,e^y(1+e^{-d(y)})]$ whenever $0\le d(y)=o(\sqrt y/t)$.

To prove this take the exact local optimizer for each unit log bin. Its residual deficit budget, in units $E(y)/t$, is $\kappa+W_2(t)-tD(t)+O(t^{-1})$ by (2). The tangent error on the bin and changes across the wider slab are $o(1)$ in this normalization by the modulus of continuity just established. Where the positive-part budget is relevant $W_2(t)=W_2(0)+o(1)$. Use $h=y^{3/4}/\sqrt t$, $S=h/t$, so $hS/y^2=E(y)/t$. The [partition calculation](robin-census-constant-nov18.md) now yields (3) with these scales. Specifically, primes below $y^{3/5}$ have $\exp(o(S))$ exponent choices; for the remaining primes the relative-to-optimum partition sum is bounded by the product of the two-state factors and a convergent geometric tail as in the [strict entropy proof](robin-census-entropy-nov18.md). The scaled local prime density is Lebesgue measure because $h\gg y^{1/2}\log^2 y$. Optimizing the partition bound for a limiting nonnegative budget $g$ yields $\inf_{u>0}(ug+\pi^2/(6u))=\pi\sqrt{2g/3}$. For $g>0$ the two-sided Gibbs toggles around $m_y$ realize every slightly smaller budget. The root of $\log(1+1/p)-s\log p$ differs from $y$ by $O(1)$, so this changes only $O(1)$ edge factors. Replacing the slope at $\log m_y$ by $s$ costs $O(y^{-3/2}t h)=o(E(y)/t)$. Nonpositive limiting budgets give the zero normalized lower bound; budgets tending to minus infinity exclude candidates. Compactness on the bounded remaining range gives the uniform absolute $o(1)$. In the short intervals use the same mean tilt and integer-multiplier argument as in the linked partition calculation. One can choose $D_0\ge d(y)$ with $\sqrt S\,t=o(D_0)$ and $D_0=o(\sqrt y/t)$. Its denominator cost $O(D_0/(y t))=o(E(y)/t)$ and collision cost $O(D_0)=o(S)$ leave the positive limiting budgets unchanged.

The recurrence in (1) cannot be replaced simply by $F(t)\to\beta$. For any positive $\epsilon_j\downarrow0$ sufficiently small, continuity near zero and strict nonconstancy of $F$ give a point with $D\in(\epsilon_j,2\epsilon_j)$. Almost periodicity supplies arbitrarily large translates still satisfying that strict condition. Choose $t_j>\epsilon_j^{-2}$ in these sets. Then $F(t_j)\to\beta$ while $t_jD(t_j)\to\infty$. By (2), the CA numbers at those centers approach the constant $-b_*$ strictly from below in the primary normalization. Accordingly, the positive residual above the oscillatory baseline in Crim's Corollary 4(1) does not imply its literal claim of approach from above to the global limsup along every sequence for which $F\to\beta$. The same countersequence applies to Crim's normalization since converting logarithmic to additive abundance incurs exponentially small error in $t$ after primary normalization.

There is an explicit necessary phase restriction. If $tD(t)$ stays bounded on an unbounded sequence, then for every fixed finite list of positive ordinates all $\|\gamma_jt/(2\pi)\|\ll_j t^{-1/2}$. Already the first ordinate confines possible critical near-miss centers in $[T,2T]$ to a union of total length $O(\sqrt T)$. Taking $q$ to be the nearest integer to $\gamma_1 t/(2\pi)$ turns the other conditions into $\|q\gamma_j/\gamma_1\|\ll_j q^{-1/2}$. If any three ratios relative to a fourth ordinate obey $\sqrt q\max_j\|q\gamma_j/\gamma_1\|\to\infty$, (1) excludes critical near misses eventually. For Lebesgue-almost-every triple of real ratios this condition holds, by the convergent sum $\sum_q O(q^{-3/2})$ and Borel–Cantelli, applied to each fixed integer upper constant. It is a conditional test for the actual ordinates.

Conversely, the size of the required tail can be made explicit. If along $t\to\infty$ all phases $\gamma t$ with $0<\gamma\le A t\log t$ are within $c/\sqrt t$ of $2\pi\mathbb Z$, then $\liminf tD(t)\le\beta c^2/2+2/(\pi A)$. This uses $1-\cos u\le u^2/2$ and the signed-ordinate tail $\sum_{|\gamma|>H}|\rho|^{-2}\sim\log H/(\pi H)$. Choices making this upper bound less than $C$ would force infinitely many critical exceedances. Qualitative simultaneous approximation of each fixed finite list supplies no such relation between approximation error, height, and return time.

## The possible near-miss centers have finite total measure

For each fixed $A>0$ define $\mathcal C_A=\{t\ge1:D(t)\le A/t\}$. Without a Diophantine assumption on any ordinate, its tail satisfies
$$
 |\mathcal C_A\cap[T,\infty)|\ll_A 1/\log T.
 \tag{4}
$$
In each dyadic $[T,2T]$ the candidate centers are contained in $O_A(T/\log T)$ clusters, each of diameter $O_A(1/(T\log T))$. Distinct clusters have mutual distance at least $2\log T+4\log\log T-O_A(1)$. By (2), every sufficiently large integer meeting the exact borderline tolerance has its $t=\log\log n$ in such a cluster. The estimate is for the continuous set of allowed centers in the spectral condition. It does not count those integers.

For $h\to0$, the Riemann–von Mangoldt formula gives
$$
 D(h)\gg |h|\log(1/|h|):
$$
restrict the nonnegative signed-ordinate terms to $1/|h|\le|\gamma|\le2/|h|$, where $1-\cos(\gamma h)$ is bounded below. There is also an effective lower bound far from the origin:
$$
 D(h)\gg h^2 e^{-|h|/2}\qquad (|h|\ge h_0).
 \tag{5}
$$
For this use the positive arithmetic prime measure in the explicit formula. With $H\ge2$, put $K_H(v)=H(1-H|v|)_+$ and $w_H(\gamma)=(\sin(\gamma/(2H))/(\gamma/(2H)))^2$, its Fourier transform. On $v>0$ the distributional formula is
$$
 \sum_\rho e^{i\gamma v}
 =e^{v/2}-e^{-v/2}d\psi(e^v)/dv
   -e^{-v/2}\sum_{k\ge1}e^{-2kv}.
$$
Here RH supplies $\Re\rho=1/2$, and the notation for the derivative denotes a positive sum of prime-power atoms. For $h>1/H$ test with $K_H(v-h)$. The test is justified by positive compact smooth mollification, followed by dominated convergence in the zero sum since $w_H(\gamma)=O_H((1+\gamma^2)^{-1})$. The nonpositive atomic and trivial-zero contributions give
$$
 \sum_\rho \cos(\gamma h) w_H(\gamma)\le e^{(h+1/H)/2}.
$$
By the zero count $\sum w_H(\gamma)\ge c H\log H$ for all sufficiently large $H$, for instance by restricting to $|\gamma|\le H$. Since $(1/4+\gamma^2)w_H(\gamma)\le1/4+4H^2$,
$$
 (1/4+4H^2)D(h)\ge cH\log H-e^{(h+1/H)/2}.
$$
Choose $H=B e^{h/2}/h$ with a sufficiently large fixed $B$ to obtain (5). Also $D(h)>0$ for every fixed $h>0$ by allowing $H$ to grow; evenness gives the negative side. Continuity therefore supplies a positive lower bound on compact sets away from zero.

Finally $\sqrt{2D(u)}$ is the norm of $(|\rho|^{-1}(e^{i\gamma u}-1))_\rho$ in $\ell^2$. The triangle inequality gives $D(t-s)\le4A/T$ whenever $s,t\in\mathcal C_A\cap[T,2T]$. The near-origin lower bound forces $|t-s|\ll_A1/(T\log T)$ if $|t-s|$ is small. Otherwise compact positivity and (5) give $|t-s|\ge2\log T+4\log\log T-O_A(1)$ for large $T$. Small distance is then an equivalence relation on these centers: composing two small differences cannot give a large difference. Each equivalence class has the stated diameter, and the large separation bounds their number. Their total length in $[T,2T]$ is $O_A(1/(\log T)^2)$. Summation over $[2^jT,2^{j+1}T]$ proves (4).
