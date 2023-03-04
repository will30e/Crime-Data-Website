import json
import csv
import urllib.request


def list_dic_gen(param1,param2):
  newDic = {}
  newArr = []  
  for j in param2:
    for i in range(len(param1)):
      newDic[param1[i]] = j[i]
    var = newDic.copy()
    newArr.append(var)
    newDic.clear()

  return newArr
  
      
      
      
# print(list_dic_gen([], [[]]))
# print(list_dic_gen(['One','Two'], [['First','Second']]))
# print(list_dic_gen(['Second'], [['One'],['Third Fourth']]))


def read_values(filename):
  list = []
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      list.append(row)
      
    return list
      
def list_gen(param1,param2):
  list = []
  list2 = []
  list3 = []
  for dic in param1:
    for key in param2:
      if key in dic:
        list.append(dic[key])
        list2 = list.copy()
    list3.append(list2)
    list.clear()
    
  return list3

# print(list_gen([{'Used Key': 'Data', 'Unused Keys' : 'More Data'}],['Used Key']))
# print(list_gen([{'Hint': 'Length 2 Not Required', 'Num' : 8675309},
# {'Num': 1, 'Hint' : 'Use 1st param order'}],['Hint', 'Num']))


def write_values(listlist,file):
  with open (file, 'a') as f:
    writer = csv.writer(f)
    for list in listlist:
      writer.writerow(list)
      

      
def split_date(dstring):
  acc = []
  year = dstring[0] + dstring[1] + dstring[2] + dstring[3]
  month = dstring[5] + dstring[6]
  acc.append(int(year))
  acc.append(int(month))
  
  return acc
  
# print(split_date('2022-06-20T08:10:06.000'))


def fix_data(lod,key):
  for dic in lod:
    nish = split_date(dic[key])
    dic["year"] = nish[0]
    dic["month"] = nish[1]
  return lod


def json_loader(str):
  response = urllib.request.urlopen(str)
  contents = response.read().decode()
  obj = json.loads(contents)
  return obj


def make_values_numeric(los,dic):
  for string in los:
    for d in dic:
      if string == d:
        dic[string]=int(dic[string])

  return dic
        
      
    


# print(make_values_numeric(['number'],
# {'name' : 'ValJean', 'number' : '24601'}))


def save_data(lod,lok,filename):
  with open(filename,"w") as f:
    writer = csv.writer(f)
    writer.writerow(lok)
    for dic in lod:
      list = []
      for key in lok:
        list.append(dic[key])
      writer.writerow(list)
        

# dl = [{'date': '07-31-2021', 'location': 'NY', 'fake' : 'data'},
# {'location': 'NJ', 'date': '08-01-2021'}]


# print(save_data(dl,['date', 'location'], 'bore.csv'))

def load_data(filename):
  lst_2 = []
  with open (filename,"r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for i in reader:
      dic = {}
      for j in range(len(header)):
        dic[header[j]] = i[j]
      lst_2.append(dic)
  return lst_2

# print(load_data("sample.csv"))
  
  
  