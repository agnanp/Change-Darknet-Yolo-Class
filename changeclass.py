import os
import glob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--input_img", type=str, default="./imgdir",
                help="paht to input folder")
ap.add_argument("-o","--old_class", type=str, default="0",
                help="old class")
ap.add_argument("-n","--new_class", type=str, default="0",
                help="new class")
args = vars(ap.parse_args())
                               
data_path = os.path.join(args["input_img"],'*txt')
files = sorted(glob.glob(data_path))

for f1 in files:
    res = []
    with open(f1, "r") as infile:
        for line in infile:                        # Iterate each line 
            val = line.split()        
            if val[0] == str(args["old_class"]):
                val[0] = str(args["new_class"])             
            res.append(val)  

    with open(f1, "w") as outfile:          #Open file to write
        for line in res:
            outfile.write(str(line[0])+" "+str(line[1])+" " +str(line[2])+" " +str(line[3])+" " +str(line[4])+"\n")              #Write Data