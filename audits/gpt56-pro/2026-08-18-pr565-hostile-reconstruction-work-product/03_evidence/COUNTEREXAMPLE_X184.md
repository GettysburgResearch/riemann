# Counterexample to the advertised 1/40 P61 bias

Run:

```bash
python3 code/reproduce_x184.py
```

The script independently evaluates the definitions at `x=184` using 120 decimal digits and an overflow-safe enumeration of exactly the relevant squarefree divisors of `P_61`.

Retained values:

```text
F(184)       = 10.693579648773829950805315504985464444048948533877...
M(184)       = 445.857603542602836315578077301107642672774873102716...
F(184)/M(184)= 0.023984293558766304673273158653137477483677710807...
1/40         = 0.025
F-M/40       = -0.452860439791240957084136427542226622770423293690...
```

Thus the frozen lower bound fails at an ordinary integer activation point; no subtle one-sided transition argument can repair the original statement as written.
