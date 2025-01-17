from django.contrib import admin
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_filter=('realtor','id')
    list_editable=('is_published',)
    search_fields=('title','description','address','city','state','zipcode')

# Register your models here.
admin.site.register(Listing,ListingAdmin)