# import urllib
# import urllib.request to data from url
# function that takes a url a input and returns a response


import urllib.request as urllib


def main(url):
    print("checking connectivity...")

    response = urllib.urlopen(url)
    print("connection established", url)
    print(f"The response was {response.getcode()}")

print("This is a site connectivity checker program")
input_url = input("Input the URL of the site: ")

main(input_url)