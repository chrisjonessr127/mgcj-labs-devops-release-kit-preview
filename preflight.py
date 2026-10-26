#!/usr/bin/env python3
"""Local command-presence check. No installs or AWS API calls."""
import shutil
import subprocess
import sys


def check(label, args):
    if shutil.which(args[0]) is None:
        print(f"MISSING: {label}")
        return False
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        print(f"UNAVAILABLE: {label}")
        return False
    if result.returncode != 0:
        print(f"UNAVAILABLE: {label}")
        return False
    lines = (result.stdout or result.stderr).strip().splitlines()
    print(f"OK: {label}" + (f" — {lines[0]}" if lines else ""))
    return True


def main():
    print("MGCJ Labs — local tool check")
    print(f"Python: {sys.version.split()[0]}")
    checks = [
        ("Git", ["git", "--version"]),
        ("GitHub CLI", ["gh", "--version"]),
        ("Terraform", ["terraform", "version"]),
        ("AWS CLI", ["aws", "--version"]),
        ("Docker CLI", ["docker", "--version"]),
        ("Docker engine", ["docker", "info", "--format", "{{.ServerVersion}}"]),
        ("Docker Buildx", ["docker", "buildx", "version"]),
    ]
    results = [check(label, args) for label, args in checks]
    print("No cloud resources were created. This check does not validate kit compatibility.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
