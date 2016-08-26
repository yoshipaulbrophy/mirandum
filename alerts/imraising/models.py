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

from django.db import models
import main.models
import json
import iso8601

class ImraisingUpdate(main.models.Updater):
    api_key = models.CharField(max_length=255)

class ImraisingEvent(main.models.UpdaterEvent):
    details = models.TextField()
    updater = models.ForeignKey(ImraisingUpdate)
    
    def as_dict(self):
        details = json.loads(self.details)

        datetime = iso8601.parse_date(details['time'])    
        info = {
            'name': details['nickname'],
            'comment': details['message'],
            'donation_amount': float(details['amount']['display']['total']),
            'currency': details['amount']['display']['currency'],
            'amount': " ".join([str(details['amount']['display']['total']), details['amount']['display']['currency']]),
            'timestamp': datetime,
        }
        return info

class ImraisingAlertConfig(main.models.AlertConfig):
    blacklist = models.TextField(blank=True, null=True)
    filter_type = models.CharField(max_length=20, choices=(
        ('1equal', 'Equals'),
        ('2gt', 'Greater than'),
        ('3default', 'Default'),
    ), default='3default', help_text="When filtering for specific amounts, comparison to use.")
    filter_amount = models.FloatField(blank=True, null=True)
    text_to_speech = models.BooleanField(default=False)
