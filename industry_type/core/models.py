from django.db import models


class IndustryType(models.Model):
    industry_type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.industry_type


class CompanyDetails(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    contact = models.PositiveBigIntegerField()
    industry_type = models.ForeignKey(IndustryType, related_name='industry', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} owned by {self.owner_name}'
