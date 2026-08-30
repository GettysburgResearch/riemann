# L-107303 — Complete clean charts have exact zero or square-root Kummer–Artin–Schreier trace

Claim ID: `L-107303`  
Programme aliases: `LFAM2.COMPLETE_CLEAN_TRACE`, `RIEMANNSTRUCT.AUGMENTATION_GAUSS`  
Status: **PROVED EXACT COMPLETE-CHART TRACE THEOREM**  
Created: 2026-08-30  
Depends on: `L-107302`; elementary Gauss sums  
Programme issues: #763, #737, #739  
Number-field RH status: **not assumed; no transfer claimed**

Let \(k_\ell,k_\rho\) be odd finite residue fields of cardinalities
\(Q_\ell,Q_\rho\). Let \(\eta,\theta\) be constituents of
\(\mathscr C_{\ell,\rho}^{\rm nr}\), so

\[
\eta^2\ne1,\qquad \theta^2\ne1.
\]

Fix nonzero owner residues \(P,Q\). For additive characters
\(\psi_\ell,\psi_\rho\) and parameters \(a\in k_\ell\),
\(b\in k_\rho\), put

\[
\begin{aligned}
S_{\eta,\theta}(a,b)
={}&
\sum_{d\in k_\ell^\times}
\sum_{c\in k_\rho^\times}
\eta(Qd^2)\theta(Pc^2)\\
&\qquad\qquad\cdot
\psi_\ell(ad)\psi_\rho(bc).
\end{aligned}
\tag{L-107303.1}
\]

The sum factors into two one-variable Gauss sums.

If \(a=0\) or \(b=0\), then

\[
\boxed{S_{\eta,\theta}(a,b)=0,}
\tag{L-107303.2}
\]

because the corresponding nontrivial multiplicative character sum vanishes.

If \(a\ne0\) and \(b\ne0\), then

\[
\boxed{
|S_{\eta,\theta}(a,b)|
=
\sqrt{Q_\ell Q_\rho}.
}
\tag{L-107303.3}
\]

The proof is the exact identity

\[
\left|
\sum_{x\in k^\times}\chi(x)\psi(ax)
\right|^2
=
|k|
\tag{L-107303.4}
\]

for nontrivial \(\chi,\psi\), applied to \(\chi=\eta^2,\theta^2\).

Hence every nonresonant constituent of the complete shared-conductor clean
chart is either exactly killed or has pure square-root size. No family average,
asymptotic equidistribution, or RH input is used.

## Meaning

The function-field obstruction is no longer the complete local
Kummer–Artin–Schreier sum. It is the passage from the literal incomplete
Boolean/Wick source and physical shell to this complete clean chart, together
with the three explicit quadratic-resonant sectors of `L-107302.5`.

## Scope

Summing constituentwise by the triangle inequality may pay the rank of the
augmentation object. The desired global theorem must retain the object and its
cohomology before taking absolute values. This lemma does not prove the
number-field estimate or principal binding.
