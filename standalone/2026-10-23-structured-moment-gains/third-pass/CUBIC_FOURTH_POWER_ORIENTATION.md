# Physical cubic inverse: fourth-power sextic numerator

Proposed source-dependent local audit, 24 October 2026. This third-pass
addition preserves the two earlier frozen PR1020 packets.

## Outcome and scope

The first row Poisson transform of the cubic inverse has the coefficient
`mu(c) gamma_2(c) conjugate(chi_c(k)^2)`. Its realization by a conjugate
sextic Gauss sum has Fourier numerator **k^4**. The proposed k^2 realization,
its K^2/D reflection, and the resulting cubic 5/6 recursion are withdrawn.
Conjugating the original inverse conjugates both the coefficient and the
character and still gives k^4.

The exact good-prime primitive local system below couples numerator
exponents zero and four at a squarefree physical row prime. Its reflected
exponent-four coefficient is nonzero and of unit size on the central line.
The primitive correction therefore does not itself produce a square
conductor. This does not exclude a new estimate for the actual fourth-power
subsequence or a different integral representation.

## 1. Pinned conventions

Work over E=Q(omega), with primary generators and the fixed excluded set S
of [the pinned OpenAI source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The source file has SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
Use its sextic symbol chi_c, alpha(c)=c/|c|, and normalized Gauss sums

\[
 \gamma_j(c)=(Nc)^{-1/2}\sum_{x\bmod c}\chi_c(x)^j e(x/c).
\]

At good squarefree indices its `eq:signal` states

\[
 \gamma_2(c)^3=\mu(c)\alpha(c),\qquad
 \gamma_1(c)\gamma_2(c)=\mu(c)\alpha(c)G(c).       \tag{1.1}
\]

G is a function on one fixed finite ray group supported at 2 and 3. It is
expanded in that group's characters when a multiplicative coefficient is
needed. The source's reciprocity sign R(a,b) is a bicharacter of that same
fixed group. All residue characters retain their natural zero extension.

## 2. Exact first-Poisson orientation

For coprime good squarefree a,b, CRT with h=bu+av gives

\[
\begin{split}
 &(Nab)^{-1/2}\sum_{h\bmod ab}
     \chi_a(h)^2\overline{\chi_b(h)^2}e(-kh/(ab))\\
 &\qquad=\gamma_2(a)\overline{\gamma_2(b)}
                   \overline{\chi_a(k)^2}\chi_b(k)^2.       \tag{2.1}
\end{split}
\]

The CRT cross factors cancel by cubic reciprocity, and the additive minus
sign is harmless because -1 is a cube. Both sides vanish at nonunit
frequencies, by the primitive Gauss identity. Consequently the cubic
inverse with coefficient mu(c)nu(c) has the transformed column

\[
 B_k(c)=\mu(c)\nu(c)\gamma_2(c)\overline{\chi_c(k)^2}.       \tag{2.2}
\]

Common-support extraction adds punctures and finite ray factors; it does
not reverse this character orientation.

From (1.1),

\[
 \gamma_1(c)=G(c)\gamma_2(c)^2,\qquad
 \mu(c)\gamma_2(c)=\alpha(c)G(c)\overline{\gamma_1(c)}.       \tag{2.3}
\]

Put g_{-1}(m,c)=sum_{x mod c} chi_c(x)^(-1)e(mx/c). At good squarefree c,

\[
 (Nc)^{-1/2}g_{-1}(m,c)=\chi_c(m)\gamma_{-1}(c),\qquad
 \gamma_{-1}(c)=\chi_c(-1)\overline{\gamma_1(c)}.            \tag{2.4}
\]

These identities include the zero values when (m,c)>1. Hence

\[
 \boxed{B_k(c)=\nu(c)\alpha(c)G(c)\chi_c(-1)
                         \frac{g_{-1}(k^4,c)}{\sqrt{Nc}}.} \tag{2.5}
\]

The remaining factor chi_c(-1) is fixed ray data. Numerator k^2 would
give the opposite cubic character while leaving the Gauss coefficient
unchanged. Conjugating (2.5) still has numerator k^4.

If k=R1 R2^2 e^3 with R1,R2 coprime and squarefree, its primitive sextic
numerator core is R1^4 R2^2; primes of e remain punctures. For squarefree
k the numerator norm is (Nk)^4.

## 3. Primitive local system

The variable u is unnormalized: g(m,c) is divided by (Nc)^u. The normalized
variable is s=u-1/2. Fix a good prime p, q=Np, and (k0,p)=1. For numerator
k0^2 p^(2a), a=0,1,2, the only possible local denominator exponents are

\[
 j=0\quad\hbox{or}\quad j=2a+1.                         \tag{3.1}
\]

For 1<=j<=5 the local character is induced from the nonprincipal
chi_p^(-j). Summation over lifts forces additive valuation j-1=2a. Then

\[
 g_{-1}(k_0^2p^{2a},p^{2a+1})
   =q^{2a}\chi_p(k_0)^{2(2a+1)}g_{-(2a+1)}(1,p),          \tag{3.2}
\]

of modulus q^(2a+1/2). Principal local characters at exponents divisible
by six also vanish here, since 2a<=4. Higher exponents vanish by lift
summation.

Let bold Psi_a be the vector of full Gauss Dirichlet series in all needed
fixed ray sectors, and bold P_a the same vector with p-divisible
denominators removed. Any earlier punctures are retained in both. The
angular order remains fixed in this local operation.

Extracting p^j changes the remaining numerator state from a to a-j mod3.
This follows from Gauss multiplicativity and sextic reciprocity; its
extra reciprocity sign is a character of the fixed ray group. Therefore
there are unitary matrices A_p,B_p,C_p, independent of u, with

\[
\begin{aligned}
 \boldsymbol\Psi_0&=\boldsymbol P_0+q^{1/2-u}A_p\boldsymbol P_2,\\
 \boldsymbol\Psi_1&=\boldsymbol P_1+q^{5/2-3u}C_p\boldsymbol P_1,\\
 \boldsymbol\Psi_2&=\boldsymbol P_2+q^{9/2-5u}B_p\boldsymbol P_0.
\end{aligned}                                                    \tag{3.3}
\]

Unitary here is a finite-dimensional statement: these matrices permute
fixed ray characters and multiply by their values at p, fixed angular
phases, and normalized local Gauss factors. No moving-level norm claim
is made. In particular,

\[
\begin{aligned}
 \boldsymbol P_0&=(I-q^{5-6u}A_pB_p)^{-1}
       (\boldsymbol\Psi_0-q^{1/2-u}A_p\boldsymbol\Psi_2),\\
 \boldsymbol P_1&=(I+q^{5/2-3u}C_p)^{-1}\boldsymbol\Psi_1,\\
 \boldsymbol P_2&=(I-q^{5-6u}B_pA_p)^{-1}
       (\boldsymbol\Psi_2-q^{9/2-5u}B_p\boldsymbol\Psi_0).
\end{aligned}                                                    \tag{3.4}
\]

The inverses are holomorphic for Re u>1. Their products over finitely
many primes cost at most a subpower in the product of those primes on
any fixed strip Re u>=1+delta. Thus a fixed-level angular sextic
holomorphy theorem on Re u>1 transfers to the primitive punctured
series for each fixed row. This does not provide a sparse mean.

## 4. Fourth-power conductor survives local extraction

This section is conditional on the stated fixed-level geometric angular
Eisenstein functional equation. Its arithmetic factor at numerator m is
assumed to be (Nm)^(1-u), with fixed finite-dimensional scattering data
as in (4.1). This is the precise candidate interface tested here.
This arithmetic factor can also be read by
comparing the Whittaker powers |m|^(u-1/2) and |m|^(3/2-u). With v=2-u,
and suppressing the common factor from k0, write

\[
\boldsymbol\Psi_2(u)=q^{4-4u}S_{2,p}(u)\boldsymbol\Psi_2^*(v),\qquad
 \boldsymbol\Psi_0(u)=S_{0,p}(u)\boldsymbol\Psi_0^*(v).       \tag{4.1}
\]

The star labels the dual angular data, not a silent switch of sextic
symbol. Fixed archimedean scalars are absorbed in the S matrices. Their
subscripts also permit the unit-modulus Fourier-angle factors at the two
numerators, so equality of these phase factors is not presumed. In unitary
normalization both S matrices are unitary on u=1+it where the scattering
expression is defined. The calculation can alternatively be read as a direct algebraic
test of any proposed functional equation of the form (4.1).

Substitution into the last equation of (3.4), followed by the dual local
split, gives the coefficient of bold P_2^*(v) as

\[
 q^{4-4u}(I-q^{5-6u}B_pA_p)^{-1}S_{2,p}(u)
       [I-q^{-1}S_{2,p}(u)^{-1}B_pS_{0,p}(u)A_p^*].        \tag{4.2}
\]

The exponent -1 is exact:

\[
 (9/2-5u)+(1/2-v)-(4-4u)=-1.                            \tag{4.3}
\]

On u=1+it, both bracketed matrices have singular values between
1-q^(-1) and 1+q^(-1). The reflected state-two branch is therefore
invertible and has size comparable to one. Its q^(4-4u) factor remains.
Expanding the denominator adds sixth-power shifts, and does not replace
the fourth-power shift by a second-power shift. The other reflected
branch has state zero. State one, the p^2 numerator, never appears in
this block. Accordingly this extraction does not justify K^2/D for the
physical squarefree labels; the natural Fourier scale is K^4/D, with
the other completion variables still to be paid.

No smaller global zero-free boundary follows from this note.
