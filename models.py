from django.db import models

class PostalAddress(models.Model):
    postcode = models.CharField(max_length=8)
    posttown = models.CharField(max_length=30)
    dependent_locality = models.CharField(max_length=35)
    double_dependent_locality = models.CharField(max_length=35)
    throughfare_and_descriptor = models.CharField(max_length=80)
    dependent_throughfare_and_descriptor = models.CharField(max_length=80)
    building_number = models.CharField(max_length=4)
    building_name  = models.CharField(max_length=50)
    subbuilding_name = models.CharField(max_length=30)
    po_box = models.CharField(max_length=6)
    department_name = models.CharField(max_length=60)
    organisation_name = models.CharField(max_length=60)
    udprn_key = models.CharField(max_length=8)
    postcode_type = models.CharField(max_length=1)
    su_organisation_indicator = models.CharField(max_length=1)
    delivery_point_suffix = models.CharField(max_length=2)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.postcode


# Create your models here.
