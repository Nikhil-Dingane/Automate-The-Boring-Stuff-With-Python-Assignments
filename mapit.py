import webbrowser
print("Enter the place name:")
placename=input()
print("Enter state name:")
statename=input()
print("Enter country name:")
countryname=input()
webbrowser.open("https://www.google.com/maps/place/"+placename+","+statename+","+countryname)