import os
source_path='/Volumes/RKSS/Mac_BackUp/'
#destination_path='/Users/ritvikkhare/Downloads/duplicate_files/'
destination_path='/Volumes/RKSS/DeleteWala/'
# /Volumes/RKSS/Mac_BackUp
arr = os.listdir(source_path)
print ("Total Files in Folder = ", len(arr))
print (arr)
cntImages = 0
cntDuplicateImages = 0
cntAbnormalName =0 
cntVideos = 0
listVideos=[]
listImages=[]
for x in arr:
 if(".m4v" in x and "._" not in x):
  cntVideos+=1
  listVideos.append(x)      
 if (".png" in x and "._" not in x):
  cntImages+=1
  listImages.append(x)
  #print(x)
  if("(1)" in x):
   cntDuplicateImages += 1
   if("._" in x):
    yFileName = x.replace("._","")
    cntAbnormalName+=1
    os.replace(source_path+yFileName, destination_path+yFileName)
    #print(x, " Replaced with trial = ", yFileName)
    #print("File Paths = ", source_path+yFileName, destination_path+yFileName)

print("Count Videos =", cntVideos)
print("Png File count= ",cntImages)
print("Duplicate Png=", cntDuplicateImages)
print("Abnormal Names =", cntAbnormalName)
print("Path of File = " + source_path+x)
print("List Videos = ", len(listVideos))
print("List Images = ", len(listImages))

places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listVideos.txt', 'w') as filehandle:
    for listitem in listVideos:
        filehandle.write('%s\n' % listitem)

with open('listImages.txt', 'w') as filehandle:
    for listitem in listImages:
        filehandle.write('%s\n' % listitem)