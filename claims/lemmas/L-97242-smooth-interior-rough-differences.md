# L-97242 - Every smooth-interior rough difference is nonnegative

Claim ID: `L-97242`  
Status: **PROVED EXACT CALCULUS THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Put
\[
\phi(u)=u e^{u/2}\mathbf1_{u\ge0}.
\]
For every integer `r>=1` and `u>0`,
\[
\boxed{
\phi^{(r)}(u)=e^{u/2}\left(\frac{u}{2^r}+\frac{r}{2^{r-1}}\right)>0.
}
\tag{L-97242.1}
\]
Let `a_i>=0` and assume `u>=a_1+...+a_r`. Then repeated use of the fundamental
theorem of calculus gives
\[
\boxed{
\prod_{i=1}^r(I-T_{a_i})\phi(u)
=\int_0^{a_1}\!\cdots\!\int_0^{a_r}
\phi^{(r)}(u-v_1-\cdots-v_r)\,dv_1\cdots dv_r\ge0.
}
\tag{L-97242.2}
\]
Thus every rough history whose entire translation cube stays inside one active
row cell contributes nonnegatively. Any possible negative contribution is
supported on histories crossing at least one activation boundary.
