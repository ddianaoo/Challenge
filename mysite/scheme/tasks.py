
import csv
from faker import Faker
from .models import Scheme
import datetime
import os
from os import path
from pathlib import Path
from time import sleep
from django.core.files.base import ContentFile


def datagenerate(records, columns, names, filename, scheme_id):
    scheme = Scheme.objects.get(id=scheme_id)
    scheme.upload = 'In Progress'
    scheme.save()

    fake = Faker('en_US')
    filename_ = filename
    with open(filename_, 'w') as csvFile:
        print(True)
        writer = csv.writer(csvFile)
        if names:
            writer.writerow(names)

        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()

        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@test.com"
            userId = Fname + "." + Lname + domain_name

            gen_dict = {
                    "Email": userId,
                    "Full Name": full_name,
                    'Job': fake.job(),
                    'Company': fake.company(),
                    'Text': fake.word(),
                    'Integer': fake.pyint(max_value=100),
                    }

            filtered_dict = {}
            for (k, v) in gen_dict.items():
                if k in columns:
                    filtered_dict[k] = v
            writer.writerow(filtered_dict)

        scheme.upload = 'media/' + filename_
        scheme.save()

    return filename
