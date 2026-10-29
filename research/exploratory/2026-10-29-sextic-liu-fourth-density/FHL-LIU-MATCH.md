# Matching the FHL and allowed-generator sextic rows

**Scope.** This is a source-level comparison of de Faveri §2.3.4 with Liu §3 and the z=0 clause of Theorem 12.14. It does not independently prove either preprint's construction or the Liu moment theorem. The field must satisfy Liu's actual Part II hypothesis: fix a cyclotomic field F containing μ₁₂ and a common finite set S containing both constructions' required bad primes and making O_{F,S} principal. The conclusion below is for this F and this common S; it does not establish the moment over Q(ω), which does not contain μ₁₂.

Fix the same embedding μ₆→C and the same sextic power-residue orientation in both sources. Let u be a good ideal. De Faveri §2.3.4 chooses a decomposition

    u=(x) E g⁶,    x≡1 mod c,                                   (1)

where E runs over a fixed finite set of good ideal representatives, each with a chosen S-generator m_E, and g is a good fractional ideal. Choose one such decomposition once for u; for example the source existence assertion with second argument the unit ideal suffices. Since O_{F,S} is principal, choose an S-generator α_g of g. Let α_u be Liu's allowed S-generator of u, unique modulo S-unit sixth powers. Equality of extended S-ideals in (1) implies

    ε_u = α_u/(x m_E α_g⁶) ∈ O_{F,S}×.                           (2)

The class of ε_u modulo sixth powers belongs to the fixed finite group `O_{F,S}×/(O_{F,S}×)⁶`. Its associated good-ideal character

    ξ_ε(a)=(ε/a)₆=χ_a(ε)                                         (3)

is one of Liu's fixed finite unit characters Υ_S by Lemma 3.3. Exact sign/conjugation of (3) is fixed by the common residue orientation; changing it only replaces the finite character by its inverse.

For every good prime p outside the finite supports of u, E, g and the divisor of x m_E, de Faveri's definition and (2) give

    χ_u^FHL(p)=(x m_E/p)₆
               = ξ_{ε_u}(p)^−1 (α_u/p)₆
               = ξ_{ε_u}(p)^−1 χ_p(α_u).                       (4)

The first equality uses the same fixed decomposition (1), which is permitted at those primes; the sixth power of α_g contributes 1. Both sides of (4) are finite-order Hecke characters in p on the good ideals: de Faveri §2.5.1 proves this for the FHL side, and Liu Lemma 3.3 proves it for the allowed-generator and unit-character sides. Equality at all but finitely many primes therefore makes their primitive inducing characters equal, by the standard uniqueness of Hecke characters (equivalently class-field/Chebotarev). At each good p|u both original row presentations vanish, while at other good primes equality extends from the primitive characters. Consequently the equality with original zero masks holds on **every** good column ideal a:

    χ_u^FHL(a)=ξ_{ε_u}(a)^−1 χ_a(α_u).                          (5)

This is stronger than equality of conductors alone. Fractional choices in (1) do not introduce a moving exceptional set into (5): they are used only for the almost-all-prime comparison and are removed by uniqueness. Both sides retain the zeros when `(a,u)≠1`. The fixed bad factors at S are omitted in the good-column convention.

For u varying, partition rows by the finitely many classes `[ε_u]`. Within one class the right-hand side is exactly Liu's common presentation `ν(a)χ_a(k)` with fixed `ν=ξ_ε^−1` in a finite group containing Υ_S, and k=α_u. Liu's allowed row sum contains one allowed-generator class for every exterior ideal and is nonnegative after taking moments, so a sixth-free or finite-class restriction can only decrease it. Liu Theorem 12.14, z=0, and Remark 12.16 then give its ordinary **plain fourth moment** for these rows, subject to their stated fixed-profile, height and principal-inducing exclusions. A good nonunit sixth-free u is nonprincipal by its tame local conductor, so only the unit label can be principal. The theorem does **not** by itself give a product moment involving an actual Möbius inverse coefficient; the deduction here uses its plain fourth moment only.

**Independent review.** Families checked the S-unit ratio and the good-prime masks. The auxiliary g in (1) may meet a later column even when that column is coprime to u; the almost-all-prime comparison and Hecke-character uniqueness are therefore essential, and no raw residue quotient is evaluated at such primes. The source moment and residue conventions remain imported.
