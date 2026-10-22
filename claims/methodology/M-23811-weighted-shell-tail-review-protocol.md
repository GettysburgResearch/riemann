# M-23811 — Review protocol for weighted shell-tail stability

Methodology ID: `M-23811`  
Title: Fail-closed review of the parabolic shell moat, weighted prime transport, and the one-sided Chebyshev sampling remainder  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238

## 1. Preferred proof spine

```text
positive parabolic seed
-> exact dyadic seed shell
-> normalized continuum shell tail H_(1/2)<=0
-> finite shell = continuum profile + summable floor error
-> logarithmically weighted prime upper-tail charge
-> exact zero-cost weighted carry transport
-> in-support payment of one shell charge
-> dyadic shell telescope
-> prime ramp >=4 sqrt(X)-X^o(1)
-> square-screw / Landau
-> RH.
```

The only new asymptotic theorem is `WSTS`:

\[
\mathcal B_X
=\max_z
\left(
\sum_{z\le p\le X}(\log p)
[r_X(p)-\mathbf1_{p\le\lfloor X/2\rfloor}r_{\lfloor X/2\rfloor}(p)]
\right)_+
\le X^{o(1)}.
\]

## 2. Frozen exact interfaces

A review packet must bind immutable versions of:

```text
parabolic seed and prime-only reduction       PR #248
normalized continuum tail                     L-23823
weighted prime transport                      L-23824
finite shell approximation                    L-23825
in-support shell assembly                     L-23826
square-screw / Landau consumer                PR #202
fixed-ratio Mertens shell firewall            PRs #229/#234/#236
```

No status of an imported full proposal is inherited.

## 3. Review order

1. Recompute `J'(theta)` in `L-23823`.
2. Verify `S_N+1<=2 sqrt(N)-1/10` for `N>=2`.
3. Reconstruct
   ```text
   H_c(theta)=H(theta)-sqrt(c)H(theta/c)
   ```
   and the dyadic moat.
4. Verify the raw and endpoint-removal amounts in `L-23824`.
5. Confirm exact zero objective cost for one weighted transfer.
6. Verify that the largest-prime boundary atom stays inside the shell endpoint.
7. Reconstruct the finite response approximation in `L-23825`.
8. Audit the Stieltjes sign and endpoint convention in the Chebyshev remainder.
9. Verify dyadic shell telescoping in `L-23826/T-23811`.
10. Attack `WSTS` through the first `2/3` Mertens mutation.

## 4. Mandatory mutations

A proof-producing consumer must reject:

```text
replace log(p)r_p by unweighted r_p;
reverse the direction of the weighted monotone coupling;
omit the destination endpoint-removal block;
charge the boundary outside the assembled endpoint;
lose one prime or prime-square source row;
replace H_c by |H_c|;
take absolute values of d[theta(t)-t] before adding the negative moat;
omit one dyadic shell;
use only the classical PNT error and call it X^o(1);
lose the fixed-ratio Mertens coordinate;
prove the estimate only for finitely many endpoints.
```

## 5. Why the logarithmic weight is mandatory

The raw prime residual is sampled with density about `1/log p`; its unweighted
upper tails need not inherit the continuum order. Multiplication by `log p`
restores the Chebyshev measure `d theta`, and `L-23824` shows that this weighted
order has an exact zero-cost carry implementation.

A claimed proof using unweighted prime transport is solving a different and in
general false finite statement.

## 6. Why the classical PNT is not the closing theorem

`L-23825` gives

\[
\text{weighted shell tail}
=
\sqrt X H_{1/2}(z/X)
+\mathcal E_X(z)
+\text{summable floor error}.
\]

The first term is negative. A classical zero-free-region estimate bounds
`mathcal E_X`, but not at the required subpolynomial scale uniformly through the
critical shell. A proof must exploit the source-specific sign interaction; it
may not discard the negative main term and quote an absolute PNT remainder.

## 7. Proof-status discipline

```text
normalized continuum shell theorem       exact/proposed
finite weighted transport                exact/proposed
rational synthetic replay                exact finite control
WSTS                                      open RH-bearing theorem
T-23811 after WSTS                        full conditional proof
accepted proof of RH                      no
```

A finite numerical trend, an average-in-`X` result, or an almost-all tail bound
does not prove `WSTS`.
