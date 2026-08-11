# R-90410 — The Möbius innovation is not minimized by random or positive Euler signs

Claim ID: `R-90410`  
Status: **EXACT FINITE REFUTATION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90410`  
Scope: blocks a unit-constant/random-mean extremality shortcut; it does not refute a more delicate deterministic comparison

At parent \(N=4\), let \(a=\log2\), \(b=\log3\), and retain the
complete three nontrivial carry rows. For prime signs
\(\varepsilon_2,\varepsilon_3\), `L-90410` gives

\[
I_\varepsilon(4,1)=I_\varepsilon(4,3)
=(6-\varepsilon_2)a,
\]

\[
I_\varepsilon(4,2)=6a-\varepsilon_3b.
\]

Therefore the normalized complete-row energy is

\[
\mathcal E_4(\varepsilon)
=
\frac{
2(6-\varepsilon_2)^2a^2
+(6a-\varepsilon_3b)^2
}{16}.
\tag{R-90410.1}
\]

The Möbius point is
\((\varepsilon_2,\varepsilon_3)=(-1,-1)\). The all-positive point satisfies

\[
\boxed{
\mathcal E_4(-1,-1)-\mathcal E_4(1,1)
=
3a^2+\frac32ab>0.
}
\tag{R-90410.2}
\]

Moreover the uniform Rademacher mean obeys

\[
\boxed{
\mathcal E_4(-1,-1)
-\mathbb E_\varepsilon\mathcal E_4(\varepsilon)
=
\frac32a^2+\frac34ab>0.
}
\tag{R-90410.3}
\]

Hence neither

\[
\mathcal E_\mu\le\inf_\varepsilon\mathcal E_\varepsilon
\]

nor the unit-constant comparison

\[
\mathcal E_\mu\le\mathbb E_\varepsilon\mathcal E_\varepsilon
\]

is valid even at the first nontrivial endpoint.

This does not rule out a scale-dependent multiplicative comparison, an
opposite-parity theorem after additional exact recombination, or the actual
deterministic PIG. It rules out the simplest attempt to specialize the random
theorem by extremality.
