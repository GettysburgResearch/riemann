# L-91345 — The `P_61` one-prime splice has uniformly positive target and strictly larger score

Claim ID: `L-91345`  
Status: **PROVED EXACT FINITE-PREFIX / ONE-PRIME SCALAR THEOREM**  
Created: 2026-08-12  
Depends on: `L-91328`; finite divisor-prefix arithmetic  
RH status: **unproved**

## 1. The rational prefix state

Put

\[
 P_{61}=\prod_{q\le61}q
\]

and, for real `z>=1`, define

\[
 \boxed{
 A_{61}(z)
 =\sum_{\substack{d\mid P_{61}\\d\le z}}
  \frac{\mu(d)}d.
 }
\tag{L-91345.1}

This is a finite rational step function with `2^18=262144` activation states.
The exact standard-library checker orders all divisors and uses the common
denominator `P_61`.  It proves

\[
 \boxed{
 A_{61}(z)\le1
 \qquad(z\ge1),
 }
\tag{L-91345.2}

with equality only on the initial cell, and

\[
 \boxed{
 A_{61}(z)
 \ge
 \frac{55036345385124606673}{3351096610268770599522}
 >0.0164233
 \qquad(z\ge67).
 }
\tag{L-91345.3
}

The minimum is attained on the activation cell beginning at `z=70`.

## 2. One new rough prime preserves a fixed positive first moment

Let

\[
 p\ge67,
 \qquad y\ge1,
 \qquad x=py.
\]

The first-moment prefix after adjoining the new Euler factor is

\[
 \boxed{
 A_{61;p}(x)
 =A_{61}(x)-\frac1pA_{61}(y).
 }
\tag{L-91345.4
}

Using (L-91345.2), (L-91345.3), and `p>=67`,

\[
\begin{aligned}
 A_{61;p}(x)
 &\ge
 \frac{55036345385124606673}{3351096610268770599522}
 -\frac1{67}\\
 &=
 \frac{336338530534578047569}
 {224523472888007630167974}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 A_{61;p}(x)>0.0014980
 \qquad(p\ge67,\ y\ge1).
 }
\tag{L-91345.5
}

No prime distribution estimate or floating sign decision is used.

## 3. Target and score finite forcings

For `a>0`, retain the finite forcing

\[
 F_a^{(61)}(x)
 =\sum_{\substack{d\mid P_{61}\\d\le x}}
 \mu(d)
 \left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right).
\tag{L-91345.6
}

After one new rough prime define

\[
 F_{a;p}^{(61)}(x)
 =F_a^{(61)}(x)-p^{-1/2}F_a^{(61)}(x/p).
\tag{L-91345.7
}

`L-91328` proves, for `a=1,2`,

\[
 F_{a;p}^{(61)}(x)>\frac3{50}\sqrt x
 \qquad(p\ge67,\ x\ge p).
\tag{L-91345.8
}

The function is affine in `a`.  Since

\[
 \frac43=\frac23\cdot1+\frac13\cdot2,
 \qquad
 \frac53=\frac13\cdot1+\frac23\cdot2,
\]

the native target and score packets

\[
 \boxed{
 \mathcal T_{61;p}(x)=3F_{4/3;p}^{(61)}(x),
 \qquad
 \mathcal S_{61;p}(x)=3F_{5/3;p}^{(61)}(x)
 }
\tag{L-91345.9
}

satisfy

\[
 \boxed{
 \mathcal T_{61;p}(x)>rac9{50}\sqrt x,
 \qquad
 \mathcal S_{61;p}(x)>rac9{50}\sqrt x.
 }
\tag{L-91345.10
}

## 4. Score is strictly larger than target

The two source kernels differ by the square-root first moment.  Exactly,

\[
\begin{aligned}
 \mathcal S_{61;p}(x)-\mathcal T_{61;p}(x)
 &=\sqrt x\,A_{61;p}(x).
\end{aligned}
\tag{L-91345.11
}

Combining with (L-91345.5),

\[
 \boxed{
 \mathcal S_{61;p}(x)-\mathcal T_{61;p}(x)
 >
 \frac{336338530534578047569}
 {224523472888007630167974}
 \sqrt x.
 }
\tag{L-91345.12
}

Thus the exact one-prime arithmetic packet is not merely positive in both scalar
ledgers.  It carries a fixed favorable endpoint-score surplus.

## 5. Consequence for the current splice

For the preferred range

\[
 p\ge67,
 \qquad1\le y<67,
 \qquad x=py,
\]

the scalar target and score obligations of `O-91310` are closed:

```text
one-prime SHARP target                 uniformly positive;
one-prime endpoint score               uniformly positive;
score minus target                      uniformly positive;
finite scalar separation witness        impossible.
```

The only remaining part of the one-prime splice is physical row/capacity typing.
`L-91344` reduces its inherited-row component to one positive rough Green bulk
and a finite `P_61` boundary packet.

## 6. Verification

The companion exact checker proves:

```text
all 262,144 rational divisor-prefix states;
global upper bound A_61<=1;
minimum for z>=67 at z=70;
exact positive gap after subtracting 1/67;
affine target/score interpolation identities.
```

Retained verdict:

```text
PASS_P61_ONE_PRIME_TARGET_SCORE_SURPLUS
```

## 7. Proof boundary

```text
P_61 first-moment prefix corridor             DIRECTED/INTEGER EXACT
one-prime first-moment positivity             EXACT
target positivity                              EXACT FROM L-91328
score positivity                               EXACT FROM L-91328
strict score-over-target surplus               EXACT
finite Green-boundary row inequality           OPEN
ordinary/radix-four physical splice            OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```