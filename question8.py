# 8). Access the nested key ‘salary’ from the following JSON
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
#    { 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
#    { 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# emp-id     emp-name -- salary



import json

def salary(lst1):
    for a,v1 in lst1.items():
        for b,v2 in v1.items():
            print("name:", v2['name'])  #print name of employee
            print("salary:",v2['payable']['salary'])  #print salary of employees


sampleJson = '''{
    "company":{
        "employee1":{
            "name":"Pooja",
            "payable":{
                "salary":7000, "bonus":800
            }
        }, "employee2":{
            "name":"Harpreet",
            "payable":{
                "salary":8000, "bonus":900
            }
        }, "employee3":{
            "name":"Nidhi",
            "payable":{
                "salary":9000, "bonus":1000
            }
        }
    }
}'''

lst1 = json.loads(sampleJson)
salary(lst1)
