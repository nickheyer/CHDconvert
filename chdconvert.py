import os
import subprocess
import sys
from pyunpack import Archive
import shutil

input_dir = input("Input Dir:\n") if len(sys.argv) < 2 else sys.argv[1]
tmp_dir = input_dir + "_tmp"
chdman = os.path.join(os.path.dirname(__file__),'chdman.exe')
operator = sys.argv[2] if (len(sys.argv) == 3 and sys.argv[2] in ["-d", "--delete", "-r", "--replace"]) else None

incoming_files = [f for f in os.listdir(input_dir) if f.split(".")[-1] == "7z"] #only 7z files in that dir
if os.path.exists(tmp_dir) == False:
        os.mkdir(tmp_dir)
for x in incoming_files:
    out = os.path.join(tmp_dir, x.split(".")[0])
    if os.path.exists(out) == False:
        os.mkdir(out)
    inp = os.path.join(input_dir, x)
    print(f"Unarchiving {inp}")
    Archive(inp).extractall(out)
    print(f"{x} has been unarchived.")

    extracted_files = [f for f in os.listdir(out) if f.split(".")[-1] in ["iso", "cue"]] #only isos or cues
    for i in extracted_files:
        if operator in ["-r", "--replace"]:
            p = os.path.join(input_dir, x)
            os.remove(p)
            print(f"{p} removed after unarchiving.")
            output_dir = input_dir
        else:
            output_dir = os.path.join(input_dir + "_out")
        if os.path.exists(output_dir) == False:
            os.mkdir(output_dir)
        out_path = f'"{os.path.join(output_dir, ".".join(i.split(".")[:-1]))}.chd"'
        cmd = " ".join([chdman, "createcd", "-f", "-i", f'\"{os.path.join(tmp_dir, out, i)}\"', "-o", out_path])
        print("COMMAND: " + cmd)
        subprocess.call(cmd)
        print(f"{i} has been converted to chd.")
    
    if operator:
        shutil.rmtree(tmp_dir)
    
