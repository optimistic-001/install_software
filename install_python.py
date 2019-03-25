# -*- coding:UTF-8 -*-
import os
import sys

def install_python(python_number,wget_url):
    '''
    安装python
    '''
    if python_number == 1:
        py_file = 'python2.7'
        pip_file = 'pip2.7'
        python_name = 'Python-2.7.12'
    elif python_number == 2:
        py_file = 'python3'
        pip_file = 'pip3'
        python_name = 'Python-3.6.1'

    print ("\033[1;31;40m  安装依赖环境  \033[0m")
    cmd_yum = "yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel"
    res_yum = os.system(cmd_yum)
    if_exec(res_yum,"安装依赖环境失败，请检测yum状态！！！")

    print ("\033[1;31;40m  安装" + py_file + "  \033[0m")
    cmd_wget = 'wget ' + wget_url
    res_wget = os.system(cmd_wget)
    if_exec(res_wget,"下载python源码安装包失败，请检测网络是否正确！！！")

    cmd_mkdir = 'mkdir -p /usr/local/' + py_file
    res_mkdir = os.system(cmd_mkdir)
    if_exec(res_mkdir,"创建文件失败！！！")

    print ("\033[1;31;40m  解压python源码 \033[0m")
    cmd_tar = 'tar -zxf ' + python_name + '.tgz'
    res_tar = os.system(cmd_tar)
    if res_tar != 0:
        os.system("rm -f " + python_name + '.tgz')
        if_exec(res_tar,"解压失败，请重新执行脚本！！！")

    print ("\033[1;31;40m  编译python源码 \033[0m")
    cmd_conf = "cd " + python_name + " && ./configure --prefix=/usr/local/" + py_file + " && make && make install"
    res_conf = os.system(cmd_conf)
    if_exec(res_conf,"编译python源码失败！！！")

    cmd_ln = "ln -s /usr/local/" + py_file + "/bin/" + py_file + " /usr/bin/" + py_file
    res_ln = os.system(cmd_ln)
    if_exec(res_ln,"建立软连接失败！！！")

    cmd_ln_pip = "ln -s /usr/local/" + py_file + "/bin/" + pip_file + " /usr/bin/" + pip_file
    res_ln_pip = os.system(cmd_ln_pip)
    if_exec(res_ln_pip,"建立软连接失败！！！")

    os.system(py_file + " -V")


def if_exec(res,explain):
    if res != 0:
        print (explain)
        sys.exit(1)


def main():
    if os.getuid() == 0:
        python_number = input ('python版本：\n\t1.python2.7\n\t2.python3.6\n请输入python版本编号：')
        if python_number == 1:
            wget_url = 'https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
            install_python(python_number,wget_url)
        elif python_number == 2:
            wget_url = 'https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz'
            install_python(python_number,wget_url)
        else:
            print ("请输入正确的python版本编号！！！")
            sys.exit(1)
    else:
        print ('当前用户不是root用户，请以root用户执行脚本！！！')
        sys.exit(1)



if __name__ == '__main__':
    main()


