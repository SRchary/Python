from django import forms

class contact_form(forms.Form):
    name    = forms.CharField( max_length =5 ,widget=forms.TextInput(attrs={'autocomplete':'off' ,'class':'form-control' ,"placeholder":'Enter Name' }))
    email   = forms.EmailField(label ="Enter Email",widget=forms.TextInput(attrs={'autocomplete':'off' ,'class':'form-control',"placeholder":'Enter Email' }))
    address1 = forms.CharField(label ="Address",widget=forms.TextInput(attrs={'autocomplete':'off' ,'class':'form-control',"placeholder":'Address1' }))
    address2 = forms.CharField(label ="Address",widget=forms.TextInput(attrs={'autocomplete':'off' ,'class':'form-control',"placeholder":'Address 2' }))
    city = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off' ,'class':'form-control',"placeholder":'City' }))
    state  = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off' ,'id':"state_id",'class':'form-control',"placeholder":'State' }))
    zip    = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off' ,'id':"zip_id",'class':'form-control',"placeholder":'ZIP Code' }))
    send_email = forms.BooleanField(required=False,initial=False,label='Extra cheeze')


