#coding:utf-8  
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()
'''
    扫描的任务表
'''
class Task(Base):
    # 表的名字:
    __tablename__ = 'task'

    # 表的结构:
    id = Column(Integer(), primary_key=True);
    hospitalId = Column(String(100));  #医院id
    departmentId = Column(String(2000)); #科室id
    dutydata = Column(String(2000)); #预约时间 {’2016-1-1’:1,'2017-1-1':2} json 预约日期：1上午 2下午
    doctortype=Column(Integer());#预约的医生 1.专家 2.非专家 3 全部
    adddate=Column(TIMESTAMP, default=func.now());
    user114id = Column(Integer, ForeignKey('user114.id'));#绑定的114帐户id
    userid = Column(Integer);#用户id
    user114 = relationship("User114",lazy='subquery');
    hashcode = Column(Integer());
    status=Column(Integer());
    '''
        订单成功后的信息如下
    '''
    orderid=Column(String(50));
    orderdate=Column(String(50));
    orderdocotor=Column(String(50));
    identityCode=Column(String(50));#识别码
    
    __dutydate=None;#抢到票的时间
    __dutyCode=None;#抢到票的
    def setDutydate(self,dutydate):
        self.__dutydate=dutydate;
    def getDutydate(self):
        return self.__dutydate;
    def setDutycode(self,dutycode):
        self.__dutyCode=dutycode;
    def getDutycode(self):
        return self.__dutycode;
'''
    114任务的用户
'''
class User114(Base):
    # 表的名字:
    __tablename__ = 'user114';
    # 表的结构:
    id=Column(Integer(), primary_key=True);
    username = Column(String(20));#帐号
    pwd = Column(String(100));  #密码
    patientid = Column(String(100)); #就诊人 
    phone=Column(String(100));  #手机号
    adddate=Column(TIMESTAMP, default=func.now());
    userid=Column(Integer());#用户ID
    task = relationship("Task", back_populates="user114", uselist=True);
'''
    设置
'''
class Settings(Base):
    # 表的名字:
    __tablename__ = 'settings';
    # 表的结构:
    id=Column(Integer(), primary_key=True);
    #执行任务的间隔时间 秒为单位
    interval_Of_Task = Column(Integer());
    #执行漏票的 间隔单位
    interval_Of_Realtime = Column(Integer());
    #抢票的时间段3600,7200
    take_ticket_time=Column(String(100));
class Robot(Base):
    # 表的名字:
    __tablename__ = 'robot';
    # 表的结构:
    id=Column(String(100), primary_key=True);
    # 定时刷新
    update_time = Column(TIMESTAMP, default=func.now());
    #
    hashcode = Column(Integer()); 
    
    
    
    
    