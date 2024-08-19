from wf.task import task

from latch.resources.workflow import workflow
from latch.types.directory import LatchOutputDir
from latch.types.file import LatchFile
from latch.types.metadata import LatchAuthor, LatchMetadata, LatchParameter

metadata = LatchMetadata(
    display_name="Curio Demo Workflow",
    author=LatchAuthor(
        name="LatchBio",
    ),
    parameters={
        "fastq_file": LatchParameter(
            display_name="Fastq File",
            batch_table_column=True,  # Show this parameter in batched mode.
        ),
        "output_directory": LatchParameter(
            display_name="Output Directory",
            batch_table_column=True,  # Show this parameter in batched mode.
        ),
        "threshold": LatchParameter(
            display_name="Threshold",
            batch_table_column=True,  # Show this parameter in batched mode.
        ),
    },
)


@workflow(metadata)
def template_workflow(
    fastq_file: LatchFile, output_directory: LatchOutputDir, threshold: int
) -> LatchOutputDir:
    return task(fastq_file=fastq_file, output_directory=output_directory)
