# -*- coding: utf8 -*-
##copy Math file to My mobile phone sd card,or reverse
import os
import os.path
import shutil
def mycopytree(src, dst):
    """用法mycopytree(source,destiny)
    将src目录下的所有文件同步到dst目录下
    """
    ##
    names = os.listdir(src)
    #确定dst目录是否存在,不存在则创建
    if not os.path.isdir(dst):
        os.makedirs(dst)
        
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname):
                mycopytree(srcname, dstname)
            else:
                if(not os.path.exists(dstname)):
                    shutil.copy2(srcname, dstname)
                else:
                    #判断文件是否更新
                    if(os.stat(srcname)[8] > os.stat(dstname)[8]):
                        #移除文件，然后拷贝
                        print("{0} is newer,overwritting".format(srcname))
                        os.remove(dstname)
                        shutil.copy2(srcname, dstname)
                    else:
                        print("{0} is not newer,omited".format(srcname))
        except:
            print('Error File:',srcname)

def truncate(dst,src):
    """删除dst有,而src下没有的dst下的文件
    """
    #recurring    
    if os.path.isdir(dst):
        names = os.listdir(dst)
        for name in names:
            dst2 = os.path.join(dst, name)
            src2 = os.path.join(src, name)
            truncate(dst2,src2)        
    #print("compair {} with {}".format(dst,src))
    if not os.path.exists(src):#src maps to dst if they are file
        deldir(dst)    
        print("deleting {0} as {1} vanished.".format(dst,src))
    
def deldir(path):
    """truncate dst dir to syn"""
    if not os.path.isdir(path):
        os.remove(path)
    else:
        names = os.listdir(path)
        for name in names:
            path2 = os.path.join(path, name)
            deldir(path2)
        os.rmdir(path)

def sysndir(src,dst,type):
    mycopytree(src,dst)   
    if type==1:
        truncate(dst,src)
    
     
if __name__ == '__main__':
    import os
    source = os.getcwd()
    #dst = input("Input the Mobile drive letter:")
    dst = 'I:\\library\\Excel'
    
    sysndir(source,dst,1)
    print("##Backup Complete.")

