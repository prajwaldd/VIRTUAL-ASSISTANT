from model import speaker_identifier
from interface import unauthorized

if __name__ == "__main__":

    #predict the user using speaker_identifier method from model
    pred = speaker_identifier()

    if pred == 1:
        print("Welcome back !")

        #if authorized start interacting and launch voice assistant
        exec(open("interface.py").read())
    else:
        print(" Sorry you are Unauthorized to acsess !!")
        #speak "You are unauthorized"
        unauthorized()












