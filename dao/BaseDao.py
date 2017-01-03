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
engine = create_engine('mysql+pymysql://root:pengjiu009@112.74.98.248:3306/114?charset=utf8mb4')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def saveTask(new_app):
    session = DBSession()    
    session.add(new_app)
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
        以setting 表作为分布式锁
    '''
def querySettingWithLocking():
    session = DBSession()
    settings=session.query(Bean.Settings).with_lockmode("update").one();
    #session.commit();
    res={"settings":settings,"session":session};
    #session.close()
    return res;
'''
    以setting表 释放锁
'''
def releaseSettingWithLocking(session):
    session.commit();
    #session.close() 

def queryTaskOfAll():
    session = DBSession()
    d=session.query(Bean.Task).filter_by(status=1).all();
    session.commit();
    #session.close()
    return d

    
if __name__ == '__main__':
    data=querySettingWithLocking()
    settings=data["settings"];
    session=data["session"];
    releaseSettingWithLocking(session);
    time.sleep(10);
    print settings.id;



