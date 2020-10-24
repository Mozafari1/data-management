import shutil

infile = "1.log"
outfile = "2.log"
original = r'2.log'
target = r'1.log'

delete_list = ["}{"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "\n")
        fout.write(line)
shutil.copyfile(original, target)

delete_list = ["{'ip': ", "'asn': {'asn':", "'name':", "'domain':", "'route':", "'type':", "}", "'calling_code':", "'city':", "'continent_code':", "'continent_name':", "'country_code':", "'country_name':", "'is_eu':",
               "'latitude':", "'longitude':", "'postal':", "'region':", "'region_code':", "'threat': {'is_tor':", "'is_proxy':", "'is_anonymous':", "'is_known_attacker':", "'is_known_abuser':", "'is_threat':", "'is_bogon':", "'status':", "'ip': ", "'", '"', "No.31,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
shutil.copyfile(original, target)


# if asn:None
delete_list = ["asn: None"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "None, None, None, None, None")
        fout.write(line)
shutil.copyfile(original, target)


delete_list = ["No.31,", ", Ltd.", ", LLC", "IDC,",
               ", Inc.", ", S.A.", "Kejizhongyi Avenue,", ", S.", ", d.o.o.", ", Sociedad Anonima.", ",Inc", ".,Ltd", ", LTD", ", CAT", "Co., Ltd", "C. por A. - CODETEL,", ",Internet Service Provider"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
shutil.copyfile(original, target)
# replace l Ltd., T
delete_list = ["l Ltd., T"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "l T")
        fout.write(line)
shutil.copyfile(original, target)
# CANTV Servicios, Venezuela,
delete_list = ["CANTV Servicios, Venezuela"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "CANTV Servicios Venezuela")
        fout.write(line)
shutil.copyfile(original, target)

# RailTel Corporation of India Ltd., Internet Service Provider,
delete_list = [
    "RailTel Corporation of India Ltd., New Delhi,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "RailTel Corporation of India Ltd New Delhi")
        fout.write(line)
shutil.copyfile(original, target)

# # PERN AS Content Servie Provider, Islamabad, Pakistan,
delete_list = [
    "PERN AS Content Servie Provider, Islamabad, Pakistan"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "PERN AS Content Servie Provider Islamabad Pakistan")
        fout.write(line)
shutil.copyfile(original, target)

delete_list = [
    "Axtel,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Axtel")
        fout.write(line)
shutil.copyfile(original, target)
# O2 Czech Republic, a.s.,
delete_list = [
    "O2 Czech Republic, a.s.,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "O2 Czech Republic a.s.,")
        fout.write(line)
shutil.copyfile(original, target)
# Charter Communications, Inc,
delete_list = [
    "Charter Communications, Inc,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Charter Communications Inc,")
        fout.write(line)
shutil.copyfile(original, target)
# RailTel Corporation of India Ltd., Internet Service Provider, New Delhi,
delete_list = [
    "RailTel Corporation of India Ltd., Internet Service Provider, New Delhi,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "RailTel Corporation of India Ltd New Delhi,")
        fout.write(line)
shutil.copyfile(original, target)

delete_list = [
    "TM Net, Internet Service Provider,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "TM Net Internet Service Provider,")
        fout.write(line)
shutil.copyfile(original, target)
# JSC Zap-Sib TransTeleCom, Novosibirsk
delete_list = [
    "JSC Zap-Sib TransTeleCom, Novosibirsk"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "JSC Zap-Sib TransTeleCom Novosibirsk")
        fout.write(line)
shutil.copyfile(original, target)
# #Telia Lietuva, AB,
delete_list = [
    "Telia Lietuva, AB,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Telia Lietuva AB,")
        fout.write(line)
shutil.copyfile(original, target)
# Royal Green Online Ltd. Internet Service Provider, Dhaka,
delete_list = [
    "Royal Green Online Ltd. Internet Service Provider, Dhaka,,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Royal Green Online Ltd. Internet Service Provider Dhaka,")
        fout.write(line)
shutil.copyfile(original, target)

delete_list = [
    "No.293,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "No.293 ")
        fout.write(line)
shutil.copyfile(original, target)

# TELEFONICA VENEZOLANA, C.A.,
delete_list = [
    "TELEFONICA VENEZOLANA, C.A.,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "TELEFONICA VENEZOLANA C.A., ")
        fout.write(line)
shutil.copyfile(original, target)
#  DataShack, LC,
delete_list = [
    "DataShack, LC,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "DataShack LC,")
        fout.write(line)
shutil.copyfile(original, target)
#  Bell Teleservices India Pvt Ltd., ISP having own OFC network in Bangalore, India.,
delete_list = [
    "Bell Teleservices India Pvt Ltd., ISP having own OFC network in Bangalore, India.,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Bell Teleservices India Pvt Ltd. ISP having own OFC network in Bangalore India,")
        fout.write(line)
shutil.copyfile(original, target)
# MetroNet Bangladesh Limited, Fiber Optic Based  Metropolitan Data,
delete_list = [
    "MetroNet Bangladesh Limited, Fiber Optic Based  Metropolitan Data,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "MetroNet Bangladesh Limited Fiber Optic Based  Metropolitan Data,")
        fout.write(line)
shutil.copyfile(original, target)
#Interserver, Inc,
delete_list = [
    "Interserver, Inc,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Interserver Inc,")
        fout.write(line)
shutil.copyfile(original, target)
# Capitalonline Data Service Co.,LTD,
delete_list = [
    "Capitalonline Data Service Co.,LTD,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Capitalonline Data Service Co.LTD,")
        fout.write(line)
shutil.copyfile(original, target)

# Communication, Communications, Informatics Ltd.,
delete_list = [
    "Communication, Communications, Informatics Ltd.,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "Communication Communications Informatics Ltd.,")
        fout.write(line)
shutil.copyfile(original, target)
# ELIMNET, INC.,
delete_list = [
    "ELIMNET, INC.,"]
with open(infile, encoding="utf-8") as fin, open(outfile, "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(
                word, "ELIMNET INC.,")
        fout.write(line)
shutil.copyfile(original, target)
