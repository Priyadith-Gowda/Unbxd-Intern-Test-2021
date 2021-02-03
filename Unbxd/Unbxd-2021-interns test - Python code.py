import requests
import json

def jsonreader():
    response = requests.get("https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=743&start=0")
    json_data = json.loads(response.text)
    x = json_data["response"]["products"]
    final_res = []
    for l in x:
        
        for i in l.keys():
            if(type(l[i]) is list):
                for j in range(len(l[i])):
                    if("::" in str(l[i][j])):
                        l_res = l[i][j].split("::")
                        if(l_res[1] not in final_res):
                            final_res.append(l_res[1])
                    else:
                        if(l[i][j] not in final_res):
                            final_res.append(l[i][j])

        for i in range(len(final_res)):
            if(final_res[i] == 'False'):
                final_res[i] = "NO"
            elif(final_res[i] == "True"):
                final_res[i] = "YES"
    #print((final_res))
    
    for i in final_res:
        print(str(i)+',')

if __name__=="__main__":
    jsonreader()
