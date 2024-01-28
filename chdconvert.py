import os
import subprocess
import sys
from pyunpack import Archive
import shutil

input_dir = input("Input Dir:\n") if len(sys.argv) < 2 else sys.argv[1]
tmp_dir = input_dir + "_tmp"
chdman = os.path.join(os.path.dirname(__file__), 'chdman.exe')
operator = sys.argv[2] if (len(sys.argv) == 3 and sys.argv[2] in ["-d", "--delete", "-r", "--replace"]) else None
error_log_file = "skipped_archives.txt"

# Updated to handle both gz and 7z files
incoming_files = [f for f in os.listdir(input_dir) if f.split(".")[-1] in ["gz", "7z"]]  
for x in incoming_files:
    try:
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)
        archive_name = x.rsplit(".", 1)[0]
        out = os.path.join(tmp_dir, archive_name)  # Updated to handle file names with multiple periods
        if not os.path.exists(out):
            os.mkdir(out)
        inp = os.path.join(input_dir, x)
        print(f"Unarchiving {inp}")
        Archive(inp).extractall(out)
        print(f"{x} has been unarchived.")

        extracted_files = [f for f in os.listdir(out) if f.split(".")[-1] in ["iso", "cue"]]  
        for i in extracted_files:
            if operator in ["-r", "--replace"]:
                p = os.path.join(input_dir, x)
                os.remove(p)
                print(f"{p} removed after unarchiving.")
                output_dir = input_dir
            else:
                output_dir = os.path.join(input_dir + "_out")
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            out_path = f'"{os.path.join(output_dir, archive_name)}.chd"' # Use archive name for CHD file  
            cmd = " ".join([chdman, "createcd", "-f", "-i", f'\"{os.path.join(tmp_dir, out, i)}\"', "-o", out_path])
            print("COMMAND: " + cmd)
            subprocess.call(cmd)
            print(f"{i} has been converted to chd.")

        if operator:
            shutil.rmtree(tmp_dir)

    except Exception as e:
        print(f"Error processing {x}: {e}")
        with open(error_log_file, "a") as error_log:
            error_log.write(f"{x}: {str(e)}\n")
