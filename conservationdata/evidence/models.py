from django.db import models


# Create your models here.
class Evidence(models.Model):

    """
    """

    INTERVENTION_TYPES = [
        ('Experimental', 'Experimental'),
        ('Observational', 'Observational'),
        ('Review', 'Review')
    ]

    intervention_title = models.CharField(max_length=255)
    species_group = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    effectiveness_score = models.IntegerField()
    evidence_type = models.CharField(max_length=20, choices=INTERVENTION_TYPES)
    brief_outcome = models.TextField()

    def __str__(self):
        return self.intervention_title
