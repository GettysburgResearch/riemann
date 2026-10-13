# Parity, cubic fibers, and a damped generalized moment

Status: proposed research packet. It proves an exact parity reduction, a full hierarchy for a weighted version of the original arithmetic moment, asymptotic obstructions to several larger coefficient classes, and finite transform/measure-comparison theorems. The original undamped generalized moment and RH remain open.

Scope: the literal zero-extended sextic/Möbius family over the Eisenstein field, with ideal columns and all nonzero element rows. Every analytic estimate states its test, row-height, smaller-scale, and moving-exclusion premises. In particular the numerical use of a pointwise exponent 7/8 is conditional on the displayed uniform pointwise premise; this packet does not certify that exponent independently.

Base: PR 926, commit `086bf0560c0c2679a1fe41418f583d2c5ca743c3`. This is a separate research continuation. Earlier packet bytes and their review identities are preserved. The comparison with later PRs is source-qualified below; those branches are not silently integrated.

## 1. What the reassessment changed

The target remains

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad
M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D)|^{2k},
\]

with a desired estimate

\[
M_{2k}(D,D^{h_k})\ll_\epsilon
D^{h_k+k+e_k+\epsilon},\qquad h_k=o(k),\quad e_k=o(k).
\tag{1.1}
\]

Orders are fixed before the scale tends to infinity. The cofinal sequence is chosen afterward; no uniform constant in k is needed for the existing extraction argument. Its zero-free boundary is

\[
\Re s>\frac12+\frac{5h_k}{12k}+\frac{e_k}{2k},
\tag{1.2}
\]

for the fixed twists, test detector, and contragredient coverage stated in the source. A finite list of higher moments is not (1.1).

The recent work improves shared-prime sectors, exact divisor reunion, and the amount of scale sampling required. The long, nearly coprime singleton part survives. On that part, taking two native second moments and bounding the other factors by a pointwise exponent b gives

\[
e_k=(2b-1)(k-1).
\tag{1.3}
\]

This packet proves a stronger diagnostic than checking a finite menu of Hölder allocations: all fixed integer-product sextic sieve bounds can hold simultaneously in a common-spike model with the same cofinal slope. More elaborate use of those norms alone cannot make (1.3) sublinear.

There is also a native arithmetic warning. The all-distinct prime-column face already has subsequences of size at least

\[
D^{2k+h/6-o(1)}\qquad(0<h<6/5).
\tag{1.4}
\]

This does not lower-bound the complete Möbius moment. It proves that a proof must allow cancellation between the selected prime face and composite squarefree columns. An arbitrary positive subdivision by prime count would destroy precisely the cancellation being sought.

## 2. The new exact object: parity damping

At each good prime split the sextic character, including its nonunit zero, as

\[
\chi_p(u)=Q_p(u)C_p(u),\qquad
Q_p=\chi_p^3\in\{0,\pm1\},\quad
C_p=\chi_p^4\in\{0\}\cup\mu_3.
\]

Introduce independent fair signs in the polynomial with only cubic row coefficients and expand its even power in those signs. This defines real coefficients \(\mathcal C_{k,r}(u)\), indexed by the squarefree parity ideal

\[
r=\operatorname{rad}_2(n_1\cdots n_km_1\cdots m_k).
\]

The complete original moment is exactly

\[
M_{2k}=\mathcal B_k+
\sum_{r\ne1}\mu_K(r)\sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u),
\tag{2.1}
\]

where the baseline is nonnegative and unconditionally satisfies

\[
0\le\mathcal B_k\ll HD^{k+\epsilon}.
\]

The coefficients in the remainder depend on the row through cubic characters and their zero masks. They are not arbitrary row-independent coefficients to which one may directly apply a quadratic large sieve. The baseline is also not just the complete-residue principal character projection: it contains all even-total-multiplicity tuples.

Now give each prime sign mean \(-(Np)^{-t}\), with \(t\ge0\), in the polynomial with the original sextic phase. Its positive averaged moment is exactly

\[
\mathcal F_{k,t}
=\mathcal B_k+
\sum_{r\ne1}\frac{\mu_K(r)}{(Nr)^t}
       \sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u).
\tag{2.2}
\]

In particular \(\mathcal F_{k,0}=M_{2k}\). The parameter acts on the surviving singleton sector itself; on completely disjoint columns, \(Nr\asymp D^{2k}\).

### The full hierarchy that is proved

Under the explicitly quantified native pointwise premise \(\mathrm{PW}_b\), the complete damped family obeys

\[
\boxed{\mathcal F_{k,t}(D,H)
\ll HD^{k\max\{1,2b-2t\}+\epsilon}.}
\tag{2.3}
\]

If the stated native second moment at the same ambient row height and all smaller column scales is also supplied, the stronger bound is

\[
\boxed{\mathcal F_{k,t}(D,H)
\ll HD^{k+(k-1)(2b-2t-1)_++\epsilon}.}
\tag{2.4}
\]

These estimates retain the whole signed union. They are not estimates for separately positive parity sectors.

| Available pointwise input | Damping at which every fixed moment has diagonal size | Status |
|---|---:|---|
| Elementary counting, b=1 | t=1/2 | Unconditional |
| Uniform native \(\mathrm{PW}_{7/8}\) | t=3/8 | Conditional on that premise |
| General \(\mathrm{PW}_b\) | t=b-1/2 | Conditional when b<1 |
| Original problem | t=0 | Open |

The proof centers the independent signs. The coefficient at a centered prime set d becomes the exact shorter native sum

\[
\xi_u(d)(D/Nd)^{-t}
A_u^{(dq)}(D/Nd;x^{-t}W).
\]

This is the key arithmetic compatibility: the cofactor is still an inverse Möbius sum, with a literal coprimality mask. A finite inverse Euler product supplies the moving-mask adapter. A self-contained sign norm inequality and ideal divisor counting then prove (2.3). Combining the resulting nonnegative majorant with the native second moment proves (2.4).

The same decomposition also proves

\[
|\mathcal C_{k,r}(u)|\ll D^{k+\epsilon}(Nr)^{-1/2},
\]

and hence pays the entire range \(1<Nr\le R\) with cost at most \(HD^{k+\epsilon}\sqrt R\). This is useful for small parity conductor; it leaves the fully singleton endpoint open.

Full statements and proofs: [PARITY_DAMPED_MOMENTS.md](PARITY_DAMPED_MOMENTS.md).

## 3. Why the proved damping does not improve the old zero-free line

Jensen gives the exact comparison

\[
M_{2k}(D,H;W)
\le D^{2kt}\mathcal F_{k,t}(D,H;x^tW).
\tag{3.1}
\]

At the proved threshold \(t=b-1/2\), this returns the old pointwise slope. The factor in (3.1) cannot be discarded by positivity or by the semigroup law. A bounded coefficient-array example attains its power cost; that example is explicitly distinguished from the fixed native Hecke family.

The new parameter also has an exact arithmetic realization. Multiplication of a physical row by a cube preserves every cubic phase:

\[
C_n(ua^3)=C_n(u)\mathbf1_{(a,n)=1},\qquad
Q_n(ua^3)=Q_n(u)Q_n(a).
\tag{3.2}
\]

Over a complete good modulus f, the biased average is the native cube-orbit average against the positive product

\[
R_t(a)=\prod_{p\mid f}\bigl(1+(Np)^{-t}Q_p(a)\bigr),
\qquad a\in(O/f)^\times.
\tag{3.3}
\]

This is a concrete bridge to Riesz products and independent sign measures. Complete residue classes are essential in (3.3). Representatives a of a complete modulus need not fit in the short physical budget; multiplication by a cube costs \(N(a)^3\) in row norm.

The accompanying note computes the exact cost of changing the sign bias. It also projects that comparison onto the finite Walsh space actually used by a fixed moment. On that relevant space, the optimal general L2 cost has a power proportional to k when the target damping is below 1/2. The full infinite-product comparison is even more singular, but that larger obstruction must not be confused with the finite support of the actual moment. Neither comparison excludes a better result for the special Möbius polynomial.

Full proofs, the physical row budget, and the positive-damping diagonal floor: [CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md](CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md).

## 4. Two approaches that now have precise failure mechanisms

### Deforming the prime count

The nearby family \(\mu_K(n)z^{\omega(n)}\) is not a harmless enlargement of the coefficient class. After averaging the exact sixth-power masks, its principal Euler series has the local factorization

\[
F_z(s)=\zeta_K(s)^{-z}E_z(s)
=(s-1)^zG_z(s),\qquad G_z(1)\ne0.
\]

For every fixed nonintegral z near 1, the branch at 1 forces coefficient growth exponent one. Averaging actual sixth-power rows amplifies this to

\[
\limsup_{D\to\infty}
\frac{\log(1+M_{2k,z}(D,D^h))}{\log D}\ge2k+h/6.
\tag{4.1}
\]

The prime-count derivative \(\mu_K(n)\omega(n)\) has the same obstruction. At z=1 the local singularity becomes an ordinary zero, so no such conclusion is made for the original Möbius coefficients. The classical zeta-power singularity is not claimed as a new discovery; the packet proves its native all-row amplification and its implication for this proposed moment strategy without importing a Selberg-Delange asymptotic.

Full proof, including the separate asymptotic all-distinct prime-face result: [ARITHMETIC_PARITY_OBSTRUCTION.md](ARITHMETIC_PARITY_OBSTRUCTION.md).

### Treating theta reflection as a contraction

The normalized good-prime Bessel transform is a unitary involution on the mean-zero finite field space. On the odd sextic characters, it and normalized additive Fourier generate an exact S3 action on the three channels \(1,3,5\).

There is a striking exact zero compression on mixed \(+1,-1\) singleton orientations. It does not close the estimate: the entire omitted component returns through the quadratic channel on the second reflection. A native equal-product four-prime example has nonzero physical covariance while that compression is zero. Thus the compression cannot be identified with the original row covariance.

Moreover, the transformed quadratic channel carries Gauss phases and conductor-dependent dilations. It is not automatically one of the finite-order inverse columns covered by the previous quadratic-product theorem. The note states the additional adapter and gives an explicitly optimistic norm-budget comparison; no physical identity is asserted from the finite representation theory alone.

Exact spectra, the S3 orbit and leakage identities, and the native mismatch: [BESSEL_CHANNELS_AND_LEAKAGE.md](BESSEL_CHANNELS_AND_LEAKAGE.md).

## 5. What a successful next strike must prove

The most useful new target is quantitative removal of parity damping on the **complete native** quadratic/cubic remainder. Starting from a pointwise exponent b, fix a positive eta below b-1/2 and put

\[
t=b-\frac12-\eta.
\]

An estimate

\[
\mathcal F_{k,t}(D,D^{h_k};x^tW_*)
\ll D^{h_k+k+d_k+\epsilon},\qquad
h_k=o(k),\quad 0\le d_k=o(k),
\tag{5.1}
\]

for a cofinal sequence and the exact zero-safe detector/twist coverage would, by (3.1) and the existing extraction theorem, move the boundary to b-eta. The source still has to satisfy all its row and contragredient conventions. Driving t to zero with sublinear remaining losses would recover the full target.

This is a concrete arithmetic estimate, not a consequence of the results already proved. It involves the actual signed cubic coefficients in (2.1). A general coefficient bound, a complete-residue identity, or a low-rank projection is insufficient. The new proofs say exactly why each of those replacements loses the information needed at this step.

## 6. Source map and validation

| Prior source | What was used in this reassessment | Boundary retained |
|---|---|---|
| PR 926, `086bf0560c0c2679a1fe41418f583d2c5ca743c3` | Native family, pointwise/second-moment interfaces, quadratic products, fixed-detector extraction | Component estimates and conditional extraction |
| PR 927, `f9939c957f5aac6b2099b591e4988991700a152b` | Exact auxiliary reunion and higher cubic pools | Native singleton covariance remains |
| PR 928, `ab98878279cd5614fe79bb94aa916e97c9ee50b4` | Shared-graph selectors, principal short/long cancellation, joint descent | Selectors do not act arbitrarily on free singleton ideals; principal cancellation does not bound the nonzero-frequency remainder |
| PR 929, `97bf40329489992e9384c34d7595af6d01a40774` | Conductor averages, rational-prime incidence, Gaussian sampling | Stronger paid sectors and sampling do not prove the sampled arithmetic premise |
| PR 911, `2f8b6a3898a722d0602a91dea73bac344a3bb7dd` | Recovered finite native witnesses and prime-slot route status | Finite signs and a Mellin tube do not supply the full prime-slot complement |

The literature connection to random multiplicative functions is classical; the elementary sign inequality is re-proved in this packet. The Bessel note pins the precise imported reflection normalization. It does not import a GRH-dependent cubic dispersion estimate to prove a statement about RH.

The mathematical arguments establish the infinite statements at their declared scope. The finite diagnostics check local residue arithmetic, Walsh/biased-sign identities, rational exponent envelopes, finite product-measure comparisons, and transform identities. They cannot establish the pointwise premise, a new uniform arithmetic cancellation estimate, an infinite moment hierarchy at t=0, or RH.

Publication and exact-commit review scope are recorded in [VALIDATION.md](VALIDATION.md). Each review applies only to its named files at the published source commit. This packet remains a proposed research contribution rather than an integrated theorem in main.
