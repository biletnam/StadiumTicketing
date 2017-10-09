from django import forms
from django.contrib import messages
from .models import EventBook, Event


class EventBookCreateForm(forms.ModelForm):
    """
    Form class to handle creation of event bookings
    """
    class Meta:
        model = EventBook
        fields = ('amount', 'tickets')

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')

        if 'event' in kwargs:
            self.event = kwargs.pop('event')

        super(EventBookCreateForm, self).__init__(*args, **kwargs)

        # check if event is payable
        is_payable = self.event.is_payable

        if not is_payable:
            self.fields.pop('amount')

        for field_name, field_obj in self.fields.items():
            field_obj.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super(EventBookCreateForm, self).clean()
        paid_amount = cleaned_data.get('amount')
        tickets = cleaned_data.get('tickets')

        if paid_amount is None:
            error = 'This field is required'
            self.add_error('amount', error)
            return cleaned_data

        def check_payment(amount_paid, tickets_no):
            event_amount = self.event.price  # set event amount
            expected_amount = event_amount * tickets_no
            if amount_paid < expected_amount:
                error = ("The amount you paid is less than expected amount."
                         " We expected you to pay KES%(expected)s but you paid "
                         "KES%(amount_paid)s" % dict(expected=expected_amount,
                                                     amount_paid=paid_amount))
                self.add_error('amount', error)

            if amount_paid > expected_amount:
                error = ("The amount you paid exceeds required amount."
                         " We expected you to pay KES%(expected)s but you paid "
                         "KES%(amount_paid)s" % dict(expected=expected_amount,
                                                     amount_paid=paid_amount))
                self.add_error('amount', error)

        if self.event.is_payable:
            check_payment(paid_amount, tickets)

        return cleaned_data

    def save(self, commit=True):
        obj = super(EventBookCreateForm, self).save(commit=False)
        obj.event = self.event
        obj.user = self.request.user
        obj.save()
        return obj


class AdminCreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AdminCreateEventForm, self).clean()
        is_payable = cleaned_data.get('is_payable')
        price = cleaned_data.get('price')
        if is_payable is True:
            if not price:
                error = ('is payable is set True therefore price field'
                         ' cannot be left blank')
                self.add_error('price', error)

        if not is_payable and price:
            cleaned_data['price'] = None

        return cleaned_data
