#coding:utf-8  
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()
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
    user114id = Column(Integer, ForeignKey('user114.id'));
    user114 = relationship("user114", back_populates="task");
    hashcode = Column(Integer());
    '''
        订单成功后的信息如下
    '''
    orderid=Column(String(50));
    orderdate=Column(String(50));
    orderdocotor=Column(String(50));
    identityCode=Column(String(50));#识别码
    
    __dutydate=None;
    __dutyCode=None;
    def setDutydate(self,dutydate):
        self.__dutydate=dutydate;
    def getDutydate(self):
        return self.__dutydate;
    def setDutycode(self,dutycode):
        self.__dutyCode=dutycode;
    def getDutycode(self):
        return self.__dutycode;
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
    task = relationship("task", back_populates="user114", uselist=False);
    
    
    
    
    
    
    