# Internal review: exact quartic completion and the corrected Möbius factor

**Reviewer:** `full_inverse`, independently of `alternative_major`.

**Objects reviewed:** `work/round4_alternative/QUARTIC_ALL_ROW_COMPLETION.md`, SHA256 `5e89202a6a9c72382ab01e38a6444a80c1c31199e030a01c92b19700d52620f4`, and `work/round4_alternative/CORRECTED_QUARTIC_CODEC.md`, SHA256 `cf82e4e81c15c16814d49d4415301207e30c4152829e03ad55280ad6148f1754`. The completion was first checked at `af28abe424a3699f79ad0faa1795bd1143a00c2fcefc5de1eda3b4be43b3fe54`; the later change only cites the corrected pure-angular codec in its section 6, leaving its completion algebra unchanged.

**Status:** internal algebraic and source review. The exact identities check. No centered moment or new zero-free region is approved by this review.

## 1. High numerator valuations

I checked (2.1) directly against the prime-power Gauss formula in DDHL,
[arXiv:2306.11875v4, §3](https://arxiv.org/html/2306.11875v4).
For $p^4\mid k$, the local terms of modulus exponents one through three vanish. The exponent-four term is $\varphi(p^4)$, whereas the lifted tail contributes $(Np)^4$ times the modulus-zero term of the series at $k/p^4$. Their exact difference is $(Np)^3$. This gives the stated coefficient of $\psi_{\gamma p}(k)$ and hence

$$
\Delta_p(s,\xi)\psi_{\gamma p}(k,s,\xi;v)
=\psi_\gamma(k,s,\xi;v)
-\xi(p)^4(Np)^{4-4s}\psi_\gamma(k/p^4,s,\xi;v).
$$

The CRT factors are unchanged by extracting four prime powers. The primary ray class modulo four is unchanged as well. The argument works at arbitrarily high numerator valuations and does not require a recursive fourth-power-free reduction.

## 2. Combined identity and scales

I checked the application of CDFD
[arXiv:2604.01316v2, Corollary 6.2](https://arxiv.org/html/2604.01316v2)
to each high-valuation term. The products $a,b,c,T$ have disjoint support. In particular, division by $t^4$ changes neither the quadratic factor in $\Delta_a^*$ nor either primitive Gauss factor indexed by $e$ and $f$. Thus the $t$-independence of the displayed coefficient $C_{e,f}$ is valid, and the products of the $\Delta$ factors combine exactly as stated in (3.1).

The normalized shifts in (4.1)--(4.3) also check. For example,

$$
(Ne)^{5/2-3s}=(Ne)^{-1/2}((Ne)^{-3})^{s-1},
$$

and the $f$ and $t$ terms give amplitudes $(Nf)^{-1/2}$ and one respectively. The changed numerator has norm
$K(Nf)^2/((Nt)^4(Ne)^2)$, giving precisely the displayed factors
$(Nt)^{-2}(Ne)^{-2}(Nf)^{-2}$ in $L'$. The geometric expansions have ratio of modulus less than one for $\Re s>3/4$, and their $h,j$ Mellin shifts are correct.

The finite-support cutoff $D''<1/2$ for a test supported in $[1,2]$ is exact. The caution about the reciprocal incoming scale $1/L''$ is necessary. No averaged density or centered diagonal estimate follows from the absolute convergence of a fixed-row Euler expansion.

## 3. A source-version correction discovered during review

The earlier fixed-ray factor in the inherited quartic Möbius codec must be corrected. DDHL v4 (3.11) includes the factor
$((\overline\pi/\pi)_4)^{-2}$, which was absent from the formula used in the earlier note. The corrected exact identity is

$$
\boxed{\widetilde g_4(c)^2=\mu_F(c)\frac{c}{|c|}}
\qquad(c\text{ primary}),
$$

with no additional $(-1/c)_4$ factor.

Here is a proof that includes both types of prime. For a degree-one primary prime $\pi=a+bi$ with norm $p=a^2+b^2$, $a$ is odd and $b$ is even. Modulo $\pi$, $\overline\pi\equiv2a$. Quadratic reciprocity gives $(a/p)=1$: for $|a|>1$, its Jacobi-symbol form is $(a/p)=(p/|a|)=(b^2/|a|)=1$, and the unit cases are immediate. Therefore

$$
\left(\frac{\overline\pi}{\pi}\right)_4^{-2}
=\left(\frac{2a}{p}\right)_2
=\left(\frac2p\right)_2
=(-1)^{(p-1)/4}
=\left(\frac{-1}{\pi}\right)_4.
$$

The two finite signs in v4 (3.11) cancel, giving
$\widetilde g_4(\pi)^2=-\pi/|\pi|$.

For an inert primary prime $\pi=-p$, with $p\equiv3\pmod4$, work in the residue field $\mathbb F_{p^2}$. Frobenius preserves the trace additive character and sends the quartic character to its inverse. Thus $g(\chi)=g(\overline\chi)$. Since $\chi(-1)=1$, conjugation also gives $g(\overline\chi)=\overline{g(\chi)}$. The Gauss sum is real and has modulus $p$, so its square is $p^2$. This agrees with $\mu_F(\pi)\pi/|\pi|=1$.

The square of the CRT reciprocity multiplier is one, so the identity extends multiplicatively to squarefree primary moduli. For nonsquarefree moduli, both sides vanish by the local Gauss formula; at one they are both one.

As a concrete check, for the primary prime $\pi=-1+2i$ of norm five, direct finite Gauss summation gives
$\widetilde g_4(\pi)^2=(1-2i)/\sqrt5$, agreeing with the corrected formula and disagreeing with the earlier extra finite sign. This finite check illustrates the correction; the preceding primewise argument proves the all-modulus statement.

The correction preserves the fixed angular type $\ell=\pm1$ in the prospective quartic route. It does not affect the exact all-row completion or the primitive-sieve tail lemma, which depend on the CRT identities and local magnitudes. It must nevertheless be recorded explicitly wherever the old codec is cited.

The separate corrected-codec file was checked in full. Its literal-zero versions of the two $\mu\widetilde g_4$ identities follow by multiplication on squarefree moduli and are both zero otherwise. Its exact trigonometric norm-five calculation agrees with the finite character table and supplies a valid counterexample to the old extra-ray formula. No algebraic error was found in that file.

## 4. Confirmation at the frozen Git source commit

I independently extracted QUARTIC_ALL_ROW_COMPLETION.md and
CORRECTED_QUARTIC_CODEC.md from
standalone/2026-10-22-quartic-full-sieve/ through git show at exact commit
193c3d79f0522f08f62afc5c24c29f139d889080.
Their Git-object bytes match, respectively, SHA256
5e89202a6a9c72382ab01e38a6444a80c1c31199e030a01c92b19700d52620f4
and
cf82e4e81c15c16814d49d4415301207e30c4152829e03ad55280ad6148f1754,
the reviewed revisions identified above. Neither contains a control byte
other than a line feed.

The source commit has tree
1e71897b46a6b7b75fe8694c48b7d08911260276 and parent
e87c5f669f81fe6371af926917d1c5b21023bce8. I read the packet README at
that same commit; its SHA256 is
d2d4db8df9309fd16cfeb3ff58fdaf5b1454a85417e9897264edd2b1756b3d44.
Its account of the exact all-row completion, the corrected pure-angular
Möbius factor, and the remaining centered spectral estimate agrees with
this review.

These quartic results are native exact deductions from the stated
published local identities. Their status differs from the packet's
marked-moment refinement, which imports the pinned QRH reflection and
recursion. The README preserves that distinction and explicitly says that
the requested substantial zero-free-boundary improvement has not been
achieved. This review confirms only the stated exact algebra at the
frozen commit. It remains an internal scoped review, not external peer
review, formal verification, integration approval, or approval of a new
zero-free boundary. No source mathematics was changed in this check.
