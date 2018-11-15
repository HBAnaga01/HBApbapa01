from django.db import models
from django.utils import timezone

### from adminsortable.models import SortableMixin  #HBAnaga20180921 1430 add

class Post(models.Model):

### class Post(SortableMixin):  # HBAnaga20180921 1425 UP --> models.Model up


    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    # HBAnaga 20180921 1409 add start
###    the_order = models.PositiveIntegerField(
###      default=0, editable=False, db_index=True)
    # HBAnaga 20180921 1409 add end
 
    # HBAnaga 20180921 1409 add start
###   class Meta:
###        ordering = ['the_order']
    # HBAnaga 20180921 1409 add end
    
    
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
#HBAnaga ADD start upload

  


#HBAnaga ADD end upload
        
        
