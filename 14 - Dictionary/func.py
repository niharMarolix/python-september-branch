# import requests
# import math

# def getWeather(apiKey, city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
#     response = (requests.get(url))
#     resp = response.json()
#     kelvinTemp = resp['main']['temp']
#     celcius = math.ceil(kelvinTemp-273)
#     return celcius

# cityName = "gachibowli"
# apiKey = "15d458110f825260aa4bca35dc1ad88a"
# result = getWeather( apiKey, cityName)
# print(result)


# # def prod(num1, num2):
# #     res = num1*num2
# #     print(res)

# # a = 3
# # b = 8
# # prod(b,a)



# def greet(a):
#     print("hi")
#     return a

# a = "how do u do"
# greet("hey bro")
# print(a)


