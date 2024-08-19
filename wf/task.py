from latch.resources.tasks import small_task
from latch.types.directory import LatchOutputDir
from latch.types.file import LatchFile
import subprocess
import sys
import os

@small_task
def task(fastq_file: LatchFile, output_directory: LatchOutputDir) -> LatchOutputDir:
    os.makedirs("/root/results", exist_ok=True)

    print("Hello world")

    fastqc_cmd = [
        "fastqc",
        "--outdir", "/root/results",
        fastq_file.local_path
    ]

    try:
        result = subprocess.run(fastqc_cmd, check=True, capture_output=True, text=True)

        print("FastQC completed successfully.")
        print("Output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error running FastQC: {e}")
        print("Error output:")
        print(e.stderr)
        sys.exit(1)

    return LatchOutputDir("/root/results", output_directory.remote_directory)

