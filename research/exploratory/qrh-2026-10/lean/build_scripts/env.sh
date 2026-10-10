export S=${LEANBUILD:?set LEANBUILD to your scratch dir}
export ELAN_HOME=$S/elan
export PATH=$S/elan/bin:$PATH
export P=$S/src/standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean
export GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1
export LEAN_NUM_THREADS=2
