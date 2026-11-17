
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Donor, Recipient, BloodUnit, Hospital, BloodRequest, Donation, BloodTest, CollectionSite
from .forms import DonorForm, RecipientForm, HospitalForm, DonationForm,  BloodUnitForm, BloodTestForm, BloodRequestForm, CollectionSiteForm


# DASHBOARD
@login_required
def dashboard(request):
    context = {
        'total_donors': Donor.objects.count(),
        'total_blood_units': BloodUnit.objects.count(),
        'total_hospitals': Hospital.objects.count(),
        'total_requests': BloodRequest.objects.count(),
    }

    return render(request, 'bloodbank/dashboard.html', context)


# REGISTER DONOR
@login_required
def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'bloodbank/add_donor.html', {
        'form': form
    })


# VIEW DONORS
@login_required
def donor_list(request):
    donors = Donor.objects.select_related('bloodtype').all()

    return render(request, 'bloodbank/donor_list.html', {
        'donors': donors
    })


# UPDATE DONOR
@login_required
def update_donor(request, donor_id):
    donor = get_object_or_404(Donor, donorid=donor_id)

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)

        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'bloodbank/add_donor.html', {
        'form': form,
        'page_title': 'Update Donor',
        'button_text': 'Update Donor'
    })


# DELETE DONOR
@login_required
def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, donorid=donor_id)

    if request.method == 'POST':
        donor.delete()
        return redirect('donor_list')

    return render(request, 'bloodbank/delete_donor.html', {
        'donor': donor
    })


# REGISTER RECIPIENT - CREATE
@login_required
def add_recipient(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form = RecipientForm()

    return render(request, 'bloodbank/add_recipient.html', {
        'form': form
    })


# VIEW RECIPIENTS - READ
@login_required
def recipient_list(request):
    recipients = Recipient.objects.select_related('bloodtype').all()

    return render(request, 'bloodbank/recipient_list.html', {
        'recipients': recipients
    })


# UPDATE RECIPIENT
@login_required
def update_recipient(request, recipient_id):
    recipient = get_object_or_404(
        Recipient, recipientid=recipient_id
    )

    if request.method == 'POST':
        form = RecipientForm(request.POST, instance=recipient)

        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form = RecipientForm(instance=recipient)

    return render(request, 'bloodbank/add_recipient.html', {
        'form': form,
        'page_title': 'Update Recipient',
        'button_text': 'Update Recipient'
    })


# DELETE RECIPIENT
@login_required
def delete_recipient(request, recipient_id):
    recipient = get_object_or_404(
        Recipient, recipientid=recipient_id
    )

    if request.method == 'POST':
        recipient.delete()
        return redirect('recipient_list')

    return render(request, 'bloodbank/delete_recipient.html', {
        'recipient': recipient
    })


# REGISTER HOSPITAL - CREATE
@login_required
def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()

    return render(request, 'bloodbank/add_hospital.html', {
        'form': form
    })


# VIEW HOSPITALS - READ
@login_required
def hospital_list(request):
    hospitals = Hospital.objects.all()

    return render(request, 'bloodbank/hospital_list.html', {
        'hospitals': hospitals
    })


# UPDATE HOSPITAL
@login_required
def update_hospital(request, hospital_id):
    hospital = get_object_or_404(
        Hospital, hospitalid=hospital_id
    )

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)

        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)

    return render(request, 'bloodbank/add_hospital.html', {
        'form': form,
        'page_title': 'Update Hospital',
        'button_text': 'Update Hospital'
    })


# DELETE HOSPITAL
@login_required
def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(
        Hospital, hospitalid=hospital_id
    )

    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')

    return render(request, 'bloodbank/delete_hospital.html', {
        'hospital': hospital
    })


# ADD DONATION
@login_required
def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('donation_list')

    else:
        form = DonationForm()

    return render(request, 'bloodbank/add_donation.html', {
        'form': form
    })


# VIEW ALL DONATIONS
@login_required
def donation_list(request):
    donations = Donation.objects.select_related(
        'donor',
        'bloodtype',
        'collectionsite'
    ).all()

    return render(request, 'bloodbank/donation_list.html', {
        'donations': donations
    })


# UPDATE DONATION
@login_required
def update_donation(request, donation_id):
    donation = get_object_or_404(
        Donation,
        donationid=donation_id
    )

    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)

        if form.is_valid():
            form.save()
            return redirect('donation_list')

    else:
        form = DonationForm(instance=donation)

    return render(request, 'bloodbank/add_donation.html', {
        'form': form,
        'page_title': 'Update Donation',
        'button_text': 'Update Donation'
    })


# DELETE DONATION
@login_required
def delete_donation(request, donation_id):
    donation = get_object_or_404(
        Donation,
        donationid=donation_id
    )

    if request.method == 'POST':
        donation.delete()
        return redirect('donation_list')

    return render(request, 'bloodbank/delete_donation.html', {
        'donation': donation
    })

    # ADD BLOOD UNIT
@login_required
def add_blood_unit(request):
    if request.method == 'POST':
        form = BloodUnitForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blood_unit_list')

    else:
        form = BloodUnitForm()

    return render(request, 'bloodbank/add_blood_unit.html', {
        'form': form
    })


# VIEW BLOOD INVENTORY
@login_required
def blood_unit_list(request):
    blood_units = BloodUnit.objects.select_related(
        'donation',
        'donation__donor',
        'donation__bloodtype'
    ).all()

    return render(request, 'bloodbank/blood_unit_list.html', {
        'blood_units': blood_units
    })


# UPDATE BLOOD UNIT
@login_required
def update_blood_unit(request, bloodunit_id):
    blood_unit = get_object_or_404(
        BloodUnit,
        bloodunitid=bloodunit_id
    )

    if request.method == 'POST':
        form = BloodUnitForm(request.POST, instance=blood_unit)

        if form.is_valid():
            form.save()
            return redirect('blood_unit_list')

    else:
        form = BloodUnitForm(instance=blood_unit)

    return render(request, 'bloodbank/add_blood_unit.html', {
        'form': form,
        'page_title': 'Update Blood Unit',
        'button_text': 'Update Blood Unit'
    })


# DELETE BLOOD UNIT
@login_required
def delete_blood_unit(request, bloodunit_id):
    blood_unit = get_object_or_404(
        BloodUnit,
        bloodunitid=bloodunit_id
    )

    if request.method == 'POST':
        blood_unit.delete()
        return redirect('blood_unit_list')

    return render(request, 'bloodbank/delete_blood_unit.html', {
        'blood_unit': blood_unit
    })

    # ADD BLOOD TEST
@login_required
def add_blood_test(request):
    if request.method == 'POST':
        form = BloodTestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blood_test_list')

    else:
        form = BloodTestForm()

    return render(request, 'bloodbank/add_blood_test.html', {
        'form': form
    })


# VIEW ALL BLOOD TESTS
@login_required
def blood_test_list(request):
    blood_tests = BloodTest.objects.select_related(
        'bloodunit',
        'bloodunit__donation',
        'bloodunit__donation__donor'
    ).all()

    return render(request, 'bloodbank/blood_test_list.html', {
        'blood_tests': blood_tests
    })


# UPDATE BLOOD TEST
@login_required
def update_blood_test(request, test_id):
    blood_test = get_object_or_404(
        BloodTest,
        testid=test_id
    )

    if request.method == 'POST':
        form = BloodTestForm(request.POST, instance=blood_test)

        if form.is_valid():
            form.save()
            return redirect('blood_test_list')

    else:
        form = BloodTestForm(instance=blood_test)

    return render(request, 'bloodbank/add_blood_test.html', {
        'form': form,
        'page_title': 'Update Blood Test',
        'button_text': 'Update Blood Test'
    })


# DELETE BLOOD TEST
@login_required
def delete_blood_test(request, test_id):
    blood_test = get_object_or_404(
        BloodTest,
        testid=test_id
    )

    if request.method == 'POST':
        blood_test.delete()
        return redirect('blood_test_list')

    return render(request, 'bloodbank/delete_blood_test.html', {
        'blood_test': blood_test
    })


  # ADD BLOOD REQUEST
@login_required
def add_blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blood_request_list')
    else:
        form = BloodRequestForm()

    return render(request, 'bloodbank/add_blood_request.html', {
        'form': form,
        'page_title': 'Add Blood Request',
        'button_text': 'Save Blood Request'
    })


# LIST BLOOD REQUESTS
@login_required
def blood_request_list(request):
    blood_requests = BloodRequest.objects.select_related(
        'hospital',
        'recipient',
        'bloodtype'
    ).all()

    return render(request, 'bloodbank/blood_request_list.html', {
        'blood_requests': blood_requests
    })


# UPDATE BLOOD REQUEST
@login_required
def update_blood_request(request, request_id):
    blood_request = get_object_or_404(
        BloodRequest,
        requestid=request_id
    )

    if request.method == 'POST':
        form = BloodRequestForm(
            request.POST,
            instance=blood_request
        )

        if form.is_valid():
            form.save()
            return redirect('blood_request_list')
    else:
        form = BloodRequestForm(instance=blood_request)

    return render(request, 'bloodbank/add_blood_request.html', {
        'form': form,
        'page_title': 'Update Blood Request',
        'button_text': 'Update Blood Request'
    })


# DELETE BLOOD REQUEST
@login_required
def delete_blood_request(request, request_id):
    blood_request = get_object_or_404(
        BloodRequest,
        requestid=request_id
    )

    if request.method == 'POST':
        blood_request.delete()
        return redirect('blood_request_list')

    return render(request, 'bloodbank/delete_blood_request.html', {
        'blood_request': blood_request
    })  


    # ADD COLLECTION SITE
@login_required
def add_collection_site(request):
    if request.method == 'POST':
        form = CollectionSiteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('collection_site_list')
    else:
        form = CollectionSiteForm()

    return render(request, 'bloodbank/add_collection_site.html', {
        'form': form,
        'page_title': 'Add Collection Site',
        'button_text': 'Save Collection Site'
    })


# LIST COLLECTION SITES
@login_required
def collection_site_list(request):
    collection_sites = CollectionSite.objects.all()

    return render(request, 'bloodbank/collection_site_list.html', {
        'collection_sites': collection_sites
    })


# UPDATE COLLECTION SITE
@login_required
def update_collection_site(request, site_id):
    collection_site = get_object_or_404(
        CollectionSite,
        collectionsiteid=site_id
    )

    if request.method == 'POST':
        form = CollectionSiteForm(
            request.POST,
            instance=collection_site
        )

        if form.is_valid():
            form.save()
            return redirect('collection_site_list')
    else:
        form = CollectionSiteForm(instance=collection_site)

    return render(request, 'bloodbank/add_collection_site.html', {
        'form': form,
        'page_title': 'Update Collection Site',
        'button_text': 'Update Collection Site'
    })


# DELETE COLLECTION SITE
@login_required
def delete_collection_site(request, site_id):
    collection_site = get_object_or_404(
        CollectionSite,
        collectionsiteid=site_id
    )

    if request.method == 'POST':
        collection_site.delete()
        return redirect('collection_site_list')

    return render(request, 'bloodbank/delete_collection_site.html', {
        'collection_site': collection_site
    })