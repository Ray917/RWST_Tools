import sys
import os
import zipfile

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
        fz.close()      
    else:print('文件损坏。')

def kernel(t):
    if(t=='exit'):sys.exit()
    elif(t=='cls'):os.system('cls')
    elif(t=='' or t=='\n' or t=='\r'):pass
    elif(t=='extension'):
        print('extension')
        print('extension::list')
        print('extension::install [插件文件]')
        print('extension::uninstall [插件名字]')
        print('extension [插件名字]')
    elif(t=='pack'):
        print('pack [可执行文件]')
    elif(t=='?'):
        print('exit')
        print('cls\n')
        kernel('extension')
        print('')
        kernel('pack')
    elif(t=='extension::list'):
        pd=0
        for i in open(path+'\\module\\dir.txt','r'):
            pd+=1
            n=i
            if(n[len(n)-1]=='\n'):n=n[0:len(n)-1]
            os.system(path+'\\extensions\\'+n+' name')
            print(' - ',end='')
            sys.stdout.flush()
            os.system(path+'\\extensions\\'+n+' version')
            print('')
        if(pd==0):print('RWST没有任何插件啊！')
        else:print('共有 '+str(pd)+' 个插件。')
    elif(t[0:10]=='extension '):
        t+='.exe'
        exn=t[10:len(t)]
        pd=0
        for i in open(path+'\\module\\dir.txt','r'):
            pd+=1
            n=i
            if(n[len(n)-1]=='\n'):n=n[0:len(n)-1]
            if(n==exn):
                print('可执行文件：'+path+'\\'+exn)
                print('名字：',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' name')
                print('\nRWST代码：',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' code')
                print('\n版本：',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' version')
                print('\n作者：',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' author')
                print('\n简介：',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' intr')
                print('')
                break
        if(pd==0):print('RWST没有任何插件啊！')
    elif(t[0:21]=='extension::uninstall '):
        kernel('extension '+t[21:len(t)])
        che=str(input('您确定要卸载嘛？ [Y/n] '))
        if(che=='Y' or che=='y'):
            t+='.exe'
            exn=t[21:len(t)]
            pd=0
            for i in open(path+'\\module\\dir.txt','r'):
                pd+=1
                n=i
                if(n[len(n)-1]=='\n'):n=n[0:len(n)-1]
                if(n==exn):
                    os.system('del '+path+'\\extensions\\'+exn)
                    pd=-1
                    break
            if(pd==0):print('RWST没有任何插件啊！')
            elif(pd!=-1):print('RWST没有这个插件啊！')
            elif(pd==-1):
                pd=0
                w=''
                for i in open(path+'\\module\\dir.txt','r'):
                    pd+=1
                    n=i
                    if(n[len(n)-1]=='\n'):n=n[0:len(n)-1]
                    if(n!=exn):w+=n+'\n'
                f=open(path+'\\module\\dir.txt','w')
                f.write(w)
                f.close()
                print('插件卸载成功！')
        else:
            print('太好啦，主人并没有抛弃我嘛……（卸载操作已被用户取消。）')
    elif(t[0:19]=='extension::install '):
        che=str(input('您确定要安装嘛？ [Y/n] '))
        if(che=='Y' or che=='y'):
            pa=t[19:len(t)]
            if(pa[0]==chr(34) and pa[len(pa)-1]==chr(34)):
                pa=pa[1:len(pa)-1]
            os.system('copy '+chr(34)+pa+chr(34)+' .')
            os.system('ren *.rwx temp.zip')
            unzip_file('.\\temp.zip','.')
            os.system('del temp.zip')
            pd=0
            for i in open('.\\info.txt','r'):
                pd+=1
                if(pd==1):print('版本：',end='')
                elif(pd==2):
                    print('RWST代码：',end='')
                    exn=i[0:len(i)-1]
                elif(pd==3):
                    print('作者：',end='')
                    if(i!='RayGroup Official\n'):n='1'
                    else:n='0'
                elif(pd==4):print('名字：',end='')
                elif(pd==5):print('简介：',end='')
                print(i,end='')
            if(n=='1'):print('这个插件来自第三方哒，不是睿集团官方的插件。因此我们并不能保证此插件的安全性哦！')
            che=str(input('\n您真的要安装嘛？ [Y/n]'))
            if(che=='Y' or che=='y'):pass
            else:
                os.system('del info.txt & del main.exe')
                print('安装操作已被用户取消。')
                return
            os.system('ren main.exe '+exn+'.exe')
            os.system('del info.txt')
            os.system('move '+exn+'.exe '+path+'\\extensions')
            f=open(path+'\\module\\dir.txt','a+')
            if(f.readline()!=''):f.write('\n')
            f.write(exn+'.exe')
            f.close()
            print('嗯！成功安装上了呢！')
        else:
            print('安装操作已被用户取消。')
    elif(t[0:5]=='pack '):
        os.system('copy '+t[5:len(t)]+' .')
        f=open('.\\info.txt','w')
        for i in range(0,5):
            n=str(input())
            f.write(n)
            if(i!=4):f.write('\n')
            if(i==1):os.system('ren '+n+'.exe main.exe')
        f=zipfile.ZipFile('out.zip','w')
        f.write('.\\main.exe',compress_type=zipfile.ZIP_DEFLATED)
        f.write('.\\info.txt',compress_type=zipfile.ZIP_DEFLATED)
        f.close()
        os.system('del main.exe & del info.txt & ren out.zip out.rwx')
        os.system('move out.rwx %USERPROFILE%\\Desktop')
    else:
        print('错误：没有找到相应的代码或命令。')
        print('请检查你的输入然后重新尝试。')

if(__name__=='__main__'):
    os.system('title RWST Tools 中文版')
    os.system('chcp 936')
    os.system('cls')

    print('RWST Tools 中文版 V1 64位。')
    print('版权所有 睿集团 2020。保留所有权利。')

    path='C:\\RayGroup\\RWST_CN'

    while(True):
        if(os.path.exists(path+'\\RWST.exe')==False):
            print('\n错误：找不到RWST。')
            path=str(input('手动输入RWST安装路径 >> '))
            if(path=='exit'):sys.exit()
            elif(path=='cls'):os.system('cls')
        else:
            print('\nRWST路径已成功找到。')
            break

    print('\n输入 ? 来阅读 命 令 大 全 哦！')

    while True:
        tt=str(input('\nRwstTools>> '))
        kernel(tt)
