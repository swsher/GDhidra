import requests

def main():
    headers = {"User-Agent": ""}
    data = {"secret": "Wmfd2893gb7", "levelID": 97459496}
    url = "http://www.boomlings.com/database/downloadGJLevel22.php"
    request = requests.post(url, data, headers=headers)
    levelString = request.text.split("#")[0]
    with open("level.txt", 'w') as file:
        file.write(levelString)

    print(levelString)

if __name__=="__main__":
    main()