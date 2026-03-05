import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #use dt table as map. to update values in empl table
    #first approach used creating dictionary and mapping.
    #more practical to use merge
    employee = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    #select top salary values per department
    top= employee.groupby('name_y')['salary'].max().reset_index()
    #filter in original df
    ranks= employee.merge(top,how="right")[["name_y","name_x","salary"]]
    #rename columns
    ranks.columns=["Department","Employee","Salary"]
    print(ranks)
    return ranks

    #note, merge is a versatile function for filtering and joining. 

    