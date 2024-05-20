import os
from shutil import copyfile
data_path = './Market'
data_path2= './Market-1501-v15.09.15'

if not os.path.isdir(data_path):  
    if os.path.isdir(data_path2):
        os.system('mv %s %s'%(data_path2, data_path))
    else:
        print('change data path')

save_path = data_path+'/pytorch'
if not os.path.isdir(save_path):
    os.mkdir(save_path)
query_path = data_path2+'/query'
query_save_path = data_path+'/pytorch/query'

if not os.path.isdir(query_save_path):
    os.mkdir(query_save_path)

for root, dirs, files in os.walk(query_path, topdown= True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID = name.split('_')
        src_path = query_path+'/'+name
        dst_path = query_save_path+'/'+ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path,dst_path+'/'+name)
#MultipleQuery
        
query_path = data_path2+'/gt_bbox'
if os.path.isdir(query_path):
    query_save_path = data_path+ '/pytorch/multi-query'
    if not os.path.isdir(query_save_path):
        os.mkdir(query_save_path) 
    for root, dirs,files in os.walk(query_path,topdown=True):
        for name in files:
            if not (name[-3:]=='jpg'):
                continue
            ID = name.split('_')
            src_path = query_path+'/'+name
            dst_path = query_save_path+'/'+ID[0]
            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)
            copyfile(src_path,dst_path+'/'+name)

#train all
train_path = data_path2+'/bounding_box_train'
train_save_path = data_path+'/pytorch/train-all'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)
for root, dirs, files in os.walk(train_path):
    for name in files:
        if not name[-3:] == 'jpg':
            continue
        ID  = name.split('_')
        src_path = train_path+'/'+name
        dst_path = train_save_path+'/'+ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path,dst_path+'/'+name)

train_path = data_path2 + '/bounding_box_train'
train_save_path = data_path + '/pytorch/train'
val_save_path = data_path + '/pytorch/val'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)
    os.mkdir(val_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
            dst_path = val_save_path + '/' + ID[0]  #first image is used as val image
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)




  
        



