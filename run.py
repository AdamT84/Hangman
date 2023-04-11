import random

HANGMAN_PICS = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

words = "basketball football baseball soccer tennis golf hockey \
        volleyball rugby badminton tabletennis swimming athletics \
        gymnastics wrestling boxing cycling skiing snowboarding \
        archery shooting fencing rowing kayaking canoeing diving \
        weightlifting powerlifting bodybuilding triathlon marathon \
        pentathlon decathlon surfing skateboarding rockclimbing \
        mountaineering fishing hunting horsebackriding \
        polo squash racquetball lacrosse ultimatefrisbee \
        kickboxing karate taekwondo judo aikido capoeira \
        jiu-jitsu muaythai crossfit parkour calisthenics bocce croquet \
        curling darts billiards bowling skating sledding \
        tobogganing bobsleigh luge snowmobiling \
        kiteboarding windsurfing parasailing".split()
