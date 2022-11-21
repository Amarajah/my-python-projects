import pyshorteners
long_url = input("Enter the url you wish to shorten: ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("Your short url is " + short_url)