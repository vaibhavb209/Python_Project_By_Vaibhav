def isNameValid(banknm):
    if(not banknm.isalpha()):
        return False
    return True

def isifscValid(ifsc):
    s1=ifsc[0:4]
    s2=ifsc[5:6]
    s3=ifsc[6:12]
    if len(ifsc)==11:
        if not s1.isalpha():
            return False
        if not s2.isdigit():
            return False
        if not s3.isalnum():
            return False
        return True
    
def isaccValid(accno):
    if(len(accno)==12):
        if not accno.isdigit():
            return False
        return True

def isAgeValid(age):
    if(len(age)==2 or len(age)==1):
        if(age.isdigit()):
            a=int(age)
            if a>1 and a<100:
                return True
    return False

def isGenderValid(gender):
    if gender.lower() in["male","female","transgender"]:
        return True
    return False

def isdobValid(dob):
    if len(dob)==10:
        dd=int(dob[0:2])
        mm=int(dob[3:5])
        yy=int(dob[6:10])
        if not dd>0 and dd<=31:
            return False
        if not mm>0 and mm<13:
            return False
        if not yy>1900 and yy<2023:
            return False
    return True

def isaddValid(address):
    if len(address)<50:
        return True
    return False

def iscityValid(city):
    if city.isalpha():
        return True
    return False

def istypeValid(type_acc):
    if type_acc in["Savings","Current","Joint"]:
        return True
    return False

def isbalValid(bal):
    if bal.isdigit():
        b=int(bal)
        if b>0:
            return True
        else:
            return False
        
def ispanValid(pancard):
    if len(pancard)==10:
        s1=pancard[0:5]
        s2=pancard[5:9]
        s3=pancard[9:10]
        if s1.isalpha() and s1.isupper() and s2.isdigit() and s3.isalpha() and s3.upper():
            return True
    return False

def isadharValid(adharcard):
    if len(adharcard)==12:
        if adharcard.isdigit():
            return True
    return False
