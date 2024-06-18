
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input_sample': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'input_cycle': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'marker_sheet': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title=None,
        description='Path to comma-separated file containing information about the markers',
    ),
    'illumination': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='input that defines type of illumination correction to be performed',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

