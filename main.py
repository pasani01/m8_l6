from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def index():
    return {'message':'Hello !'}

@app.get('/hello/{name}')
async def say_hello(name : str):
    return {'message': f'hello {name}'}

@app.get('/carp/{num}')
async def iki_kati(num: int):
    return {'message': f'{num} nin 2  kati {num*2} dir'}

@app.get('/chek/{name}/{age}')
async def chek_age(name : str ,age: int):
    if age>=18 :
        return {'message': f'sayin {name} siz yetiskin kisisiniz !'}
    return {'message': f'{name} sen yetiskin birey degilsin !'}
 
@app.get('/sum')
async def sum_value(a : int=0 ,b : int=0):
    s =a+b
    return {'message': f'{a} + {b} = {s}'}

@app.get('/weather/{city}')
async def city_weather(city: str = 'Tashkent'):
    return {'message': f'{city} de hava sicak'}

@app.get('/odd_or_even/{num}')
async def odd_or_even_call(num : int =0):
    if num % 2 ==0:
        return {'message' : f'{num} sayisi cift'}
    return {'message': f'{num} sayisi tek'}

@app.get('/length/{text}')
async def length_text(text: str = 'test'):
    s = len(text)
    return {'message': f'{text} uzunlugu {s} dir'}


@app.get('/convert')
async def convert_text(text : str='hello', upper : str ='false'):
    if upper =='true':
        s=text.upper()
        return {'message': f'{s}'}
    elif upper == 'false':
        s=text.lower()
        return {'message': f'{s}'}

    return {'message': f'hatali giris yaptiniz'}
    