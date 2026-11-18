# Exact finite check and certified first-crossing integrals for rooted CUE

18 November 2026. This check concerns the cosine raw moment in the CUE law obtained by a global Haar/root-label derivative-square tilt. The finite calculations use rational arithmetic. The continuum calculations enclose the correction at two bands. [Moment window](prime84_cue_moment_window.md) · [Independent derivation](uniform86_cue_window_adjudication_input.md)

## Exact finite partial crossing

Set \(N=40,\ n=N+1=41,\ r=4,\ a=11/50,\ b=7/25\). The band \(\lfloor aN\rfloor<k\le\lfloor bN\rfloor\) consists of \(9,10,11\). The maximum three-term sum is \(33\). Of the \(3^4=81\) ordered four-term sums, 50 are strictly below \(n\), 16 equal \(n\), and 15 exceed \(n\). Equal totals are included in the formal window.

Write \(J=(1,\ldots,1)^{\mathsf T}\), \(L=(2i-n+1)_{0\le i<n}\), and \(P=I-JJ^{\mathsf T}/n-LL^{\mathsf T}/(L^{\mathsf T}L)\). In the Fourier mode basis the free-point generating determinant is
\[
\det\bigl[I+P(T(e^{tF})-I)P\bigr],
\qquad
F(z)=-\sum_{k=9}^{11}\frac{z^k+z^{-k}}{2k}.
\]
Here \(T\) forms the \(n\)-mode Toeplitz matrix with entries \([z^{i-j}]\). The full \(n\)-dimensional matrix inside the determinant acts by the identity on \(\ker P\). Compute coefficients through degree four using Laurent multiplication followed by exact rational matrix multiplication. The log derivative is \(\operatorname{tr}(M^{-1}M')\) for the matrix series \(M\), with the root contributing \(-t\sum 1/k\) to the log determinant. This direct evaluation uses the full projection determinant, independently of the two-dimensional complementary inverse and its signed path formula. The surrogate and the ordered crossing sum are evaluated separately.

| Quantity | Exact value |
|---|---:|
| Direct fourth moment | \(483952530159221/9042666599736000\) |
| Formal fourth moment | \(30253355007779/565166662483500\) |
| Direct minus formal | \(-3384187/302541624000\) |
| First-crossing prediction | \(-3384187/302541624000\) |

The zeroth through third raw moments agree exactly. The fourth-moment prediction is \(-1/8\) times the sum of \(A_n(k_1+\cdots+k_4)/(k_1k_2k_3k_4)\) over the 15 strictly crossing tuples, where \(A_n(m)=2(m-n)(m^2+nm-n^2+1)/(n(n^2-1))\). These are exact identities for this finite example.

## Full-cube integral

For \(ra\ge1\), the constraint \(\sum x_i>1\) omits at most a null set. Let \(H=\log(b/a)\) and \(m_j=(b^j-a^j)/j\). Expanding the first and third powers of \(s=\sum x_i\) under \(\prod dx_i/x_i\) gives, for \(r\ge3\),
\[
I_r=2H^r+(2r m_3-4r m_1)H^{r-1}
+6r(r-1)m_2m_1H^{r-2}
+2r(r-1)(r-2)m_1^3 H^{r-3}.
\]
The final term comes from three distinct coordinates and is omitted for \(r=2\). At \(a=13/50,\ b=8/25,\ r=4\), evaluating the expression by 160-bit Arb arithmetic gives the raw-moment correction enclosure
\[
-2^{1-r}I_r\ \in\
[-0.0001099788872477072953195452027468801467795283355\ \pm 6.05\times10^{-50}].
\]

## Partial-crossing integral

For \(a=11/50,\ b=7/25,\ r=4\), put \(y_i=b-x_i\) and \(d=b-a=3/50\). The crossing part is \(\sum y_i<L=rb-1=3/25=2d\), subject to \(0\le y_i\le d\). Remove four single-coordinate caps from this simplex. Distinct caps intersect only on a set of measure zero. For one cap, shift the coordinate with \(y_i>d\) down by \(d\). The resulting simplex has radius \(L-d\), its first denominator parameter is \(a\), and the others are \(b\).

In each simplex the integrand has the shape
\[
A(u-S)\prod_{i=1}^r(c_i-y_i)^{-1},\qquad
S=\sum y_i,\quad u=1+L',\quad 0\le S<L',
\]
where \(L'\) is \(L\) or \(L-d\), and \(A(v)=2(v-1)(v^2+v-1)\). Expand each reciprocal as a geometric series through degree \(M=64\). The truncated product has exact rational integrals by the radial Dirichlet identity
\[
\int_{\sum y_i<L'} y^\alpha S^j\,dy=
\frac{\prod_i \alpha_i!}{(|\alpha|+r-1)!}
\frac{(L')^{|\alpha|+r+j}}{|\alpha|+r+j}.
\]
With \(q=\max_i(L'/c_i)<1\), the geometric-product remainder lies between zero and \((\prod c_i^{-1})\,r q^{M+1}/(1-q)^r\) pointwise. On the simplex \(0\le A(u-S)\le A(u)\), by \(A'(v)=6v^2-4>0\) for \(v\ge1\). Multiplying by \(A(u)\) and the simplex volume gives a one-sided rational error bound. The full simplex and the cap errors enter with opposite signs. Applying \(-1/8\) to the resulting rational interval and enclosing it in Arb gives
\[
-2^{1-4} I_4\ \in\
[-1.116093794622113479066\times10^{-5}\ \pm 1.87\times10^{-27}].
\]
The exact rational enclosure has width less than \(2.63\times10^{-27}\).

The analytic CUE moment window is \(rb\le1\), with the first-crossing formula used here when \((r-1)b\le1<rb\). The arithmetic result under RH applies on the separate range \(rb<1/2\). The certificates here concern CUE.

The script uses python-flint 0.9.0. Replay from the repository root with `PYTHONPATH=/workspace/riemann-runtime python scripts/prime89_first_chamber_certificate.py`. [Script](../../scripts/prime89_first_chamber_certificate.py) · [Recorded output](../../experiments/results/prime89_first_chamber_certificate.txt)
