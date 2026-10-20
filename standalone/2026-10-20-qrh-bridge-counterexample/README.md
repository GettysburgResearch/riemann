# A counterexample in the actual range of a proposed QRH-to-RH bridge

20 October 2026. **Exact counterexample and elementary infinite family.**
This is separate from the frozen boundary-iteration packet. It does not
disprove RH or prove that QRH cannot imply RH by another argument.

Source: G. Puglisi, *On the complex zeros of the Riemann zeta-function*,
[arXiv:2210.03121v9](https://arxiv.org/html/2210.03121v9), 22 April 2024.
The paper's Lemma 1 asserts, for even J and u<=0, that

\[
 \sum_{j=1}^{J-1}p_j(u)\le\tfrac12p_{J-1}(u),
 \qquad p_j(u)=e^{-u}u^j/j!.
\]

Its final argument uses this with u=-z_0 log U, z_0 log U>=10,
and J=2 floor(z_0 log U+2). The counterexamples below satisfy
this actual prescription, not merely the broader lemma statement.

## An exact finite counterexample

Take u=-11 and J=26. After removing the positive common factor e^11,
the asserted difference is

\[
 D_{11}:=\sum_{j=1}^{25}\frac{(-11)^j}{j!}
               -\frac{(-11)^{25}}{2\,25!}
 =\frac{3791459973096443589997}{9495690262216704000000}>0.
\]

Thus the claimed inequality has the wrong sign. Here
J=2 floor(11+2), and 11>=10, exactly as required in the final use.
The accompanying standard-library checker computes this rational
value from the primitive factorial sum. It does not read a claimed
answer as an input to the calculation.

## Failure for every integer parameter n>=11

Set J=2n+4 and a_n=n^(2n+3)/(2n+3)!. Taylor's integral remainder gives

\[
 e^{-n}-\sum_{j=0}^{J-1}\frac{(-n)^j}{j!}
 = n a_n\int_0^1 e^{-nt}(1-t)^{J-1}\,dt
 \le \frac{n a_n}{n+J-1}<\frac{a_n}{3}.
\]

The inequality uses (1-t)^(J-1)<=exp(-(J-1)t), followed by
enlarging the integration interval to [0,infinity). Since J-1 is odd,

\[
 D_n=e^{-n}-1-\left(e^{-n}-\sum_{j=0}^{J-1}
                         \frac{(-n)^j}{j!}\right)+\frac{a_n}{2}
     >-1+\frac{a_n}{6}.
\]

Exactly a_11>6. Moreover,

\[
 \frac{a_{n+1}}{a_n}
 =\left(1+\frac1n\right)^{2n+3}
          \frac{(n+1)^2}{(2n+5)(2n+4)}>1.
\]

Indeed the first three binomial terms give
(1+1/n)^(2n+3)>=5+8/n+3/n^2, and

\[
 \left(5+\frac8n+\frac3{n^2}\right)(n+1)^2
       -(2n+5)(2n+4)=n^2+4+\frac{14}{n}+\frac3{n^2}>0.
\]

Hence a_n>6 and D_n>0 for every integer n>=11. All these examples
have J=2 floor(n+2), so the failure persists arbitrarily far in the
final argument's parameter regime. No floating approximation or
asymptotic assumption is needed.

## Consequence and validation limits

The paper's final contradiction uses precisely this false inequality;
that step is invalid as written. Its claimed QRH-to-RH theorem therefore
cannot be imported through this proof. This is a specific proof defect,
not a counterexample to the theorem's conclusion or an impossibility
result for a different proof.

Run `python -I -S -B verify_counterexample.py`, and optionally repeat
with `-O`. The checker uses rational arithmetic, checks the displayed
finite value and a_11>6, and checks additional finite members. The
infinite assertion rests on the readable integral and binomial proof
above, not on those finite examples. The source version and the actual
parameter prescription were read directly; the checker does not
authenticate the entire external paper.
