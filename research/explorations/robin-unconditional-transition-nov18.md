# An unconditional transition in the number of near-Robin integers

Fix $\kappa>0$. Write $x=\log N$, $L=\log x$, and let $C_\kappa(N)$ count $N\le n\le2N$ such that
$$
 B(n)=\log\frac{\sigma(n)}{e^{\gamma_E}n\log\log n}\ge
 -\frac{\kappa}{(\log\log n)^3}.
$$
Then the following **proposed asymptotic** uses only the classical quantitative prime number theorem:
$$
 \lim_{N\to\infty}\frac{L^2}{x}\log C_\kappa(N)
 =\begin{cases}
 \pi\sqrt{2\kappa/3}, &0<\kappa\le\pi^2/6,\\
 \kappa+\pi^2/6,&\kappa\ge\pi^2/6.
 \end{cases}
 \tag{1}
$$
The same holds if $2N$ is replaced by $N(1+e^{-d(x)})$ for any nonnegative $d(x)=o(x/L^2)$. No zero location or density hypothesis is made. The local factor contributions near $p=x$ give the square-root branch. A further prime of log size comparable to $x/L^2$ accounts for the linear branch. This range of tolerances is larger than the square-root tolerance in the [zero-abscissa criterion](robin-census-constant-nov18.md).

## Upper bound

For the one or two unit bins $v\le \log n<v+1$ in the requested interval, it suffices to prove the estimate at $x=v$ (the normalization changes by $1+o(1)$). Use the exact tangent deficit $D_x$ and single-prime toggle weights $w_p$ of the [partition argument](robin-census-constant-nov18.md). The quantitative prime number theorem implies $K(x)=O_A(L^{-A})$ for every fixed $A>0$ by direct integration. Thus (2) there gives $D_x(n)\le(\kappa+o(1))/L^3$. Here put
$$
 h=x/L,\qquad S=x/L^2,\qquad \lambda=txL,\qquad s=1/(xL)
$$
for any fixed $t>1$. For $p\le x$, exponents $j\ge1$ cost at least $(j-1)s\log p$. For $p>x$, after the first exponent each additional exponent costs at least $(1-1/x)s\log p$ because $p^{-2}\le s\log p/x$. Consequently
$$
 \sum_n e^{-\lambda D_x(n)}
 \le\zeta(t(1-1/x))\prod_p(1+e^{-\lambda w_p}).
$$
The zeta factor is bounded for sufficiently large $x$. The local prime measures on either side of $x$ at scale $h$ converge after division by $S$ to Lebesgue measure. This follows from the ordinary prime number theorem with error $O_A(x/L^A)$ and partial summation. Per fixed compact interval in $u=|p-x|/h$, the weights satisfy $\lambda w_p=tu+o(1)$. In $[x/2,2x]$ each shell of length $h$ has $O(S)$ primes and $w_p\gg (|p-x|-2)/x^2$, so the contribution at $u>M$ here is $O_t(Se^{-c_tM})$.

For $p<x/2$ use $w_p\ge1/x$. For $2x<p\le A x$ with $A>2$ fixed, $w_p\ge(s/2)\log p$, making the log product $o(S)$. For $p>Ax$, $w_p\ge (1-1/A)s\log p$; choose $A$ so $t(1-1/A)>1$ and sum this tail over all integers. These estimates give the limit $\pi^2/(6t)$ for $S^{-1}\sum_p\log(1+e^{-\lambda w_p})$ as in the preceding partition argument. Thus the upper constant is $\inf_{t>1}(t\kappa+\pi^2/(6t))$, exactly the right side of (1).

## Lower bound in the prescribed interval

Start at $m=\operatorname{lcm}(1,\ldots,\lfloor x\rfloor)$. Its [explicit arithmetic identity](robin-lcm-nov18.md) and the quantitative prime number theorem give $B(m)\ge-O_A(L^{-A})$ for each fixed $A$, and $\log m=x+O_A(x/L^A)$. At fixed $M,t>0$ toggle primes $|p-x|\le Mh$ in both directions as in the [short-interval construction](robin-census-constant-nov18.md). For lower bounds on $B$ the loss of a toggle is $(h/x^2)(u_p+o(1))$, using the tangent at $\log m$ and $hS/x^2=1/L^3$. The replacement of its slope by $s$ costs $o(L^{-3})$ in total by the bound on $\log m-x$. In the Bernoulli law with basic toggling probabilities $(1+e^{tu_p})^{-1}$ the normalized mean cost and entropy are
$$
 b_M(t)=2\int_0^M\frac{u}{1+e^{tu}}\,du,\qquad
 H_M(t)=2\int_0^M\log(1+e^{-tu})\,du + t b_M(t).
$$
A chemical tilt of size $o(1)$, with opposing signs on the two sides, can prescribe any mean log equal to $x-o(h)$, since the derivative of the mean is $\asymp_{M,t}h$. It leaves both limits unchanged. The variance of the log is $O_M(S L^2)$, and the energy and negative log probability concentrate in the units $S$ as in the linked proof.

Fix $q>0$ such that $q+b_M(t)<\kappa$. Prescribe the mean log $x-qS$. All but a vanishing fraction of the probability is on configurations $n'$ with $\log n'=x-(q+o(1))S$, energy at most $(b_M(t)+o(1))/L^3$, and negative log probability $(H_M(t)+o(1))S$. Here $qS=o(h)$ and $\sqrt S L=o(S)$. For each such $n'$ choose any prime
$$
 N/n'\le P\le (N/n')(1+e^{-d(x)}).
$$
There are $\exp((q+o(1))S)$ choices uniformly: the target $z=N/n'$ has $\log z=(q+o(1))S$, hence this interval contains $[z,z+z^{1-\epsilon}]$ for each fixed $\epsilon>0$ and all sufficiently large $x$. The prime number theorem in short intervals applies for $1-\epsilon>7/12$. Taking $\epsilon\downarrow0$ gives the stated log count. For the dyadic interval ordinary PNT alone suffices. All primes in $n'$ are at most $x+Mh$ whereas $P$ exceeds that bound, so outputs $P n'$ are distinct across all configurations and primes. Their log abundancy cannot decrease on multiplication, and the extra denominator cost is $(q+o(1))/L^3$ by the mean value theorem. Therefore all outputs satisfy the specified near equality.

The lower constant is at least $H_M(t)+q$. Let $M\to\infty$; the limits are $b(t)=\pi^2/(6t^2)$ and $H(t)=\pi^2/(3t)$. For $\kappa>\pi^2/6$ take $t=1$ and $q\uparrow\kappa-\pi^2/6$. For $0<\kappa\le\pi^2/6$ take $t>\pi/\sqrt{6\kappa}$, choose positive $q<\kappa-b(t)$, then take $t\downarrow\pi/\sqrt{6\kappa}$. This attains (1) including the endpoint.

## Other logarithmic tolerances and the limiting-density comparison

For $A>1$, replace the tolerance by $(\log\log n)^{-A}$ on $[N,2N]$ and write the count as $C_A^*(N)$. The two outer regimes give
$$
 \log C_A^*(N)\sim\begin{cases}
 xL^{1-A},&1<A<3,\\
 \pi\sqrt{2/3}\,xL^{-(A+1)/2},&A>3.
 \end{cases}
 \tag{2}
$$
For $1<A<3$, the preceding upper bound with fixed $t>1$ is $t xL^{1-A}+O_t(x/L^2)$; send $t\downarrow1$. For a lower bound choose $D=q xL^{1-A}$ with $0<q<1$, start with the LCM at $x-D$, and multiply by any prime that places the result in $[N,2N]$. Its log is $(1+o(1))D$ by the quantitative PNT, so it costs $(q+o(1))L^{-A}$ in the denominator and provides $\exp((q+o(1))xL^{1-A})$ choices. The original LCM ratio is $\ge-o(L^{-A})$. Send $q\uparrow1$. This also works in the thin interval for $d=o(xL^{1-A})$.

For $A>3$ take $h=x L^{(1-A)/2}$, $S=h/L$, $\lambda=tx^2/h$. Now $\lambda s=t L^{(A-3)/2}\to\infty$ for every fixed $t>0$. All prime intervals and starting LCM estimates needed in the [two-sided toggle proof](robin-census-constant-nov18.md) follow unconditionally from quantitative PNT with arbitrarily high fixed log saving. The small deficit $K(x)=o(L^{-A})$ and $\lambda L^{-A}=tS$ again give the unrestricted minimum at $t=\pi/\sqrt6$. The same lower tilt and rounding argument works throughout $d=o(xL^{1-A})$, since $\sqrt S L=o(xL^{1-A})$ and $xL^{1-A}=o(S)$.

Weingartner's limiting-density expansion gives $\log A(t)=-\exp(t e^{-\gamma_E})(1-(\pi^2/6)e^{2\gamma_E}/t^2+O(t^{-3}))$, where $A(t)$ is the limit at each fixed threshold $t$ as the counting endpoint goes to infinity. Substituting the moving threshold $t=e^{\gamma_E}L\exp(-\kappa/L^3)$ into that expression gives $\log(NA(t))=(\kappa+\pi^2/6+o(1))x/L^2$. Formula (1) agrees with this prediction when $\kappa\ge\pi^2/6$. Below that value the predicted coefficient exceeds the finite-interval coefficient by $(\sqrt\kappa-\pi/\sqrt6)^2$. The new proof works with integer divisibility at the moving endpoint directly. [Weingartner, Theorem 1](https://arxiv.org/abs/1011.4262)
