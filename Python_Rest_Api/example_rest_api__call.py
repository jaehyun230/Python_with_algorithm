import request

#Rest API 경로를 통하여 Response 데이터 받아오기
target_url = "https://jsonplaceholder.typicode.com/users"
response = request.get(url=target_url)

#Response 데이터가 json 형식임으로 바로 파이썬 객체로 변환
data = repose.json()

#모든 사용자(user) 정보를 확인하여 name 정보만 삽입
name_list = []
for user in data :
  name_list.append(user['name'])
 
print(name_list)
