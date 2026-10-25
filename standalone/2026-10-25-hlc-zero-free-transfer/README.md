# Hardy--Littlewood--Chowla mechanisms and the actual zero-free targets

Date: 25 October 2026.

**Status: exploratory research with complete finite identities and conditional
analytic implications. No new zero-free region or proof of RH is obtained.**
The source-qualified benchmark in the recent research branches remains
\(B_{\flat}=0.874886647039964\ldots\); this packet does not independently
certify the imported OpenAI/Liu framework.

This packet studies Guangshi Lü, Zhiwei Wang and Jie Wu,
*On the Hardy--Littlewood--Chowla conjecture*, arXiv:2610.20242v1,
against the actual coefficient and range requirements of PRs 1014, 1019,
1020 and 1021. The source claims cancellation of \(\mu(p+2)\) on primes.
Its determinant argument is relevant to signed arithmetic cancellation,
but its stated bounds do not directly improve a zero-free half-plane.

The objective here was to find a usable transfer, then try to close it.
Three concrete deductions survived the checks. Their missing analytic
inputs remain stated next to their conclusions.

## 1. A direct quantitative bridge for ordinary zeta

Let \(M(t)=\sum_{n\le t}\mu(n)\) and \(E(t)=\psi(t)-t\). Assume explicitly
that \(M(t)\ll_\epsilon t^{\beta_M+\epsilon}\) and
\(E(t)\ll_\epsilon t^{\beta_P+\epsilon}\).
For fixed smooth tests \(W,K\), with
\(\kappa=\int K\ne0\), set

\[
 S_H(X)=\sum_hK(h/H)\sum_n\mu(n)\Lambda(n-h)W(n/X).
\]

Two Stieltjes integrations give the exact main term and the bound

\[
 \frac{S_H(X)}{\kappa H}
 =\sum_n\mu(n)W(n/X)
 +O_\epsilon\!\left(
     \frac{X^{\beta_M+\beta_P+\epsilon}}H+
     \frac{X^{\beta_M+\beta_P+1+\epsilon}}{H^2}\right).
 \tag{1}
\]

For \(H=X^\theta\), a bound for the **full signed average**
\(S_H/H\ll_\epsilon X^{\alpha+\epsilon}\) consequently yields

\[
 \Re s>\max\{\alpha,\beta_M+\beta_P+1-2\theta\}
 \quad\Longrightarrow\quad \zeta(s)\ne0,                 \tag{2}
\]

provided the test family detects every zero. The proof supplies either
the compact family \(W_\tau(u)=W(u)u^{-i\tau}\), for every fixed
\(\tau\), or a single log-Gaussian test with a nowhere-zero Mellin
transform. No hidden assumption that an arbitrary smoothing cannot
cancel a reciprocal-zeta pole is used.

**A substantial conditional target:** grant both old summatory exponents
\(7/8+\epsilon\). At \(\theta=49/50\), the remainder exponent is
\(79/100\). Proving the full signed average with exponent \(4/5\)
would therefore establish the half-plane \(\Re s>4/5\).
A square-root version, if established independently of the current
exponent, would iterate through
\(7/8\to79/100\to31/50\to1/2\), giving RH.
These are conditional consequences, not achieved regions.

The attempted closure fails at a precise place: the centered average
\(S_H-\kappa HM_W\) is already controlled by (1); its control leaves
the unknown Möbius main term exposed. The new paper treats a fixed
shift and does not bound the required full, growing-shift average.

Read [the complete transfer and its attempted closures](SHIFT_BRIDGE.md).

## 2. The native inverse moment has an exact affine prime form

The current family route needs a particular native Möbius norm, not a
norm of a nearby Gauss-weighted coefficient. There is a useful exact
prime-only identity:

\[
 \mu_E(n)\log Nn
 =-\sum_{\substack{ap=n\\p\ {\rm prime}\\(a,p)=1}}
                              \mu_E(a)\log Np.           \tag{3}
\]

The coprimality restriction performs the cancellation otherwise carried
by the higher prime powers. It cannot be dropped.

Apply (3) to one leg of the full native moment, after the exact profile
adjustment \(V_D(y)=\log D\,V(y)/\log(Dy)\). This gives

\[
 I(D)=\Delta(D)-\frac{\mathcal T(D)}{D\log D},
 \qquad \Delta(D)\ll U.                                 \tag{4}
\]

Here \(\mathcal T\) is an explicitly defined **complete signed sum** of
prime--Möbius correlations of the form
\(\mu_E(a)\mu_E(ap+h)\log Np\), with every original character, row,
coprimality condition, smooth profile, and natural zero retained.
The shifts range through the appropriate Eisenstein lattice.
The same identity is proved for PR1019's actual orthogonal complement,
retaining its full Gram-inverse kernel and original conjugation convention.

A one-sided lower bound for the complete \(\mathcal T\) would supply
PR1014's open native estimate. Scalar fixed-shift cancellation does not
bound that sum. The affine/field/conductor extension and fixed power
saving are both still missing. This is an exact matching target, not
a claim that rewriting the moment has made its estimate easier.

Read [the full native and projected identities](NATIVE_AFFINE_REDUCTION.md).

## 3. An exact calculation explains the unmarking cost

The source removes auxiliary marks by averaging \(b\) disjoint groups,
each using \(K\) prime bands. For its fixed parameters the prime-weighted
variance of the normalized average tends to

\[
 \frac{r(\rho)^K-1}{b},\qquad
 r(\rho)=\left(\rho^2+\frac1{\log2}\right)
                           e^{(\log2)(\rho-1)^2},
 \quad r(\rho)^K\ge2^K.                                 \tag{5}
\]

The finite version is an exact CRT generating-polynomial identity.
Only \(O(\log\log x)\) disjoint bands of the paper's prescribed shape
fit at scale \(x\). Thus the displayed absolute Cauchy--Schwarz
unmarking estimate does not turn into a fixed power saving just by
increasing the number of groups. The fixed-parameter asymptotic is
not asserted uniformly for growing \(b,K\).

Read [the finite identity, prime asymptotic, and quantifiers](MARK_VARIANCE.md).

## 4. What was tried beyond the paper's final theorem

| Attempt | Exact outcome |
|---|---|
| Substitute the new theorem into the native inverse consumer | Required coefficient, conductor, affine-shift range and \(D^{1/30}\) saving are not supplied |
| Move the auxiliary primes to fixed powers of \(x\) | The dirty-edge list saving remains too weak; enlarging the list or moment order exhausts the root-counting modulus budget |
| Strengthen the paper's one-sign Möbius input to a power bound | Even an idealized upgrade yields \(X M^{\beta-1}\), whose exponent is at least \(\beta\); it does not automatically contract the old exponent |
| Set the additive shift to zero | The marks vanish on large primes, and the actual sum is \(-\vartheta(x)\), not \(o(x)\) |
| Use finite prime marks in PR1021's positive marked-count criterion | A fixed finite mark has no global logarithmic branch at zeta zeros; a controlled infinite-prime limit is still needed |
| Use a zero-mean kernel to remove the difficult main term | It removes the Möbius signal needed for zero detection |

The detailed [source audit](SOURCE_AUDIT.md) identifies the relevant
pages and equations. It found no concrete fatal defect in the portions
checked. It is not a full independent certification of the source's
52-page proof.

## 5. Evidence and reading order

1. SHIFT_BRIDGE.md: the alternative ordinary-zeta route and full power target.
2. NATIVE_AFFINE_REDUCTION.md: the exact connection to the current family work.
3. MARK_VARIANCE.md: what the existing auxiliary-mark estimate actually costs.
4. SOURCE_AUDIT.md and SOURCES.md: dependency scope and reproducible source identity.
5. CHECKS.md: exact finite checks, independent arithmetic controls, and their limits.

All four check scripts passed in isolated Python execution. The exact
checker uses rational arithmetic and formal prime logarithms. Separate
floating-point checks reproduce the double-Stieltjes identity and test
the native/projected affine identity using actual Eisenstein primary
ideals and sextic residue symbols. None of those finite checks supplies
an all-scale correlation estimate.

The mathematical files are frozen at
[14aba2d9af60f2c2849dfe31bab10f5c6996c8aa](https://github.com/GettysburgResearch/riemann/commit/14aba2d9af60f2c2849dfe31bab10f5c6996c8aa).
The separate [shift-bridge review](REVIEW_SHIFT_BRIDGE.md) and
[variance/affine review](REVIEW_VARIANCE_AFFINE.md) fetched the load-bearing
files at that exact commit and verified the reviewed bytes. Their stated
independence limits and conditional scope remain part of the record.

The useful next task is to bound the **full signed average in (1)** or
the **complete affine sum in (4)**. Estimating another centered error
after deleting the Möbius main term would not advance the zero-free
boundary.
