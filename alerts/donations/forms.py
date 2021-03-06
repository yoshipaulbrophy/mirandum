#  Copyright 2016 Google Inc. All Rights Reserved.
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License. 
import django.forms as forms
from donations.models import TopList, Goal
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class TopForm(forms.ModelForm):
    class Meta:
        model = TopList
        fields = ['format', 'count', 'seperator', 'type', 'days', 'font', 'font_size', 'font_color', 'font_effect', 'font_weight', 'outline_color']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['start_date', 'end_date', 'amount', 'description', 'source_type']
    start_date = DateField(widget=AdminDateWidget())
    end_date   = DateField(widget=AdminDateWidget(), required=False)
