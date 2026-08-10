# Pole-null Lévy/heat completion of the Zeta23–Weil programme

**Status:** `PROPOSED COMPLETE GENERALIZATION / INDEPENDENT REVIEW REQUIRED`

The Fredholm-Pontryagin packet turns Weil's complete zero form into a trace-class operator. This note removes two avoidable asymmetries and exposes a smaller final object.

## 1. Exact metric

For `1/2<a<c`, use

```text
J_(a,c)=(c^2-d^2/du^2)^(-1) M_(exp(-a|u|)).
```

Its evaluation kernel is the explicit strip Cauchy–Sobolev kernel

```text
K(z,w)
 =4a/[(c^2+z^2)(c^2+conj(w)^2)
      (4a^2+(z-conj(w))^2)].
```

It decays like `|Re z|^-4` on the zeta strip and its prime-shift trace norm decays like

```text
exp(-a|y|)(|y|+1/a).
```

Thus the complete zero and prime sides are trace class, while all global Xi-cardinal sources remain in the space.

## 2. The two inevitable negative directions

The centered functions

```text
E_+(z)=Xi(z)(1-2 i z),
E_-(z)=Xi(z)(1+2 i z)
```

vanish at every nontrivial zero and interpolate the two pole coordinates `z=+i/2,-i/2` exactly.

For the pole-free form `Q=W-P`, their Gram is `-I_2`. Every off-line Xi-cardinal can be corrected by `E_+,E_-` to vanish at both pole coordinates without changing any zero value.

Hence, exactly,

```text
negative index(Q)
 = 2 + number of reflected off-line zero pairs.
```

Equivalently, after projecting to the two pole-null constraints, the negative index is exactly the number of off-line pairs.

This converts RH from positivity into a fixed-index theorem:

```text
RH <=> negative index(Q)=2.
```

## 3. Gamma factor as a Lévy energy

The digamma identity gives

```text
mu(t)-mu(0)
 = 1/pi int_0^infinity
   exp(-y/2)/(1-exp(-2y)) [1-cos(ty)] dy.
```

Therefore, on pole-null tests,

```text
W(f,f)
 = int jump_kernel(y) ||f-T_y f||^2 dy
   +2pi mu(0)||f||^2
   -2 sum Lambda(n)/sqrt(n)
      Re <f,T_(log n)f>.
```

The continuum gamma contribution is an exact Dirichlet jump form; the primes are discrete attractive adjacencies. The pole-free form obeys the diamagnetic inequality `Q(|f|)<=Q(f)` on its natural domain.

## 4. Entire heat criterion

For the projected trace-class operator `A0`, put

```text
Theta(beta)=tr(exp(-beta A0)-I).
```

Then

```text
RH <=> Theta(beta)<=0 for every beta>0.
```

One negative eigenvalue forces `Theta(beta)->+infinity` exponentially. Unlike the logarithm of the Fredholm determinant, the word expansion

```text
Theta(beta)
 =sum_(k>=1) (-beta)^k/k! tr(A0^k)
```

converges for every complex beta and has an absolutely convergent all-prime expansion.

## Exact next attack

The live target is no longer a generic determinant sign. It is one of:

```text
prove the pole-free Lévy-prime form has index at most two;
prove the projected heat pressure is nonpositive;
construct a positivity-preserving Feynman-Kac/polymer expansion
for the constrained operator.
```

These targets retain sensitivity to a single off-line pair, remove the pole rank-two nuisance exactly, and expose the archimedean side as a genuine Markov jump energy.
