# L-91317 — The pole-node Jordan innovation is exactly positive at every scale

Claim ID: `L-91317`  
Status: **EXACT UNCONDITIONAL SOURCE-SIDE RECURRENCE; BOUNDARY IDENTIFICATION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: main `L-91015/L-91029`, `L-91316`  
RH status: **unproved**

## 1. Pole-normalized fluctuation

For `a>0`, write

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)},
 \qquad
 \kappa_a=\frac1{\zeta(1+2a)},
 \tag{L-91317.1}
\]

and

\[
 Q_a(s)=\frac{\kappa_a}{s-1}+H_a(s).
 \tag{L-91317.2}
\]

The pole-normalized finite part is

\[
 \boxed{
 F(a):=\frac{H_a(1)}{\kappa_a}
 =\gamma-\frac{\zeta'}{\zeta}(1+2a).
 }
 \tag{L-91317.3}
\]

## 2. Exact dyadic innovation

The coefficient-one recurrence of main `L-91015`, evaluated at the pole node
`s=1`, gives

\[
 F(2a)
 =F(a)+\frac{Q_a'(1+2a)}{Q_a(1+2a)}.
 \tag{L-91317.4}
\]

Therefore

\[
 \boxed{
 F(a)-F(2a)
 =-\frac{Q_a'(1+2a)}{Q_a(1+2a)}.
 }
 \tag{L-91317.5}
\]

Using the positive Euler logarithm,

\[
 \log Q_a(s)
 =\sum_p\sum_{k\ge1}
 \frac{1-p^{-2ak}}{k}\,p^{-ks},
 \tag{L-91317.6}
\]

we obtain

\[
 \boxed{
 F(a)-F(2a)
 =\sum_p\sum_{k\ge1}
 (\log p)(1-p^{-2ak})p^{-k(1+2a)}
 >0.
 }
 \tag{L-91317.7}
\]

The sum converges absolutely for every `a>0`.

Thus

\[
 \boxed{
 F(a)>F(2a)>F(4a)>\cdots.
 }
 \tag{L-91317.8}
\]

## 3. Prime-jump interpretation

Let

\[
 d\nu_{a,1+2a}(t)
 =\sum_p\sum_{k\ge1}
 \frac{1-p^{-2ak}}{k p^{k(1+2a)}}
 \delta_{k\log p}(dt).
 \tag{L-91317.9}
\]

Then

\[
 \boxed{
 F(a)-F(2a)
 =\int_0^\infty t\,d\nu_{a,1+2a}(t).
 }
 \tag{L-91317.10}
\]

The innovation is the first moment of the positive compound-Poisson
prime-power jump measure. It is therefore already a literal one-particle Fock
norm/current, not merely a positive number.

Higher derivatives give the complete positive moment tower

\[
 (-1)^m\partial_s^m\log Q_a(s)|_{s=1+2a}
 =\int t^m\,d\nu_{a,1+2a}(t)>0
 \qquad(m\ge1).
 \tag{L-91317.11}
\]

## 4. Terminal behavior

Since

\[
 -\frac{\zeta'}{\zeta}(1+2a)\longrightarrow0
 \qquad(a\to\infty),
 \tag{L-91317.12}
\]

one has

\[
 \boxed{
 F(a)\longrightarrow\gamma.
 }
 \tag{L-91317.13}
\]

Therefore

\[
 \boxed{
 F(a)-\gamma
 =\sum_{j\ge0}
  \bigl[F(2^ja)-F(2^{j+1}a)\bigr]
 }
 \tag{L-91317.14}
\]

with an absolutely convergent positive source-side innovation series.

## 5. Consequence for the three-route proposal

At the pole-aligned node:

```text
coefficient-one inherited state        exact;
new arithmetic innovation              exact positive Fock moment;
all-generation source telescope        exact;
terminal state                          Euler's constant gamma.
```

Thus no source-side scalar sign remains. The only conclusion-producing theorem
is the completed boundary identification:

> map the positive prime-jump innovation (L-91317.10), together with the
> explicit gamma/pole zero and the retained theta/Brownian/`p=2` reserve, to
> the critical/stable model-space outputs with no residual hyperbolic port.

This is `PAAE_a/ONAE_a`. It remains open and RH-bearing.

## 6. Firewall

Equation (L-91317.7) does not itself prove RH. The controls of PR #398 can
retain a positive safe source recurrence while carrying a nonzero crossed-zero
port. The completed source-to-model norm identity remains indispensable.
