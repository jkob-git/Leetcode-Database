import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates= person.duplicated(subset='email')  #finds duplicates
    emails=person[duplicates]["email"]      #filters duplicate in dataframe
    emails= emails.drop_duplicates()        #drops email with multiple duplicates
    print(emails)                           #check
    output=pd.DataFrame({"Email":emails})       

    return output