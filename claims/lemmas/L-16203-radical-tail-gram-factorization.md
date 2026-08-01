# L-16203 — Exact radical-tail Gram factorization reduces the relative sandwich to boundary scalarization

Claim ID: `L-16203`  
Status: **PROVED ABSTRACT FORM IDENTITY; BOUNDARY SCALARIZATION OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-15102`, `L-16201`, `L-16202`

## 1. Motivation

The requested estimate appears impossibly strong when written as an absolute
operator approximation:

```text
||A_lambda-sigma_lambda G_lambda-a_lambdaD_lambda||
 =o(a_lambda d_8/lambda^(2tau)).                         (L-16203.1)
```

For an exact radical source family there is a better formulation. The small
factor `d_8` is already carried by the norm of the omitted prolate tails. One
only needs the Weil form, restricted to the **normalized tail space**, to become
asymptotically scalar. This is a relative `o(1)` theorem rather than an absolute
superexponential estimate.

## 2. Abstract setup

Let `H` be a Hilbert space, let `q` be a Hermitian form on a common domain, and
let `S` be a finite-dimensional source coefficient space. Let

```text
J:S -> Dom(q)                                               (L-16203.2)
```

have range in the radical of the full form:

```text
q(Js,x)=0
for every s in S and every admissible x.                   (L-16203.3)
```

Let `P` be an orthogonal localization/projection on `H`, and define

```text
L=PJ,
T=(I-P)J.                                                   (L-16203.4)
```

Thus `Js=Ls+Ts` is the exact global source, `Ls` is retained, and `Ts` is the
omitted tail.

Define forms on `S` by

```text
A_S(s,t)=q(Ls,Lt),                                         (L-16203.5)
D_T(s,t)=<Ts,Tt>_H.                                        (L-16203.6)
```

## 3. Exact tail factorization

For every `s,t in S`,

```text
boxed:
A_S(s,t)=q(Ts,Tt).                                         (L-16203.7)
```

Equivalently, in form notation,

```text
boxed:
A_S=T^* q T.                                               (L-16203.8)
```

Likewise, the ordinary leakage Gram is

```text
D_T=T^*T.                                                   (L-16203.9)
```

Thus every affine comparison on the source block is exactly a comparison of
two forms on the omitted tails.

## 4. Scalarization theorem

Suppose there are real `a` and `epsilon>=0` such that on the tail range

```text
T(S) subset Dom(q)
```

one has

```text
|q(x,y)-a<x,y>|
 <=epsilon ||x|| ||y||,
x,y in T(S).                                               (L-16203.10)
```

Then

```text
boxed:
-epsilon D_T <= A_S-aD_T <=epsilon D_T.                   (L-16203.11)
```

In particular, for every positive source Gram `G_S`,

```text
boxed:
||A_S-aD_T||_(G_S)
 <=epsilon ||D_T||_(G_S).                                 (L-16203.12)
```

If `S_lambda` is a fixed low-mode sector for which

```text
||D_T||_(G_S) <=(C+o(1))d_8(lambda),                      (L-16203.13)
```

then

```text
lambda^(2tau)
 ||A_S-aD_T||_(G_S)/(a d_8)
 <=(C+o(1)) lambda^(2tau) epsilon/a.                      (L-16203.14)
```

Consequently the requested sector remainder follows from the much more natural
boundary theorem

```text
boxed:
lambda^(2tau_lambda) epsilon_lambda/a_lambda ->0.         (L-16203.15)
```

No superexponential absolute estimate remains: `d_8` is supplied automatically
by the tail Gram.

## 5. Proof

Since `Js=Ls+Ts` and the range of `J` is radical,

```text
0=q(Js,Jt)
 =q(Ls,Lt)+q(Ls,Tt)+q(Ts,Lt)+q(Ts,Tt).                   (L-16203.16)
```

Radicality in the first slot gives

```text
0=q(Js,Lt)=q(Ls,Lt)+q(Ts,Lt),                            (L-16203.17)
```

and radicality in the second slot, by Hermitian symmetry, gives

```text
0=q(Ls,Jt)=q(Ls,Lt)+q(Ls,Tt).                            (L-16203.18)
```

Substituting either pair into (L-16203.16) yields

```text
q(Ls,Lt)=q(Ts,Tt),
```

proving (L-16203.7)--(L-16203.8).

For a coefficient vector `s`, apply (L-16203.10) with `x=y=Ts`:

```text
|A_S(s,s)-aD_T(s,s)|
 <=epsilon D_T(s,s).                                     (L-16203.19)
```

This is exactly the Loewner inequality (L-16203.11). Whitening by `G_S` gives

```text
||G_S^(-1/2)(A_S-aD_T)G_S^(-1/2)||
 <=epsilon
   ||G_S^(-1/2)D_TG_S^(-1/2)||,
```

which proves (L-16203.12). Equations (L-16203.13)--(L-16203.15) follow
immediately. QED.

## 6. Approximate radical version

If the source map is not exactly radical, define the full defect form

```text
C_S(s,t)=q(Js,Jt).                                        (L-16203.20)
```

The same expansion gives

```text
A_S(s,t)
 =q(Ts,Tt)+C_S(s,t)-q(Js,Tt)-q(Ts,Jt).                   (L-16203.21)
```

Thus the production remainder separates into:

```text
boundary scalarization error,
full-source radical defect,
two source-tail cross defects.                            (L-16203.22)
```

For an exact radical source all three extra terms vanish identically. For the
moving prolate source they must be kept correlated; bounding them separately
may lose the mode hierarchy.

## 7. Relation to the prolate defect

For the standard pair of time and frequency projections, the concentration
defect on an exact prolate eigenmode equals the squared norm of its omitted
component. Therefore, after the exact source adapter is fixed, the matrix
`D_T=T^*T` is the natural object to compare with the prolate defect matrix.

This identification is **not automatic** through the nonlinear arithmetic map
`E`. A production theorem must prove one of:

```text
D_T = D_lambda exactly,                                   (L-16203.23)
```

or

```text
||D_T-D_lambda||_(G_S)=o(d_8/lambda^(2tau)).              (L-16203.24)
```

The theorem then combines with (L-16203.15).

## 8. New exact analytic target

The positive route is reduced to two relative boundary statements on the
constrained low source sector:

```text
A. tail-metric identification:
   D_T = D_lambda + o(d_8/lambda^(2tau));

B. boundary Weil scalarization:
   q|_(T(S_lambda))
    =a_lambda <.,.>
     +o(a_lambda/lambda^(2tau))                           (L-16203.25)
```

in operator norm after normalizing the tail vectors.

These are strictly more plausible than the ambient full-space sandwich:

- the tail sector has fixed small dimension;
- all vectors share the same boundary scale;
- the superexponential concentration defect has already been factored out;
- prime and archimedean terms remain combined inside `q` before norms are taken.

## 9. Proof boundary

The exact factorization and scalarization implication are proved. The actual
CCM prolate source is not shown here to be an exact radical family, the tail
Gram is not yet identified with `I-K_lambda` after the `E` map, and the boundary
Weil scalarization estimate (L-16203.25B) remains open. No RH proof is claimed.
