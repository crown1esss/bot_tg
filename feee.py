import json
def give_info():
    with open('data/monday_nechet.json' , 'w') as file:
        monday_nechet = {
            '1':'Управление проектами информатизации  12-40 : 14:20   Аудитория -  А-422',
            '2': 'Системы управления данными  14-20 : 15-50   Аудитория -  Г-413'

        }
        json.dump(monday_nechet, file, indent=4, ensure_ascii=False)

    with open('data/monday_chet.json', 'w') as file:
        monday_chet = {

            '1': 'Управление проектами информатизации  10-40 : 12:10   Аудитория -  А-422',
            '2':'Управление проектами информатизации  12-40 : 14:20   Аудитория -  А-422',
            '3': 'Системы управления данными  14-20 : 15-50   Аудитория -  Г-413'
        }


        json.dump(monday_chet, file, indent=4 , ensure_ascii=False)
    with open('data/tuesday_nechet.json', 'w') as file:
            tuesday_nechet = {
                '1': 'Информационная безопасность   9-00 : 10-30   Аудитория -  А-422',
                '2': 'Контроллинг  10-40 : 12-10  Аудитория -  А-418',
                '3': 'Контроллинг 12-40 : 14-10   Аудитория -  A-418'
            }
            json.dump(tuesday_nechet, file, indent=4, ensure_ascii=False)
    with open('data/tuesday_chet.json', 'w') as file:
            tuesday_chet = {

                '1': 'Управление проектами информатизации  10-40 : 12:10   Аудитория -  А-422',
                '2': 'Экономика предприятия  12-40 : 14-10   Аудитория -  А-220'
            }


            json.dump(tuesday_chet, file, indent=4, ensure_ascii=False)
    with open('data/wednesday_nechet.json', 'w') as file:
            wednesday_nechet = {
                '0':'ДистанционОЧКА'
            }
            json.dump(wednesday_nechet, file, indent=4, ensure_ascii=False)

    with open('data/wednesday_chet.json', 'w') as file:
            wednesday_chet = {

                '0':'ДистанционОЧКА'
            }

            json.dump(wednesday_chet, file, indent=4, ensure_ascii=False)
    with open('data/thursday_nechet.json', 'w') as file:
            thursday_nechet = {
                '0':'Выходной'
            }
            json.dump(thursday_nechet, file, indent=4, ensure_ascii=False)
    with open('data/thursday_chet.json', 'w') as file:
            thursday_chet = {

                '0':'Выходной'
            }


            json.dump(thursday_chet, file, indent=4, ensure_ascii=False)

    with open('data/friday_nechet.json', 'w') as file:
            friday_nechet = {
                '0':'Типо практика'
            }
            json.dump(friday_nechet, file, indent=4, ensure_ascii=False)
    with open('data/friday_chet.json', 'w') as file:
            friday_chet = {

                '0':'Типо практика'
            }


            json.dump(friday_chet, file, indent=4, ensure_ascii=False)
    with open('data/saturday_nechet.json', 'w') as file:
            saturday_nechet = {
                '1': 'Мат моделирование прикладных задач   12-40 : 14-10   Аудитория -  А-314',
                '2': 'Мат моделирование прикладных задач  14-20 : 15-50  Аудитория -  А-314',
                '3': 'Методы анализа данных 16-20 : 17-50   Аудитория -  Г-427',
                '4': 'Методы анализа данных  18-00 : 19-30   Аудитория -  Г-427'

            }
            json.dump(saturday_nechet, file, indent=4, ensure_ascii=False)
    with open('data/saturday_chet.json', 'w') as file:
            saturday_chet = {

                '1': 'Мат моделирование прикладных задач  12-40 : 14-10   Аудитория -  А-314',
                '2': 'Методы анализа данных 16-20 : 17-50   Аудитория -  Г-427',
                '3': 'Методы анализа данных  18-00 : 19-30   Аудитория -  Г-427'
            }

            json.dump(saturday_chet, file, indent=4, ensure_ascii=False)
give_info()