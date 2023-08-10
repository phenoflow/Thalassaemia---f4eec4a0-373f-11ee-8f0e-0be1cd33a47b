# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"D104.00","system":"readv2"},{"code":"D104200","system":"readv2"},{"code":"D104211","system":"readv2"},{"code":"D104600","system":"readv2"},{"code":"D104811","system":"readv2"},{"code":"D104900","system":"readv2"},{"code":"D104A00","system":"readv2"},{"code":"D104z00","system":"readv2"},{"code":"Dyu1100","system":"readv2"},{"code":"105439.0","system":"med"},{"code":"1171.0","system":"med"},{"code":"21643.0","system":"med"},{"code":"31075.0","system":"med"},{"code":"31405.0","system":"med"},{"code":"32943.0","system":"med"},{"code":"37808.0","system":"med"},{"code":"45151.0","system":"med"},{"code":"4666.0","system":"med"},{"code":"46733.0","system":"med"},{"code":"54429.0","system":"med"},{"code":"57144.0","system":"med"},{"code":"66137.0","system":"med"},{"code":"71992.0","system":"med"},{"code":"73946.0","system":"med"},{"code":"8866.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('thalassaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thalassaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thalassaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thalassaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
