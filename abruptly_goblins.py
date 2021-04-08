#Tasked to find the best day available from a list of gamers.

gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Input name & availability.")

kimberly = {'name': "Kimberly Warner", 'availability': ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    return {
        'Monday':    0,
        'Tuesday':   0,
        'Wednesday': 0,
        'Thursday':  0,
        'Friday':    0,
        'Saturday':  0,
        'Sunday':    0,
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
#print(count_availability)
#prints: {'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}

def find_best_night(availability_table):
    highest_num = 0
    for day, available in availability_table.items():
        if available > highest_num:
            highest_num = available
            best_date = day
    return best_date

game_night = find_best_night(count_availability)
#print(game_night)

def available_on_night(gamers_list, day):
    gamers_available = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            gamers_available.append(gamer['name'])
    return gamers_available

attending_game_night = available_on_night(gamers, game_night)
#print(attending_game_night)

form_email = "Hi {name}, I invite you to join us on {day_of_week} to enjoy a game night of your favorite game; {game}"
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")
#prints: "Hi Thomas Nelson, I invite you to join us on Thursday to enjoy a game night of your favorite game; Abruptly Goblins!"
#for everyone available_on_night

#THOSE WHO CAN NOT ATTEND
unable_to_attend_best_night = []
for gamer in gamers:
    if gamer['name'] not in attending_game_night:
        unable_to_attend_best_night.append(gamer)

#print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")
#prints same email above but altered for the second best night.
#prints: "Hi Kimberly Warner, I invite you to join us on Monday to enjoy a game night of your favorite game; Abruptly Goblins!"