from dataclasses import dataclass
from typing import ClassVar

from zafkiel.ocr import Keyword

"""

"""


@dataclass(repr=False)
class ResourceStage(Keyword):
    instances: ClassVar = {}