"""Regenerate complete reports, authenticate semantic receipts, verify and test."""
import hashlib,subprocess,sys
from pathlib import Path
import transport,harmonic,kernel_samples,verify
from arithmetic import canonical,strict_read,require

def main():
    root=Path(__file__).parent;out=root/'reports';out.mkdir(exist_ok=True)
    expected=strict_read(root/'EXPECTED.json')
    for name,make in (('transport_result.json',transport.build),
                      ('harmonic_result.json',harmonic.build),
                      ('kernel_samples.json',kernel_samples.build)):
        text=canonical(make());digest=hashlib.sha256(text.encode()).hexdigest()
        require(digest==expected[name],'semantic receipt differs: '+name)
        (out/name).write_text(text+'\n')
        print('REPLAY',name,digest,flush=True)
    scope=verify.run(out)
    require(canonical(scope)==canonical(strict_read(root/'verification_scope.json')),'verification scope differs')
    args=[sys.executable,'-S','-B']
    if sys.flags.optimize:args.append('-O')
    subprocess.run(args+[str(root/'test_packet.py')],check=True,cwd=root)
    print('DCN26 REPLAY PASS',canonical(scope),flush=True)
if __name__=='__main__':main()
