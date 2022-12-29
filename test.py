from intramove.intramove import Intramove

imove = Intramove()

# print(imove.get_available_packages())

# imove.buy_package(product="headlines-100", quantity=1)

my_id = imove.get_id(email="abdulatifsal@gmail.com", name="Abdellatif Dalab")["client_id"]

my_api_key = imove.get_api_key(my_id)["api_key"]

for i in range(1):
    analysis = imove.analyze_headline(
        api_key=my_api_key,
        headline="ECB Hikes Rates by 50bps, Signals Further Increases",
        date="12/15/2022",
        callback_url="",
    )

    print(analysis)
