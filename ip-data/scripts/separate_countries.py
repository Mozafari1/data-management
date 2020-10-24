import csv
import time
search_data = []
found_data = []
country_name = []
Path_file = '../fixed_data/'
path_1 = Path_file+'countries/'
col_number = 17

x = 'Kuwait'

data_in = x
input_file_name = x


def read_csv_file():

    with open(Path_file+'fixed_data.csv', "r", encoding="utf-8", newline='') as rfile:
        read_data = csv.reader(rfile)
        for row in read_data:
            search_data.append(row)


def search_in_data():
    col = [i[col_number] for i in search_data]
    if data_in in col:
        for i in range(0, len(search_data)):
            if data_in == search_data[i][col_number]:
                found_data.append(search_data[i])
    else:
        pass


def write_to_csv_file():
    with open(path_1+input_file_name+'.csv', "w+", encoding="utf-8", newline='') as wfile:
        writer = csv.writer(wfile)
        writer.writerows(found_data)


if __name__ == "__main__":
    read_csv_file()
    search_in_data()
    write_to_csv_file()

    # date = col[0]
    # action[1]
    # server_port[2]
    # message[3]
    # ssh[4]
    # perform[5]
    # ip[6]
    # asn[7]
    # network_provider[8]
    # domain [9]
    # route{10]
    # type [11]
    # calling_code [12]
    # city[13]
    # continent_code[14]
    # continent[15]
    # country_code[16]
    # country 17
    # is_eu 18
    # latitude 19
    # longitude 20
    # postal 21
    # region 22
    # region_code 23
    # is_tor 24
    # is_proxy 25
    # is_anonymous  26
    # is_known_attacker 27
    # is_known_abuser 28
    # is_threat 29
    # is_bogon 30
    # status 31
