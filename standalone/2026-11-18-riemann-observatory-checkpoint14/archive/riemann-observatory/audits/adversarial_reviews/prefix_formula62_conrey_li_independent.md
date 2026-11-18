# Independent check of a Conrey–Li negative kernel

I checked arXiv:math/9812166v1 §2, both kernel-domain arguments, the zeta and odd-character witness reductions in §3, and the original local interval script and retained output. The replay below is scoped to the published counterexamples. It gives no obstruction to a different domain, different operator, or a different de Branges construction. [Primary preprint](../../sources/witness62_operator_frontier/conrey_li.pdf) · [Initial technical audit](witness62_conrey_li_deep.md)

## Entire-function kernel and shift domain

Write $E^\#(z)=\overline{E(\bar z)}$ and take the inner product linear in its first argument. For a zero $w$ of $E$, the Hermite–Biehler inequality gives upper-half-plane nonvanishing, while $E^\#(z)=\epsilon E(z-i)$ and the absence of real zeros imply $-1<\Im w<0$. In particular $E(w+i)$ and $E(w-i)$ are nonzero. The kernel simplifies to
$$
K_E(w,z)=-\frac{E^\#(z)E(\bar w)}{2\pi i(\bar w-z)}.
$$
At $w+i$ the second term in its kernel vanishes since $E(\bar w-i)=0$. Substituting $E^\#(z+i)=\epsilon E(z)$ gives the source equation (2.3) exactly:
$$
\overline{E(w+i)}\,K_E(w,z+i)=-\overline{E(w-i)}\,K_E(w+i,z).
$$
Hence $K_E(w,\cdot)$ belongs to the positive-$i$ shift domain, for which both it and its shifted function lie in $\mathcal H(E)$. The reproducing identity evaluates the real quadratic form directly as $\Re K_E(w,w+i)$. At $w+i=\bar w$, cancellation of the removable denominator gives
$$
\Re K_E(w,w+i)=\Re\frac{\overline{E'(w)}\,E(w+i)}{2\pi i}.
$$

Take $E(z)=X(1-iz)$ and a real critical-line zero parameter $\rho=1/2+it$, so $w=-t-i/2$. The two completions used by the source are real on the critical line by functional equation and real Dirichlet coefficients. In the $\chi_4$ case the sign of the real functional equation is $+1$, since the alternating positive decreasing series at $s=1/2$ has strictly positive sum. Differentiating the real-valued function $t\mapsto X(1/2+it)$ makes $X'(\rho)$ purely imaginary. With $E'(w)=-iX'(\rho)$ and $E(w+i)=X(\rho+1)$, the real form is
$$
-\frac1{2\pi}\Re[X'(\rho)X(\rho+1)].
$$
The original interval script brackets a root by evaluating the real critical-line function at exact rational endpoints with opposite strict signs. Analyticity implies continuity, so existence follows without root enumeration or a uniqueness assumption. A Taylor-series interval at the entire box encloses $X'$, and direct interval multiplication encloses the displayed real form for every point of the box. These are logically separate checks. Negative sign throughout a box does not alone certify a zero, and opposite endpoint signs do not alone fix the quadratic-form sign. Gamma factors with positive real bases use the real logarithm, and the Dirichlet completion uses the Hurwitz difference $4^{-s}[\zeta(s,1/4)-\zeta(s,3/4)]$ with its completed prefactor.

I reran the original python-flint 0.9.0, 256-bit script. Its full JSON output matched the retained result byte for byte, including the two root brackets, the derivative signs, and the boundary and interior ratios. [Original interval code](../../experiments/code/witness62_conrey_li_deep.py) · [Retained output](../../experiments/results/witness62_conrey_li_deep.json)

## Reciprocal-function kernel and independent witness

The space $\mathcal F(W)$ has inner product with weight $|W|^{-2}$ on the real axis and reproducing kernel $K_W(w,z)=W(z)\overline{W(w)}/(2\pi i(\bar w-z))$ at every $\Im w>0$. At a single such $w$, the defined shift sends $F=K_W(w,\cdot)$ to $TF=K_W(w+i,\cdot)$, another kernel in the space. Thus
$$
\Re\langle F,TF\rangle
=\frac{|W(w+i)|^2}{2\pi(2\Im w+1)}
  \Re\frac{W(w)}{W(w+i)}.
$$
This interior calculation needs no deduction of extension across the original boundary. The paper's boundary witness \(\Im w=0\) uses its theorem's extension consequence. Continuity also moves a strict boundary negative into the upper half-plane, and the test below directly locates one such interior point.

The extension step itself checks out at the level needed here. Under the assumed nonnegativity, the sum of the two mixed kernels is positive semidefinite. It is the shifted Hardy kernel on $\Im z>-1/2$ multiplied, after harmless nonzero factors, by $1-B(z)\overline{B(w)}$ for $B=(W-W(\cdot+i))/(W+W(\cdot+i))$. Its positivity makes the rule $L_w\mapsto \overline{B(w)}L_w$ contractive on the span of kernels in the original upper half-plane. This span is dense in the larger Hardy space by the identity theorem, so the rule is well-defined and extends. The adjoint is multiplication by $B$ on the original open subset and identifies its analytic continuation on the larger half-plane. Testing the corresponding adjoint identity at kernels gives $|B|\le1$ there. Its Cayley transform recovers the claimed nonnegative real part, with denominator nonvanishing by the maximum modulus principle unless trivially constant, a case also covered by the original quotient.

For the independent zeta replay, set $w=-282+i10^{-6}$ and $s=1-iw=1+10^{-6}+282i$. With $W(w)=1/X(s)$ the actual kernel ratio is $X(s+1)/X(s)$. The printed source uses its reciprocal. The real parts have the same sign because $\Re(1/q)=\Re(q)/|q|^2$. The code uses mpmath interval arithmetic at 75 decimal digits and no FLINT or special-function point evaluation for gamma or zeta. It computes
$$
\frac{X(s)}{X(s+1)}
=\frac{s-1}{s+1}\sqrt\pi\,
 \exp\{\log\Gamma(s/2)-\log\Gamma((s+1)/2)\}
 \frac{\zeta(s)}{\zeta(s+1)}.
$$
The log-gamma computation uses the branch analytic on the right half-plane and real on the positive real axis. The exponentiated difference is consequently the gamma quotient with the correct branch. Zeta is computed by Euler–Maclaurin from the first 511 terms, with $N=512$ and 12 Bernoulli corrections. The bounded periodic Bernoulli remainder on $\Re s>1$ has modulus at most
$$
\frac{|B_{2M}|}{(2M)!}|(s)_{2M}|
\frac{N^{1-\Re s-2M}}{\Re s+2M-1},\qquad M=12.
$$
The log-gamma Stirling expansion through $B_{2M}$ has remainder bounded by the absolute periodic Bernoulli integral. For $\Re z>0$, use $|z+t|\ge(|z|+t)/\sqrt2$ to bound it by
$$
\frac{2^M|B_{2M}|}{2M(2M-1)|z|^{2M-1}}.
$$
The two remainder bounds are added to both real and imaginary interval components before taking the quotients. The code confirms both zeta enclosures exclude zero. Positive real bases in the completion use the real logarithm. At this interior point, coarse outward intervals containing the program output are
$$
-0.000131763480808189 < \Re[X(s)/X(s+1)] < -0.000131763480808188,
$$
$$
-0.004750153564007396 < \Re[X(s+1)/X(s)] < -0.004750153564007395.
$$
They force a negative numerical range on the single kernel above. This is an independent numerical enclosure for one of the four source models, using rigorous analytic remainder formulas and a separate interval implementation. It does not revalidate the other three models in mpmath. [Independent script](../../experiments/code/prefix_formula62_conrey_li_independent.py) · [Independent output](../../experiments/results/prefix_formula62_conrey_li_independent.txt)
