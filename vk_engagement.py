#!/usr/bin/env python3
"""Engagement rate and subscriber growth for a VK page.

Reads a CSV of your own post stats (export from the page you manage).
Columns per line: date,subscribers,likes,comments,reposts

Usage: python vk_engagement.py posts.csv
"""
import csv
import sys


def main(path: str) -> int:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            subs = int(r["subscribers"])
            er = (int(r["likes"]) + int(r["comments"]) + int(r["reposts"])) / subs * 100
            rows.append((r["date"], subs, er))
    if not rows:
        print("no rows", file=sys.stderr)
        return 1
    for date, subs, er in rows[-14:]:
        print(f"{date}  subs={subs}  er={er:.2f}%")
    avg = sum(er for _, _, er in rows) / len(rows)
    growth = (rows[-1][1] - rows[0][1]) / rows[0][1] * 100
    print(f"\naverage ER: {avg:.2f}%")
    print(f"subscriber growth over period: {growth:+.1f}%")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
