#!/bin/sh
basedir="/home/pi/software/raspi"
logpath=${basedir}"/log/"

#删除当前log
sudo rm -rf ${logpath}"*.log"

#进入cam目录
cd $basedir

#后台运行监控脚本
nohup python -u raspi_run.py > ${logpath}"web.log"  2>&1 &
