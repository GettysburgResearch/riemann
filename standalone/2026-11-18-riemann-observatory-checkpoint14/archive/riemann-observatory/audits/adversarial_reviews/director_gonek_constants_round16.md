# Explicit finite divisor constants for fixed derivative orders

18 November 2026. The director checked the two independent floor-summation proofs, all small and integer endpoints, the symmetric choice of inner order, and the Abel substitution into the single finite coefficient step in Gonek's Lemma 8. These elementary estimates allocate constants in the source's Lemma 7. They do not allocate the later contour, gamma or full weighted-tail constants, and no optimality or publication novelty is claimed.

Sources and independent calculations: Gonek's pinned 1984 journal scan, Lemmas 7–8, pp.133–135; [initial (1,1) proof](prime142_gonek_convolution_constant.md); [independent centered-floor improvement](weighted142_gonek_convolution_review.md); [all-positive-order proof](prime145_explicit_all_derivative_convolution.md); [independent sharper proof and zero orders](weighted145_explicit_all_derivative_review.md). The [whole source audit](director_gonek_whole_round15.md) pins its version and external assumptions. The [explicit Abel input](director_explicit_abel_round15.md) uses the targeted unconditional Fiori–Jaskari bound, not its conditional transfer theorem.

## All positive integer orders

For real z>1, L=log z, integers mu,nu>=1, M=mu+nu and B=mu^mu nu^nu/M^M, define

```text
C_(mu,nu)(z)=sum_(dr≤z) (log d)^mu (log r)^nu.
```

Then

```text
abs(C_(mu,nu)(z)−[mu!nu!/(M+1)!] z L^(M+1))
 <= [min(mu,nu)+exp(−1)+B] z L^M.
```

The weaker coefficient with +1 in place of exp(-1) also follows. These inequalities include every integer endpoint and arbitrarily small z-1. If using the coefficients of zeta^(mu)zeta^(nu), put the sign (-1)^(mu+nu) on both the original sum and its main term.

For the proof, let S_nu(q)=sum_(r≤q)(log r)^nu, q>=1. Monotonicity and integration by parts give

```text
0 <= q(log q)^nu−S_nu(q)
 <= nu q(log q)^(nu−1)+(log q)^nu
 <= [nu+exp(−1)]q(log q)^(nu−1).
```

The last step uses sup_(q≥1) log(q)/q=exp(-1). The error at q=1 is zero; for nu=1 the zeroth log power is one. Opening the convolution with q=z/d bounds its inner error by [nu+exp(-1)]z L^M, since the d=1 term vanishes and sum_(2≤d≤z)1/d<=L.

The main sum has kernel g(t)=(log t)^mu(L-log t)^nu/t on [1,z]. In v=log t its logarithmic derivative is -1+mu/v-nu/(L-v), strictly decreasing from positive to negative infinity. The kernel is unimodal and zero at both endpoints. Its maximum is at most B L^M. Integration against the centered discrepancy floor(t)-t+1/2 bounds the sum-minus-integral by half the variation, hence by that maximum. The integral is the exact beta integral mu!nu! L^(M+1)/(M+1)!. Interchanging d,r gives the smaller inner order and proves the displayed bound. No negative log power or discarded upper atom is involved.

For one zero order and m>=1, the same method, retaining the nonzero upper boundary of the kernel, gives

```text
abs(sum_(dr≤z) (log d)^m−z L^(m+1)/(m+1)) <= 2z L^m.
```

If both orders are zero, comparison with z H_floor(z) gives abs(sum_(dr≤z)1-z log z)<=z. The convention (log 1)^0=1 is explicit in these zero-order statements.

## A convenient rational (1,1) allocation and its finite use

For mu=nu=1 the simpler rational bound

```text
abs(sum_(dr≤z) log d log r−z L³/6) <= (9/4) z L²
```

comes directly from the inner coefficient 2 and centered variation 1/4. It is looser than the sharper general coefficient 5/4+exp(-1), and is retained for convenient rational bookkeeping.

Define explicitly, for real delta,

```text
B_n(delta)=−sum_(drk=n) log d log r Lambda(k) k^(i delta),
I_3(x,delta)=integral_1^x u^(i delta−1)log³(x/u) du,
L_x=log x.
```

This is the (1,1) coefficient in the source's Lemma 8 with its negative von Mangoldt factor. The finite divisor error is bounded by (9/4)x sum_(k≤x) Lambda(k)k^(-1)log²(x/k). The positive-power Abel estimate, whose upper boundary vanishes, gives

```text
sum_(k≤x) Lambda(k)k^(-1)log²(x/k)
 <= L_x³/3+21L_x²+40L_x,
abs(A_3(x,delta)) <= 24L_x³+60L_x²  for real abs(delta)≤1/2.
```

The second coefficient uses 1+10sqrt(5)<24. Combining the two independently checked steps yields, for every x>1,

```text
abs(sum_(n≤x)B_n(delta)+(x/6)I_3(x,delta))
 <= x[(19/4)L_x³+(229/4)L_x²+90L_x].
```

The main convolution uses three variables; powers at n=x are included exactly. These are finite identities and inequalities, not numerical evidence for an asymptotic. Improving these deliberately conservative constants is less consequential than controlling the remaining differentiated gamma factors and contour terms. A useful next task is to keep an explicit ledger through those steps and determine whether the resulting derivative-tail onset is practical. Nothing here improves the leading source constant or proves the full fourth-moment cancellation problem.
