from .models import Modals, Type, Price, SaleLocationCopard, SaleLocationIAAI
from django import forms


class ModalForm(forms.ModelForm):
    class Meta:
        model = Modals
        fields = ['type', 'price', 'phone']

    type = forms.ModelChoiceField(queryset=Type.objects.all(), empty_label=None, widget=forms.RadioSelect)
    price = forms.ModelChoiceField(queryset=Price.objects.all(), empty_label=None, widget=forms.RadioSelect)


# class CalculatorFormCopart(forms.ModelForm):
#     class Meta:
#         model = SaleLocationCopard
#         fields = '__all__'
#
#
# class CalculatorFormIAAI(forms.ModelForm):
#     class Meta:
#         model = SaleLocationIAAI
#         fields = '__all__'
#
#
# class AuctionForm(forms.Form):
#     CHOICES = (
#         ('IAAI', 'IAAI'),
#         ('Copart', 'Copart'),
#     )
#     auction = forms.ChoiceField(choices=CHOICES)
#     # sale_location = forms.ChoiceField(choices=[])
#     #
#     # def __init__(self, *args, **kwargs):
#     #     super(AuctionForm, self).__init__(*args, **kwargs)
#     #     auction_choice = self.initial.get('auction') or self.data.get('auction')
#     #     if auction_choice == 'IAAI':
#     #         sale_locations = SaleLocationIAAI.objects.values_list('id', 'name')
#     #     elif auction_choice == 'Copart':
#     #         sale_locations = SaleLocationCopard.objects.values_list('id', 'name')
#     #     else:
#     #         sale_locations = []
#     #     self.fields['sale_location'].choices = sale_locations
#
#
#
# class EngineForm(forms.Form):
#     CHOICES = (
#         ('gas', 'Бензин'),
#         ('diesel', 'Дизель'),
#         ('electro', 'Електро'),
#     )
#
#     operation = forms.ChoiceField(
#         choices=CHOICES,
#         widget=forms.RadioSelect(attrs={'class': 'radio-buttons'}),  # Add CSS class for styling if needed
#     )
#
#
# class AuctionPriceForm(forms.Form):
#     auction_price = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))

class CalculateForm (forms.Form):
    OPTIONS_AUCTION = (
        ('', '---------'),
        ('IAAI', 'IAAI'),
        ('Copart', 'Copart'),
            )
    auction_field = forms.ChoiceField(
        choices=OPTIONS_AUCTION,
        widget=forms.Select,
        initial='',
        label='Обери аукціон'
    )

    OPTIONS_ENGINE = (
        ('', '---------'),
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Електро', 'Електро'),
        )

    fuel_field = forms.ChoiceField(
        choices=OPTIONS_ENGINE,
        widget=forms.Select,
        initial='',
        label='Обери тип двигуна'
    )

    auction_price = forms.CharField(
        max_length=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label= 'Bартість автомобіля на аукціоні'
    )

    engine_field = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Обʼєм двигуна (Обʼєм батареї (кВт) для електромобілів)'
    )

    year_field = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Рік випуску'
    )

    copart_data = forms.CharField(widget=forms.HiddenInput, required=False)
    iaai_data = forms.CharField(widget=forms.HiddenInput, required=False)

