import numpy as np

directions = np.array(["Left", "Right", "Straight", "Back"])
challenges = ["pond", "fruit yard", "mountain", "forest"]
route_responses = {
    "Swim across": "You swim across and continue with your exploration",
    "Walk alongside": "You walk along the pond, finding a safe passage.",
    "Pick a fruit": "You pick a fruit and eat",
    "Keep exploring": "You keep exploring to find a new discovery"
}


def make_a_decision(prompt, options):
    while True:
        print(prompt)
        for index, option in enumerate(options, 1):
            print(f"{index}. {option}")
        try:
            your_choice = int(input("Select an option: "))
            if 1 <= your_choice <= len(options):
                return options[your_choice - 1]
        except ValueError:
            print("Your choice is not valid! Please enter a number.")


def first_option():
    first_decision = make_a_decision("Which path do you choose?", directions)

    if first_decision == "Left":
        print(f"Infront of you there is a {challenges[0]}.")
        second_decision = make_a_decision("Do you swim across or walk alongside?",
                                          ["Swim across", "Walk alongside the pond"])
    else:
        print(f"You get into a {challenges[1]}.")
        second_decision = make_a_decision("Do you pick a fruit or keep exploring?", ["Pick a fruit", "Keep exploring"])

    print(route_responses[second_decision])
    return first_decision, second_decision


def second_option():
    decision3 = make_a_decision("You hear a lion roar, do you hide or ignore it?", ["Hide", "Ignore the sound"])
    return decision3


def final_option():
    decision4 = make_a_decision("You find an abandoned pet. What do you do?", ["Take it Home", "Leave it there"])

    if decision4 == "Take it Home":
        print("You have a kind heart, buddy!")
    else:
        print("You leave it there and keep exploring.")

    return decision4


def game_loop():
    print("It's playtime!")
    first_decision, second_decision = first_option()
    third_decision = second_option()
    fourth_decision = final_option()

    print(f"Summary of your choices: {first_decision}, {second_decision}, {third_decision}, {fourth_decision}")


def main():
    while True:
        game_loop()
        replay = input("Replay? (yes/no): ").lower()
        if replay == "no":
            print("Thank you for participating")
            break
        elif replay == "yes":
            continue
        else:
            print("Invalid input type 'yes' or 'no'.")


main()
