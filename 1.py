from fastapi import FastAPI #импортируем FastAPI
from fastapi.responses import FileResponse #импортируем класс

app = FastAPI() #создаем экземпляр приложения

@app.get("/") #создаем декоратор

def read_index(): #объявляем функцию
    return FileResponse('index.html') #Это тело функции. Оно и помогает обратиться к нашему файлу