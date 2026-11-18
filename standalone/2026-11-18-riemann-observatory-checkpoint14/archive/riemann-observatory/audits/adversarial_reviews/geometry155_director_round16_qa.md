# Independent QA of the Round 16 signed Mellin and Gonek notes

2026-11-18. Both director notes pass the requested scope and normalization checks. I made no edits to them. [Signed Mellin note](director_signed_mellin_round16.md) · [Gonek constants note](director_gonek_constants_round16.md)

## Signed Mellin result

- The sharp-versus-Gaussian comparison uses a uniformly bounded difference-kernel norm and the uniform inner-line weighted tails from disk estimates. The resulting convergence of the inverse is uniform in the physical point for each admitted test. It does not assert a uniform point-evaluation operator bound from critical \(H^{1/2}\) alone.
- The right-edge Dirichlet series has absolutely summable weights for \(a>1\). Its two inverse kernels evaluate \(n^af(n)\) and \(n^{a-1}f(1/n)\), giving the printed negative prime term and the reflection factor \(1/n\). In passing to the compact smooth approximation, the note correctly uses the uniform original physical value envelope for the prime sum and pole terms, rather than inferring continuity of those terms in the critical norm. The scope of the norm-plus-local-\(H^1\) functional continuity claim is the \(Q\)-integral.
- The symmetric \(p\ge0\) result stays distinct from one-sided signed convergence for \(p>1\) via Selberg. The right-edge Gamma contribution is handled separately on its two axes, including the constant imaginary sign term; this does not establish one-sided convergence of the zero sum. The all-height comparison uses \(O(\log T)\) local zero counts and \(O(N_0/\sqrt T)\) point bounds, so it includes every exact endpoint atom.
- The literal author's condition (A) gives finite one-sided limits of both \(f\) and \(f'\), and midpoint values. The critical Gagliardo seminorm excludes nonzero value jumps without absolute Fourier inversion. Continuity and bounded one-sided derivatives then yield local \(H^1\). The compact cusp is clearly outside (A), with a genuinely divergent compensated local term. The earlier smooth \(p=3\) absolute witness is inside the signed theorem. The earlier smooth raw-height witness under (A)(B) alone remains valid. No author-error finding is added by the cusp. [Independent contour and cusp proof](geometry154_critical_contour_and_cusp_adjudication.md)

## Gonek finite constants and endpoint atoms

I inspected Gonek's actual printed pp. 134–135, PDF pp. 12–13, especially the definition in Lemma 8 and the minus sign on its expanded convolution. For two positive orders, the proof's centered discrepancy \(E(t)=\lfloor t\rfloor-t+1/2\) obeys \(|E|\le1/2\). For smooth \(g\) the exact inclusive formula is
\[
 \sum_{1\le d\le z}g(d)-\int_1^z g(t)\,dt
 =E(z)g(z)+\tfrac12 g(1)-\int_1^z E(t)g'(t)\,dt.
\]
Here \(E(z)\) is evaluated on its right-continuous branch, including when \(z\) is an integer. Both boundary values vanish for two positive orders, and the half-variation of the unimodal kernel is its maximum. The stated \(B L^M\) bounds that maximum after dropping the factor \(1/t\). The inner discrepancy follows by comparing the monotone sum with its integral and retaining at most one last term. The factor \(e^{-1}\) is the exact maximum of \(\log q/q\). Interchanging the two divisor variables legitimizes the minimum of the inner orders.

With one zero order, orient the outer factor as \((\log d)^m\) and open the inner count as \(\lfloor z/d\rfloor\). The error against \(z\sum_{d\le z}g(d)\) is at most \(zL^m\), with \(g(t)=\log^m(t)/t\). The kernel has \(g(1)=0\) and \(g(z)=L^m/z\), generally nonzero. If \(g_*\) is its maximum, the exact centered identity bounds the discrepancy by \(\tfrac12 g(z)+\tfrac12(2g_*-g(z))=g_*\le L^m\). The nonzero upper term is thus retained and the displayed constant 2 follows after restoring the outside factor \(z\). This covers the case where the maximum occurs at the upper endpoint. For both orders zero, \(zH_{\lfloor z\rfloor}-\lfloor z\rfloor\le\sum\lfloor z/d\rfloor\le zH_{\lfloor z\rfloor}\), and \(\log z\le H_{\lfloor z\rfloor}\le 1+\log z\), so the stated error is at most \(z\). These estimates also cover \(1<z<2\).

The \(B_n(\delta)\) signs are exact. The source uses \(\zeta^{(\mu)}(s)\zeta^{(\nu)}(s)(\zeta'/\zeta)(s-i\delta)\), so at \((1,1)\) the two negative logarithms cancel and the remaining factor is \(-\Lambda(k)k^{i\delta}\). Grouping by \(k\) thus gives \(-\sum_{k\le x}\Lambda(k)k^{i\delta}C_{1,1}(x/k)\), with main term \(-(x/6)A_3(x,\delta)\). At \(k=x\) the original \(C_{1,1}(1)\), the main power and the error bound all vanish. The positive-power Abel boundary also vanishes at \(x\); there is no discretization loss from including \(n=x\).

For the final numerical constants,
\[
 (9/4)(L^3/3+21L^2+40L)+(24L^3+60L^2)/6
 =(19/4)L^3+(229/4)L^2+90L .
\]
The two Abel coefficients follow from the director's scoped input \(\int r(u)\,du/u<20\) and \(1+10\sqrt5<24\), with \(\delta=0\) for the positive Λ-weighted square and real \(|\delta|\le1/2\) for the cubic difference. No numerical bounds for the later contour or weighted tail are implied. [Pinned Gonek scan](../../sources/classical63_lfunctions/gonek1984.pdf#page=12) · [Scoped Abel bounds](director_explicit_abel_round15.md)
