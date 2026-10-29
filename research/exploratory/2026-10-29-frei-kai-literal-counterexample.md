# Literal counterexample to a stated fixed-field theorem

**Scope:** This is a check of the statement, not a review of the authors' intended large-conductor argument. The source is [Frei–Kai, *Exceptional zeros of Hecke L-functions*, version 1](https://hexagonmath.org/2610.00466v1), with the directly accessible [PDF](https://hexagonmath.org/pdf/2610.00466v1). The page without `/pdf/` is an HTML landing page. The PDF was downloaded as `/tmp/frei-kai.pdf` and its text extracted to `/tmp/frei-kai.txt` in this workspace environment.

On page 1, Theorem 1.1 quantifies over every number field `K`, every real Hecke character `chi` with conductor ideal `q`, and every real zero `beta` in `(0,1)` of `L(s,chi)`. It states

```text
(1-beta) log Nq >= epsilon_K > 0.
```

On page 3, Section 3 includes the following dismissal of the trivial case: “As the Dedekind zeta function of K definitely has no zero at s = 1, the theorem’s assertion holds true for the trivial character.” The absence of a zero exactly at 1 does not imply the displayed inequality for zeros at other points.

Take the explicit quaternionic number field

```text
K = Q(sqrt((5+sqrt(5))(41+sqrt(205)))).
```

[The published discussion in *On a Mertens-type conjecture for number fields*, §6.2](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/on-a-mertenstype-conjecture-for-number-fields/B01C7628DF4D57CAE8410901FD6A9321) attributes this example to Serre and states it is a `Q_8`-extension with `zeta_K(1/2)=0`. Independently, the introduction of [*Central values of zeta functions of non-Galois cubic fields*](https://doi.org/10.1007/s00222-025-01373-6) attributes infinitely many degree-eight quaternionic central-vanishing examples to Fröhlich. These are source-reported constructions; this note does not independently recompute their Artin root numbers.

Choose `chi=1`. It is a real Hecke character, its conductor is the unit ideal, `Nq=1`, and its L-function is `zeta_K`. Thus `beta=1/2` satisfies the theorem's hypotheses, while the asserted inequality becomes `0 >= epsilon_K > 0`. This is a direct contradiction to the printed statement.

The source's Lemma 5.4 assumes `Nq` sufficiently large, and Section 6.1 reduces to large `Nq` after invoking the finiteness of the bounded-conductor family and nonvanishing at 1. The latter is suitable for controlling zeros sufficiently close to 1 with a positive logarithmic denominator, but it cannot repair the `log Nq=0` assertion. Section 6.1 also prints `(1-beta) Nq < epsilon` where the theorem's contradiction hypothesis would involve `(1-beta) log Nq < epsilon`. The estimate following it is suggestive of the logarithmic hypothesis, but correcting that apparent mismatch and replacing `log Nq` by, for example, `log(2Nq)` would require a separate proof audit. No assertion here is made that the intended large-conductor result is false.
