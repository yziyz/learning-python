import os
import subprocess

if __name__ == "__main__":
    svnAddTemplate = r'svn add %s'
    svnCommitTemplate = r'svn ci -m "添加%s"'

    fileList = os.listdir("/home/user/web前端/picasso-webapp")
    for file in fileList:
        subprocess.Popen(svnAddTemplate % file, shell=True).wait()
        subprocess.Popen(svnCommitTemplate % file, shell=True).wait()
