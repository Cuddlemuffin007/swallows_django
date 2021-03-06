from django.db import models


class BattingStat(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=30)
    age = models.IntegerField()
    g = models.IntegerField()
    pa = models.IntegerField()
    ab = models.IntegerField()
    r = models.IntegerField()
    h = models.IntegerField()
    _2b = models.IntegerField()
    _3b = models.IntegerField()
    hr = models.IntegerField()
    rbi = models.IntegerField()
    sb = models.IntegerField()
    cs = models.IntegerField()
    bb = models.IntegerField()
    so = models.IntegerField()
    ba = models.FloatField()
    obp = models.FloatField()
    slg = models.FloatField()
    ops = models.FloatField()
    tb = models.IntegerField()
    gdp = models.IntegerField()
    hbp = models.IntegerField()
    sh = models.IntegerField()
    sf = models.IntegerField()
    ibb = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.f_name, self.l_name)
