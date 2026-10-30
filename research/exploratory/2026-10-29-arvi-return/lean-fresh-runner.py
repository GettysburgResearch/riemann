import resource, subprocess, sys, time
cmd = ['leanchecker', '--fresh', '--verbose', 'Candidate.Main']
print('command:', repr(cmd), flush=True)
start = time.monotonic()
try:
    result = subprocess.run(cmd, timeout=3600)
    status = result.returncode
except subprocess.TimeoutExpired:
    print('timed out after 3600 seconds', flush=True)
    status = 124
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
print(f'wall_seconds={time.monotonic()-start:.3f} user_seconds={usage.ru_utime:.3f} system_seconds={usage.ru_stime:.3f} max_rss_kib={usage.ru_maxrss}', flush=True)
sys.exit(status)
