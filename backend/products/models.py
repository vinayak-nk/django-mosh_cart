from django.db.models import (
  Model, CharField, TextField, DecimalField
)

# Create your models here.
class Product(Model):
  title = CharField(max_length=128)
  content = TextField(blank=True, null=True)
  price = DecimalField(max_digits=15, decimal_places=2, default=99.99)
  
  @property
  def sale_price(self):
    saleprice = float(self.price)
    return saleprice * 0.8
  
  def get_discount(self):
    return '20%'