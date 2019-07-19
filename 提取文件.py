#以一个文件中的字段从一个目录中提取文件
##help
import pandas as pd 
import os
import argparse 
parser = argparse.ArgumentParser(prog="python3 text1.py")
parser.add_argument("i",help="input_file")
parser.add_argument("i2",help="input_path")
parser.add_argument("o",help="output_path")
args = parser.parse_args()
##输入文件、输出路径、输入路径
input_file = args.i 
output_path = args.o
input_path = args.i2
##创建一个输出路径
if not os.path.exists(output_path):
    os.makedirs(output_path)
##读取文件第一列的字段
df = pd.read_csv(input_file, header=None, sep="\t")
object_list = df[0]
##错误返回
for i in object_list:
    try:
        os.system("cp {0}/{1}.fa {2}/".format(input_path,i,output_path))
    except:
        os.system("{0} >> {1}/faile".format(i,"/".join(input_path.split("/")[0:-1])))


       