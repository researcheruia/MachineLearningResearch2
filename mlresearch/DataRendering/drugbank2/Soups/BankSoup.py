"""En este módulo se declara una clase concreta inherente de AbstractUrlsContainer"""
# TODO Las mejorías que se le pueden hacer a esta clase están más relacionadas con lo que se le pueda implementar a
#  la clase abstracta padre. Sin embargo, se piensa que es posible optimizar la descarga de las imágenes
from abc import ABCMeta
from json import dump
from time import sleep


import numpy as np
from re import compile
from requests import Session
from requests.utils import default_headers
from requests.exceptions import ChunkedEncodingError


from . import AbstractUrlsContainer


class BankSoup(AbstractUrlsContainer, metaclass=ABCMeta):
    """BankSoup es una clase específica que sirve para descargar información sobre fármacos de
    https://go.drugbank.com Lo más importante de la clase es que descarga las imágenes de las moléculas en formato
    .svg. Adicionalmente, recopila información de las masas molares de cada activo, así como otra información de tipo
    identificativa."""

    def __init__(self, executable_path, domain, parser="html.parser"):
        self.get_all_info(
            domain,
            executable_path,
            parser,
            "C:/Users/mvmor/OneDrive/Escritorio/MachineLearningResearch/mlresearch/media"
        )
        super().__init__(executable_path, domain, parser)

    def first_soup(self):
        return self.first_soup

    def prepare_driver(self, executable_path):
        return super().prepare_driver(executable_path)

    def get_page_source(self, executable_path, url):
        return super().get_page_source(executable_path, url)

    def get_soup(self, executable_path, url, parser="html.parser"):
        return super().get_soup(executable_path, url, parser)

    def get_all_urls(self, soup, executable_path, domain, parser="html.parser"):
        return super().get_all_urls(soup, executable_path, domain, parser)

    def get_molecular_info(
            self,
            list_simple_data,
            soup,
            images_path,
            image_identifier="structure",
            weight_identifier="weight"):
        list_keys = [
            "generic_name",
            "iupac_name",
            "kind",
            "case_number",
            "smiles"
        ]
        molecular_image = self.get_image(soup, images_path, image_identifier)
        if molecular_image:
            molecule_simple_data = {
                key: self.get_simple_data(soup, element) for key, element in zip(list_keys, list_simple_data)
            }
            average_w, isotopic_w = self.get_weight(soup, weight_identifier)
            molecular_weight = {
                "average_weight": float(average_w),
                "mono_isotopic_weight": float(isotopic_w)
            }
            image_dict = {
                "molecule": molecular_image
            }
            return molecule_simple_data | molecular_weight | image_dict
        else:
            return False

    def get_all_info(self, domain, executable_path, parser, images_path,):
        list_simple_data = [
            "generic-name",
            "iupac-name",
            "type",
            "cas-number",
            "smiles"
        ]
        url_pattern = ("{}/drugs/DB{}".format(domain, str(number)[1:]) for number in range(100000, 199999))
        molecules_gen = (self.get_molecular_info(
            list_simple_data,
            self.get_soup(executable_path, url, parser),
            images_path
        ) for url in url_pattern)
        dict_ = {"drugs": []}
        for molecules in molecules_gen:
            if not molecules:
                continue
            else:
                dict_["drugs"].append(molecules)
                with open("molecules.json", "w") as json_file:
                    dump(dict_, json_file)
        return molecules_gen

    @staticmethod
    def get_image(soup, path, identifier="structure"):
        try:
            href = soup.find("div", {"class": identifier}).find("a", {"class": "moldbi-vector-thumbnail"}).get("href")
        except AttributeError:
            return None
        url_image = "https://go.drugbank.com{}".format(href)
        session = Session()
        response = session.get(url_image, headers=default_headers(), stream=True)
        session.close()
        pattern_name = compile(r"/DB\d{5}")
        name = pattern_name.findall(href)[0]
        sleep(3)
        if response.ok:
            with open("".join((path, name, ".svg")), "wb") as molecule_img:
                try:
                    molecule_img.write(response.content)
                except ChunkedEncodingError:
                    return False
            return "".join((path, name, ".svg"))
        return False

    @staticmethod
    def get_weight(soup, identifier="weight"):
        try:
            weights = soup.find("dt", {"id": identifier}).find_next_sibling("dd").text.strip().split(" ")
            if weights:
                try:
                    return float(weights[1]), float(weights[-1])
                except IndexError:
                    return float(weights[-1]), np.NaN
                except ValueError:
                    return float(weights[-1]), np.NaN
            else:
                return np.NaN, np.NaN
        except AttributeError:
            return np.NaN, np.NaN

    @staticmethod
    def get_simple_data(soup, identifier):
        return soup.find("dt", {"id": identifier}).find_next_sibling("dd").text
