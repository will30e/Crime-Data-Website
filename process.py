# part 1
def gen_dictionary(data,y):
  acc = {}
  for i in data:
    
    if y in i:
      v = i[y]
      
      acc[v] = 0


  return acc



                                                                

# part 2
def total_matches(lod,k,v):
  acc = 0
  for i in lod: 
    val = i[k]
    if (val == v):
      acc += 1

  return acc


# part 3
def total_matches_specific(lod,k,v,k2,v2):
  acc = 0
  for i in lod:
    val = i[k]
    if (i[k2] == v2 and val == v):
      acc += 1
  return acc


#Part 4
def remove_min(data,min_val):
  new_Dict = {}
  for i in data:
    val = data[i]
    if val > min_val:
      new_Dict[i] = val

  return new_Dict

