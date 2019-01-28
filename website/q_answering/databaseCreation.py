import csv
import sys


csv.field_size_limit(sys.maxsize)


def get_oq_list(csvfile):
    oq_list = []
    with open(csvfile, 'r') as f:
        freader = csv.reader(f, delimiter='\n')
        for row in freader:
            oq_info = row[0].split('|')
            oq_dict = {
                "rownr": oq_info[0],
                "date": oq_info[1],
                "filename": oq_info[2],
                "id": oq_info[3],
                "text": oq_info[4],
            }
            oq_list.append(oq_dict)

    return oq_list


def get_art_list(csvfile):
    art_list = []
    with open(csvfile, 'r') as f:
        freader = csv.reader(f, delimiter='\n')
        for row in freader:
            art_info = row[0].split('|')
            art_dict = {
                "rownr": art_info[0],
                "id": art_info[1],
                "journalcode": art_info[2],
                "date": art_info[3],
                "text": art_info[4],
                "title": art_info[5],
            }
            art_list.append(art_dict)

    return art_list


"""
def create_oq_DB(oq_list):
    for info_dict in oq_list:
        article = OldQuestion(question_id=info_dict["id"],
                              date=info_dict["date"],
                              filename=info_dict["filename"],
                              text=info_dict["text"],
                              )
        article.save()
"""
