from typing import List

from pydantic import BaseModel, Field

__all__ = ["DockerSync"]


class DockerSync(BaseModel):
    src: str = Field(..., title="源镜像", description="Docker源镜像")
    dst: List[str] = Field(..., title="目的镜像列表", description="要同步到这些地方")
    tag: List[str] = Field(..., title="Tag列表", description="要同步的 Tag 列表")
