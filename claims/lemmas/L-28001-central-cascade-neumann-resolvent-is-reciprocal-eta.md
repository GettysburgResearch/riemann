# L-28001 — The central cascade Neumann resolvent is reciprocal eta

Claim ID: `L-28001`  
Title: The complete all-stage central carry cascade has coefficientwise resolvent `1/eta(s)`, with an explicit dyadic Möbius inverse  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-27701/L-27702` only for the central residual notation  
Scope: exact Dirichlet-convolution and causal-resolvent algebra; no positivity or RH claim

## 1. Central residual coefficients

Let

\[
 e(n)=(-1)^{n-1}
 \qquad(n\ge1)
\]

be the coefficient sequence of the Dirichlet eta function

\[
 \eta(s)=\sum_{n\ge1}e(n)n^{-s}.
\]

Put

\[
 a(1)=0,
 \qquad
 a(n)=(-1)^n\quad(n\ge2).
\tag{L-28001.1}
\]

Then, in the Dirichlet-convolution algebra,

\[
 \boxed{a=\varepsilon-e,}
\tag{L-28001.2}
\]

where `epsilon` is the unit mass at one.  Hence, initially for `Re(s)>1`,

\[
 \boxed{
 A(s):=\sum_{n\ge1}a(n)n^{-s}=1-\eta(s).
 }
\tag{L-28001.3}
\]

The logarithmic central residual operator is exactly convolution by `a`:

\[
 (\mathcal UF)(t)
 =\sum_{n\ge2}a(n)F(t-\log n)
 =\sum_{k\ge1}
   [F(t-\log(2k))-F(t-\log(2k+1))].
\tag{L-28001.4}
\]

## 2. Iterates and coefficientwise resolvent

For every integer `j>=0`,

\[
 \boxed{
 \mathcal U^jF(t)
 =\sum_{n\ge1}a^{*j}(n)F(t-\log n),
 }
\tag{L-28001.5}

where `a^(*0)=epsilon`.

Since every factor in the support of `a` is at least two,

\[
 a^{*j}(n)=0
 \qquad\text{whenever }2^j>n.
\tag{L-28001.6}

Therefore the formal Neumann series

\[
 \boxed{
 b:=\sum_{j\ge0}a^{*j}
 }
\tag{L-28001.7}

is coefficientwise finite.  It satisfies exactly

\[
 (\varepsilon-a)*b
 =e*b
 =\varepsilon.
\tag{L-28001.8}

Thus `b` is the Dirichlet-convolution inverse of the eta coefficients.  No
analytic convergence argument is needed for this coefficient identity.

Taking Dirichlet series in `Re(s)>1` gives

\[
 \boxed{
 \sum_{n\ge1}{b(n)\over n^s}
 ={1\over\eta(s)}.
 }
\tag{L-28001.9}

Equivalently,

\[
 {1\over\eta(s)}
 ={1\over(1-2^{1-s})\zeta(s)}.
\tag{L-28001.10}

## 3. Explicit inverse coefficients

In the absolute-convergence half-plane,

\[
 {1\over1-2^{1-s}}
 =\sum_{j\ge0}2^j(2^j)^{-s}.
\]

Convolving with the coefficients of `1/zeta(s)` gives

\[
 \boxed{
 b(n)=\sum_{2^j\mid n}2^j\mu(n/2^j).
 }
\tag{L-28001.11}

Write

\[
 n=2^r m,
 \qquad m\text{ odd}.
\]

Then

\[
 \boxed{
 b(n)=
 \begin{cases}
 \mu(m),&r=0,\\[1mm]
 2^{r-1}\mu(m),&r\ge1,
 \end{cases}}
\tag{L-28001.12}

with the usual convention that `mu(m)=0` when `m` is not squarefree.

Hence the complete central resolvent is not an unsigned smoothing.  It is a
very explicit dyadically weighted odd-part Möbius state.

## 4. Exact causal all-stage solution

Let `F` vanish on `(-infinity,0)`.  At every fixed `t`, only integers
`n<=e^t` can contribute.  Consequently

\[
 \boxed{
 (\mathcal RF)(t)
 :=\sum_{j\ge0}\mathcal U^jF(t)
 =\sum_{n\le e^t}b(n)F(t-\log n)
 }
\tag{L-28001.13}

is a finite sum and obeys the exact renewal equation

\[
 \boxed{
 (I-\mathcal U)\mathcal RF=F.
 }
\tag{L-28001.14}

Thus the proposed infinite central carry cascade is literally the causal
`1/eta` resolvent.

## 5. The first mixed-radix obstruction

The stage decomposition at `n=6` is

\[
 a(6)=1,
 \qquad
 a^{*2}(6)=a(2)a(3)+a(3)a(2)=-2,
\]

and higher powers vanish at six.  Hence

\[
 \boxed{b(6)=1-2=-1,}
\tag{L-28001.15}

agreeing with (L-28001.12).  The first failure of pure central monotonicity is
therefore not an accidental endpoint perturbation: it is the first visible
odd-part Möbius sign in the full eta resolvent.

## 6. Strip-sensitive consequence

The finite Euler factor

\[
 1-2^{1-s}
\]

has zeros only on `Re(s)=1`.  Therefore every zero of `zeta(s)` in

\[
 {1\over2}<\operatorname{Re}s<1
\]

is an uncancelled pole of `1/eta(s)`.

Any theorem proving a cofinal subpower bound for the complete central-resolvent
state, or an all-stage positive cascade with subpower repair debt, is therefore
genuinely strip sensitive.  It cannot follow from a phase-blind estimate of the
lattice commutator alone.

This identifies the exact bridge to the repository's dyadic Möbius, reflected
Selberg, balanced Type-II, and first-cell Mertens programmes.

## 7. Proof boundary

Closed exactly:

- the central residual coefficient sequence;
- every iterate as a Dirichlet-convolution power;
- coefficientwise finiteness of the Neumann resolvent;
- the reciprocal-eta transform;
- the explicit dyadic Möbius coefficients;
- the causal all-stage renewal equation;
- the product-six mutation.

Open:

- a positive or subpower-debt realization of the full resolvent;
- a reflected source-specific contraction;
- RH.
