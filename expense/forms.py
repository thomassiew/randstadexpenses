from django import forms
from expense.models import ExpenseClaim
class ExpenseClaimForm(forms.ModelForm):
    name = forms.CharField(required=True)
    branchcode = forms.CharField(required=True)
    bankcode = forms.CharField(required=True)
    bankaccname = forms.CharField(required=True)
    transactiondate = forms.CharField(required=True)
    costcenter = forms.CharField(required=True)
    glcode = forms.CharField(required=True)
    description = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    class Meta:
        model = ExpenseClaim
        fields = ('name',
        'branchcode',
                   'bankcode',
                   'bankacc',
                   'bankaccname',
                   'transactiondate',
                    'costcenter',
                    'glcode' ,
                    'description',
                    'amount'
                    )

