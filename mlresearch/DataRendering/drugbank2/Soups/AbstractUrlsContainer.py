"""En este módulo se creó una clase abstracta que, en otras palabras, es un objeto de Python que pretende ser un
generador de los url presentes en el sitio que se ingresa como parámetro en el método .__init__(). Cabe destacar
que las clases abstractas no pueden inicializarse instancias directamente en el código, sino que se debe declarar
subclases concretas, que es precisamente lo que se hace en los módulos BankSoup.py y MedSoup.py."""
# TODO Se debe investigar sobre cómo lograr declarar adecuadamente de modo que los objetos de sus subclases sean
#  también instancias de un "Generator".
from abc import ABC, abstractmethod
from time import sleep


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException


class AbstractUrlsContainer(ABC):
    """Una instancia hipotética de esta clase lo que hace es comenzar a buscar links en el link que se le ingrese
    como parámetro de inicialización. Además, guarda los links en un iterador. No se darán detalles de cada método,
    pues no se considera necesario dado que se asume que los lectores de esta documentación no conocen el lenguaje
    Python 3.11"""
    @abstractmethod
    def __init__(self, executable_path, domain, parser="html.parser"):
        self.pages = set()
        self.first_soup = self.get_soup(executable_path, domain, parser)
        self.num, self.end = self.get_all_urls(self.first_soup, executable_path, domain, parser)

    @staticmethod
    @abstractmethod
    def prepare_driver(executable_path):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=executable_path, options=options)
        return driver

    @abstractmethod
    def get_page_source(self, executable_path, url):
        driver = self.prepare_driver(executable_path)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        return page_source

    @abstractmethod
    def get_soup(self, executable_path, url, parser="html.parser"):
        page_source = self.get_page_source(executable_path, url)
        return BeautifulSoup(page_source, parser)

    @abstractmethod
    def get_all_urls(self, soup, executable_path, domain, parser="html.parser"):
        for links in soup.find_all("a"):
            if "href" in links.attrs:
                if links.attrs["href"] in self.pages:
                    continue
                else:
                    new_link = links.attrs["href"]
                    self.pages.add(new_link)
                    sleep(3)
                    try:
                        soup = self.get_soup(executable_path, "".join([domain, new_link]), parser)
                    except WebDriverException:
                        soup = self.get_soup(executable_path, new_link, parser)
                    try:
                        self.get_all_urls(soup, executable_path, domain, parser)
                    except TimeoutException:
                        print("TimedPromise timed out after 300000 ms")
                        continue
                    except RecursionError:
                        print("RecursionError")
                        continue
        return 0, len(self.pages) - 1

    def __iter__(self):
        return iter(self.pages)
