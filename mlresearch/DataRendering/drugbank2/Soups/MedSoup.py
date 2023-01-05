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
        self.pages = set()
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
        self.first_soup = self.get_soup(executable_path, domain, parser)
        self.get_all_urls(self.first_soup, executable_path, domain, parser)
        self.num, self.end = 0, len(self.pages) - 1

    def prepare_driver(self, executable_path):
        return super().prepare_driver(executable_path)

    def get_page_source(self, executable_path, url):
        return super().get_page_source(executable_path, url)

    def get_soup(self, executable_path, url, parser="html.parser"):
        return super().get_soup(executable_path, url, parser)

    def get_all_urls(self, s, executable_path, domain, parser="html.parser"):
        path = "C:/Users/mvmor/OneDrive/Escritorio/MachineLearningResearch/mlresearch/json2/{}.json"
        ul = s.find("ul", attrs={"class": "classdruglist"})
        if ul:
            for a in ul.find_all("a"):
                if "href" in a.attrs:
                    href = self.get_adverse_effects(domain, a, path, executable_path, parser)
                    if href and href not in self.pages:
                        self.pages.add(href)
                    with open("links.txt", "w") as links_file:
                        print(*list(self.pages), sep="\n", file=links_file)
                    try:
                        soup = self.get_soup(executable_path, "".join([domain, href]), parser)
                    except WebDriverException:
                        soup = self.get_soup(executable_path, href, parser)
                    if soup.find("ul", attrs={"class": "classdruglist"}):
                        try:
                            boolean = self.get_all_urls(soup, executable_path, domain, parser)
                            continue
                        except AttributeError:
                            print(href)
                            continue
                    else:
                        continue
                else:
                    continue
        return True

    def compare_effect(self, effect):
        for element in self.adverse_effects:
            if re.match(element, effect, flags=re.IGNORECASE):
                return element
        return effect

    def get_adverse_effects(self, domain, a, path, executable_path, parser):
        name = a.text
        href = a.attrs["href"]
        try:
            soup = self.get_soup(executable_path, "".join([domain, href]), parser)
        except WebDriverException:
            soup = self.get_soup(executable_path, href, parser)
        content = soup.find("div", attrs={"id": "content_4"})
        if content and not exists(path.format(name.replace("/", "-"))):
            div = content.find("div", attrs={"class": "refsection_content"})
            text = [p.text for p in div.find_all("p") if p.text in self.adverse_effects]
            text_2 = list(map(self.compare_effect, text))
            dict_ = {
                name: {
                    key: int(bool(key in text_2)) for key in self.adverse_effects
                }
            }
            with open(path.format(name.replace("/", "-")), "w") as js:
                dump(dict_, js)
        return href






