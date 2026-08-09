# L-32418 — Simple radix-four sources form a tight frame for the ordinary pole current

Claim ID: `L-32418`  
Title: Convolving the already-formed ordinary reflected zeta identity by two complementary radix-four sources produces an exact gauge-free tight frame of the RH-sensitive logarithmic-derivative current  
Status: **PROPOSED COMPLETE EXACT SOURCE-ORDER / PHYSICAL-FRAME LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: ordinary reflected Selberg identity; PR #241 independent-frequency physical localization  
Scope: exact filtered ordinary current and reflected identities; no upper energy estimate or RH conclusion

## 1. Source order is load bearing

Let

\[
 B_0(s)=\frac1{\zeta(s)},
 \qquad
 L_0(s)=-\frac{\zeta'}\zeta(s),
 \qquad
 q_0=B_0L_0=B_0'.
\]

Let `Lambda` and

\[
 C=\Lambda\log+\Lambda*\Lambda
\]

be the ordinary von Mangoldt and Selberg sequences.

Define the two finite inverse-zeta sources

\[
\boxed{
 b_\pm=(\varepsilon\pm4\delta_4)*\mu,
 \qquad
 B_\pm(s)=\frac{1\pm4^{1-s}}{\zeta(s)}.
}
\tag{L-32418.1}
\]

In this lemma the Dirichlet system remains the **ordinary zeta system**. The sources `b_\pm` are applied only after the ordinary Selberg/reflected identity has been formed.

Define the filtered ordinary currents

\[
\boxed{
 r_\pm=b_\pm*\Lambda.
}
\tag{L-32418.2}
\]

Their Dirichlet series are therefore

\[
\boxed{
 R_\pm(s)
 =(1\pm4^{1-s})q_0(s).
}
\tag{L-32418.3}

There is no derivative of the finite filter in (L-32418.3). This is different from the currents `q_\pm=B_\pm'` of `L-32416` and is the reason the frame below is gauge free.

## 2. Exact critical tight frame

On `s=1/2+it`, put

\[
 a=4^{1-s},\qquad |a|=2.
\]

Then

\[
 |1-a|^2+|1+a|^2=10.
\]

Multiplying by `|q_0|^2` gives the pointwise vertical identity

\[
\boxed{
 |R_-(1/2+it)|^2+|R_+(1/2+it)|^2
 =10|q_0(1/2+it)|^2.
}
\tag{L-32418.4}

After multiplication by any common safe physical window and Plancherel, the same equality holds for the complete all-line physical energies. On a finite block aligned to `log 4`, the only differences are the explicit finite filter collars at its two ends; there is no interior frame loss.

Thus the filtered pair contains the complete ordinary RH-sensitive current with an **exact frame constant ten**.

## 3. Source-convolved ordinary reflected identities

For independent twists `t,u`, the ordinary reflected Selberg identity is

\[
 C_{t,-u}-C_t-C_{-u}=2\Lambda_t*\Lambda_{-u}.
\tag{L-32418.5}
\]

Convolve the complete identity, for each sign separately, by

\[
 b_{\pm,t}*b_{\pm,-u}.
\]

Associativity gives

\[
\boxed{
 (b_{\pm,t}*b_{\pm,-u})*
 (C_{t,-u}-C_t-C_{-u})
 =2r_{\pm,t}*r_{\pm,-u}.
}
\tag{L-32418.6}

The right side is exactly the Hermitian current whose critical-line pair energy is (L-32418.4).

Applying PR #241's independent-frequency physical block kernel gives the corresponding exact localized identities with every product and individual term retained.

## 4. Bare source fields are finite and deterministic

The atomized carry multiplier contributes one factor `zeta(s)N_theta(s)`. Hence

\[
\boxed{
 \zeta(s)N_\theta(s)B_\pm(s)
 =(1\pm4^{1-s})N_\theta(s).
}
\tag{L-32418.7]

(The closing bracket in the tag is typographical only.)

Thus the bare source leg in each individual reflected term is a deterministic two-tap field. In particular, the exact individual-term factorization of PR #337 `L-32710` has no diffuse inverse-zeta boundary in this formulation.

The higher leg remains `b_\pm*C`; no estimate for that leg is asserted here.

## 5. Exact source reconstruction

The sources reconstruct the ordinary inverse-zeta coefficient sequence at zero delay:

\[
\boxed{
 \mu=\frac{b_-+b_+}{2}.
}
\tag{L-32418.8}

Likewise the filtered ordinary currents reconstruct

\[
\boxed{
 q_0=\frac{r_-+r_+}{2}.
}
\tag{L-32418.9}

Equation (L-32418.4) is substantially sharper than the Cauchy bound obtained from (L-32418.9): the full pair energy is known exactly, not merely bounded.

## 6. Relation to the separate-system pair of L-32416

Two superficially similar constructions must not be conflated:

```text
L-32416:
    B_\pm are treated as two Dirichlet systems;
    generalized primes Lambda_\pm differ;
    their exact orthogonalization gives the positive paired reserve L-32417;

this lemma:
    the Dirichlet system is ordinary zeta;
    both channels use the same ordinary Lambda and C;
    b_\pm are external source filters;
    the RH current frame is exactly gauge-free.
```

A future completion may combine the positive reserve information of the first construction with the exact pole-current frame of the second only after writing an explicit source-convolved congruence. It may not identify the two by notation alone.

## 7. Proof boundary

Closed exactly:

1. gauge-free filtered ordinary currents;
2. pointwise critical tight-frame identity;
3. exact source-convolved reflected identities;
4. deterministic two-tap bare physical legs;
5. zero-delay coefficient and current reconstruction;
6. source-order distinction from `L-32416/L-32417`.

Open:

1. a source-complete upper/dissipative estimate for the two filtered reflected product blocks;
2. a rigorous congruence importing a positive Selberg reserve into those blocks without changing source order;
3. RH.
