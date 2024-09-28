import add_error

DEFAULT_POSITION = ["Нападающий", "Полузащитник", "Защитник", "Вратарь"]
DEFAULT_TEAM = ["Pro (11x11)", "8х8"]
DEFAULT_Y = ["Y", "y", "L", "l", "Н", "н", "Д", "д"]


def start():
    full_name = input("Введите ФИО игрока: ")
    number = input("Номер: ")
    position = input("Позиция: ")
    birthday = input("День рождения (01.01.2000): ")
    team = input("Команда: ")
    date = input("Дата принятия игрока (Январь, 2000): ")
    height = input("Рост: ")
    weight = input("Вес: ")

    
    name = ""
    surname = ""
    patronymic = ""

    if len(full_name.split(" ")) == 2:
        q = input("Игрок без отчетства?")
        for i in DEFAULT_Y:
            if q == i:
                name_split = split_name(full_name, False)
            elif i == "д":
                return
    
    elif len(full_name.split(" ")) == 3:
        name_split = split_name(full_name)
    name = name_split[0]
    surname = name_split[1]    
    try:
        patronymic = name_split[2]
    except:
        patronymic = ""

    result = create_player(name, surname, number, position, birthday, team, date, height, weight, patronymic)
    
    if result == None:
        print("Произошла неизвестная ошибка, попробуйте повторить, если это не поможет, то обратитесь к разработчику")
    elif result:
        print("Страница игрока успешно создана")
    elif not result:
        print("Страница игрока не создана из-за ошибки, попробуйте повторить, если это не поможет, то обратитесь к разработчику")
    else:
        print("Если Вы видите это сообщение и станица игрока успешно создана, то обратитесь к разработчику. Спасибо")

def create_player(name, surname, number_player, position, birthday, team, date, height, weight, patronymic = ""):
    for i in DEFAULT_POSITION:
        if position == i:
            position = position
            break
        elif i == "Вратарь":
            add_error.add_warn(2)
            return
        
    for i in DEFAULT_TEAM:
        if team == i:
            team = team
            break
        elif i == "8x8":
            add_error.add_warn(4)
            return
    name_sur = name + surname
    
    name_patronymic = ""

    if patronymic == "":
        name_patronymic = name
    else:
        name_patronymic += name + " " + patronymic

    number_player_int = 0
    height_int = 0
    weight_int = 0    
    try:
        number_player_int = int(number_player)
        height_int = int(height)
        weight_int = int(weight)
    except:
        add_error.add_error(1)
        return  
    

    date_string = check_date(date, True)
    date_int = check_date(date, False, True)

    if (date_int or date_string) == None:
        return 
    
    result = create_page(name, name_patronymic, surname, number_player_int, position, birthday, team, date_string, date_int, height_int, weight_int)
    return result

 


def split_name(name, res = True):
    
    split_n = name.split(" ")
    i = 0
    result = False
    if res:
        for name in split_n:
            i += 1
            if i == 3:
                result = True
            else:
                result = False

        if not (result):
            add_error.add_warn(3)
            return   
        return split_n
    else:
        for name in split_n:
            i += 1
            if i == 2:
                result = True
            else:
                result = False 
                
        if not (result):
            add_error.add_warn(3)  
            return
        return split_n


def check_date(date, date_Bool = False, date_int_Bool = False):
    date_str = ""
    date_int = ""

    date_split = date.split(", ")
    match date_split[0]:
        case "Январь":
            date_int = f"01.01.{date_split[1]}"
        case "Февраль":
            date_int = f"01.02.{date_split[1]}"
        case "Март":
            date_int = f"01.03.{date_split[1]}" 
        case "Апрель":
            date_int = f"01.04.{date_split[1]}" 
        case "Май":
            date_int = f"01.05.{date_split[1]}" 
        case "Июнь":
            date_int = f"01.06.{date_split[1]}" 
        case "Июль":
            date_int = f"01.07.{date_split[1]}" 
        case "Август":
            date_int = f"01.08.{date_split[1]}" 
        case "Сентябрь":
            date_int = f"01.09.{date_split[1]}" 
        case "Октябрь":
            date_int = f"01.10.{date_split[1]}" 
        case "Ноябрь":
            date_int = f"01.11.{date_split[1]}"
        case "Декабрь":
            date_int = f"01.12.{date_split[1]}"
        case _:
            add_error.add_warn(5)     
            return 
    date_str = date
    if date_Bool and not date_int_Bool:
        return date_str
    if not date_Bool and date_int_Bool:
        return date_int
    

def create_page(
        name: str,
        name_patronymic: str,
        surname: str,
        number: int,
        position: str,
        birthday: str,
        team: str,
        date_string: str,
        date_int: str,
        height: str, 
        weight: str
    ):
    
    with open(f"player_{number}.html", "w+", encoding="utf-8") as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} {surname}</title>
    <link rel="stylesheet" href="./css/main.css" />
</head>

<body>
    @@include('blocks/header.html')


    <div class="page_player">

        <div class="player">
            <div class="photoblock">
                <div class="card_photo">
                    <img src="img/player/no_photo.png" alt="">
                </div>
            </div>

            <div class="aboutme">
                <div class="name">
                    <h3>{surname}</h3>
                    <h4>{name_patronymic}</h4>
                    <div class="position_number">
                        <div class="number">{number}</div>
                        <div class="position">{position}

                        </div>
                    </div>
                </div>
                <div class="information">
                    <ul class="information_me">
                        <li>
                            <div class="title_information">Возраст</div>
                            <div class="text" id="age"></div>
                        </li>
                        <li>
                            <div class="title_information">Дата рождения</div>
                            <div class="text" id="birthday">{birthday}</div>
                        </li>
                        <li>
                            <div class="title_information">Команда</div>
                            <div class="text">{team}</div>
                        </li>
                        <li>
                            <div class="title_information">Присоединился</div>
                            <div class="text">{date_string}</div>
                        </li>
                        <li>
                            <div class="title_information" id="teamTime">Время в команде</div>
                            <div class="text" id="datateamTime">{date_int}</div>
                        </li>
                        <li>
                            <div class="title_information">Рост</div>
                            <div class="text">{height}
                            </div>
                        </li>
                        <li>
                            <div class="title_information">Вес</div>
                            <div class="text">{weight}
                            </div>
                        </li>
                        <li>
                            <div class="title_information">Опыт</div>
                            <div class="text" id="experience">0</div>
                        </li>
                        <li>
                            <div class="title_information">Титул</div>
                            <div class="text" id="title"></div>
                        </li>
                    </ul>
                </div>
            </div>

        </div>

        <div class=statisticplayersall>
            <div class="title">Статистика</div>
            <div class="wrapper_block">
                <div class="block">
                    <div class="matchesall">0</div>
                    <div class="text">Матчей</div>
                </div>
                <div class="block">
                    <div class="goalall">0</div>
                    <div class="text">Голов забито</div>
                </div>
                <div class="block">
                    <div class="goalallOnaverage">0</div>
                    <div class="text">В среднем</div>
                </div>
                <div class="block">
                    <div class="assistall">0</div>
                    <div class="text">Ассистов</div>
                </div>
                <div class="block">
                    <div class="assistallOnaverage">0</div>
                    <div class="text">В среднем</div>
                </div>
                <div class="block">
                    <div class="assistgoalsall">0</div>
                    <div class="text">Гол+пас</div>
                </div>
                <div class="block">
                    <div class="goallostall">0</div>
                    <div class="text">Голов пропущено</div>
                </div>
                <div class="block">
                    <div class="zeromatchall">0</div>
                    <div class="text">Матчей на 0</div>
                </div>
            </div>
        </div>

        <div class=statisticthisyears>
            <div class="title">Текущий сезон</div>
            <div class="wrapper_block">
                <div class="block">
                    <div class="matches">0</div>
                    <div class="text">Матчей</div>
                </div>
                <div class="block">
                    <div class="goal">0</div>
                    <div class="text">Голов забито</div>
                </div>
                <div class="block">
                    <div class="goalOnaverage">0</div>
                    <div class="text">В среднем</div>
                </div>
                <div class="block">
                    <div class="assist">0</div>
                    <div class="text">Ассистов</div>
                </div>
                <div class="block">
                    <div class="assistOnaverage">0</div>
                    <div class="text">В среднем</div>
                </div>
                <div class="block">
                    <div class="assistgoals">0</div>
                    <div class="text">Гол+пас</div>
                </div>
                <div class="block">
                    <div class="goallost">0</div>
                    <div class="text">Голов пропущено</div>
                </div>
                <div class="block">
                    <div class="zeromatch">0</div>
                    <div class="text">Матчей на 0</div>
                </div>
            </div>
        </div>

        <div class="wrapper_achieved">
            <div class="achieved">
                <div class="experience">
                    <div class="title">Достижения</div>
                    <div class="wrapper_awards">
                        <div class="block_awards">
                            <div class="Number_Awards">0</div>
                            <div class="text">Наград</div>
                        </div>
                        <div class="block_awards">
                            <div class="Number_Month_nomination">0</div>
                            <div class="text">Номинант футболист месяца</div>
                        </div>
                        <div class="block_awards">
                            <div class="Number_Player_Month">0</div>
                            <div class="text">Футболист месяца</div>
                        </div>
                        <div class="block_awards">
                            <div class="Number_Year_nomination">0</div>
                            <div class="text">Номинант футболист года</div>
                        </div>
                        <div class="block_awards">
                            <div class="Number_Year_best">0</div>
                            <div class="text">Футболист года</div>
                        </div>
                    </div>

                    <div class="title">Список наград</div>
                    <div class="block">
                        <div class="text">
                            <div class="year">-</div>
                            <div class="company">-</div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <div class="photo">
            <div class="title_gallerey">Галерея</title>
                <div class="block">
                    <div class="img-container">
                        <div class="img">
                            <img src="img/player/photo_player/14-1.jpg" alt="">
                        </div>

                        <div class="img">
                            <img src="img/player/photo_player/.JPG" alt="">
                        </div>

                        <div class="img">
                            <img src="img/player/photo_player/.JPG" alt="">
                        </div>

                        <div class="img">
                            <img src="img/player/photo_player/.JPG" alt="">
                        </div>

                    </div>
                    <div class="pop-up">
                        <span>&times;</span>
                        <img src="img/prosmotr/1.JPG" alt="">
                    </div>
                </div>
            </div>
        </div>

    </div>

    @@include('blocks/footer.html')

    <script src="./js/index.bundle.js"></script>""" + """

    <script>
        document.querySelectorAll('.img-container img').forEach(img => {
            img.onclick = () => {
                document.querySelector('.pop-up').style.display = 'block';
                document.querySelector('.pop-up img').src = img.getAttribute('src'); // Исправление: заменили дефис на знак равенства
            }
        });

        document.querySelector('.pop-up span').onclick = () => {
            document.querySelector('.pop-up').style.display = 'none';
        }
    </script>

    <script src="js/playerpage.bundle.js"></script>
    <script src="js/playerstatistics.bundle.js"></script>
    <script src="./js/levelplayer.bundle.js"></script>
    <script src="./js/Awards.bundle.js"></script>

</body>

</html>""")
        return True

#print(check_date("Март, 2024", True))
#print(split_name("A D", False))
#create_player("Василий", "Голуб", "14", "Полузащитник", "26.01.1988", "8х8", "Февраль, 2023", "177", "67", "Васильевич")

# ДЛЯ ПРОВЕРКИ РАБОТОСПОСОБНИСТИ ФУНКЦИЙ
