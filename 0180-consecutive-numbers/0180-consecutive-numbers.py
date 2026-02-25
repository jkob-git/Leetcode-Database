import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    cons_nums=[]
    diction = {}
    for id,num in zip(logs['id'],logs['num']):
        diction[id]=num
    print(diction)
    # id,+1,+2
    # keyword: at least 3 times
    for id in range(1,len(logs['id'])-1) :
        if (diction[id] == diction[id+1] == diction[id+2]):
            cons_nums.append(diction[id])
    #remove duplicate values
    cons_nums=list(set(cons_nums))
    output=pd.DataFrame({"ConsecutiveNums":cons_nums})
    return output