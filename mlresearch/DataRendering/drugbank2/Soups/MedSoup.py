"""Módulo análogo a BankSoup.py, solo que creado específicamente para la información existente en
https://reference.medscape.com"""
# TODO Las mejorías que se le pueden hacer a este módulo van de la mano con las que se le pueden hacer a BankSoup.py
from abc import ABCMeta
from copy import deepcopy
from json import dump
from os.path import exists
import re


from selenium.common.exceptions import WebDriverException


from . import AbstractUrlsContainer


class MedSoup(AbstractUrlsContainer, metaclass=ABCMeta):

    def __init__(self, executable_path, domain, parser="html.parser"):
        self.adverse_effects = [
            "Abdominal cramps",
            "Abdominal pain",
            "Affected liability",
            "Agitation",
            "Akathisia",
            "Alertness decreased",
            "Anorexia",
            "Anxiety",
            "Asthenia",
            "Circadian rhythm disruption",
            "Constipation",
            "Decreased appetite",
            "Decreased weight",
            "Depression",
            "Diarrhea",
            "Dizziness",
            "Drooling",
            "Drowsiness",
            "Dyspepsia",
            "Dysphoria",
            "Ejaculation disorder",
            "Enuresis",
            "Fever",
            "Headache",
            "Hypercholesterolemia",
            "Hyperglycemia",
            "Hyperprolactinemia",
            "Hypertriglyceridemia",
            "Hypotension",
            "Increased appetite",
            "Increased sweating",
            "Insomnia",
            "Irritability",
            "Nasopharyngitis",
            "Nausea",
            "Nervousness",
            "Orthostatic hypotension",
            "Parkinsonism",
            "Rhinitis",
            "Rhinorrhea",
            "Somnolence",
            "Tachycardia",
            "Tremor",
            "Urinary incontinence",
            "Vomiting",
            "Weight gain",
            "Xerostomia"
        ]
        self.get_all_info(executable_path, parser)
        super().__init__(executable_path, domain, parser)

    def prepare_driver(self, executable_path):
        return super().prepare_driver(executable_path)

    def get_page_source(self, executable_path, url):
        return super().get_page_source(executable_path, url)

    def get_soup(self, executable_path, url, parser="html.parser"):
        return super().get_soup(executable_path, url, parser)

    def get_all_urls(self, soup, executable_path, domain, parser="html.parser"):
        super().get_all_urls(soup, executable_path, domain, parser)

    def compare_effect(self, effect):
        for element in self.adverse_effects:
            if re.match(element, effect, flags=re.IGNORECASE):
                return element
        return effect

    def get_adverse_effects(self, soup, path):
        try:
            name = soup.find("span", attrs={"class": "drug_section_link"})
        except AttributeError:
            return False
        if name:
            name = name.text
            div = soup.find("div", attrs={"id": "content_4"})
            if div:
                div2 = div.find("div", attrs={"class": "refsection_content"})
                text = [p.text for p in div2.find_all("p") if p.text in self.adverse_effects]
                text_2 = list(map(self.compare_effect, text))
                dict_ = {
                    name: {
                        key: int(bool(key in text_2)) for key in self.adverse_effects
                    }
                }
                if not exists(path.format(name.replace("/","-"))):
                    with open(path.format(name.replace("/","-")), "w") as js:
                        dump(dict_, js)
                    return dict_
                return False
            return False
        return False

    def get_all_info(self, executable_path, parser="html.parser"):
        path = "C:/Users/mvmor/OneDrive/Escritorio/MachineLearningResearch/mlresearch/json2/{}.json"
        with open("links.txt", "r") as links_file:
            links = set([link.strip("\n") for link in links_file.readlines()])
        links2 = deepcopy(links)
        for link in links2:
            links.remove(link)
            soup = self.get_soup(executable_path, link, parser)
            if soup:
                soup2 = soup.find("ul", attrs={"class": "classdruglist" })
                if soup2:
                    a = soup2.find_all("a")
                    for tags in a:
                        url = tags.attrs["href"]
                        if url:
                            s = self.get_soup(executable_path, url, parser)
                            dict_ = self.get_adverse_effects(s, path)
                            if dict_:
                                print(dict_)
                                continue
                            else:
                                with open("links.txt", "w") as l_file:
                                    links.add(url)
                                    try:
                                        print(*list(links), sep="\n", file=l_file)
                                    except PermissionError:
                                        print(*list(links), sep="\n")
                                self.get_all_info(executable_path, parser)
                        else:
                            continue
                else:
                    continue
            else:
                continue




