"""
Datastore models
"""
from google.cloud import ndb

# Create your models here.

class Redirect(ndb.Model):
    """Redirect model."""
    name = ndb.StringProperty()
    destination_url = ndb.StringProperty()
    created_on = ndb.DateTimeProperty(auto_now_add=True)
