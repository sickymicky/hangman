import random, os

# from wordlist import words
# from check_spaces import check_for_spaces

# words = ("blue-ringed octopus", "red-deer", "blue whale", "gorilla", "polar-bear", "sand-dollar", "great white shark", "grizzly bear","three-toed-toad")
words = ("blue-ringed octopus","great white shark", "grizzly bear", "three-toed-toad","aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "blue whale","boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo","killer whale", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer","red fox", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses):
    print("*" * stars)

    for line in hangman_art[wrong_guesses]:
        print(line)

    print("*" * stars)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def check_for_spaces(answer, hint):

    if "-" in answer or " " in answer:
        for i in range(len(answer)):

            if answer[i] == "-":
                hint[i] = "-"
            elif answer[i] == " ":
                hint[i] = " "
            else:
                hint[i] = "_"


stars = 20


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    

    check_for_spaces(answer, hint)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    os.system("clear")
    while is_running:
      
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("\nEnter a letter: ").lower()
        os.system("clear")
        

        if len(guess) != 1 or not guess.isalpha():
            print(f"Guessed letters: {guessed_letters}")
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"Guessed letters: {guessed_letters}")
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)
        print(f"Guessed letters: {guessed_letters}")

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
                    guessed_letters.add(guess)
        else:
            wrong_guesses += 1
            
            print(f"{guess} not in word!")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
