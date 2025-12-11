import sys
import os
import subprocess

if len(sys.argv) < 4:
    print("Usage: python trimmp3.py input.mp3 start_timestamp end_timestamp [output.mp3]")
    sys.exit(1)

input_file = sys.argv[1]
start = sys.argv[2]   # e.g. "1:03"
end = sys.argv[3]     # e.g. "2:37"

# Default output name: input_trimmed.mp3
output_file = (
    sys.argv[4]
    if len(sys.argv) > 4
    else os.path.splitext(input_file)[0] + "_trimmed.mp3"
)

result = subprocess.run(
    [
        "ffmpeg",
        "-i", input_file,
        "-ss", start,
        "-to", end,
        "-c", "copy",
        output_file
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0:
    print(f"Successfully created '{os.path.basename(output_file)}'")
else:
    print("Trimming failed.")
