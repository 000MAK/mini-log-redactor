import argparse,re
from pathlib import Path

PATTERNS=[
    (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[A-Za-z0-9._~+/=-]+"),r"\1[REDACTED]"),
    (re.compile(r"(?i)\b(api[_-]?key|access[_-]?token|secret|password)\b(\s*[:=]\s*)([^\s,;]+)"),r"\1\2[REDACTED]"),
    (re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})\b"),"[REDACTED_TOKEN]"),
]
def redact(text):
    for pattern,repl in PATTERNS: text=pattern.sub(repl,text)
    return text

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("output"); a=ap.parse_args(); src,dst=Path(a.input).resolve(),Path(a.output).resolve()
    if src==dst: ap.error("Output must differ from input")
    if dst.exists(): ap.error("Output already exists; choose a new path")
    dst.write_text(redact(src.read_text(encoding="utf-8",errors="replace")),encoding="utf-8"); print(f"Redacted log written to {dst}. Review it manually before sharing.")
if __name__=="__main__": main()
