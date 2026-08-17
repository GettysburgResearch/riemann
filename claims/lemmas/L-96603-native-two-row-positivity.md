# L-96603 — The finite terminal source equals the two native Mobius rows

Apply `L-96601` to the native parity source and `L-96602` to every terminal leaf. Every substitution is an exact source equality, every occurrence has one owner, and all terminal rows are nonnegative. Therefore, for every real `X>=1`,

```text
c_X(2)>=0,
c_X(3)>=0.
```

The sparse coefficient dictionaries are

```text
a_2(n)=1_(n=1)-mu(n)+2 1_(2|n)mu(n/2)-1_(3|n)mu(n/3),

3a_3(n)=1_(n=1)-mu(n)-1_(2|n)mu(n/2)
         +5 1_(3|n)mu(n/3)-3 1_(4|n)mu(n/4).
```
