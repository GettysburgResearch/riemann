## Checkpoint 5 — multiplicity-aware jet-coherence transfer

Exact checkpoint base:
eafd6d86055179e5b2fa9b3747ea740b8609ba64.

The real reverse--Rolle branch now allows arbitrary finite critical
multiplicity. At every noncommon odd-order turn,

\[
\rho_c^{\mathrm{jet}}=r!f(c)/f^{(r+1)}(c)
\]

is the leading principal coefficient that classifies turn orientation.
Common derivative-order mass transfers directly, giving

\[
N_{\mathbb R}^{\mathrm{mult}}(f)
\ge
\mathfrak m_{\mathrm{com}}
+(2\mathfrak C_{\mathrm{jet}}-1)R_{\mathrm{jet}}-1.
\]

The theorem recovers draft L-104522.4 on the simple noncommon stratum. It also
retains the exact defect

\[
N_{\mathbb R}^{\mathrm{mult}}(f')
=\mathfrak m_{\mathrm{com}}+R_{\mathrm{jet}}
+\Delta_{\mathrm{mult}},
\]

so high derivative multiplicity cannot inflate the transfer premise.

Ordinary residues are insufficient: \(x^6\pm1/64\) have identical zero
ordinary first/second residue charges and the same critical event orders, but
zero versus two real roots. Their leading jet carriers have opposite signs.

Exact replay:

    PASS_T105104_JET_COHERENCE_REVERSE_ROLLE
    15/15 focused tests in normal and optimized Python
    digest bcd3ac0f644c49e47be6b2e019a57b2e7d2b8b6df14dfec97da854cb44b3bed6

Xi jet proportions and moment estimates, the jet/global-observable bridge,
RCMV104530, and RH remain open.
