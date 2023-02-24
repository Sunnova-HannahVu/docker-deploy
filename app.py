import os
import subprocess
import time
import glob

EFS_VOLUME_NAME = 'fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com'
EFS_DIR_PATH = '/mnt/' + EFS_VOLUME_NAME + '/lambda/pvwatts-production-profile'

print(EFS_VOLUME_NAME)
print(EFS_DIR_PATH)

### CHANGE PERMISSIONS ON DIRECTORY
# process = subprocess.run('chmod 777 /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda', shell=True,capture_output=True,cwd='/')
# print(process)

### MAKE TGY AND TWY DIRECTORY
process = subprocess.run('mkdir /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/TGY_Borders', shell=True,capture_output=True,cwd='/')
print(process)
process = subprocess.run('mkdir /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/TWY_Borders', shell=True,capture_output=True,cwd='/')
print(process)
process = subprocess.run('mkdir /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile', shell=True,capture_output=True,cwd='/')
print(process)

### DELETE FILES FROM EFS DIRECTORY
# process = subprocess.run('rm -rfv /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile/*', shell=True,capture_output=True)
# print(process)

# # ### COPY PYTHON PACKAGES FROM LOCAL DIRECTORY TO EFS VOLUME
process = subprocess.run('scp -r ./pvwatts-production-profile /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda', shell=True,capture_output=True)
#process = subprocess.run('scp -r ./TGY_Borders /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/TGY_Borders', shell=True,capture_output=True)
# # #process = subprocess.run('rsync -v ./pvwatts-production-profile /mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda', shell=True,capture_output=True)
# print(process)

# # ### LIST DIRECTORY CONTENTS
# pvwatts_list = os.listdir(EFS_DIR_PATH)
# print('LIST DIRECTORY CONTENTS')
# print('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile')
# print(pvwatts_list)


# print('Remove .DS_Store and .gitattributes')
# os.remove('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile/.DS_Store')
# # os.remove('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile/.git_attributes')
# print('Successfully removed')

### LIST DIRECTORY CONTENTS
pvwatts_list = os.listdir(EFS_DIR_PATH)
print('LIST DIRECTORY CONTENTS')
print('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda/pvwatts-production-profile')
print(pvwatts_list)

lambda_list = os.listdir('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda')
print('LIST DIRECTORY CONTENTS')
print('/mnt/fs-0e737a84260f1cf4b.efs.us-east-1.amazonaws.com/lambda')
print(lambda_list)