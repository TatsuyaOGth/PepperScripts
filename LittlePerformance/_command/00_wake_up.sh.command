#!/bin/sh

source common.sh
echo "wake up"


for ((i = 0; i < ${SIZE}; ++i))
do
  CMD=${COMMAND}\ ${SRC_DIR}wake_up.py\ ${HOSTS[$i]}\ ${PORTS[$i]}
  if test ${i} -eq ${LAST}
  then
    ${CMD}
  else
    ${CMD} &
  fi
done



exit 0	
