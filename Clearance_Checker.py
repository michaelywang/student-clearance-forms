def checking_clearance():

    import pandas as pd
    df=pd.read_excel('Fencing Clearance List 19-20.xls')

    # Create boolean expressions for each required form

    No_Medical_Clearance = df['Internal Fields - Medically Cleared']=="NO"
    No_Winter_Update = df['Internal Fields - Winter Sports Physical Update Form']!='Yes'
    No_Payment = df['General - Payment Status']=='None'
    No_Overall_Approval = df['General - Approval']=='None'

    # Return names of Students + Email addresses for those missing forms

    student_info=df[['Participant Information - Personal - Last Name','Participant Information - Personal - First Name','Participant Information - Contact - Student\'s contact Email','First Parent Or Guardian - First Parent or Guardian - First Name', 'First Parent Or Guardian - First Parent or Guardian - Last Name', 'First Parent Or Guardian - Contact - Email']]

    Missing_Med_Clearance=student_info[No_Medical_Clearance]
    Missing_Winter_Update=student_info[No_Winter_Update]
    Missing_Payment=student_info[No_Payment]

    return Missing_Med_Clearance, Missing_Payment, Missing_Winter_Update