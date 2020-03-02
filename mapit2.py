import webbrowser,sys
webbrowser.open("https://www.google.com/maps/place/"+" ".join(sys.argv[1:]))