#!/bin/bash
#
# @brief   gen_shared_file
# @version v1.0.1
# @date    Sun Jun  9 07:07:23 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf myipc
python3 -m coverage run -m --source=../gen_shared_file unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html

