# Verified-height closure of the first Xi impedance levels

Date: 2026-08-14  
Branch: `research/gpt56-pro/92200-verified-height-third-order-closure`  
Base: PR #449 at `e67f20803c8bbaa4b33aae366870269e5f560731`  
RH status: **unproved**

## Executive result

The complete-Bernstein programme is advanced in four directions.

1. The reciprocal Xi curvature is rewritten as an exact pairwise dispersion
   over squared zero parameters.
2. The rigorously verified critical-line reserve below height
   `3,000,175,332,800`, together with an explicit local zero-count bound,
   is used to dominate every possible off-line negative interaction in the
   first two nontrivial pairwise dispersions.
3. This gives proposed unconditional closure of all infinitesimal safe Xi
   Caratheodory matrices through three nodes and of all Xi-impedance Loewner
   matrices through two nodes.
4. An exact reciprocal Toeplitz congruence turns every higher Loewner order
   into an ordinary Stieltjes-Hankel determinant of the safe admittance.

The same domination mechanism closes more than `1.5e11` consecutive adjacent
Hankel inequalities.  It does not close higher-rank Hankel determinants or RH.

## I. Pairwise squared-pole identities

Writing

```text
p(t)=sum_alpha w_alpha/(t+s_alpha),
Z(t)=1/p(t),
```

one has exactly

```text
p p''-2(p')^2
 =sum_(alpha,beta) w_alpha w_beta
  (s_alpha-s_beta)^2/[(t+s_alpha)^3(t+s_beta)^3],
```

and

```text
2p'p'''-3(p'')^2
 =6 sum_(alpha,beta) w_alpha w_beta
  (s_alpha-s_beta)^2/[(t+s_alpha)^4(t+s_beta)^4].
```

Real squared poles contribute positively.  A conjugate off-line pair has one
negative internal interaction.

## II. Why the verified height is unexpectedly powerful

Every possible off-line zero has ordinate above

```text
H=3,000,175,332,800.
```

At such heights its squared pole has imaginary-to-real ratio `O(1/H)`.  A
single verified simple critical zero below `H/2` supplies a real anchor whose
positive interaction is of order `b^4`, while all possibly negative local
interactions in a four-unit height packet have total size only
`O(b^2 log b)`.

The explicit inequality

```text
b^2 > 2160 log(b+3)
```

holds with a margin above `1e20` at the verified endpoint.  The analogous
fourth-power inequality has the same margin.  This yields the proposed global
signs

```text
p p''-2(p')^2 > 0,
2p'p'''-3(p'')^2 > 0.
```

## III. Closed low orders

The first identity makes `Z=1/p` strictly concave.  Combined with the exact
three-node determinant factorization from PR #445, it gives proposed
unconditional positivity of every safe infinitesimal Xi Caratheodory packet
of size at most three.

The second identity makes

```text
g(t)=1/sqrt(Z'(t))
```

strictly concave.  Integrating `1/g^2` against the chord gives

```text
[Z(y)-Z(x)]/(y-x) <= sqrt(Z'(x)Z'(y)),
```

so every two-node Loewner matrix of `Z` is proposed positive.

An exact rational control shows the separation is sharp: one lower real
anchor plus one high conjugate pair may have `Z'>0` and `Z''<0` everywhere yet
a strictly negative three-node Loewner determinant.

## IV. Exact all-order coordinate change

Let

```text
A_k=(-1)^k p^(k)/k!,
H_n=(A_(i+j+1))_(0<=i,j<n).
```

The confluent Loewner matrix of `Z=1/p` is exactly congruent to `H_n` through
an invertible lower-triangular Toeplitz matrix of reciprocal Taylor
coefficients.  Hence

```text
Z is n-monotone
<=> H_n(t)>=0 for every safe t.
```

Also

```text
det H_n
 =sum_(|S|=n) product(weights)
   Vandermonde(s_S)^2/product_(s in S)(t+s)^(2n).
```

The next matrix-order gate is therefore the explicit determinant

```text
det [[A1,A2,A3],[A2,A3,A4],[A3,A4,A5]].
```

## V. Further finite-order range

For every `m` up to

```text
floor(H/20)-3,
```

the adjacent Hankel minor

```text
A_m A_(m+2)-A_(m+1)^2
```

has the same pairwise dispersion with denominator power `m+3`.  The phase
rotation remains below the positive half-plane and the verified anchor still
dominates every local negative row.  This closes a proposed tower exceeding
`1.5e11` derivative levels.

Adjacent log-convexity supplies every proper principal minor of the next
`3x3` Hankel matrix.  Only its full determinant remains.

## VI. Eventual order-three Loewner frame

A separate projected-pole frame argument gives a proposed positive lower
bound for the complete `3x3` Hankel matrix when

```text
x=sqrt(t) >= 5,000,000.
```

Three moving height bands provide a uniform Vandermonde frame.  Off-line
horizontal displacement changes the projected real frame only quadratically,
and the perturbation is dominated by the frame moat.

Thus a directed proof on the compact interval

```text
1/2 < x <= 5,000,000
```

would make the Xi impedance matrix monotone of order three.

## VII. Exact firewalls

The branch retains the following rejections.

```text
ordinary concavity -> complete Bernstein             false;
adjacent Hankel log-convexity -> all Hankel PSD       false in general;
finite low-order passivity -> RH                       false;
finite numerical samples -> compact interval theorem  false.
```

The actual all-order target remains a positive Krein-string or equivalent
complete-Bernstein realization.

## VIII. Replays

Retained verdicts:

```text
PASS_VERIFIED_HEIGHT_THIRD_ORDER_CURVATURE
PASS_HIGHER_LOEWNER_FIREWALL
PASS_XI_SCHWARZIAN_ORDER_TWO
PASS_RECIPROCAL_LOEWNER_HANKEL
```

The replays certify exact finite algebra and the printed numerical margins.
They do not certify the external computations, infinite zero-product limits,
proposed zeta-specific domination theorems, matrix monotonicity, or RH.

## Exact boundary

```text
pairwise curvature identities                         EXACT
verified-height/local-count inputs                     EXTERNAL RIGOROUS
three-node infinitesimal Xi positivity                 PROPOSED UNCONDITIONAL
Xi impedance order-two matrix monotonicity             PROPOSED UNCONDITIONAL
adjacent Hankel tower through >1.5e11 levels           PROPOSED UNCONDITIONAL
reciprocal Loewner-Hankel congruence                   EXACT
order-three Loewner tail above x=5e6                   PROPOSED COMPLETE
compact order-three Hankel determinant                 OPEN / DIRECTED
higher-rank Hankel and all Loewner orders              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
