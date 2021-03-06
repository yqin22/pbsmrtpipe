"""Place for dev integration tests"""
import unittest
import logging

from test_integration import _TestDriverPipelineId
from base import HAS_CLUSTER_QSUB

log = logging.getLogger(__name__)


class DevLocalDriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_local"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


@unittest.skipIf(not HAS_CLUSTER_QSUB, "No qsub exe found.")
class DevLocalChunkDriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_local_chunk"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


@unittest.skipIf(not HAS_CLUSTER_QSUB, "No qsub exe found.")
class DevDistDriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_dist"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


class Dev01DriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_01"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


class Dev02DriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_02"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


class Dev03DriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_03"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


class Dev04DriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_04"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}


class DevLocalWithStaticTaskDriverIntegration(_TestDriverPipelineId):
    WORKFLOW_XML = "pbsmrtpipe.pipelines.dev_04_w_static_task"
    JOB_NAME = WORKFLOW_XML
    ENTRY_POINTS = {'e_01': "hello_entry_point.txt"}
