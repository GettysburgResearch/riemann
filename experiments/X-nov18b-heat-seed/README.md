# Reproduce the heat-flow strip comparison

The script recomputes a global upper bound for the de Bruijn–Newman constant from a supplied upper bound for the real parts of the nontrivial zeta zeros. Run with Python 3 and python-flint (tested with version 0.9.0).

~~~sh
python check.py --constants
python check.py 7/8
python check.py 10499/12000
python check.py 873345856107/1000000000000
~~~

The default time step is $1/8192000$. The last two commands use stronger external zero-free theorems or claims than the first one. Each command prints the exact rational endpoint and an upward decimal rounding. The mathematical comparison, its external analytic inputs, and the provenance of each seed are in the [research note](../../research/explorations/nov18b-heat-seed.md).

## Input data and license

Dale James Raymond released *Proof and replay materials for Lambda ≤ 0.107964910079*, version 1.0, dated 29 October 2026, under CC BY 4.0. The included compact archive repackages two unmodified JSON files from the published proof archive. It changes their archive paths and compression. [Source record and original archive](https://doi.org/10.5281/zenodo.23752103) · [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/)

| File in the compact archive | SHA-256 of uncompressed bytes |
|---|---|
| M8_LATE_PLAN.json | ec346b7c1136eda38021eb6323033b3b48ed21e6f7458eeeac7cc9579db2497a |
| MAIN_CLOCK_SOURCE.json | b59905d7b994d3424ba14f9347be75a2429ae4d4b0de2c2404971ffda1d4d536 |

The new checker imports the mathematical validity of Raymond's finite-head wall, physical logarithmic-derivative sources, and full signed kernels. Its own rational computations check the heat-time coverage used, every incoming contact cap, the complete signed own-pair value, the directed reset and the positive terminal-strip cleanup. The two files and these checks suffice for reproducing the new integration with those inputs.

For the four entries in the converse table the time step is $1/512000$.

~~~sh
python check.py 12433/20000 --ticks 512000
python check.py 68973/100000 --ticks 512000
python check.py 76061/100000 --ticks 512000
python check.py 422139/500000 --ticks 512000
~~~
