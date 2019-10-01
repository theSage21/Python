import os
from pathlib import Path
from shutil import rmtree

old = Path("old")
new = Path("new")

for group in sorted(os.listdir(old)):
    if not os.path.exists(new / group):
        os.mkdir(new / group)
    for file in os.listdir(old / group):
        if (
            os.path.isdir(old / group / file)
            or os.path.exists(new / group / file)
            or os.path.exists(f"stats/{file}.failed")
        ):
            continue
        os.system(f"touch stats/{file}.failed")
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
        ok = True
        for cmd in [
            f"python {new/group/file}",
            f"pyannotate --py3 -p --type-info stats/{file} -w {new/group/file}",
        ]:
            x = os.system(cmd)
            if x != 0:
                os.system(f"rm {new / group / file}")
                ok = False
                continue
        if ok:
            with open(new / group / file, "r") as fl:
                code = "".join(list(fl.readlines())[5:-4])
            with open(new / group / file, "w") as fl:
                fl.write(code)
            os.system(f"rm stats/{file}.failed")
