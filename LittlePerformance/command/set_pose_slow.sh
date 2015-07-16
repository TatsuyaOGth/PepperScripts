#!/bin/sh

cd `dirname $0`
source common.sh

echo "set pose"


for ((i = 0; i < ${SIZE}; ++i))
do
  CMD=${COMMAND}\ ${SRC_DIR}default_pose.py\ ${HOSTS[$i]}\ '0.1'
  if test ${i} -eq ${LAST}
  then
    ${CMD}
  else
    ${CMD} &
  fi
done

exit 0	
