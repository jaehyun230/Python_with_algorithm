import json

#사전 자료형(dict) 선언
user = {
  "id" = "jaehyon"
  "password" = "1234567"
  "age" = "28"
  "hobby" = ["computer", "research", "webtoon"]
}

#파이썬 json 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file :
  json_data = json.dump(user, file, indent=4)
