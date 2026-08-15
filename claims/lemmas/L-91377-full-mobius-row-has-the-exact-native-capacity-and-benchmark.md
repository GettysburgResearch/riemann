# L-91377 — The full Möbius row has exactly the native capacities and literal benchmark

Claim ID: `L-91377`  
Status: **PROVED EXACT NORMALIZATION THEOREM**  
Created: 2026-08-14  
Depends on: the positive component-row carry identity and `mu * log = Lambda`  
RH status: **unproved**

## 1. Full equality row

For real `X>=1` and integer `j>=2`, define the full Möbius equality row

\[
\boxed{
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
}
\tag{L-91377.1}
\]

No positivity is asserted.

Let the ordinary response of one component be

\[
 C_Y(q)=\frac1{\sqrt q}H(Y/q),
 \qquad
 H(Z)=\sum_{m\le Z}\frac1{\sqrt m}\log\frac Zm.
\tag{L-91377.2}
\]

## 2. Exact native ordinary capacity

By finite summation,

\[
\begin{aligned}
 C_{c_X}(q)
 &=\frac1{\sqrt q}
 \sum_{km\le X/q}\frac{\mu(k)}{\sqrt{km}}
 \log\frac{X}{qkm}\\
 &=\frac1{\sqrt q}
 \sum_{n\le X/q}\frac1{\sqrt n}
 \log\frac{X}{qn}\sum_{k\mid n}\mu(k).
\end{aligned}
\]

Only `n=1` survives. Therefore

\[
\boxed{
 C_{c_X}(q)=w_X(q)
 =\frac1{\sqrt q}\log\frac Xq\,\mathbf1_{q\le X}.
}
\tag{L-91377.3}
\]

## 3. Exact native radix-four capacity

Put

\[
 \Xi_d(q)=C_d(q)-2C_d(4q)
\]

and

\[
 \Omega_X(q)=w_X(q)-2w_X(4q).
\]

Linearity of (L-91377.3) gives

\[
\boxed{
 \Xi_{c_X}(q)=\Omega_X(q).
}
\tag{L-91377.4}
\]

Thus `c_X` is the unique arithmetic row under discussion with the exact native
ordinary and detail responses. Its unresolved feature is coefficientwise sign.

## 4. Exact literal entropy

Let

\[
 \mathcal E(Y)=\sum_jQ_Y(j)G_j
 =\sum_{m\le Y}\frac{\log m}{\sqrt m}\log\frac Ym.
\tag{L-91377.5}
\]

Then

\[
\begin{aligned}
 \mathcal H(c_X)
 &=\sum_{km\le X}
   \frac{\mu(k)\log m}{\sqrt{km}}
   \log\frac{X}{km}\\
 &=\sum_{n\le X}\frac1{\sqrt n}\log\frac Xn
   \sum_{k\mid n}\mu(k)\log\frac nk.
\end{aligned}
\]

The inner convolution is `Lambda(n)`. Hence

\[
\boxed{
 \mathcal H(c_X)=J_\Lambda(X)
 :=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
}
\tag{L-91377.6}
\]

## 5. Exact boundary

The theorem fixes the normalization dictionary:

```text
full Möbius row ordinary response    w_X exactly;
full Möbius row detail response      Omega_X exactly;
full Möbius row literal entropy      J_Lambda exactly;
full Möbius row coefficient sign     open / RH-bearing.
```

A finite-Euler truncation changes all three coordinates by a positive rough
reservoir and may not be substituted for `c_X` without an explicit physical
reservoir allocation.
