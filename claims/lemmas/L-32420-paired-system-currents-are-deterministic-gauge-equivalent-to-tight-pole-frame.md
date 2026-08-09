# L-32420 — Paired system currents are deterministic-gauge equivalent to the tight ordinary pole frame

Claim ID: `L-32420`  
Title: The two currents carrying the positive paired reserve differ from the gauge-free tight radix-four frame of the ordinary reciprocal-zeta current by one explicit deterministic two-tap field, so the two current pairs have exactly the same exponential energy status  
Status: **PROPOSED COMPLETE EXACT CURRENT-CONGRUENCE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32416/L-32418`; atomized carry physical localization  
Scope: current/source congruence and block routing; no dissipative upper estimate or RH conclusion

## 1. The two current pairs

Retain

\[
 B_0=1/\zeta,
 \qquad q_0=B_0',
\]

and put

\[
 a(s)=4^{1-s},
 \qquad L=\log4,
 \qquad F_\pm=1\pm a.
\]

There are two different current pairs in `L-32416` and `L-32418`.

The **separate-system currents** are

\[
 q_\pm^{\rm sys}=B_\pm'= (F_\pm B_0)',
\tag{L-32420.1}
\]

and are the currents attached to the positive paired generalized-prime/Selberg reserve of `L-32417/L-32419`.

The **externally filtered ordinary currents** are

\[
 r_\pm=F_\pm q_0,
\tag{L-32420.2}
\]

and form the gauge-free tight pole-current frame of `L-32418`.

## 2. Exact deterministic gauge

Since

\[
 a'(s)=-La(s),
\]

one has

\[
 F_-'=La,
 \qquad F_+'=-La.
\]

Therefore

\[
\boxed{
 q_-^{\rm sys}=r_-+LaB_0,
 \qquad
 q_+^{\rm sys}=r_+-LaB_0.
}
\tag{L-32420.3}
\]

This is an exact identity of Dirichlet series.

After multiplication by the atomized carry factor `zeta(s)N_theta(s)`, the gauge becomes

\[
\boxed{
 \zeta N_\theta\,[LaB_0]
 =LaN_\theta.
}
\tag{L-32420.4}
\]

It contains no zeta factor, reciprocal-zeta factor, prime coefficient, or arithmetic remainder. It is a deterministic one-delay field.

The inverse transform of `N_theta` is the standard atomized carry kernel and has uniformly bounded `L2` norm on every fixed balanced carry-position interval. Hence the gauge contributes only a uniform fixed amount to each logarithmic block.

## 3. Exact aligned-block frame for the externally filtered currents

Use blocks of length

\[
 L=\log4.
\]

Let `u(x)` be the physical ordinary pole current after removal of the common critical carrier. Multiplication by

\[
 a(s)=4^{1-s}
\]

is translation by `L` with critical amplitude `2`. Consequently

\[
 r_-(x)=u(x)-2u(x-L),
 \qquad
 r_+(x)=u(x)+2u(x-L).
\tag{L-32420.5}
\]

Pointwise,

\[
\boxed{
 |r_-(x)|^2+|r_+(x)|^2
 =2|u(x)|^2+8|u(x-L)|^2.
}
\tag{L-32420.6}
\]

For the aligned block

\[
 I_m=[mL,(m+1)L],
 \qquad
 E_m=\int_{I_m}|u(x)|^2dx,
\]

put

\[
 E_m^{\rm ext}
 =\int_{I_m}(|r_-|^2+|r_+|^2)dx.
\]

Then exactly

\[
\boxed{
 E_m^{\rm ext}=2E_m+8E_{m-1}.
}
\tag{L-32420.7]

(The closing bracket in the tag is typographical only.)

This is the block version of the critical vertical frame constant ten.

In the reverse direction

\[
 u={r_-+r_+\over2},
\]

so

\[
\boxed{
 E_m\le\frac12E_m^{\rm ext}.
}
\tag{L-32420.8}

Thus the ordinary pole current and the external pair have exactly the same exponential block-growth exponent.

## 4. Separate-system pair has the same exponent

Let `E_m^sys` be the analogous two-channel block energy of the separate-system currents. From (L-32420.3)--(L-32420.4), the difference vector between the two pairs is

\[
 (G,-G),
 \qquad G=LaN_\theta,
\]

with uniformly bounded block norm.

Therefore

\[
\boxed{
 \left|
 \sqrt{E_m^{\rm sys}}-\sqrt{E_m^{\rm ext}}
 \right|
 \le C
}
\tag{L-32420.9}

for one fixed constant `C` depending only on the chosen carry-position/window normalization.

Consequently

\[
\boxed{
 E_m^{\rm sys}=e^{o(m)}
 \quad\Longleftrightarrow\quad
 E_m=e^{o(m)}.
}
\tag{L-32420.10}

The same equivalence holds for polynomial block bounds.

Thus the pair on which `L-32417/L-32419` prove positive source-complete reserves is not spectrally detached from the ordinary RH pole current: the difference is an explicit deterministic gauge.

## 5. What this removes from the final proof problem

The following source-typing question is closed:

```text
positive paired reserve lives on q_±^sys;
actual RH detector lives on q_0;
are these different arithmetic energy species?
```

Answer: **no at exponential scale**. The exact bridge is

```text
q_±^sys
 = finite tight filters of q_0
 + deterministic gauge.
```

No positive inverse expansion, source-to-edge reconstruction, or asymptotic prime estimate is required for this bridge.

## 6. What remains

This lemma deliberately does not infer an upper energy estimate from reserve positivity. The outstanding statement is now purely the reflected/dissipative one:

> In the complete independent-frequency source-convolved identities for the separate-system pair, prove that the positive paired reserve `L-32417/L-32419` enters the block ledger with the dissipative orientation needed to bound `E_m^sys`, rather than merely appearing as a positive comparison quantity.

If that inequality is produced, (L-32420.10) transfers it immediately to the ordinary reciprocal-zeta pole current and hence to the existing RH criterion.

## 7. Proof boundary

Closed exactly:

1. current-level source-order congruence;
2. deterministic gauge formula;
3. exact aligned-block tight-frame identity;
4. reverse reconstruction bound;
5. equivalence of ordinary and paired-system exponential energy exponents.

Still open:

1. the reflected dissipative block inequality;
2. a polynomial/subexponential paired current-energy theorem;
3. RH.
