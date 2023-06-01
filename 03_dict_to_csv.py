import csv

def main():
    persons = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Дмитрий', 'age': 36, 'job': 'Musician'},
    ]
    with open('person_list.csv', 'w', encoding='utf-8', newline='') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for person in persons:
            writer.writerow(person)

if __name__ == "__main__":
    main()
