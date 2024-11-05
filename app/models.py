from django.db import models
from datetime import date

# Create your models here.
class Customer(models.Model):
    userid=models.CharField(max_length=6,default='')
    mpin=models.IntegerField(default=000000)
    name=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)
    marital = models.CharField(max_length=10, choices=[('married', 'married'), ('unmarried', 'unmarried')],default='')
    occupation=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    district=models.CharField(max_length=100,default='')
    mandal=models.CharField(max_length=100,default='')
    village=models.CharField(max_length=100,default='')
    pin=models.IntegerField(default=0)
    permanent_address=models.CharField(max_length=100,default='')
    current_address=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=25,default='')

# Model for Family Details
class FamilyMember(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    name = models.CharField(max_length=100,default='')
    age = models.DateField(default=0)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],default='')
    relationship = models.CharField(max_length=100, choices=[('father', 'father'), ('mother', 'mother'), ('son', 'son'),('daughter','daughter'),('grandmother','grandmother'),('grandfather', 'grandfather'),('grandson','grandson'),('granddaughter','granddaughter')],default='')
    
# Model for Bank Account Details
class BankAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100,default='')
    type=models.CharField(max_length=50, choices=[('Current', 'Current Account'), ('savings', 'Savings'), ('joint', 'Joint Account')])
    bank_address = models.CharField(max_length=255,default='')
    account=models.IntegerField(default=0)
    ifsc=models.CharField(max_length=100,default='')
    nominee=models.CharField(max_length=50,default='')
    

# Model for Credit Details
class Credit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    amount=models.IntegerField(default=0)
    date=models.DateField(default='')
    mode=models.CharField(max_length=100,default='')
    
class Debit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    amount=models.IntegerField(default=0)
    date=models.DateField(default='')
    mode=models.CharField(max_length=100,default='')
    
class PF(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    UAN_no=models.IntegerField(default=0)
    PF_number_or_Number_ID=models.CharField(default='',max_length=50)
    upload_UAN_card=models.ImageField(upload_to='images')

# Model for Loan Details
class Personal_Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100, default='')
    product = models.CharField(max_length=200, default='')
    account = models.IntegerField(default=0)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, default='')
    ROI = models.CharField(max_length=100, default='')
    Date_of_sanction = models.DateField(default=date.today)  # No value parameter needed
    date_of_first_emi = models.DateField(default=date.today)  # No value parameter needed
    date_of_last_emi = models.DateField(default=date.today)  # No value parameter needed

class Gold_Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100, default='')
    product = models.CharField(max_length=200, default='')
    account = models.IntegerField(default=0)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, default='')
    ROI = models.CharField(max_length=100, default='')
    Date_of_sanction = models.DateField(default=date.today)  # No value parameter needed
     # No value parameter needed

    
class House_Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    account=models.IntegerField(default=0)
    product=models.CharField(max_length=200,default='')
    name = models.CharField(max_length=100)
    power=models.CharField(max_length=100,default='')
    amount=models.IntegerField(default=0)
    ROI=models.CharField(max_length=100,default='')
    term=models.CharField(max_length=100,default='')
    emi = models.DecimalField(max_digits=10, decimal_places=2,default='')
    
class Vehicle_Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    company_name=models.CharField(max_length=100,default='')
    vehicle_model=models.IntegerField(default=0)
    vehicle_type=models.CharField(max_length=50, choices=[('Two Wheeler', 'Two Wheeler'), ('Three Wheeler', 'Three Wheeler'), ('Four Wheeler', 'Four Wheeler')])
    engline_num=models.IntegerField(default=0)
    chasis_num=models.IntegerField(default=0)
    sanctioned_amout=models.IntegerField(default=0)
    term=models.IntegerField(default=0)

class Life_Insurance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    Policy_holder_name = models.CharField(max_length=50)
    Policy_number=models.IntegerField(default=0)
    Company = models.CharField(max_length=100, default='')
    starting_date = models.DateField(default=date.today)
    term=models.CharField(max_length=100, default='')
    premium=models.IntegerField(default=0)
    sum_assured=models.IntegerField(default=0)
    nominee_name=models.CharField(max_length=100,default='')
    
class Health_Insurance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    insurance_company=models.CharField(max_length=100,default='')
    employee_code=models.CharField(max_length=100,default='')
    policy_number=models.IntegerField(default=0)
    validity_period_from=models.DateField(default=date.today)
    validity_period_to=models.DateField(default=date.today)
    benificiary_name=models.CharField(max_length=100,default='')
    member_id=models.IntegerField(default=0)
    dob=models.DateField(default=date.today)
    relation=models.CharField(max_length=50, choices=[('Self', 'Self'), ('Father', 'Father'),('Mother', 'Mother'), ('Son', 'Son'),('Daughter','Daughter')])
    family_sum_assured=models.IntegerField(default=0)
    balance_sum_assured=models.IntegerField(default=0)
    
class Term_Insurance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    policy_holder_name=models.CharField(max_length=100,default='')
    ploicy_no=models.IntegerField(default=0)
    date_of_commencement_of_risk=models.DateField(default=date.today)      #start date
    premium_payment_term=models.CharField(max_length=50,default='')            # no of years
    premium_payment_mode=models.CharField(max_length=50, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')])             #monthly,yearly
    last_premium_date=models.DateField(default=date.today)
    critical_illness_beifit=models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')])   
    critical_illness_sumassured=models.IntegerField(default=0)
    accidental_death_benifit=models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')])   
    accdental_death_beifit_sum_assured=models.IntegerField(default=0)
    return_of_premium=models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')])   
    joint_life_cover=models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')])   
    policy_term=models.IntegerField(default='')
    due_date=models.DateField(default=date.today)                                  #when premium payable
    premium_amount=models.IntegerField(default=0)
    sum_assured=models.IntegerField(default=0)
    
class Vehicle_Insurance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    policy_number = models.CharField(max_length=50,default='')
    campany_name=models.CharField(max_length=100,default='')
    Name_of_insured=models.CharField(max_length=100,default='')
    reg_no=models.CharField(max_length=100,default=0)
    reg_date=models.DateField(default=date.today)
    engine_no=models.IntegerField(default=0)
    chasis_no=models.IntegerField(default=0)
    RTA_location=models.CharField(max_length=100,default='')
    Vehiclemake_model=models.CharField(max_length=100,default='')
    Period_of_insurance_from=models.DateField(default=date.today)
    Period_of_insurance_to=models.DateField(default=date.today)
    Agent_no=models.IntegerField(default=0)
    #upload_doc=models
    

# Model for Properties
class Property(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    property_type = models.CharField(max_length=100,choices=[('land', 'Land'), ('house', 'House'), ('flat', 'Flat'),('plot','Plots')])
    area = models.CharField(max_length=255,default='')
    address = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return f"{self.property_type} - {self.area}"

# Model for Investment Details
class Stocks_Investment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    name=models.CharField(max_length=100,default='')
    ursid=models.CharField(max_length=50,default='')
    demat=models.CharField(max_length=25,default='')
    platform=models.CharField(max_length=30,default='')
    company=models.CharField(max_length=50,default='')
    shares=models.IntegerField(default=0)
    buyprice=models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    
class Mutual(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    fund_name=models.CharField(max_length=100,default='')
    invested_amount=models.IntegerField(default=0)
    lock_in_period=models.IntegerField(default=0)
    fundplan=models.CharField(max_length=100,choices=[('growth plan', 'growth plan'),('dividend','dividend'),('dividend reinvestment','dividend reinvestment'),('term','term')])
    type=models.CharField(max_length=100,choices=[('One time', 'one time'),('sip','sip')])
    platform=models.CharField(max_length=50,default='')
    
    

class Schemes(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    type = models.CharField(max_length=100,choices=[('stategovernment', 'State Government'), ('centralgovernment', 'Central Government'),('bank','Bank'),('postal','Postal'),('others','others')])
    name=models.CharField(max_length=100,default='')
    holder_name=models.CharField(max_length=100,default='')
    number=models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    term=models.CharField(max_length=100,default='')
    start_date = models.DateField(default=date.today)
    end_date=models.DateField(default=date.today)
    maturity_date = models.DateField(default=date.today)
    
    
class Card(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    type = models.CharField(max_length=100,choices=[('credit', 'Credit Card'), ('debit', 'Debit Card'),('pancard','Pan Card'),('Rationcard', 'Ration Card'), ('aadharcard', 'Aadhar Card'),('Driving licence','Driving Licence'),('vehicle card','Vehicle Card'),('ID card','ID Card'),('voter card','Voter Card'),('Warranty card','Warranty Card'),('other','Other')])
    name=models.CharField(max_length=100,default='')
    card_num=models.CharField(max_length=100,default='')
    
    
class Documents(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sno=models.IntegerField(default=0)
    doc_name=models.CharField(max_length=150,default='')
    doc = models.ImageField(upload_to='images/')