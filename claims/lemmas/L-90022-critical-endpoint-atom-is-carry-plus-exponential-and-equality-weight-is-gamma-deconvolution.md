# L-90022 — The critical endpoint atom is carry plus one elementary delay, and the equality weight is the Gamma deconvolution

Claim ID: `L-90022` (provisional branch range)  
Title: After critical tilting, the positive parabolic endpoint kernel is the exact carry law convolved with a Bernoulli–exponential delay; the reciprocal-zeta equality state is precisely the formal independent factor from that law to `Gamma(2,1/2)`  
Status: **PROPOSED COMPLETE EXACT PROBABILITY / TRANSFORM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #265 `L-26204`; PR #335 `L-33101`; elementary Laplace algebra  
Scope: exact continuum bridge among endpoint-scale, carry, and Gamma states; no positivity of the deconvolution factor and no RH conclusion

## 1. Critical endpoint-atom law

Retain the positive endpoint-scale kernel of PR #265,

\[
 \varrho(v)=e^{-v/2}k(e^{-v}),
 \qquad v\ge0,
\tag{L-90022.1}
\]

whose Laplace transform is

\[
\boxed{
 \widehat\varrho(z)
 =\zeta\left(z+\frac12\right)
  {z-\frac12\over z(z+\frac12)}.
}
\tag{L-90022.2}
\]

PR #265 also proves

\[
 \widehat\varrho(1/2)=2.
\]

Therefore

\[
\boxed{
 d\nu(v)={1\over2}e^{-v/2}\varrho(v)\,dv
}
\tag{L-90022.3}
\]

is a probability law. Let

\[
 V\sim\nu.
\]

For `s>=0`,

\[
\begin{aligned}
 \phi_V(s)
 :=\mathbb E[e^{-sV}]
 &={1\over2}\widehat\varrho\left(s+\frac12\right)\\
 &=\boxed{
 {s\zeta(s+1)\over(s+1)(2s+1)}.
 }
\end{aligned}
\tag{L-90022.4}

The value at `s=0` is removable and equals one.

## 2. Exact carry law

PR #335 `L-33101` defines the continuum carry variable `T` and proves

\[
\boxed{
 \phi_T(s)
 :=\mathbb E[e^{-sT}]
 ={2s\zeta(s+1)\over(s+1)(s+2)}.
}
\tag{L-90022.5}

Consequently

\[
\boxed{
 {\phi_V(s)\over\phi_T(s)}
 ={s+2\over2(2s+1)}
 ={1\over4}+{3\over4}{1\over1+2s}.
}
\tag{L-90022.6}

Let `Z` be independent of `T` with

\[
\boxed{
 Z=\begin{cases}
 0,&\text{with probability }1/4,\\
 E,&\text{with probability }3/4,
 \end{cases}
 \qquad E\sim\operatorname{Exp}(1/2).
}
\tag{L-90022.7}

Its Laplace transform is exactly the final expression in (L-90022.6). Laplace uniqueness gives

\[
\boxed{
 V\overset d=T+Z,
 \qquad T\perp Z.
}
\tag{L-90022.8}

Thus the critical endpoint atom is not a new unrelated scale law: it is the exact carry law plus one elementary randomized delay.

The means are

\[
 \mathbb ET={3\over2}-\gamma,
 \qquad
 \mathbb EZ={3\over2},
\]

so

\[
\boxed{
 \mathbb EV=3-\gamma.
}
\tag{L-90022.9}

## 3. Gamma target

Let

\[
 G\sim\operatorname{Gamma}(2,1/2).
\]

Then

\[
\boxed{
 \phi_G(s)={1\over(1+2s)^2}.
}
\tag{L-90022.10}

Dividing by (L-90022.4),

\[
\boxed{
 {\phi_G(s)\over\phi_V(s)}
 ={s+1\over s(2s+1)\zeta(s+1)}.
}
\tag{L-90022.11}

## 4. The endpoint equality weight is exactly the deconvolution factor

PR #265 derives the unique causal equality weight `L_*` for the positive endpoint-scale convolution:

\[
\boxed{
 \widehat L_*(z)
 ={z+\frac12\over
   z(z-\frac12)\zeta(z+\frac12)}.
}
\tag{L-90022.12}

Define its critical tilt

\[
\boxed{
 W_*(t)={1\over2}e^{-t/2}L_*(t)
}
\tag{L-90022.13}

as a causal signed distribution. Then

\[
\begin{aligned}
 \widehat W_*(s)
 &={1\over2}\widehat L_*\left(s+\frac12\right)\\
 &=\boxed{
 {s+1\over s(2s+1)\zeta(s+1)}
 }\\
 &=\boxed{{\phi_G(s)\over\phi_V(s)}}.
\end{aligned}
\tag{L-90022.14}

Therefore the exact convolution identity is

\[
\boxed{
 \operatorname{Law}(G)
 =\nu*W_*
}
\tag{L-90022.15}

in the causal transform/distribution sense.

If `W_*` were a nonnegative probability law, (L-90022.15) would become the independent decomposition

\[
\boxed{
 G\overset d=V+W,
 \qquad W\sim W_*,\quad W\perp V.
}
\tag{L-90022.16}

No such positivity is claimed.

## 5. Normalization and mean

The zeta pole at one makes the value of (L-90022.14) at `s=0` removable:

\[
\boxed{
 \widehat W_*(0)=1.
}
\tag{L-90022.17}

Using

\[
 s\zeta(1+s)=1+\gamma s+O(s^2),
\]

one obtains

\[
 \widehat W_*(s)
 =1-(1+\gamma)s+O(s^2).
\]

Thus the formal first moment is

\[
\boxed{
 \mathbb E W_*=1+\gamma,
}
\tag{L-90022.18}

consistent with

\[
 (3-\gamma)+(1+\gamma)=4=\mathbb EG.
\]

## 6. Relation to the martingale Gamma–carry theorem

PR #335 proves the state-dependent centered transport

\[
 T+\left({5\over2}+\gamma\right)
 \le_{\rm cx}G.
\]

The present theorem identifies the stronger independent-factor question after passing from `T` to the natural endpoint atom `V=T+Z`:

```text
state-dependent martingale route:
    centered carry -> Gamma by convex order;

endpoint-scale independent route:
    V -> Gamma by the formal factor W_*;

obstruction in W_*:
    exactly 1/zeta(s+1).
```

Thus the reciprocal-zeta equality state of the endpoint programme is precisely the missing independent Gamma-convolution factor. The two research programmes are exact transforms of one another at the critical scale.

This also explains why a finite martingale lift may be weaker than proving positivity of `L_*`: state-dependent transport can exist even when the independent deconvolution factor is signed.

## 7. Spectral firewall

Every off-line zeta zero gives a pole of (L-90022.14) in the corresponding shifted half-plane. Therefore positivity of `W_*`, complete monotonicity of its transform, or any honest independent probability factorization in (L-90022.16) is conclusion-producing and cannot be imported as a routine consequence of the continuum convex-order theorem.

The exact bridge is useful because it identifies the smallest discrepancy between the two routes; it does not erase it.

## 8. Proof boundary

Closed exactly:

1. the critical endpoint-atom probability law;
2. its Laplace transform;
3. the decomposition `V=T+Z` with elementary `Z`;
4. the exact ratio from `V` to the Gamma target;
5. identification of that ratio with the critically tilted endpoint equality weight;
6. normalization and mean of the formal factor;
7. the exact endpoint/Gamma/Pascal bridge.

Open:

1. positivity of the deconvolution factor;
2. a finite state-dependent arithmetic lift with subquadratic loss;
3. the complete prime-power gap estimate;
4. RH.