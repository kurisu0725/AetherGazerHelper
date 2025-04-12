from dataclasses import dataclass
from typing import ClassVar, Optional

from zafkiel.ocr import Keyword


@dataclass(repr=False)
class ResourceStage(Keyword):
    instances: ClassVar = {}
    switch_name: Optional[str] = None
    list_idx: Optional[int] = None

    def __post_init__(self):
        super().__post_init__()
        assert isinstance(self.switch_name, (str, type(None))),  "switch_name必须是字符串或None"
        assert isinstance(self.list_idx, (int, type(None))),  "list_idx必须是整数或None"

@dataclass(repr=False)
class ActivityOption(Keyword):
    instances: ClassVar = {}