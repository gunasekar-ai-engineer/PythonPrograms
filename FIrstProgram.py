print("Hi... I'm an AI Bot...")
ai_name = input("How would you like to Name me.. ").upper()
print(f"Thank you for naming me as '{ai_name}'. I can run and complete rounds on your command.")
can_run = True
continue_run = "YES"
total_running_count = 0
while can_run:
    if continue_run == "YES":
        total_running_count = int(input("How many rounds you wanna me to run : "))
    elif continue_run == "NO":
        print(
            f"\nThank you for making to rest for a while... This is {ai_name}, your AI Bot Signing off.. Good Bye.. Have a Good Day...")
        break
    else:
        print("Could you please command me by saying 'Yes' or 'No'")
        total_running_count = 0

    for current_round in range(total_running_count):
        print(
            f"\nI'm {ai_name}, an AI Bot. I completed Round No. {current_round + 1} and started Round No. {current_round + 2} :-D")
    else:
        if total_running_count != 0:
            print(f"Oops.... I stopped Running :-( Because you asked me to run only '{total_running_count}' Rounds.")
    continue_run = input(f"\nDo you wanna me to continue running.. ").upper()
