from pathlib import Path

p = Path(r"C:\Users\admin\Documents\Upyog\upyog-mdms-data\data\pg\tenant\citymodule.json")
text = p.read_text(encoding="utf-8")

if '"code": "pg.karjat"' in text:
    print("pg.karjat already present")
    raise SystemExit(0)

needle = """        {
          \"code\": \"pg.citya\"
        }"""
insert = """        {
          \"code\": \"pg.citya\"
        },
        {
          \"code\": \"pg.karjat\"
        }"""

count = text.count(needle)
if count == 0:
    raise SystemExit("pattern not found for pg.citya")

p.write_text(text.replace(needle, insert), encoding="utf-8")
print(f"inserted pg.karjat after {count} pg.citya entries")
