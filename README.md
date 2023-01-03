# GoogleSheetsSave&Send
I needed to create a backup for my google sheets and then send the backup to my work mail.
so I created this script to help me do this automatically.


This script downloads a sheet from `Google Sheets` send it via gmail and then deletes it from the location downloaded


thanks to [The-Intrigued-Engineer](https://github.com/The-Intrigued-Engineer) for the [encoding solution](https://github.com/The-Intrigued-Engineer/python_emails/blob/main/with_attachments.py)


### Setup Instructions
>1. Create a Google Cloud Platform project and get the `.jason` file. This is the authentication for the google drive.
**!!SAVE THE FILE SOMEWHARE SAFE!!**
[Here's a tutorial for that](https://www.youtube.com/watch?v=wrR0YLzh4DQ&ab_channel=MillibitTutorials%3ARuchir%27sCodingClips)
>2. Get the Key of the Spasific Google Sheet you want to download.
for example, in this sheet `https://docs.google.com/spreadsheets/d/1zmW8vR7Nwm8Uedfr9zI7WmNsfuTwzk8WCtj4wbN6LUA/edit#gid=0`
the Key is `1zmW8vR7Nwm8Uedfr9zI7WmNsfuTwzk8WCtj4wbN6LUA`
>3. Make sure your Google Account have eneabled `Two-Factor Authentication` then in the Account Managment go to Security>>App Password>>Create new password for `email` app and device `other`. you will get a `string` key **!!SAVE THE FILE SOMEWHARE SAFE!!** once you see it google will never show it again!
>4. Change the script according to the outcome of the other steps above
>5. Enjoy :)
