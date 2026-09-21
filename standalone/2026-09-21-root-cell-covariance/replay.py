"""Complete deterministic replay and authentication; no numerical scouting."""
from hashlib import sha256
from pathlib import Path
import subprocess
import sys
from core import canonical,need,strict_read

def authenticate(report,expected):
    got=sha256(canonical(report).encode()).hexdigest()
    need(type(expected) is str and got==expected,'semantic report digest')
    return got

def main():
    here=Path(__file__).resolve().parent
    expected=strict_read(here/'EXPECTED.json')
    flags=['-S','-B']+(['-O'] if sys.flags.optimize else [])
    for program,report in [('produce.py','native'),('algebra.py','algebra'),('verify.py','verification')]:
        subprocess.run([sys.executable,*flags,program],cwd=here,check=True)
        authenticate(strict_read(here/'reports'/f'{report}.json'),expected[report])
    subprocess.run([sys.executable,*flags,'test_packet.py'],cwd=here,check=True)
    print('RSC26 COMPLETE REPLAY PASS (finite scope only)')

if __name__=='__main__':main()
