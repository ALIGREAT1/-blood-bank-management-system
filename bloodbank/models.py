
from django.db import models


# =====================================================
# 1. BLOOD TYPE
# =====================================================

class BloodType(models.Model):
    bloodtypeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


# =====================================================
# 2. DONOR
# =====================================================

class Donor(models.Model):
    donorid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    bloodtype = models.ForeignKey(
        BloodType,
        on_delete=models.PROTECT,
        related_name='donors'
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Inactive', 'Inactive'),
        ],
        default='Active'
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# =====================================================
# 3. RECIPIENT
# =====================================================

class Recipient(models.Model):
    recipientid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    bloodtype = models.ForeignKey(
        BloodType,
        on_delete=models.PROTECT,
        related_name='recipients'
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# =====================================================
# 4. HOSPITAL
# =====================================================

class Hospital(models.Model):
    hospitalid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


# =====================================================
# 5. COLLECTION SITE
# =====================================================

class CollectionSite(models.Model):
    collectionsiteid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# =====================================================
# 6. DONATION
# =====================================================

class Donation(models.Model):
    donationid = models.AutoField(primary_key=True)

    donor = models.ForeignKey(
        Donor,
        on_delete=models.PROTECT,
        related_name='donations'
    )

    bloodtype = models.ForeignKey(
        BloodType,
        on_delete=models.PROTECT
    )

    collectionsite = models.ForeignKey(
        CollectionSite,
        on_delete=models.PROTECT,
        related_name='donations'
    )

    donationdate = models.DateField()

    def __str__(self):
        return f"Donation {self.donationid} - {self.donor}"


# =====================================================
# 7. BLOOD UNIT
# =====================================================

class BloodUnit(models.Model):
    bloodunitid = models.AutoField(primary_key=True)

    donation = models.ForeignKey(
        Donation,
        on_delete=models.PROTECT,
        related_name='blood_units'
    )

    volume = models.PositiveIntegerField()
    expirydate = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Reserved', 'Reserved'),
            ('Issued', 'Issued'),
            ('Expired', 'Expired'),
            ('Quarantined', 'Quarantined'),
        ],
        default='Quarantined'
    )

    def __str__(self):
        return f"Blood Unit {self.bloodunitid}"


# =====================================================
# 8. BLOOD TEST
# =====================================================

class BloodTest(models.Model):
    testid = models.AutoField(primary_key=True)

    bloodunit = models.ForeignKey(
        BloodUnit,
        on_delete=models.PROTECT,
        related_name='tests'
    )

    testtype = models.CharField(max_length=100)

    testresult = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Passed', 'Passed'),
            ('Failed', 'Failed'),
        ],
        default='Pending'
    )

    labtechnician = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Test {self.testid} - {self.testtype}"


# =====================================================
# 9. BLOOD REQUEST
# =====================================================

class BloodRequest(models.Model):
    requestid = models.AutoField(primary_key=True)

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.PROTECT,
        related_name='blood_requests'
    )

    recipient = models.ForeignKey(
        Recipient,
        on_delete=models.PROTECT,
        related_name='blood_requests'
    )

    bloodtype = models.ForeignKey(
        BloodType,
        on_delete=models.PROTECT
    )

    requestdate = models.DateField(auto_now_add=True)
    unitsrequired = models.PositiveIntegerField()

    priority = models.CharField(
        max_length=20,
        choices=[
            ('Normal', 'Normal'),
            ('Urgent', 'Urgent'),
            ('ICU', 'ICU'),
        ],
        default='Normal'
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
            ('Fulfilled', 'Fulfilled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Request {self.requestid} - {self.hospital}"
