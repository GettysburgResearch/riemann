# L-34410 — The relative compact source has zero deep bare field

Claim ID: `L-34410`  
Title: One further radix-four difference of the compact main-pole source has positive inverse data, a three-tap divisor prefix whose bare physical field vanishes identically on deep balanced rows, and a logarithmic current equal to the aligned compact innovation up to one fixed bare gauge  
Status: **PROPOSED COMPLETE EXACT SOURCE/FIELD THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-34406/L-34409`; elementary Euler algebra and atomized carry switching  
Scope: exact relative source typing and bare-field cancellation; no current upper estimate or RH claim

## 1. Relative compact source

Put

\[
 x=4^{-s}
\]

and retain

\[
 B_\sharp(s)=\frac{1-4x}{\zeta(s)}.
\]

Define

\[
\boxed{
 B_\diamond(s)
 =(1-x)B_\sharp(s)
 =\frac{(1-4^{-s})(1-4^{1-s})}{\zeta(s)}.
}
\tag{L-34410.1}

Its Dirichlet source is

\[
\boxed{
 b_\diamond
 =(\varepsilon-\delta_4)
  *(\varepsilon-4\delta_4)*\mu.
}
\tag{L-34410.2}

The numerator zeros lie only on the boundary lines `Re(s)=0` and `Re(s)=1`; hence no nontrivial zeta-zero pole is cancelled.

## 2. Positive inverse and generalized-prime coefficients

The inverse is

\[
\boxed{
 A_\diamond(s)
 =\frac{\zeta(s)}{(1-4^{-s})(1-4^{1-s})}.
}
\tag{L-34410.3}

Both extra local factors have geometric series with positive coefficients. Therefore

\[
\boxed{a_\diamond(n)>0}
\tag{L-34410.4}

for every positive integer `n`.

The generalized-prime sequence is

\[
\boxed{
 \Lambda_\diamond
 =\Lambda
  +L\sum_{r\ge1}(1+4^r)\delta_{4^r},
 \qquad L=\log4,
}
\tag{L-34410.5}

so

\[
\boxed{\Lambda_\diamond(n)\ge0.}
\tag{L-34410.6}

Thus the relative source retains the standard positive-inverse/nonnegative-generalized-prime structure.

## 3. Three-tap divisor prefix

Since

\[
 \mathbf1*\mu=\varepsilon,
\]

one has exactly

\[
\boxed{
 \mathbf1*b_\diamond
 =(\varepsilon-\delta_4)
  *(\varepsilon-4\delta_4)
 =\varepsilon-5\delta_4+4\delta_{16}.
}
\tag{L-34410.7}

Let

\[
 H_\diamond(N)
 =\sum_{m\le N}(\mathbf1*b_\diamond)(m).
\]

Then

\[
\boxed{
 H_\diamond(N)
 =\begin{cases}
 0,&N=0,\\
 1,&1\le N<4,\\
 -4,&4\le N<16,\\
 0,&N\ge16.
 \end{cases}}
\tag{L-34410.8}

In particular the divisor-prefix state has compact support in the parent variable.

## 4. Exact vanishing of the deep bare carry field

For an integer split `n=j+k`, the bare carry image is

\[
 Y_\diamond(n,j)
 =H_\diamond(n)-H_\diamond(j)-H_\diamond(k).
\]

Hence whenever

\[
\boxed{j\ge16,\qquad k\ge16,}
\tag{L-34410.9}

one has

\[
\boxed{Y_\diamond(n,j)=0.}
\tag{L-34410.10}

The same statement holds in the centered-interval physical coordinate. Indeed the atomized bare field is the prefix defect

\[
 H_\diamond(X)-H_\diamond(\theta X)
 -H_\diamond((1-\theta)X),
\]

with the standard floor convention. Therefore for every fixed `eta>0`, once

\[
X\ge16/\eta,
\qquad
\eta\le\theta\le1-\eta,
\]

all three arguments lie in the zero region of (L-34410.8), and

\[
\boxed{
 \mathcal P_{B_\diamond}(X,\theta)=0
}
\tag{L-34410.11}

exactly, not merely asymptotically.

Thus both source-convolved **individual** reflected terms, which factor through the bare field, vanish on every deep balanced block for this source.

## 5. Relation of its current to the aligned compact innovation

Let

\[
 q_\sharp=B_\sharp'
\]

be the hard compact current and

\[
 q_\diamond=B_\diamond'.
\]

Since `x'=-(log4)x`, differentiating (L-34410.1) gives

\[
\boxed{
 q_\diamond
 =(1-x)q_\sharp
  +LxB_\sharp.
}
\tag{L-34410.12}

At coefficient level,

\[
\boxed{
 q_\diamond
 =(\varepsilon-\delta_4)*q_\sharp
  +L\delta_4*b_\sharp.
}
\tag{L-34410.13}

Evaluate on an aligned row `e+=(4n,4j)`.  The first term gives

\[
 \mathcal L_{e^+}((\varepsilon-\delta_4)q_\sharp)
 =Q_\sharp(e^+)-Q_\sharp(e)
 =I_\sharp(e).
\]

On every deep balanced row `L-34409` gives

\[
 \mathcal L_e(b_\sharp)=3.
\]

Therefore

\[
\boxed{
 Q_\diamond(e^+)
 =I_\sharp(e)+3L.
}
\tag{L-34410.14}

Equivalently,

\[
\boxed{
 I_\sharp(e)=Q_\diamond(e^+)-3\log4.
}
\tag{L-34410.15}

The fixed gauge has no scale growth. Thus a critical bound for the own current of `B_diamond` is equivalent, up to an absolute additive constant, to the critical bound needed in the compact recurrence.

## 6. Reflected simplification

For a general inverse-zeta source, PR #337 `L-32710` identifies the two individual source-convolved reflected Selberg terms as physical cross-inner-products with the bare source field.

Equation (L-34410.11) therefore gives, on every sufficiently deep balanced physical block,

\[
\boxed{
 \mathfrak B_I(B_\diamond C_\diamond,B_\diamond)=0,
}
\tag{L-34410.16}

and similarly for the reflected conjugate term.

Hence the complete source-convolved reflected identity simplifies there to

```text
product-source block
    = 2 * current normal Gram.
```

No unweighted/bare boundary survives in the balanced interior.

This equality is not yet an upper estimate: the product-source block still carries the same RH-sensitive current information. The theorem removes the individual boundary terms exactly but does not declare the remaining product block soft.

## 7. Consequence for the proof search

The hard aligned compact innovation can now be attacked through a source with all of the following simultaneous properties:

```text
finite zero-safe numerator;
positive Dirichlet inverse;
nonnegative generalized primes;
three-tap divisor prefix;
zero bare field on every deep balanced row;
current = aligned compact innovation + fixed constant gauge;
reflected individual terms = exactly zero in the deep balanced block.
```

This is a strictly cleaner source than either the denominator-bearing Q=4 all-pass source or the one-step compact source for the final reflected estimate.

The remaining theorem is correspondingly sharp:

> bound the source-convolved **product** block of `B_diamond` at the critical `n log^A n` scale (equivalently, bound its current normal Gram), using the positive inverse/generalized-prime structure and the critical reserve increments developed on the Q4 branches.

## 8. Proof boundary

Closed exactly here:

1. relative source and zero-safe pole retention;
2. positive inverse and nonnegative generalized-prime coefficients;
3. three-tap divisor-prefix collapse;
4. exact vanishing of the deep bare carry/physical field;
5. exact current relation to the compact aligned innovation;
6. exact disappearance of both reflected individual terms in the deep balanced block.

Still open:

1. critical upper estimate for the product/current block;
2. coefficient-one recurrence;
3. RH.
