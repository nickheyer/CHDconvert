import os
import subprocess
import sys
from pyunpack import Archive
import shutil

input_dir = input("Input Dir:\n") if len(sys.argv) < 2 else sys.argv[1]
tmp_dir = input_dir + "_tmp"
chdman = os.path.join(os.path.dirname(__file__),'chdman.exe')
operator = sys.argv[3] if (len(sys.argv) == 3 and sys.argv[2] in ["-d", "--delete"]) else None

incoming_files = [f for f in os.listdir(input_dir) if f.split(".")[-1] == "7z"] #only 7z files in that dir
if os.path.exists(tmp_dir) == False:
        os.mkdir(tmp_dir)
for x in incoming_files:
    out = os.path.join(tmp_dir, x.split(".")[0])
    if os.path.exists(out) == False:
        os.mkdir(out)
    Archive(os.path.join(input_dir, x)).extractall(out)
    print(f"{x} has been unarchived.")

    extracted_files = [f for f in os.listdir(out) if f.split(".")[-1] in ["iso", "cue"]] #only isos or cues
    for i in extracted_files:
        output_dir = os.path.join(input_dir + "_out")
        if os.path.exists(output_dir) == False:
            os.mkdir(output_dir)
        cmd = " ".join([chdman, "createcd", "-f", "-i", f'\"{os.path.join(tmp_dir, out, i)}\"', "-o", f'"{output_dir}\\{i.split(".")[0]+".chd"}"'])
        print("COMMAND: " + cmd)
        subprocess.call(cmd)
        print(f"{i} has been converted to chd.")

if operator:
    shutil.rmtree(tmp_dir)
    
