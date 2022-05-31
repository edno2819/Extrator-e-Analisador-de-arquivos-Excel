from utils import *
from functionsGui import ExecuteGui
import eel
import sys
import logging
import json


class GerePages:
    current_html = 'index.html'

    def ChangeCurrentPage(self, name):
        self.current_html = name


@eel.expose
def bnt_catalogar():
    eel.creat_table_catalog(json.dumps({}))


@eel.expose
def bnt_scrap():
    print('teste botão 1')
    ExecuteGui.button1()


@eel.expose
def bnt_analise():
    print('teste botão 2')
    ExecuteGui.button2()


@eel.expose
def bnt_scrap_corection():
    print('teste botão 3')
    ExecuteGui.button3()


def close_callback(route, websockets):
    global log
    sys.exit(0)


def start_eel():
    ports = [8000, 8001, 27000, 8080]

    eel.start('index.html', size=(690, 540), close_callback=close_callback)

    # for port in ports:
    #     if not check_port(port):
    #         eel.start("index.html", size=(730, 700),
    #                   port=port, close_callback=close_callback)
    #         return


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename=f'./src/logs/log_{time_now("%Y-%m-%d %H-%M-%S")}.log',
        filemode='w',
    )

    log = logging.getLogger(__name__)

    eel.init('src/views')
    start_eel()
