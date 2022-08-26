from time import strftime, time
from django.db import models
from datetime import datetime, timedelta, timezone

# Create your models here.

class order (models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_customer = models.CharField(max_length=200)
    order_complete = models.BooleanField()
    order_count = models.IntegerField()
    order_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        name_in_admin = str(self.order_id) + " " + str(self.order_customer)
        return str(name_in_admin)

    def deadline_days(self):
        realise_date = self.order_date + timedelta(days=14, hours=12)

        now = datetime.now(timezone.utc)

        deadline_days = realise_date - now

        days_count = deadline_days.days
        return days_count

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ['order_complete', 'order_date', ]



