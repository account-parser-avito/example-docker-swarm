"""
Запуск парсера
"""


import uvicorn


HOST = '0.0.0.0'
PORT = 5010
DEBUG = False
RELOAD = True


if __name__ == "__main__":
    uvicorn.run('main:app', host=HOST, port=PORT, debug=DEBUG, reload=RELOAD)


