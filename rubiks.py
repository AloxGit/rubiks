import functools
from collections import deque

  
def compare(newList):
  if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, newList, endList), True):  
    return 1
  else: 
    return 0 
  
def compareInverse(newList):
  if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, newList, startList), True):  
    return 1
  else: 
    return 0  

  
def toStr(list):
  sConfig = ''.join(str(e) for e in list)  
  return sConfig
  
def F(config):
  newConfig = config.copy()
  newConfig[0] = config[6]
  newConfig[1] = config[7]
  newConfig[2] = config[8]
  newConfig[3] = config[0]
  newConfig[4] = config[1]
  newConfig[5] = config[2]
  newConfig[6] = config[9]
  newConfig[7] = config[10]
  newConfig[8] = config[11]
  newConfig[9] = config[3]
  newConfig[10] = config[4]
  newConfig[11] = config[5]
  
  return newConfig

def Fi(config):
  newConfig = config.copy()
  newConfig[6] = config[0]
  newConfig[7] = config[1]
  newConfig[8] = config[2]
  newConfig[0] = config[3]
  newConfig[1] = config[4]
  newConfig[2] = config[5]
  newConfig[9] = config[6]
  newConfig[10] = config[7]
  newConfig[11] = config[8]
  newConfig[3] = config[9]
  newConfig[4] = config[10]
  newConfig[5] = config[11]
  
  return newConfig

def U(config):
  newConfig=config.copy()
  newConfig[0]=config[5]
  newConfig[1]=config[3]
  newConfig[2]=config[4]
  newConfig[3]=config[16]
  newConfig[4]=config[17]
  newConfig[5]=config[15]
  newConfig[12]=config[1]
  newConfig[13]=config[2]
  newConfig[14]=config[0]
  newConfig[15]=config[14]
  newConfig[16]=config[12]
  newConfig[17]=config[13]
  
  return newConfig

def Ui(config):
  newConfig=config.copy()
  newConfig[5]=config[0]
  newConfig[3]=config[1]
  newConfig[4]=config[2]
  newConfig[16]=config[3]
  newConfig[17]=config[4]
  newConfig[15]=config[5]
  newConfig[1]=config[12]
  newConfig[2]=config[13]
  newConfig[0]=config[14]
  newConfig[14]=config[15]
  newConfig[12]=config[16]
  newConfig[13]=config[17]
  
  return newConfig


def L(config):
  newConfig=config.copy()
  newConfig[0]=config[13]
  newConfig[1]=config[14]
  newConfig[2]=config[12]
  newConfig[6]=config[2]
  newConfig[7]=config[0]
  newConfig[8]=config[1]
  newConfig[12]=config[20]
  newConfig[13]=config[18]
  newConfig[14]=config[19]
  newConfig[18]=config[7]
  newConfig[19]=config[8]
  newConfig[20]=config[6]
  
  return newConfig
def Li(config):
  newConfig=config.copy()
  newConfig[13]=config[0]
  newConfig[14]=config[1]
  newConfig[12]=config[2]
  newConfig[2]=config[6]
  newConfig[0]=config[7]
  newConfig[1]=config[8]
  newConfig[20]=config[12]
  newConfig[18]=config[13]
  newConfig[19]=config[14]
  newConfig[7]=config[18]
  newConfig[8]=config[19]
  newConfig[6]=config[20]
  
  return newConfig


def solver(start, end):
  bfs = deque()
  pair = ("", start)
  bfs.append(pair)
  
  v1={toStr(start): pair[0]}
  
  bfs2 = deque()
  pair = ("", end)
  bfs2.append(pair)
  
  v2={toStr(end): pair[0]}
  
  while 1:
    pair = bfs.popleft()
    config = pair[1]
    moves = pair[0]
    
    
    fConfig = F(config)
    pair = (moves + "F ", fConfig)
    if compare(fConfig):
        return pair[0]  
      
    sConfig = toStr(fConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
       
    fiConfig = Fi(config)
    pair = (moves + "Fi ", fiConfig)
    if compare(fiConfig):
        return pair[0]
    sConfig = toStr(fiConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
    
    lConfig = L(config)
    pair = (moves + "L ", lConfig)
    if compare(lConfig):
        return pair[0]
    sConfig = toStr(lConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
    
    liConfig = Li(config)
    pair = (moves + "Li ", liConfig)
    if compare(liConfig):
        return pair[0]
    sConfig = toStr(liConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
    
    
  
    uConfig = U(config)
    pair = (moves + "U ", uConfig)
    if compare(uConfig):
        return pair[0]
    sConfig = toStr(uConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
    
    uiConfig = Ui(config)
    pair = (moves + "Ui ", uiConfig)
    if compare(uiConfig):
        return pair[0]
    sConfig = toStr(uiConfig)
    v1[sConfig]=pair[0]
    if sConfig in v2:
        return v1[sConfig]+v2[sConfig]
    bfs.append(pair)
    
      
    
    
    
    
    pair = bfs2.popleft()
    config = pair[1]
    moves = pair[0]
    
    
    fConfig = F(config)
    pair = ("Fi " + moves, fConfig)
    if compareInverse(fConfig):
        return pair[0]  
    sConfig = toStr(fConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
       
    fiConfig = Fi(config)
    pair = ("F " + moves, fiConfig)
    if compareInverse(fiConfig):
        return pair[0]  
    sConfig = toStr(fiConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
    
    lConfig = L(config)
    pair = ("Li " + moves, lConfig)
    if compareInverse(lConfig):
        return pair[0]  
    sConfig = toStr(lConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
    
    liConfig = Li(config)
    pair = ("L " + moves, liConfig)
    if compareInverse(liConfig):
        return pair[0]  
    sConfig = toStr(liConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
  
    uConfig = U(config)
    pair = ("Ui " + moves, uConfig)
    if compareInverse(uConfig):
        return pair[0]  
    sConfig = toStr(uConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
    
    uiConfig = Ui(config)
    pair = ("U " + moves, uiConfig)
    if compareInverse(uiConfig):
        return pair[0]  
    sConfig = toStr(uiConfig)
    v2[sConfig]=pair[0]
    if sConfig in v1:
        return v1[sConfig]+v2[sConfig]
    bfs2.append(pair)
    
      
    

    
startList = []
endList = []

for i in range(0, 24):
  ele = int(input())
  startList.append(ele)
  

for i in range(0, 24):
  ele = int(input())
  endList.append(ele)

# startList = [6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23]
# endList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
  
# a=Fi(Ui(L(U(F(Ui(F(F(Ui(Li(U(Fi(L(F(startList)))))))))))))) 
# for i in range(0, 24):
#     print (a[i])
# Fi U Li Ui F F Ui F U L Ui Fi 
  
print(solver(startList, endList))


  