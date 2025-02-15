# comments/forms.py
from django import forms
from .models import GuestFeedback

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = GuestFeedback
        fields = '__all__'
        widgets = {
            'date_of_stay': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'additional_comments': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'exceptional_employee': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            # Personal Information
            'name': 'Your Full Name',
            'contact_no': 'Contact Number',
            'email': 'Email Address',
            'date_of_stay': 'Date of Your Stay',
            
            # First Impression
            'welcome_rating': 'Your Welcome on Arrival',
            'reception_rating': 'Reception Experience',
            'hotel_cleanliness': 'Hotel Cleanliness & Tidiness',
            
            # Room Experience
            'room_cleanliness': 'Room Cleanliness',
            'amenities_rating': 'Room Amenities Quality',
            'room_service': 'Room Service Efficiency',
            'housekeeping': 'Housekeeping Service Quality',
            
            # Restaurant/Bar
            'restaurant_ambience': 'Restaurant/Bar Ambience',
            'waiting_team': 'Waiting Team Service',
            'complaint_response': 'Complaint Handling',
            'food_presentation': 'Food Presentation & Taste',
            'restaurant_setup': 'Restaurant Facilities',
            'toilet_cleanliness': 'Restroom Cleanliness',
            
            # Ordering Food
            'staff_recommendation': 'Staff Recommendations Quality',
            'waiting_time': 'Order Waiting Time',
            'food_temperature': 'Food Serving Temperature',
            'value_money': 'Value for Money',
            'portion_size': 'Portion Size Satisfaction',
            
            # Additional Fields
            'additional_comments': 'Your Additional Comments',
            'exceptional_employee': 'Exceptional Staff Member (if any)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field], forms.IntegerField):
                self.fields[field].widget = forms.RadioSelect(
                    choices=RATING_CHOICES,
                    attrs={'class': 'form-check-input'}
                )
                # Add help text for rating fields
                self.fields[field].help_text = "1 = Poor, 5 = Excellent"
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})