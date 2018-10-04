from django import forms
from expense.models import ExpenseClaim
from expense.choices import *
class ExpenseClaimForm(forms.ModelForm):
    branchcode = forms.CharField(
        required=True,
        label="Branch Code",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                
                }))
    bankcode = forms.ChoiceField(
        choices = BANK_CODE, 
        label="Bank Code",
        widget=forms.Select(attrs={
                'class' : 'form-control',
                
                }), 
                required=True)
    glcode = forms.ChoiceField(
        choices = GL_CODE, 
        label="GL Code",
        widget=forms.Select(attrs={
                'class' : 'form-control',
                
                }), 
                required=True)
    bankacc = forms.CharField(
        required=True,
        label="Bank Acc No.",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type':'number'
                }))
    bankaccname = forms.CharField(
        required=True,
        label="Bank Acc Name",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
                }))
    transactiondate = forms.CharField(
        required=True,
        label="Transaction Date",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Choose your date here'
                }))
    costcenter = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
                }))
    
    description = forms.CharField(
        required=True,
        label="Description",
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'cols': 2, 'rows': 4,
                'placeholder': 'Write Your Description'
                }))
    amount = forms.CharField(
        required=True,
        label="Amount",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type':'number',
                'placeholder': 'RM'
                }))

    class Meta:
        model = ExpenseClaim
        fields = (
            'glcode',
            'bankcode',
        'branchcode',
                   
                   'bankacc',
                   'bankaccname',
                   'transactiondate',
                    'costcenter',
                     
                    'description',
                    'amount'
                    )
        
    
