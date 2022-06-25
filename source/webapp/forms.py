from django import forms

from webapp.models import Advertisement


class AdvertisementCreateForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'description', 'picture', 'price')


class AdvertisementApproveForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('status', 'published_at')


class AdvertisementUpdateForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'description', 'picture', 'price')
