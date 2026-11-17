
from django.contrib import admin
from .models import (
    BloodType,
    Donor,
    Recipient,
    Hospital,
    CollectionSite,
    Donation,
    BloodUnit,
    BloodTest,
    BloodRequest
)


# ADMIN SITE CUSTOMIZATION
admin.site.site_header = "Blood Bank Management System"
admin.site.site_title = "Blood Bank Administration"
admin.site.index_title = "System Administration Dashboard"


# BLOOD TYPE
@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    list_display = ('bloodtypeid', 'name')
    search_fields = ('name',)
    ordering = ('name',)


# DONOR
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = (
        'donorid', 'firstname', 'lastname',
        'age', 'bloodtype', 'phone', 'status'
    )
    list_filter = ('bloodtype', 'status')
    search_fields = ('firstname', 'lastname', 'phone', 'email')
    ordering = ('firstname',)


# RECIPIENT
@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        'recipientid', 'firstname', 'lastname',
        'age', 'bloodtype', 'phone'
    )
    list_filter = ('bloodtype',)
    search_fields = ('firstname', 'lastname', 'phone')
    ordering = ('firstname',)


# HOSPITAL
@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospitalid', 'name', 'address', 'contact', 'email')
    search_fields = ('name', 'address', 'contact', 'email')
    ordering = ('name',)


# COLLECTION SITE
@admin.register(CollectionSite)
class CollectionSiteAdmin(admin.ModelAdmin):
    list_display = ('collectionsiteid', 'name', 'location')
    search_fields = ('name', 'location')
    ordering = ('name',)


# DONATION
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'donationid', 'donor', 'bloodtype',
        'collectionsite', 'donationdate'
    )
    list_filter = ('bloodtype', 'collectionsite', 'donationdate')
    search_fields = (
        'donor__firstname',
        'donor__lastname',
        'collectionsite__name'
    )
    date_hierarchy = 'donationdate'
    ordering = ('-donationdate',)


# BLOOD UNIT
@admin.register(BloodUnit)
class BloodUnitAdmin(admin.ModelAdmin):
    list_display = (
        'bloodunitid', 'donation', 'volume',
        'expirydate', 'status'
    )
    list_filter = ('status', 'expirydate')
    search_fields = (
        'donation__donor__firstname',
        'donation__donor__lastname'
    )
    date_hierarchy = 'expirydate'
    ordering = ('expirydate',)


# BLOOD TEST
@admin.register(BloodTest)
class BloodTestAdmin(admin.ModelAdmin):
    list_display = (
        'testid', 'bloodunit', 'testtype',
        'testresult', 'labtechnician'
    )
    list_filter = ('testresult', 'testtype')
    search_fields = ('testtype', 'labtechnician', 'remarks')
    ordering = ('-testid',)


# BLOOD REQUEST
@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'requestid', 'hospital', 'recipient',
        'bloodtype', 'unitsrequired',
        'priority', 'status', 'requestdate'
    )
    list_filter = ('priority', 'status', 'bloodtype')
    search_fields = (
        'hospital__name',
        'recipient__firstname',
        'recipient__lastname'
    )
    date_hierarchy = 'requestdate'
    ordering = ('-requestdate',)
