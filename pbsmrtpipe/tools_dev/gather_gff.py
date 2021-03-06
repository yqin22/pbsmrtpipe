import logging
from pbcommand.cli import pbparser_runner
from pbcommand.models import get_gather_pbparser, FileTypes
import sys
from pbcommand.utils import setup_log
from pbsmrtpipe.tools.gather import run_main_gather_gff

log = logging.getLogger(__name__)


class Constants(object):
    TOOL_ID = "pbsmrtpipe.tasks.gather_gff"
    CHUNK_KEY = "$chunk.gff_id"
    VERSION = "0.1.0"
    DRIVER = "python -m pbsmrtpipe.tools_dev.gather_gff --resolved-tool-contract "
    OPT_CHUNK_KEY = '"pbsmrtpipe.task_options.gff_gather_chunk_key"'


def get_parser():
    p = get_gather_pbparser(Constants.TOOL_ID,
                            Constants.VERSION,
                            "Dev Gff Gather",
                            "General Chunk Gff Gather",
                            Constants.DRIVER,
                            is_distributed=False)
    p.add_input_file_type(FileTypes.CHUNK, "cjson_in", "GCHUNK Json",
                          "Gathered CHUNK Json with Gff chunk key")
    p.add_output_file_type(FileTypes.GFF, "gff_out", "Gff", "Gathered Gff", "gathered.gff")

    p.arg_parser.add_str(Constants.OPT_CHUNK_KEY,
                         "chunk_key",
                         "$chunk.gff_id",
                         "Chunk key", "Chunk key to use (format $chunk:{chunk-key}")
    return p


def args_runner(args):
    return run_main_gather_gff(args.cjson_in, args.gff_out, args.chunk_key)


def rtc_runner(rtc):
    return run_main_gather_gff(rtc.task.input_files[0], rtc.task.output_files[0], rtc.task.chunk_key)


def main(argv=sys.argv):
    return pbparser_runner(argv[1:],
                           get_parser(),
                           args_runner,
                           rtc_runner,
                           log,
                           setup_log)


if __name__ == '__main__':
    sys.exit(main())
