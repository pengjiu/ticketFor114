#coding:utf-8  
import requests
import cookielib
import mechanize
import urllib

class Robot_114:
    login_url="http://www.bjguahao.gov.cn/quicklogin.htm";
    confirm_url="http://www.bjguahao.gov.cn/order/confirm.htm";
    def __init__(self,task):
        cookiejar = cookielib.LWPCookieJar()
        self.session=requests.Session();
        self.session.cookies=cookiejar;
        self.session.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'};
        self.task=task;
        '''
            登录平台
        '''
    def login(self):
        username=self.task.user114.username;
        pwd=self.task.user114.pwd;
        login_data={'mobileNo':username,'password':pwd,'yzm':'','isAjax':'true'};
        r=self.session.post(Robot_114.login_url,data=login_data);
        if r.json()['msg']!="ok":
            raise Exception("登录失败！");
    '''
        医院下的科室的某一天预约信息。
    '''
    def partduty(self):
        dutyCode=self.task.getDutycode();
        dutyDate=self.task.getDutydate();
        r=self.doPartduty( dutyCode, dutyDate);
        if r.json()['msg']!="ok":
            raise Exception("登录失败！");
        return r;
    def doPartduty(self,dutyCode,dutyDate):
        login_data={'hospitalId':self.task.hospitalId,'departmentId':self.task.epartmentId,'dutyCode':dutyCode,'dutyDate':dutyDate,'isAjax':'true'};
        r=self.session.post(Robot_114.login_url,data=login_data);
        return r.json();
    '''
        提交预订
    '''
    def confirm(self,dutySourceId,doctorId,smsVerifyCode):
        confirm_data={'dutySourceId':dutySourceId,'hospitalId':self.task.hospitalId,'departmentId':self.task.departmentId,'doctorId':doctorId,
                    'patientId':self.task.user114.patientid,'hospitalCardId':'','medicareCardId':'','reimbursementType':'1',
                    'smsVerifyCode':smsVerifyCode,'childrenBirthday':'','isAjax':'true'};
        r=self.session.post(Robot_114.confirm_url,data=confirm_data);
        return r;
    def cancel(self,dutySourceId,doctorId,smsVerifyCode):
        login_data={'dutySourceId':dutySourceId,'hospitalId':self.task.hospitalId,'departmentId':self.task.departmentId,'doctorId':doctorId,
                    'patientId':self.task.user114.patientid,'hospitalCardId':'','medicareCardId':'','reimbursementType':'1',
                    'smsVerifyCode':smsVerifyCode,'childrenBirthday':'','isAjax':'true'};
        r=self.session.post(Robot_114.login_url,data=login_data);
        return r;
    def execute(self):    
        
        pass;
if __name__ == '__main__':
    r=Robot_114();
    r.login();
        
        