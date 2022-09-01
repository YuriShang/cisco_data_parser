from netmiko import ConnectHandler
from datetime import datetime
from settings import config
import sys


# Параметры устройства
device = {
    'device_type': config["device"]["type"],
    'ip': config["device"]["ip"],
    'username': config["user"]["username"],
    'password': config["user"]["password"]
}

# Подключение к устройству
net_connect = ConnectHandler(**device)


def cisco_commands(num):
    """
    Возвращает сформированный словарь команд либо одну выбранную команду
    """
    dct = {
        1: {"show version": "Версия коммутатора"},
        2: {"show startup-config": "Стартовая конфигурация коммутатора"},
        3: {"show running-config": "Текущая конфигурация коммутатора"},
        4: {"show ip interface | include line protocol|access list": "Сведения о списках контроля доступа (ACL) коммутатора"},
        5: {"show interface": "Сведения об интерфейсах коммутатора"}
    }
    if num != 0:
        return dct[num]

    commands = {}

    for k, v in dct.items():
        for key, value in v.items():
            commands.setdefault(key, value)

    return commands


# Валидация номера команды
try:
    command_number = int(sys.argv[1])
except ValueError:
    print("\nНеобходимо ввести целочисленное значение\n")
    sys.exit()
except IndexError:
    print("Необходимо ввести номер команды")
    sys.exit()


if not 0 <= command_number <= 5:
    print("\nНеверный номер команды\n")
    sys.exit()

print()
commands = cisco_commands(command_number)


# Пробегаемся по всем командам и поочередно выполняем каждую,
# либо выполняем одну выбранную

print(f"Отчет сформирован: {datetime.now()}\n")
for command, description in commands.items():
    res = net_connect.send_command(command)
    print("===========================================================================================================")
    print(f"{description}")
    print("===========================================================================================================")
    print(f"\n{res}\n")


