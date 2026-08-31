# The exact lower boundary of the pair occupation body

For every feasible pair(A,B), this note determines the smallest possible
C among single monotone pair profiles and constructs the unique
minimizing profile. The objective is the occupation moment C, not the
original physical energy or a retained-gamma moment.

The coordinates are the original source occupations

    A=integral v du, B=integral uv du, C=integral v^2 du.

NATIVE_OCCUPATION_MOMENTS.md at
a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc proves their feasible(A,B)
range. The clipped quadratic minimization principle is already proved
in NATIVE_OCCUPATION_SUPPORT_REDUCTION.md, present at
808a0353e38fa8eaf6b2999bb97426d167ab598d with blob
fe9880eca9b21ef72586fb5ed4770e910630dcde. The contribution here is its
complete fixed-moment specialization, including all transition curves,
closed values and degenerate endpoints. No new numerical discovery is
claimed.

## 1. Feasibility and the complete formula

Write v=f(u) along u-time, ignoring vertical segments of zero du mass.
The feasible range is exactly

    0<=A<=1,  A/2<=B<=A-A^2/2.                            (1)

Necessity is Chebyshev's inequality and the final-interval rearrangement.
For sufficiency, the constant profile A and the threshold
1_{u>=1-A} both have mass A; convex combinations of those two profiles
are legal and fill the interval of B in(1).

At A=0 the only profile is0 almost everywhere and C_min=0. At A=1 it
is1 almost everywhere, B=1/2 and C_min=1. Henceforth let0<A<1 and put

    d=B-A/2,   B_max=A-A^2/2,
    B_0=A/2+min(A,1-A)/6,
    B_1= A-2A^2/3                 if A<=1/2,
         1/2-2(1-A)^2/3           if A>=1/2.              (2)

These satisfy A/2<=B_0<=B_1<B_max. The two definitions of B_1 agree
at A=1/2, where B_0=B_1=1/3. The complete lower envelope is:

| Regime | Range | C_min |
| --- | --- | --- |
| No clipping | A/2<=B<=B_0 | A^2+12(B-A/2)^2 |
| Lower clipping only | A<1/2 and B_0<=B<=B_1 | 4A^3/[9(A-B)] |
| Upper clipping only | A>1/2 and B_0<=B<=B_1 | 2A-1+4(1-A)^3/[9(1/2-B)] |
| Both endpoints clipped | B_1<=B<=B_max | A-sqrt((2A-A^2-2B)/3) |

The formulas agree on their shared boundaries. At B=B_max the last
formula is C_min=A and is realized by the threshold1_{u>=1-A}.
At B=A/2 the first formula is C_min=A^2 and is realized by the constant
profile A. No denominator in the one-clipping rows vanishes in its
stated range.

## 2. The source profiles and their transition curves

In the no-clipping region define

    f(u)=A-6d+12du.                                      (3)

Its endpoint values are A-6d and A+6d. Thus it lies in[0,1] precisely
when d<=min(A,1-A)/6. Direct integration gives the first row of the
table and the prescribed A,B. Its slope is nonnegative.

For A<1/2 in the lower-clipping region put

    L=3(A-B)/A,  t=1-L=3B/A-2,
    f(u)=(2A/L^2)(u-t)_+.                              (4)

Here2A<=L<=1, so t>=0 and the terminal height2A/L is at most1.
Its moments are

    integral f=A,
    integral u f=A(1-L/3)=B,
    integral f^2=4A^2/(3L)=4A^3/[9(A-B)].              (5)

The lower clip first appears at L=1, or B=2A/3=B_0. Its terminal
height reaches1 at L=2A, or B=A-2A^2/3=B_1. These are exactly the
two stated transition curves.

The upper-clipping region is obtained by the involution

    f'(u)=1-f(1-u),
    A'=1-A, B'=1/2-A+B, C'=1-2A+C.                     (6)

Apply(4) to A',B' and transform back. The resulting profile is
nondecreasing, has only an upper clip, and gives the third row of the
table. In particular its transition curves are
B_0=(2A+1)/6 and B_1=1/2-2(1-A)^2/3.

For both clips, with B<B_max, put

    V=2A-A^2-2B,  L=sqrt(12V),  a=1-A-L/2,
    f(u)=clip_[0,1]((u-a)/L).                          (7)

In this region0<L<=2min(A,1-A), so0<=a<=a+L<=1.
The profile ramps from0 to1 over an interval of length L. Integration
gives

    A=1-a-L/2,
    B=A-A^2/2-L^2/24,
    C=A-L/6=A-sqrt(V/3).                              (8)

At B=B_max, L=0 and(7) is replaced by its threshold limit. At a
one-clip transition L equals2A or2(1-A), so(7) agrees with the
corresponding profile in(4) or(6). At the no-clip transition the
affine pieces also agree. Thus this is one continuous envelope with
four formula regimes, or three clipping types after reflection.

Every profile above is an actual path: draw its nondecreasing graph,
include the initial and final vertical completions, and parameterize
the resulting curve monotonically. These particular paths have
finitely many linear segments. No discontinuous activation in the
original path parameter is required.

## 3. Global minimality and uniqueness

Except for the terminal threshold case, every displayed profile has
the form

    f_*(u)=clip_[0,1](lambda+beta u),  beta>=0,          (9)

and exactly the required A,B. Let g be any measurable function in[0,1]
with the same two moments; it need not even be monotone. The elementary
interval-projection inequality says pointwise

    (f_*-(lambda+beta u))(g-f_*)>=0.

Because the two moment differences vanish, integration yields
integral f_*(g-f_*)>=0. Consequently

    integral g^2-integral f_*^2
       >= integral (g-f_*)^2 >=0.                     (10)

This proves global minimality and uniqueness almost everywhere for
all the nonterminal formulas. Their nonnegative slopes ensure that
the unique boxed minimizer is also admissible as a monotone profile.
Equation(10) gives a quantitative stability statement in u-time,
without identifying that norm with the original physical Hilbert norm.

At B=B_max, the mass-A final-step rearrangement is uniquely optimal
for B. Indeed, with t=1-A and h=1_{u>=t},

    integral (u-t)(g-h)<=0

for every boxed g with mass A. Equality requires g=h almost everywhere
away from the single point t. Thus the threshold is the only feasible
profile at this B and gives C=A. The cases A=0,1 were already settled.

Uniqueness of the profile gives uniqueness of its completed oriented
planar graph, allowing pauses and weak monotone reparametrizations.
It does not determine additional coordinates in a higher-arity source.

The table determines the entire lower boundary in the C direction;
it is not a claim to have determined the upper boundary or every
higher-arity compatibility condition. It can supply exact source
constraints in a physical optimization, but minimizing C alone is
not minimizing the original Gamma-weighted family energy. All source
measure, physical-alias and retained-gamma distinctions remain in force.

This is a proof-only all-parameter result, requiring no new scientific
job or numerical test panel.
