from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Customer,  FamilyMember, BankAccount, Credit, Debit, Vehicle_Insurance, Property, Stocks_Investment,Schemes,Card,Personal_Loan,Gold_Loan,House_Loan,Documents,Mutual,Vehicle_Loan,Life_Insurance,Health_Insurance,Term_Insurance,PF
import random
import string

# Create your views here.
def Home(request):
    return render(request,'index.html')

def customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        marital=request.POST.get('marital')
        occupation=request.POST.get('occupation')
        state = request.POST.get('state')
        district = request.POST.get('district')
        mandal = request.POST.get('mandal')
        village = request.POST.get('village')
        pin = request.POST.get('pin')

        # Basic form validation (you can add more if needed)
        if len(phone) == 10 and len(pin) == 6:
            # Save the data to the database
            digits = ''.join(random.choices(string.digits, k=2))
            letters = ''.join(random.choices(string.ascii_uppercase, k=4))
            user= letters + digits
            Customer.objects.create(
                userid=user,
                name=name,
                phone=phone,
                marital=marital,
                occupation=occupation,
                state=state,
                district=district,
                mandal=mandal,
                village=village,
                pin=pin
            )
            
            return HttpResponseRedirect(f'/form-success/{user}')  # Redirect after successful submission
        else:
            error_message = "Please ensure the phone number is 10 digits and the pin code is 6 digits."
            return render(request, 'customer.html', {'error_message': error_message})

    return render(request, 'customer.html')

def form_success_view(request,id):
    customer = get_object_or_404(Customer, userid=id)

    if request.method == 'POST':
        mpin_new = request.POST.get('mpin')  # Assuming you're getting the new MPIN from a form

        # Update the mpin field
        customer.mpin = mpin_new
        customer.save(update_fields=['mpin'])  # Save only the 'mpin' field

        # After updating, you can redirect or render a response
        return redirect('login_page')
    
    return render(request,'form_success.html',{'user_id': id})

def login_page(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        mpin = request.POST.get('mpin')

        if Customer.objects.filter(userid=userid, mpin=mpin).exists():
            messages.success(request, 'Login successful')
            return HttpResponseRedirect(f'/user/{userid}')
    # If the request is GET, just render the login page
    return render(request, 'login.html')

def user(request, id):
    # Fetch the user
    user_data = Customer.objects.get(userid=id)
    
    # Fetch related data using ForeignKey relationship
    family_members = FamilyMember.objects.filter(customer=user_data)
    bank_accounts = BankAccount.objects.filter(customer=user_data)
    #House = House_Loan.objects.filter(customer=user_data)
    personal = Personal_Loan.objects.filter(customer=user_data)
    gold = Gold_Loan.objects.filter(customer=user_data)
    house=House_Loan.objects.filter(customer=user_data)
    credits = Credit.objects.filter(customer=user_data)
    debits = Debit.objects.filter(customer=user_data)
    properties = Property.objects.filter(customer=user_data)
    vehinsurance = Vehicle_Insurance.objects.filter(customer=user_data)
    stockinvestments = Stocks_Investment.objects.filter(customer=user_data)
    schemes=Schemes.objects.filter(customer=user_data)
    cards=Card.objects.filter(customer=user_data)
    documents=Documents.objects.filter(customer=user_data)
    funds=Mutual.objects.filter(customer=user_data)

    # Pass the fetched data to the template
    context = {
        'userid':id,
        'user': user_data,
        'family_members': family_members,
        'bank_accounts': bank_accounts,
        'house': house,
        'personal':personal,
        'gold':gold,
        'credits': credits,
        'debits': debits,
        'properties': properties,
        'vehinsurances': vehinsurance,
        'stockinvestments': stockinvestments,
        'schemes':schemes,
        'cards':cards,
        'docs':documents,
        'fundsinvestments':funds
    }

    return render(request, 'user_home.html', context)


def save_personal(request):
    
    if request.method == 'POST':
        userid = request.POST.get('userid')
        permanent_address = request.POST.get('permanent_address')
        current_address = request.POST.get('current_address')
        email = request.POST.get('email')

        # Assuming you have a 'Profile' model related to 'Customer'
        customer = Customer.objects.get(userid=userid)

        # Update the profile data for the user
        customer.permanent_address = permanent_address
        customer.current_address=current_address
        customer.email=email
        customer.save(update_fields=['permanent_address','current_address','email'])
        
        return HttpResponse("Profile updated successfully!")
    return HttpResponseRedirect(f'/user/{userid}')



# View for saving FamilyMember data
def family(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        relationship = request.POST.get('relationship')

        # Fetch the customer using userid
        customer = Customer.objects.get(userid=userid)
        
        # Save the family member data to the database
        FamilyMember.objects.create(
            customer=customer,  # Use the ForeignKey relationship
            sno=sno,
            name=name,
            age=age,
            gender=gender,
            relationship=relationship
        )
    return HttpResponseRedirect(f'/user/{userid}')

# View for saving BankAccount data
def bankacc(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        bank_name = request.POST.get('bank_name')
        type=request.POST.get('type')
        bank_address = request.POST.get('bank_address')
        account=request.POST.get('num')
        ifsc=request.POST.get('ifsc')
        nominee=request.POST.get('nominee')
        
        customer = Customer.objects.get(userid=userid)
        BankAccount.objects.create(
            customer=customer,
            sno=sno,
            bank_name=bank_name,
            type=type,
            bank_address=bank_address,
            account=account,
            ifsc=ifsc,
            nominee=nominee
        )
        # return HttpResponse('Bank account saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

# View for saving Credit data
def credit(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        address = request.POST.get('address')
        amount=request.POST.get('amount')
        date=request.POST.get('date')
        mode=request.POST.get('mode')
        customer = Customer.objects.get(userid=userid)
        Credit.objects.create(
            customer=customer,
            sno=sno,
            name=name,
            address=address,
            amount=amount,
            date=date,
            mode=mode
        )
        # return HttpResponse('Credit details saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

def debit(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        address = request.POST.get('address')
        amount=request.POST.get('amount')
        date=request.POST.get('date')
        mode=request.POST.get('mode')
        customer = Customer.objects.get(userid=userid)
        Debit.objects.create(
            customer=customer,
            sno=sno,
            name=name,
            address=address,
            amount=amount,
            date=date,
            mode=mode
        )
        # return HttpResponse('Debit details saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

def add_personal_loan(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        bank_name = request.POST.get('bank_name')
        ifsc = request.POST.get('ifsc')
        product = request.POST.get('product')
        account = request.POST.get('account')
        duration = request.POST.get('duration')
        Roi = request.POST.get('ROI')
        Date_of_sanction = request.POST.get('Date_of_sanction')
        loan_amount = request.POST.get('loan_amount')
        emi_amount = request.POST.get('emi_amount')
        date_of_first_emi = request.POST.get('date_of_first_emi')
        date_of_last_emi = request.POST.get('date_of_last_emi')

        customer = get_object_or_404(Customer, userid=userid)
        Personal_Loan.objects.create(
            customer=customer,
            sno=sno,
            bank_name=bank_name,
            ifsc=ifsc,
            product=product,
            account=account,
            loan_amount=loan_amount,
            duration=duration,
            ROI=Roi,
            Date_of_sanction=Date_of_sanction,
            emi_amount=emi_amount,
            date_of_first_emi=date_of_first_emi,
            date_of_last_emi=date_of_last_emi
        )
    return HttpResponseRedirect(f'/user/{userid}')


def edit_personal_loan(request, pk):
    loan = get_object_or_404(Personal_Loan, pk=pk)
    if request.method == "POST":
        userid = request.POST.get('userid')
        loan.sno = request.POST.get('sno')
        loan.bank_name = request.POST.get('bankname')
        loan.ifsc = request.POST.get('ifsc')
        loan.product = request.POST.get('product')
        loan.account = request.POST.get('account')
        loan.duration = request.POST.get('duration')
        loan.ROI = request.POST.get('ROI')
        loan.Date_of_sanction = request.POST.get('Date_of_sanction')
        loan.loan_amount = request.POST.get('loan_amount')
        loan.emi_amount = request.POST.get('emi_amount')
        loan.date_of_first_emi = request.POST.get('date_of_first_emi')
        loan.date_of_last_emi = request.POST.get('date_of_last_emi')
        loan.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'loan': loan})


def delete_personal_loan(request, pk):
    loan = get_object_or_404(Personal_Loan, pk=pk)
    loan.delete()
    return HttpResponse('Personal Loan deleted successfully')


def add_gold_loan(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        bank_name = request.POST.get('bank_name')
        ifsc = request.POST.get('ifsc')
        product = request.POST.get('product')
        account = request.POST.get('account')
        loan_amount = request.POST.get('loan_amount')
        duration = request.POST.get('duration')
        ROI = request.POST.get('ROI')
        Date_of_sanction = request.POST.get('Date_of_sanction')
        
        customer = get_object_or_404(Customer, userid=userid)
        Gold_Loan.objects.create(
            customer=customer,
            sno=sno,
            bank_name=bank_name,
            ifsc=ifsc,
            product=product,
            account=account,
            loan_amount=loan_amount,
            duration=duration,
            ROI=ROI,
            Date_of_sanction=Date_of_sanction,
        )
    return HttpResponseRedirect(f'/user/{userid}')


def edit_gold_loan(request, pk):
    loan = get_object_or_404(Gold_Loan, pk=pk)
    if request.method == "POST":
        userid = request.POST.get('userid')
        loan.sno = request.POST.get('sno')
        loan.bank_name = request.POST.get('bankname')
        loan.ifsc = request.POST.get('ifsc')
        loan.product = request.POST.get('product')
        loan.account = request.POST.get('account')
        loan.duration = request.POST.get('duration')
        loan.ROI = request.POST.get('ROI')
        loan.Date_of_sanction = request.POST.get('Date_of_sanction')
        loan.loan_amount = request.POST.get('loanamount')
        loan.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'loan': loan})


def delete_gold_loan(request, pk):
    loan = get_object_or_404(Gold_Loan, pk=pk)
    loan.delete()
    return HttpResponse('Gold Loan deleted successfully')


def add_vehicle_loan(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        company_name = request.POST.get('company_name')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_type = request.POST.get('vehicle_type')
        engine_num = request.POST.get('engine_num')
        chasis_num = request.POST.get('chasis_num')
        sanctioned_amount = request.POST.get('sanctioned_amount')
        term = request.POST.get('term')

        customer = get_object_or_404(Customer, userid=userid)
        Vehicle_Loan.objects.create(
            customer=customer,
            sno=sno,
            company_name=company_name,
            vehicle_model=vehicle_model,
            vehicle_type=vehicle_type,
            engline_num=engine_num,
            chasis_num=chasis_num,
            sanctioned_amout=sanctioned_amount,
            term=term,
        )
        return HttpResponseRedirect(f'/user/{userid}')

def edit_vehicle_loan(request, pk):
    loan = get_object_or_404(Vehicle_Loan, pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        loan.sno = request.POST.get('sno')
        loan.company_name = request.POST.get('company_name')
        loan.vehicle_model = request.POST.get('vehicle_model')
        loan.vehicle_type = request.POST.get('vehicle_type')
        loan.engline_num = request.POST.get('engine_num')
        loan.chasis_num = request.POST.get('chasis_num')
        loan.sanctioned_amout = request.POST.get('sanctioned_amount')
        loan.term = request.POST.get('term')
        loan.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'loan': loan})

def delete_vehicle_loan(request, pk):
    loan = get_object_or_404(Vehicle_Loan, pk=pk)
    loan.delete()
    return HttpResponse('Vehicle Loan deleted successfully')

def add_house_loan(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        account = request.POST.get('account')
        product = request.POST.get('product')
        name = request.POST.get('name')
        power = request.POST.get('power')
        amount = request.POST.get('amount')
        Roi = request.POST.get('ROI')
        term = request.POST.get('term')
        emi = request.POST.get('emi')
        
        customer = get_object_or_404(Customer, userid=userid)
        House_Loan.objects.create(
            customer=customer,
            sno=sno,
            account=account,
            product=product,
            name=name,
            power=power,
            amount=amount,
            ROI=Roi,
            term=term,
            emi=emi
        )
    return HttpResponseRedirect(f'/user/{userid}')
        


def edit_house_loan(request, pk):
    loan = House_Loan.objects.get(pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        loan.sno = request.POST.get('sno')
        loan.account = request.POST.get('account')
        loan.product = request.POST.get('product')
        loan.name = request.POST.get('name')
        loan.power = request.POST.get('power')
        loan.amount = request.POST.get('amount')
        loan.Roi = request.POST.get('ROI')
        loan.term = request.POST.get('term')
        loan.emi = request.POST.get('emi')
        loan.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'loan': loan})
        

def delete_house_loan(request, pk):
    loan = get_object_or_404(House_Loan, pk=pk)
    loan.delete()
    return HttpResponse('House Loan deleted successfully')


def add_term_insurance(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        policy_holder_name = request.POST.get('policy_holder_name')
        ploicy_no = request.POST.get('ploicy_no')
        date_of_commencement_of_risk = request.POST.get('date_of_commencement_of_risk')
        premium_payment_term = request.POST.get('premium_payment_term')
        premium_payment_mode = request.POST.get('premium_payment_mode')
        last_premium_date = request.POST.get('last_premium_date')
        critical_illness_beifit = request.POST.get('critical_illness_beifit')
        critical_illness_sumassured = request.POST.get('critical_illness_sumassured')
        accidental_death_benifit = request.POST.get('accidental_death_benifit')
        accdental_death_beifit_sum_assured = request.POST.get('accdental_death_beifit_sum_assured')
        return_of_premium = request.POST.get('return_of_premium')
        joint_life_cover = request.POST.get('joint_life_cover')
        policy_term = request.POST.get('policy_term')
        due_date = request.POST.get('due_date')
        premium_amount = request.POST.get('premium_amount')
        sum_assured = request.POST.get('sum_assured')

        customer = get_object_or_404(Customer, userid=userid)
        Term_Insurance.objects.create(
            customer=customer,
            sno=sno,
            policy_holder_name=policy_holder_name,
            ploicy_no=ploicy_no,
            date_of_commencement_of_risk=date_of_commencement_of_risk,
            premium_payment_term=premium_payment_term,
            premium_payment_mode=premium_payment_mode,
            last_premium_date=last_premium_date,
            critical_illness_beifit=critical_illness_beifit,
            critical_illness_sumassured=critical_illness_sumassured,
            accidental_death_benifit=accidental_death_benifit,
            accdental_death_beifit_sum_assured=accdental_death_beifit_sum_assured,
            return_of_premium=return_of_premium,
            joint_life_cover=joint_life_cover,
            policy_term=policy_term,
            due_date=due_date,
            premium_amount=premium_amount,
            sum_assured=sum_assured,
        )
        return HttpResponseRedirect(f'/user/{userid}')

def edit_term_insurance(request, pk):
    insurance = get_object_or_404(Term_Insurance, pk=pk)
    if request.method == 'POST':
        insurance.sno = request.POST.get('sno')
        insurance.policy_holder_name = request.POST.get('policy_holder_name')
        insurance.ploicy_no = request.POST.get('ploicy_no')
        insurance.date_of_commencement_of_risk = request.POST.get('date_of_commencement_of_risk')
        insurance.premium_payment_term = request.POST.get('premium_payment_term')
        insurance.premium_payment_mode = request.POST.get('premium_payment_mode')
        insurance.last_premium_date = request.POST.get('last_premium_date')
        insurance.critical_illness_beifit = request.POST.get('critical_illness_beifit')
        insurance.critical_illness_sumassured = request.POST.get('critical_illness_sumassured')
        insurance.accidental_death_benifit = request.POST.get('accidental_death_benifit')
        insurance.accdental_death_beifit_sum_assured = request.POST.get('accdental_death_beifit_sum_assured')
        insurance.return_of_premium = request.POST.get('return_of_premium')
        insurance.joint_life_cover = request.POST.get('joint_life_cover')
        insurance.policy_term = request.POST.get('policy_term')
        insurance.due_date = request.POST.get('due_date')
        insurance.premium_amount = request.POST.get('premium_amount')
        insurance.sum_assured = request.POST.get('sum_assured')
        insurance.save()
        return HttpResponseRedirect(f'/user/{insurance.customer.userid}')
    return render(request, 'user_home.html', {'insurance': insurance})

def delete_term_insurance(request, pk):
    insurance = get_object_or_404(Term_Insurance, pk=pk)
    insurance.delete()
    return HttpResponse('Term Insurance record deleted successfully')

# View to add a new health insurance record
def add_health_insurance(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        insurance_company = request.POST.get('insurance_company')
        employee_code = request.POST.get('employee_code')
        policy_number = request.POST.get('policy_number')
        validity_period_from = request.POST.get('validity_period_from')
        validity_period_to = request.POST.get('validity_period_to')
        benificiary_name = request.POST.get('benificiary_name')
        member_id = request.POST.get('member_id')
        dob = request.POST.get('dob')
        relation = request.POST.get('relation')
        family_sum_assured = request.POST.get('family_sum_assured')
        balance_sum_assured = request.POST.get('balance_sum_assured')

        customer = get_object_or_404(Customer, userid=userid)
        Health_Insurance.objects.create(
            customer=customer,
            sno=sno,
            insurance_company=insurance_company,
            employee_code=employee_code,
            policy_number=policy_number,
            validity_period_from=validity_period_from,
            validity_period_to=validity_period_to,
            benificiary_name=benificiary_name,
            member_id=member_id,
            dob=dob,
            relation=relation,
            family_sum_assured=family_sum_assured,
            balance_sum_assured=balance_sum_assured,
        )
        return HttpResponseRedirect(reverse('health-insurance-list'))

    return render(request, 'add_health_insurance.html')

# View to edit an existing health insurance record
def edit_health_insurance(request, pk):
    insurance = get_object_or_404(Health_Insurance, pk=pk)
    if request.method == 'POST':
        insurance.sno = request.POST.get('sno')
        insurance.insurance_company = request.POST.get('insurance_company')
        insurance.employee_code = request.POST.get('employee_code')
        insurance.policy_number = request.POST.get('policy_number')
        insurance.validity_period_from = request.POST.get('validity_period_from')
        insurance.validity_period_to = request.POST.get('validity_period_to')
        insurance.benificiary_name = request.POST.get('benificiary_name')
        insurance.member_id = request.POST.get('member_id')
        insurance.dob = request.POST.get('dob')
        insurance.relation = request.POST.get('relation')
        insurance.family_sum_assured = request.POST.get('family_sum_assured')
        insurance.balance_sum_assured = request.POST.get('balance_sum_assured')

        insurance.save()
        return HttpResponseRedirect(reverse('health-insurance-list'))

    return render(request, 'edit_health_insurance.html', {'insurance': insurance})

# View to delete a health insurance record
def delete_health_insurance(request, pk):
    insurance = get_object_or_404(Health_Insurance, pk=pk)
    insurance.delete()
    return HttpResponseRedirect(reverse('health-insurance-list'))



# View for saving Insurance data
def veh_insurance(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        policy_number=request.POST.get('policy_num')
        campany_name=request.POST.get('company_name')
        Name_of_insured=request.POST.get('name_of_insured')
        reg_no=request.POST.get('reg_no')
        engine_no=request.POST.get('eng_no')
        chasis_no=request.POST.get('chasis_no')
        RTA_location=request.POST.get('rta_loc')
        Vehiclemake_model=request.POST.get('vehicle_loc')
        Period_of_insurance_from=request.POST.get('from')
        Period_of_insurance_to=request.POST.get('to')
        Agent_no=request.POST.get('agent_no')
       
        # Retrieve the customer
        customer = get_object_or_404(Customer, userid=userid)

        # Create the insurance record
        Vehicle_Insurance.objects.create(
            customer=customer,
            sno=sno,
            policy_number=policy_number,
            campany_name=campany_name,
            Name_of_insured=Name_of_insured,
            reg_no=reg_no,
            engine_no=engine_no,
            chasis_no=chasis_no,
            RTA_location=RTA_location,
            Vehiclemake_model=Vehiclemake_model,
            Period_of_insurance_from=Period_of_insurance_from,
            Period_of_insurance_to=Period_of_insurance_to,
            Agent_no=Agent_no
        )
        # return HttpResponse('Insurance details saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

def edit_veh_insurance(request, pk):
    loan = Vehicle_Insurance.objects.get(pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        loan.sno = request.POST.get('sno')
        loan.policy_number=request.POST.get('policy_num')
        loan.campany_name=request.POST.get('company_name')
        loan.Name_of_insured=request.POST.get('name_of_insured')
        loan.reg_no=request.POST.get('reg_no')
        loan.engine_no=request.POST.get('eng_no')
        loan.chasis_no=request.POST.get('chasis_no')
        loan.RTA_location=request.POST.get('rta_loc')
        loan.Vehiclemake_model=request.POST.get('vehicle_loc')
        loan.Period_of_insurance_from=request.POST.get('from')
        loan.Period_of_insurance_to=request.POST.get('to')
        loan.Agent_no=request.POST.get('agent_no')
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'loan': loan})

def delete_veh_insurance(request, pk):
    loan = get_object_or_404(Vehicle_Insurance, pk=pk)
    loan.delete()
    return HttpResponse('Vehicle Insurance deleted successfully')

def add_life_insurance(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        policy_holder_name = request.POST.get('Policy_holder_name')
        policy_number = request.POST.get('Policy_number')
        company = request.POST.get('Company')
        starting_date = request.POST.get('starting_date')
        term = request.POST.get('term')
        premium = request.POST.get('premium')
        sum_assured = request.POST.get('sum_assured')
        nominee_name = request.POST.get('nominee_name')

        customer = get_object_or_404(Customer, userid=userid)
        Life_Insurance.objects.create(
            customer=customer,
            sno=sno,
            Policy_holder_name=policy_holder_name,
            Policy_number=policy_number,
            Company=company,
            starting_date=starting_date,
            term=term,
            premium=premium,
            sum_assured=sum_assured,
            nominee_name=nominee_name,
        )
        return HttpResponseRedirect(f'/user/{userid}')

def edit_life_insurance(request, pk):
    insurance = get_object_or_404(Life_Insurance, pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        insurance.sno = request.POST.get('sno')
        insurance.Policy_holder_name = request.POST.get('Policy_holder_name')
        insurance.Policy_number = request.POST.get('Policy_number')
        insurance.Company = request.POST.get('Company')
        insurance.starting_date = request.POST.get('starting_date')
        insurance.term = request.POST.get('term')
        insurance.premium = request.POST.get('premium')
        insurance.sum_assured = request.POST.get('sum_assured')
        insurance.nominee_name = request.POST.get('nominee_name')
        insurance.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'insurance': insurance})

def delete_life_insurance(request, pk):
    insurance = get_object_or_404(Life_Insurance, pk=pk)
    insurance.delete()
    return HttpResponse('Life Insurance record deleted successfully')

def insurance(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        company=request.POST.get('company')
        insurance_type = request.POST.get('insurance_type')
        policy_number = request.POST.get('policy_number')
        coverage_amount = request.POST.get('amount')
        
       
        # Retrieve the customer
        customer = get_object_or_404(Customer, userid=userid)

        # Create the insurance record
        # Insurance.objects.create(
        #     customer=customer,
        #     sno=sno,
        #     insurance_type=insurance_type,
        #     company=company,
        #     coverage_amount=coverage_amount,
        #     policy_number=policy_number
        # )
        # return HttpResponse('Insurance details saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

# View for saving Property data
def property(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')     
        type = request.POST.get('property_type')
        area = request.POST.get('area')
        address = request.POST.get('address')
        
        customer = Customer.objects.get(userid=userid)
        Property.objects.create(
            customer=customer,
            sno=sno,
            property_type=type,
            area=area,
            address=address
        )
        # return HttpResponse('Property details saved successfully')
    return HttpResponseRedirect(f'/user/{userid}')

# View for saving Investment data
def stock_investment(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        id = request.POST.get('usrid')
        demat=request.POST.get('demat')
        platform = request.POST.get('platform')
        company = request.POST.get('company')
        shares=request.POST.get('shares')
        buyprice = request.POST.get('buyprice')
        amount = request.POST.get('amount')
        date=request.POST.get('date')
        
        customer = Customer.objects.get(userid=userid)
        Stocks_Investment.objects.create(
            customer=customer,
            sno=sno,
            name=name,
            ursid=id,
            demat=demat,
            platform=platform,
            company=company,
            shares=shares,
            buyprice=buyprice,
            amount=amount,
            date=date
        )
    return HttpResponseRedirect(f'/user/{userid}')

def edit_stock_invest(request, pk):
    invs = Stocks_Investment.objects.get(pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        invs.sno = request.POST.get('sno')
        invs.name = request.POST.get('name')
        invs.ursid = request.POST.get('usrid')
        invs.demat=request.POST.get('demat')
        invs.platform = request.POST.get('platform')
        invs.company = request.POST.get('company')
        invs.shares=request.POST.get('shares')
        invs.buyprice = request.POST.get('buyprice')
        invs.amount = request.POST.get('amount')
        invs.date=request.POST.get('date')
        invs.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'invs': invs})

def del_stock_invest(request, pk):
    loan = get_object_or_404(Stocks_Investment, pk=pk)
    loan.delete()
    return HttpResponse('Stock Investment deleted successfully')

#Mutual Funds
def funds_investment(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        period=request.POST.get('period')
        fundplan = request.POST.get('fundplan')
        type = request.POST.get('type')
        platform=request.POST.get('platform')
        
        customer = Customer.objects.get(userid=userid)
        Mutual.objects.create(
            customer=customer,
            sno=sno,
            fund_name=name,
            invested_amount=amount,
            lock_in_period=period,
            fundplan=fundplan,
            type=type,
            platform=platform
        )
    return HttpResponseRedirect(f'/user/{userid}')

def edit_fund_invest(request, pk):
    invs = Mutual.objects.get(pk=pk)
    if request.method == 'POST':
        userid = request.POST.get('userid')
        invs.sno = request.POST.get('sno')
        invs.name = request.POST.get('name')
        invs.amount = request.POST.get('amount')
        invs.period=request.POST.get('period')
        invs.fundplan = request.POST.get('fundplan')
        invs.type = request.POST.get('type')
        invs.platform=request.POST.get('platform')
        invs.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'invs': invs})

def del_fund_invest(request, pk):
    loan = get_object_or_404(Mutual, pk=pk)
    loan.delete()
    return HttpResponse('Mutual Investment deleted successfully')

def schemes(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        type = request.POST.get('type')
        name=request.POST.get('name')
        holder_name=request.POST.get('holder_name')
        number=request.POST.get('number')
        amount = request.POST.get('amount')
        term=request.POST.get('term')
        start_date = request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        maturity=request.POST.get('maturity')
        
        customer = Customer.objects.get(userid=userid)
        Schemes.objects.create(
            customer=customer,
            sno=sno,
            type=type,
            name=name,
            holder_name=holder_name,
            number=number,
            amount=amount,
            term=term,
            start_date=start_date,
            end_date=end_date,
            maturity_date=maturity
        )
    return HttpResponseRedirect(f'/user/{userid}')

def card(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        type=request.POST.get('type')
        name=request.POST.get('name')
        card_no=request.POST.get('card_no')
        
        customer = Customer.objects.get(userid=userid)
        Card.objects.create(
            customer=customer,
            sno=sno,
            type=type,
            name=name,
            card_num=card_no
        )
    return HttpResponseRedirect(f'/user/{userid}')





# Editings
# Edit Family Member View
def edit_family(request, member_id):
    member = get_object_or_404(FamilyMember, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.name = request.POST.get('name')
        member.age = request.POST.get('age')
        member.gender = request.POST.get('gender')
        member.relationship = request.POST.get('relationship')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_family(request, member_id):
    member = get_object_or_404(FamilyMember, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')

def edit_bank(request, member_id):
    member = get_object_or_404(BankAccount, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.bank_name = request.POST.get('bank_name')
        member.bank_address = request.POST.get('bank_address')
        member.account=request.POST.get('num')
        member.ifsc=request.POST.get('ifsc')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_bank(request, member_id):
    member = get_object_or_404(BankAccount, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')

def edit_credit(request, member_id):
    member = get_object_or_404(Credit, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.name = request.POST.get('name')
        member.address = request.POST.get('address')
        member.amount=request.POST.get('amount')
        member.date=request.POST.get('date')
        member.mode=request.POST.get('mode')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_credit(request, member_id):
    member = get_object_or_404(Credit, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')

def edit_debit(request, member_id):
    member = get_object_or_404(Debit, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.name = request.POST.get('name')
        member.address = request.POST.get('address')
        member.amount=request.POST.get('amount')
        member.date=request.POST.get('date')
        member.mode=request.POST.get('mode')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_debit(request, member_id):
    member = get_object_or_404(Debit, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')


# def edit_insurance(request, member_id):
#     member = get_object_or_404(Insurance, id=member_id)
#     if request.method == "POST":
#         userid = request.POST.get('userid')
#         member.sno = request.POST.get('sno')
#         member.company=request.POST.get('company')
#         member.insurance_type = request.POST.get('insurance_type')
#         member.policy_number = request.POST.get('policy_number')
#         member.coverage_amount = request.POST.get('coverage_amount')
#         member.save()
#         return HttpResponseRedirect(f'/user/{userid}')
#     return render(request, 'user_home.html', {'member': member})

# def delete_insurance(request, member_id):
#     member = get_object_or_404(Insurance, id=member_id)
#     member.delete()
#     # Redirect using named URL
#     return HttpResponse('Deleted Successful')

def edit_property(request, member_id):
    member = get_object_or_404(Property, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.type = request.POST.get('property_type')
        member.area = request.POST.get('area')
        member.address = request.POST.get('address')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_property(request, member_id):
    member = get_object_or_404(Property, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')

def edit_schemes(request, member_id):
    member = get_object_or_404(Schemes, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.type = request.POST.get('investment_type')
        member.name=request.POST.get('name')
        member.amount = request.POST.get('amount')
        member.start_date = request.POST.get('start_date')
        member.end_date=request.POST.get('end_date')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_schemes(request, member_id):
    member = get_object_or_404(Schemes, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')

def edit_card(request, member_id):
    member = get_object_or_404(Card, id=member_id)
    if request.method == "POST":
        userid = request.POST.get('userid')
        member.sno = request.POST.get('sno')
        member.type = request.POST.get('type')
        member.name=request.POST.get('name')
        member.card_num=request.POST.get('card_no')
        member.save()
        return HttpResponseRedirect(f'/user/{userid}')
    return render(request, 'user_home.html', {'member': member})

def delete_card(request, member_id):
    member = get_object_or_404(Card, id=member_id)
    member.delete()
    # Redirect using named URL
    return HttpResponse('Deleted Successful')


def pricing(request):
    return render(request,'pricing.html')

def documents(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        doc = request.FILES.get('doc')

        print("userid:", userid)
        print("sno:", sno)
        print("name:", name)
        print("doc:", doc)

        if doc:  # Ensure the file is not None before creating the record
            customer = Customer.objects.get(userid=userid)
            Documents.objects.create(
                customer=customer,
                sno=sno,
                doc_name=name,
                doc=doc
            )
        else:
            print("No file found in the request.")
            return HttpResponse("No file uploaded.", status=400)
    return HttpResponseRedirect(f'/user/{userid}')


def add_pf(request):
    if request.method == 'POST':
        customer = request.POST['customer']  # Ensure customer ID is passed correctly
        sno = request.POST['sno']
        UAN_no = request.POST['UAN_no']
        PF_number_or_Number_ID = request.POST['PF_number_or_Number_ID']
        upload_UAN_card = request.FILES['upload_UAN_card']
        
        pf_record = PF(customer_id=customer, sno=sno, UAN_no=UAN_no,
                       PF_number_or_Number_ID=PF_number_or_Number_ID,
                       upload_UAN_card=upload_UAN_card)
        pf_record.save()
        return redirect('list-pf')

    return render(request, 'add_pf.html')

def edit_pf(request, id):
    pf_instance = get_object_or_404(PF, id=id)
    
    if request.method == 'POST':
        pf_instance.customer_id = request.POST['customer']  # Ensure customer ID is passed correctly
        pf_instance.sno = request.POST['sno']
        pf_instance.UAN_no = request.POST['UAN_no']
        pf_instance.PF_number_or_Number_ID = request.POST['PF_number_or_Number_ID']
        
        if 'upload_UAN_card' in request.FILES:
            pf_instance.upload_UAN_card = request.FILES['upload_UAN_card']
        
        pf_instance.save()
        return redirect('list-pf')

    return render(request, 'edit_pf.html', {'pf_instance': pf_instance})

def delete_pf(request, id):
    pf_instance = get_object_or_404(PF, id=id)
    if request.method == 'POST':
        pf_instance.delete()
        return redirect('list-pf')
    return render(request, 'delete_pf.html', {'pf_instance': pf_instance})