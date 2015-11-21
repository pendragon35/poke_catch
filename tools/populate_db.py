import csv
import django
import sys

from pcatch.pcalc.models import Rates

NUM_POS = 0
NAME_POS = 1
CATCH_POS = 2
DP = 0
BW = 1
XY = 2
VALID_TABLES = ["tables/table_dp.csv", "tables/table_bw.csv", "tables/table_xy.csv"]

django.setup()


def print_usage():
    print "python populate_db.py -f table_??.csv"


if (len(sys.argv) < 3 or sys.argv[1] != "-f" or sys.argv[2] not in VALID_TABLES):
    print_usage()
    sys.exit()

fname = sys.argv[2]

try:
    with open(fname) as table:
        reader = csv.reader(table)
        for row in reader:
            if (len(row) != 3):
                continue
            poke_num_in = int(row[NUM_POS])
            catch_rate = int(row[CATCH_POS])

            try:  # key already exists
                p = Rates.objects.get(poke_num=poke_num_in)
                # print "use old"
            except Rates.DoesNotExist:
                p = Rates(poke_num=poke_num_in, poke_name=row[NAME_POS])
                # print "made new"

            if (fname == VALID_TABLES[DP]):
                p.dp_rate = catch_rate
            elif (fname == VALID_TABLES[BW]):
                p.bw_rate = catch_rate
            elif (fname == VALID_TABLES[XY]):
                p.xy_rate = catch_rate

            p.save()
            # print "saved"

except IOError:
    print "file does not exist"
    sys.exit()
