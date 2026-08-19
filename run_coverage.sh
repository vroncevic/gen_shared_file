#!/bin/bash
#
# @brief   gen_shared_file
# @version 1.0.3
# @date    Sun Aug 09 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_shared_file
pylint gen_shared_file > gen_shared_file.report
echo "Done"
