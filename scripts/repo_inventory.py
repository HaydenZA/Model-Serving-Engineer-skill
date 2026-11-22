#!/usr/bin/env python3
"""Create a deterministic, non-secret inventory of a model-serving repository."""
from __future__ import annotations
import argparse, json, os, subprocess
from pathlib import Path

MANIFESTS = {"CMakeLists.txt", "Cargo.toml", "go.mod", "pyproject.toml", "requirements.txt", "package.json", "Dockerfile", "compose.yaml", "docker-compose.yml", "Makefile", "BUILD", "WORKSPACE"}
LOCK_SUFFIXES = (".lock", "-lock.json")
SKIP = {".git", ".venv", "venv", "node_modules", "target", "build", "dist", "models", ".cache"}
SECRET_WORDS = ("token", "secret", "password", "credential", "private_key")

def git(root: Path, *args: str) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(root), *args], text=True, stderr=subprocess.DEVNULL, timeout=10).strip()
    except Exception:
        return None

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--output")
    ns = ap.parse_args()
    root = Path(ns.root).resolve()
    if not root.is_dir():
        ap.error("root must be a directory")
    files, manifests = [], []
    counts: dict[str, int] = {}
    for base, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP)
        for name in sorted(names):
            p = Path(base) / name
            rel = p.relative_to(root).as_posix()
            lower = rel.lower()
            if any(word in lower for word in SECRET_WORDS) or name.startswith(".env"):
                continue
            files.append(rel)
            ext = p.suffix.lower() or "[none]"
            counts[ext] = counts.get(ext, 0) + 1
            if name in MANIFESTS or name.endswith(LOCK_SUFFIXES) or rel.startswith((".github/workflows/", ".forgejo/workflows/")):
                manifests.append(rel)
    data = {
        "root": str(root),
        "git": {"commit": git(root, "rev-parse", "HEAD"), "branch": git(root, "branch", "--show-current"), "status": git(root, "status", "--porcelain"), "remotes": git(root, "remote", "-v")},
        "file_count": len(files), "extensions": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
        "manifests_and_ci": manifests, "top_level": sorted(p.name for p in root.iterdir() if p.name != ".git")
    }
    text = json.dumps(data, indent=2)
    if ns.output:
        Path(ns.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
