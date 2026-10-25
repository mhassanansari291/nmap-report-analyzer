#!/usr/bin/env python3
"""Summarize open services from an existing Nmap normal-output file."""
import argparse
import csv
import re
import sys
from pathlib import Path

PORT_RE = re.compile(r"^\s*(\d{1,5})/(tcp|udp)\s+open\s+(\S+)(?:\s+(.*))?$", re.I)

def parse_nmap(path):
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise RuntimeError(f"Cannot read input file '{path}': {exc}") from exc
    host_match = re.search(r"Nmap scan report for\s+(.+)", content)
    host = host_match.group(1).strip() if host_match else "Unknown target"
    services = []
    for line in content.splitlines():
        match = PORT_RE.match(line)
        if match:
            port, protocol, service, details = match.groups()
            services.append({"port": port, "protocol": protocol.lower(),
                             "service": service, "details": (details or "").strip()})
    return host, services

def main():
    parser = argparse.ArgumentParser(
        description="Summarize open services from an existing Nmap -oN output file.")
    parser.add_argument("input", help="Nmap normal-output file, e.g. initial-scan.txt")
    parser.add_argument("-o", "--output", default="nmap-summary.md",
                        help="Markdown output path (default: nmap-summary.md)")
    parser.add_argument("--csv", help="Optional CSV output path")
    args = parser.parse_args()
    source = Path(args.input).expanduser()
    if not source.is_file():
        print(f"Error: input file not found: {source}", file=sys.stderr)
        return 2
    try:
        host, services = parse_nmap(source)
        lines = ["# Nmap Service Summary", "",
                 f"- **Input file:** `{source}`", f"- **Target:** `{host}`",
                 f"- **Open services parsed:** {len(services)}", ""]
        if services:
            lines += ["| Port | Protocol | Service | Version / Details |",
                      "|---:|:---:|---|---|"]
            for item in services:
                detail = item["details"].replace("|", "\\|") or "Not provided"
                lines.append(f"| {item['port']} | {item['protocol']} | {item['service']} | {detail} |")
        else:
            lines += ["No matching open-port lines were found.",
                      "Check that the input is an Nmap `-oN` output file."]
        lines += ["", "> This tool summarizes existing scan output only. It does not scan, "
                  "validate vulnerabilities, or exploit targets.", ""]
        output = Path(args.output).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(lines), encoding="utf-8")
        print(f"Markdown report written to: {output}")
        print(f"Target: {host}")
        print(f"Open services parsed: {len(services)}")
        if args.csv:
            csv_path = Path(args.csv).expanduser()
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["port", "protocol", "service", "details"])
                writer.writeheader()
                writer.writerows(services)
            print(f"CSV report written to: {csv_path}")
        return 0
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
