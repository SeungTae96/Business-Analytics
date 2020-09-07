#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("21대 총선의 국회의원 수는 총 300명인데 그 중 지역구는 253명이고 전국구는 47명입니다")
a_region = int(input("A당의 지역구 당선 의원수를 입력하세요: "))
b_region = int(input("B당의 지역구 당선 의원수를 입력하세요: "))
c_region = int(input("C당의 지역구 당선 의원수를 입력하세요: "))
d_region = int(input("D당의 지역구 당선 의원수를 입력하세요: "))
a_approval = float(input("A당의 정당 지지율을 입력하세요 (%): "))
b_approval = float(input("B당의 정당 지지율을 입력하세요 (%): "))
c_approval = float(input("C당의 정당 지지율을 입력하세요 (%): "))
d_approval = float(input("D당의 정당 지지율을 입력하세요 (%): "))

#전국구 의원수 계산 
#준연동형 의석 수 계산시 음수면 값을 0 으로 대체
def calculator(region, approval) :
    country = round(max((approval * 300 / 100 - region) / 2, 0)) + round(approval * 17 / 100) 
    return country

#봉쇄조항 설정 & 결과
if a_approval < 3 or b_approval < 3 or c_approval < 3 or d_approval < 3 : 
    print("비례대표 의석 배분을 받기 위해선 최소 정당 득표율(3%, 봉쇄조항)을 넘겨야 합니다")
else : 
    print("A당의 지역구 의원수는", a_region, "명 이고, 전국구 의원수는", calculator(a_region, a_approval), "명 입니다")
    print("B당의 지역구 의원수는", b_region, "명 이고, 전국구 의원수는", calculator(b_region, b_approval), "명 입니다")
    print("C당의 지역구 의원수는", c_region, "명 이고, 전국구 의원수는", calculator(c_region, c_approval), "명 입니다")
    print("D당의 지역구 의원수는", d_region, "명 이고, 전국구 의원수는", calculator(d_region, d_approval), "명 입니다")

