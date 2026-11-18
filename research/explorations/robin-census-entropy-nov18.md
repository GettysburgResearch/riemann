# Counting Robin exceptions detects attainment of the real-part supremum

Write $V(N)=\#\{5040<n\le N:\sigma(n)\ge e^{\gamma_E} n\log\log n\}$ and $\Theta=\sup_\rho\Re\rho$. If $1/2<\Theta<1$ and $a=(1+\Theta)/2$, then
$$
 \log(1+V(N))\ll (\log N)^a/\log\log N.
$$
If a zero has real part $\Theta$, the two sides are comparable in both directions. If no zero attains $\Theta$, the left side is little-oh of the right side. The distinction uses the summable coefficients in the integrated explicit formula and the number of admissible exponent choices near a tangent optimizer.

## An upper bound for the total deficit

Partition by $v\le y=\log n<v+1$ for positive integers $v$. Put $s=1/(v\log v)$, $I_p(k)=1+\cdots+p^{-k}$ and $T_p(k)=\log I_p(k)-sk\log p$. Write $t_p=\max_{k\ge0}T_p(k)$ and $D_v(n)=\sum_p(t_p-T_p(v_p(n)))$. Only finitely many $t_p$ are nonzero. As established in the [tangent bound](robin-tangent-nov18.md), $t_p\le-\log(1-1/p)-s\log p$ when $p\le v$ and $t_p=0$ above $v$. Consequently at every exception
$$
 0\le D_v(n)\le -K(v)-R(v)+\log\log v-\log\log y+s(y-v)
 \le |K(v)|+O(v^{-2}/\log v).
$$
Here $K$ is the integrated $\vartheta$ error and $R\ge0$. The [integrated explicit formula](robin-finite-horizon-nov18.md) gives $|K(v)|\ll v^{\Theta-1}/\log v$. Indeed its $\psi$ analogue differs by $O(1/(\sqrt v\log v))$, and each normalized nontrivial-zero term is bounded by $C v^{\Re\rho-\Theta}/(|\rho||1-\rho|)$. This summable majorant yields $K(v)=o(v^{\Theta-1}/\log v)$ if no zero lies on the boundary. Denote the resulting uniform deficit budget for the bin by $D_v$.

## Counting exponent choices

The primes $p\le v^{3/5}$ have at most $\exp(O(v^{3/5}\log v))$ possible joint exponent vectors, since each exponent is at most $(v+1)/\log2$. Their deficits are nonnegative, so they can be discarded in bounding the count of the remaining choices.

Fix $M\ge1$, take $\lambda=Mv^{2-a}$ and $H=v^2/\lambda=v^a/M$. For $p>v^{3/5}$ put $h_p=\log(1+1/p)-s\log p$. Every marginal $T_p(k)-T_p(k-1)$ after the first is at most $p^{-2}-s\log p\le -s\log p/2$ for large $v$. Thus $t_p=\max(0,h_p)$, and the single-prime partition sum obeys
$$
 \sum_{k\ge0}e^{-\lambda(t_p-T_p(k))}
 \le 1+e^{-\lambda|h_p|}+\frac{p^{-\lambda s/2}}{1-p^{-\lambda s/2}}.
$$
The sum of the last terms over $p>v^{3/5}$ is $o(1)$ because $\lambda s\to\infty$. For $p\ge2v$ also $h_p\le-s\log p/2$ and the same summation bound applies. On $v^{3/5}<p<v/2$ monotonicity gives $h_p\gg1/v$, costing $O(ve^{-c\lambda/v})=o(1)$. The function $h(u)=\log(1+1/u)-s\log u$ has its unique zero within $O(1)$ of $v$, since $h(v)=O(v^{-2})$ and $-h'(u)\asymp v^{-2}$ on $[v/2,2v]$. On this last range
$$
 e^{-\lambda|h_p|}\ll \exp(-c|p-v|/H).
$$
On each side partition the interval into shells of length $H$. Brun–Titchmarsh gives $O(H/\log H)$ primes per shell with an absolute constant, including an incomplete last shell by enlargement. Summing the exponential weights gives $O(H/\log v)$, uniformly in the implied constant for each fixed $M$ and all sufficiently large $v$. Multiplying partition sums and using $D_v(n)\le D_v$ bounds the logarithm of the count in the bin, with 1 added inside the logarithm, by
$$
 O(v^{3/5}\log v)+\lambda D_v+O(v^a/(M\log v)).
$$
For $M=1$ this proves the claimed big-oh bound after summing over $O(\log N)$ bins. In the unattained case $\lambda D_v=o_M(v^a/\log v)$ for each fixed $M$. Taking the upper limit and then letting $M$ grow proves little-oh, also after summation over bins.

## A matching lower bound at an attained supremum

When $\Theta$ is attained, the [almost-periodic boundary profile and extremum argument](robin-lcm-short-nov18.md) give, in every sufficiently large $[Y,CY]$ for some fixed $C>1$, a point $x$ with $\psi(x)=x$ and LCM log Robin ratio at least $c_0 x^{\Theta-1}/\log x$. Indeed $-J$ has the same normalized profile as the LCM ratio. Bracket a positive peak by negative peaks in adjacent windows and take the interior minimum of $J$. The one-sided derivatives force $\psi(x)=x$. Fixed ratios preserve a positive constant in the amplitude.

Put $m=\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)$ and $H=b x^a$ with fixed small $b>0$. Multiply $m$ by an arbitrary subset of the primes $x<p\le x+H$. Each prime gains $\log(1+1/p)$ in log abundancy and raises the tangent to $\log\log y$ at $y=\log m=x$ by $\log p/(x\log x)$. Their difference is bounded below by $-C(H+1)/x^2$. By concavity this tangent bounds the entire increase of the denominator. The prime number theorem in short intervals (here $a>3/4$) gives both $\gg H/\log x$ and $\ll H/\log x$ primes. Hence the total loss is at most $C' b^2 x^{\Theta-1}/\log x$, smaller than the starting margin for small $b$. All resulting integers are distinct strict violations. Choosing the original bracket so $x\asymp\log N$ and $x\le(\log N)/2$ ensures that all lie below $N$, since their logarithms are at most $x+O(H)$. This proves $\log V(N)\gg (\log N)^a/\log\log N$.

## The strict-exception profile and its normalization

Assume now that $1/2<\Theta<1$ is attained. With signed ordinates and multiplicity, put
$$
 f(t)=\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)t}}{\rho(1-\rho)},\qquad
 c_* = \pi\sqrt{2/3},\qquad L(Y)=Y^a/\log Y .
$$
Here $a=(1+\Theta)/2$ as throughout this note. The integrated explicit formula gives $-K(Y)=(f(\log Y)+o(1))Y^{\Theta-1}/\log Y$. The same asymptotic holds for the LCM log Robin ratio at index $Y$: its square-prime corrections have smaller order and the logarithmic Taylor remainder is $O_\alpha(Y^{2\alpha-2}/\log Y)$ for $\Theta<\alpha<a$. These claims are the [boundary profile](robin-lcm-short-nov18.md) and its proof.

Define $V_{\rm loc}(Y)$ as the number of strict failures or equalities with $|\log n-Y|\le Y^a\log Y$, and $q_+=\max(q,0)$. Then
$$
 \frac{\log(1+V_{\rm loc}(Y))}{L(Y)}
   =c_*\sqrt{f(\log Y)_+}+o(1).
 \tag{4}
$$
In fact the lower bound counts strict failures only. When $f(\log Y)$ is bounded strictly below zero there are no failures in the slab for sufficiently large $Y$.

Here are the details adapting the [near-Robin partition calculation](robin-census-constant-nov18.md). Let $S=x^a/\log x$, $h=x^a$ and $E=x^{\Theta-1}/\log x$. Then $hS/x^2=E$. For a unit bin starting at $x$ within the slab, the exact baseline deficit in equation (2) of that calculation is nonnegative and bounded by $(f(\log Y)+o(1))E$ at each exception. Uniformity over these bins follows from $x/Y\to1$ uniformly and uniform continuity of the absolutely convergent series $f$. For fixed $t>0$ let $\lambda=tx^2/h$. The local prime partition computation applies verbatim with this $h$: $h\gg x^\alpha\log x$ for some $\Theta<\alpha<a$, $\lambda s\to\infty$ and $x/h$ grows as a power. It gives log partition sum at most $(\pi^2/(6t)+o(1))S$. The number of bins contributes only $O(\log Y)$ to the logarithm. Along any sequence on which $f(\log Y)\to F\ge0$, optimize $tF+\pi^2/(6t)$ over fixed positive $t$ to get the upper bound $c_*\sqrt F$, including zero by taking $t\to\infty$. If $F<0$ nonnegativity of the deficit excludes all exceptions.

For the lower bound when $F>0$, take $x=Y$ and begin at its LCM. Its log Robin ratio is $(F+o(1))E$ and $\log m=\psi(x)=x+O_\alpha(x^\alpha)$. Toggle primes on either side of $x$ up to distance $Mh$ with $M$ fixed. All configurations lie within the slab because their log sizes differ from $x$ by $O_M(h)+O_\alpha(x^\alpha)$. Concavity, linearization at $\psi(x)$, replacement of the slope by $s=1/(x\log x)$ and Taylor expansion of the two marginal costs bound the loss by
$$
 (h/x^2)\sum_{p\ {\rm toggled}}|p-x|/h+o(E)
$$
uniformly. The slope replacement relative to $E$ costs $O(x^{\alpha-a})$. The prime counts and all Taylor remainders obey the estimates of the linked partition calculation since $hS/x^2=E$. Its independent Gibbs toggles with parameter $t>\pi/\sqrt{6F}$ have limiting mean normalized cost at most $\pi^2/(6t^2)<F$, variance $O_M(S)$ before normalization, and hence yield strict violations with probability tending to one. The same concentration and log-probability calculation gives an entropy lower bound tending, as $M\to\infty$, to $\pi^2/(3t)$. Let $t\downarrow\pi/\sqrt{6F}$ to get $c_*\sqrt F$. For $F=0$ the nonnegative lower bound suffices. Applying this argument to convergent subsequences of the bounded signal proves (4) with an absolute $o(1)$.

For the cumulative function,
$$
 \frac{\log(1+V(e^Y))}{L(Y)}
 =c_* G(\log Y)+o(1),\qquad
 G(t)=\sup_{h\ge0}e^{-ah}\sqrt{f(t-h)_+}.
 \tag{5}
$$
For the upper bound cover by unit bins, each contained in its own local slab, and use (4) with the largest resulting exponent. Integer bins below $\sqrt Y$ have negligible normalized logarithm by the first upper bound of this note. With $t=\log Y$ and $u=Ye^{-h}\in[\sqrt Y,Y]$, the ratio $L(u)/L(Y)=e^{-ah}t/(t-h)$ differs from $e^{-ah}$ uniformly by $O_a(1/t)$. For the lower bound restrict $h$ to $[0,K]$ for arbitrary fixed $K$. Center the local slab at $u'=u-3u^a\log u$ so it lies below $Y$. Its main term differs uniformly from $c_*L(u)\sqrt{f(\log u)_+}$ by $o(L(Y))$. Finally take $K\to\infty$, using boundedness of $f$ to control the omitted part of the supremum.

### What the cumulative profile determines

Both $f$ and $G$ are uniformly almost periodic. For $G$ this follows because the map taking a bounded input $b$ to $\sup_{h\ge0} e^{-ah}b(\cdot-h)$ is Lipschitz in uniform norm and commutes with translations. The positive-part square root is uniformly continuous on the bounded range of $f$. An almost-periodic function known up to $o(1)$ at positive infinity is unique: its relatively dense approximate periods carry any nonzero value to arbitrarily large positive arguments. Hence (5) determines $G$ uniquely.

In this class the running supremum also determines the entire Fourier series $f$, including multiplicities of the boundary zeros. We give the uniqueness argument, which does not assume analyticity of $f$. Ingham's zero-density theorem at any fixed $b\in(1/2,\Theta)$ bounds the number of its boundary frequencies up to height $T$ by $O(T^k)$ for some $k<1$. In particular $\sum_{\Re\rho=\Theta}|\Im\rho|/(|\rho||1-\rho|)<\infty$, so $f$ is $C^1$ and $f'$ is uniformly continuous. Its mean is zero, it is nonzero, and $M_0=\sup f>0$.

There is an open interval on which $W(t)=e^{2at}G(t)^2$ increases strictly. Indeed choose $t_n$ with $f(t_n)\to M_0$; uniform continuity of $f'$ implies $f'(t_n)\to0$ (otherwise an integral of the derivative to one side would exceed $M_0$). Some fixed $\ell>0$ then ensures $f>M_0/2$ and $|f'|<a M_0/2$ throughout $[t_n-\ell,t_n+\ell]$ for all large $n$. Consequently $e^{2at} f(t)$ increases strictly there. For such $n$ also $f(t_n)>e^{-2a\ell}M_0$. All arguments $u\le t_n-\ell$ therefore have $e^{2au}f(u)_+<e^{2at_n}f(t_n)$. The running maximum $W(t)=\sup_{u\le t}e^{2au}f(u)_+$ now increases strictly on $(t_n,t_n+\ell)$.

On any open interval where $W$ increases strictly, continuity implies $e^{2at}f(t)_+=W(t)$ throughout: a strict gap at an interior point would make $W$ constant on a short interval to its right. Thus two candidate boundary profiles with the same $G$ agree there. Their difference has an absolutely convergent Fourier series on a union of two frequency sets, still of count $O(T^{k'})$ for some $k'<1$. On every open interval one can isolate each prescribed frequency of this union by a compact smooth test. Specifically, take the genus-zero product vanishing at all other distinct frequencies (at $i\gamma$ in the bilateral Laplace variable) and multiply by a compact Gevrey transform centered at the target with vertical decay $\exp(-c|\tau|^r)$ for $k'<r<1$. The product grows at most $\exp(C(1+|z|)^{k'})$, and the [compact isolation proof](trace-single-column-nov18.md) gives a test of arbitrarily short support, translated into the interval, which is nonzero at the target and zero at all others. Pairing the vanishing difference with this test kills each Fourier coefficient in turn. Bohr coefficients of $f$ give $m_\rho/[\rho(1-\rho)]$ at frequency $\Im\rho$, recovering each boundary ordinate and its multiplicity. This is a uniqueness statement about the full asymptotic profile.
