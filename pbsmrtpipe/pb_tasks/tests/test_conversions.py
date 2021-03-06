import unittest
import logging
import os.path as op
import subprocess

from pbcommand.testkit import PbTestApp
from pbcommand.utils import which

log = logging.getLogger(__name__)

DATA = op.join(op.dirname(__file__), "data")


class Constants(object):
    BAX2BAM = "bax2bam"
    BAM2FASTA = "bam2fasta"

# XXX hacks to make sure tools are actually available
HAVE_BAX2BAM = which(Constants.BAX2BAM) is not None
HAVE_BAM2FASTX = which(Constants.BAM2FASTA) is not None
DATA_DIR = "/mnt/secondary-siv/testdata"
HAVE_DATA_DIR = op.isdir(DATA_DIR)

@unittest.skipUnless(HAVE_BAX2BAM and HAVE_DATA_DIR, "Missing bax2bam")
class TestBax2Bam(PbTestApp):
    TASK_ID = "pbsmrtpipe.tasks.h5_subreads_to_subread"
    DRIVER_EMIT = 'python -m pbsmrtpipe.pb_tasks.pacbio emit-tool-contract {i} '.format(i=TASK_ID)
    DRIVER_RESOLVE = 'python -m pbsmrtpipe.pb_tasks.pacbio run-rtc '

    # User Provided values
    # Abspath'ed temp files will be automatically generated
    INPUT_FILES = [
        DATA_DIR + "/SA3-RS/lambda/2372215/0007_tiny/m150404_101626_42267_c100807920800000001823174110291514_s1_p0.hdfsubread.xml",
    ]
    MAX_NPROC = 24

    RESOLVED_NPROC = 1
    RESOLVED_TASK_OPTIONS = {}
    RESOLVED_IS_DISTRIBUTED = True


@unittest.skipUnless(HAVE_BAM2FASTX and HAVE_DATA_DIR, "Missing bam2fastx")
class TestBam2Fasta(PbTestApp):
    TASK_ID = "pbsmrtpipe.tasks.bam2fasta"
    DRIVER_EMIT = 'python -m pbsmrtpipe.pb_tasks.pacbio emit-tool-contract {i} '.format(i=TASK_ID)
    DRIVER_RESOLVE = 'python -m pbsmrtpipe.pb_tasks.pacbio run-rtc '
    INPUT_FILES = [ "/mnt/secondary-siv/testdata/SA3-DS/lambda/2372215/0007_micro/Analysis_Results/m150404_101626_42267_c100807920800000001823174110291514_s1_p0.all.subreadset.xml" ]
    MAX_NPROC = 24
    RESOLVED_NPROC = 1
    RESOLVED_TASK_OPTIONS = {}
    RESOLVED_IS_DISTRIBUTED = True


@unittest.skipUnless(HAVE_BAM2FASTX and HAVE_DATA_DIR, "Missing bam2fastx")
class TestBam2Fastq(TestBam2Fasta):
    TASK_ID = "pbsmrtpipe.tasks.bam2fastq"
