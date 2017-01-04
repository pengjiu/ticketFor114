#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, subqueryload
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP
from sqlalchemy.sql.functions import func
from dao import Bean
from threading import Thread
import time


Base = declarative_base() 


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://mysql:pengjiu009@112.74.98.248:3306/114?charset=utf8mb4')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def saveTask(task):
    session = DBSession()    
    session.add(task)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
def updateTaskById(taskId,modified_status):
    session = DBSession()
    session.query(Bean.Task).filter(Bean.Task.id==taskId).update({Bean.Task.status:modified_status})
    session.commit()
    session.close()
    '''
        查询 setting表
    '''
def querySetting():
    session = DBSession()
    settings=session.query(Bean.Settings).one_or_none();   
    session.close()
    return settings;

def queryRobotOfAll():
    session = DBSession()
    res=session.query(Bean.Robot).all();
    session.close()
    return res;

def queryRobotById(robotId):
    session = DBSession();
    res=session.query(Bean.Robot).filter(Bean.Robot.id==robotId).one_or_none();
    session.close();
    return res;

def updateRobotDatetimeById(robotid):
    session = DBSession()
    #Robots=session.query(Bean.Robot).filter(Bean.Robot.id==robotid).update({Bean.Robot.status:modified_status})
    res=session.execute('update robot set update_time=now() where id=:id',{'id': robotid});

    session.commit();    
    session.close()
    return res;
     

def queryTaskOfAll():
    
    session = DBSession()
    d=session.query(Bean.Task).filter_by(status=1).all();
    session.commit();
    #session.close()
    return d


if __name__ == '__main__':
    print queryRobotById(2);
     



