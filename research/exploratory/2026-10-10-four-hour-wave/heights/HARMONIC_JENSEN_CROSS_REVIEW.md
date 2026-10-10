# Independent review of the harmonic-column companion count

Reviewer: `/root/height_mechanisms`, 2026-10-10 UTC.
Result: **ACCEPT HC3–HC9 at the explicitly imported complete-census and actual
xi-product/theta-source scope.** This is an analytic review, not a rerun of
FLINT's historical complete count.

Reviewed document:
`../xi/outer-ray/HARMONIC_COLUMN_TRANSPORT.md`, SHA-256
`e6bba10148bb10aa1cf290d3f8d865387bae68c73d658ce2655038c93caf9ab3`.
This receipt covers Sections 1–2 and dependencies needed for HC3–HC9. It does
not certify the later harmonic transport or its final column conclusion.

1. Each complete nonreal quartet is outside real part 8192 and inside
   imaginary width 1/2. Consequently its coefficient
   `2 Re(rho^(-2))` in the polynomial evaluated at `-it` is positive.
   Whole real pairs also have positive coefficients. Multiplicities and
   nested whole blocks preserve coefficientwise monotonicity, while local
   entire convergence gives convergence of each Taylor coefficient and
   derivative. Thus both `f_n<=f` and `f_n'<=f'` hold on the positive axis.
2. The actual positive theta density gives
   `u sinh(tu)<=cosh((t+1)u)` for `t,u>=0`, since
   `sinh(tu)<=exp(tu)/2` and `u<=exp(u)`. It therefore gives
   `f'(t)<=f(t+1)`. The same nonnegative coefficient signs imply the modulus
   bounds for both `P_n` and `P_n'`, hence the factor 11 is correct uniformly
   for every real `1<=lambda<=10`.
3. The Jensen base is the actual `E_n(0)=F(0)>1/4`. On radius `2t`, the
   comparison value is `f(2t+1)=xi(2t+3/2)`. The reviewed native real-axis
   growth inequality `xi(s)<=2 s^(s/2+1)` therefore gives exactly
   `log88+(t+7/4)log(2t+3/2)`. Closed inner-disk zeros contribute at least
   `log2`, with all analytic multiplicities; exceptional outer radii are
   safely handled by an outer limit.
4. For `t>=1024`, the exact normalized upper coefficient is
   `21/20480+(4103/4096)(49/40)=201215/163840<4/3`.
   Since `log2>2/3`, the complete companion count is strictly less than
   `2t logt`, uniformly in the polynomial index and lambda.

The complete census is essential to the quartet sign condition. The proof
does not infer this condition from 8,049 sign-change brackets alone, and the
review does not promote a polynomial companion count to a limiting companion
zero census without the separate limiting argument.
