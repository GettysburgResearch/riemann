# Two-scale tightness on deterministic grids

18 November 2026. Let \(p>1\), \(a=1+\alpha>1\), \(b=1+\beta>1\), and \(C<\infty\). For each row \(n\), let \(X_n(t_i)\) be real random variables on an arbitrary finite deterministic grid \(0=t_0<t_1<\cdots<t_m=1\), with \(X_n(0)\) tight. A uniformly bounded larger clock is equivalent by deterministic rescaling or constant extension. Suppose all pairs of grid nodes at distance \(h>0\) satisfy
\[
 E|X_n(t_j)-X_n(t_i)|^p\le C\min\{h^a+\epsilon_n,\ A_nh^b\},
 \qquad A_n\ge1,\quad 0<\epsilon_n\le1,\quad\epsilon_n\to0.                \tag{1}
\]
Define \(w_n=(\epsilon_n/A_n)^{1/b}\), \(\lambda_n=\epsilon_n/w_n=(A_n\epsilon_n^\beta)^{1/b}\), and put \(a'=\min(a,p)\), \(b'=\min(b,p)\). Let \(Z_n\) be the polygonal interpolation. For any deterministic \(0<\delta\le1\),
\[
 \|\omega(Z_n,\delta)\|_{L^p}
 \le C_1\left[
 \delta^{(a'-1)/p}+
 \lambda_n^{1/p}
 \min\{1,(\delta/w_n)^{(b'-1)/p}\}
 \right],                                                         \tag{2}
\]
where \(\omega\) is the uniform modulus and \(C_1\) depends only on \(C,a,b,p\). In particular \(\lambda_n\to0\) suffices for tightness of the interpolations in the uniform topology. If the maximum mesh tends to zero, or the maximum adjacent step increment tends to zero in probability, the right-continuous step processes have the same continuous limits in \(D,J_1\). No lower bound on grid spacing is required. Given convergence of finite-dimensional laws to those of a continuous process, this proves the functional limit. The condition \(\lambda_n\to0\) is sharp for a general guarantee from (1) alone, in the sense of the counterexample below.

## Exponent available by direct optimization

For \(1<q\le\min(a,b)\), the sharp bound on the scalar envelope in (1) is
\[
 \sup_{0<h\le1}\frac{\min(h^a+\epsilon_n,A_nh^b)}{h^q}
 \asymp 1+A_n^{q/b}\epsilon_n^{1-q/b}.                              \tag{3}
\]
The constants depend only on the exponents. At \(h=w_n\) the minimum is exactly \(\epsilon_n\), so the second term is necessary. At \(h=1\) it is at least 1. For \(h\le w_n\) use \(A_nh^b\), and for \(h\ge w_n\) use \(h^a+\epsilon_n\). This bounds the ratio by \(1+\epsilon_n/w_n^q\). Hence a uniform \(h^q\) estimate in this range is available exactly when \(\sup_n A_n^{q/b}\epsilon_n^{1-q/b}<\infty\).

If \(\sup_n A_n<\infty\), the maximal direct grid exponent is \(b\), even when \(b>a\). If \(A_n\) is unbounded, \(q\le \min(a,b)\) is necessary for a uniform direct envelope bound. An exponent \(q>b\) fails by \(h\downarrow0\) at any row with \(\epsilon_n>0\). In the remaining potential case \(b>a\) and \(a<q\le b\), along \(A_n\to\infty\) evaluate at \(h=A_n^{-1/(b-a)}\). There \(A_nh^b=h^a\), hence the bound would need a constant at least \(A_n^{(q-a)/(b-a)}\). If a uniform grid exponent \(q>1\) is available, direct polygonal interpolation preserves \(\min(q,p)\), which is the best possible general cap for a nonconstant linear cell. Formula (2) permits tightness even when no fixed \(q>1\) is available from (3).

For example, with \(a=b=2\), \(A_n=L_n^2\), \(\epsilon_n=L_n^{-M}\), and \(L_n\to\infty\), the sharp grid exponent from (3) is \(2M/(M+2)\). The universal tightness threshold is \(M>2\). If the first estimate is available with any fixed logarithmic saving \(M\), one obtains any fixed exponent \(2-\eta\), \(0<\eta<1\), by taking \(M\ge2(2-\eta)/\eta\). This recovers the two bounds used for the derivative-weighted shrinking prime band. [Application](uniform81_shrinking_band_process.md)

## Proof of the modulus estimate

Abbreviate \(w=w_n\) and \(\epsilon=\epsilon_n\). On the continuous interpolation, all increments at distance \(h\le1\) have
\[
 E|Z_n(t)-Z_n(s)|^p
 \ll h^{a'}+\epsilon\min\{1,(h/w)^{b'}\}.                            \tag{4}
\]
For full grid-node increments with \(h\ge w\) use the first estimate in (1), and for \(h\le w\) use \(A_nh^b=\epsilon(h/w)^b\le\epsilon(h/w)^{b'}\). For a fractional increment of length \(h\) inside one cell of total length \(d\ge h\), multiply the full-cell moment by \((h/d)^p\). If \(h\ge w\), the coarse bound gives \((h/d)^p(d^a+\epsilon)\le h^{a'}+\epsilon\). If \(h<w\) and \(d\ge w\), it gives
\[
 (h/d)^p(d^a+\epsilon)\le h^{a'}+\epsilon(h/w)^p
                      \le h^{a'}+\epsilon(h/w)^{b'} .
\]
Here \(d\le1\) and \(d\ge h\) control the exponent \(a-p\) with either sign. If \(h\le d<w\), use \((h/d)^p\epsilon(d/w)^b\le \epsilon(h/w)^{b'}\), again valid with either sign of \(b-p\). A general interval splits into at most three pieces, two fractional cells and one full grid interval. The inequality \(|\sum_{\ell=1}^3 x_\ell|^p\le3^{p-1}\sum_\ell|x_\ell|^p\) and monotonicity of the right side of (4) give (4) for the whole interval. This is why just the grid condition suffices even for very small times inside a large cell.

Let \(M_j\) be the maximum absolute increment of \(Z_n\) over adjacent dyadic nodes at level \(j\). Since the maximum of nonnegative \(p\)-th powers is at most their sum, (4) gives
\[
 \|M_j\|_{L^p}\ll
      2^{-(a'-1)j/p}
     +\left[\epsilon\,2^j\min\{1,(2^{-j}/w)^{b'}\}\right]^{1/p}.
\]
Deterministic chaining for continuous functions bounds the modulus at scale \(2^{-k}\) by a fixed multiple of \(\sum_{j\ge k}M_j\): approximate each endpoint by its left dyadic approximants and join the level-\(k\) approximants by at most two adjacent increments. Take \(L^p\) norms by Minkowski and sum each geometric series. The second series increases geometrically up to \(2^{-j}\asymp w\) and decreases geometrically after that scale. If \(2^{-k}\ge w\), its bound is \(O((\epsilon/w)^{1/p})\). If \(2^{-k}<w\), its bound is \(O((\epsilon/w)^{1/p}(2^{-k}/w)^{(b'-1)/p})\). An enclosing dyadic scale disposes of arbitrary \(\delta\). This proves (2) with a row-independent constant. If \(\epsilon_n=0\) in some rows, simply use the coarse power bound for those rows and omit the second term.

By Markov, the \(p\)-th power of the right side of (2) divided by \(\eta^p\) bounds the probability of modulus above a tolerance \(\eta>0\). With \(\lambda_n\to0\) this gives the uniform diagonal tightness criterion, together with tightness at zero. If constants and parameter moduli are effective, it gives a computable modulus-in-probability after a computable row onset. The step function \(X_n^{\rm step}\) differs uniformly from \(Z_n\) by at most the maximum adjacent increment, which is at most \(\omega(Z_n,\text{mesh}_n)\); the \(J_1\) distance is bounded by the uniform distance. For a fixed tolerance and a continuous proposed limit, one can compare bounded-Lipschitz path tests through polygonal interpolations on a fixed finite mesh. The error comes from (2), the proposed limit's own modulus estimate, and effective finite-dimensional comparison on that mesh. This is conditional on an effective finite-dimensional law estimate, which does not follow from (1) itself. If the original statistic is embedded by deterministic time changes, uniform convergence of the clocks plus (2) gives the same conclusion after composition with the limit clock.

## Sharp obstruction at the crossover

Suppose \(\lambda_n\not\to0\). Pass to a subsequence with \(\lambda_n\ge c>0\). Then \(w_n\le\epsilon_n/c\to0\). Set \(m_n=\lfloor1/w_n\rfloor\) and take the equally spaced grid \(j/m_n,\ 0\le j\le m_n\), of pitch \(d_n=1/m_n\asymp w_n\), with \(d_n\ge w_n\). Fix a random index \(J_n\) uniform on \(1,\ldots,m_n-1\). At that point let \(X_n(J_n/m_n)=v\), and take \(X_n=0\) at every other grid point, with constant \(v>0\). For any distinct grid pair its \(p\)-th increment moment is at most
\[
 \frac{2v^p}{m_n-1}\ll v^p w_n\le (v^p/c)\epsilon_n .
\]
Every pair distance is at least \(w_n\), so \(h^a+\epsilon_n\ge\epsilon_n\) and \(A_nh^b\ge\epsilon_n\). Thus (1) holds uniformly, even with any prescribed positive \(C\) by choosing \(v\) sufficiently small. At fixed finitely many deterministic times the interpolation and step evaluations tend in probability to zero, since each time can encounter the spike with probability \(O(w_n)\). Their sup norms nonetheless equal \(v\) almost surely. Polygonal paths retain \(v\)-sized oscillations on intervals of length \(d_n\to0\). The steps are also not \(J_1\)-tight: any tight subsequence would have a limit whose finite-dimensional distributions vanish on a dense deterministic set of its almost-sure continuity times and at the right endpoint, forcing the zero path by right continuity. Endpoint evaluation is continuous in the J1 topology. The sup norm is continuous in \(J_1\), contradicting the constant value \(v\). This constructs a worst-case counterexample, rather than a necessary condition on the behavior of a particular process whose bounds may have slack.

With only the bound \(C(h^a+\epsilon_n)\) and \(\epsilon_n>0\), the very same example with \(d_n\asymp \epsilon_n\) satisfies that bound and fails tightness, however fast the deterministic error tends to zero. A lower grid spacing, an a priori bound on jumps, or other structure could change such a problem. Under the two-scale hypotheses above, no such restriction is needed for the interpolated modulus.
