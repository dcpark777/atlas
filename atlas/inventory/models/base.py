from dataclasses import dataclass

@dataclass
class BaseAsset:
    id: int = None
    name: str = None
    description: str = "Default description"