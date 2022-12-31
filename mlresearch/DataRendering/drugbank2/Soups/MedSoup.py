"""Módulo análogo a BankSoup.py, solo que creado específicamente para la información existente en
https://reference.medscape.com"""
# TODO Las mejorías que se le pueden hacer a este módulo van de la mano con las que se le pueden hacer a BankSoup.py
from abc import ABCMeta
from json import dump
from time import sleep


from selenium.common.exceptions import TimeoutException, WebDriverException


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
        super().__init__(executable_path, domain, parser)
        self.info = self.get_all_info(executable_path, parser)

    def prepare_driver(self, executable_path):
        return super().prepare_driver(executable_path)

    def get_page_source(self, executable_path, url):
        return super().get_page_source(executable_path, url)

    def get_soup(self, executable_path, url, parser="html.parser"):
        return super().get_soup(executable_path, url, parser)

    def get_all_urls(self, soup, executable_path, domain, parser="html.parser"):
        soup.find("div", attrs={"id": "drugdbmain2"})
        for links in soup.find_all("a"):
            if "href" in links.attrs:
                if links.attrs["href"] in self.pages or "drugs" not in links.attrs["href"]:
                    continue
                else:
                    new_link = links.attrs["href"]
                    self.pages.add(new_link)
                    sleep(3)
                    try:
                        soup = self.get_soup(executable_path, new_link, parser)
                    except WebDriverException:
                        soup = self.get_soup(executable_path, "".join([domain, new_link]), parser)
                    try:
                        self.get_all_urls(soup, executable_path, domain, parser)
                    except TimeoutException:
                        print("TimedPromise timed out after 300000 ms")
                        continue
                    except RecursionError:
                        print("RecursionError")
                        continue
        return 0, len(self.pages) - 1

    def get_all_info(self, executable_path, parser):
        dict_ = {
            "drugs": []
        }
        for url in self.pages:
            soup = self.get_soup(executable_path, url, parser)
            if not self.get_adverse_effects(soup):
                continue
            else:
                dict_["drugs"].append(self.get_adverse_effects(soup))
                with open("adverse.json", "w") as json_file:
                    dump(dict_, json_file)
        return iter(dict_["drugs"])

    def get_adverse_effects(self, soup):
        name = soup.find("span", attrs={"class": "drug_section_link"})
        if name:
            h2 = soup.find("h2", text="Adverse Effects")
            if h2:
                text = [p.text for p in h2.find_all_next("p") if p.text in self.adverse_effects]
            else:
                return False
            return {
                name: {
                    key: int(key in text) for key in self.adverse_effects
                }
            }
        return False
