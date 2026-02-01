import webbrowser
# to open in existing browser
webbrowser.open('https://labex.io/linuxjourney')
# to open in a new browser 
webbrowser.open_new('https://tryhackme.com/')
#
webbrowser.open_new_tab('https://tryhackme.com/')
# decide the browser
c = webbrowser.get('firefox')
c.open('https://www.facebook.com')