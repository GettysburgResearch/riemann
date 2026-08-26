# Growing marked-place interferometry in the quadratic quintic family

Status: **exact stable exterior-character selection rules and a uniform
`(q,m)` Hasse-envelope phase diagram; no sharpness, distribution,
individual L-function zero, RH, or GRH claim**

Bounded replay:
[`quadratic_quintic_growing_marked_place_phase_diagram.py`](quadratic_quintic_growing_marked_place_phase_diagram.py).

## 0. Outcome

The fixed-`m` six-place theorem extends to a stable all-`m` character law,
and that law has a genuine growing-mark transition.

Let `q` be an odd prime power, let `A` be a set of `m` distinct rational
places in `F_q`, let

\[
 R_{5,m}(A)=
 \sum_{D\in\mathcal H_5(q)}\prod_{a\in A}\chi(D(a)),
\tag{0.1}
\]

and let `U_A` be the normalized Frobenius class of the source-convention
curve

\[
 C_A:y^2=\prod_{a\in A}(a-x).
\]

For odd `m>=11`, `U_A` lies in `USp(m-1)` and

\[
 \boxed{
 R_{5,m}
 =-q^{5/2}\chi_{\omega_5}
  -m q^{3/2}\chi_{\omega_3}
  -\binom{m+1}{2}q^{1/2}\chi_{\omega_1}.}
\tag{0.2}

For even `m>=12`, `U_A` lies in `USp(m-2)` and

\[
 \boxed{
\begin{aligned}
 R_{5,m}={}&-q^{5/2}\chi_{\omega_5}
 -q^2\chi_{\omega_4}
 -m q^{3/2}\chi_{\omega_3}\\
 &-m q\chi_{\omega_2}
 -\binom{m+1}{2}q^{1/2}\chi_{\omega_1}
 -\binom{m+1}{2}.
\end{aligned}}
\tag{0.3}

These are exact identities, not asymptotic decompositions.  The apparently
large polynomial coefficients in the raw multi-place formula have collapsed
into one copy of each stable fundamental exterior channel.

Since

\[
 \dim\chi_{\omega_k}^{\operatorname{USp}(2g)}
 =\binom{2g}{k}-\binom{2g}{k-2},
\tag{0.4}

the normalized correlation satisfies, uniformly for `11<=m<=q`,

\[
 \boxed{
 { |R_{5,m}(A)|\over q^4(q-1)}
 \ll \min\{1,m^5q^{-5/2}\}.}
\tag{0.5}

Thus

\[
 m=o(\sqrt q)
 \quad\Longrightarrow\quad
 \sup_{|A|=m}{|R_{5,m}(A)|\over|\mathcal H_5(q)|}=o(1).
\tag{0.6}

At `m` of order `sqrt(q)`, the compact-character envelope stops forcing
decay.  This is an upper-bound transition, not a theorem that a correlation
of constant size is attained.

At the opposite extreme `m=q`, the envelope is maximally uninformative—but
the exact answer is zero.  The full-place auxiliary curve
`y^2=x-x^q` has an even zeta numerator, so every odd exterior character in
(0.2) vanishes.  This supplies an exact exceptional endpoint beyond the
generic phase diagram and makes the noncommutation of the `m` and `q` limits
concrete.

## 1. Stable decomposition from the locked coefficient identity

Write

\[
 P_A(u)=\det(1-\sqrt q,U_Au)
 =\sum_jp_ju^j,
 \qquad
 p_j=(-1)^jq^{j/2}e_j(U_A).
\tag{1.1}

The exact degree-five multi-place theorem gives

\[
 R_{5,m}
 =\left(\binom{m+1}{2}-qm\right)\ell_1
 +(m-q)\ell_3+\ell_5.
\tag{1.2}

For odd `m`, infinity is ramified and `L_A=P_A`, so

\[
 \ell_j=p_j.
\]

Put `C_m=binom(m+1,2)`.  Substitution in (1.2) and collection by Frobenius
weight gives

\[
 R_{5,m}
 =q^{5/2}(e_3-e_5)
  +m q^{3/2}(e_1-e_3)
  -C_mq^{1/2}e_1.
\tag{1.3}

In stable rank `g>=5`,

\[
 e_k-e_{k-2}=\chi_{\omega_k}.
\tag{1.4}

Hence `e_3-e_5=-chi_(omega_5)`,
`e_1-e_3=-chi_(omega_3)`, and `e_1=chi_(omega_1)`.  This proves (0.2).

For even `m`, infinity splits and

\[
 L_A(u)=(1-u)P_A(u).
\]

Therefore

\[
 R_{5,m}
 =(C_m-qm)(p_1-p_0)
 +(m-q)(p_3-p_2)+(p_5-p_4).
\tag{1.5}

Separating odd and even Frobenius weights yields

\[
\begin{aligned}
R_{5,m}={}&q^{5/2}(e_3-e_5)
 +q^2(e_2-e_4)
 +m q^{3/2}(e_1-e_3)\\
&-m q e_2-C_mq^{1/2}e_1+qm-C_m.
\end{aligned}
\tag{1.6}

Use (1.4), together with

\[
 e_2=\chi_{\omega_2}+1.
\]

The scalar `-mq` from that substitution cancels the displayed `+qm`.
Equation (0.3) follows.

The replay substitutes arbitrary labelled values for `e_1,...,e_5` in both
parities and verifies (1.3) and (1.6) over 60 exact integer rows.  These rows
check algebra only; the proof is the symbolic collection above.

## 2. The uniform Hasse envelope

Every compact-group character obeys

\[
 |\chi_{\omega_k}(U)|\le\dim\chi_{\omega_k}.
\]

For the auxiliary curves, `2g=m-1` in odd degree and `2g=m-2` in even
degree.  Equation (0.4) therefore gives

\[
 \dim\chi_{\omega_k}=O_k(m^k).
\tag{2.1}

The first term in (0.2)--(0.3) has raw envelope
`O(q^(5/2)m^5)`.  The remaining terms have envelopes

\[
 O(q^2m^4),\quad O(q^{3/2}m^4),\quad
 O(qm^3),\quad O(q^{1/2}m^3),\quad O(m^2).
\tag{2.2}

Under the geometric feasibility condition `m<=q`, every term in (2.2) is
bounded by the first scale up to an absolute constant.  Division by the
exact family size

\[
 |\mathcal H_5(q)|=q^4(q-1)
\]

and comparison with the trivial correlation bound one proves (0.5).

If `m=q^gamma`, the leading character envelope has exponent

\[
 q^{-5/2+5\gamma}.
\tag{2.3}

It decays for `gamma<1/2`, becomes order one at the formal boundary
`gamma=1/2`, and must be replaced by the trivial bound beyond it.  This is
the marked-place analogue of a growing-rank boundary layer: fixed-rank Hasse
control is not uniform across all apertures.

## 3. The full-aperture endpoint is an exact null stratum

Set `A=F_q`, so `m=q`.  The companion full-place theorem proves

\[
 P_A(u)=(1+s_qqu^2)^{(q-1)/2}.
\tag{3.1}

Hence every odd elementary symmetric function vanishes:

\[
 e_1(U_A)=e_3(U_A)=e_5(U_A)=0.
\]

For `q>=11`, this is equivalently

\[
 \chi_{\omega_1}(U_A)
 =\chi_{\omega_3}(U_A)
 =\chi_{\omega_5}(U_A)=0.
\tag{3.2}

Since `q` is odd, the relevant stable formula is (0.2), and (3.2) makes its
right side zero term by term.  For all odd prime powers, including the small
ranks, the even generating series proves the same exact correlation zero.

Thus the endpoint does not saturate (0.5).  It lies on a special
supersingular exterior-null stratum.  A typical growing-mark family and the
complete-place configuration must not be conflated.

## 4. Interpretation and claim boundary

The phase diagram adds three pieces of experimental guidance.

1. Fixed-`m` Hasse envelopes remain uniform for `m=o(sqrt(q))`.
2. Near `sqrt(q)`, detector size and auxiliary genus compete; compact
   dimension alone no longer proves decorrelation.
3. At full aperture, extra geometry can restore exact cancellation far
   beyond the generic envelope.

This is precisely the kind of noncommuting `(q,g,m)` behavior that raw
fixed-rank moments miss.  It suggests conditioning future marked-place
experiments on the geometry of the place configuration, not only its
cardinality.

Proved exactly:

- the stable character identities (0.2)--(0.3);
- the character-dimension envelope (0.5);
- uniform decorrelation in the regime (0.6);
- compatibility of the full-place zero with the simultaneous exterior-null
  stratum.

Not proved:

- sharpness or attainment of the `sqrt(q)` envelope;
- a distribution theorem for the characters as `m` grows;
- a closed-place or FFPS physical-source realization;
- a memberwise statement, an individual L-function zero, RH, or GRH;
- external novelty or priority.
