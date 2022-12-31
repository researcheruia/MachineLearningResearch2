"""El objetivo de este módulo es optimizar la ejecución del programa."""
from time import sleep
from threading import Thread

from . import BankSoup, MedSoup


def drug_bank_data():
    executable_path = "geckodriver.exe"
    domain = "https://go.drugbank.com"
    parser = "html.parser"
    return BankSoup(executable_path, domain, parser)


def med_scape_data():
    executable_path = "geckodriver.exe"
    domain = "https://reference.medscape.com/drugs/psychiatrics"
    parser = "html.parser"
    return MedSoup(executable_path, domain, parser)


def executing():
    threads = []
    for i in range(10):
        t1 = Thread(target=drug_bank_data)
        threads.append(t1)
        t2 = Thread(target=med_scape_data)
        threads.append(t2)
    for t in threads:
        t.start()
        sleep(5)
        print("thread playing the game...")
    for t in threads:
        t.join()

    return "It's time to play the game..."
