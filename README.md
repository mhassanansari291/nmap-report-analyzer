# Nmap Report Analyzer

A Python CLI tool that reads an **existing Nmap normal-output file** (`-oN`) and summarizes open services into Markdown and optional CSV.

## Features
- Extracts target label and open TCP/UDP service rows.
- Creates Markdown and optional CSV output.
- Handles missing/unreadable input files with an error message.
- Does not scan, authenticate to, or exploit any network target.

## Requirements
- Python 3.9+
- No third-party packages

## Usage
```bash
python3 nmap_report_analyzer.py initial-scan.txt
```
Writes `nmap-summary.md`.

To choose the output path and also create CSV:
```bash
python3 nmap_report_analyzer.py initial-scan.txt -o report.md --csv services.csv
```

Help:
```bash
python3 nmap_report_analyzer.py --help
```

## Example
For an input line `21/tcp open ftp vsftpd 2.3.4`, the output table includes port `21`, protocol `tcp`, service `ftp`, and details `vsftpd 2.3.4`.

## Limitations
This parses Nmap's normal text output and may not handle every wrapped or unusual format. It does not decide whether a service is vulnerable. Review results manually.

## Ethical use
Only scan systems you own or have explicit permission to test. This project itself only parses a local text file.

## License
MIT; see `LICENSE`.
