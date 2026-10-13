# Growing-prime freezing and invertible noise

**Status: PROPOSED, with complete proofs at the stated scope; not independently reviewed. The original generalized moment and RH remain unproved. No zero-free exponent is improved.**

This continuation starts from PR #930 at `ef64e9591fa5a5530c513606b0a17cbbdba9820a`. It changes the deformation rather than optimizing another positive moment envelope: first keep an increasing set of genuine Möbius prime signs, then measure the exact signed cost of restoring the remaining signs.

## The positive theorem

For the native sextic phases over $K=\mathbb Q(\sqrt{-3})$, write

$$
P_{u,Y}(D)=\sum_n\mu_K(n)^2\xi_u(n)W(Nn/D)e(n),
$$

where $e_p=-1$ for $Np\le Y$ and the remaining prime signs are independent and uniform. Literal nonunit zeros, moving column exclusions and every physical row are retained. With $X=\max(2,\beta D)$ for $\operatorname{supp}W\subset[\alpha,\beta]$, put

$$
\mathcal F_{k,Y}=\sum_u w_H(u)\mathbb E|P_{u,Y}(D)|^{2k},
\qquad w_H\ge0,\quad\sum_u w_H(u)\le H.
$$

[Theorem 2.1 and Corollary 2.2](PRIME_FREEZING.md) prove, unconditionally for every fixed $k$ and $\epsilon>0$,

$$
\mathcal F_{k,Y}\ll H D^{k+\epsilon}
\quad\text{when}\quad Y=(\log X)^2.
$$

More generally it suffices that $\sqrt Y/\log(2Y)=o(\log X)$; for example $Y=(\log X)^2(\log\log X)^{2-\delta}$ for any fixed $\delta>0$. The large-$D$ threshold can depend on the chosen little-o function. This is genuinely a growing set of frozen primes, not a fixed exceptional set. It is also genuinely a randomized family: **the signs at larger primes have not yet been restored**.

The proof first establishes the uniform budget

$$
\mathcal F_{k,\mathcal B}\ll H X^{k+\epsilon}
\exp\!\left(2k\sum_{p\in\mathcal B}(Np)^{-1/2}\right)
$$

for any frozen set $\mathcal B$. It uses elementary hypercontractivity, ideal counting, and a deterministic/random prime-factor decomposition. The growing-range corollary needs only Chebyshev's prime upper bound, not a zero-free premise.

## What happens when the remaining primes are restored

Order the relevant primes by norm, and let $j_0$ include those up to $(\log X)^2$. At the step restoring the sign at $p_j$, write the exact native polynomial as

$$
P=U_{u,j}+e_{p_j}V_{u,j}.
$$

The cofactor $V$ retains its actual sextic phase, the exclusion of $p_j$, all previously restored Möbius signs, and its exact shorter column scale $D/Np_j$. The row range is unchanged.

For the fourth moment define

$$
\mathcal J_4=\sum_{j>j_0}\sum_u w_H(u)\mathbb E_{\rm later}
\left[\operatorname{Re}(U_{u,j}\overline{V_{u,j}})
\bigl(|U_{u,j}|^2+|V_{u,j}|^2\bigr)\right].
$$

The exact identity is

$$
\boxed{M_4=\mathcal F_{2,j_0}-4\mathcal J_4.}
$$

The corresponding odd-binomial formula holds at every fixed even moment. It introduces **no Jensen power loss**. However, the needed lower bound

$$
\boxed{\mathcal J_4\ge-C_\epsilon H D^{2+\epsilon}}
\tag{OPEN}
$$

**is not proved**. It is equivalent, up to the known diagonal starting term, to the desired fourth-moment upper bound, not a weaker substitute for it. The reverse inequality $\mathcal J_4\le\mathcal F_{2,j_0}/4$ follows already from positivity of $M_4$.

Every local flux has zero complete-residue mean, but the physical short row ball is not invariant under the required residue permutation. The finite diagnostics exhibit both signs of the actual local flux. Monotonicity, independent cofactors, and summing absolute values would each throw away the missing arithmetic information.

At $H=D^{1+\theta}$, proving the open bound with the original test and twist quantifiers for arbitrarily small fixed $\theta>0$ would feed the inherited $17/24$ extraction interface. The all-order signed target is stated explicitly in [Section 4](PRIME_FREEZING.md). Neither target is proved here.

## Two-sided noise control and a classical connection

[The companion note](NOISE_MULTIPLIERS.md) proves uniform finite moment estimates for an arbitrary independent bias profile $\mathbb E e_p=-a_p$, $0\le a_p\le1$. The local noise multiplier and its inverse are

$$
H_p(s)=\frac{1+e_p\xi(p)(Np)^{-s}}{1-a_p\xi(p)(Np)^{-s}},
\qquad G_p(s)=H_p(s)^{-1}.
$$

If $h,g$ are their coefficient sequences, then, for every deterministic bounded coefficient array supported on $Nn\le X$,

$$
\mathbb E\left|\sum_n b(n)h(n)\right|^{2k}
+\mathbb E\left|\sum_n b(n)g(n)\right|^{2k}
\ll X^{k+\epsilon}.
$$

The bound is uniform in the profile, local phases and masks, and applies also when the profile changes with $X$. The inverse contains a deterministic square-ideal correction; the proof keeps it. The exact dependent convolution cannot be estimated by pretending its two factors are independent: their $p^2$ terms supply an explicit counterexample to that substitution.

For a fixed infinite power profile, the familiar analytic factorization is

$$
Z_{u,t}(s)=H_{u,t}(s)/L_u^S(s+t),
$$

with $H$ and its inverse holomorphic on $\Re s>1/2$. Consequently the shifted inverse-$L$ poles survive. **This core mechanism is classical, not a discovery of this pass:** Aymone--Sidoravicius already establish the untwisted factorization and its zero-free interpretation. The note reconstructs it with native phases and masks, gives uniform positive and negative moments, and separates fixed infinite profiles from cutoff-dependent finite ones.

## A boundary on coefficient generalization

For every fixed $A>2$, an elementary smooth-product construction using the prime ideal theorem produces bounded, cutoff-dependent coefficient arrays which align on primes frozen through $(\log X)^A$ and have size $X^{1-1/A-o(1)}$. Thus a universal coefficient theorem cannot extend the growing range beyond log-power two in that form. This is **not** a counterexample for the native smooth Möbius coefficients. No fixed annular-test counterexample is claimed.

## Sources and credit

- Native parent: PR #930, `ef64e9591fa5a5530c513606b0a17cbbdba9820a`, `standalone/2026-10-12-parity-and-cubic-fibers/PARITY_DAMPED_MOMENTS.md`, particularly Sections 1 and 5--7. Its pointwise equivalence and Jensen barrier are inherited, not newly claimed.
- Related work inspected, not integrated or independently audited: PR #933 metadata at `8685591132bc6f283f670d252121c1629df3a208`; PR #934 `research/exploratory/2026-10-10-quasi-rh-wave/FINDINGS.md` at `3092feee25c583ec760c5f14f4aa4c98d9c5df39`. Neither supplies an analytic premise for these unconditional bounds. No full-repository freshness audit is claimed.
- Marco Aymone and Vladas Sidoravicius, *Partial sums of biased random multiplicative functions*, arXiv:1412.1157v2, Lemma 2.1 and proof of Theorem 1.1, Claim 4.1; Journal of Number Theory 172 (2017), 343--382, DOI 10.1016/j.jnt.2016.08.020. Primary source: https://arxiv.org/abs/1412.1157 . The parsed PDF text was inspected; attempted PDF screenshots were unavailable.
- The log-power-two scale also occurs in a different initial-bias problem: Rodrigo Angelo and Max Wenqiang Xu, *Oscillations of random multiplicative functions under initial bias*, IMRN 2026, rnag198; arXiv:2411.14447. Its completely multiplicative sign-change conclusions are not used here.
- Standard ingredients: fixed-field ideal counting; Chebyshev's bound; the classical prime ideal theorem only for the coefficient-class lower example. The necessary sign inequality and coefficient estimates are proved in the notes. No global priority claim is made for elementary probabilistic estimates.

## Evidence and review boundary

The two mathematical notes contain full proofs at their declared scope. The single exact checker passed **30,634 predicates** in ordinary and optimized Python, with identical JSON output. These are finite algebra checks, not independent asymptotic cases or an analytic certification. The native test uses all 54 nonzero Eisenstein rows of norm at most 13, but **only columns built from five explicitly named prime ideals**, not every native column below the norm cap.

[VALIDATION.md](VALIDATION.md) gives exact coverage and the same-author reconstruction checklist. No independent reviewer, subagent audit, Lean build, or repository-wide CI run is claimed. All new files remain a standalone proposal; earlier research and the integrated record are unchanged.

Replay: `python check.py` and `python -O check.py`. The JSON reports and a SHA-256/Git-blob manifest are included.
