from dataclasses import dataclass

from atlas.models.base import BaseAsset

@dataclass
class BaseJob(BaseAsset):
    asset_type = "Job"
    description: str = "Default Job description"


@dataclass
class ScheduledJob(BaseJob):
    asset_type = "ScheduledJob"
    description: str = "Default ScheduledJob description"
    schedule: str = None
    last_run: str = None
    next_run: str = None
    # job_metadata = None
    # job_parameters = None
    # job_outputs = None
    # job_status = None
    # job_logs = None
    # job_errors = None
    # job_results = None
    # job_artifacts = None
    # job_resources = None
    # job_dependencies = None
    # job_notifications = None
    # job_alerts = None
    # job_history = None
    # job_metrics = None
    # job_monitoring = None
    # job_sla = None
    # job_audit = None
    # job_security = None
    # job_policies = None
    # job_rules

@dataclass
class BatchJob(BaseJob):
    asset_type = "BatchJob"
    description: str = "Default BatchJob description"
    location: str = None
    format: str = None
    created_at: str = None
    last_updated: str = None
    # job_metadata = None
    # job_parameters = None
    # job_outputs = None
    # job_status = None
    # job_logs = None
    # job_errors = None
    # job_results = None
    # job_artifacts = None
    # job_resources = None
    # job_dependencies = None
    # job_notifications = None
    # job_alerts = None
    # job_history = None
    # job_metrics = None
    # job_monitoring = None
    # job_sla = None
    # job_audit = None
    # job_security = None
    # job_policies = None
    # job_rules

@dataclass
class StreamingJob(BaseJob):
    asset_type = "StreamingJob"
    description: str = "Default StreamingJob description"
    location: str = None
    format: str = None
    created_at: str = None
    last_updated: str = None
    # job_metadata = None
    # job_parameters = None
    # job_outputs = None
    # job_status = None
    # job_logs = None
    # job_errors = None
    # job_results = None
    # job_artifacts = None
    # job_resources = None
    # job_dependencies = None
    # job_notifications = None
    # job_alerts = None
    # job_history = None
    # job_metrics = None
    # job_monitoring = None
    # job_sla = None
    # job_audit = None
    # job_security = None
    # job_policies = None
    # job_rules
