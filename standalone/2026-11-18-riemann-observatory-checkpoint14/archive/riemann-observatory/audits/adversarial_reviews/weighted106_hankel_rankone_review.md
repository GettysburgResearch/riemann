# Independent check of the rank-one Hankel threshold

I checked the new rank-one section of the finite Hankel witness note. The exact criterion, singular equality case and least-degree asymptotic all hold. Here \(L\) is the witness polynomial degree or Hankel order. The matrix has size \(L+1\) and uses raw moments through degree \(2L\). [Rank-one argument](geometry102_finite_hankel_bound.md)

With \(d=b-a>0\), \(H=\log(b/a)\), and \(\sigma^2=H/2\), the formal rank-one generating function is \(e^{\sigma^2 z^2/2}(1-dz)\). For \(X\sim N(0,\sigma^2)\), differentiating the Gaussian MGF gives
\[
 \mathbb E[(1-dX/\sigma^2)e^{zX}]
 =e^{\sigma^2 z^2/2}(1-dz).
\]
This is an identity of entire functions and hence of all moment coefficients. The signed density relative to Gaussian measure is positive for \(x<\sigma^2/d\), zero at \(\sigma^2/d\), and negative above it. Its total mass is one.

In the normalized probabilists' Hermite basis \(h_k(x)=\operatorname{He}_k(x/\sigma)/\sqrt{k!}\), multiplication by \(x\) sends \(h_k\) to \(\sigma\sqrt{k+1}h_{k+1}+\sigma\sqrt{k}h_{k-1}\). Its compression to \(0\le k\le L\) is the symmetric tridiagonal \(T_L\) with edge \(k-1,k\) of weight \(\sigma\sqrt k\). The quadratic form for the signed moments is \(I-(d/\sigma^2)T_L\) in this basis and is congruent to the Hankel matrix in monomials. The determinant recurrence gives \(\det(xI-T_L)=\sigma^{L+1}\operatorname{He}_{L+1}(x/\sigma)\). Thus the form is positive semidefinite exactly when the largest zero of \(\operatorname{He}_{L+1}\) is at most \(\sigma/d\). At equality every eigenvalue of the form is nonnegative, and a nonzero vector is in its kernel. Only a strict crossing gives a negative quadratic form.

For an equality fixture within the stated band family, take \(b=\sqrt{2\log 2/3}\) and \(a=b/2\), which gives \(\sigma/d=\sqrt3\). At \(L=2\) the polynomial \(\operatorname{He}_3(u)=u^3-3u\) has largest zero exactly \(\sqrt3\), giving a singular positive semidefinite form. At \(L=3\), \(\operatorname{He}_4(u)=u^4-6u^2+3\) has largest zero \(\sqrt{3+\sqrt6}>\sqrt3\), so a negative direction appears. The \(L=0,1\) forms are positive definite, making \(L=3\) the least witness degree in this example.

For the leading asymptotic, each of the two weighted shifts in \(T_L\) has norm at most \(\sigma\sqrt L\), giving the upper bound \(2\sigma\sqrt L\). The two highest-index adjacent basis vectors give the elementary lower bound \(\sigma\sqrt L\). For a sharper lower bound take the last \(q=\lfloor\sqrt L\rfloor\) vertices, where \(q\ge2\) for large \(L\). All internal weights are at least \(\sigma\sqrt{L-q+1}\). The first sine vector of the \(q\)-vertex constant-weight path has positive coordinates. Comparing its weighted edge contributions term by term gives
\[
 \frac{\lambda_{\max}(T_L)}{\sigma}
 \ge 2\sqrt{L-q+1}\cos\!\left(\frac{\pi}{q+1}\right)
 =2\sqrt L-O(1).
\]
This proves the required limit without an orthogonal-polynomial zero asymptotic. Put \(u=\sigma/d\). A negative direction requires \(L>u^2/4\), and \(L=\lceil (u+C)^2/4\rceil\) suffices for one fixed \(C>0\) large enough and all large \(u\), by the strict criterion and the lower bound. Therefore the least degree \(L_*=u^2/4+O(u)\), in particular \(L_*\sim\sigma^2/(4d^2)\). The draft's separate coarse upper bound \(\lfloor u^2\rfloor+1\) follows from the two-vertex test.

In the family \(a=b/2\) as \(b\downarrow0\), this gives \(L_*=(\log 2)/(2b^2)+O(1/b)\). The first difference between the actual raw moments and the formal series is at \(r=\lfloor 1/b\rfloor+1\), including when \(1/b\) is integral. Its rank-one sign is positive for actual minus extrapolated by the fixed-rank first-crossing calculation. A raw moment comparison at this scale does not give a negative Hankel quadratic form. In fact the exact criterion makes all forms with \(L=O(1/b)\) positive definite for sufficiently narrow bands. The asymptotic concerns the formal rank-one sequence and implies no arithmetic moment extension. No canonical record was changed. [Raw crossing and parity](geometry93_rank_three_barrier.md)
