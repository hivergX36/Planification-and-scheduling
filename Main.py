from class_schedule import * 
import re 

Problem = schedule_Lmax()

datProb = Problem.parse_data("data.text")

datProb = [datProb[i] for i in range(len(datProb)) if datProb[i] != "\n"]
datProb = [ re.sub("\n", "", datProb[i]) for i in range(len(datProb))]
print(datProb)