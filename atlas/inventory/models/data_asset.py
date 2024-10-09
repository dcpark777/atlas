from dataclasses import dataclass

from atlas.models.base import BaseAsset

@dataclass
class BaseData(BaseAsset):
    asset_type = "Data" # maybe pull this from super class's name? or super class. make an enum for asset types
    description: str = "Default DataAsset description"
    location: str = None
    format: str = None
    created_at: str = None # maybe make this timestamp?

@dataclass
class Dataset(BaseData):
    asset_type = "Dataset"
    description: str = "Default Dataset description"
    # schema = None # maybe add schema here?