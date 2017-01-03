from dao import BaseDao



def doWork():
    try:
        data=BaseDao.querySettingWithLocking();
        settings=data["settings"];
        lock_session=data["session"];
        
        print settings.id;
    finally:
        if lock_session!=None:
            BaseDao.releaseSettingWithLocking(lock_session);
    
def work():
    doWork();
    
if __name__ == '__main__':
    work();