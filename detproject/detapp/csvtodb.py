
# from sqlalchemy import create_engine


# columns = [
#     "age",
#     "work",
#     "fwt",
#     "education",
#     "edu_no",
#     "marital_status",
#     "occupation",
#     "relationship",
#     "race",
#     "sex",
#     "cap_gain",
#     "cap_loss",
#     "hours_pw",
#     "native_country",
#     "salary"
# ]

# df = pd.read_csv("C:\Users\PC\Downloads\adult_dataset.csv",names=columns,nrows=35000)

# engine = create_engine('postgresql://postgres:Admin@2021@localhost:5432/detdb')

# df.to_sql('detemployee', engine,index=False)


import pandas as pd
from .models import detemployee
from django.conf import settings

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'postgresql://postgres:Admin@2021@localhost:5432/detdb'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)
df.to_sql(detemployee, con=engine)





age = models.IntegerField()
    work = models.TextField(blank = True)
    fwt = models.IntegerField()
    education = models.TextField(blank = True)
    edu_no = models.IntegerField()
    marital_status = models.TextField(blank = True)
    occupation = models.TextField(blank = True)
    relationship = models.TextField(blank = True)
    race = models.TextField(blank = True)
    sex = models.CharField(max_length=10)
    cap_gain = models.IntegerField()
    cap_loss = models.IntegerField()
    hours_pw = models.IntegerField()
    native_country = models.TextField(blank = True)
    salary = models.CharField(max_length=10)




import pandas as pd
from .models import detemployee
from django.conf import settings

# user = settings.DATABASES['default']['USER']
# password = settings.DATABASES['default']['PASSWORD']
# database_name = settings.DATABASES['default']['NAME']

# database_url = 'postgresql://postgres:Admin@2021@localhost:5432/detdb'.format(
#     user=user,
#     password=password,
#     database_name=database_name,
# )

# engine = create_engine(database_url, echo=False)
# df.to_sql(detemployee, con=engine)

import sqlalchemy
from sqlalchemy import create_engine

# print("prasanna")

# columns = [
#     "age",
#     "work",
#     "fwt",
#     "education",
#     "edu_no",
#     "marital_status",
#     "occupation",
#     "relationship",
#     "race",
#     "sex",
#     "cap_gain",
#     "cap_loss",
#     "hours_pw",
#     "native_country",
#     "salary"
# ]

# print("outside column")

# df = pd.read_csv(r'C:\Users\PC\Downloads\adult_dataset.csv',names=columns,nrows=35000)
# print("into df ::::::::::::::::::::::::")

# engine = create_engine('postgresql://postgres:Admin@2021@localhost:5432/detdb3')

# print("engine connected ::::::::::::::::::::::::::::::::")

# df.to_sql('detemployee', engine,index=False)

# print("executed :::::::::::::::::::::::::::::::::::")













# print("1111111111111111111111")

# # This CSV doesn't have a header so pass
# # column names as an argument
# columns = [
#     "age",
#     "work",
#     "fwt",
#     "education",
#     "edu_no",
#     "marital_status",
#     "occupation",
#     "relationship",
#     "race",
#     "sex",
#     "cap_gain",
#     "cap_loss",
#     "hours_pw",
#     "native_country",
#     "salary"
# ]

# print("222222222222222222222")

# # Instantiate sqlachemy.create_engine object
# engine = create_engine('postgresql://postgres:Admin@2021@localhost:5432/detdb5')

# print("333333333333333333333333")

# # Create an iterable that will read "chunksize=1000" rows
# # at a time from the CSV file
# for df in pd.read_csv(r'C:\Users\PC\Downloads\adult_dataset.csv',names=columns,chunksize=1000):
#   df.to_sql(
#     'detapp_detemployee', 
#     engine,
#     index=False,
#     if_exists='append' # if the table already exists, append this data
#   )

# print("444444444444444444444444444444444")












# print("111111111111111111111111")
# import psycopg2
# conn = psycopg2.connect("host=localhost dbname=detdb9 user=postgres password=Admin@2021")
# cur = conn.cursor()
# with open(r"C:\Users\PC\Downloads\adult_dataset.csv", 'r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f) # Skip the header row.
#     cur.copy_from(f, 'detapp_detemployee', sep=',')

# conn.commit()

# print("222222222222222222222222")


# import pandas as pd

# df = pd.read_csv(r"C:\Users\PC\Downloads\adult_dataset.csv", index_col=0)

# for index, row in df.iterrows():
#     print(index,row)



# from .models import detemployee
# import pandas as pd

# filename = r'C:\Users\PC\Downloads\adult_dataset.csv'
# df = pd.read_csv(filename)

# for index, row in df.iterrows():
#         if detemployee.objects.exists():
#             pass
#         else:
#             # print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
#             detemployee.objects.create(age = row[0], work = row[1] , fwt = row[2] , education = row[3] ,
#             edu_no = row[4] , marital_status = row[5] ,  occupation = row[6] ,relationship = row[7],
#             race = row[8] , sex = row[9] , cap_gain = row[10] , cap_loss = row[11] , hours_pw = row[12] ,
#             native_country = row[13] ,salary = row[14])





# from csv import reader
# with open(r'C:\Users\PC\Downloads\adult_dataset.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#         print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])


# from csv import DictReader
# with open(r'C:\Users\PC\Downloads\adult_dataset.csv', 'r') as read_obj:
#     csv_dict_reader = DictReader(read_obj)
#     column_names = csv_dict_reader.fieldnames
#     print(column_names)







# import pandas as pd
# # from sqlalchemy import create_engine

# # # This CSV doesn't have a header so pass
# # # column names as an argument

# columns = [
#     "age",
#     "work",
#     "fwt",
#     "education",
#     "edu_no",
#     "marital_status",
#     "occupation",
#     "relationship",
#     "race",
#     "sex",
#     "cap_gain",
#     "cap_loss",
#     "hours_pw",
#     "native_country",
#     "salary"
# ]

# # Load in the data
# df = pd.read_csv(r"C:\Users\PC\Downloads\adult_dataset.csv",names=columns)

# # Instantiate sqlachemy.create_engine object
# engine = create_engine('postgresql://postgres:Admin@2021@localhost:5432/detdb5')

# # Save the data from dataframe to
# # postgres table "iris_dataset"

# df.to_sql('detdb5_detemployee', engine,index=False) # Not copying over the index
