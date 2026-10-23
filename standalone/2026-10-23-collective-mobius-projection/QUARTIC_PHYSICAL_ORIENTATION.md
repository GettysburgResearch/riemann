# The physical quartic inverse has the opposite Gauss orientation

Status: exact interface correction, 23 October 2026. This note concerns the proposed inverse consumer of PR1016, not the correctness of its separately stated native Gauss-sum tail or completion identities. It identifies an additional missing interface before the centered spectral estimate can be applied.

Fix the native DDHL convention

\[
 \chi_c(x)=(x/c)_4,\qquad
 g_4(k,c)=\sum_{x\bmod c}\chi_c(x)\,e_F(kx/c).
\]

For odd squarefree c, put gamma(c)=g_4(1,c)/sqrt(Nc). Exact finite Fourier scaling gives

\[
 {g_4(k,c)\over\sqrt{Nc}}=\gamma(c)\overline{\chi_c(k)}. \tag{O1}
\]

The corrected codec proved in PR1016 is gamma(c)^2=mu(c)alpha(c), alpha(c)=c/|c|. Thus

\[
 \mu(c)\gamma(c)=\alpha(c)\overline{\gamma(c)},\qquad
 \mu(c)\overline{\gamma(c)}=\alpha(c)^{-1}\gamma(c). \tag{O2}
\]

Both O1 and O2 are valid with their literal zeros. The relevant primary source conventions are [DDHL v4, section 3](https://arxiv.org/html/2306.11875v4), and the inherited codec is at commit `7ea66551190f291101b0dd44fb1fc9b3331c560d`, `standalone/2026-10-22-quartic-full-sieve/CORRECTED_QUARTIC_CODEC.md`.

## 1. Track both factors through Poisson

Start with the physical inverse column mu(c)chi_c(u)^e, e=+1 or -1. In the coprime pair c,d in its squared moment, row Poisson transforms chi_c^e times chi_d^-e. CRT splits its root into the two primitive roots, with factor chi_c^e(d)chi_d^-e(c). Quartic reciprocity makes this last factor a fixed ray phase. Consequently, up to those fixed ray phases, the transformed c-column has both factors

\[
 A_e(c;k)=\mu(c){\tau(\chi_c^e)\over\sqrt{Nc}}\chi_c^{-e}(k). \tag{O3}
\]

Changing the sign of the Fourier exponential changes k to -k and only adds a fixed ray phase. It does not invert the character of k. The coprime pair already determines the orientation; additional common-divisor branches cannot repair a wrong orientation on this branch.

If e=+1, O2 gives

\[
 A_+(c;k)=\alpha(c)\overline{\gamma(c)}\,\overline{\chi_c(k)}. \tag{O4}
\]

For e=-1, use the exact root identity tau(bar chi_c)=chi_c(-1)overline{tau(chi_c)}. Then

\[
 A_-(c;k)=\chi_c(-1)\alpha(c)^{-1}\gamma(c)\chi_c(k). \tag{O5}
\]

The factor chi_c(-1) is fixed finite ray data. The remaining coefficient in O5 is **not** alpha(c)^-1*g_4(k,c)/sqrt(Nc): its k-character is chi_c, whereas O1 contains bar chi_c. Conjugating the whole expression gives O4 and does not remove the mismatch.

For squarefree c the exact native representation is instead

\[
 \boxed{A_-(c;k)=\chi_c(-1)\alpha(c)^{-1}
                  {g_4(k^3,c)\over\sqrt{Nc}}.} \tag{O6}
\]

Indeed bar chi_c(k^3)=chi_c(k), including zeros. Equivalently O5 equals the proposed native k-column multiplied by the moving quadratic factor chi_c(k)^2. That factor depends on the physical row and cannot be absorbed into a row-independent column weight or a fixed ray character.

## 2. A one-prime distinction

Take c=-1+2i, Nc=5. In its residue field, i=3 and the quartic character on 1,2,3,4 is 1,-i,i,-1. After dividing by the nonzero value at k=1, the physical negative-sign transform O5 has row values chi_c(k), while the native series O1 has row values bar chi_c(k). At k=2 these are -i and +i; at k=1 both equal one. No k-independent scalar can equate the two functions.

This distinction is checked by exact finite Fourier sums in `verify_quartic_orientation.py`, in Q(zeta_20). The checker does not prove a global estimate; it verifies the native Fourier sign and rejects the erroneous identification without floating-point arithmetic.

## 3. Consequences and remaining possible repairs

The native all-row completion and native primitive-sieve tail in PR1016 remain statements about g_4(k,c), and their proofs do not use O3. Likewise the new all-row sieve and tail in `QUARTIC_ALL_ROW_SIEVE_AND_TAIL.md` remain valid as stated. Their transfer to this physical inverse is a separate issue.

Directly using O6 changes the numerator norm from Nk to (Nk)^3. The cited DDHL functional equation, whose conductor factor is N(nu)^(1-s), then has (Nk)^(3-3s), and its natural packet scaling cannot be read with nu=k. The set of numerators k^3 is sparse; an unrestricted numerator mean up to K^3 is not a mean of size K for that set. Natural row valuations in a nonsquarefree-modulus completion also change: the local condition v_p(nu)=e-1 becomes 3v_p(k)=e-1.

Another possible repair is a dedicated functional equation for the multiplicatively twisted family sum_c gamma(c)alpha(c)^-1 chi_c(k)(Nc)^-s and its reflected partners. Such a theorem would have to retain the growing finite conductor, the squarefree projector, all local masks, and the arithmetic diagonal. This note does not supply it.

Thus the open interface is earlier than a numerical choice of level cost in the native centered estimate. A valid physical orientation must first be established. The conditional principal amplifier implication remains valid if its explicitly stated full physical inverse-moment premise is proved by some method. This note does not disprove that premise or any zero-free theorem; it prevents using the native k-series as its proof without an additional transformation.
