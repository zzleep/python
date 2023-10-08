# copyfile() = copies content of a file
# copy() =  copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('C:\\Users\\96654\\Desktop\\test.txt','C:\\Users\\96654\\Desktop\\copy.txt') # 2 arguments src & dst (src,dst)
# You can change shutil.copyfile to shutil.copy() or shutil.copy2() depending on what you want to copy