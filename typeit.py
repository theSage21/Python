import os
from pathlib import Path

old = Path("old")
new = Path("new")

for group in sorted(os.listdir(old)):
    if not os.path.exists(new / group):
        os.mkdir(new / group)
    for file in os.listdir(old / group):
        with open(old / group / file, "r") as fl:
            code = f"""
from pyannotate_runtime import collect_types
collect_types.init_types_collection()
collect_types.start()
{fl.read()}
collect_types.stop()
collect_types.dump_stats('stats/{file}')
            """
        with open(new / group / file, "w") as fl:
            fl.write(code)
        print("\n" * 80)
        print(new / group / file)
        os.system(f"python {new/group/file}")
        os.system(f"pyannotate --py3 -p --type-info stats/{file} -w {new/group/file}")
        with open(new / group / file, "r") as fl:
            code = "".join(list(fl.readlines())[5:-4])
        with open(new / group / file, "w") as fl:
            fl.write(code)
