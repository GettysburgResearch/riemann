# Independent review of the signed Mobius complement

20 October 2026. Reviewed `type_i/SIGNED_MOBIUS_COMPLEMENT.md` at SHA256
`acbdcc145517976b4f8cec4d75db1c2fd6a691f3cf7f424bac822a5d3eb9cf61`,
against the exact T4--T6 interface and the packet's uniform reciprocal
and cubic mean inputs. The reviewer did not co-derive the complement
factorization or its consumer. Upstream reflection and the common
zero-free premise remain explicit dependencies.

No new-interface defect was found.

The signed prime coefficient in MC2 follows from multiplying the
complementary factor by the Mobius value minus one. For MC3's `a,b`,
`L(a)/L(2a)` contributes `1+x`, and `1/L(b)` contributes `1-y`.
Multiplying the absolutely convergent correction in MC4 gives exactly
`1+x-y`. The correction requires only positive real parts of `a,b`
and `Re(a+b)>1`; it does not require `2 Re a>1` and never divides by
`1+x-y`. Defining it with the k-primes omitted gives a bound uniform
in k. The remaining incomplete Hecke factors cost only `(Nk)^epsilon`
on each fixed permitted strip.

For `s=1/2-delta+it`, the three analytic conditions translate exactly
to MC8. The third ensures positive `Re a`, while the first two put
both reciprocal arguments strictly inside their zero-free half-planes.
The numerator has nonzero angular type and hence no translated
principal pole. Its ordinary polynomial conductor bound is enough;
no Lindelof bound for that numerator is used. A fixed positive contour
gap, the uniform reciprocal estimates and rapid smooth Mellin decay
justify the contour shift from absolute convergence and give MC9.
Fixed logarithmic derivatives use a slightly wider strip. The two
piecewise optimizations in MC10--MC11 are correct, including their
meeting point beta=2/3 and the beta=1/2 limiting interpretation.

For the consumer, T5 has k-weight `(Nk)^(1/2-s)`, hence modulus
`K^delta`. With the original row coefficient `mu(r)` and `r=km`,
`mu(km)=mu(k)mu(m)` on the exact coprime support. Each finite ray
matrix coefficient separates as a finite sum of characters in k and m.
The smooth weight `f(Nk Nm/R)` has bounded normalized seminorms at
fixed k. Therefore MC9 applies to each actual complementary dyad,
including all primes removed by k. The right-line cubic mean and
Cauchy give the factor K in MC13. Since `KM` is comparable to R and
`tau_beta(delta)<1+delta`, geometric dyadic summation proves MC14.
Its optimized saving exponent in MC15 is algebraically correct.

The consumer cuts the complementary variable only after exact
reflection. It does not impose a new roughness or prime condition on
the original row. The full-divisor case m=1 and bounded complements
remain; their absence of saving is explicitly preserved. Thus the
result is a strict bound for a proper reflected tail, conditional on
the specified common unitary premise. It gives no full Type-III prime
saving and no numerical zero-free improvement by itself.
