from django.db import models

# Create your models here.


class District(models.Model):
    district_num = models.IntegerField(default=0)

    def __str__(self):
        return "District " + str(self.district_num)


class BallotText(models.Model):
    ballot_text = models.CharField(max_length=120)
    district_num = models.IntegerField(default=0)
    ballot_cat = models.IntegerField(default=0)

    def __str__(self):
        return self.ballot_text


class Candidate(models.Model):
    candidate = models.ForeignKey(BallotText, on_delete=models.CASCADE)
    candidate_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)
    district_num = models.IntegerField(default=0)
    ballot_cat = models.IntegerField(default=0)

    def __str__(self):
        return self.candidate_text
