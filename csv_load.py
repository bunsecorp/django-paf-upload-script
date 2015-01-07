import csv, sys, os, datetime
your_djangoproject_home="~/django-software/website/"
csv_filepathname="~/paf/CSV PAF.csv"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

from ratedtenant.models import PostalAddress

with open(csv_filepathname, 'rb') as f:
    reader = csv.reader(f)
    itr = 0
    try:
        for row in reader:
            addr = PostalAddress(postcode=row[0].decode("latin-1"), posttown=row[1].decode("latin-1"), dependent_locality=row[2].decode("latin-1"), double_dependent_locality=row[3].decode("latin-1"), throughfare_and_descriptor=row[4].decode("latin-1"), dependent_throughfare_and_descriptor=row[5].decode("latin-1"), building_number=row[6].decode("latin-1"), building_name=row[7].decode("latin-1"), subbuilding_name=row[8].decode("latin-1"), po_box=row[9].decode("latin-1"), department_name=row[10].decode("latin-1"), organisation_name=row[11].decode("latin-1"), udprn_key=row[12].decode("latin-1"), postcode_type=row[13].decode("latin-1"), su_organisation_indicator=row[14].decode("latin-1"), delivery_point_suffix=row[15].decode("latin-1")) 
            addr.save()
            itr += 1
            print itr 
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
print datetime.datetime.now().strftime('%c')

