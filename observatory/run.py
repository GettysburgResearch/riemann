"""Run from any working directory: python /path/to/observatory/run.py."""
from pathlib import Path
import argparse
import json
import sys

def main():
    parser=argparse.ArgumentParser(description="Riemann Observatory v0.1: local research desk")
    parser.add_argument("--port",type=int,default=8765)
    parser.add_argument("--compute",type=Path,help="Run an experiment JSON (request or exported envelope), print result, then exit")
    args=parser.parse_args()
    if args.compute:
        from engine import compute
        payload=json.loads(args.compute.read_text(encoding="utf-8"))
        print(json.dumps(compute(payload.get("request",payload)),ensure_ascii=False,allow_nan=False))
        return
    if not 1024 <= args.port <= 65535:
        parser.error("Choose a port between 1024 and 65535")
    try:
        import uvicorn
    except ImportError:
        sys.exit("Install first: python -m pip install -r observatory/requirements.txt")
    print(f"Riemann Observatory → http://127.0.0.1:{args.port}\nLocal numerical scouts; not a certificate service. Ctrl+C to stop.")
    uvicorn.run("server:app",host="127.0.0.1",port=args.port,app_dir=str(Path(__file__).resolve().parent),workers=1)

if __name__=="__main__":
    main()
