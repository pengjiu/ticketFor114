#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
from dao import BaseDao, Bean
import time
import datetime
from macpath import split
from robot import Robot_114

#提前和延后的时间
robot_range_time=3*60;

#机器唯一编码
def getRobotId():
    return 1;
'''
    重新设置所有的robot hashcode
'''
def makeRobotHashcode():
    pass;

def schedulerUpdatetime():
    settting=BaseDao.querySetting();
    BaseDao.updateRobotDatetimeById(getRobotId());
    #休眠指定时间后再更新
    time.sleep(settting.interval_Of_Task);
    
    
def getLastestTimeByNow(take_ticket_time):
    now = datetime.datetime.now();
    now_seconds=now.hour*3600+now.minute*60+now.second; 
    times=take_ticket_time.split(',');
    times=map(int,times);
    times.sort();
    lastest_time=None;
    for t in times:
        if t>now_seconds:
            lastest_time=t;
            break;
    if lastest_time==None:
        #因为当天没有能抢的时间点，要休眠到第二天第一个时间点
        res=(24*3600-now_seconds)+times[0];
    else:
        res=lastest_time-now_seconds;
    return res;    
def doWorkOfTimer():
    setting=BaseDao.querySetting();
    robot=BaseDao.queryRobotById(getRobotId());
    if robot==None:
        robot=Bean.Robot();
        robot.id=getRobotId();
        BaseDao.saveTask(robot);
        pass;
    lastestTimeDiff=getLastestTimeByNow(setting.take_ticket_time);
    interval_time=lastestTimeDiff-robot_range_time;
    time.sleep(interval_time);
    doWorkAtRegularTime();
    
def doWorkAtRegularTime():
    robots=BaseDao.queryRobotOfAll();
    tasks=BaseDao.queryTaskOfAll();
    robot=Robot_114();
    robot.login();
    
def work():
    while(True):
        doWorkOfTimer();
    
if __name__ == '__main__':
    #work();
    setting="70000,30000,65000";
    now = datetime.datetime.now();
    now_seconds=now.hour*3600+now.minute*60+now.second; 
    lastestTime=getLastestTimeByNow(setting,now_seconds);
    print lastestTime,now_seconds
    