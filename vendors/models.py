from django.db import models


class Vendor(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("F&B", "F&B"),
        ("Non-F&B", "Non-F&B"),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    social_media_alias = models.CharField(max_length=255)
    ssm_no = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    product_picture = models.ImageField(upload_to="product_pictures/")
    menu = models.FileField(upload_to="menus/")

    # user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    # description = models.TextField(blank=True, null=True, default = None)
    # rating = models.DecimalField(max_digits = 1, decimal_places = 1, default=0)


class Market(models.Model):
    date = models.DateField()


class MarketApplicant(models.Model):
    SLOT_TYPE_CHOICES = [
        ("SILVER", "SILVER"),
        ("GOLD", "GOLD"),
        ("PLATINUM", "PLATINUM"),
    ]

    market = models.ForeignKey("Market", on_delete=models.CASCADE)
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    slot = models.CharField(max_length=20, choices=SLOT_TYPE_CHOICES)
    certificate = models.FileField(upload_to="certificates/")
    equipment_list = models.FileField(upload_to="equipment_lists/")

    approved = models.BooleanField(default=False)
    # if selected
    proof_of_payment = models.FileField(
        upload_to="proof_of_payments/", blank=True, null=True, default=None
    )
    booth_no = models.CharField(max_length=255, blank=True, null=True, default=None)


class Notification(models.Model):
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


"""
vendor registers an account (name, phone number, social media alias, ssm no, product name, product type, product picture, menu, equipment)
they can edit their own vendor page, can view others but not edit other vendor pages

admins can delete and remove vendors


admins announce new market every week (2-per week)
vendors can apply by filling out a form only need to attach certificate, and equipment list as the others are already recorded in database

have a page only admins can view
    1. click on which market to view applicatns and which applicants to approve (click approve button next to each applicant entry)
    2. notify selected vendors to pay and distribute booth numbers
    3. add those to the MarketVendor database
    

maybe 2 months after a market, delete all applicant records (approved and non-approved) to clear space

"""
