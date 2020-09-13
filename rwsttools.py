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
    else:print('File is broken.')

def kernel(t):
    if(t=='exit'):sys.exit()
    elif(t=='cls'):os.system('cls')
    elif(t=='' or t=='\n' or t=='\r'):pass
    elif(t=='extension'):
        print('extension')
        print('extension::list')
        print('extension::install [Extension File]')
        print('extension::uninstall [Extension Name]')
        print('extension [Extension Name]')
    elif(t=='pack'):
        print('pack [Exe File]')
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
        if(pd==0):print('RWST does not have any extension.')
        else:print(str(pd)+' extension(s).')
    elif(t[0:10]=='extension '):
        t+='.exe'
        exn=t[10:len(t)]
        pd=0
        for i in open(path+'\\module\\dir.txt','r'):
            pd+=1
            n=i
            if(n[len(n)-1]=='\n'):n=n[0:len(n)-1]
            if(n==exn):
                print('Exe file: '+path+'\\'+exn)
                print('Extension Name: ',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' name')
                print('\nCode: ',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' code')
                print('\nVersion: ',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' version')
                print('\nAuthor: ',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' author')
                print('\nIntroduction: ',end='')
                sys.stdout.flush()
                os.system(path+'\\extensions\\'+n+' intr')
                print('')
                break
        if(pd==0):print('RWST does not have any extension.')
    elif(t[0:21]=='extension::uninstall '):
        kernel('extension '+t[21:len(t)])
        che=str(input('Are you sure to uninstall? [Y/n] '))
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
            if(pd==0):print('RWST does not have any extension.')
            elif(pd!=-1):print('RWST dose not have this extension.')
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
                print('Extension uninstall successfully.')
        else:
            print('Uninstall canceled.')
    elif(t[0:19]=='extension::install '):
        che=str(input('Are you sure to install? [Y/n] '))
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
                if(pd==1):print('Version: ',end='')
                elif(pd==2):
                    print('Code: ',end='')
                    exn=i[0:len(i)-1]
                elif(pd==3):
                    print('Author: ',end='')
                    if(i!='RayGroup Official\n'):n='1'
                    else:n='0'
                elif(pd==4):print('Name: ',end='')
                elif(pd==5):print('Introduction: ',end='')
                print(i,end='')
            if(n=='1'):print('This extension is not from RayGroup Official, maybe it is unsafe.')
            che=str(input('\nDo you really want to install it? [Y/n]'))
            if(che=='Y' or che=='y'):pass
            else:
                os.system('del info.txt & del main.exe')
                print('Install canceled.')
                return
            os.system('ren main.exe '+exn+'.exe')
            os.system('del info.txt')
            os.system('move '+exn+'.exe '+path+'\\extensions')
            f=open(path+'\\module\\dir.txt','a+')
            if(f.readline()!=''):f.write('\n')
            f.write(exn+'.exe')
            f.close()
            print('Extension install successfully.')
        else:
            print('Install canceled.')
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
        print('ERROR: Command not found exception.')
        print('Please check your input and try again.')

if(__name__=='__main__'):
    os.system('title RWST Tools')
    os.system('chcp 437')
    os.system('cls')

    print('RWST Tools V1 for 64-bit.')
    print('Copyright 2020 Ray Group. All rights reserved.')

    path='C:\\RayGroup\\RWST_EN'

    while(True):
        if(os.path.exists(path+'\\RWST.exe')==False):
            print('\nERROR: Could not found RWST.')
            path=str(input('Type RWST install dir here >> '))
            if(path=='exit'):sys.exit()
            elif(path=='cls'):os.system('cls')
        else:
            print('\nRWST path found successfully.')
            break

    print('\nType ? to read the rwst-tools-code.')

    while True:
        tt=str(input('\nRwstTools>> '))
        kernel(tt)
