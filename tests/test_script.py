from pathlib import Path

log_path = Path("samples/access.log")

with log_path.open() as f:
    for line_number, line in enumerate(f, start=1):
        print(line_number, line.rstrip())