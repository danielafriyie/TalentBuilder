from django import forms

careers = {
    '': '',
    'accounts_assistant': 'Accounts Assistant',
    'administrator': 'Administrator',
    'junior_administrator': 'Junior Administrator',
    'investment_manager': 'Investment Manager',
    'banking_fixed_income': 'Banking-Fixed Income',
    'banking_compliance': 'Banking-Compliance',
    'book_keeper': 'Book Keeper',
    'business_analyst': 'Business Analyst',
    'business_development_manager': 'Business Development Manager',
    'communication_manager': 'Communication Manager',
    'compliance_quality_manager': 'Compliance-Quality Manager',
    'plant_&_service_manager': 'Plant and Service Manager',
    'project_manager': 'Project Manager',
    'customer_service': 'Customer Service',
    'digital_marketer': 'Digital Marketer',
    'e_commerce': 'E-Commerce',
    'engineer': 'Engineer',
    'estate_manager': 'Estate Manager',
    'event_manager': 'Event Manager',
    'executive_assistant': 'Executive Assistant',
    'finance_analyst': 'Finance Analyst',
    'finance_director': 'Finance Director',
    'financial_advisor': 'Financial Advisor',
    'risk_management': 'Risk Management',
    'grants_manager': 'Grants Manager',
    'head_teacher': 'Head Teacher',
    'teacher': 'Teacher',
    'health_&_safety_advisor': 'Health and Safety Advisor',
    'hotel_manager': 'Hotel Manager',
    'human_resource_manager': 'Human Resource Manager',
    'it_architect_consultant': 'IT Architect-Consultant',
    'it_director': 'IT Director',
    'program_manager': 'Program Manager',
    'software_developer': 'Software Developer',
    'help_desk_support': 'Help-Desk Support',
    'project_coordinator': 'Project Coordinator',
    'lawyer_intellectual_property': 'Lawyer Intellectual Property',
    'management_consultant': 'Management Consultant',
    'managing_director': 'Managing Director',
    'marketing_manager': 'Marketing Manager',
    'nurse': 'Nurse',
    'operations_&_project_manager': 'Operations and Project Manager',
    'operations_coordinator': 'Operations Coordinator',
    'receptionist': 'Receptionist',
    'secretary': 'Secretary',
    'social_services': 'Social Services',
    'procurement': 'Procurement',
    'product_manager': 'Product Manager',
    'property_management': 'Property Management',
    'sales_executive': 'Sales Executive',
    'sales_consultant': 'Sales Consultant',
    'senior_banker': 'Senior Banker',
    'account_manager': 'Account Manager',
    'social_media_manager': 'Social Media Manager',
    'social_care_worker': 'Social Care Worker',
    'tutor_or_trainee': 'Tutor / Trainee',
    'warehouse_supervisor': 'Warehouse Supervisor',
    'web_developer': 'Web Developer',
    'data_analyst': 'Data Analyst',
    'architect': 'Architect',
    'z_general_cv': 'General CV'
}


class UploadCVForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=True)
    cv_format = forms.ChoiceField(choices=[('', ''), ('modern_cv', 'Modern CV'), ('traditional_cv', 'Traditional CV')],
                                  required=True)
    career_type = forms.ChoiceField(choices=[(x, y) for x, y in sorted(careers.items())],
                                    required=True)
    cv_upload = forms.FileField(required=True)
    agree_to_terms = forms.BooleanField(required=True)

    # styling form widgets
    name.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your name'})
    email.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your email'})
    phone.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your phone number'})
    cv_format.widget.attrs.update({'class': 'form-control form-control-lg'})
    career_type.widget.attrs.update({'class': 'form-control form-control-lg'})
    cv_upload.widget.attrs.update({'class': 'form-control form-control-lg'})
