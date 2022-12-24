from intramove import Intramove

imove = Intramove()

# Using the same email and name from checkout, get your unique ID

my_id = imove.get_id(email="abdulatifsal@gmail.com", name="abdellatif")

# Use your unique ID to get your active API key
my_api_key = imove.get_api_key(my_id)


#print(imove.get_status(my_api_key))
# Start using the API!
callback_url= ""#"https://webhook.site/6116f4f2-2ff8-49e7-a50b-706b67f74b08"

analysis = imove.analyze_headline(
    api_key=my_api_key,
    headline="The US stock market crashed",
    date="",
    #callback_url=callback_url,
)

if not callback_url:
    print(analysis)
