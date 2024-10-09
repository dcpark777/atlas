from dataclasses import dataclass

from atlas.models.base import BaseAsset

@dataclass
class BaseModel(BaseAsset):
    asset_type = "Model"
    description: str = "Default Model description"
    created_at: str = None
    last_updated: str = None
    location: str = None

@dataclass
class DeepLearningModel(BaseModel):
    asset_type = "DeepLearningModel"
    description: str = "Default DeepLearningModel description"
    model_type: str = None
    framework: str = None
    # training_metadata = None
    # inputs = None
    # outputs = None