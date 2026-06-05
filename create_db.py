# функція для ініціалізації бази даних та додавання даних
def create_db():
    from app import app
    from models import db, Game, GameMobale, GamePC

    with app.app_context():
        db.drop_all()  # видаляє всі таблиці (для навчання)
        db.create_all()  # створює заново

        if not Game.query.first():
        # ТИПИ СУШІ
            game1 = Game(name="brawl stars",
                         description="Швидкі розраховані на багато користувачів бої 3 на 3 і королівська битва для мобільних пристроїв.",
                         price=5.0,
                         image="images/brawl_stars.png", link="https://supercell.com/en/games/brawlstars/")

            game2 = Game(name="soul knight",
                         description="Досліджуйте підземелля, збирайте божевільну зброю, ухиляйтеся від куль і розстрілюйте всіх підряд! Просте керування та плавний ігровий процес.",
                         price=7.0,
                         image="images/www.jpg", link="https://soulknight.chillyroom.com/et")

            game3 = Game(name="granny",
                         description="Ласкаво просимо в будинок Бабусі. Гренні тримає вас під замком у своєму будинку. Вам потрібно вибратися звідти, але будьте обережні та дуже тихі.",
                         price=8.0,
                         image="images/unnamed.png", link="https://grannyhorror.com/")

            game4 = Game(name="Five Nights at Freddy's",
                         description="Ласкаво просимо на нову літню роботу в піцерію Freddy Fazbear's Pizza. Головне завдання — стежити за камерами та вижити п'ять ночей.",
                         price=8.0,
                         image="images/fnaf.webp", link="http://www.scottgames.com")

            game5 = Game(name="subnautica",
                         description="Спустіться в глибини чужого підводного світу, сповненого чудес і небезпек. Створюйте спорядження, пілотуйте підводні човни та виживайте.",
                         price=8.0,
                         image="images/SNPS4.webp", link="https://subnautica.com")

            game6 = Game(name="plants-vs-zombies",
                         description="Готуйтеся удобрити своїх рослини, адже натовп веселих зомбі збирається вторгнутися у ваш дім. Використовуйте арсенал із 49 рослин-вбивць.",
                         price=8.0,
                         image="images/images1.jpg", link="https://www.ea.com/games/plants-vs-zombies")

            game7 = Game(name="cuphead",
                         description="Класичний екшен-платформер, зосереджений на битвах з босами. Натхненний мультфільмами 1930-х років, з джазовим саундтреком та акварельними фонами.",
                         price=8.0,
                         image="images/images.steamusercontent.jpg", link="https://cupheadgame.com/")

            game8 = Game(name="terraria",
                         description="Копайте, боріться, досліджуйте, будуйте! У цій насиченій екшеном пригоді немає нічого неможливого. Весь світ — це ваше полотно.",
                         price=8.0,
                         image="images/images.jpg", link="https://www.terraria.org/")

            game9 = Game(name="Minecraft",
                         description="Досліджуйте нескінченні світи та будуйте все, що завгодно: від найпростіших домівок до величних замків. Грай у режимі творчості або виживання.",
                         price=8.0,
                         image="images/i.webp", link="https://www.minecraft.net")

            game10 = Game(name="Doki Doki Literature Club",
                          description="Ласкаво просимо до літературного клубу! Пишіть вірші для своєї коханої та відчуйте весь жах шкільного кохання в цій психологічній новелі.",
                          price=8.0,
                          image="images/image112345s.jpg", link="https://ddlc.moe/")

            game11 = Game(name="RimWorld",
                          description="Науково-фантастичний симулятор колонії під керівництвом ШІ-оповідача. Генерує історії, відстежуючи психологію, потреби, поранення та стосунки персонажів.",
                          price=8.0,
                          image="images/f0c83dc0-ac26-44ba-9e7b-3778d1417006.png", link="https://rimworldgame.com/")

            game12 = Game(name="Dont-Starve",
                          description="Безкомпромісна гра про виживання в дикій природі, наповнена наукою та магією. Спробуйте вижити, опинившись у пастці загадкового та безжального дикого світу.",
                          price=8.0,
                          image="images/dontstarve.png", link="https://www.klei.com/games/dont-starve")

            game13 = Game(name="Assassin's Creed III",
                          description="Американські колонії, 1775 рік. Охороняйте свою землю та свій народ, запаліть вогонь революції v ролі ассасина Коннора.",
                          price=8.0,
                          image="images/Assassin's_Creed_III_Cover.webp",
                          link="https://www.ubisoft.com/en-us/game/assassins-creed")

            game14 = Game(name="GTA V",
                          description="Коли молодий вуличний шахрай, касовий грабіжник і психопат опиняються вплутаними в кримінальний світ, вони мають здійснити серію небезпечних пограбувань.",
                          price=8.0,
                          image="images/ГТА.png", link="https://www.rockstargames.com/gta-v")

            game15 = Game(name="Roblox",
                          description="Кінцева віртуальна всесвіт, яка дозволяє вам грати, створювати та бути чим завгодно, що ви можете собі уявити. Приєднуйтесь до мільйонів гравців.",
                          price=8.0,
                          image="images/Роблокс.jpg", link="https://www.roblox.com/")

            game16 = Game(name="Evil Nun",
                          description="Страшна черниця заманила вас у школу. Розгадуйте головоломки, шукайте таємниці та втікайте з цього закладу, поки не стало надто пізно.",
                          price=8.0,
                          image="images/Evil Nun.png", link="https://keplerians.com/")

            game17 = Game(name="Slime Rancher",
                          description="Історія Беатрікс ЛеБо, відважного молодого ранчеро, яка вирушає на життя за мільярд світлових років від Землі, щоб збирати різнокольорових слаймів.",
                          price=8.0,
                          image="images/Slime Rancher.webp", link="https://www.slimerancher.com/")

            game18 = Game(name="Wolfenstein",
                          description="Шутер від першої особи, в якому ви вирушаєте на захоплюючу місію по всьому Берліну, щоб повалити нацистську військову машину.",
                          price=8.0,
                          image="images/Wolfenstein.jfif", link="https://bethesda.net/en/game/wolfenstein-youngblood")

            game19 = Game(name="Hollow Knight",
                          description="Класична двовимірна екшен-пригода у величезному взаємопов'язаному світі. Досліджуйте зруйноване королівство героїв та комах.",
                          price=8.0,
                          image="images/Hollow_Knight.jpg", link="https://www.hollowknight.com/")

            game20 = Game(name="Little Nightmares",
                          description="Пориньте в похмуру казку Little Nightmares, яка змусить вас згадати свої дитячі кошмари. Допоможіть дівчинці на ім'я Шоста вибратися з Черева — таємничого підводного судна, що кишить жахливими мешканцями.",
                          price=6.0,
                          image="images/литл наймерс.jpg", link="https://www.bandainamcoent.com/games/little-nightmares")

            game21 = Game(name="The Last of Us",
                          description="У спустошеній цивілізації, де лютують заражені та жорстокі виживші, загартований у боях головний герой має вивести 14-річну дівчинку з військової карантинної зони.",
                          price=15.0,
                          image="images/The Last of Us.webp",
                          link="https://www.playstation.com/games/the-last-of-us-part-i/")

            game22 = Game(name="Stray",
                          description="Пригодницька гра від третьої особи, в якій ви опинитеся в ролі бродячого кота, що мусить розгадати давню таємницю та втекти з давно забутого кіберміста.",
                          price=10.0,
                          image="images/Stray_cover_art.jpg", link="https://stray.game")

            game23 = Game(name="Stardew Valley",
                          description="Вам дісталася стара дідусева ферма. Озброївшись інструментами та жменею монет, ви вирушаєте починати нове життя та перетворювати пустище на квітучий сад.",
                          price=7.5,
                          image="images/Logo_of_Stardew_Valley.png", link="https://www.stardewvalley.net")

            # Розкоментовано та змінено на Undertale (картинка залишена незмінною)
            game24 = Game(name="Undertale",
                          description="Ласкаво просимо в підземелля, куди падають людські діти. У цій унікальній рольовій грі вам не обов'язково нікого вбивати. Спілкуйтеся, підкорюйте серця монстрів або оберіть шлях безжального бійця.",
                          price=4.99,
                          image="images/png-klev-club-9747-p-nadpis-anderteil-png-21.png", link="https://undertale.com")

            game25 = Game(name="Among Us",
                          description="Групова гра на дедукцію та командну роботу. Намагайтесь підготувати свій космічний корабель до відльоту. Але стережіться самозванців, які прагнуть усіх убити!",
                          price=7.5,
                          image="images/Among_Us.png", link="https://www.innersloth.com/games/among-us/")

            game26 = Game(name="Angry Birds",
                          description="Класична головоломка, де ви використовуєте унікальні здібності розлючених пташок, щоб руйнувати захисні споруди жадібних зелених свиней, які викрали їхні яйця.",
                          price=7.5,
                          image="images/Angry_Birds_promo_art.png", link="https://www.rovio.com/games/angry-birds-friends/")

            game27 = Game(name="Ам Ням",
                          description="Весела фізична головоломка. Перерізайте мотузки, долайте перешкоди та годуйте кумедного зеленого монстрика Ам Няма його улюбленими цукерками.",
                          price=7.5,
                          image="images/Cut_the_Rope_logo.png", link="https://www.zeptolab.com/games/cut_the_rope")

            game28 = Game(name="Subway Surfers",
                          description="Динамічний нескінченний раннер. Тікайте від сердитого інспектора, бігайте по дахах потягів, ухиляйтеся від перешкод та збирайте монети.",
                          price=7.5,
                          image="images/EdinburghIcon.png", link="https://www.sybo.games")

            # НОВА ГРА ДЛЯ КАТЕГОРІЇ "ВСІ ІГРИ"
            game29 = Game(name="Cyberpunk 2077",
                          description="Пригодницька екшн-RPG у відкритому світі мегаполіса Найт-Сіті, де ви граєте за кібернетично посиленого найманця.",
                          price=29.99,
                          image="images/Ryrrx206WNZbVZv6yow2JQ.jpeg", link="https://www.cyberpunk.net")

            # Додаємо всі ігри та роли в чергу (session) БД (Сюди додано game29)
            db.session.add_all([
                game1, game2, game3, game4, game5, game6, game7, game8, game9, game10,
                game11, game12, game13, game14, game15, game16, game17, game18, game19,
                game20, game21, game22, game23, game24, game25, game26, game27, game28,
                game29
            ])

        if not GameMobale.query.first():
            gamemobale1 =  GameMobale(name="brawl stars",
                     description="Швидкі розраховані на багато користувачів бої 3 на 3 і королівська битва для мобільних пристроїв.",
                     price=5.0,
                     image="images/brawl_stars.png", link="https://supercell.com/en/games/brawlstars/")

            gamemobale2 = GameMobale(name="soul knight",
                         description="Досліджуйте підземелля, збирайте божевільну зброю, ухиляйтеся від куль і розстрілюйте всіх підряд! Просте керування та плавний ігровий процес.",
                         price=7.0,
                         image="images/www.jpg", link="https://soulknight.chillyroom.com/et")

            gamemobale3 = GameMobale(name="granny",
                         description="Ласкаво просимо в будинок Бабусі. Гренні тримає вас під замком у seuму будинку. Вам потрібно вибратися звідти, але будьте обережні та дуже тихі.",
                         price=8.0,
                         image="images/unnamed.png", link="https://grannyhorror.com/")

            gamemobale4 = GameMobale(name="Roblox",
                          description="Кінцева віртуальна всесвіт, яка дозволяє вам грати, створювати та бути чим завгодно, що ви можете собі уявити. Приєднуйтесь до мільйонів гравців.",
                          price=8.0,
                          image="images/Роблокс.jpg", link="https://www.roblox.com/")

            gamemobale5 = GameMobale(name="Evil Nun",
                          description="Страшна черниця заманила вас у школу. Розгадуйте головоломки, шукайте таємниці та втікайте з цього закладу, поки не стало надто пізно.",
                          price=8.0,
                          image="images/Evil Nun.png", link="https://keplerians.com/")

            gamemobale6 = GameMobale(name="Among Us",
                          description="Страшна черниця заманила вас у школу. Розгадуйте головоломки, шукайте таємниці та втікайте з цього закладу, поки не стало надто пізно.",
                          price=8.0,
                          image="images/Among_Us.png", link="https://www.innersloth.com/games/among-us/")

            gamemobale7 = GameMobale(name="Angry Birds",
                          description="Страшна черниця заманила вас у школу. Розгадуйте головоломки, шукайте таємниці та втікайте з цього закладу, поки не стало надто пізно.",
                          price=8.0,
                          image="images/Angry_Birds_promo_art.png", link="https://www.rovio.com/games/angry-birds-friends/")

            gamemobale8 = GameMobale(name="Ам Ням",
                          description="Весела фізична головоломка. Перерізайте мотузки, долайте перешкоди та годуйте кумедного зеленого монстрика Ам Няма його улюбленими цукерками.",
                          price=7.5,
                          image="images/Cut_the_Rope_logo.png", link="https://www.zeptolab.com/games/cut_the_rope")

            gamemobale9 = GameMobale(name="Subway Surfers",
                          description="Динамічний нескінченний раннер. Тікайте від сердитого інспектора, бігайте по дахах потягів, ухиляйтеся від перешкод та збирайте монети.",
                          price=7.5,
                          image="images/EdinburghIcon.png", link="https://www.sybo.games")




            # Додаємо всі головні інгредієнти в чергу (session) БД
            db.session.add_all(
                [gamemobale1, gamemobale2, gamemobale3, gamemobale4,gamemobale5,gamemobale6,gamemobale7,gamemobale8,gamemobale9])

        if not GamePC.query.first():
            gamepc1 = GamePC(name="Five Nights at Freddy's",
                         description="Ласкаво просимо на нову літню роботу в піцерію Freddy Fazbear's Pizza. Головне завдання — стежити за камерами та вижити п'ять ночей.",
                         price=8.0,
                         image="images/fnaf.webp", link="http://www.scottgames.com")

            gamepc2 = GamePC(name="subnautica",
                             description="Спустіться в глибини чужого підводного світу, сповненого чудес і небезпек. Створюйте спорядження, пілотуйте підводні човни та виживайте.",
                             price=8.0,
                             image="images/SNPS4.webp", link="https://subnautica.com")

            gamepc3 = GamePC(name="plants-vs-zombies",
                             description="Готуйтеся удобрити свої рослини, адже натовп веселих зомбі збирається вторгнутися у ваш дім. Використовуйте арсенал із 49 рослин-вбивць.",
                             price=8.0,
                             image="images/images1.jpg", link="https://www.ea.com/games/plants-vs-zombies")

            gamepc4 = GamePC(name="cuphead",
                             description="Класичний екшен-платформер, зосереджений на битвах з босами. Натхненний мультфільмами 1930-х років, з джазовим саундтреком та акварельними фонами.",
                             price=8.0,
                             image="images/images.steamusercontent.jpg", link="https://cupheadgame.com/")

            gamepc5 = GamePC(name="terraria",
                             description="Копайте, боріться, досліджуйте, будуйте! У цій насиченій екшеном пригоді немає нічого неможливого. Весь світ — це ваше полотно.",
                             price=8.0,
                             image="images/images.jpg", link="https://www.terraria.org/")

            gamepc6 = GamePC(name="Minecraft",
                             description="Досліджуйте нескінченні світи та будуйте все, що завгодно: від найпростіших домівок до величних замків. Грай у режимі творчості або виживання.",
                             price=8.0,
                             image="images/i.webp", link="https://www.minecraft.net")

            gamepc7 = GamePC(name="Doki Doki Literature Club",
                             description="Ласкаво просимо до літературного клубу! Пишіть вірші для своєї коханої та відчуйте весь жах шкільного кохання в цій психологічній новелі.",
                             price=8.0,
                             image="images/image112345s.jpg", link="https://ddlc.moe/")

            gamepc8 = GamePC(name="RimWorld",
                             description="Науково-фантастичний симулятор колонії під керівництвом ШІ-оповідача. Генерує історії, відстежуючи психологію, потреби, поранення та стосунки персонажів.",
                             price=8.0,
                             image="images/f0c83dc0-ac26-44ba-9e7b-3778d1417006.png", link="https://rimworldgame.com/")

            gamepc9 = GamePC(name="Dont-Starve",
                             description="Безкомпромісна гра про виживання в дикій природі, наповнена наукою та магією. Спробуйте вижити, опинившись у пастці загадкового та безжального дикого світу.",
                             price=8.0,
                             image="images/dontstarve.png", link="https://www.klei.com/games/dont-starve")

            gamepc10 = GamePC(name="Assassin's Creed III",
                              description="Американські колонії, 1775 рік. Охороняйте свою землю та свій народ, запаліть вогонь революції v ролі ассасина Коннора.",
                              price=8.0,
                              image="images/Assassin's_Creed_III_Cover.webp",
                              link="https://www.ubisoft.com/en-us/game/assassins-creed")

            gamepc11 = GamePC(name="GTA V",
                              description="Коли молодий вуличний шахрай, касовий грабіжник і психопат опиняються вплутаними в кримінальний світ, вони мають здійснити серію небезпечних пограбувань.",
                              price=8.0,
                              image="images/ГТА.png", link="https://www.rockstargames.com/gta-v")

            gamepc17 = GamePC(name="Slime Rancher",
                            description="Історія Беатрікс ЛеБо, відважного молодого ранчеро, яка вирушає на життя за мільярд світлових років від Землі, щоб збирати різнокольорових слаймів.",
                            price=8.0,
                            image="images/Slime Rancher.webp", link="https://www.slimerancher.com/")

            gamepc18 = GamePC(name="Wolfenstein",
                            description="Шутер від першої особи, в якому ви вирушаєте на захоплюючу місію по всьому Берліну, щоб повалити нацистську військову машину.",
                            price=8.0,
                            image="images/Wolfenstein.jfif", link="https://bethesda.net/en/game/wolfenstein-youngblood")

            gamepc19 = GamePC(name="Hollow Knight",
                            description="Класична двовимірна екшен-пригода у величезному взаємопов'язаному світі. Досліджуйте зруйноване королівство героїв та комах.",
                            price=8.0,
                            image="images/Hollow_Knight.jpg", link="https://www.hollowknight.com/")

            gamepc20 = GamePC(name="Little Nightmares",
                            description="Пориньте в похмуру казку Little Nightmares, яка змусить вас згадати свої дитячі кошмари. Допоможіть дівчинці на ім'я Шоста вибратися з Черева — таємничого підводного судна, що кишить жахливими мешканцями.",
                            price=6.0,
                            image="images/литл наймерс.jpg", link="https://www.bandainamcoent.com/games/little-nightmares")

            gamepc21 = GamePC(name="The Last of Us",
                            description="У спустошеній цивілізації, де лютують заражені та жорстокі виживші, загартований у боях головний герой має вивести 14-річну дівчинку з військової карантинної зони.",
                            price=15.0,
                            image="images/The Last of Us.webp",
                            link="https://www.playstation.com/games/the-last-of-us-part-i/")

            gamepc22 = GamePC(name="Stray",
                            description="Пригодницька гра від третьої особи, в якій ви опинитеся в ролі бродячого кота, що мусить розгадати давню таємницю та втекти з давно забутого кіберміста.",
                            price=10.0,
                            image="images/Stray_cover_art.jpg", link="https://stray.game")

            gamepc23 = GamePC(name="Stardew Valley",
                            description="Вам дісталася стара дідусева ферма. Озброївшись інструментами та жменею монет, ви вирушаєте починати нове життя та перетворювати пустище на квітучий сад.",
                            price=7.5,
                            image="images/Logo_of_Stardew_Valley.png", link="https://www.stardewvalley.net")

            gamepc24 = GamePC(name="Undertale",
                            description="Ласкаво просимо в підземелля, куди падають людські діти. У цій унікальній рольовій грі вам не обов'язково нікого вбивати. Спілкуйтеся, підкорюйте серця монстрів або оберіть шлях безжального бійця.",
                            price=4.99,
                            image="images/png-klev-club-9747-p-nadpis-anderteil-png-21.png", link="https://undertale.com")

            # НОВА ГРА ДЛЯ КАТЕГОРІЇ "ІГРИ НА ПК"
            gamepc25 = GamePC(name="Cyberpunk 2077",
                              description="Пригодницька екшн-RPG у відкритому світі мегаполіса Найт-Сіті, де ви граєте за кібернетично посиленого найманця.",
                              price=29.99,
                              image="images/Ryrrx206WNZbVZv6yow2JQ.jpeg", link="https://www.cyberpunk.net")

            # Додавання у сесію тепер працює коректно, бо всі змінні унікальні (Сюди додано gamepc25)
            db.session.add_all([
                gamepc1, gamepc2, gamepc3, gamepc4, gamepc5, gamepc6, gamepc7, gamepc8, gamepc9, gamepc10, gamepc11,
                gamepc17, gamepc18, gamepc19, gamepc20, gamepc21, gamepc22, gamepc23, gamepc24, gamepc25
            ])
        db.session.commit()

if __name__ == '__main__':
    create_db()
    print("Базу даних успішно ініціалізовано!")