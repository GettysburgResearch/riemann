# FFPS correlated-mask amplifier: exact restricted-Gram packet

Status: **exact bounded formal tensor theorem, with one explicit fixed-tensor
arithmetic mask and strict global-FFPS firewalls**.

## Start here

The main result is a genuine loophole in the earlier local/product-mask no-go.
For the corrected square-phase Gram

\[
G=\bigotimes_i(p_iI_{m_i}-J_{m_i}),\qquad m_i={p_i-1\over2},
\]

a correlated joint support can have a larger denominator than the complete
grid and hence smaller sharp restricted dual energy.  The smallest prime
example is the \((5,7)\) grid: deleting a two-cell matching changes the
denominator from \(72\) to \(74\), so the leverage drops from \(1/2\) to
\(18/37\).

There are two complementary many-prime conclusions.

1. A random fixed-size identity proves nonconstructively that some formal
   half-density mask over all odd primes through \(x\) has leverage at most
   \(2^{2-d}(1+o(1))\), where \(d=\pi(x)-1\).
2. If every \(p_i\equiv1\pmod4\), a quadratic-residue parity checkerboard is
   explicit.  Its optimal weight is the positive uniform weight \(2\), and
   its leverage is

   \[
   {4\over
   \prod_i (m_i+1)/m_i+\prod_i p_i/m_i}<2^{2-d}.
   \]

The mechanism is spectral.  A local or product deletion populates lower-order
tensor modes.  The global checkerboard indicator has support only on the
constant tensor line and the all-primes Legendre line, whose eigenvalue is
\(\prod_i p_i\).  It gains energy without signed cancellation.

This is not a global FFPS moment theorem.  The quickest machine-readable entry
point is `exact_mathematics` in `ffps_correlated_mask_amplifier.json`; the
proof-facing entry points are Sections 2, 4, and 5 below.

## 1. Frozen source contract

The exact algebra is completed before any source packet is read.  The producer
then fail-closes against these committed prerequisites:

| source | commit | exact lock | role |
|---|---|---|---|
| `ffps_principal_leverage.json` | `5c9462064aefe43164fcf5bc0b6d76b575e67a49` | blob `d96cd12a5fbfe86b63d9c6b7076c8a99aa139f4c`; LF-SHA256 `cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3` | corrected local Gram |
| `FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md` | `5c9462064aefe43164fcf5bc0b6d76b575e67a49` | blob `e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a`; LF-SHA256 `6b3a0958422f01b44b7702b1088f4e13926d5d11a7725bde2582cd2d371b07e6` | sign-pair/source firewall |
| `ffps_conditioned_mask_no_go.json` | `d6cdca528f664acb8fd9e33541f855faa45bb5ca` | blob `1aa8ea28e164a8389b66b6b780d5e081e6a96848`; LF-SHA256 `fe6024020775e977e3dfe31822137b579c9cef438f9e94666714179ed43d469b` | local/product-mask no-go |
| `FFPS_CONDITIONED_MASK_NO_GO.md` | `d6cdca528f664acb8fd9e33541f855faa45bb5ca` | blob `c300500a1563c5299f3ddffd47571309511bb563`; LF-SHA256 `0a3d7d30780b48de82bb2203e1b1ff0eed7912e348b91be329bc202f945b0524` | metric boundary |
| `ffps_coherent_tensor_cost_frontier.json` | `7d1da8cc11718f138897cd36e8cc83a77c4f65d6` | blob `eb21ae1cdd158395d3547b946f2ee25a84e23e05`; LF-SHA256 `f6b65bb4a8cdaaa7c91464d8fba86b7691350bf14cdcc8a68c90848be6f89d51` | complete-tensor conductor frontier |
| `FFPS_COHERENT_TENSOR_COST_FRONTIER.md` | `7d1da8cc11718f138897cd36e8cc83a77c4f65d6` | blob `292487efca3df3971518edba0c0b23b830be2c16`; LF-SHA256 `037ec4751504d2387a87e606dbd8eb74dbcc3abb554ccb77ee449fd838a4583e` | global-moment firewall |
| `ffps_tensor_signed_amplifier_no_go.json` | `4347a83499f697e3a73393c212507e74f927a2f2` | blob `5f666e6a6ada7cd79eb9af27038ad64d599d4eee`; LF-SHA256 `d9d2bd40bbbd22caba3fe67dd2967f092195e5fe7cdff479c21ff6b6c04062aa`; payload `a61fe11c49e38630762931971c573a87be1763974f9a7ee599ccf10f915c1e95` | complete-frame signed theorem and correlated warning |
| `FFPS_TENSOR_SIGNED_AMPLIFIER_NO_GO.md` | `4347a83499f697e3a73393c212507e74f927a2f2` | blob `1ce6a9c461d5937f4d6bb2de9f430b466ff1e78c`; LF-SHA256 `85bbfdc3f3d137fa6d9a56d0f5445ad131c3628ecb29286155dce5864c8f7929` | metric distinction and \((5,7)\) seed |

The committed signed packet audits live PR #751 at
`98af0db6ec7f77d6333a77a3dac53c4698852f43`.  Its frozen `L-106024` blob is
`d94787dc2cd1cedd74d33ddc6269daf8de1cc061`.  That claim's coordinates are
literally the unordered residue pairs \(\{c,-c\}\), and its Gram premise is
\(pI-J\).  The present theorem is logically independent of the signed
complete-frame theorem.

## 2. Sharp optimization on an arbitrary retained support

Let \(A\) be a nonempty joint support, \(G_A\) the corresponding principal
submatrix, and \(N=\prod_i m_i\) the native amplitude.  Since every local
Gram is positive definite, so is \(G_A\).  For any real or complex weight
vector \(\alpha\) on \(A\), constrained by
\(\mathbf1_A^*\alpha=N\), weighted Cauchy--Schwarz gives

\[
N^2=|\mathbf1_A^*\alpha|^2
\le
(\mathbf1_A^*G_A\mathbf1_A)
(\alpha^*G_A^{-1}\alpha).
\]

Thus, writing \(E_A=\mathbf1_A^*G_A\mathbf1_A\),

\[
\boxed{
\min_{\mathbf1_A^*\alpha=N}\alpha^*G_A^{-1}\alpha
={N^2\over E_A},
\qquad
\alpha_{\rm opt}={N G_A\mathbf1_A\over E_A}.}
\tag{2.1}
\]

Equality in Cauchy--Schwarz also proves uniqueness.  Notice the metric: this
uses \(G_A^{-1}\), not the principal block of \(G^{-1}\).  Confusing those two
matrices erases the correlated-mask loophole.

The uniform indicator used to calculate \(E_A\) is not normally the optimal
weight.  It happens to be optimal in the Legendre checkerboard of Section 5,
where the resulting weight is uniformly \(+2\).

## 3. The complete two-prime support problem

Put \(p=2m+1\), \(q=2n+1\), and regard a support as cells in an
\(m\)-by-\(n\) grid.  If it has size \(s\), row degrees \(r_i\), and column
degrees \(c_j\), expansion of

\[
(pI_m-J_m)\otimes(qI_n-J_n)
\]

gives the exact identity

\[
\boxed{E_A=pqs+s^2-p\sum_i r_i^2-q\sum_j c_j^2.}
\tag{3.1}
\]

For \(s=at+b\), \(0\le b<t\), convexity on integers gives

\[
R_t(s):=\min_{x_1+\cdots+x_t=s}\sum_i x_i^2
=ta^2+b(2a+1).
\tag{3.2}
\]

Simultaneously balanced row and column margins exist for every
\(0\le s\le mn\) (equivalently by Gale--Ryser; the producer constructs them
by bipartite Havel--Hakimi).  Therefore

\[
\boxed{E_{m,n}^{\max}(s)=pqs+s^2-pR_m(s)-qR_n(s).}
\tag{3.3}
\]

This reduces an exact search through \(2^{mn}\) supports to the \(mn\)
nonempty sizes.  The producer exhausts all masks for
\((m,n)=(2,3),(2,4),(3,3)\) and checks every size against (3.3).

### Full grid minus a matching

Delete a matching of size \(k\) from the full grid.  Substitution in (3.1)
gives

\[
\boxed{E_{\rm full\setminus match(k)}-E_{\rm full}
=k(k+2mn-2m-2n-3).}
\tag{3.4}
\]

If \(p,q\ge5\) are distinct, then \(m,n\ge2\) are distinct.  For \(k=2\),
the bracket equals \(2(m-1)(n-1)-3\), whose minimum is \(1\) at
\((m,n)=(2,3)\).  Every such prime pair therefore has a strict correlated
improvement.  At \((p,q)=(5,7)\),

\[
E_{\rm full}=72,\qquad E_{\rm matched}=74,\qquad
{N^2\over E_{\rm matched}}={36\over74}={18\over37}<{1\over2}.
\]

### Two-prime large-dimension limit

From (3.2),

\[
0\le R_t(s)-{s^2\over t}\le {t\over4}.
\]

Consequently, uniformly for \(0\le\rho\le1\), when
\(s=\lfloor\rho mn\rfloor\) and \(m,n\to\infty\),

\[
{E_{m,n}^{\max}(s)\over (mn)^2}
\longrightarrow4\rho-3\rho^2.
\]

The limiting quadratic has its unique maximum at \(\rho=2/3\).  Uniform
convergence forces every discrete optimizing density to tend to \(2/3\),
and the sharp leverage tends to \(3/4\).

## 4. Arbitrary tensor order: exact random fixed-size identity

Let \(d\ge1\), \(N=\prod_i m_i\),
\(T=\operatorname{Tr}G\), and \(B=\mathbf1^*G\mathbf1\).  Tensoring the local
trace and constant-line formulas gives

\[
T=2^dN^2,
\qquad
B=N\prod_i(m_i+1).
\tag{4.1}
\]

Choose \(A\) uniformly among the size-\(s\) subsets.  A diagonal coordinate is
retained with probability \(s/N\); an ordered pair of distinct coordinates is
retained with probability \(s(s-1)/(N(N-1))\).  Hence

\[
\boxed{
\mathbb E E_A={s\over N}T
+{s(s-1)\over N(N-1)}(B-T).}
\tag{4.2}
\]

At least one support has \(E_A\ge\mathbb E E_A\), so (2.1) gives a leverage
upper bound \(N^2/\mathbb E E_A\).

An earlier draft formulation incorrectly suggested that some mask must attain
the average.  That is false and is now an explicit refusal test: for
\((m,n)=(2,3)\), \(s=2\), the average is \(216/5\), while every individual
Gram energy is an integer.  Only “at least the average” is used.

For fixed \(d\), as \(\min_i m_i\to\infty\), a support density \(\rho\) has
normalized expected denominator

\[
2^d\rho-(2^d-1)\rho^2+o(1).
\]

Rounding to the nearest integer size is harmless.  The maximizing density and
the resulting existence bound are

\[
\boxed{
\rho_d={2^{d-1}\over2^d-1},
\qquad
\text{leverage}\le{2^d-1\over4^{d-1}}+o(1).}
\tag{4.3}
\]

This fixed-\(d\) statement is not used uniformly when \(d\) grows.

### All odd primes through \(x\)

There is instead an exact growing-\(d\) calculation.  Let
\(3\le p\le x\), \(d=\pi(x)-1\), and take the exact half size \(s=N/2\)
(it is integral once \(x\ge5\)).  Put

\[
b={B\over N^2}=\prod_{3\le p\le x}{p+1\over p-1}.
\]

Dividing (4.2) by \(N^2\) gives, without a uniformity assumption,

\[
{\mathbb E E_A\over N^2}
={2^dN\over4(N-1)}+{b(N-2)\over4(N-1)}.
\tag{4.4}
\]

The exact factorization

\[
b=\prod_{3\le p\le x}(1-p^{-2})
\prod_{3\le p\le x}(1-p^{-1})^{-2}
\]

and classical Mertens give

\[
b\sim {e^{2\gamma}\over3\zeta(2)}(\log x)^2.
\]

Thus \(b/2^d\to0\), while \(N\to\infty\), and (4.4) proves

\[
\text{formal leverage}\le2^{2-d}(1+o(1)).
\tag{4.5}
\]

For \(M=\prod_{3\le p\le x}p\), the prime number theorem gives
\(\log M\sim x\), \(d\sim x/\log x\).  Therefore (4.5) is

\[
\boxed{
\exp\!\left(-({\log2}+o(1)){\log M\over\log\log M}\right)
=M^{-\log2/\log\log M+o(1/\log\log M)}.}
\tag{4.6}
\]

This is subpolynomial in \(M\), but far smaller than the complete tensor's
order \((\log\log M)^{-2}\) leverage.  Its support is nonconstructive and
formal.

## 5. Explicit Legendre/Jacobi checkerboard

Now restrict to distinct primes \(p_i\equiv1\pmod4\).  On the unordered pair
coordinate \(\{c,-c\}\), define

\[
(v_i)_{\{c,-c\}}=\left({c\over p_i}\right).
\]

This is well-defined because \((-1|p_i)=1\).  Exactly
\((p_i-1)/4=m_i/2\) pair coordinates have each sign, so
\(\mathbf1^*v_i=0\), and

\[
(p_iI-J)v_i=p_iv_i.
\]

Let \(w=\bigotimes_i v_i\), and let the mask indicator be
\(a=(\mathbf1+w)/2\).  It is a zero-one vector of size \(N/2\).  On CRT
coordinates its support is the explicit Jacobi parity condition

\[
\boxed{\prod_i(c_i|p_i)=+1.}
\tag{5.1}
\]

Write \(Q=\prod_i(m_i+1)\) and \(P=\prod_i p_i\).  The two tensor lines are
orthogonal and satisfy \(G\mathbf1=Q\mathbf1\), \(Gw=Pw\).  Hence

\[
\boxed{E_A=a^*Ga={N\over4}(Q+P).}
\tag{5.2}
\]

Moreover, on \(A\),

\[
(Ga)|_A={Q+P\over2}\mathbf1_A.
\]

Substitution into (2.1) shows that the sharp weight is exactly
\(\alpha=2\mathbf1_A\), positive and uniform, and proves

\[
\boxed{
{N^2\over E_A}
={4\over\prod_i(m_i+1)/m_i+\prod_i p_i/m_i}.}
\tag{5.3}
\]

For \((p_1,p_2)=(5,13)\), the producer constructs the six retained CRT pair
coordinates, audits the full \(12\)-by-\(12\) Gram and inverse, obtains
\(E_A=258\), and verifies leverage \(24/43\) with six weights all equal to
\(2\).  The closed three-prime \((5,13,17)\) control gives \(192/647\).

Since \(p_i/m_i>2\), (5.3) is strictly less than \(2^{2-d}\).  Along all
primes \(p\le x\), \(p\equiv1\pmod4\), the classical prime number theorem in
the fixed progression gives

\[
\log M=\vartheta(x;4,1)\sim{x\over2},
\qquad
d=\pi(x;4,1)\sim{x\over2\log x}
\sim{\log M\over\log\log M}.
\]

Thus the explicit checkerboard has the same conductor-scale upper bound
(4.6).  PNT in arithmetic progressions is an imported classical theorem, not
a result of the finite producer.

## 6. What is and is not proved

Proved exactly here:

- the restricted optimizer (2.1) for every nonempty support;
- the complete two-prime support-size frontier (3.3);
- the matching gain (3.4) and strict improvement for every distinct
  \(p,q\ge5\);
- the exact random fixed-size identity (4.2) and existence consequence;
- the fixed-\(d\) limit (4.3) and the separate growing-prime bound (4.6);
- the explicit residue-pair/Jacobi checkerboard (5.1)--(5.3).

Not proved:

- that an arbitrary high-energy formal mask is a source-realizable FFPS
  arithmetic condition;
- that the explicit checkerboard survives varying owners, conductors, physical
  collapse, carrier removal, or the corrected global assembly;
- WCADD, WCKUM, BPOE, SOCM, any global FFPS mixed/double/principal moment, or
  any conductor-uniform family estimate;
- individualization of a principal member, RH, or GRH;
- an external novelty claim.

The explicit checkerboard is arithmetic only at the fixed local tensor level
licensed by the unordered residue-pair coordinates of `L-106024`.  CRT
realizability there must not be promoted to a varying-owner FFPS theorem.

## 7. Reproduction

The packet uses exact integers and `Fraction` only.  It enumerates 1,152 tiny
control subsets, never a character family, conductor family, finite field, or
L-function.  Source/file/operation/matrix/wall caps fail closed, and no Python
`assert` statement is used, so optimized mode checks the same conditions.

```powershell
python research/l-families/atlas/function_field/ffps_correlated_mask_amplifier.py --check
python -O research/l-families/atlas/function_field/ffps_correlated_mask_amplifier.py --check
python -m pytest -q tests/test_ffps_correlated_mask_amplifier.py
python -O -m pytest -q tests/test_ffps_correlated_mask_amplifier.py
python -m ruff check research/l-families/atlas/function_field/ffps_correlated_mask_amplifier.py tests/test_ffps_correlated_mask_amplifier.py
```

Regenerate the JSON only by omitting `--check` from the first command.
