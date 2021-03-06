# -*- coding: utf-8 -*-
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

from __future__ import unicode_literals

from django.db import models, migrations

def migrate_updater(apps, schema_editor):
    StreamtipEvent = apps.get_model("streamtip", "StreamtipEvent")
    UpdaterEvent = apps.get_model("main", "UpdaterEvent")
    for event in StreamtipEvent.objects.all():
        try:
            ue = UpdaterEvent.objects.get(pk=event.updaterevent_ptr_id)
            ue.base_updater = event.updater.updater_ptr
            ue.save()
        except Exception:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_updaterevent_base_updater'),
        ('streamtip', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_updater)
    ]
