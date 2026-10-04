from django.shortcuts import redirect, render

from .forms import EnquiryForm


def enquiry_create(request):
    """
    Displays the journey planning form and saves valid submissions.
    """

    if request.method == "POST":
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("enquiry_success")

    else:
        form = EnquiryForm()

    return render(
        request,
        "enquiries/form.html",
        {
            "form": form,
        },
    )


def enquiry_success(request):
    """
    Confirmation page shown after a successful enquiry submission.
    """

    return render(
        request,
        "enquiries/success.html",
    )