# Unconditional cancellation in the far tail of the Möbius sawtooth sum

Set \(B(x)=\{x\}-1/2\), with values at the jumps immaterial, and
\[
 S_N(u)=\sum_{n\le N}\mu(n)B(u/n).
\]
For fixed \(0<\epsilon<1/2\), uniformly for \(N^{1+\epsilon}\le V\le N^{2-\epsilon}\),
\[
 \int_V^{2V}|S_N(u)|^2du\ll_\epsilon N^3(\log N)^{-1/100}.       \tag{1}
\]
In particular, for every fixed \(r<1/200\),
\[
 \int_{N^{3/2}/(\log N)^r}^{\infty}|S_N(u)|^2\frac{du}{u^2}
           \ll_r (\log N)^{2r-1/100}+N^{-1/2}=o(1).              \tag{2}
\]
This is an estimate of the actual signed arithmetic sum. For arbitrary bounded coefficients, the far tail beginning at a fixed multiple of \(N^{3/2}\) can instead remain bounded away from zero.

## Frequency decomposition and the general bound

For \(|a_n|\le1\), the Fourier coefficient of \(\sum_{n\le N}a_nB(u/n)\) at reduced frequency \(j/q\), with \(q\ge1\), \(j\ne0\) and \((j,q)=1\), is
\[
 c_{j/q}= -\frac{1}{2\pi i j}\sum_{k\le N/q}\frac{a_{qk}}{k}.
\]
All denominators divide \(\operatorname{lcm}(1,\dots,N)\), so the ordinary periodic Fourier expansion converges in local \(L^2\). Distinct reduced frequencies have spacing at least \(N^{-2}\). The resulting large sieve gives, for any subset of the frequencies,
\[
 \int_V^{2V}\left|\sum c_\lambda e^{2\pi i\lambda u}\right|^2du
            \ll (V+N^2)\sum |c_\lambda|^2.                       \tag{3}
\]
Indeed majorize the integration by a smooth bump, nonnegative and at least one on the interval, whose rescaling to unit length is fixed. Its rapidly decreasing transform has absolute Gram row sums \(O(V+N^2)\). Pass from finite sums to the periodic \(L^2\) limit. The Fourier coefficient energy is \(O(N)\) by \(\sum_{q\le N}(1+\log(N/q))^2\ll N\). Restriction to \(|j|>A\) or \(q<N/B_0\) costs
\[
 O\left(\frac{N}{A}+\frac{N(1+\log B_0)^2}{B_0}\right)
\]
for \(2\le A,B_0\le N\). Take \(A=B_0=\lceil(\log N)^2\rceil\).

## Mean square for one numerator

On the retained part insert \(a_{qk}=\mu(q)\mu(k)1_{(q,k)=1}\). For \(m=|j|k\le AB_0\) put \(f_m(q)=\mu(q)1_{(q,m)=1}\), a real 1-bounded multiplicative function. For \(N/B_0\ll Q\le N\) and \(h\) in any fixed polynomial range \(Q^\eta\le h\le Q^{1-\eta}\),
\[
 \sum_{Q\le x\le 2Q}\left|\sum_{x<n\le x+h}f_m(n)\right|^2
                   \ll_\eta Q h^2(\log N)^{-1/100}.              \tag{4}
\]
To see uniformity of the long mean, write \(f_m=\mu*b_m\) with \(b_m\) the indicator of integers all of whose prime factors divide \(m\). Up to \(d=\sqrt Q\) use the ordinary Möbius estimate with any logarithmic saving and \(\sum b_m(d)/d\le\prod_{p\mid m}(1-1/p)^{-1}\le m\). For larger \(d\), \(\sum_{d>\sqrt Q}b_m(d)/d\le Q^{-1/4}\prod_{p\mid m}(1-1/\sqrt p)^{-1}\le Q^{-1/4}4^{\omega(m)}\). Thus the long mean on every such dyadic shell costs any inverse power of \(\log N\). For the short mean apply Matomäki–Radziwiłł's uniform Theorem 1 with their explicit choice \(\delta=(\log h)^{-1/200}\). Outside proportion \(O((\log h)^{-1/100})\) the difference of short and long means is \(O((\log h)^{-1/200})\); square there and use boundedness on the exceptional set. [Matomäki and Radziwiłł, Theorem 1 and the example following it](https://arxiv.org/abs/1501.04585)

For any subinterval \(I\subset[Q,2Q]\) in the retained range, take \(H=Q^2/(|j|V)\). We have \(Q^{\epsilon/2}\ll H\ll Q^{1-\epsilon/2}\) for large \(N\), since \(|j|,B_0\) are polylogarithmic. With \(e(v)=e^{2\pi i v}\), we claim
\[
 \int_V^{2V}\left|\sum_{q\in I} f_m(q)e(ju/q)\right|^2du
       \ll_\epsilon VQH(\log N)^{-1/100}.                        \tag{5}
\]
After majorizing by a smooth integration weight as in (3), its Gram kernel divided by \(V\) is \(K(Vj(1/q-1/q'))\) for a fixed Schwartz function \(K\). Partition the integers in \(I\) in successive blocks of length \(\ell=\lfloor H(\log N)^{-1/100}\rfloor\), apart from the two partial edge blocks. Replacing the arguments \(q,q'\) in the kernel by their block centers has absolute total cost
\[
 \ll (\ell/H)\sum_{q,q'\in I}(1+|q-q'|/H)^{-2}
 \ll (\ell/H)QH.
\]
This follows by the mean value theorem for \(K\); shifting either index by \(\ell\) shifts the argument by \(O(\ell/H)\). The kernel on block centers has absolute row sums \(O(H/\ell)\). By averaging the origin of the grid over the \(\ell\) integer shifts and using (4), choose a grid for which the sum of the squared whole-block sums is \(O(Q\ell(\log N)^{-1/100})\). A block starting at the first endpoint costs at most \(O(\ell^2)\), as do the two partial blocks. Applying the row-sum bound gives (5), including the outer factor \(V\).

Take square roots in (5) and sum over the dyadic \(Q\ll N/k\), using subintervals to enforce both ends of each original cutoff. Minkowski's inequality and \(\sum Q^{3/2}\ll(N/k)^{3/2}\) give total norm at most
\[
 C_\epsilon N^{3/2}(\log N)^{-1/200}
             \sum_{j\ge1}j^{-3/2}\sum_{k\ge1} k^{-5/2}.
\]
The tails of the Fourier series removed above satisfy a stronger logarithmic saving by (3). This proves (1). To get (2), sum (1) on dyadic intervals from the stated lower bound up to \(N^{7/4}\), using, for example, \(\epsilon=1/5\) and stopping at the nearest dyadic boundary. Beyond that use (3) with the full energy \(O(N)\), giving \(O(N/N^{7/4}+N^3/N^{7/2})\).

## Where a general-coefficient argument fails

Take \(U=cN^{3/2}\) with fixed \(c>0\), and \(a_n=e(-U/n)\) on \(N/2<n\le N\), zero elsewhere. The fractional parts of \(U/n\) on that range are equidistributed as \(N\to\infty\): for every fixed nonzero integral \(k\) the monotone derivative of \(kU/x\) has magnitude comparable to \(N^{-1/2}\) and stays that far from every integer, so the first derivative exponential-sum test costs \(O_{k,c}(\sqrt N)\). At \(u=U\) the average of \(e(-U/n) B(U/n)\) consequently tends to the first Fourier coefficient \(-1/(2\pi i)\). At \(u=U+v\), \(0\le v\le c_0N\), the average changes by at most \(O(c_0)+o(1)\). Away from a proportion \(O(c_0)+o(1)\) of original fractional parts at distance \(\le2c_0\) from a jump this follows from the unit slope of \(B\). Choose a small fixed \(c_0>0\). The squared tail integral then costs at least a fixed positive multiple of \(N^3/U^2\). At least one of the real and imaginary coefficient arrays also has positive limiting lower bound along a subsequence.

For a square-integrable Nyman residual with the constant and linear terms removed, let \(D_2f(u)=f(u/2)\) and \(P=(1-D_2)(1-2D_2)\). For \(u<N\) the elementary identity \(\sum_{n\le N}\mu(n)\lfloor u/n\rfloor=1_{u\ge1}\) gives exactly \(P(S_N+1_{u\ge1})(u)=0\). For \(u>4\) the target \(P1_{u\ge1}\) vanishes. The same bound (2) applies to the filtered far tail by dilating the integral a fixed number of times. The interval from \(N\) to the onset in (2) remains uncontrolled. A proof of smallness of this particular sharply cut off approximant across the remaining interval would require separate justification even under RH.

## A stretched-exponential gain for the ordinary Möbius coefficients

There is an absolute \(c>0\) such that
\[
 \int_{N^{3/2}\exp(-c(\log N)^{1/6})}^{\infty}
      |S_N(u)|^2\frac{du}{u^2}
       \ll \exp(-c(\log N)^{1/6}).                              \tag{6}
\]
Decreasing \(c\) only strengthens the stated combination of bounds. For fixed small \(\epsilon>0\), (1) improves to \(O_\epsilon(N^3\exp(-c_\epsilon(\log N)^{1/6}))\) for \(N^{1+\epsilon}\le V\le N^{11/6-\epsilon}\). The input is the unconditional estimate in Ramachandra–Sankaranarayanan–Srinivas, Theorem 1(12):
\[
 \frac1Q\int_Q^{2Q}\left|\sum_{x<n\le x+H}\mu(n)\right|^2dx
 \ll H^2 e^{-(\log Q)^{1/6}}+Q^{1/3+O(1/\log\log Q)}
 \qquad(1\le H\le Q).
\]
Changing the endpoint convention in the displayed integral has no effect. [Published theorem](https://doi.org/10.4064/aa-73-4-367-371)

Here are the uniformity details for the extra coprimality factors. Write \(E=(\log N)^{1/6}\) and take \(A=B_0=\lceil e^{aE}\rceil\) with a sufficiently small fixed \(a>0\). For \(Q\gg N/B_0\), \(m\le AB_0\), and \(Q^{1/6+\eta}\le h\le Q^{1-\eta}\), the normalized \(L^2\) norm of the length-\(h\) sum of \(f_m\) is \(\ll_\eta h e^{-bE}\) for an absolute \(b>0\) (for large enough \(N\) depending on \(\eta\)). In the convolution \(f_m=\mu*b_m\) split at \(d=Q^{\eta/4}\). For smaller \(d\) use Minkowski, applying the published theorem at \(Q/d,h/d\) after the change of variable \(x\mapsto x/d\). The second term is power-smaller than \((h/d)^2\). The first costs \((h/d)e^{-b_1 E}\) in normalized \(L^2\), for instance with \(b_1=1/4\) for fixed \(0<\eta<1/3\). Summing \(b_m(d)/d\le\prod_{p\mid m}(1-1/p)^{-1}\le m\) costs at most \(O(e^{2aE})\). In this sentence the sum is over \(d\), with weights \(b_m(d)/d\).

For \(d>Q^{\eta/4}\) use the pointwise bound \(h/d+1\), with \(d\le3Q\). For a fixed \(0<\theta<1/6\), put \(C_\theta=\prod_{p\mid m}(1-p^{-\theta})^{-1}\le m^{O_\theta(1)}\). The tail of \(\sum b_m(d)/d\) is at most \(C_\theta Q^{-(1-\theta)\eta/4}\), and \(\sum_{d\le3Q}b_m(d)\le C_\theta(3Q)^\theta\). Both terms cost a power saving relative to \(h\). For an integer block length the continuous mean-square estimate transfers to the integer grid since the short sum is constant between integer starting points (up to null endpoints). In (5), choose \(\ell=\lfloor H e^{-aE}\rfloor\), which stays above \(Q^{1/6+\epsilon/3}\) on the stated \(V\)-range for all sufficiently large \(N\). The block replacement, the mean-square input and the discarded frequency energy now each gain \(e^{-c_\epsilon E}\). The convergent sums over \(j,k\) are unchanged. Dyadic summation through the \(N^{7/4}\) boundary with, say, \(\epsilon=1/20\) proves (6).
