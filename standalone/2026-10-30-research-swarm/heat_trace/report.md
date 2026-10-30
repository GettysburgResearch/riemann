# A growing derivative hierarchy for the actual xi heat trace

Status: proposed analytic theorem with a complete argument below; independent review pending.  
Scope: alternating derivatives of the zero heat trace, uniform in time and in an explicitly growing derivative order. This is not complete monotonicity of all orders and does not prove RH or a new individual zero-free half-plane.  
Sources: the classical zero symmetries/strip and the explicit counting and finite-verification inputs stated below; compare Sra v2, Lemma 2.2, Proposition B.1, and Corollary C.4.  
What was run: symbolic derivation and elementary constant checks; no high derivative of xi was numerically evaluated.  
Smallest remaining gap toward RH: positivity for arbitrarily high orders at times bounded away from zero remains open.

## 1. The object and the claim

For every upper-half-plane nontrivial zeta zero write

$$\rho=\tfrac12+\delta_\rho+i\gamma_\rho,\qquad
\lambda_\rho=(\gamma_\rho-i\delta_\rho)^2,$$

retaining multiplicities. Define

$$H(t)=\sum_{\gamma_\rho>0}e^{-t\lambda_\rho},\qquad
H_n(t)=(-1)^nH^{(n)}(t)=\sum_{\gamma_\rho>0}\lambda_\rho^n e^{-t\lambda_\rho}.$$

The sums and their fixed derivatives converge locally absolutely for $t>0$. Functional-equation symmetry makes them real. They are the actual zero heat trace used by Sra and Polson, not the ordinary theta Fourier kernel or a sum restricted to known on-line zeros.

Use these source inputs:

1. $|\delta_\rho|<1/2$.
2. With $N(Y)$ counting upper-half-plane zeros, including multiplicities, and
   $M(Y)=Y(\log(Y/(2\pi))-1)/(2\pi)$, $M(0)=0$,

   $$|N(Y)-M(Y)|\le\tfrac18\log(Y+2)+4\quad(Y\ge0).$$

3. Every zero with $0<\gamma\le U$ is on the critical line.

The counting bound implies $N(Y)\le Y\log Y$ for $Y\ge100$ and
$\sum_{\gamma>U}\gamma^{-2}\le2(\log U+1)/U<1$ for $U\ge100$.
It also supplies an ordinate $\eta\in(U/4,U/3]$ for $U\ge1000$; this is exactly the elementary counting consequence used in Sra's Corollary C.4. In particular, the retained zero is real in the xi coordinate when input 3 holds. Put $q=\eta^2$.

**Theorem.** Under these inputs, if $U\ge10^6$, then

$$H_n(t)>0\quad\text{for every }t>0\text{ and every integer }
0\le n\le \left\lfloor\frac{U^2}{8\cdot10^6}\right\rfloor.$$

At the published verified height $U=3\cdot10^{12}$, the range ends at

$$1,125,000,000,000,000,000.$$

This large finite number is an analytic consequence of the inputs, not the number of tests performed. It supplies necessary derivative signs, not the Hankel-minor inequalities or all-order assertion equivalent to RH. No novelty or priority claim is made for the heat-trace representation or complete-monotonicity criterion. The proposed contribution is the explicit uniform growing-order estimate and proof.

The mechanism has two regimes. At small time the kernel samples a broad ordinate interval and the counting law forces enough positive mass. At larger time a retained verified real zero dominates the unverified tail for the stated range of derivative orders.

## 2. A low-order retained-zero estimate

First suppose $0\le n\le2U/5$, $U\ge1000$. Write

$$a=\gamma^2-\delta^2,\quad b=2\gamma\delta,\quad
r=\gamma^2+\delta^2,\quad\phi=2\arctan(\delta/\gamma).$$

The real part of a tail summand is

$$r^n e^{-at}\cos(bt-n\phi).$$

The numbers $b$ and $\phi$ have the same sign. Thus the summand is nonnegative if both $|b|t$ and $n|\phi|$ are at most $\pi/2$. Here $n|\phi|\le n/\gamma\le2/5$. A negative contribution requires $t>\pi/(2\gamma)$.

Since $q\le U^2/9$ and $\gamma>U\ge1000$,

$$a-q\ge\tfrac78\gamma^2,\qquad
\frac r q\le\frac{16(\gamma^2+1/4)}{U^2}.$$

At a time when its sign is negative, the summand divided by the retained positive term $q^ne^{-qt}$ has absolute value at most

$$\left(\frac r q\right)^n e^{-7\pi\gamma/16}.$$

The function $\gamma^2(16(\gamma^2+1/4)/U^2)^n e^{-7\pi\gamma/16}$ decreases for $\gamma\ge U$: its logarithmic derivative is at most $2(n+1)/\gamma-7\pi/16<0$.
Using the reciprocal-square tail sum, the total relative negative part is at most

$$U^2(16+4/U^2)^n e^{-7\pi U/16}
\le U^2e^{-9U/80}<1.$$

For the last inequality use $\log(16+4/U^2)<3$, $n\le2U/5$, and $\pi>3$; the final expression decreases for $U\ge1000$ and is below one at 1000. All other verified terms are nonnegative. Therefore $H_n(t)>0$ for all $t>0$ in this low-order range. In particular it covers $n<400$.

## 3. All high derivative orders at small time

This part uses only inputs 1 and 2. We prove

$$H_n(t)\ge\frac{\log X}{320\sqrt t}
\left(\frac{n}{et}\right)^n>0,
\quad n\ge400,\quad0<t\le10^{-6},\quad X=\sqrt{n/t}.$$

Set $L=t^{-1/2}\ge1000$, $y=\gamma\sqrt t$, $u=\delta\sqrt t$, and $v=\sqrt{y^2+u^2}$. Then $|u|\le1/2000$. The summand equals $t^{-n}(y-iu)^{2n}e^{-(y-iu)^2}$, whose phase is

$$\psi=2yu-2n\arctan(u/y).$$

### 3.1 A broad interval has positive phase

When $|y-\sqrt n|\le10$, we have $y\ge\sqrt n/2\ge10$. Using $|z-\arctan z|\le|z|^3/3$,

$$|\psi|\le 6|u|\,|y-\sqrt n|+
\frac{2n|u|^3}{3y^3}<\tfrac12.$$

Hence the real part is at least half its modulus on this entire interval. In particular, put $P_n=n^ne^{-n}$. On the central interval $|y-\sqrt n|\le1/2$,

$$y^{2n}e^{-y^2}\ge e^{-3/4}P_n,$$

by $\log(1+z)\ge z-z^2$ for $|z|\le1/2$. The complex modulus is no smaller than this real-axis value. Every central zero therefore contributes at least $t^{-n}P_n/8$.

### 3.2 Count the central zeros

The central ordinate interval is $[A,B]=[X-L/2,X+L/2]$, where $X\ge20L\ge20000$. Endpoint conventions can be taken half-open; the estimates count multiplicity and require no zero-free endpoints.

Since $A\ge39X/40$, $A/(2\pi)>X/7$ and $X>49$,

$$M(B)-M(A)\ge\frac{L}{4\pi}\log X>\frac{L}{13}\log X.$$

The two counting errors total at most $\tfrac14\log(2X)+8<2\log X$. Consequently

$$N(B)-N(A)\ge\left(\frac L{13}-2\right)\log X
\ge\frac L{20}\log X.$$

The positive central mass is at least $t^{-n}P_nL\log X/160$.

### 3.3 Bound all possible negative mass

For every $v>0$, $v^{2n}e^{-v^2}\le P_ne^{-(v-\sqrt n)^2}$, by $\log z\le z-1$. Therefore

$$|(y-iu)^{2n}e^{-(y-iu)^2}|
\le e^{2u^2}P_ne^{-(v-\sqrt n)^2}.$$

For $k\le|y-\sqrt n|<k+1$, $k\ge10$, this is at most $2P_ne^{-(k-1)^2}$, because $|v-y|\le|u|<1$.

The counting bound implies that any positive-ordinate interval of length at most $L$ and upper endpoint $b$ contains at most $L\log(b+2)$ zeros when $L\ge1000$. Indeed its main-term difference is at most $(L/(2\pi))\log(b+2)$ and its errors at most $\tfrac14\log(b+2)+8$; use $\log(b+2)\ge\log2>1/2$.

The two parts of the $k$-th shell thus contain at most $2L(k+1)\log X$ zeros. All possible negative mass, including the complete infinite tail, is at most

$$4t^{-n}P_nL\log X
\sum_{k=10}^{\infty}(k+1)e^{-(k-1)^2}.$$

Since $(k-1)^2\ge k+71$ and $e>2$, the sum is at most $3/2^{78}$. Subtracting this quantity from the central lower bound leaves more than $t^{-n}P_nL\log X/320$. This proves the small-time estimate, uniformly for all integers $n\ge400$.

## 4. The verified height controls the remaining times

Let $t_0=10^{-6}$, $t\ge t_0$, and $n\le t_0U^2/8$. Retain the real zero at $\eta\in(U/4,U/3]$. For $\gamma>U$ put $x=(\gamma/U)^2\ge1$. Then $r/q\le17x$ and

$$\log(17x)\le3x,$$

using $\log17<3$ and $\log x\le x-1$. Thus every tail term, regardless of its phase, satisfies

$$\frac{r^ne^{-at}}{q^ne^{-qt}}
\le\exp\left(3n\frac{\gamma^2}{U^2}-\frac78\gamma^2t\right)
\le e^{-t_0\gamma^2/2}.$$

For $U\ge10^6$, the function $\gamma^2e^{-t_0\gamma^2/2}$ decreases for $\gamma\ge U$. The reciprocal-square tail bound gives

$$\sum_{\gamma>U}e^{-t_0\gamma^2/2}
\le U^2e^{-t_0U^2/2}<1.$$

Hence

$$H_n(t)\ge\bigl(1-U^2e^{-U^2/(2\cdot10^6)}\bigr)q^ne^{-qt}>0.$$

Sections 2–4 cover every $t>0$ and every claimed $n$, proving the theorem.

## 5. What this contributes and what it leaves open

Sra's retained-zero proof treats $H$ and $-H'$, and its asymptotic result treats each fixed derivative as $t\downarrow0$. The estimate above makes the small-time range uniform in derivative order and then connects it to an explicit quadratic-in-height finite hierarchy. It is a quantitative extension of that representation, not an unrelated new characterization of RH.

The new calculation also identifies the difficult scale: for derivative order $n$, the unshifted kernel peaks at ordinate $\sqrt{n/t}$ with width comparable to $t^{-1/2}$. Fixed small time averages many zeros and forces positivity from the counting law. The unresolved regime combines arbitrarily high derivative order with larger times, where the spectral interval can be narrow. An argument that only improves broad averaging cannot automatically cover that regime.

No passage from this very long finite hierarchy to all orders is justified. No all-order Hankel positivity, Thorin positivity, or new zero-free strip follows from the theorem as stated.

## Sources and attribution

- Suvrit Sra, *On some positivity properties of the Riemann Xi function*, author-site v2, 29 October 2026. [Primary PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf); [author repository](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi/v2/riem-xi-v2.pdf), inspected PDF Git blob `f98e0bd0d2d1353245a482581ffa74580c644996`. The inputs above are its (2.1)–(2.3); the retained ordinate is its Corollary C.4. Its proof attributes the counting input to Bellotti–Wong (2025) and the height verification to Platt–Trudgian (2021).
- The heat-trace/probability connection has prior work by Nicholas G. Polson, discussed explicitly in Sra's §§2 and 5. This packet claims no priority for that connection or the all-order RH criterion.
- Existing repo overlap: `PROGRAMMES.md` §3 and §4, `OPEN_CUTS.md` §3 and §4, and the latest source-qualified literature pass in PR #1024. This estimate concerns the actual zero heat trace, rather than the repo's physical Weil resolvent or a high-derivative descent theorem.
