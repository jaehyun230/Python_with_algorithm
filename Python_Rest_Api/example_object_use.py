import json

#사전 자료형(dict) 선언
user = {
  "id" = "jaehyon"
  "password" = "1234567"
  "age" = "28"
  "hobby" = ["computer", "research", "webtoon"]
}

#파이썬 객체 json 객체로 변환
json_data = json.dumps(user, indent = 4)
print(json_data)
