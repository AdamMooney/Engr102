import csv


class Participant:
    def __init__(self, age, industry, salary, currency, country, experience, education):
        # self.x = x
        self.age = age
        self.industry = industry
        self.salary = salary
        self.currency = currency
        self.country = country
        self.experience = experience
        self.education = education


class AverageSalary:
    def __init__(self, key, average, participant_count):
        self.key = key
        self.average = average
        self.participant_count = participant_count

        

def main():

    rows = load_csv_file("survey.csv")
    participants = create_participants(rows)

    print("Answer #1:", len(participants))

    industry_groups = group_by_attribute(participants, "industry")

    average_salaries_by_industry = get_average_salary(industry_groups)
     
    filtered_average_salary_by_industry = get_average_salary(industry_groups)

    filtered_average_salary_by_industry = []
    
    for group in average_salaries_by_industry:
        if group.participant_count >= 10:
            filtered_average_salary_by_industry.append(group)

    sorted_filtered_average_salary_by_industry = sorted(filtered_average_salary_by_industry, key = lambda x: x.average, reverse=True)

    top_5_industries = []
    for entry in sorted_filtered_average_salary_by_industry:
        top_5_industries.append(entry.key)
    print("Answer #2:", top_5_industries)


    age_groups = group_by_attribute(participants, "age")
    average_salaries_by_age = get_average_salary(age_groups)

    for group in average_salaries_by_age:
        print(group.key, group.average)
    

    education_level = group_by_attribute(participants, "Education")
    Education_level_by_participant = get_education(education_level)

    for group in Education_level_by_participant:
        print(group.key, group.education)
    


    return






def get_average_salary(groups_list):

    average_salaries = []
    for key, group in groups_list.items():
        avg = int(sum([x.salary for x in group]) / len(group))
        
        average_salaries.append(AverageSalary(key, avg, len(group)))

    return average_salaries

def group_by_attribute(objects, property):

    
    groups = {}
    
    
    for obj in objects:
        value = getattr(obj, property)
        if value in groups:
            groups[value].append(obj)
        else:
            groups[value] = [obj]

    return groups




def create_participants(rows):


    participants = []

    for row in rows[1:]:
        age = row[1]
        industry = row[2]
        salary = int(row[5].replace(",",""))
        currency = row[7]
        country = row[10]
        experience = row[13]
        education = row[15]
        
        if currency == "USD":
            participants.append(Participant(age, industry, salary, currency, country, experience, education))

    return participants



def load_csv_file(filename):
    
    rows = []
    with open(filename, "r", encoding='iso-8859-1') as f:
        reader_obj = csv.reader(f)

        for row in reader_obj:
            rows.append(row)

    return rows

if __name__ == "__main__":
    main()