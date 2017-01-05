#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
from dao import BaseDao, Bean
import time
import datetime
from macpath import split

#提前和延后的时间
robot_range_time=3*60;

__robotId=None;
#机器唯一编码
def getRobotId():
    if __robotId==None:
        __robotId=1;
    return __robotId;
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
   
def getBound():
    upbound=downbound=-1;
    robots=BaseDao.queryRobotOfAll();
    robots=sorted(robots,key=robots.hashcode);
    if len(robots)==0:
        raise Exception("getBound len(robots)==0 ,robot列表为空 ，"+getRobotId());
    for robot in robots:
        if robot.id==getRobotId():
            upbound=robot.hascode;
        elif upbound>-1 and robot.hashcode>upbound:
            downbound=robot.hashcod;
            break;
    if upbound==-1:
        raise Exception("getBound upbound==-1 ,没有找到robot ，"+getRobotId());
    if downbound==-1:
        downbound=robots[0];
    return {"upbound":upbound,"downbound":downbound};
def doWorkAtRegularTime():
    bounds=getBound();
    upbound=bounds["upbound"];
    downbound=bounds["downbound"];
    tasks=BaseDao.queryTaskOfAll();
    user114s={x.user114 for x in tasks};
    for user114 in user114s:
        hashcode=user114.id%10;
        #当前的user114的id%10要>=当前robot的边界 and <下一个robot的边界
        if hashcode>=upbound and hashcode<downbound:
            RobotMaster(user114).execute();
    
    
def work():
    while(True):
        doWorkOfTimer();
    
    
class RobotMaster:
    def __init__(self,user114):
        self.user114=user114;
    def execute(self):
        print self.user114.id;
        
if __name__ == '__main__':
    #work();
    doWorkAtRegularTime();
    
    
    
    
    