"""Build the pinned original djplatt/arb_zeta in a separate Debian amd64 workspace."""
import argparse
import hashlib
import os
import subprocess
import urllib.request
from pathlib import Path

REVISION = "d918aa093a304819a0f7d1c27bfaf67c8c0f0602"
PACKAGES = {
    "f/flint-arb/libflint-arb-dev_2.23.0-1+b1_amd64.deb": "2a32102e1dca67b9b0cdf4ce1c03bcd9b44da66be7d5a18c7cda2f62bed7cfea",
    "f/flint-arb/libflint-arb2_2.23.0-1+b1_amd64.deb": "d1adcc0d0a18dea0ff06f34085d13bbeb9ed50cedea7eda2584c4f1dd42f2bb4",
    "f/flint/libflint-dev_2.9.0-5_amd64.deb": "134855d68e018fb01e103eca2e43470cda9243744ca176d0210e0f8c02769fa5",
    "f/flint/libflint17_2.9.0-5_amd64.deb": "114f2ec9184fdfd5de242bb14c5ff134e578ebee1eb5d5f3fcd2acc7405cb107",
    "m/mpfr4/libmpfr-dev_4.2.0-1_amd64.deb": "9831a86897b68d401ff371a3af5ac2c29b4f9447e0228731ec9f2e571fef3fe5",
    "n/ntl/libntl44_11.5.1-1+b2_amd64.deb": "1ec859c23f8875141a2ddb4c7a81f0a1b837b64cd4cb822917b1e3f725c4540e",
    "g/gf2x/libgf2x3_1.3.0-1+b1_amd64.deb": "0a23432f3abaea3e0882aeb23d51ae978fbf9199bdebce9a088f7a072ac0abff",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workdir", type=Path)
    root = parser.parse_args().workdir.resolve()
    libs = root / "old-libs"
    libs.mkdir(parents=True, exist_ok=True)
    src = root / "platt-original"
    if not src.exists():
        subprocess.run(["git", "init", str(src)], check=True)
        subprocess.run(["git", "-C", str(src), "fetch", "--depth", "1",
                        "https://github.com/djplatt/arb_zeta.git", REVISION], check=True)
        subprocess.run(["git", "-C", str(src), "checkout", "--detach", REVISION], check=True)
    head = subprocess.check_output(["git", "-C", str(src), "rev-parse", "HEAD"], text=True).strip()
    if head != REVISION or subprocess.run(["git", "-C", str(src), "diff", "--quiet", REVISION]).returncode:
        raise RuntimeError("Expected the exact original revision, with clean tracked sources")
    for package, checksum in PACKAGES.items():
        path = libs / Path(package).name
        if not path.exists():
            urllib.request.urlretrieve("https://deb.debian.org/debian/pool/main/" + package, path)
        if hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
            raise RuntimeError(f"Unexpected Debian package digest: {path}")
        subprocess.run(["dpkg-deb", "-x", str(path), str(libs)], check=True)
    shared = libs / "usr/lib/x86_64-linux-gnu"
    includes = libs / "usr/include"
    sources = subprocess.check_output(["git", "-C", str(src), "ls-files", "*.c"], text=True).splitlines()
    subprocess.run(["gcc", "-O2", f"-I{includes}", f"-I{includes/'flint'}", *sources,
                    f"-L{shared}", f"-Wl,-rpath-link,{shared}", "-lflint-arb", "-lflint",
                    "-lm", "-o", "arb_zeta"], check=True, cwd=src,
                   env={**os.environ, "LD_LIBRARY_PATH": str(shared)})
    audit = Path(__file__).with_name("check_buckets.c").resolve()
    subprocess.run(["gcc", "-O2", f"-I{includes}", f"-I{includes/'flint'}", str(audit),
                    "win_zeta.c", f"-L{shared}", f"-Wl,-rpath-link,{shared}", "-lflint-arb",
                    "-lflint", "-o", str(root/"check-historical-buckets")], check=True, cwd=src,
                   env={**os.environ, "LD_LIBRARY_PATH": str(shared)})
    subprocess.run([str(root/"check-historical-buckets")], check=True,
                   env={**os.environ, "LD_LIBRARY_PATH": str(shared)})
    binary = src / "arb_zeta"
    print(f"{binary}  sha256={hashlib.sha256(binary.read_bytes()).hexdigest()}")
    print(f"LD_LIBRARY_PATH={shared}")


if __name__ == "__main__":
    main()
