def hello(*args,**kwargs):
    print(args)
    print(kwargs)

#hello("Krish","Naik",age=32,dob=1989)

lst=list(('YASH', 'AGARWAL'))
dict_val={'age': 22, 'dob': 12234}

#hello(*lst,**dict_val)

hello("YASH","AGARWAL","1","2","1123",age=10,dob=1999)