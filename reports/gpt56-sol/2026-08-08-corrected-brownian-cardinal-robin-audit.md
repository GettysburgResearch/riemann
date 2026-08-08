# Corrected Brownian cardinal fiber and the global-mixture firewall

**Agent:** `gpt56-sol`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-sol/296-correct-robin-cardinal-fiber`  
**Parent:** PR #296 at `4a68887f9f713aea7f63444030379fb864766a2d`  
**Status:** **exact source correction and route refutation; RH unproved**

## 1. Objective

The central carry continuation was corrected through PR #317. Its complete eta
recombination is exactly the previously known pure-central producer, so it does
not provide a new positive completion. I therefore pivoted to the independent
Brownian/Nörlund approximant route on PR #296.

The parent branch had proposed to prove the finite real-zero theorem through a
cardinal decomposition into Robin fibers and a reflected-tail inequality. This
pass derives the cardinal fiber directly from the Mellin tail identity and tests
the claimed closure.

## 2. The published fiber is algebraically impossible

For any positive random variable,

```text
X(1/2+z)=m(1/2+z)+m(1/2-z)
```

is even in `z`. The parent fiber

```text
cosh(ell z/2)+sinh(ell z/2)/ell
```

has a nonzero linear coefficient and is not even. It cannot be the centered
cardinal contribution.

The exact layer-cake calculation gives

```text
Phi_ell(z)=cosh(ell z/2)+2z sinh(ell z/2).
```

## 3. Correct Robin theorem

For `ell>0`, `Phi_ell/2` is the characteristic determinant of

```text
-u''=lambda u,
u'(0)=0,
u'(ell/2)+(1/2)u(ell/2)=0.
```

The quadratic form is nonnegative, so every zero is imaginary.

For `ell<0`, the terminal Robin sign reverses. There is exactly one negative
eigenvalue, equivalently one real zero pair `+-kappa`, determined by

```text
kappa tanh(kappa |ell|/2)=1/2.
```

Thus the negative-length sector cannot be treated as another positive Robin
fiber.

## 4. Reflected-tail domination is impossible

At every finite endpoint the Brownian/Nörlund variable has an exponential upper
tail. Hence the positive-length weight at `a` decays super-exponentially as
`a->infinity`, while the reflected negative-length weight behaves as
`e^(-a/2)`. Therefore

```text
W_N(a)/W_N(-a) -> 0.
```

The proposed pointwise domination `W_N(a)>=W_N(-a)` fails for every finite `N`.

## 5. Even positive fibers do not form a real-zero cone

The first canonical-product coefficient inequality for an even order-one
function with imaginary zeros is

```text
c1^2 >= 2 c0 c2.
```

Both `Phi_0=1` and `Phi_8` individually have no off-axis zeros. Nevertheless

```text
F=Phi_0+(1/10)Phi_8
```

has

```text
c0=11/10,
c1=8/5,
c2=16/5,

c1^2=64/25 <176/25=2c0c2.
```

So `F` has an off-axis zero. Positive superposition of good Robin fibers is not
closed.

This eliminates a second possible shortcut: removing the negative-length sector
would still not prove BLNRZ.

## 6. Correct global frontier

The finite approximant has the exact corrected representation

```text
F_N(z)
 =(1/2) integral e^(ell/4) Tbar_N(e^ell) Phi_ell(z) d ell.
```

A genuine proof now needs one aggregate object:

```text
a canonical system for F_N;
an Hermite-Biehler function whose real part is F_N;
or an all-order hyperbolic Jensen-polynomial proof.
```

One-fiber Sturm-Liouville theory cannot be integrated termwise into that result.
The length-moment coefficients and the first Newton obstruction are written in
`L-21710` as exact finite acceptance tests.

## 7. Exact status

```text
finite Brownian/gamma/Norlund algebra        retained
published cardinal formula                  false
correct centered cardinal fiber             proved
one-fiber Robin classification              proved
finite reflected-tail domination            false
positive fiber cone closure                 false
aggregate canonical-system theorem          open / RH-bearing
Riemann Hypothesis                           unproved
```

No full proof is claimed and no proof step is assigned to reviewers.
