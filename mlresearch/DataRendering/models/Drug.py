from django.db import models


def adverse_default():
    return {
        "Abdominal cramps": 0,
        "Abdominal pain": 0,
        "Affected liability": 0,
        "Agitation": 0,
        "Akathisia": 0,
        "Alertness decreased": 0,
        "Anorexia": 0,
        "Anxiety": 0,
        "Asthenia": 0,
        "Circadian rhythm disruption": 0,
        "Constipation": 0,
        "Decreased appetite": 0,
        "Decreased weight": 0,
        "Depression": 0,
        "Diarrhea": 0,
        "Dizziness": 0,
        "Drooling": 0,
        "Drowsiness": 0,
        "Dyspepsia": 0,
        "Dysphoria": 0,
        "Ejaculation disorder": 0,
        "Enuresis": 0,
        "Fever": 0,
        "Headache": 0,
        "Hypercholesterolemia": 0,
        "Hyperglycemia": 0,
        "Hyperprolactinemia": 0,
        "Hypertriglyceridemia": 0,
        "Hypotension": 0,
        "Increased appetite": 0,
        "Increased sweating": 0,
        "Insomnia": 0,
        "Irritability": 0,
        "Nasopharyngitis": 0,
        "Nausea": 0,
        "Nervousness": 0,
        "Orthostatic hypotension": 0,
        "Parkinsonism": 0,
        "Rhinitis": 0,
        "Rhinorrhea": 0,
        "Somnolence": 0,
        "Tachycardia": 0,
        "Tremor": 0,
        "Urinary incontinence": 0,
        "Vomiting": 0,
        "Weight gain": 0,
        "Xerostomia": 0
    }


class Drug(models.Model):
    molecule = models.FileField(upload_to="molecules/", null=True, blank=True, default=None)
    generic_name = models.CharField(max_length=200)
    iupac_name = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    smiles = models.TextField()
    average_weight = models.FloatField()
    mono_isotopic_weight = models.FloatField()
    case_number = models.CharField(max_length=100)
    adverse_effects = models.JSONField(default=adverse_default)




