import re
import csv
from collections import Counter
def reader(filename):
    with open(filename) as f:
        log=f.read()
        regexp1=[r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',r'\d{1,2}\/\D{1,3}\/\d{1,4}',r'\d[10]\:\d{1,2}\:\d{1,2}\s[+]0000',r'GET.*HTTP/1.1',r'\b200',r'\s\d{4,6}\s',r'http.*20..','Mozilla..*\d{1,3}\.\d{1,2}']
        all=[re.findall(regexp1[i],log) for i in range(len(regexp1))]
        dict = {'IP ADDRESS':all[0] , 'DATE':all[1],'TIME':all[2],'REQUEST STATUS':all[3],'FILE SIZE':all[4],'REQUEST':all[5],'REQUEST URL':all[6],'WEB BROWSER URL':all[7]}
    f.close()
    with open("parsed file.csv", 'w', encoding='utf-8', newline='') as f:
            for key, value in dict.items():
                writer = csv.writer(f)
                writer.writerow(dict.keys())
                writer.writerows(zip(*dict.values()))
                break   
    f.close()

if __name__=='__main__':
    reader(filename='log.txt')
