import datetime

def check_birthday(file_path):
    today = datetime.date.today().strftime('%m/%d')
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            name, birthday = line.strip().split(',')
            if birthday == today:
                print(f"🎉 今日は{name}さんの誕生日です！")

if __name__ == "__main__":
    check_birthday("birthdays.txt")
