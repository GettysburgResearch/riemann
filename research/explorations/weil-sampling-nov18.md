# A fixed finite arithmetic matrix for a prescribed zeta search region

**Status.** Proposed analytic consequence of the [cluster projector and tilted theta window](weil-contour-nov18.md). The bounds are asymptotic with absolute, unevaluated constants. This gives one prescribed subspace for an entire search region. The arithmetic matrix requires a separate positivity proof or certificate.

## The basis and the implication

Fix $U\ge100$ and $0<d<1/2$. Write
$$
 H=\log U\,(1+\log(1/d)),\qquad \eta=\min(1/4,(H/U)^{1/3}),\qquad
 S=U/(2\pi)+C(U^{1/3}H^{2/3}+H),\qquad L=\tfrac12\log S.
$$
Fix sufficiently large absolute constants $C,C'>0$ as specified by the estimates below. Choose once and for all a real smooth function on the line which equals one on $(-\infty,0]$ and zero on $[1,\infty)$. Its rescaling gives an even cutoff $\chi$ equal to one on $|x|\le L-2/S$ and zero on $|x|\ge L-1/S$. The cutoff is fixed by $U,d$. Take the functions
$$
 g_k(x)=\chi(x)e^{-ik\pi x/L},\qquad
 -C'(\eta U+H)\le k\pi/L\le U+C'H/\eta,\qquad k\in\mathbb Z.
$$
Let $A_{jk}=W(g_k,g_j)$, where $W$ is the sesquilinear polarization of the arithmetic Weil form in the preceding note, linear in its first argument. Its explicit formula needs only the archimedean and pole terms and the prime powers $n< e^{2L}=S$, since all the test autocorrelations vanish outside $(-2L,2L)$.

**Theorem.** If $A$ is positive semidefinite, every zeta zero of ordinate in $[100,U]$ has distance less than $d$ from the critical line. For families with $H=o(U)$ the matrix dimension and the number $N(U)$ of positive ordinates through $U$, with multiplicity, satisfy
$$
 \dim A=(1+o(1))\,{U\log U\over2\pi}=(1+o(1))\,N(U).
$$
The largest prime-power cutoff is $S=(1+o(1))U/(2\pi)$ in this regime. The conclusion allows off-line zeros at distances below the chosen resolution. It gives a one-way certificate.

## Sampling proof

Suppose a defect at $T\in[100,U]$ has displacement $\delta\ge d$. Construct $f_\infty$ from the two disjoint circles as in the preceding note, using $\theta=\pi/4-\eta$ chosen from the prescribed inputs. Its values at all zeros are the exact opposite signs on the two clusters and zero elsewhere. The contours depend on the defect; the trial space above does not.

We record two uniform decay estimates. For all $j\le2$ and large $|x|$ with $\sin(2\eta)e^{2|x|}\ge1$, the physical tail satisfies
$$
 |f_\infty^{(j)}(x)|\ll \exp(\eta U+C_0H+C_1|x|-\pi\sin(2\eta)e^{2|x|}).
$$
This is the shifted theta tail from the preceding proof, since $T\le U$ and $\log T(1+\log(1/\delta))\le H$. At $|x|=L-O(1/S)$ the exponent can be made smaller than $-M\log(1+S)$ for any prescribed absolute $M$ by increasing $C$. The decrease beyond this point also bounds the integrals of the tails. All constants in the rest of the proof are independent of the particular defect.

In frequency, whenever real $t$ has distance at least one from both disks, the contour representation gives
$$
 |\widehat f_\infty(t)|\ll (2+|t|)^{C_2}
 \begin{cases}
 \exp(\eta U+C_0H-\eta t),&t\ge0,\\
 \exp(\eta U+C_0H-(\pi/2-\eta)|t|),&t<0 .
 \end{cases}
$$
Indeed the constant term in $(F_\theta(t)/F_\theta(v)-1)/(t-v)$ integrates to zero outside each disk. Bound the remaining factor by the reciprocal contour estimate times $|F_\theta(t)|$. Stirling and polynomial growth of zeta give $|\Xi(t)|\ll(2+|t|)^{C_2}e^{-\pi|t|/4}$, and $F_\theta(t)=e^{\theta t}\Xi(t)$. This calculation on the actual source keeps both tails.

Form its $2L$-periodization $p(x)=\sum_{\ell\in\mathbb Z}f_\infty(x+2\ell L)$. Absolute convergence with derivatives follows from the physical tail. The Fourier series coefficients for the convention $e^{-ik\pi x/L}$ are $(2L)^{-1}\widehat f_\infty(k\pi/L)$ by integration over one period. On $[-L,L]$, all copies with $\ell\ne0$ have arguments of absolute value at least $L$. Their sum and first two derivatives are $O_M((1+S)^{-M})$ by the physical tail: the $|\ell|=1$ terms satisfy this bound individually, and subsequent copies have the additional decay from the exponential in $e^{2|x+2\ell L|}$.

Truncate this Fourier series to the prescribed frequency interval, obtaining $p_0$. Its omitted tails and first two derivatives are again $O_M((1+S)^{-M})$, by choosing $C'$ large after fixing $C,M$. For details, write $B_+=U+C'H/\eta$ and $B_-=C'(\eta U+H)$. The first positive omitted node pays the exponential $\exp(-(C'-C_0)H)$. The negative nodes pay at least $\exp(-((\pi/2-\eta)C'-1)(\eta U+H)+C_0H)$. Both sets lie outside the unit neighborhoods of the disks. Summing a fixed polynomial in $|k|\pi/L$ times the remaining geometric tails costs only powers of $2+B_++B_-+L+\eta^{-1}$. Its logarithm is $O(\log(2+C')+\log(2+C)+H)$, since $\eta^{-1}\ll U^{1/3}$ and $\log(1+H)\ll H$. This absorbs fixed differentiation orders and both summation prefactors.

Put $g=\chi p_0$, a vector in the prescribed matrix's trial space. On the support of $\chi$ its difference from $\chi f_\infty$ and its first two derivatives are $O(S^2(1+S)^{-M})$; the two powers account for derivatives of $\chi$. Their weighted $L^1$ norms with weight $e^{|x|/2}$ are $O(LS^{1/4+2}(1+S)^{-M})$. The error from $\chi f_\infty-f_\infty$ is arbitrarily small in the same weighted norms by the physical tail. Choosing constants as above makes the full error vector of evaluations at the zeros have $\ell^2$ norm at most $1/4$, by two integrations by parts and the Riemann–von Mangoldt count. The sign calculation in the cluster theorem yields $W(g)<0$. This proves the contrapositive. The dimension estimate follows from lattice spacing $\pi/L$ and $\eta U+H+H/\eta=o(U)$ when $H=o(U)$.

**What remains.** A positive finite matrix would certify the specified region. No positivity statement about these matrices, either individually or at growing heights, is proved here. The asymptotic construction has no implementation or certified numerical constants.
