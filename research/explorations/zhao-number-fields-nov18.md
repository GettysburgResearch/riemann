# The quadratic fields in Zhao's spectral criterion, and a degree bound

Assume GRH for the Dedekind zeta function of a number field $K$. Write $B_K=\sum_\gamma(1/4+\gamma^2)^{-1}$, over all nontrivial zeros $1/2+i\gamma$ with multiplicity. Zhao's §8(3) asks for a classification in connection with an integrated prime-ideal Mertens inequality. The strict spectral condition $B_K<2$ in that question holds for exactly **168 quadratic fields**, 116 real and 52 imaginary. Their fundamental discriminants range from $-479$ through $1201$. The [complete list](zhao-quadratic-fields-nov18.json) and [reproducible certificate](../../scripts/check_zhao_quadratic_fields_nov18.py) enumerate the condition. Among fields of any degree, $B_K<2$ implies $[K:\mathbb Q]\le8$. The sign question for fields violating the strict spectral condition requires further information about the zeros. [Zhao, §8](https://doi.org/10.1007/s40993-025-00640-y)

## Conductor bound and enumeration

For $K=\mathbb Q(\sqrt d)$ take the signed fundamental discriminant $d$, $q=|d|$, and $a=\mathbf1_{d<0}$. Factorization gives $B_K=B_\zeta+B_\chi$, where $B_\zeta=2+\gamma_E-\log(4\pi)$ and $\chi=(d/\cdot)$. Write $T=2-B_\zeta$. The Hadamard logarithmic derivative and functional equation give
$$
 B_\chi=\log(q/\pi)+\psi((1+a)/2)+2L'(1,\chi)/L(1,\chi).
$$
For $s>1$ the same identities give
$$
 \frac12\log(q/\pi)+\frac12\psi((s+a)/2)+L'(s,\chi)/L(s,\chi)
   =(s-1/2)\sum_\gamma((s-1/2)^2+\gamma^2)^{-1}
   \le(s-1/2)B_\chi .
$$
Euler factors give $L'/L(s,\chi)\ge\zeta'/\zeta(s)$. Taking $s=7/4$ shows that $B_\chi\le T$ implies
$$
 q\le\pi\exp((2s-1)T-\psi((s+a)/2)-2\zeta'(s)/\zeta(s)).
$$
At 96-bit Arb precision the two right sides lie strictly between 5317 and 5318 for even $\chi$, and between 2597 and 2598 for odd $\chi$.

For an independent comparison with Zhao's character-only threshold $B_\chi<2$, the program reruns the conductor bound with $T=2$. The resulting upper endpoints are 5968.719 and 2914.936, rounded upward. It tests all 2,699 fundamental discriminants in these enlarged ranges. For a fast rigorous enclosure of the logarithmic derivative, compute the sums for $L(1)$ and $L'(1)$ out to $N=4q$ with binary fixed-point coefficients rounded down in magnitude at scale $2^{40}$. The absolute rounding error is at most $N/2^{40}$ in either sum. Let $B$ be the largest absolute prefix sum of $\chi$ in its complete period. Since $N$ is a conductor multiple, partial summation gives truncation errors at most $B/N$ and $B\log(N)/N$, respectively. Every classification uses strict inequality on interval endpoints. For the 49 cases whose first interval crossed either boundary, the program finds the unique primitive real Conrey character of the required modulus and parity, then evaluates the 96-bit interval Taylor series of its $L$-function at 1 through the linear term. Every tested field lies strictly to one side of the threshold. Run with python-flint 0.9.0 and FLINT 3.6.0.

This reproduces Zhao's stated total of 178 discriminants for the character-only condition, 125 positive and 53 negative. The online version of Table 2 goes directly from $520$ to $721$ and omits 12 positive discriminants from the displayed inventory. They are $553,561,569,577,601,604,609,641,649,673,681,697$. All 166 discriminants actually displayed in the two tables agree with the replay at the character-only threshold. Among the 12 omitted from the display, $569,604,641$ pass the character-only threshold and the other nine also pass the quadratic-field threshold. [Zhao, Table 2](https://link.springer.com/article/10.1007/s40993-025-00640-y/tables/2) · [Table 3](https://link.springer.com/article/10.1007/s40993-025-00640-y/tables/3)

## Fields of higher degree

Write $n=r_1+2r_2$ and $\Delta=|\operatorname{disc}K|$. Apply the completed logarithmic derivative for $s(s-1)\Lambda_K(s)$, and use $\zeta_K'/\zeta_K(s)\ge n\zeta'/\zeta(s)$ from the Euler factors. Just as above, $B_K\le2$ implies for every real $s>1$
$$
 \log\Delta\le A(s)+r_1u(s)+r_2v(s)
$$
where
$$
\begin{aligned}
 A&=4(s-1/2)-2/s-2/(s-1),\\
 u&=\log\pi-\psi(s/2)-2\zeta'(s)/\zeta(s),\\
 v&=2\log(2\pi)-2\psi(s)-4\zeta'(s)/\zeta(s).
\end{aligned}
$$
Minkowski's bound gives $\log\Delta\ge 2\log(n^n/n!)+2r_2\log(\pi/4)$. At $s=5$, $u<0.497$ and $v/2-\log(\pi/4)<0.629$, so the two bounds require
$$
 2\log(n^n/n!)\le 17.1+0.629n .
$$
At $n=16$ the left side exceeds $27.37$, while the right side is $27.164$. For $n\ge16$ the successive differences on the left are $2n\log(1+1/n)\ge 2(16/17)>0.629$. This excludes all degrees $n\ge16$. Every one of the remaining signatures has an explicit absolute discriminant cutoff from the displayed inequality. The ordinary Riemann zeta function is the unique degree-one case.

### A sharper degree bound from three derivatives

Let $D(s)$ denote the logarithmic derivative of $s(s-1)\Lambda_K(s)$. At $s=7/2$ put $\mathcal{T}D=D'-(3/2)D''+(16/6)D^{(3)}$. The Hadamard identity gives one contribution per zero at ordinate $t$,
$$
 h(t)=-\Re\left((3+it)^{-2}+3(3+it)^{-3}+16(3+it)^{-4}\right).
$$
It satisfies $h(t)\le (1/4+t^2)^{-1}$ for all real $t$. Indeed, the difference multiplied by $(x+1/4)(x+9)^4$, with $x=t^2$, is
$$
 x(63x^2-1856x+21735)/4 +14499/2>0
$$
by the discriminant of the displayed quadratic. Thus $B_K\ge\mathcal{T}D$.

The discriminant term disappears on differentiation. Every prime-ideal contribution to $\mathcal{T}(\zeta_K'/\zeta_K)$ is nonnegative by the absolutely convergent Euler series. Write $f(z)=z^{-2}+3z^{-3}+16z^{-4}$. The two rational poles contribute $-f(s)-f(s-1)$. Each complex place gives $\sum_{j\ge0} f(s+j)$ by the polygamma series. A real place gives at least half that amount: its derivatives involve the even shifts $s+2j$, while together the real gamma factors at $s$ and $s+1$ give the complex factor by duplication, and $f$ decreases. Consequently
$$
 B_K\ge \frac n2\sum_{j\ge0} f(s+j)- f(s)-f(s-1).
$$
For $n=9$ the right side exceeds 2.016, already by retaining the first eight terms and bounding the remainder below by $\int_{s+8}^\infty f(v)dv=1/(s+8)+3/(2(s+8)^2)+16/(3(s+8)^3)$. This is a rational calculation. The bound increases with $n$. Hence all candidates for the strict spectral criterion have degree at most **eight**.

A five-derivative test also restricts the signatures. Set $s=4$, $a=7/2$, and $b=(99/100,21/4,25,28,420)$. The zero test is $h(t)=-\sum_{k=1}^5 b_k\Re(a+it)^{-k-1}$. The [rational checker](../../scripts/check_zhao_signatures_nov18.py) shows $h(t)\le(1/4+t^2)^{-1}$ by clearing denominators. On each interval $[l,r]$ with successive endpoints $0,8,16,32,64,128,256,512$, it verifies the resulting polynomial at $x=(l+rt)/(1+t)$ has positive coefficients after multiplying by $(1+t)^6$. It also checks the shift $x=512+t$. Put $f(z)=\sum_{k=1}^5 b_k z^{-k-1}$. The completed logarithmic derivative then bounds $B_K$ below by
$$
 (r_1+r_2)\sum_{j\ge0}f(4+2j)+r_2\sum_{j\ge0}f(5+2j)-f(4)-f(3).
$$
Each Euler term is nonnegative. Using the first 64 terms and the integral lower bound for each tail gives more than $2.02$ for signatures $(5,1)$ and $(2,3)$. Replacing a complex place by two real places increases the bound since $f$ is decreasing. Thus a degree-eight field passing the spectral criterion is totally imaginary, and a passing degree-seven field has at most three real places.

## An unconditional finite predicate

Without GRH define $B_K^*=2D(1)$ using the completed logarithmic derivative above. The Hadamard product and its symmetry give
$$
 B_K^*=\sum_\rho \Re\left(\frac1\rho+\frac1{1-\rho}\right).
$$
The terms are positive and the series converges. A central real zero contributes 4 for each occurrence. Any distinct real pair $\beta,1-\beta$ contributes $2/[\beta(1-\beta)]\ge8$. Thus $B_K^*<2$ excludes a nontrivial real zero.

The conductor and degree arguments extend to this finite predicate without any assumption on nonreal zeros. For a zero test expressed as a real part of a meromorphic function of $z=\rho$, average it at $z$ and $1-\bar z$. This preserves the summed value and makes the two sides of the critical strip equivalent. The target $\Re(1/z+1/(1-z))$ is harmonic in the strip. It suffices to minorize it on $\Re z=0$, by the harmonic minimum principle. Indeed all rational functions decay uniformly to zero at imaginary infinity. On small interior semicircles about 0 and 1 the polar real part is nonnegative and the regular part is bounded below by its boundary limit minus $o(1)$.

For the basic logarithmic derivative bound at real $s>1$, the boundary surplus with $x=(\Im z)^2$ is
$$
 \frac{s-1/2}{1+x}-\frac12\left(\frac{s}{s^2+x}+\frac{s-1}{(s-1)^2+x}\right)
 =\frac{s(s-1)(2s-1)(s^2-s+x-1)}{2(s^2+x)(1+x)((s-1)^2+x)}\ge0
$$
whenever $s\ge(1+\sqrt5)/2$. This includes $s=7/4$ used in the quadratic enumeration. Applied to the completed Dirichlet function and to the pole-cancelled zeta function, it proves the exact unconditional classification of $B_K^*<2$ for quadratic fields by the same 168 entries. The $L$-jets used in that certificate were evaluated on the real line unconditionally.

For the derivative tests with weights $b_k$, the boundary surplus is
$$
 \frac1{1+x}+\frac12\sum_{a\in\{s,s-1\}}\sum_k b_k\Re(a+i\sqrt x)^{-k-1}.
$$
The [exact rational strip certificate](../../scripts/check_zhao_field_strip_nov18.py) clears denominators and counts nonnegative numerator roots by Sturm's theorem. It proves strict positivity for $s=7/2$, $b=(1,3,16)$ and for $s=4$, $b=(0.998,5.24,23.92,30.43,332.6)$, where all decimals are exact rationals. The first yields $B_K^*>2.0405$ for $n\ge9$. The second yields $B_K^*>2.0118$ for signature $(5,1)$ and $B_K^*>2.0562$ for $(2,3)$, with the same monotonicity under replacement of a complex place by two real places. Therefore the degree and signature restrictions above also hold for the unconditional predicate $B_K^*<2$.
