import random
songs_dict = {
    "happy" : ["Good Vibrations - The Beach Boys",
                "The Twist - Chubby Checker",
                "Big Yellow Taxi - Joni Mitchell",
                "Dancing Queen - Abba",
                "I Believe In A Thing Called Love - The Darkness",
                "I'm Yours - Jason Mraz"],
    "sad" : ["Gary Jules  - Mad World",
                "R.E.M. - Everybody Hurts",
                "Someone Like You - Adele",
                "Sinead O'Connor - Nothing Compares 2 U",
                "Johnny Cash - Hurt",
                "Passenger - Let Her Go"]
    }


mood_choice = input("What mood are you in? Choose between happy and sad. \n")
print("I recommend the song " + songs_dict[mood_choice][random.randint(0, len(songs_dict[mood_choice]))])
