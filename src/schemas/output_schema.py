from pydantic import BaseModel, HttpUrl
from typing import Optional

class Metadata(BaseModel):
    processId: str
    processName: str
    outputFormat: str

class ProcessOutput(BaseModel):
    status: str
    outputPath: Optional[HttpUrl]
    error: Optional[str]

class OutputModel(BaseModel):
    Metadata: Metadata
    ProcessOutput: ProcessOutput

class OutputFile(BaseModel):
    local_path: str
    name: str
    type: Optional[str]

OUTPUT_FILES: list[OutputFile] = []  # List output files HERE
