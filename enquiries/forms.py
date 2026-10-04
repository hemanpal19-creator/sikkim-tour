from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    """
    Form used by visitors to submit a journey planning enquiry.
    """

    class Meta:
        model = Enquiry

        fields = (
            "name",
            "email",
            "phone",
            "travel_date",
            "travelers",
            "message",
        )

        widgets = {
            "travel_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell us about the journey you have in mind...",
                }
            ),
        }
        


# Why?

# Using a ModelForm means Django automatically connects the form to your Enquiry model.

# So later:

# Website form
#       ↓
# Django validation
#       ↓
# Enquiry model
#       ↓
# SQLite
#       ↓
# Admin

# No duplicated field definitions.