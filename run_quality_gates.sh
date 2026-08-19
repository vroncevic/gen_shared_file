#!/bin/bash
#
# @brief   gen_shared_file
# @version 1.0.3
# @date    Sun Aug 09 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_shared_file
python3 gates/gates/isp_checker.py gen_shared_file
python3 gates/gates/limits_checker.py gen_shared_file
python3 gates/gates/srp_checker.py gen_shared_file

echo "Done"
