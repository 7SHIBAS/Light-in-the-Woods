# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mae = Character("Mae", color="#952430")
define bea = Character("Bea", color="#4f7175")
define gregg = Character("Gregg", color="#e8971a")
define angus = Character("Angus", color="#7b2515")
define lori = Character("Lori", color="#2d3740")
define germ = Character("Germ", color="#0a1d1e")
define selma = Character("Selmers", color="#d15384")
define narrator = Character("")
define player = Character("Player")
define candy = Character("Candy")
define stan = Character("Stan")
define name = Character("Alex")
define guardian = Character("Guardian")
define cafebird = Character("Trish")
define loriunknown = Character("???")
define maeunknown = Character("???")
define selmaunknown = Character("???")
define trishunknown = Character("???")
define trish = Character("Trish")
define greggunknown = Character("???", color="#d18e00")
define beaunknown = Character("???")
define angusunknown = Character("???")
define harleyunknown = Character("???")
define harley = Character("Harley")
define receptionist = Character("???")
define marcie = Character("Marcie")




#sprite flips
image mae neutral flip = im.Flip("mae neutral.png", horizontal=True)
image mae grump flip = im.Flip("mae grump.png", horizontal=True)
image mae angry flip = im.Flip("mae angry.png", horizontal=True)
image mae freakout flip = im.Flip("mae freakout.png", horizontal=True)
image mae skeptical flip = im.Flip("mae skeptical.png", horizontal=True)
image mae curious flip = im.Flip("mae curious.png", horizontal=True)
image mae happy flip = im.Flip("mae happy.png", horizontal=True)
image mae curious2 flip = im.Flip("mae curious2.png", horizontal=True)
image mae panic flip = im.Flip("mae panic.png", horizontal=True)
image mae sad1 flip = im.Flip("mae sad1.png", horizontal=True)
image mae laugh flip = im.Flip("mae laugh.png", horizontal=True)
image bea neutral flip = im.Flip("bea neutral.png", horizontal=True)
image gregg neutral flip = im.Flip("gregg neutral.png", horizontal=True)
image angus neutral flip = im.Flip("angus neutral.png", horizontal=True)
image lori neutral flip = im.Flip("lori neutral.png", horizontal=True)
image lori nervous flip = im.Flip("lori nervous.png", horizontal=True)
image lori nervous2 flip = im.Flip("lori nervous2.png", horizontal=True)
image lori anxious flip = im.Flip("lori anxious.png", horizontal=True)
image lori anxious2 flip = im.Flip("lori anxious2.png", horizontal=True)
image lori anxious3 flip = im.Flip("lori anxious3.png", horizontal=True)
image lori breath flip = im.Flip("lori breath.png", horizontal=True)
image lori sad flip = im.Flip("lori sad.png", horizontal=True)
image lori sad2 flip = im.Flip("lori sad2.png", horizontal=True)
image germ neutral flip = im.Flip("germ neutral.png", horizontal=True)
image selma neutral flip = im.Flip("selma neutral.png", horizontal=True)
image candy neutral flip = im.Flip("candy neutral.png", horizontal=True)
image stan neutral flip = im.Flip("stan neutral.png", horizontal=True)




define tallright = Position(xpos=0.9, xanchor=0.9, ypos=100, yanchor=100)


label start:

    # variables
    define loriheight = 2.2
    define angusheight = 0.67
    define beaheight = 0.3
    define maeheight = 2.2
    define selmaheight = .02
    define greggheight = .5
    define germheight = 1.7
    $ currentDay = "December 7"
    $ maeAP = 0
    $ beaAP = 0
    $ greggAP = 0
    $ angusAP = 0
    $ loriAP = 0
    $ selmaAP = 0
    $ germAP = 0
    $ selmaName = "Selmers"
    $ beenToChurch = False
    $ timid = 0
    $ bold = 0
    $ inquisitive = 0
    $ cynical = 0
    $ rebellious = 0
    $ understanding = 0
    $ gender = ""
    $ chosendrink = ""
    $ wentWithGregg = ""
    $ confectionChoice = "treat"
    $ loriInteractionRude = False
    $ loriInteractionNull = False
    $ loriInteractionBold = False
    $ loriInteractionNotBold = False
    $ loriInteractionNeutral = False
    $ firstWander = True
    $ audiencepoet = ""

    # Scene completion status
    $ beaSelmaPoetry = False
    $ maeLoriSleepover = False
    $ maeChurch1 = False
    $ maeLoriSleepoverCompleted = False

    scene bg black with fade
    
    # Day 1

    $ renpy.music.set_volume(.7, 0, channel='music')

    "Your heart begins to race as you hear a low rumbling in the distance."

    #background music, crows cawing, cars in distance, wind, etc

    scene bg hometown_bus_station with fade

    play music "music/Ecitara.mp3" fadein 1.0

    "You impatiently turn your head in the direction of the sound, praying it was your salvation."
    "You wait, perked up like a guard dog."
    "..."
    "Nope, another false alarm. Just another random car heading who knows where."
    "You sigh and recline against the backrest of the uncomfortable bench."
    "You still felt so tense. You need to ease up. Relax."
    "It's a clear day out. The crows are cawing, the air is pleasantly cool, and best of all you're getting the hell away from here soon."
    "All in all it's a good afternoon to wait for a bus."
    "You take a quick glance down at your bags to make sure they hadn't been stolen, then pull out your phone to check the time."
    "1:34."
    "The bus is scheduled to arrive at 2:00, but you had been waiting here for hours."
    "It felt awkward hanging around for so long but you'd rather be here than in the proximity of your overbearing mother any longer."
    "Luckily nobody was around to witness your antsy fidgeting."
    "Finals are ending but most folk around here have a slightly fancier ride home than a public bus."
    "It may be calm today but it'll get a lot more hectic once the college kids start rolling in, just like it does every break."
    "Honestly you couldn't stand it anymore."
    "Ever since you had drifted apart from your friends, you'd grown bitter toward the noise and crowds and fun everyone else was having."
    "Apparently Possum Springs doesn't have this problem. If anything, it's said to be pretty dull."
    "In fact, the house you've inherited there appears to be rather secluded. It's way out in the woods away from everything."
    "It would have been nice to visit it sometime before your father died, but Mom forbade it."
    "At least the old man was decent enough to let you have it."
    "Getting it legally sorted out was a pain, but in the end you're entitled to that house, just like it says in his will."
    "Once you had raised enough money to live comfortably for a while, you packed your bags and left home without so much as a goodbye."
    "And that's why you're sitting here right now."
    "Alone."

    scene bg hometown_bus_station_bus with dissolve

    "As you reflect on your current life situation, you somehow miss the warning signs of the bus's approach and are caught off guard by its sudden appearance in front of you."
    "The roaring engine, faded paint, and peeling seats were anything but inviting, but to you this was your chariot to a better life."
    "A few people in their late teens and early 20's step off the bus, all of them with backpacks."
    "These must be the lucky few who could finish their finals early."
    "Either that or they decided to drop out at the last possible minute."
    "Judging by their upbeat attitudes, it's probably the former."
    "You watch as they crowd around the luggage compartment, the driver having to squeeze past to unlock it."
    "Then comes an eternity of students sorting out their suitcases."
    "Eventually, all but you and the driver disperse."
    "You stand with your ticket in hand and make eye contact with him. He just nods his head toward the luggage compartment."
    "Without a word, you stuff your bags inside then board the bus, sitting down somewhere in the middle section."

    scene bg bus_interior1 with dissolve

    "There are more college-aged people inside and a few older ones too, but it's empty enough that you can have a spot at least a couple spaces away from anyone else."
    "You idly stare out the window. Hopefully this'll be the last time you see this place."
    "You aren't scheduled to get to Possum Springs until 6:30, so you might as well get a head-start on some much needed sleep."
    "Normally on a trip like this you'd listen to some music, but the mental stress of the day has made you unwilling to fish out the inevitably tangled earphones from your pocket."
    "You simply lean back and close your eyes, and before you know it you're in dreamland."

    stop music fadeout 2.0

    scene bg black with fade
    scene bg dream1 with fade

    # Transition into a dreary, dark landscape made of cloud like shapes
    #low booms bg music, like in nitw dreams, low rumbling thunder when guardian speaks

    "..."
    "It's dark."
    "Very dark."
    "Your eyes can hardly give you any information beyond silhouettes on the horizon against a moonless, starry sky."
    "The ground beneath you is soft."
    "Is it... moving?"
    "It's hard to tell if it is or if it's just an illusion as your mind tries to piece together what little you can see."
    "No wind or background noise either, like you're standing in space."
    "How long have you been here?"
    "It feels as though you've just arrived... but at the same time like this is where you've always existed."
    "Wait, were you walking before?"
    "You certainly are now."
    "Where to is anyone's guess."

    #pause with soft footsteps sfx

    "..."
    "An ambiguous amount of time passes as you advance."
    "Your surroundings seem to shift into impossible shapes, counter-intuitive to the geometric space you innately understand."
    "At some point, a structure that appeared to be infinitely distant comes to abruptly envelop nearly your entire field of vision."

    scene bg dream2 with dissolve

    play music "/music/theguardian.mp3" fadein 1.0

    "You stop and take a moment to look it over from top to bottom, but it would seem this thing has no top, at least not one within your comprehension."
    "Suddenly a thunderous voice calls out from within the tower, shaking the very ground you stand upon."

    #rolling thunder sfx
    guardian "Who goes there?"

    menu:
        guardian "{cps=0}Who goes there?{/cps}"
        "I-I'm… uh...":
            $ timid = timid + 1
            $ player = Character("[povname]")
            "Before you can answer, the guardian interrupts you."
            guardian "State the name your mother gave you."
            jump namescript1
            label namescript1:

                python:
                    povname = renpy.input("What is the name your mother gave you?", length = 14)
                    povname = povname.strip()
                    if povname.upper() == "HITLER":
                        povname = "Unoriginal"
                    if povname.upper() == "MAE":
                        povname = "MAE"
                    if povname.upper() == "BEA":
                        povname = "BEA"
                    if povname.upper() == "GREGG":
                        povname = "GREGG"
                    if povname.upper() == "ANGUS":
                        povname = "ANGUS"
                    if povname.upper() == "GERM":
                        povname = "GERM"
                    if povname.upper() == "LORI":
                        povname = "LORI"
                    if povname.upper() == "SELMA":
                        povname = "SELMA"
                    if povname.upper() == "SELMERS":
                        povname = "SELMERS"
                    if not povname:
                        povname = "Alex"
                    "The name given to you is [povname]?"
                if povname == "MAE":
                    "Choose another name."
                    jump namescript1
                if povname == "BEA":
                    "Choose another name."
                    jump namescript1
                if povname == "GREGG":
                    "Choose another name."
                    jump namescript1
                if povname == "ANGUS":
                    "Choose another name."
                    jump namescript1
                if povname == "GERM":
                    "Choose another name."
                    jump namescript1
                if povname == "LORI":
                    "Choose another name."
                    jump namescript1
                if povname == "SELMERS":
                    "Choose another name."
                    jump namescript1
                if povname == "SELMA":
                    "Choose another name."
                    jump namescript1
                menu:
                    "{cps=0}Your name is [povname]?{/cps}"
                    "That's right.":
                        player "I-I'm… uh… [povname], sir. Can you please tell me where I am?"
                    "That's wrong.":
                        jump namescript1

            "The booming voice speaks out again."

            guardian "You are nowhere. You do not possess an existence, and as such you cannot occupy a meaningful space to call your location."

            player "Oh... I see. I guess."

            "That's not really a satisfying answer, but what can you do?"
            "You dwell on how to proceed until the voice derails your train of thought."

            guardian "However, circumstances have aligned to allow you a chance to exist."
            guardian "The domain before you holds that which can be called true. Step forth if you wish to be judged for your worthiness to enter."

            player "O-ok..."

            "You cautiously inch forward, not sure of the spatial relation between you and the tower."

            guardian "Halt."

            "You stop in your tracks and anxiously await the guardian's next command."

            guardian "Are you ready?"

            "You mentally prepare yourself and nod."

        "My name is...":
            $ bold = bold + 1
            $ player = Character("[povname]")
            "Before you can answer, the guardian interrupts you."
            guardian "State the name your mother gave you."
            jump namescript2
            label namescript2:

                python:
                    povname = renpy.input("What is the name your mother gave you?", length = 14)
                    povname = povname.strip()
                    if povname.upper() == "HITLER":
                        povname = "Unoriginal"
                    if povname.upper() == "MAE":
                        povname = "MAE"
                    if povname.upper() == "BEA":
                        povname = "BEA"
                    if povname.upper() == "GREGG":
                        povname = "GREGG"
                    if povname.upper() == "ANGUS":
                        povname = "ANGUS"
                    if povname.upper() == "GERM":
                        povname = "GERM"
                    if povname.upper() == "LORI":
                        povname = "LORI"
                    if povname.upper() == "SELMA":
                        povname = "SELMA"
                    if povname.upper() == "SELMERS":
                        povname = "SELMERS"
                    if not povname:
                        povname = "Alex"
                    "The name given to you is [povname]?"
                if povname == "MAE":
                    "Choose another name."
                    jump namescript2
                if povname == "BEA":
                    "Choose another name."
                    jump namescript2
                if povname == "GREGG":
                    "Choose another name."
                    jump namescript2
                if povname == "ANGUS":
                    "Choose another name."
                    jump namescript2
                if povname == "GERM":
                    "Choose another name."
                    jump namescript2
                if povname == "LORI":
                    "Choose another name."
                    jump namescript2
                if povname == "SELMERS":
                    "Choose another name."
                    jump namescript2
                if povname == "SELMA":
                    "Choose another name."
                    jump namescript2
                menu:
                    "{cps=0}Your name is [povname]?{/cps}"
                    "That's right.":
                        player "My name is [povname]. What is this place?"
                    "That's wrong.":
                        jump namescript2

            
            "The booming voice speaks out again."

            guardian "You are nowhere. You do not possess an existence, and as such you cannot occupy a meaningful space to call your location."

            "You look down at your body, holding your arms out then shrugging."

            player "I can't be nowhere if I'm right here."

            guardian "Believe what you will, it does not change reality."

            "You're getting annoyed. You become more confrontational in your tone."

            player "Then just what am I supposed to do?"

            guardian "It matters not what you do. You represent a mere chance of existence that has not come to fruition."
            guardian "However, the domain before you holds that which can be called true. Step forward if you wish to be judged for your worthiness to enter."

            "You give it some thought, taking a moment to cool down. You might as well, since there's apparently nothing else for you to do."

            player "Sure, why not?"

            "You saunter up a few feet, looking around."
            "The voice didn't exactly tell you where to go and any point of reference is as unreliable as his answers."

            guardian "Halt."

            "You come to a stop."
            "It doesn't look like you've moved an inch from where you were."

            guardian "Are you ready?"

            player "Yeah, I guess."
            
        "Tell me who you are first.":
            $ inquisitive = inquisitive + 1

            "Before you can speak, the booming voice speaks out again."

            guardian "Who I am is not your concern. I ask again, who goes there?"
            guardian "State the name your mother gave you."

            $ player = Character("[povname]")
            jump namescript3
            label namescript3:

                python:
                    povname = renpy.input("What is the name your mother gave you?", length = 14)
                    povname = povname.strip()
                    if povname.upper() == "HITLER":
                        povname = "Unoriginal"
                    if povname.upper() == "MAE":
                        povname = "MAE"
                    if povname.upper() == "BEA":
                        povname = "BEA"
                    if povname.upper() == "GREGG":
                        povname = "GREGG"
                    if povname.upper() == "ANGUS":
                        povname = "ANGUS"
                    if povname.upper() == "GERM":
                        povname = "GERM"
                    if povname.upper() == "LORI":
                        povname = "LORI"
                    if povname.upper() == "SELMA":
                        povname = "SELMA"
                    if povname.upper() == "SELMERS":
                        povname = "SELMERS"
                    if not povname:
                        povname = "Alex"
                    "The name given to you is [povname]?"
                if povname == "MAE":
                    "Choose another name."
                    jump namescript3
                if povname == "BEA":
                    "Choose another name."
                    jump namescript3
                if povname == "GREGG":
                    "Choose another name."
                    jump namescript3
                if povname == "ANGUS":
                    "Choose another name."
                    jump namescript3
                if povname == "GERM":
                    "Choose another name."
                    jump namescript3
                if povname == "LORI":
                    "Choose another name."
                    jump namescript3
                if povname == "SELMERS":
                    "Choose another name."
                    jump namescript3
                if povname == "SELMA":
                    "Choose another name."
                    jump namescript3
                menu:
                    "{cps=0}Your name is [povname]?{/cps}"
                    "That's right.":
                        player "It's [povname]. Now could you please explain what this place is?"
                    "That's wrong.":
                        jump namescript3

            guardian "I cannot. The place in which you reside does not exist and neither do you."

            player "I don't exist? Then how can I be here?"

            guardian "\"Here\" has no meaning relative to your location."

            player "Why am I... nowhere then?"

            guardian "You represent a mere chance of existence, something that only exists in the realm of hypotheticals."
            guardian "The domain before you holds that which can be called true. Step forth if you wish to be judged for your worthiness to enter."

            "You stare up at the tower, contemplating for a bit before doing as the voice told."

            guardian "Are you ready?"

            player "I think so."

    "A bright blue light descends from above and blankets you."
    "Its intensity blinds you to your surroundings, yet is not painful."
    "After some time, the glow fades, receding back into its lair above."

    guardian "I have looked into your soul and have determined you are not worthy. Now leave this place at once."

    menu:
        guardian "{cps=0}I have looked into your soul and have determined you are not worthy. Now leave this place at once.{/cps}"
        "Figures.":
            $ cynical = cynical + 1
            player "Figures."

            "You scoff and dejectedly turn away."

            player "Didn't wanna join your stupid club anyway."

            "You say with a mocking tone."

            stop music fadeout 2.0

            "As you sulk, the tower retracts into nothingness, as if it was never there."

        "Now wait just a second...":
            $ rebellious = rebellious + 1
            player "Now hold on just a second, what do you mean I'm not worthy? How do you know?"

            guardian "Leave this place at once or you will be removed."

            player "\"Leave this place?\" How can I leave a place that doesn't exist?"

            "*Silence.*"

            player "Answer me!"

            "You stomp forward, directing your angry expression at whatever lies ahead."

            stop music fadeout 2.0

            "You believe you're marching deeper into the tower until you realize it has completely vanished from sight, as if it was never there."

        "I understand.":
            $ understanding = understanding + 1
            player "I understand. Thanks anyway."

            "The guardian doesn't respond."
            "You look down, a little disappointed, then turn away."

            stop music fadeout 2.0

            "After a few steps you look over your shoulder to find the tower has vanished, as if it was never there."


    play music "music/Stalked.mp3" fadein .5

    scene bg dream1 with dissolve

    "You continue through the void until a distant rhythm reaches your eardrums."
    "It sounds like some sort of tribal chanting, held together by a thumping beat."
    "You're unable to pinpoint where exactly it's coming from. It's like it's hitting you from every direction."
    "It starts to drill into your mind, blocking out any other thought."
    "More unusual instruments are thrown into the mix, producing guttural clicking, grotesque hisses, and harsh industrial noises."
    "Soon your surroundings begin to unfurl and transform into something else, something sinister."
    "Amorphous shapes ensnare and constrict your body, squeezing the air from your lungs. Any attempts at resisting are met with your body failing to respond."
    "You're paralyzed. There's nothing you can do."
    "Your heart beats like it's trying to burst out of your chest and escape this hellish imprisonment on its own."
    "Before you know it, your vision is snuffed out from the suffocation but the cantations blare against your eardrums louder and louder."
    "You're helpless to stop your mind from being consumed by the uproar."
    #pause for a second

    stop music fadeout 2.0

    "Suddenly the pressure relinquishes and the pain in your ears is gone. You instinctively take a deep breath and open your eyes wide."

    #flash white, fade to bg bus2
    scene bg bus_interior2 with dissolve
    "You're back on the bus."

    "Your eyes dart all over the place, forming a report to give to your brain."
    "It's night time now, you're riding through the woods, and there are some new people on board."
    "You exhale and sink into your seat. Better check the time on your phone."

    "..."

    "No messages but at least you didn't miss your stop."
    "It's only 6:15, though it's already pitch black outside."

    $ renpy.music.set_volume(.15, 0, channel='music')
    play music "music/deathterrors_loop.mp3" fadein 2.0

    "After pocketing the device, your attention is brought to a ghastly melody coming from nearby."
    "Sitting a couple seats ahead of you is a small mouse girl with wires leading up to her ears."
    "She taps on her phone, then returns to writing something in the journal in her lap."
    "You can hear her music leaking from her earphones loud and clear from here."
    "Her taste in music is rather... unusual. You pick up on some haunting wails and chilling organ keystrokes coming through."
    "Hey, that must be where the sound in your dream was coming from!"

    menu:
        "{cps=0}What should you do?{/cps}"
        "Ask her what she's listening to.":
            $ loriAP = loriAP + 1
            "You'd love to give those spooky refrains a try once you're home. You decide to ask her what she's listening to before she slips away, never to be seen again."

            if bold >= 1:
                $ loriInteractionBold = True
                "You casually stroll up and plop down in the empty seat next to her. She doesn't seem to have taken notice of you yet."

                show lori neutral at right with dissolve:
                    yalign loriheight


                "You lean in and clear your throat, a bit louder than you need to."

                #show scared lori sprite
                show lori breath

                "The mouse glances up from her journal and nearly jumps out of her seat."
                "In a flash, she clutches her notebook and scrambles away from you until her back is pressed against the window."
                "The poor thing's rapidly breathing in and out as she watches you with fear in her eyes."
                "You hold your hands up to show you meant no harm."

                player "Whoa, didn't mean to startle you."

                "Easing back into her seat, she takes her earphones out and makes a concentrated effort to slow her breathing."

                loriunknown "Oh goodness, you scared me! Hah hah... hah..."

                "You chuckle lightheartedly."

                player "I guess that makes us even. Pretty cool music by the way."

                show lori neutral

                "The girl looks confused for a moment then realizes her earphones still playing and are audible from a distance."

                loriunknown "Oh gosh, you could hear that? I'm so sorry!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone in a panicked, embarrassed fashion."

                loriunknown "*Huff huff*"

                player "No, it's fine. Actually I wanted to get the name of it before one of us got off the bus."

                "You confidently smile as you reassure her. She looks at you like you're crazy for a second then smiles back, scooting closer to you."

                loriunknown "Well uh, it's called Deathterrors. The album, that is. It's by Kerosinners."

                player "Nice. I'll check it out once I get to my place."

                "She seems excited to talk more about it, but the bus driver cuts your conversation short as he announces you'll be arriving in Possum Springs momentarily."

                loriunknown "Oop, that's my stop!"

                player "Really? It's mine too!"

                loriunknown "No way! No one else ever gets off at Possum Springs!"

                player "Yeah, I'm moving in today."

                loriunknown "Cool! Maybe I'll see you around town later...Whoops!"

                "She reaches down to grab her pen that had just rolled off her notebook, but you get to it first and hand it back."

                loriunknown "Hah, thanks! Guess I better pack up before our stop, huh?"

                player "Yeah, that might be a good idea haha."

                hide lori with dissolve

                "While she gathers her things and stuffs them in her backpack, you take a look outside."
                "The forest has opened up into a hilly countryside. Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness."
                "A short time later, the bus pulls up to an abandoned-looking station and stops by an empty bench."
                "The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

                #this is supposed to be an exterior background but we didn't have one available :/
                scene bg ps_bus_station_night with dissolve

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "Your eyes meet at one point and you exchange friendly smiles and subtle nods."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."

                show lori neutral at right with dissolve:
                    yalign loriheight

                loriunknown "See you around!"

                "You look up to see the mouse waving goodbye to you with her free hand as she totes her suitcase to a car that had just pulled up to the curb."
                "You take a break from pulling your bags out to wave back."

                player "See ya!"

                "You're rewarded with a wide grin before she runs into the arms of the black-furred cat who had just stepped out of the vehicle, giggling and embracing her fondly."

                show mae neutral flip at left with dissolve

                # hug scene

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes Lori's luggage and hoists it into the trunk of her car, but the mouse chooses to hold onto her backpack."

                lori "Hang on, I wanna keep my notebook close by."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                hide lori
                hide mae
                with dissolve

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver wordlessly closes the compartment and locks it, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


            elif timid >= 1:
                $ loriInteractionNotBold = True
                "You quickly scurry up to the empty seat beside the girl and flash her a nervous smile. It takes a few seconds for her to notice you."

                show lori neutral at right with dissolve:
                    yalign loriheight

                loriunknown "Hm?"

                "She takes out her earphones and faces you with a somewhat confused look."

                player "Hey. Um..."

                "Your hand does a meager wave on its own then goes to anxiously grip your upper arm on the opposite side."

                loriunknown "Oh, hey? Can I help you?"

                player "Uh, I was just wondering what you were listening to."

                "The mouse girl glances down at her earphones, the little speakers still playing music, then looks back up to you with a panicked and embarrassed expression."

                loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone, breathing kinda heavily."

                loriunknown "*Huff huff*"

                player "N-no, it's fine. It sounds pretty neat actually. I was hoping you could tell me the name of it."

                "The mouse calms down a bit, reassured that she wasn't bothering you."

                loriunknown "Well uh, it's called Deathterrors. The album, that is. It's by Kerosinners."

                player "Thanks! I'll be sure to check them out!"

                "She seems happy to talk more about it, but the bus driver cuts your conversation short as he announces you'll be arriving in Possum Springs momentarily."

                loriunknown "Oop, that's my stop!"

                "She unplugs her earphones and closes her journal, then stuffs them into her bag."
                "You decide to just give her a polite nod and leave her be."

                hide lori with dissolve

                "You turn your attention to the window and look out to the countryside. Hills, a train track, a factory, and more hills. So this is Possum Springs, huh? It's quite... plain."

                "A short time later, the bus pulls up to an abandoned-looking station and stops by a bench but there's no one there waiting to board."
                "The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

                scene bg ps_bus_station_night with dissolve

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "Your eyes meet at one point and you exchange friendly smiles and subtle nods."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."

                show lori neutral at right with dissolve:
                    yalign loriheight

                "Out of the corner of your eye, you can see her check her phone, then excitedly run up to a car as it pulls up to the curb."

                show mae neutral flip at left with dissolve

                maeunknown "Lori!"

                lori "Mae!"

                # show maeLoriHug

                "A black-furred cat steps out to happily greet the mouse and give her a nice big hug."

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                hide lori
                hide mae
                with dissolve

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "As they drive away, you can see Lori looking at you through the window with a concerned look."
                "Is she worried about you being out here alone?"
                "You shrug it off and drag your things away from the bus. One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The driver wordlessly shuts the compartment and locks it then returns to the helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


            elif inquisitive >= 1:
                $ loriInteractionNotBold = True
                "Moving up to the empty seat beside her, you can't help but take a peak at what she's writing in her notebook."
                "It's hard to read from this angle but it looks to be a story, with horrific doodles in the margins."
                "Jagged-toothed monsters, devilish demons, intestines spilling out of the innocent..."
                "She catches you eavesdropping and takes out her earphones with a confused expression."

                show lori neutral at right with dissolve:
                    yalign loriheight

                loriunknown "Uh, hey? Can I help you?"

                "You snap your eyes away from her notebook and clear your throat."

                player "Pardon me, I was just wondering what you're listening to."

                "The mouse girl glances down at her earphones, the little speakers still playing music, then looks back up to you with a panicked and embarrassed expression."

                loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone, breathing kinda heavily."

                loriunknown "*Huff huff*"

                player "It's fine, I think it sounds really cool. What genre is that?"

                loriunknown "Well uh, the album is called Deathterrors by Kerosinners... and I guess you could call it a noise opera maybe??"

                player "Noise opera huh? What's the story behind it?"

                "She perks up and scoots closer to you, taking in a deep breath before giving a long winded but enthusiastic explanation."

                loriunknown "Ok so like, there's this wandering demon who invades people's dreams and it seems like he's haunting a bunch of villagers"
                loriunknown "but he's really just trying to learn emotions and how to feel and stuff, and so he's basically being raised on the nightmares people are having because of him-"
                loriunknown "Oh right, and the dreams turn into nightmares when he goes into them-"
                loriunknown "Anyway, he thinks that fear and terror is all there is in the world so he gets really good at scaring people"
                loriunknown "so then the village is trying to get rid of the demon with some ancient ritual and he sees this as a challenge and like an invitation to escalate to violence"
                loriunknown "And uh, yeah."

                player "Wow. That sure is... something. How'd you get into that kinda stuff?"

                loriunknown "Browsing obscure parts of the internet mostly."

                "She seems eager to talk more, but the bus driver cuts your conversation short as he announces you'll be arriving in Possum Springs momentarily."

                loriunknown "Oop, that's my stop! But yeah you should totally check out the rest of their albums!"

                player "Yeah, totally!"

                "She unplugs her earphones and closes her journal, then stuffs them into her bag."
                "You decide to just give her a polite nod and leave her be as she packs her stuff."

                hide lori with dissolve

                "You turn your attention to the window and look out to the countryside. Hills, a train track, a factory, and more hills. So this is Possum Springs, huh? It's quite... plain."
                "A short time later, the bus pulls up to an abandoned-looking station and stops by an empty bench."
                "The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

                scene bg ps_bus_station_night with dissolve

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "At one point, your eyes meet and you exchange friendly smiles and subtle nods."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."

                loriunknown "See you around!"

                "You look up to see the mouse waving goodbye to you with her free hand as she totes her suitcase to a car that had just pulled up to the curb."
                "You take a break from pulling your bags out to wave back."

                player "See ya!"

                "You're rewarded with a wide grin before she runs into the arms of the black-furred cat who had just stepped out of the vehicle, giggling and embracing her fondly."

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver comes and locks the compartment, then wordlessly returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."




        "Ask her to turn it down.":
            $ loriAP = loriAP - 1
            

            "You don't wanna hear any more of that creepy music, and you're sure everyone else on the bus will silently thank you for asking her to turn it down."
            "You move up to the empty seat beside hers and face her."

            show lori neutral at right with dissolve:
                yalign loriheight

            player "Excuse me."

            if understanding >= 1:
                $ loriInteractionNeutral = True
                $ loriAP = loriAP + 1

                show lori anxious3 flip

                "She jumps a little when she notices you, dropping her pen on the floor."
                "You reach down to grab it before she can react and hold it out for her."
                "Her movement is kinda jittery and she's breathing heavily."

                loriunknown "Huff huff... Thanks. Um, did you need something?"

                player "Oh, right. I came to ask if you would please turn down the volume."

                "The mouse girl glances down at her earphones then back up to you with a panicked, embarrassed expression."

                loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone."

                loriunknown "*Huff huff...*"

                player "No worries. I would have slept past my stop if it hadn't woken me up!"

                "You smile reassuringly and get a dainty grin in return."

                show lori neutral

                "She looks like she's about to say something when the driver cuts your conversation short, announcing you'll be arriving in Possum Springs momentarily."

                loriunknown "Oop, that's my stop!"

                "She unplugs her earphones and closes her journal, then stuffs them into her bag. You decide to just give her a friendly nod and leave her be."
                "You turn your attention to the window and look out to the countryside."
                "Hills, a train track, a factory, and more hills. So this is Possum Springs, huh? It's quite... plain."
                "A short time later, the bus pulls up to an abandoned-looking station and stops by an empty bench."
                "The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

                scene bg ps_bus_station_night with dissolve

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "Your eyes meet at one point and you exchange smiles and subtle nods."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "The driver takes his sweet time before waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the mouse to retrieve her bags, then reach in to dig out your own stuff."
                "Out of the corner of your eye, you can see her check her phone, then excitedly run up to a car as it pulls up to the curb."
                "A black-furred cat steps out to happily greet her and give her a nice big hug."

                show lori neutral at right:
                    yalign loriheight
                show mae neutral flip at left:
                    yalign maeheight
                with dissolve

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back home!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."

                hide mae
                hide lori
                with dissolve

                "As they drive away, you can see Lori looking at you through the window with a concerned look."
                "Is she worried about you being out here alone?"
                "You shrug it off and drag your things away from the bus. One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The driver wordlessly shuts the compartment and locks it then returns to the helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."

            else:
                $ loriInteractionRude = True
                $ cynical = cynical + 1

                show lori anxious3:
                    yalign loriheight

                "She jumps a little when she notices you, knocking her pen to the floor."
                "She hastily picks it back up then takes out her earphones. Her movement is kinda jittery and she's breathing heavily."

                show lori breath

                loriunknown "Um, hey? Huff huff... Did you need something?"

                "You point to her earphones lying on her journal, the little speakers still making noise."

                player "Would you mind turning that down?"

                "She glances down at her earphones then back up to you with a panicked, embarrassed expression."

                loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone."

                loriunknown "Huff huff... Huff huff..."

                player "Appreciate it."

                hide lori with dissolve

                "With that out of the way, you decide to look out the window and admire the countryside."
                "Hills, a train track, a factory, and more hills. So this is it, huh? It's quite... plain."
                "The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
                "The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "The mouse girl hurriedly stands up and starts walking toward the exit, looking a bit distressed."
                "Is she angry because you asked her to turn down her music?"
                "Regardless, you check your pockets to make sure you got everything and head out yourself."

                scene bg ps_bus_station_night with dissolve

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and that girl waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "She avoids eye contact with you."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for the mouse to go first, you patiently wait for her to retrieve her bags, then reach in to dig out your own stuff."
                "Out of the corner of your eye, you can see her walk up to a car as it pulls up to the curb."
                "A black-furred cat steps out to happily greet her with a nice big hug."

                show lori neutral at right:
                    yalign loriheight
                show mae neutral flip at left
                with dissolve

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                hide lori
                hide mae
                with dissolve

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver comes and locks the compartment, then wordlessly returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


        "Move away from her.":
            $ loriInteractionNull = True
            $ cynical = cynical + 1

            "You don't wanna bother her. You'll be off this bus soon anyway."
            "You move over to a seat further away from her and take a look out the window, losing yourself in thought."
            "The forest has opened up into a hilly countryside."
            "Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness. So this is it huh? It seem so... plain."
            "The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
            "The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
            "It looks like a ghost town."
            "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
            "The mouse girl stands up and walks toward the exit before you do. You wonder if she lives here."
            "Seems she's the only one besides yourself getting off at this stop. You check your pockets to make sure you got everything and head out yourself."

            stop music fadeout 2.0

            scene bg ps_bus_station_night with dissolve

            "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
            "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
            "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
            "Your eyes meet at one point and you exchange friendly smiles and subtle nods."
            "She still has her earphones in, and you can overhear all the cries and moans and screams that she doesn't seem to mind at all."

            # brief pause

            "Jeez, how long is the driver gonna make you wait?"
            "He takes his sweet time before finally waddling out and unlocking the storage door."
            "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."
            "Out of the corner of your eye, you can see her remove her earphones then excitedly run up to a car as it pulls up to the curb."
            "A black-furred cat steps out to happily greet the mouse and give her a nice big hug."

            show lori neutral at right:
                yalign loriheight
            show mae neutral flip at left:
                yalign maeheight
            with dissolve

            maeunknown "Lori!"

            lori "Mae!"

            "Welcome back to Possum Springs!"

            lori "Haha it's good to be back!"

            mae "Glad to see you again! Here, lemme get those for you."

            "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

            lori "Hang on, wanna keep my notebook close."

            mae "Gotchya. Ready to go?"

            lori "Yeah!"

            "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."

            hide mae
            hide lori
            with dissolve

            "The car revs to life and begins to drive away as you drag your things from the bus."
            "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
            "The bus driver comes and wordlessly locks the compartment, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


    $ renpy.music.set_volume(0.7, 0, channel='music')

    "Once the bus is out of sight, you take a look around and consider your options."
    "You really don't have any other than to walk to your dad's old house. You memorized an online map beforehand so you're pretty sure of how to get there."
    "Thankfully it's not too far away. You can see lights coming from a residential area through some leafless trees up ahead. That's the direction you need to go."
    "Putting one foot in front of the other, you set out along the path with your suitcases rolling behind you."

    # brief pause

    "The orange lights hum softly above as wind echoes throughout the hills. Occasionally you hear dogs bark in the distance and cars speeding down the highway."
    "These background sounds blend together to compose an ambient melody for wayfarers like yourself, reminding you of your forsakenness."
    "You're on your own now and in unfamiliar territory. Your fate is entirely in your own hands."
    "Before long you come to the end of the sidewalk."
    "A faded trail leads into the woods, but it doesn't look like it goes very far before it terminates in a sudden drop off."
    "It might actually be faster to go down that way if you weren't hindered by all these clunky packs."
    "*Sigh*"
    "You'll just have to go the long way around."

    scene bg ps_roads1_night with dissolve

    "Unfortunately that means traversing the winding road both uphill and down."
    "It's an arduous journey, and the creepy scenery does no favors to your sanity."
    "You feel like you're being watched and you swear you hear footsteps behind you every now and then."
    "After passing by the decaying remains of some old playground enclosed in chainlink fences and \"DO NOT CROSS\" tape, you reach civilization and decide to take a breather."
    "Panting softly, you sit on one of your suitcases and gaze at the seemingly endless road ahead."
    "Why the hell did they build the bus station so far away from anything?"
    "You check your phone, knowing full well there'd be no new notifications and are shocked to find you're hardly getting any service."
    "Are the radio towers here just for show?"
    "You doubt it's going to get any better when you're at the bottom of this next hill."
    "Might as well get this over with. You hop back on your feet and descend the slope in front of you. Sure enough your phone signal drops to zero as the hills close in around you." 
    "You're cold, exhausted, and cut off from the rest of the world, but home is not much further away now."
    "You turn onto an old road and pass over a set of train tracks. To your dismay, streetlights are absent for this stretch. The same goes for sidewalks."
    "Luckily, your destination should reveal itself any minute now."
    "..."
    "Were you supposed to keep left at that fork? Mild panic starts to set in as you second guess yourself."
    "Unease turns into relief, however, when you spot a mailbox adjacent to an opening in the trees."
    "You flash your phone light on it and read the numbers on it, muttering the address to yourself."

    player "163 Cedar Road. This is it."

    "You shine your light into the thicket, illuminating the trail leading to your house. You have another incline to ascend, but this one isn't so bad."
    "Branches and weeds litter the walkway, jostling your bags as you wander deeper into the woods."
    "After more twists and turns than you can be bothered to count, the path opens up into a spacious yard ending in a large and luxurious house."

    scene bg home_exterior_night with dissolve

    play music "music/welcomestranger_loop.mp3" fadein 1.0

    "Maybe it's just the relief of finally arriving here, but the sight is really quite breathtaking."
    "You made it. This is your new home."
    "You climb up the short stairway leading up to the front door and slump against it while digging out your keys."
    "The handle is really stiff, probably from the lack of use over the years, but you manage to twist it with enough force."

    scene bg home_interior_night with dissolve

    "Stumbling inside, you drop off your bags and close the door with a sigh."
    "...You can still see your breath."
    "Dammit."
    "It's just as cold in here as it is outside."
    "Ok just need to turn on the heat, then you can get some rest."

    player "Really hope the power company turned on the electricity..."

    "You mutter to yourself as you fumble around for the lights. You had called them a couple weeks ago, along with some other people to prepare the place for moving in."
    "Your fingers locate a switch that blinds you after your tired eyes had been adjusted to the dark for so long."
    "Looks like the house is fully furnished, just as your father had left it."
    "You find the thermostat and set it to a comfortably toasty temperature, then poke your head inside doorways at random until you come across a bedroom."

    scene bg home_bedroom_night with dissolve

    "The linens appear clean and are neatly made, inviting your to flop down onto the bed."
    "You lie there with your eyes closed for a while before kicking off your shoes and wrapping yourself in the covers."
    "You don't bother setting an alarm, you're treating yourself to however much sleep your body decides tonight."

    player "Goodnight, me. Sweet dreams."

    "Those are your last thoughts before passing out."

    stop music fadeout 2.0

    #fade out





    # Day 2
    $ currentDate = "December 8"

    #fade in
    scene bg home_bedroom_night with fade

    "The first thing you notice as you rouse from slumber is the unfamiliar bed you've been lying in."
    "An unwelcoming mattress, someone's old sheets, and a thicker blanket than you're used to all make for an uncomfortable sleep, even if they are all much higher quality than your bed at home."
    "Your old home you mean."
    "Before you can ponder the implications of what it means to be \"home\", your attention is abruptly brought to your immense thirst."
    "Your throat feels scratchier than a wool sweater. When was the last time you drank something?"
    "Sometime before you boarded the bus yesterday you think."
    "Ugh. You know you're going to get a headache unless you drink something soon."
    "With a groan, you muster the will to unravel yourself from the covers and roll out of bed, dropping your phone onto the floor in the process."
    "God dammit."
    "Whatever. Recovering your phone will have to wait, quenching your thirst takes priority."
    "You leave the room in search of water, remembering you brought a couple bottles for your trip."
    "Rubbing your eyes and letting out a dry yawn, you head down the hall to the foyer where morning light pours in through the large windows."

    #scene bg foyer

    "Huh, it's way earlier than you were expecting."
    "Squinting through the brightness, you walk over to where you left your backpack and bend down to unzip it."
    "God, your legs are killing you from last night."
    "After some rummaging around, you agonizingly stand back up with a lukewarm bottle of water and chug nearly the whole thing in one go."

    player "Ahhh..."

    "That felt good."
    "It cleared your head a bit too."
    "The fact that you're in your dead father's house suddenly hits you in a profound way."
    "You can't remember the last time you saw him. You didn't get to see him much, really."
    "You wish you did. He was always nice and caring and understanding."
    "He knew how rough it was to be around Mom and sympathized with you, sending you cards and money pretty regularly."
    "To your knowledge, he never remarried. He had lived in this house alone for years."
    "And now it's yours."
    "And he's gone forever."
    "Probably."
    "His whereabouts were never discovered, but somehow you doubt he's been out partying on a yacht all these years."
    "At least it's a new start for you. You have all the freedom and dignity of a real adult now."
    "No more curfews, no more shouting matches, no more threat of having your property thrown out or burned again."
    "No more privacy invasions, having your money stolen, slaps to the face, or ridiculous rules, et cetera."
    "Gee, thanks for everything, Mom."
    "..."
    "She can go to Hell."
    "You finish off your water and another thought pops into your mind."
    "You also have adult responsibilities now. Like paying bills and buying food."
    "You already set up automatic payments for the bills, and you've got sufficient money in the bank for the time being."
    "But you're betting this house is severely lacking in the food department."
    "You should take a shower and get ready to go to the store. Wherever that is. Probably up a million hills."
    "*Sigh*"
    "It's going to be another tiresome day, isn't it?"
    "You toss the empty bottle back into your bag and proceed to move all your stuff into your new bedroom, taking the time to unpack a few things while looking for your phone charger."
    "It's gotta be in one of these bags somewhere..."
    "Ah, there it is. You plug it into a socket then retrieve your phone that had rolled under the bed and hook it up to the charger."
    "Just in time too! The battery was just about dead."
    "Still no notifications, which is understandable because there's still no signal."
    "Ok, you can't live like this forever, you need to at least get the wifi set up soon."
    "Not right now though. You have more pressing matters to tend to. You grab a change of clothes, then hunt for the bathroom."

    # scene bg bathroomfoggymirror
    scene bg home_bedroom_night with fade
    play music "music/Distant.mp3" fadein 1.0

    "Steam cascades throughout the room after a lengthy shower, fogging up the mirror."

    # scene bg bathroomclearmirror with dissolve

    "After getting dressed you take a look at yourself in the now clear reflection."
    "Your appearance is less of a wreck than yesterday. That's an improvement at least."
    "How would you describe yourself?"

    menu:
        "{cps=0}How would you describe yourself?{/cps}"
        "A masculine wreck":
            $ gender = "masculine"
            $ heshethey = "he"
            $ hishertheir = "his"
            $ hisherstheirs = "his"
            $ himherthem = "him"
            "Yeah, you lean on the masculine side."
        "A feminine wreck":
            $ gender = "feminine"
            $ heshethey = "she"
            $ hishertheir = "her"
            $ hisherstheirs = "hers"
            $ himherthem = "her"
            "You lean on the feminine side of course."
        "A gender neutral wreck":
            $ gender = "neutral"
            $ heshethey = "they"
            $ hishertheir = "their"
            $ hisherstheirs = "theirs"
            $ himherthem = "them"
            "It's hard to tell where you lie on the gender scale. Just the way you like it."

    "Whew, glad we got that identity crisis out of the way."
    "Come to think of it, you can make a new identity for yourself here. You don't even have to keep your old name."
    "Nobody here knows who you are. You can just make up a new one and nobody would know."
    "It's a new start and a new you, right?"

    menu:
        "{cps=0}It's a new start and a new you, right?{/cps}"
        "Keep old name":
            "Nah you're old name works fine, even if it was given to you by someone you hate."
            $ newname = povname
            jump day2scene2
        "Use a new name":
            jump newnamecreator

    label newnamecreator:
        "What shall your new name be?"

        python:
            newname = renpy.input("What shall your new name be?", length = 14)
            newname = newname.strip()
            if newname.upper() == "HITLER":
                newname = "Unoriginal"
            if newname.upper() == "MAE":
                newname = "MAE"
            if newname.upper() == "BEA":
                newname = "BEA"
            if newname.upper() == "GREGG":
                newname = "GREGG"
            if newname.upper() == "ANGUS":
                newname = "ANGUS"
            if newname.upper() == "GERM":
                newname = "GERM"
            if newname.upper() == "LORI":
                newname = "LORI"
            if newname.upper() == "SELMA":
                newname = "SELMA"
            if newname.upper() == "SELMERS":
                newname = "SELMERS"
            if not newname:
                newname = "Alex"
        if newname == "MAE":
            "Choose a different name."
            jump newnamecreator
        if newname == "BEA":
            "Choose a different name."
            jump newnamecreator
        if newname == "GREGG":
            "Choose a different name."
            jump newnamecreator
        if newname == "ANGUS":
            "Choose a different name."
            jump newnamecreator
        if newname == "GERM":
            "Choose a different name."
            jump newnamecreator
        if newname == "LORI":
            "Choose a different name."
            jump newnamecreator
        if newname == "SELMA":
            "Choose a different name."
            jump newnamecreator
        if newname == "SELMERS":
            "Choose a different name."
            jump newnamecreator
        if newname == povname:
            jump heyoldname
        else:
            "Your chosen name is [newname]?"
        menu:
            "{cps=0}Your chosen name is [newname]?{/cps}"
            "That's right.":
                "From now on, you will go by [newname]."
                $ player = Character("[newname]")
                jump day2scene2
            "That's wrong.":
                jump newnamecreator




    label heyoldname:
        "Hey, that's your old name! Do you want to just keep your old name?"
        menu:
            "{cps=0}Hey, that's your old name! Do you want to just keep your old name?{/cps}"
            "Keep old name":
                "You decide to just keep your old name."
                jump day2scene2
            "Come up with a new name":
                    jump newnamecreator


    label day2scene2:
        "Alright, you're ready to go to the grocery store. Just need to figure out where exactly that is first."

        # scene bg hallway

        "You pick up your phone step into the hallway, praying that the internet company had set up the network before you arrived."
        "A tap on the wifi icon shows that a connection is available but it's password protected."
        "Great."
        "The password is probably written on the router, which could be anywhere."
        "You wave your phone around, hoping to find the source of the wifi based on the signal strength it shows."

        scene bg home_office_day with dissolve

        "Your method eventually leads you to an office."
        "That's odd, the lamp is already on."
        "The soft glow illuminates the tidy room and all its furnishings."
        "Bookshelves that are crammed full of binders and publications line the walls, and behind the desk are framed diplomas."
        "Interestingly there's a safe built into one of the walls."
        "No way you're getting that open without the code. It doesn't seem to be lying around anywhere nearby so you continue your search for the more pertinent code."
        "The wifi code."
        "You follow the the wires coming out the back of the computer on the desk, which leads you straight to the router."
        "Jackpot!"
        "You read the password printed on the bottom and type it into your phone. A few seconds later it finishes authenticating and you're connected."
        "Finally. You search for \"possum springs grocery\" in your maps app and it returns a short list. The only two that are within walking distance are Snack Falcon and Ham Panther."
        "Snack Falcon is closer, but they won't have what you need. They're more of a convenience store."
        "Ham Panther it is."
        "It's all the way out by the highway. Maybe you should find someplace to stop and have breakfast first. You could go for a coffee too."
        "You consult the map for the nearest cafe and find a local place called \"Posspresso.\" It's a bit out of the way, but it'll have to do. You memorize the directions and head outside."

        stop music fadeout 2.0

        # scene bg outsidehouseday

        "It's a clear day out. The sunlight pleasantly warms your face, contrasting with the frigid air. Everything is still and quiet, as if time is frozen in place."
        "It's rather comforting actually. Just you and nature as far as the eye can see."
        "You close your eyes and enter a meditative trance. Sometimes being by yourself is nice."

        # pause followed by stomach growling sound effect

        "Your peaceful introspection is interrupted by your stomach growling. That's your cue to hurry up, you suppose."
        "You start down your driveway then head over the train tracks and toward town."

        scene bg roads_day with dissolve

        "The roads are strangely lonesome, even as you pass through neighborhoods. You haven't seen a single person yet."
        "You'd think the town really was abandoned if there weren't Longest Night decorations set up everywhere."
        "Up ahead you spot the cafe on the corner of some crossroads."
        "It doesn't look much different from an ordinary house apart from the wooden sign adjacent to that reads \"POSSPRESSO: Possum Springs' Favorite Cafe!\""
        "You can hear low fi hip hop leaking through as you come up to the entrance."

        show selma neutral flip at left with dissolve:
            yalign selmaheight

        "Out of the corner of your eye you notice a bear rounds the corner of the building and approaches the entryway."
        "She's wearing a pastel blue hoodie with a tiny heart in the corner and has a green messenger bag slung over her shoulder."
        "You speed up your walk and to get the door first, holding it open for her."

        selmaunknown "Thanks."

        player "No problem."

        "You give a subtle nod then follow her inside."

        hide selma with dissolve

        scene bg cafe with dissolve

        play music "music/americano_loop.mp3" fadein 1.0

        "The cafe is comprised of a single cozy room with rustic tables and chairs littered about and local artwork covering the walls."
        "Oddly enough, a large wooden picnic table takes up the center of the area."
        "On the back wall, a young bird lady with brick red feathers smiles and waves at you."

        #show cafebird
        #unfortunately we don't have a sprite for her yet

        trishunknown "Hi there! What can I get y'all?"

        "The barista chirps as you walk up to the counter."

        show selma neutral flip at left with dissolve:
            yalign selmaheight

        selmaunknown "Heya. One sec."

        "The ursine steps aside and faces you."

        selmaunknown "You go on ahead dude, you got here before I did."

        player "Nah, it's cool, you can go first. I need a minute to decide what I want."

        selmaunknown "Aight."

        "Despite being total strangers, the bear's tone is very friendly and informal. She seems really chill."
        "You hang back and stare at the items listed on the blackboard behind the bird while she takes the bear's order."

        selmaunknown "Hmm, I'm feelin' a salted caramel mocha today."

        "She doesn't even look at the menu before ordering. She must be a regular here."

        trishunknown "Want whipped cream on top?"

        selmaunknown "Hell yeah."

        trishunknown "Hahaha will that be all for you, Selmers?"

        selma "Uh huh."

        trishunknown "Alright, that'll be \$4.09!"

        "The bear pulls a bill out of her pocket and slides it over."

        selma "Keep the change."

        trishunknown "Thank you very much!"

        hide selma with dissolve

        "Selmers steps aside and the barista looks over to you."

        trishunknown "Ain't seen you around before!"
        trish "Welcome to Posspresso! You can call me Trish! It's short for Patricia!"
        trish "Have you decided what you'd like?"

        player "Yeah, I think so. I'll have uh..."

        menu:
            player "{cps=0}Yeah, I think so. I'll have uh...{/cps}"
            "Posspresso Special":
                $ chosendrink = "posspressospecial"
                player "I'll have the Posspresso Special and a plain bagel with cream cheese, please."

                trish "Oki doki!"

                "She punches your order into a tablet and reads out your total."

            "Latte":
                $ chosendrink = "latte"
                player "I'll have a latte and a blueberry bagel with honey butter spread, please."

                trish "Oki doki!"

                "She asks a few questions about how you want your drink, then punches your order into a tablet and reads out your total."

            "Cappuccino":
                $ chosendrink = "cappuccino"
                player "I'll have a cappuccino and a chocolate chip waffle, please."

                trish "Oki doki!"

                "She asks a few questions about how you want your drink, then punches your order into a tablet and reads out your total."
            "What she had":
                $ chosendrink = "mocha"
                player "I'll have what she had. And a strawberry waffle, please."

                trish "Oki doki!"

                "She asks a few questions about how you want your drink, then punches your order into a tablet and reads out your total."

        "Seeing that you've got your debit card ready, she slides the machine over to you. You swipe your card and hit confirm."

        trish "Alright, I'll have that out for y'all in just a minute!"

        "Selmers had already gone to find a table, where she's pulled a laptop from her bag and plugged it into a nearby socket."
        "You decide not to disturb her with small talk and instead find a table for yourself, choosing one by a window."
        "You stare outside for a bit then check your phone."
        "Still no cell signal. How do people live out here?"
        "You don't have enough battery to spare to play a game to pass the time, so you put your phone away and wait in boredom."
        "A few minutes pass, and the barista calls upon Selmers once her drink is done."

        trish "Selmers!"

        show selma neutral flip at left with dissolve:
            yalign selmaheight

        "She finishes typing something then goes up to the counter to collect her drink."

        selma "Thanks."

        "You casually look up and take note of the drink she got. It looks really good."
        "It's in a glass mug so you can see the thick chocolaty treat with a layer of froth topped by a generous helping of whipped cream with caramel sauce drizzled upon it."
        "You reluctantly go back to staring at nothing until your name is called out."

        hide selma with dissolve

        "..."
        trish "[povname]!"

        if newname == povname:
            "You wince, getting flashbacks to your mother angrily shouting your name."
            "You don't recall giving the barista your name though. She must have got it from your debit card."
        else:
            "You wince at hearing your old name, getting flashbacks to your mother angrily shouting it."
            "The barista must have read the name on your debit card since you didn't give it to her earlier. You should request a new one soon."

        if chosendrink == "posspressospecial":
            "You fetch your bagel and steaming hot coffee from the counter and head back to your seat by the wall. Your drink is in a glass mug as well."
            "It's a very dark concoction with a layer of light foam, topped with dark chocolate shavings."
            "You blow on it then take a sip."

            "..."

            "This is the most bitter thing you've ever tasted."
            "The flavor is earthy and potent with a burnt chocolate aftertaste."
            "It's an exceptionally strong drink that leaves you wanting more of it."
            "You can't resist taking another satisfying sip before moving on to your bagel."
            "Nothing special here, just an ordinary bagel with ample cream cheese stuffed between its halves."
        elif chosendrink == "latte":
            "You fetch your bagel and steaming hot coffee from the counter and head back to your seat by the wall."
            "Your drink is in a glass mug as well and inside is a light brown liquid with a layer of milky foam on top."
            "You blow on it then take a sip."

            "..."

            "It's incredibly smooth and gently massages your taste buds with a light, warming flavor."
            "You can't resist taking another satisfying sip before moving on to your bagel."
            "It's full of juicy blueberries and the honey butter spread oozes pure deliciousness into your mouth."

        elif chosendrink == "cappuccino":
            "You fetch your waffle and steaming hot coffee from the counter and head back to your seat by the wall."
            "Your drink is in a glass mug as well. It's a light brown on the bottom, that turns into a milky white in the middle and there's a wide layer of foam on top."
            "You blow on it then take a sip."

            "..."

            "It gives you two distinct flavors of steamed milk and espresso. One is light and the other is strong, neither overpowering the other."
            "You can't resist taking another satisfying sip before moving on to your waffle."
            "You cut off a chunk and pop it into your mouth."
            "The sweet chocolate chips combined with the melted butter send your taste buds to heaven with a first class ticket."

        elif chosendrink == "mocha":
            "You fetch your waffle and steaming hot coffee from the counter and head back to your seat by the wall."
            "Your drink is in a glass mug as well, giving you a nice view of your sweet and salty concoction from up close."
            "You blow on it then take a sip."

            "..."

            "The salt contrasts with the sugary taste of chocolate and caramel, which balance the bitterness of espresso."
            "All the flavors combine into an exquisite beverage that gives you everything you could want in a drink."
            "You can't resist taking another satisfying sip before moving on to your waffle."
            "You cut off a chunk and pop it into your mouth."
            "Juicy strawberries are baked right into the dough, and much like your drink, the combination with butter serves to give your taste buds the ultimate experience."

        "Meanwhile, the bear on the other side of the room taps away on her keyboard."
        "You can hear a lot of frustrated backspacing after she types a long block of text. You wonder what she's working on."
        "Code? A blog post? A book maybe?"
        "You consider asking her, but she seems focused on whatever she's working on and you don't want to intrude."
        "Instead you quietly finish your breakfast then prepare to hit the road."
        "You've got a long walk ahead of you and not much daylight, considering how close it is to Longest Night."
        "As you're heading out the door, the barista chirps."

        trish "Thank ya! Have a good one!"

        player "Thanks, you too!"

        stop music fadeout 2.0

        # scene bg possumspringsroads

        "Now that your belly is filled, it's about time you worked on filling your pantry."
        "You try to mentally visualize a map of Possum Springs and the surrounding areas in relation to your current location."
        "Ham Panther is out of town to the east so... here's the street you need to take."
        "You leave the cafe behind and set out to the grocer."
        "It's almost noon already judging by the position of the sun. Best hurry if you want to make it home before dark."

        scene bg ham_panther with fade

        play music "music/itsadrag_loop.mp3" fadein 1.0

        "Now here's a familiar place. The soulless, sterile, yet gross corporate chain grocery store."
        "Ham Panthers are basically the same everywhere. And man are they everywhere."
        "Except a couple miles closer to your house apparently."
        "You initially move to grab a cart but then you remember you're going to have to carry your haul all the way back home."
        "To limit how much you can buy, you pick up a shopping basket and seek out only the basics."
        "Rice and beans... check."
        "Bread, eggs, a gallon of milk... check."
        "With how cold it is outside, you're more worried about the milk freezing on the way back rather than it spoiling."
        "...Actually wait. You're not lugging a gallon of milk 5 miles home. You put it back and grab the quart size."
        "Ok, what's next?"
        "Carrots, broccoli, and... you're certain you saw a deli here somewhere. You could go for some fresh meat."
        "You swing by the frozen foods section until you come across the deli, where an old cat in an apron and paper hat stands behind the counter."
        "He catches you looking at the meats on display and bellows out a jolly greeting."

        #supposed to be in deli uniform, no sprite available for now
        show stan neutral at right:
            yalign .5
        with dissolve

        stan "Howdy! Let me know if you need anything and I'd be happy to assist you."

        "You give him a nod of understanding then go back to deliberating which meat to get."
        "Chicken seems like a safe bet."
        
        player "Hi there..."

        "You glance at his nametag."
        
        player "...Stan. Can I get a pound of fresh chicken please?"

    stan "Sure thing! I'll have that out for you in a jiffy!"

    "You shift your weight from one foot to the other while the clerk prepares the meat."
    "Once he's finished, he slides the packaged product toward you and you cross it off your shopping list."

    stan "Have a nice day!"

    player "Thanks, you too!"

    hide stan with dissolve

    "You go down a few more aisles, tossing some extras into your basket until it's filled to the brim, then proceed to the check out."

    show gregg neutral with dissolve

    greggunknown "Heya!"

    "A fox with beach blonde fur mans the register you wandered up to."
    "He sports a dark grey turtleneck sweater underneath his apron, along with a chipper attitude."
    "The name tag pinned to the apron reads \"Gregg >:3\""

    player "Hey."

    "You start unloading the contents of your basket onto the conveyor belt. The cashier rings them up with ease, not even looking at what he's scanning."

    gregg "You find everything alright?"

    player "Yup."

    gregg "Oh okay. You just look a little tired is all."

    "You rub your eyes and blink a couple times."

    player "Is it that obvious? Well, I guess I have been on my feet for a while. Had to hoof it here from home. You know where Cedar Road is?"

    gregg "Whoa. Dude. You *walked* all the way from there? That's pretty hardcore."

    player "Heh, thanks. I just hope I make it back before dark."

    "Gregg takes a glance outside through the automatic sliding doors with a contemplative expression."

    gregg "Hey, if you want I can drive you home. My shift's about to end anyway."

    menu:
        "{cps=0}Should you let Gregg drive you home?{/cps}"
        "Sure, what could go wrong?":
            $ greggAP = greggAP + 1
            $ wentWithGregg = True

            player "You'd do that?"

            gregg "Sure! It beats standing around and scanning food."

            player "Well... okay. I guess I can get in a stranger's vehicle just this once."

            gregg "Oh I don't have a car or anything, I ride a motorized bicycle."

            player "Cool, so I can jump off if you try to kidnap me or something."

            gregg "That's the spirit!"

            "He quickly finishes scanning and bagging your groceries, practically bouncing off the walls with excitement. Must have been a slow day for him."

            gregg "Alright, meet me out front in a minute. I have to go clock out."

            "You give him a thumbs up as you reach for your bags."

            hide gregg with dissolve

            "The fox runs off without a care in the world before your receipt is even done printing. You tear it off then go outside to wait."

            # transition to outside ham panther

            stop music fadeout 2.0

            "Standing on the curb, you watch the horizon. Clouds have started to roll into the reddening sky, blocking out the sun."
            "It definitely would have been dark by the time you got home if you had to walk."

            # brief pause

            "What's taking Gregg so long? It's been a good 5 minutes."

            show gregg neutral with dissolve

            "As soon as you set down your groceries and sit, Gregg pops out of the store, zipping up a black leather jacket suitable for a biker."

            gregg "Sorry I took so long. Boss caught me leaving early and I had to make up an excuse."

            player "It's fine, still faster than me walking home."

            gregg "You ready to roll? Come on, my bike's over here."

            "He shows you to a bike rack. You're guessing his is the one with a motor  installed in front of the back wheel."
            "It also has a seat sticking out on the back and pegs to rest your feet."

            gregg "Ta-da! Pretty sweet, huh? Here, lemme take your bags."

            "Gregg picks up your bags and slips them onto the handlebars, giving them a few turns left and right to test the stability with the added weight."

            gregg "Yeah, that should work. Go ahead and hop on!"

            "Gregg jumps into his seat and pats the one behind him. You carefully climb on, holding onto his shoulders."
            "Before you've gotten comfortable in this unusual setup, he revs up the motor and the bike lurches forward."

            gregg "WOOOOOOOOOOOOOO!!!!"

            play music "music/revvedup_v2loop.mp3" fadein 1.0

            "He swivels the bike around sharply and goes down a small ramp into the parking lot where he builds up speed before making a wide turn onto the grass next to the highway."

            # transition to scrolling countryside bg

            "After a few minutes of enjoying the wind on your face and admiring the countryside, Gregg shouts to you over the noise."

            gregg "So, are you new in town? Don't think I've ever seen you before."

            player "Yeah, I moved in just last night."

            gregg "I've been here almost my whole life. How ya liking it? Bored yet?"

            player "I'm still getting used to it I think?"

            "Gregg steers back onto the pavement once you're past the \"Welcome to Possum Springs\" sign since traffic wasn't a problem here."

            gregg "Have you been to town center yet? There's more stuff to do over there, but it's still basically nothing."

            player "No, but I'll be sure to check it out!"

            gregg "Hey I don't think I caught your name. I'm Gregg!"

            player "Nice to meet you Gregg! I'm [newname]!"

            gregg "We're comin' up on Cedar in just a minute."

            "Gregg seems to know exactly where to go until it comes time to point out your driveway."

            player "My place is through there, past the trees."

            gregg "In the dark woods? Spooky."

            "Gregg slows down and turns, and one bumpy ride later you arrive at your residence."

            stop music fadeout 2.0

            # transition to player house exterior

            gregg "Wow, that's a nice big house."

            player "Right? I got it all to myself too."

            gregg "No way! How'd you manage to score a place like this? Are you secretly rich?"

            player "No, just had a dad die on me and I inherited all his belongings."

            gregg "Oh. That's uh, not what I was expecting."

            "You both stand around uncomfortably for a few seconds, then you change the topic."

            player "Anyway, thanks for driving me down here!"

            gregg "No problem dude! I would say \"anytime\" but I'm not a taxi service. Not unless it pays well enough for me to quit Ham Panther."

            "You laugh but his expression indicates he was serious."

            player "Don't worry, I'll find another way to make grocery trips. Just wish there was a closer store."

            gregg "The Snack Falcon in town isn't far but yeah, if you can't survive off chips and slushies there's kind of a monopoly on grocery stores around here."

            player "Mh-hm. Well, I guess I'll see you next time I go out shopping then."

            gregg "Probably! I'm at Ham Panther pretty much all day almost every day."
            gregg "In fact, I'm gonna take off now cause I gotta get up early tomorrow for work."

            player "Oh, sure. Drive safe!"

            gregg "Where's the fun in that?"

            "He helps you remove your bags from the bike's handlebars and you give him a grateful smile. He grins back at you as he hops onto the bike and revs the engine."

            gregg "Take care!"

            hide gregg with dissolve

            "With a casual salute, he circles around back on to the trail and you swear you can hear him hollering like he's on a rollercoaster as he rides down the hilly driveway."

            # transition inside player's house

            "With that out of the way, you carry your groceries inside and find the kitchen to put them away."
            "Whew, another long day comes to a close. It's a good time to change into your pajamas and relax for a bit."

            # changing clothes sfx

            "You can't be bothered to cook tonight, despite your stomach's protests, but you do stop by the pantry on your way to the living room to grab a snack."
            "Now you can curl up on the couch and scroll through news feeds on your phone in peace, occasionally munching on your favorite treat."
            "You kinda wish you brought your laptop with you so you could plug it into the dusty television on the opposite wall and put on a stream or something in the background."
            "You didn't bother spending money on cable now that the internet has replaced any need or general desire for it."
            "Oh well. First world problems you guess."
            "Before long the sun finishes setting, plunging you into a darkness broken only by the glow of your phone and a long drawn-out yawn lets you know it's time for sleep."
            "You begrudgingly get up then retire to your bedroom, put your phone on the charger, and settle into bed."
            "However, just before sleep overtakes you low rumblings make their approach and an abrupt train horn drags you back to consciousness."
            "Ugh, it just keeps getting louder and louder for what seems like eternity."
            "Finally it passes."
            "Not long afterward, *another* train screeches past your house."
            "Frustrated, you shove your face into your pillow and begin counting sheep."

            "1...2...3..."

            "..."

            "...156...157...158..."

            "..."

            "..."

            "..."

            # fade out



        "No, don't want to be a bother.":
            $ bold = bold + 1
            $ wentWithGregg = False

            player "Nah, I can make it on my own."

            gregg "Are you sure? I can take you, it's no big deal. Really."

            player "It's fine. Appreciate it though."

            "He shrugs."

            gregg "Your choice, man. Just be careful you don't like, wander into a bear's den on the way back."

            player "Haha I won't."

            "He quietly finishes scanning and bagging your groceries while you get your debit card ready."
            "With a swipe and a press of a button, you pay for your groceries and Gregg hands you your receipt."

            gregg "Have a nice day!"

            player "Thanks, you too."

            hide gregg with dissolve

            #transition outside

            "Alright, got that out of the way. Now you can begin your arduous journey back home."
            "Hopefully this will be the last time you'll have to walk several country miles in the freezing cold."
            "Or at all."

            stop music fadeout 2.0
            # footsteps sfx

            "The plastic bag handles dig into your hands and the unbalanced weight makes walking an awkward ordeal but you need to hurry before the sun goes down."
            "You look toward the sunset on the horizon. Admittedly it's a pretty view, framed nicely by the countryside and some clouds that have just rolled in."
            "Your admiration for nature's beauty gets interrupted when a semi truck plows past you and nearly sweeps you off your feet."
            "It had gotten windy out, but to make it worse every vehicle that passed by whipped you with an unnaturally strong gust."
            "Some people even honked their horns as they passed by, startling you every time."
            "You can't wait until you get home."

            #scene bg house with fade

            "Of course it's night and bitingly cold by the time you reach your house."
            "You drag yourself inside then unload your groceries in the kitchen, using the empty plastic bags to discard the wrappers from things you snacked on along the way."
            "Too tired to cook, you promptly retire to your bedroom, put your phone on the charger, and settle into bed."
            "However, just before sleep overtakes you low rumblings make their approach and an abrupt train horn drags you back to consciousness."
            "Ugh, it just keeps getting louder and louder for what seems like eternity."
            "Finally it passes."
            "But not long afterward, *another* train screeches past your house."
            "Frustrated, you shove your face into your pillow and begin counting sheep."

            "1...2...3..."

            "..."

            "...156...157...158..."

            "..."

            "..."

            "..."

            # fade out







    # Day 3
    $ currentDate = "December 9"

    scene bg home_exterior_night with fade

    "After a restless sleep, you awaken to the sound of birds chirping outside."
    "You lie in bed for a while hoping to fall back into slumber but the room has gotten too cold for your comfort."
    "The hell? Is the heater working properly?"
    "Drawing in a deep breath, you stretch your limbs and loosen up a few stiff muscles."
    "Your bones crackle and you let out a contented sigh when your spine finally pops into place."
    "Ahh... that felt good."
    "You crawl out from under the covers and pull back the curtains draping the window to let some light in."

    # drawing curtains sfx, and transition to background of view from window
    play music "music/whenskiesclear_loop.mp3" fadein .5

    "To your surprise, snow has appeared in full force overnight!"
    "Snowflakes plummet to the earth, covering the landscape in fluffy whiteness."
    "It's so bright it makes your eyes sting but you can't look away from it."
    "Sunrise in the woods usually evokes that sort of captivating feeling, but this weather is the icing on the cake."
    "Everything's so different, you can hardly recognize your own backyard and the surrounding forest."
    "The ground that had been littered with autumn leaves is now a clean blank slate and the trees have received a makeover heavy enough to make their branches sag."
    "As much as you'd like to spend the morning admiring the scenery, your stomach's growling is getting to be too much to ignore."
    "You need to get something to eat after skipping dinner again last night."
    "After turning up the thermostat, you make your way to the kitchen and see what you've got."

    # scene bg kitchen

    "...Not much, but you can at least fry an egg on a pan and cook a bowl of oatmeal."
    "You watch the snow fall through the window as you feast on your boring breakfast, wishing you had bought stuff to make hot cocoa at the store yesterday."
    "Leaving the dishes in the sink to wash later, you take a trip to the bathroom to get ready for the day."

    scene bg bathroom with fade
    "Steam from your recent shower clouds the mirror, making it hard to judge how presentable you are."
    "Ah it doesn't matter, you probably won't go out today."
    "You can afford to relax and enjoy yourself for the time being."
    "It's a beautiful day, you've got no pressing matters to attend to, and there's a big mysterious house waiting to be fully explored."
    "The thought of finally scouting out this place in its entirety is making you giddy."
    "Who knows what cool stuff your father had collected during his time on this Earth?"
    "There could be like, secret treasure hidden behind the walls, or literal skeletons in a closet somewhere, or a tunnel that leads underneath the local bank's vault."
    "Ok probably not any of those, but you're sure to find something of interest around here."
    "Judging by what you've seen already, your father was pretty well off and enjoyed decorating the place with antiques."
    "What did he do again? Stock trading? Something like that."
    "Maybe those books in his office could give you a clue."

    scene bg home_office_day with fade

    "You couldn't help but check every nook and cranny on the way here."
    "Aside from what must have been your father's bedroom, nothing stood out to you."
    "Just some mundane rooms filled with art, furniture, and more books."
    "The bedroom however, had sent a chill up your spine and you're not sure why."
    "It was just an empty room other than a king sized bed and nightstand on the far wall and a wardrobe on the adjacent one."
    "It smelled like old stale clothes in there, and neither of the two windows provided much light."
    "You had no reason to stay in that room so you shut the door and made a note to leave it be. Like a tomb."
    "Rifling through his office is a different matter however."
    "Those personal documents and computer files are all too inviting to not have a look into."
    "You pull a few binders out from one of the bookshelves and find nothing but boring business records."
    "These papers sure look detailed but it all goes over your head."
    "You put them away and look at another shelf."
    "This one has some modern looking publications."
    "You tilt your head and read the titles on their spines."
    "Manipulating the Economy, Maximizing Your Investments, Money is Me, The Art of Bulls and Bears, 21st Century Trading Techniques 2nd Edition..."
    "...Prediction is Not Luck, How Not to Lose Everything Twice, The Psychology of Good Investors."
    "Yawn. This is lame."
    "Maybe his computer has better stuff."
    "You're not sure what you're hoping to find, it's probably just going to be full of vacation photos and spreadsheets."
    "A cryptocurrency wallet or two if you're lucky."

    # pause

    "What's this?"
    "Stuck in the corner of the monitor is a small, faded picture of you as a kid, proudly holding up a fish you caught."
    "Your father is in the shot kneeling beside you with a big smile on his face."
    "You vaguely remember when that photo was taken."
    "It was early spring, when all the leaves were bright green."
    "You got up early and spent the whole day fishing, just you and your dad."
    "Then when the sun went down you sat on the bank and fed the fish the remainder of your bait."
    "Simpler times, those were."
    "You feel a lump in your throat, but you push it down because adults aren't supposed to cry."
    "With a heavy sigh, you press the power button on the desktop."
    "It's not the quietest machine, with its multitude of hard drives and fans spinning up but it is pretty fast. It finishes booting within seconds."
    "Dang, someone must have formatted the disk, cause it loads straight into a freshly installed operating system."
    "It's already nagging you about updates and setting a time zone and all that crap."
    "You'll deal with this later, you've still got more house to explore."
    "As you turn to leave, you notice a peculiar shelf by the door."
    "The books resting on it aren't like the other ones, these ones are old."
    "Very old."
    "They're all faded and torn. Most of them don't even have legible titles."
    "You pick one up at random from an unorganized stack."
    "It feels like it's about to fall apart in your hands. You carefully flip open the cover."
    "The inside has a drawing of a Satanic goat demon thing, sitting cross legged with a circle filled with runes around it."
    "She's holding a book in one hand and has her other hand raised with her palm facing you."
    "The opposite page bears the title Les Jours du Vide printed in a gothic font."
    "There's no author or legal information anywhere, and the whole book is written in French except for occasional images with ancient runes."
    "You put the book away and search for one written in English."
    "How about this one? Rouge Serpent?"
    "Could be in either English or French. Only one way to find out."
    "You open it up to a random page and skim over some text."
    "Luckily it turned out to be English. Unfortunately it's Old English."
    "Well, Oldish English. You can still make some sense of it."
    "You read a small passage. It's like a poem you guess?"

    #make poem have different text color, maybe a different shade of grey?

    "To upon one\nWho thinks he anything"
    "Consider all the stars\nGreater than him"
    "Burning bright\nHow many have been forgotten?"
    "What can be\nExisted or not"
    "Beloved as vast the sky\nIs nothing"

    "..."
    "You flip to the next page where an illustration of two snakes wrapped together in darkness consumes the space."
    "There's a caption underneath."

    "Fear ye when these serpents come undone, for all will be undone, and His merciful reign will come to an end."

    "Hmm."
    "Not sure what to make of that, other than your old man had an interest in the occult."
    "That would explain the weird art and furniture that would make Dracula jealous."
    "All that's missing is a collection of black metal vinyl records, the kind of music your mother always said would turn you into a Satan worshipper."

    stop music fadeout 1.0

    "You shelf the book and decide to check out one last unexplored doorway."

    scene bg home_basement with fade

    play music "music/woulditmatter_loop.mp3" fadein 1.0

    "As it turns out, it leads you downstairs into the basement-garage."
    "You didn't even realize you had a basement-garage."
    "It's cold and echoey and smells like gasoline."
    "Judging by the debris and tools strewn about, the cleaners skipped over this area. They didn't even sweep the leaves from the floor."
    "A blue tarp covers something in the corner of the room. You ponder what could possibly be underneath."
    "A pile of dead bodies, used for a demon-summoning ritual perhaps?"
    "Or maybe it's a stockpile of cocaine. Never know when you might need a couple hundred pounds."
    "More than likely though, it's gotta be a lawnmower."
    "Nothing makes an old man happier than mowing the lawn at the crack of dawn on weekends."
    "Bracing yourself for disappointment, you grab a corner of the tarp and toss it aside."

    #Visually reveal motorcycle

    "Well this is a welcome surprise."
    "The motorcycle sitting before you has seen better days, but she's still a beauty."
    "Truly a classic, timeless design."
    "She beckons you to touch her."
    "The cold metal sends tingles through your fingers."
    "You've got to take her out for a test drive."
    "Holding onto the handles, you put your leg over the bike and plop your butt in the seat."
    "You bid farewell to the woes of sprawling country roads cause this baby is your one way ticket to Coolsville."

    #If rode with Gregg on day 2
    if wentWithGregg == True:
        "You suppose you can also ride it to the grocery store so you don't have to always rely on the generosity of strangers."

    #If walked home on day 2
    elif wentWithGregg == False:
        "You suppose you can also ride it to the grocery store so you don't have to go on some grand journey every time you need to restock your pantry."

    "You can't wait to feel the wind on your face when you take her for a spin."
    "And if you could get a hold of some aviators sunglasses, you imagine you'd be pretty irresistable when you roll up to town on this thing."
    "Your fantasies of riding down the hills and picking up cuties are put on hold when you realize you're lacking the keys to this fine beast."
    "Presumably the original is lost wherever your father's body lies, but there's gotta be a spare somewhere in this house."
    "You begrudgingly hop off the bike and start searching."
    "Now where would you keep a spare key?"
    "It ain't in the toolboxes down here."
    "A thorough search upstairs yields nothing."
    "It's only when you've about given up do you happen upon the darn thing hiding under a pile of leaves in the basement."
    "How did it end up here?"
    "Whatever, it doesn't matter, you just wanna hear that engine purr!"
    "You insert the key into the ignition and give it a twist but nothing happens."
    "You try again."
    "Still nothing. Out of fuel maybe?"
    "You pop off the cap and look inside the gas tank, using the light on your phone to see into the darkness."
    "Empty."
    "A nearby gas can remedies this issue, but the engine still refuses to start."
    "Hmm."
    "You look around for the repair manual, remembering you saw something like it on the workbench."
    "You skim through it and get the gist on how to check the engine and oil and troubleshoot common problems."
    "Oil seems ok, but you're not sure if sitting around for so long has done it any favors."
    "You grab a few tools, get on the floor, and get to work opening her up."
    "Ugh, it's grimy as Hell down here. Is there a leak somewhere?"
    "Your suspicions are confirmed when you notice liquid dripping from a line below the gas tank."
    "Yeah, that's not good."
    "As far as you can tell, the manual has nothing to say on this."
    "You let out a frustrated sigh and wipe your hands on a towel before checking your phone to look up any nearby auto shops."
    "As fate would have it, the nearest one is even further out than Ham Panther."
    "One of the related results however is a local hardware store in town, not that much further away than the cafe."
    "There's a small chance they might have what you need."
    "Whatever that may be, you don't know."
    "Perhaps if you looked around you'd know it when you saw it."
    "You cover the bike back up then go back upstairs to grab your wallet, keys, and a coat before setting out toward town."

    # scene bg player_house_exterior_day_snow with dissolve
    stop music fadeout 2.0

    "The landscape blinds you once again as soon as you open the front door, though it's hard to be annoyed when the weather is so whimsical."
    "Light grey skies continue dumping a flurry of snow for you to trudge through, but at least the exercise keeps you warm."


    scene bg park with fade

    "Possum Springs' main street is hard to miss when it's right next to a church built on the tallest hill around."
    "One of the paths leading up to it is a stark leaden stairway that also houses an entrance to an underground tunnel, christened the Towne Centre Platform by a nearby bronze plaque."
    "Busy cooking sounds accompanied by smells of greasy food emanate from inside."
    "You catch a glimpse of the interior as you pass by."
    "Hanging orb lights illuminate a small shack and dining area on the bank of a subterranian river"
    "Might be worth checking out later."
    "Moving on, the street ahead of you is lined with old brick buildings."
    "Apartments converted into businesses and businesses converted into apartments as far as the eye can see."
    "It's not so confined as to feel claustrophobic though, considering there's enough space for trees to grow between buildings."
    "A short walk later, you come to the Ol' Pickaxe."
    "Going by the faded inscription on the second floor, this used to be a market house owned by someone named Kremman."
    "It seems odd to you that the current owner wouldn't just paint over the old sign, but you guess people around here like to cling to history."
    "You ascend the couple of steps leading to the front door and head inside."

    scene bg pickaxe with dissolve

    play music "music/picknaxe_loop.mp3" fadein 1.0

    "It's your typical hardware store, nothing too fancy."
    "Mostly basics you won't find at a dollar store along with a small collection of niche tools and parts."
    "Snow shovels seem to be selling quick these days."

    show bea apron at right with dissolve:
        yalign beaheight

    "Behind the counter stands a bluish green crocodile giving off gothic vibes."
    "Black eyeliner does little to hide the bags under her eyes, which drift sluggishly to look in your direction."

    beaunknown "Welcome to the Ol' Pickaxe. Let me know if I can help you find any- *yawn* -...thing."

    "You sense some hostility in her tone though it's obscured underneath a mountain of exhaustion."
    "Before you can reply, her eyelids start to droop and she hangs her head like a ragdoll."
    "A soft snoring escapes her lips."
    "..."
    "Apparently she fell asleep."
    "What are you supposed to do in this kind of situation? Wake her up? Leave her be?"
    "During your hesitation she loses her balance and sways like a tree in a storm."
    "Thankfully not a tree that's destined to fall down."
    "At some point her eyes snap open and she digs her claws into the counter as she regains her footing."

    menu:
        "You ok?":
            $ beaAP = beaAP + 1

            "You step forward, ready to help, though you're unsure what you can do."

            player "You ok?"

            "The croc blows out a sigh then pulls an electronic cigarette out from her pocket."

            beaunknown "Yeah. Just been a long week. I'll be fine as long as this thing doesn't run out of batteries."
            beaunknown "So whatchya need?"

            "The e-cig lights up in her mouth as she pulls up a stool and sits down."
            "You relax a little knowing she's no longer in imminent danger of falling."
            "Remembering what you came here for, you clear your throat and ask about what she sells."

            player "I don't suppose you have any spare motorcycle parts here, would you?"

            beaunknown "Uhh, you'd really wanna go out to the auto shop outside of town for that... What exactly are you looking for?"

            player "I'm not quite sure to be honest. I figured I'd know it if I saw it."
            player "Bike's got a gas leak so maybe some fuel lines?"

            beaunknown "Hmm."
            beaunknown "Tell ya what. I'll check the backroom and see if there's anything that *might* help."

            player "Thanks!"

            beaunknown "Mh-hm."

            "You give her a bright smile."
            "You can tell she made an attempt to smile back but couldn't muster the energy to curl her lips upward."
            "She gets up and shuffles to the back room, leaning on the walls for support."
            "Poor thing, she looks like she hasn't had a decent sleep all week."


        "You look tired.":
            $ beaAP = beaAP - 1

            "You blurt out the first thing that comes to mind."

            player "You look tired."

            "She weakly scrunches her face at you, showing off her fangs."

            beaunknown "Thanks."

            "Her voice is dripping with livid sarcasm. You decide to quickly change the topic."

            player "So uh, I was wondering if you had any spare motorcycle parts here."

            beaunknown "This is a general hardware store. You want the auto shop outside of town."

            player "I know but I thought I'd check this place out first since it was closer."

            "The croc sighs."

            beaunknown "Lemme check the backroom."

            "You flash her an innocent grin."

            player "Thanks!"

            "You can hear her scoff as she goes around to the back, leaning against the walls for support."
            "Poor thing, she looks like she hasn't had a decent sleep all week."


        "Should I come back later?":

            player "Should I come back later?"

            "She looks your way while digging out an electronic cigarette from her pocket with a stressed expression."

            beaunknown "No, ugh - sorry - what can I help you with?"

            "It feels like she's trying to rush you, and honestly you don't really want to stay much longer."
            "Might as well get what you came for before leaving though."

            player "Well, I don't suppose you carry spare motorcycle parts here, would you?"

            beaunknown "Uh. Unlikely, but what exactly do you need?"

            player "I'm not quite sure to be honest. I figured I'd know it if I saw it."
            player "Bike's got a gas leak so maybe some fuel lines?"

            "She rubs her chin and takes a puff from the e-cig, thinking."

            beaunknown "I *might* have something in the backroom that can help. Be right back."

            player "Thanks!"

            beaunknown "Mh-hm."

            "She shuffles over to the back of the store, yawning incessantly."
            "You find yourself yawning too. It's true what they say, yawning really is contagious."


    hide bea with dissolve

    "She disappears behind an archway to a room full of labelled drawers of various sizes."
    "You pass the time by taking a look around the shop."
    "Lots of boxes and miscellaneous items are strewn about like they're reorganizing their inventory."
    "You're studying the oddly large keys behind the counter when the front door opens and a short cat with black fur bursts in."

    show mae neutral flip at left with dissolve

    "Wait a minute, you recognize her as the same cat who picked up the mouse girl at the bus station the other day!"
    "You didn't notice it at the time, but one of her ears is torn and she has subtle red highlights on the top of her head."
    "She kinda gives off that punkish-but-is-actually-really-nice vibe."

    mae "Oh, hey. Is Bea here?"

    player "Is that the cashier?"

    mae "More like owner but yes."

    player "She went to check the backroom real quick."

    mae "Ok cool thanks."

    show mae skeptical flip at left

    "She narrows her eyes at you."

    mae "Do I know you from somewhere?"

    player "Sort of? I think you were at the bus station as I was getting off."

    show mae neutral flip at left

    "A look of realization dawns on her."

    mae "Oh yeah! I remember seeing you! It's not every day someone new arrives in Possum Springs!"

    player "I just moved here. My name's [newname]."

    mae "Mae. Mae Borowski. Nice to meet you!"

    player "Same!"

    mae "So what made you decide to come all the way out to Possum Springs?"

    player "Ah you know, the relaxing countryside, the fresh air... oh and inheriting a sweet house up past the train tracks."
    player "The old man was nice enough to put it in my name before he died four years back."

    show mae sad1 flip at left

    "Mae looks away and mumbles to herself."

    mae "Died... four years back...?"

    show mae panic flip at left

    "She suddenly looks like she's seen a ghost."

    mae "Uhh, look at the time Ihavetogobye!"

    #have mae run off the screen instead
    hide mae with dissolve

    "She runs out of the store just as the store owner comes back."

    show bea apron at right with dissolve:
        yalign beaheight

    bea "Was that Mae just now?"

    "You're still processing what just happened. You snap out of it and turn to the shop owner."

    player "Uh, yeah. You know her?"

    bea "You could say that. What did she want?"

    player "I dunno. She just came in, asked if you were here, then left."

    bea "Huh. Weird. Anyway, I didn't find anything that could help you. Sorry."

    player "Oh. That's ok, it was kind of a long shot. Thanks for checking though."

    bea "No problem. Let me know if there's anything else you need."

    player "Nah, I think that's all I was looking for."

    bea "Alrighty. Have a good one."

    player "You too!"

    hide bea with dissolve

    stop music fadeout 2.0

    #scene bg park

    "You walk out the door and take a few idle steps down the street, mulling over everything."
    "Well that sure was disappointing."
    "Not getting any of the parts you need, that is."
    "But that chat with Mae sure was odd too."
    "Maybe you should stop parading the fact that your dad died. It's probably freaking people out."
    "..."
    "No, it's definitely freaking people out."
    "You're internally cringing at yourself when a delightfully sweet smell reaches your nose through the bitterly cold air."
    "It draws you to the source, a shop called Bear Essentials Bakery."
    "After the long walk here, you might as well get a snack for the road."

    scene bg bakery_interior with fade

    play music "music/Indecisive_Redux.mp3" fadein 1.0

    "A bell above the door chimes as you go inside and you're met with a wave of mixed scents that remind you it's almost Longest Night."
    "The bear behind the counter perks his ears up as he reaches into an oven. He pulls out a tray full of chocolate chip cookies then faces you with a warm greeting."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angusunknown "Welcome! I'll be with you in just a second!"

    hide angus with dissolve

    "You look over the confections in the glass case while the bear sets aside the tray and puts another one in the oven."
    "After deciding what you want, you take a quick glance around the room."
    "It's a pretty wide open space, which is odd for a local bakery."
    "The thing that sticks out the most is the stage taking up nearly a third of the room."
    "Seems odd for a simple bakery to have a stage but it's probably left over from this building's previous business, much like the cracking paint on the walls."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angusunknown "Sorry for the wait. What can I get you?"

    menu:
        "Poppy seed muffin":
            $ confectionChoice = "muffin"
            player "I'll have one poppy seed muffin, please!"
        "Cinnamon roll":
            $ confectionChoice = "cinnamon roll"
            player "I'll have a cinnamon roll, please!"
        "Glazed lemon cake":
            $ confectionChoice = "cake"
            player "I'll have a slice of lemon cake, please!"
        "Raspberry scones":
            $ confectionChoice = "scones"
            player "I'll have a few raspberry scones, please!"

    angusunknown "Sure! Would you like me to heat it up?"

    "You look over your shoulder at the snowy environment, remembering how cold it is."

    player "Please do."

    "The baker catches you looking outside and chuckles as he grabs the [confectionChoice] with a pair of tongs."

    angusunknown "Haha that snow came out of nowhere, didn't it? My winter coat isn't even fully grown in yet!"

    menu:
        "I like the cold.":
            player "I like the cold."

            angusunknown "I do too, but I'd say I'm better equipped to handle it than most. Thick fur and a stocky build designed for winter weather hehe."
        "I hate the cold.":
            player "I hate the cold."

            angusunknown "I can see that. It makes me sleepy. I think it makes everyone sleepy."
        "The cold doesn't bother me.":
            player "The cold doesn't bother me."

            angusunknown "Well that's good, cause I have a feeling we're in for a loooong winter."

    "The bell on the door chimes again as the baker sets your snack inside a small toaster oven."
    "You take a look over your shoulder and to your surprise it's the fox from the grocery store!"

    show gregg neutral at right with dissolve

    gregg "Hey Angus! And look who we have here!"

    "He swaggers up to the counter and makes a grandiose gesture toward you, grinning from ear to ear."

    gregg "This is the guy I was telling you about!"

    if wentWithGregg == True:
        gregg "The one I drove home yesterday and has that big house in the woods!"

        angus "Oh? I'm glad you made it home safely."

        player "Thanks for that again. I never would have expected people out here to be so... kind."

        angus "Oh don't worry, you'll meet some jerks sooner or later."

        gregg "Not us though! We're super chill and nice!"
        gregg "By the way this is Angus. All you need to know about him is that he is the best."

        angus "Oh you."

        player "Nice to meet you, Angus. I'm [newname]."

        angus "It's a pleasure to meet you as well."

        "It seems everyone knows each other in this town. Like everyone's in one big family. It's kinda heartwarming."

        #ding sound effect

        "Everyone's attention shifts to the toaster oven when the timer dings."
        "Gregg leans over the counter and sniffs at your treat as Angus removes it."

        gregg "[confectionChoice], yum."

        player "Can I get that to go please?"

        angus "Of course!"

        player "Thanks."

        "He drops the [confectionChoice] into a small bag, then places that inside a bigger bag and sets it on the counter."
        "As he does so, you pull out your wallet and dig out your debit card."

        angus "Paying with card? Here you go. The machine takes a minute to process though."

        "He slides a tablet with a card reader plugged in toward you."
        "You insert your card and sure enough it gets stuck on the processing screen."
        "After a while, Angus clears his throat and breaks up the lull in the conversation."

        angus "So is Gregg gonna be chauffeuring you every time you need groceries or do you have another way of getting around?"
        angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."

    elif wentWithGregg == False:
        gregg "The one who walked like 10 miles just to buy eggs, bread, a quart of milk!"

        angus "Oh? That takes some real dedication."

        gregg "It's like [heshethey] knew it would snow today."
        gregg "Tons of people rushed out to stock up on food today. Already sold out of eggs and the milk's almost all gone too."

        player "I mean, I got other stuff too but yes it was quite a journey."

        gregg "I bet! By the way, I don't think I properly introduced myself yesterday. I'm Gregg!"

        "He holds out his paw."

        player "[newname]."

        "You take hold of his paw and shake it. He's got a firm, eager handshake."

        if newname.upper() == "SCOTT":
            gregg "[newname], huh? When we lived in Bright Harbor our neighbor was a Scott. I think he was an animator or something."
        if newname.upper() == "ALEC":
            gregg "[newname], huh? We knew an Alec when we lived in Bright Harbor. I think he was a musician or something."
        if newname.upper() == "BETH":
            gregg "[newname], huh? There was a Beth we ran into a few times when we lived in Bright Harbor. I think she was making an indie game or something."
        if newname.upper() == "BETHANY":
            gregg "[newname], huh? There was a Bethany we ran into a few times when we lived in Bright Harbor. I think she was making an indie game or something."

        angus "I'm Angus. It's a pleasure to meet you."

        player "Nice to meet you as well!"

        "It seems everyone knows each other in this town. Like everyone's in one big family. It's kinda cute."

        "Everyone's attention shifts to the toaster oven when the timer dings."
        "Gregg leans over the counter and sniffs at your treat as Angus removes it."

        gregg "[confectionChoice], yum."

        player "Can I get that to go please?"

        angus "Of course!"

        player "Thanks."

        "He drops the [confectionChoice] into a small bag, then places that inside a bigger bag and sets it on the counter."
        "As he does so, you pull out your wallet and dig out your debit card."

        angus "Paying with card? Here you go. The machine takes a minute to process though."

        "He slides a tablet with a card reader plugged in toward you."
        "You insert your card and sure enough it gets stuck on the processing screen."
        "After a while, Angus clears his throat and breaks up the lull in the conversation."

        angus "So are you planning on walking every time you need groceries?"
        angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."

    "The machine beeps and you take back your card. Angus passes you your receipt as you're talking."

    player "Actually I've got a motorcycle I'm trying to fix. I've never worked on this sort of thing though so it might take a while."

    "Now Gregg's ears perk up."

    gregg "Did I hear \"motorcycle?\""

    angus "That is what [heshethey] said."

    gregg "I can help you fix it!"
    gregg "I learned a bunch of stuff from working on my own bike! I bet I can get yours running smoothly in a jiffy!"

    player "That'd be nice. It doesn't run at all at the moment."

    angus "Gregg is the master at getting broken things to work."

    gregg "Yeah, I can come to your place tomorrow morning and check it out! It'll have to be super early though cause I have work later that day."

    player "That would help me out a lot, thanks so much!"

    if wentWithGregg == True:

        player "You remember how to get to my place?"

        gregg "Yup!"

        player "Cool. See you later!"

        gregg "See ya!"

    elif wentWithGregg == False:

        player "Oh, I guess you'd need to know where I live."

        "You hastily jot down your address on the back of the receipt with a pen that was lying on the counter and hand it to Gregg."

        gregg "Sweet! I'll see you there!"

        player "See ya!"

    angus "Have a nice day!"

    player "You too!"

    stop music fadeout 2.0

    hide gregg
    hide angus
    with dissolve

    scene bg park with fade

    "Taking your bag, you leave the store and decide to rest at the park lodged in between the bakery and hardware store."
    "You brush aside the snow that has accumulated on one of the stone benches next to some sort of monument."
    "It's a tall statue depicting a soldier carrying a rifle with a bayonet."
    "Some names are carved into the pillar he's standing on but there's none that you recognize."
    "You mindlessly open up your bag and pull out your [confectionChoice] while looking on."
    "Snow continues to fall, covering both the old dead grass and the freshly made tracks."
    "Looks like some people were playing out here earlier today, going by the footprints and snowman attempts they left behind."
    "You watch the squirrels roaming freely, getting last minute errands done before the real cold hits."
    "They seem to have no fear of people and hop right past you, close enough you could touch one."
    "You munch on your snack in peace until a particularly curious squirrel hops onto the far edge of the bench, staring at you."
    "He comes closer and sniffs at the treat in your hand."
    "Squirrels like [confectionChoice], right? You break off a piece and set it on the bench."
    "The squirrel hesitantly comes over and picks it up with its little hands then shoves it into its mouth and skitters off."
    "You're welcome."

    scene bg home_interior_night with fade

    "The sun had gone down by the time you made it home."
    "You lazed around and browsed the internet on your phone for a while until you were hungry enough to start dinner."
    "Limited by your lack of spices and ingredients in general, you cooked a miserable meal consisting of unseasoned chicken, plain rice, and black-eyed peas."
    "Sitting alone in the dining room pecking at your bland food reminds you of how lonely you are."
    "Watching videos on your phone helps distract you from this feeling a little, but your appetite is clearly diminished."
    "You put the leftovers in the fridge for tomorrow and head to bed."

    #scene bedroom with fade

    "You crawl under the covers and think about your future here."
    "You need to get a job at some point. Sooner or later you'll need the income."
    "You wouldn't mind making some friends too while you're here."
    "It's been so long since you've hung out with anyone, you can hardly remember what it's like."
    "At least Gregg is coming over tomorrow. He seems like a nice guy."
    "You yawn and turn over, clutching your pillow as sleep overtakes you."



    # Day 4
    $ currentDate = "December 10"

    #Sound of Gregg’s bike approaching, followed by the scene fading in
    scene bg home_interior_night with fade

    "You had managed to get used to the train and its blaring horn passing by several times each night but now your slumber is disturbed by a new sound."
    "It's the rumbling of a motor approaching, followed by tires digging into the ground just outside the front door."
    "You quickly become alert once you realize that must be Gregg coming over to fix your bike."
    "You scramble out of bed but before you can change out of your pajamas he's already knocking on the front door. You have no choice but to answer it like this."

    #Transition to front door

    "It's not even daylight out yet."
    "You flip on the lights and open the door to find Gregg standing there proudly with an overstuffed backpack in his hand."
    "He seems oblivious to the fact that you've just woken up."

    play music "music/cozycidersipping_loop.mp3" fadein 1.0

    show gregg neutral flip at left with dissolve

    gregg "Morning, [newname]! I brought all my tools and a bunch of parts."

    player "Uh, morning Gregg. I didn't expect you so early."

    gregg "I only have an hour before I have to be at work."
    gregg "Well? Where's the bike?"

    player "Oh uh, right this way."

    "You lead him inside and down the stairs into the basement."
    "It reeks of gasoline so you open up the garage door for ventilation before pulling the tarp off your motorcycle."
    "Gregg's eyes go wide at the sight of it."

    gregg "She's beautiful. I love her."

    player "I'd love her more if she didn't leak fuel."

    "You point at the puddle of gas soaking into the concrete floor."

    gregg "Ooh, yeah that's a big problem."
    gregg "Hmm."

    "He drops to the ground and gets an up close look at the engine."

    gregg "You got a towel?"

    "You grab a towel from the workbench and hand it to him."

    gregg "Thanks."

    "He wipes off some of the grime, then pulls his backpack close and rummages around until he finds a flashlight."
    "Lighting up the area underneath the bike, he pokes and prods at a few parts then furrows his brow."

    gregg "Hrmmm..."

    player "What is it?"

    gregg "Not sure yet."

    player "Can I get you anything? A drink?"

    gregg "Nah, I'm good."

    "He pulls a wrench from his bag and starts unscrewing nuts and bolts while you stand by, just observing."
    "You wish you could help, but you're really at a loss at what to do and you don't want to get in his way."
    "He takes off quite a few bits and pieces, and at times looks like he's confused by what he's working with, but he continues working with confidence."

    gregg "Hey how much fuel is in the tank, do you know?"

    player "Um."

    "Suddenly a valve clanks against the floor and the entire gas tank empties itself onto Gregg's sleeve."
    "He recoils in surprise and falls back on his rear."

    gregg "AAAAAAAH!"

    player "Oh shit!"

    gregg "Haha don't worry, it's fine! Didn't get much on me."

    "Gregg flicks his arm to get the remaining droplets off."
    "Thankfully most of it had slid off his leather jacket and splattered onto the floor instead of soaking into his fur."

    player "Still..."

    menu:
        "Wipe down his jacket":
            #+1 greggAP
            #+1 understanding

            "You grab a spare cloth and wipe the excess liquid off his jacket, noticing he got a smudge of oil on his face too."

            player "Hold still."

            gregg "Wha-?"

            "You scrub the oil spot off as gently as you can. He freezes in place as you clean his fluff."

            player "There. You had something on your face."

            gregg "O-oh!"
            gregg "Haha thanks! I wouldn't wanna show up to work with a big splotch on my face! Hahaha!"

            "His lighthearted laughter is contagious, at least enough to put a smile on your face."

        "Hand him a clean towel":
            #+1 cynical

            player "Sorry, I should have warned you ahead of time..."

            "You hand him a spare cloth."

            gregg "Nah, it's alright."

            "He wipes the excess liquid off his jacket."

            gregg "See? No harm done."

            player "You got a bit of oil on your face too. Right there."

            "You point in the general area where the splotch is on his face. He roughly scrubs at the area."

            gregg "Did I get it?"

            "Not really..."

            player "Yeah."

    gregg "Alright, let me finish working on this. I think I can get her running soon."

    "Gregg goes back to operating on your bike, wiping down gunked up parts, reseating pieces, and duct taping components."
    "Time flies by as you watch him. He really seems like he's having a good time fixing your bike and making idle chit chat."
    "Before you know it he stands and claps his paws together."

    gregg "That should do it!"
    gregg "Hopefully!"
    gregg "Let's roll her out of here and see if she starts!"

    menu:
        "I'm so excited!":
            $ greggAP = greggAP + 1

            player "I'm so excited!"

            gregg "Come on come on come on let's push her out onto the yard!"

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

            #[Sound of failing motor]

            "..."

            "Another turn."

            #[Sound of failing motor]

            "..."

            #[Sound of motor successfully starting]

            "Just as you're losing hope, the engine comes to life."

            player "Hahaha yeah!!!"

            "Gregg looks so relieved. He's flailing his arms and howling."

            gregg "AWOOOOOOOOOOOOOOO!"

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks so much for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, that sounds fun! I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

        "I'll be surprised if this works.":
            #(-1 Gregg AP, +1 cynicism)

            player "I'll be surprised if this works."

            "Gregg's ears droop."

            gregg "Hey man, don't doubt my abilities. At least it can't run *worse* now after all that work I put into it."

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you with anticipation in his eyes as you put the key into the ignition and give it a turn."

            #[Sound of failing motor]

            "..."

            "Another turn."

            #[Sound of failing motor]

            "..."

            "Just as you thought, he couldn't fix-"

            #[Sound of motor successfully starting]

            "*VROOOOOM*"

            "The engine comes to life, much to Gregg's relief."

            gregg "Yes!"

            player "Well this is a pleasant surprise."

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

        "What did you do?":
            #+1 Gregg AP, +1 inquisitive)

            player "What did you do to it?"

            gregg "I think the fuel was left sitting in there for too long and like, solidified in a tube and cracked it open."
            gregg "Now come on, let's push her out onto the yard!"

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

            #[Sound of failing motor]

            "..."

            "Another turn."

            #Sound of failing motor]

            "..."

            #[Sound of motor successfully starting]

            "Just as you're losing hope, the engine comes to life."

            player "It works!"

            "Gregg looks so relieved. He's flailing his arms and howling."

            gregg "AWOOOOOOOOOOOOOOO!"

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks so much for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, that sounds fun! I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

    hide gregg with dissolve
    stop music fadeout 2.0

    "Now that the excitement has worn down, your nerves become aware of the cold surrounding you."
    "Most notably around your bare feet."

    player "Brr..."

    "You curl your toes to get some blood flowing through them then push your bike back inside."
    "After closing the garage door, you bask in the heat for a while, then head upstairs for a long hot shower."

    #[Transition into next scene]

    "It's getting late. The sky is already turning dark."
    "You should head out to Gregg's place soon."
    "Should you eat before leaving? He didn't say anything about getting food while you're out."
    "But he didn't say anything about *not* getting food while you're out either."
    "Eh, you had leftovers for lunch and that was filling enough to keep you satiated either way."
    "You'd spent the day getting small errands done like unpacking all your stuff, setting up programs and accounts on the desktop, and taking your bike to the gas station by the highway."
    "It'll take some getting used to the biker life, but you've learned there are few joys that come close to the freedom of revving up a motorcycle and coasting downhill on an empty road."
    "You grab your daily carry stuff then head down to the basement and open the garage door."
    "Gregg had messaged you on Chattrbox a few hours ago asking you to bring over the tools he left behind."
    "You gather his things into the bag then zip it up and sling it over your shoulder."
    "Oof, this thing's heavy!"
    "You manage to bear with it and roll your bike outside, stepping into the night."
    "Moonlight pours down from between the clouds."
    "It's cold and breezy out."
    "You feel a tingling sensation on your skin."
    "Is it just cause of the cold or because you're excited to hang out with people again?"
    "A part of you feels nervous."
    "What if tonight doesn't go well? What if you do something that makes them hate you?"
    "You shiver, trying to shake off the feeling."
    "Whatever, no sense in worrying about it."
    "You close the garage door behind you and hop on your bike, taking off into the unknown."

    scene bg park with fade

    "You pull up to the curb next to the Bear Essentials Bakery and check the time on your phone."
    "5:47."
    "A little earlier than you expected, thanks to the lack of cops in Possum Springs to deter you from riding fast."
    "But... the building looks abandoned?"
    "Lights are off, the sign says closed, and the only apparent entrances are locked."
    "No response when you bang on the door either."
    "Does Gregg really live here on the second floor or was he messing with you?"
    "You can't even text him because the only wifi spots available are password protected."
    "You have no choice other than to wait and see if Gregg or Angus show up."
    "Crossing your arms, you lean against the building and sigh."
    "Your breath is easily visible in this weather, the contrails spiraling upward and being whisked away by the wind."
    "You remember pretending to be a dragon when you were a child, blowing out \"smoke\" when it was cold out."
    "You reminisce over moments like those and try spewing fire like you always wanted to."
    "Nope, still just smoke."
    "Which is really just hot air."
    "Your thoughts are interrupted by the sound of snow crunching behind you."
    "Footsteps."
    "They're coming closer."
    "More than one person."
    "You risk a glance over your shoulder, more worried that someone saw you acting out your dragon fantasies rather than someone coming to mug you."
    "You're pleasantly surprised to find Angus walking toward you with a pizza box in his arms."
    "And he's got a friend in tow."
    "That must be the guy Gregg was talking about. He's a short birdy fellow with a rucksack on his back."

    show angus neutral flip at left:
        yalign angusheight
    show germ neutral at right
    with dissolve

    angus "Hello, [newname]! Gregg hasn't let you inside yet?"

    player "Hey Angus. Nah, I haven't seen him. The place looks empty."

    angus "Hmm. He's probably watching TV in the dark and couldn't hear you."
    angus "This is Germ by the way. Germ, this is [newname]."

    germ "Hi [newname]! I hope you like video games! I brought some with me."

    "He adjusts his bag to emphasize his point."

    menu:
        "I love video games!":
            player "Nice to meet you uh... Germ? And yeah, I love video games!"
        "They're alright.":
            player "Nice to meet you uh... Germ? And yeah, video games are alright."

    "You're not sure if you heard his name right but just smiles and doesn't correct you."
    "Kind of an odd name but who are you to judge?"

    angus "And I bought pizza! I didn't know what kind you liked so I just got cheese."

    player "Cheese is fine."
    player "So are we gonna go in or...?"

    angus "Oh right. Forgot you guys are probably freezing."
    angus "Come with me."

    hide angus
    hide germ
    with dissolve

    "You and Germ follow Angus to the back of the building."
    "It feels a bit sketchy, but you doubt a guy carrying a pizza is going to mug you."
    "He starts up the metal stairway of the emergency exit."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angus "Sooo, fun fact. The stairs inside are broken."
    angus "They caved in before we bought the place. That's why we have to take the fire escape to get to the second floor."

    player "Caved in? How does something like that even happen?"

    "Angus shrugs."

    angus "This building isn't exactly up to code."
    angus "I don't think it's even legal for us to live here but it's the cheapest option and nobody's stopped us yet."

    hide angus with dissolve

    "You climb up the staircase after Angus with Germ taking up the rear."
    "When you reach the second floor, you have to crawl through a window to get inside."

    #play music "music/trvekvlt.mp3" fadein 1.0

    scene bg greggapartment with fade

    "Gregg is passed out on a stained couch in front of a TV."
    "Beer bottles litter the floor around him."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angus "Honey, I'm home! And I picked up two hitchhikers!"

    "The startled fox rolls off the couch and hits the floor with a thud."

    show gregg neutral at right with dissolve

    gregg "AAAAAAAAAAHH!"

    "He quickly regains his composure, acting like nothing had just happened."

    gregg "[newname]! Germ! What's up?"

    angus "I found Germ wandering around on the way back from the pizza joint, and [newname] was just sitting out front."

    gregg "Oops, that's my fault. I shoulda been waiting out there for ya, [newname]."
    gregg "Please accept Angus's pizza as an apology on my behalf."

    player "Apology accepted."

    angus "I'm happy I could be of service."

    "Angus slides the pizza onto a table and opens a cabinet to grab some paper plates and plastic cups while Gregg pulls a 2-liter bottle of soda out from a mini fridge in the corner."
    "Meanwhile Germ sneaks away to the television and unzips his bag."

    germ "I'm gonna set up the games."

    angus "I'll get you a plate, Germ."

    germ "Thanks."

    angus "[newname], you can just set your backpack down wherever, you know."

    player "Oh right, Gregg left his tools at my place so I brought 'em over."

    "You take off the backpack and hand it to Gregg."

    gregg "Aww, thanks for not stealing them!"

    "He carelessly tosses it against the wall beside the couch."

    player "Anytime."

    "Angus opens up the pizza box and hands you a plate."

    angus "Guests first."

    player "You don't have to tell me twice!"

    "You grin and take a couple slices then move over so Gregg can get some while you pour yourself a drink."

    gregg "So you rode your motorcycle here right? How's she run?"

    player "Pretty good once I got some fuel in her."

    angus "I'm glad Gregg could help you fix her up."

    gregg "And that she didn't explode."

    "Angus fills up a plate for Germ, then takes the remainder of the pizza for himself."

    angus "Gregg, could you get drinks for me and Germ?"

    gregg "Sure thing!"

    hide angus
    hide gregg
    with dissolve

    "Gregg pours extra drinks as you and Angus make your way to the couch."
    "Germ is crouched by the TV hooking up the connectors to the very outdated cube shaped console sitting on the floor."
    "Angus gives Germ his plate and grabs a controller for you, Gregg, and himself."

    show angus neutral at right:
        yalign angusheight
        xalign 1.1
    show germ neutral flip at left:
        yalign germheight
        xalign -.02
    with dissolve

    angus "Thanks for bringing your console, Germ. I'll take the busted controller this time."

    germ "If you insist."

    "Gregg comes by shortly after and sets the drinks on a small table then sits on the couch with his plate in his lap."

    show gregg neutral:
        yalign greggheight - .5
        xalign .7
    with dissolve

    gregg "Angus and I had to sell our consoles when we moved, [newname]. We were very sad."

    angus "I mostly play on PC."

    gregg "*I* was very sad."

    player "Where'd you move from?"

    angus "Bright Harbor."

    if newname.upper() == "SCOTT":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "ALEC":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "BETH":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "BETHANY":
        player "Ah right, you mentioned living in Bright Harbor before."

    gregg "We used to live here in Possum Springs, then moved to Bright Harbor, then back here."

    "Sounds like the two of them have some history going pretty far back."
    "It just now occurs to you that they might be more than just friends."

    player "Sorry if this is a dumb question but are you two... together?"

    "Gregg snuggles up to Angus, who leans his head on him."

    gregg "Yup! "

    angus "I can barely remember a time when I wasn't with Gregg."

    germ "*Ahem*"

    "Germ turns to you with two game cases in his hands."

    germ "What game should we play?"

    gregg "You decide, [newname]."

    menu:
        "The platformer fighting game.":
            $ gameChoice = "fighting"
            "You point at the fighting game."
        "The board-based party game.":
            $ gameChoice = "party"
            "You point at the party game."
    player "That one."

    germ "K."

    "He takes the undersized disc and pops it into the console."
    "Germ opts to stay sitting on the floor, while you, Gregg, and Angus fill up the couch. You all enjoy a few bites of pizza while the intro video plays."

    germ "This is the like, newest game I have."

    gregg "Isn't this game 20 years old?"

    germ "Yup!"

    "Germ hits start and sets up the game."

    angus "Ugh, I hate getting grease on the controller."

    gregg "That's what pants are for."

    "Gregg wipes his paws on his pants."

    angus "Be right back, I'm gonna grab some napkins."

    "Angus gets up and steps over the wires on the way to the table."
    "He comes back with a stack of napkins and hands them out to everyone before sitting back down."

    gregg "Ready?"

    angus "Yeah."

    "You all pick a character and begin a round."

    if gameChoice == "fighting":

        "Germ is surprisingly good at this game. His inputs are efficient and he punishes with grace."
        "Despite that, he gives you and the others a fair chance by leaving his defenses open."
        "Gregg's aggressive plays allow him to take a couple of lives, at the cost of his character getting killed as well more often than not."
        "Angus seems to be trying to get used to the controls, which only adds to the hilarity when he accidentally knocks someone off the stage."
        "You just try to survive as long as you can and land a few hits whenever you can."
        "Unsurprisingly Germ wins the round."

        gregg "Angus. You press X to jump."

        "Gregg points to the button on Angus's controller."

        angus "Well I wish you would have told me before I died a million times!"

        "Germ unassumingly eats his pizza while waiting for the next round to start. Everyone chooses a new character and you go to a random stage."
        "As soon as it loads, Gregg immediately jumps off and dies."

        gregg "Wait I thought I was the other guy! Restart!"

        germ "No redoes."

        "Against your better judgement, you decide to taunt Gregg, both in real life and in the game."

        player "Yeah, no redoes."

        "You blow a raspberry at the fox as your character dances on screen."
        "Your in-game taunt ends up getting you killed but thankfully Gregg restrains himself from doing the same to you in reality."
        "Angus fares a little better this time."
        "You all go easy on him and avoid targeting him unless he engages first. Gregg however is out for blood, doing whatever it takes to get you off the stage."
        "Usually Germ ends up finishing both of you off."
        "Eventually it's just Germ and Angus left standing. You eat your pizza and watch while Gregg coaches Angus."
        "It all comes to an anticlimactic conclusion when Angus misses an easy punish and slowly falls off the bottom of the stage."

        gregg "Angus! You have to press B and up at the same time to recover!"

        angus "I was doing that!"

        gregg "No like, you have to slam the stick like this."

        "Gregg demonstrates."

        angus "Hrm."

        "You start up another round. This time you all have the same idea to gang up on Germ."
        "He doesn't seem to mind, and he methodically takes you all on simultaneously."
        "You and Gregg manage to get a few combos off on him but once again the match ends with a showdown between Angus and Germ."
        "Germ shields against Angus's special then completely whiffs his own attack, giving Angus a chance to launch him off stage."

        gregg "OOOOOOOOOOOOOOH! GOT HIM!"

        "You all have a laugh at the outcome, especially after Gregg's reaction to it."


    elif gameChoice == "party":

        "You decide on a board then your characters all roll a die and move forward however many spaces."
        "Each space you land on has a different effect, whether it's gaining or losing money, acquiring an item, teleporting to a different spot on the board, or a variety of other events."
        "And at the end of each turn, you have to play a minigame. Sometimes it's a free-for-all, sometimes it's 2 vs. 2 or 1 vs. 3 with randomly selected teams."
        "The game is designed to be impossible to play seriously no matter how hard you try, with all its randomness and janky controls."
        "As frustrating as it can be to lose everything because the game felt like it, it's difficult to stay mad when you get your points swapped with the guy in first place on the next turn."
        "There's a lot of downtime between minigames since you just have to press a button to roll the die and watch the game play out, giving you ample time to munch on your pizza."
        "Germ is such a pro at this game he eats his while playing the minigames."
        "Gregg's aggressive plays are counterbalanced by his incredibly bad luck throughout the round, landing him in last place."
        "Angus on the other hand plays safely. Perhaps a bit too safely, since he usually ends up missing chances to get points."
        "It all culminates in a last minute exchange where Germ risks everything on a duel between you and him. Of course the minigame you have to play for the championship is entirely based on chance."
        "Basically you have to jump onto one of the colored quadrants of a carousel and hope it's not the wrong one."
        "It spins around for a while and when it stops a monster chained to the wall eats whoever is on the space closest to it."
        "If no one is on that spot, you choose another one and it takes another spin. This goes on indefinitely until one of you dies."
        "Germ goes first, picking red. You jump on yellow and you both go for a spin."
        "When it starts to slow down it looks like Germ is about to lose but he ends up just out of the monster's range when it stops. Death narrowly avoids you as well."
        "Now you both hop off and choose a quadrant again."
        "You both last a shockingly large number of turns. A statistically improbable amount. But sooner or later one of you has to die."
        "The tension is rising. Will you outlast your opponent? Or does he have lady luck on his side tonight? Who will be the one to get eaten?"

        gregg "Oh my god, I can't watch."

        "Gregg covers his eyes. Germ jumps on the yellow spot. You're up next."

        player "Aaah I can't decide!"

        "Gregg takes a quick peek to offer his coaching."

        gregg "Red!"

        angus "Green."

        germ "Anything but blue."

        "It's all random anyway so you just press A and jump onto whatever space. You end up on blue."
        "The merry-go-round spins up and the monster approaches with a hungry look in its eyes."
        "As you come to a crawl, Germ coasts right past the kill area. Green and red go by and then finally it stops on blue."
        "Your character gets gobbled up and all your points are taken away, just like that."

        angus "Ooh!"

        "Gregg uncovers his eyes while the next scene loads."

        gregg "What happened? Who lost?"

        angus "[newname] got eaten!"

        gregg "OOOOOH! GERM IS THE MASTER OF LUCK!"
        gregg "AWOOOOOOOOOO!"

        "Gregg sure seems happier about this outcome than Germ does. The final results screen pops up, showing Germ on top and you on bottom."
        "Angus got second place and Gregg got third."

        player "How did you know it was gonna be blue?"

        "Germ shrugs."

        germ "I had a feelin.'"


    #fade to black and back

    hide gregg
    hide germ
    hide angus
    with dissolve

    stop music fadeout 1.5

    "The night goes on with the four of you having a good time playing games until Germ says he has to go back home."
    "At that point you were tired and getting ready to call it quits anyway. You coil up your controller's wire and help Germ pack away his system."
    "Zipping up his bag, he stands up and waves to you."

    show germ neutral flip at left:
        yalign germheight
    with dissolve

    germ "See ya!"

    hide germ with dissolve

    "That's all he says before going to leave through the window."
    "He's certainly an odd guy, but he's very friendly."
    "Gregg and Angus finish cleaning up the plates and napkins and come up to you."

    show gregg neutral flip at left:
        yalign greggheight
    show angus neutral at right:
        yalign angusheight
    with dissolve

    gregg "Whew, that was fun."

    angus "It sure was."

    player "Yeah."

    "There's an uncomfortable silence as nobody is sure what to say and everyone just wants to hurry this up and go to bed."

    gregg "So Angus, what do you think? Dragons and Dungeons next week?"

    angus "Sure, that sounds good. Perhaps our new friend would like to join us?"

    player "I'd be down for that. Just have to check my schedule first."

    angus "Ah, the persistent problem of finding a time where everyone is available."

    gregg "No problem dude, just let us know when you're free and we'll work something out."

    angus "Do you use Chattrbox by any chance? We could coordinate a date on there."

    player "Yeah, hold on."

    "You pull out your phone and exchange contact info with Angus."
    "From there, you thank him and Gregg for the pizza and say your goodbyes before climbing out the window and going down the fire escape."

    hide gregg
    hide angus
    with dissolve

    #Transition to bakery exterior

    "It was refreshing to hang out with a group again."
    "Gregg's upbeat personality is fun to be around, and Angus is a really sweet guy."
    "It's hard to pin down how you really feel about Germ since he was so quiet, but he seems cool."
    "You hop onto your bike and ride back home, reflecting on how much your life has changed in just a few short days."
    "You're enjoying a fresh independent lifestyle but you're also making new friends and coming out of your shell. It feels good."

    scene bg home_interior_night with fade

    "When you arrive at home, you notice both Gregg and Angus sent you a message on Chattrbox."

    gregg "Awesome night dude, can't wait to hang again!"
    gregg "I usually get off work at ham panther in the afternoon if you wanna swing by and ride bikes and stuff."

    angus "Just making sure you made it home safely."
    angus "Had a fun night with you all. Come by the bakery anytime if you're ever in the area and just wanna chat or something."
    angus "You won't be a bother, I don't get that many customers."

    "You send them both a short thank you message and let them know you had fun too before turning in for the night."

    # fade out



    # Day 5
    $ currentDate = "December 11"

    "Well, you made it to the end of the week without any major incidents."
    "You've just about settled into your new life."
    "Most of the paranoia and oppression you faced at your old home has melted away, and you're now comfortable living as you see fit and taking things at your own pace."
    "This morning you help yourself to a large breakfast, a long hot shower, and plenty of free time to browse the web."
    "Sitting around all day can get kinda boring though."
    "Maybe you should see if Gregg or Angus are free?"
    "Nah, don't want to seem too clingy."
    "You could explore town a bit. There's still a lot you've yet to see."
    "But where exactly would you go?"
    "You pace around the house pondering this question and wind up in what must have been the smoking room, judging by the stench of cigarette smoke permeating the air even after all these years."
    "You thought these things went out of style a century ago but here we are."
    "Not like a little smoke bothers you at this point though."
    "You recline in one of the big fancy chairs in the room and close your eyes."
    "Maybe you'll just nap away the boredom."
    "..."
    "No, this is too boring."
    "Your hand wanders over to the side table and picks up the book that was resting on it."
    "You lazily turn your head to the side and read the title."
    "\"Cryptids of the Western Hemisphere.\""
    "Opening it up to the bookmarked page, you find an article on the Jersey Devil, a weird skinny goat thing with wings."
    "The paranormal sure loves its goats, doesn't it?"
    "Upon reading further, it appears the Jersey Devil is nothing more than a fabrication by hysterical religious country bumpkins."
    "There's not even anything unique about him, he's just a winged goat with devil connotations who sometimes steals chickens."
    "As you close the book, your fingers brush against a bump on its spine."
    "Turning it over reveals a sticker, not unlike the kind you'd find on a library book."
    "Hold on a second, this *is* a library book!"
    "This thing must have been sitting here overdue for ages!"
    "You should return this to the library soon. You're certain they're just dying to get this book back."
    "They might even be so glad to see it again that they'll waive the late fee."
    "It's not like they could charge you a fee if even they wanted to, right?"
    "It's not your book, you just happened to find it."
    "Regardless of the consequences, you've been given a quest and you intend to see it through to the end."
    "This is the most excited you've ever been to go to the library."

    scene bg library_floor1 with fade

    play music "music/deweydecimal_loop.mp3" fadein 1.0

    "Possum Springs sure has an impressive library."
    "It's a three story building with lavish old-timey architecture and has been very well maintained."
    "Gargoyles adorn the outside while giant pillars and arches frame the murals on the inside."
    "The interior has been modernized with new carpet and a fresh coat of paint that accentuate the comfortingly dim lighting."
    "You can't help but admire the effort that went into this place."
    "You stare at the multitude of books organized neatly on shelves as you walk up to the reception desk. Sitting there is the same bear you met at the cafe the other day."
    "What did the barista call her?"
    "\"Selmers?\""
    "She looks up from writing something in a notepad."

    show selma neutral flip at right with dissolve:
        yalign selmaheight

    selma "Oh hey, it's you."

    player "Hey."
    player "You're... Selmers, right?"

    "Her carefree demeanor wavers slightly and there's a hint of disdain in her voice."

    selma "That's what most folk call me."
    selma "I remember you from Posspresso but I didn't get your name."

    player "[newname]."

    selma "Nice to officially meet you, [newname]."
    selma "Welcome to the Possum Springs Public Library. Is there anything I can do for you?"

    "You take one last look at the book in your hand then slide it over the counter."

    player "I found a book that belongs here and wanted to return it."

    "Selmers picks up the book and gives it a look over with an intrigued expression before scanning it into the system."
    "She rotates her chair to face the computer monitor and clicks the mouse a few times."

    selma "Wow, this was checked out way before I even started working here."
    selma "Where'd you find this?"

    player "It was uhh..."

    menu:
        "Lying at the bottom of a well":
            player "...lying at the bottom of a well."
        "Left in an abandoned house":
            player "...left in an abandoned house."
        "Sitting underneath a bench":
            player "...sitting underneath a bench."

    selma "Hmm."
    selma "That explains why it never found its way back here until now. Glad you returned it, it's the only copy we had."

    player "I don't have to pay the late fee, do I?"

    "That gets a chuckle out of her as she sets the book aside."

    selma "Naw, consider it on the house. It was probably written off as lost forever, so thanks for bringing it back."

    player "No problem."

    selma "Will that be all? Or would you like to get a library card while you're here?"

    "You raise a brow."

    player "How'd you know I didn't have one?"

    selma "I know everyone who has one."
    selma "Possum Springs is a small town and the number of people here who have a library card in 2021 is even smaller."

    player "Oh."
    player "Well since I'm here, I might as well."

    selma "Aight. Just need you to fill out this form and show me a valid ID."

    "She pulls a sheet of paper out from a filing cabinet and pushes it toward you."
    "You grab a pen from the holder and quickly fill it out."
    "Once you're done, you pull out your driver's license and pass both it and the sheet back to Selmers."

    selma "Kay, just have to type this in real quick..."

    "She looks over your license and makes a few keystrokes before handing it back."

    selma "...and now all of this..."

    "She waves the application form in the air."

    selma "...then scan it in and print your card from the office."
    selma "You're welcome to explore and find some books to check out while I do that. I'll have your card ready by the time you're done."

    player "Ok! Be back in a bit."

    hide selma with dissolve

    "You leave her to her work and go over to the bookshelves across the room, skimming over book titles without really reading them."
    "You're not looking for anything in particular but maybe something will grab your attention."
    "Nope, nothing here stands out."
    "That elevator in the corner of your eye however is a different story."
    "This floor seems to be dedicated to boring nonfiction, so the fiction section must be up above."
    "That's probably where that book you just returned will get shelved. You wonder if there are any others like it your father might have checked out as well."
    "It's kinda weird. Like you're retracing the footsteps your father took at some point."
    "You feel like you're following a treasure map and slowly piecing together his interests along the way."
    "It's neat seeing what he was like, but it also fills you with remorse for not getting to know him better while he was alive."
    "He'll always be some vague idea of a man in your mind and not someone you had a real bond with."
    "You shake off the feelings bubbling inside you and go call down the elevator."

    stop music fadeout 1.0

    "You've kind of lost interest in the books around you but you still want to finish exploring the library at least."
    "The doors open with a mechanical grinding sound and you ride up to the second floor."

    play music "music/Stagnant_Tone-down.mp3" fadein 2.0

    "Here the walls are painted a salmon pink and minty green and the lights are brighter. It no longer has that regal feeling of the first floor, but it's still warm and comforting here."
    "Desks with computers line the nearest wall and lead into the children's book section, as evidenced by the Charity Bearity mural thing in the corner."
    "You turn away from it and head down an aisle more suited to your age, where you spend some time reading titles and a few back cover descriptions to get your mind off things."
    "Your browsing leads you down each aisle until you reach the last one, where you discover a young mouse sitting on the floor among a pile of books."
    "She seems to be so engrossed in the book in her hands, she doesn't notice of your presence."
    "You consider leaving so as to not disturb her, but then you spot the poorly lit sign indicating that this is the horror section."
    "This would be where where the cryptids book and any others similar to it would be found, right?"
    "You curiously enter the aisle and make your way through it, scouring the titles."
    "You keep an eye out for anything related to cryptids, trying not to make any noise. Before you know it, you're halfway down the aisle."
    "As you're perusing a shelf, you feel your leg bump into something and hear a startled squeak from beside you."

    show lori anxious3 flip at left with dissolve:
        yalign loriheight

    "You look down and see the mouse girl pressed up against the bookshelf, frozen in place with the look of a deer caught in the headlights."
    "You step back and clear your throat, about to say \"Excuse me\" when suddenly she lets out the breath she'd been holding."

    show lori breath flip

    lori "*Huff huff huff* Sorry, sorry!"

    show lori sad2 flip

    "She hastily shovels her books aside so you can get past."

    player "No, I'm the one who should be apologizing..."

    show lori anxious3 flip

    "She glances back up to you."

    lori "Wait a minute... Haven't I seen you before?"

    "Your memory finally catches up and you recognize her as the girl who was listening to that weird music on the ride into town."

    lori "You were on the bus the other day, weren't you?"

    # if player asked her to turn down music and was rude:
    if loriInteractionRude == True:

        player "Oh yeah, I remember you!"
        player "I think your music is what's been giving me nightmares lately."

        show lori sad flip

        lori "I just keep getting in your way I guess..."

        "She mumbles, looking away."
        "You shrink down, realizing how rude you're being."
        "You should try being more amicable."
        "And if that doesn't work, you could always just leave her alone."
        "The girl clears her throat and looks back up to you."

        show lori anxious2 flip

        lori "So are you visiting Possum Springs or something?"

        player "I just moved in actually."
        player "My name's [newname]."

        lori "Lori."

        "You squat down and crane your neck to read the titles of the books in her little pile."

        player "Whatcha reading?"

        show lori neutral flip

        "She seems to lighten up in response to your interest in her reading material."

        lori "Oh these? Just some spooky stories to read in the dark."

        player "You a big horror fan?"

        lori "Well, I *am* going to film school to make horror movies."

        player "Really? What kind of movies do you watch?"

        show lori nervous2 flip

        lori "Uh, scary ones? Ones about existential dread and incomprehensible terrors mostly but I also watch a ton of monster movies."

        player "Nice! That reminds me, I just returned a book on monsters. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        show lori neutral flip

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome! See you there!"

        player "You bet!"
        player "I guess I'll let you get back to your books now. See you later!"


    # if player asked her to turn it down but was nice about it and did startle her
    if loriInteractionNeutral == True:

        player "Oh yeah, I remember you!"
        player "Fitting that you would be in the horror section given what she was listening to earlier."

        show lori neutral flip

        lori "It's kinda my thing. I'm even going to film school to work on horror movies!"

        player "Wow, really? Like slashers and monster flicks?"

        lori "Well yeah, but I also wanna do existential dread and like... incomprehensible terrors and stuff."

        player "That's cool. You get inspiration from books?"

        "You squat down and crane your neck to read the titles of the books in her little pile."

        lori "Yup! I like to doodle scenes I read and that helps me think of new ideas."

        player "Nice. That reminds me, I just returned an encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        lori "Before I forget, what's your name?"

        player "[newname]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I guess I'll let you get back to your books now. See you later!"


    # if player changed seats without talking to her
    if loriInteractionNull == True:

        player "Oh yeah, I remember you!"
        player "Do you live here? I just moved in the other day."

        show lori neutral flip

        lori "Yup! Been here my whole life til I started going to film school a few months ago. I'm here on break now."

        player "Nice! What kind of films do you like?"

        lori "Most kinds, but horror in particular. Like, existential dread and incomprehensible terrors but regular monster movies are cool too!"

        player "Yeah I noticed you have a knack for horror. Funny enough, I just got finished returning a book on cryptids."

        "You squat down and pick up a book from the pile scattered on the floor, reading the title. \"Picnic by the Roadside.\""

        lori "It wouldn't happen to have been \"Cryptids of the Western Hemisphere\" would it?"

        player "How'd you know?"

        lori "I've been looking for that book forever! I used to check it out all the time as a kid but I haven't seen it in a while. It's one of the best encyclopedias on cryptids!"

        player "Hopefully they'll put it on the shelf soon and you can snag it before anyone else does."

        lori "That would make my day."
        lori "What's your favorite cryptid?"
        lori "I know it's kind of cliché but mine's the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"
        lori "Before I forget, what's your name?"

        player "[newname]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I guess I'll let you get back to your books now. See you later!"


    # if player asked about the music and was bold
    if loriInteractionBold == True:

        player "Hey! What a coincidence seeing you here!"

        lori "Not really. Possum Springs is like, really small. We would have run into each other sooner or later."

        player "Seems like it! I don't believe I caught your name earlier. I'm [newname]."

        show lori neutral flip

        lori "Nice to meet you again, [newname]! I'm Lori!"

        player "Whatchya been reading, Lori?"

        "You squat down and take a look at some of the books strewn about. Most of them are from this aisle apparently."

        lori "Just some spooky stories to read in the dark. It's technically studying material."

        player "Studying for what?"

        lori "Film school assignments!"

        "She holds up a book, \"Monster Design in Cinema.\""

        player "Cool! That reminds me, I just returned an encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        player "I guess I'll let you get back to your books now. See you later!"



    # if player asked about the music and was timid or inquisitive
    if loriInteractionNotBold == True:

        player "Hey! I remember you!"
        player "I still haven't gotten around to listening to that album yet but it's on my to do list. Been adjusting after moving in."

        show lori neutral flip

        lori "I get that, resettling and stuff. I've been away from home for a while and I'm getting used to living next to train tracks again."

        player "Oof. I live a little bit away from them and have a bunch of trees to block out most of the noise but the trains are still pretty loud."

        lori "To think I used to play and take naps and read books right between the tracks."

        player "That sounds... dangerous."

        "You squat down and take a look at some of the books strewn about."

        player "You gonna read these by the tracks?"

        lori "Maybe!"

        "You gloss over some of the titles and cover art of the books on the floor. They're all from this aisle apparently."

        player "You a big horror fan?"

        "She giggles."

        lori "Yup! I'm going to school to work on horror films!"

        player "Good luck with that! You certainly seem to have a passion for it!"

        lori "Thanks! I'm mostly into existential dread and unseen forces that mess with your head, but I also have a penchant for slashers and monster movies."

        player "Nice. That reminds me, I just returned an encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        lori "Before I forget, what's your name?"

        player "[newname]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I guess I'll let you get back to your books now. See you later!"

    #####################

    "You give her a friendly smile and stand back up."

    lori "Bye!"

    "She waves a tiny paw at you then resumes reading while you scoot around her and out of the aisle."

    hide lori with dissolve

    "Where to now?"
    "There's still another floor to explore. You've just about exhausted your options on this floor so it's time to head up."
    "The elevator rattles louder this time as its doors open and close, making you question just how safe this thing really is."

    stop music fadeout 2.0

    "Safe enough to get you to the third floor unharmed is the answer you get soon enough."
    "Dust floats through the air, tickling your nostrils as soon as the elevator doors open."
    "The lighting on this floor is much more subdued and the walls are painted a dark blue. "
    "You creep forward, wondering if there's anybody up here."
    "It's dead silent save for the sounds of the heating unit. You pass by each aisle and confirm you're alone."
    "Come to think of it, this whole building is pretty empty. It's just you, Selmers, and Lori, each on different floors."
    "Selmers was right about not many people using the library these days."
    "Getting back to the matter at hand, you wonder what the purpose of this floor in particular is."
    "A quick look around reveals it's for really old media and records apparently."
    "Things like last century's yearbooks, outdated almanacs, newspaper clippings, and even some tomes that remind you of the ones back home."
    "As youre scouting the area, something catches your eye: a big glowing box on one of the desks."
    "It looks like one of those old tube computer monitors, but even bulkier."
    "And warmer."
    "You can feel the heat coming off it from a few feet away."
    "This must be one of those microfilm projector things."
    "A microfiche, you think it's called."
    "There's no film loaded into it though so there's nothing on the screen."
    "Someone must have forgotten to turn it off when they used it last."
    "You flip the power switch off, plunging the room into near total darkness."
    "Welp, that about concludes your tour of the library today."
    "You make your way back to the elevator and return to the ground floor. Selmers should have your card ready by now."
    "As you walk up to the counter empty handed, the bear looks up with a casual grin."

    show selma neutral at right with dissolve:
        yalign selmaheight

    selma "Find what you were looking for?"

    player "Not quite, but that's more my fault than the library's."

    selma "If you're looking for a book in particular, I can help you find it if we have it."

    player "Thanks, I'll keep that in mind."

    selma "I also got your card printed. Here ya go."

    "She slides the card over the counter."

    selma "It expires three years from today, or one year after your last check out. Whichever comes first."

    player "Thank you!"

    selma "Wish I got paid commission for these. But I don't. Haha."

    player "How often do you convince someone to sign up for a card?"

    selma "Almost as often as someone new comes in."
    selma "I have experience in sales."

    player "Wow."

    selma "And if you don't mind me trying to sell you on something else, the library's hosting an event this coming Tuesday at 4:00PM where we read books aloud to small children."
    selma "We're short on staff so we're asking for volunteers."
    selma "It'd be nice if you could, y'know, come and read for the kids. We'll have juice and cookies too."

    menu:
        "I'll think about it.":

            player "I'll think about it."

            selma "That's better than a flat out no I guess."

            "You can't help but feel a twinge of guilt. You look away momentarily, mulling over whether you should go or not."

            selma "Anyway is that all I can do for you?"

            "You refocus your attention back to her."

            player "Oh, yeah. Thanks, have a nice day."

            selma "You too."

        "Sorry, don't think I can make it.":

            player "Sorry, don't think I can make it."

            selma "I expected as much. Don't worry, we'll find someone else."
            selma "Or I'll just pull double duty like last time."

            player "That understaffed, huh?"

            selma "Yup."

            "You can't help but feel some sympathy toward her. Maybe you could come out and help for an hour or two."

            selma "Well if you change your mind, let me know."

            player "Will do."

            selma "Anyway, do you need assistance with anything else?"

            player "Nope. I'm good, thanks."

            selma "K. Have a nice day."

            player "You too."

        "I'd be happy to!":
            player "I'd be happy to!"

            selma "That- was not the response I was expecting. You sure? Those kids can be real punks sometimes."

            player "It's no trouble, I can handle them."

            selma "If you say so. Let me know if you change your mind later."

            player "Sure."

            selma "Thanks though. It means a lot and it would be cool seeing you here."

            "She has a genuinely appreciative smile on her face, but there's something else behind it you can't quite grasp."
            "Does she just want you to come help out or is there more to it?"

            selma "Anyway is there anything else I can do for you?"

            "You refocus your attention back to the conversation at hand."

            player "Oh yeah, no I'm good."

            selma "Ok. Hope you have a nice day!"

            player "Thanks, you too!"


    hide selma with dissolve

    "On your way home, you think about how surprisingly lively Possum Springs is."
    "Already you've been invited to several events and met some pretty cool people."
    "You never imagined how much happier you'd be living out here."
    "When you get to your house, you decide to make some lunch and chill out until evening."
    "Nightfall creeps up on you quickly and you suddenly realize you don't have a specific time to be at the bakery."
    "Wait a minute, bakery? Like the one Gregg and Angus live above?"
    "Surely they'd know something about a party underneath their apartment."
    "You shoot them both a text and wait a while."
    "No response."
    "Screw it, you should just head out now. Better to be early than to arrive after the party's over."
    "You hastily freshen up, then hop on your bike and ride into town."
    "As you pull up to the store, you hear the final notes of a song blasting from inside, rattling the windows."
    "Bright light leaking through inhibits your view of the interior until you step inside and your eyes adjust."
    "Standing on the stage are some familiar faces who are just as shocked to see you as you are to find them here."
    "Gregg with a guitar, Angus at the mic, Mae on bass, and Bea from the hardware store next to a keyboard and laptop."

    show bea at right:
        xalign 2.0

    show angus at left:
        xalign -1.0

    "On the wall behind them is a DVD player screensaver being displayed from a projector mounted on the ceiling."

    show lori neutral at right:
        yalign loriheight
        xalign 1.02
    with dissolve

    lori "[newname]! You made it!"

    "You look to the source of the voice. You didn't even notice the mouse girl sitting at one of the tables. She stands up and runs toward you."

    lori "Sorry I forgot to give you a time to come. To be honest I wasn't sure when we were meeting!"

    player "Uh, it's fine."

    "You're still confused from discovering Gregg and Angus are in a band with Mae and the hardware store girl."

    lori "Guys, this is [newname]! [newname], that's Gregg, Angus, Mae, and Bea!"

    "She points to each of them as she lists their names."

    player "I've already met everyone, actually."

    "Gregg hops down from the stage with his guitar still strapped over his body."

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    with dissolve

    gregg "Yeah, we played video games and ate pizza the other day."

    show lori breath

    lori "Whaaaaaat? Really??"

    show bea neutral at right:
        yalign beaheight
        xalign .9
    with moveinright

    bea "Mae and I saw them at the Ol' Pickaxe too."

    lori "Oh gosh, I-I thought..."

    "Lori trails off and shrinks down in shame."

    show angus neutral flip at left:
        yalign angusheight
        xalign .12
    with moveinleft

    angus "It's cool. [newname] is cool."  

    lori "Sorry for inviting [newname] without knowing if it was ok... I thought it was going to be a bigger party..."

    gregg "No, it's fine. Tell ya what, we'll go out to eat after putting things away here. You hungry, [newname]?"

    player "I could eat."

    bea "I can make time for something quick at the diner. And I can get dinner to-go for my dad while we're there."

    gregg "Cool! Let's pack up and get the heck outta here!"

    "Gregg hops back on stage and kicks open his worn guitar case. Angus, Bea and Mae go ahead and start putting their things away while Lori waits at a table."

    hide lori
    hide gregg
    hide angus
    hide bea
    with dissolve

    show mae neutral at right:
        xalign 1.5

    menu:
        "Offer to help clean":
            #+1 trust

            player "Let me help you with that!"

            show gregg neutral flip at left:
                yalign greggheight
            with dissolve

            gregg "Hm? Oh sure. Can you unplug those amps and put 'em in the storage closet over there?"

            player "'Course!"

            "You readily do as he requested while the others put away their instruments."
            "Angus coils up the mic wire and collapses the tripod while Bea folds up the table her keyboard was on and stuffs the laptop in her bag."
            "Mae strummed on her bass a few times, adjusting the tuning before putting it away in a case and helping out with general cleaning."
            "She was awfully quiet and seemed to keep her distance from you, only occasionally making weird glances in your direction. She whispers something to Bea."
            "You brush it off and finish helping, bumping into Gregg as he stowed the last speaker."

            player "I didn't know you guys were in a band. I thought this was just gonna be a movie party."

            gregg "Is that what Lori told you? We ended up watching the movie early on, then Bea wanted to test a song she's been writing."

            player "Bea writes music?"

            gregg "Yeah, she just finished going to school for that sort of thing."
            gregg "Honestly, I haven't picked up my guitar in ages and kinda suck at playing now."
            gregg "But it was fun getting together and playing again!"

            player "I never would have imagined all you guys were in a band."

            gregg "Believe me, this is the least crazy thing about us."
            gregg "Hey be right back, I need to hit the bathroom."

            hide gregg with dissolve
            show bea neutral at right:
                xalign 2.0

            "The fox locks away all the gear with a key then heads to the back of the building and out the exit door."
            "Rather than question where exactly he's going, you decide to approach Lori who had been seated at a table looking stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine! You guys done?"

            player "I think so. Just waiting on Gregg to get back."

            "You chat with Lori while Mae, Bea and Angus converse amongst themselves."
            "After a minute or so Gregg walks back in and approaches you. The others hop down from the stage and gather around."
            "The crocodile has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright

            bea "Ready to go?"

        "Hang back with Lori":
            $ loriAP = loriAP + 1

            show bea neutral at right:
                xalign 2.0

            "You pull up a seat across from Lori, who looks stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine!"
            lori "...Sorry I made things awkward earlier."

            "You shrug nonchalantly."

            player "Don't worry about it. It all worked out in the end."

            if loriAP > 1:
                lori "Shame you missed out on the movie though... maybe we can watch it together another time?"

                player "I'd love that! It's been ages since I've last seen it!"

                lori "I watch it every year hahaha!"

            else:
                lori "Yeah..."

            "Out of the corner of your eye you see Gregg rush out the exit toward the back of the building while the others finish putting everything away."

            player "Hey so, dumb question, but are they like, in a band?"

            "You gesture toward the group on the stage."

            lori "Oh! Yeah, well, they used to be. But Bea just finished her degree in music studies and wanted to test a song she's been writing so they brought out all their old instruments."

            player "Wow. Did it turn out well?"

            lori "Nnnnot really. Gregg's pretty rusty with his guitar."
            lori "Don't let him know I said that though!"

            "Just then, Gregg returns from whatever it was he was doing and everyone gathers around the table you and Lori are seated at."
            "Bea has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright
            
            bea "Everything's packed up. You ready to go?"


    show angus neutral at left:
        yalign angusheight
        xalign -1.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.2
    with moveinleft

    gregg "Yup!"

    show angus neutral flip at left:
        yalign angusheight
        xalign .12
    with moveinleft

    angus "Indeed!"

    lori "Mh-hm!"

    player "Yeah!"

    show mae sad1 at right:
        yalign maeheight
        xalign .67
    with moveinright

    mae "Sure."

    "Bea adjusts her grip on the keyboard and turns toward the door."

    bea "Let's roll."

    hide mae
    hide gregg
    hide bea
    hide angus
    hide lori
    with dissolve

    "You all file out through the doorway and into the cold dark street."

    show bea neutral at right:
        yalign beaheight
        xalign 1.08
    with dissolve

    "Bea turns toward the group and does a headcount."

    bea "There's too many of us to fit in my car so I guess we're walking."

    show angus neutral flip at left:
        yalign angusheight
        xalign .08
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.1
    with dissolve

    gregg "I volunteer to sit in Angus's lap to make space."

    bea "That would work if I didn't have a big box of records in the passenger seat, and a keyboard soon to be occupying the back."

    gregg "Aww."

    hide gregg
    hide angus
    with dissolve

    bea "Be right back."

    hide bea with dissolve

    "Bea starts toward the Ol' Pickaxe where her car is parked."

    show mae panic flip at left:
        yalign maeheight
    with dissolve

    mae "I'll go with you!"

    "Mae hastily runs off to catch up to Bea."

    show mae at right:
        yalign maeheight
        xalign 2.0
    with move
    show bea at right:
        yalign beaheight
        xalign 2.0

    "You consider going with them just so your body can warm up by walking but the moment of opportunity has already passed."
    "You're all just standing here with nothing else to do so why not break the ice?"

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    show lori neutral at right:
        yalign loriheight
        xalign 1.06
    with dissolve

    player "So why is there a stage in the middle of the bakery?"

    angus "It's a holdover from the previous business. We used to break in and play music on it way back in the day."
    angus "No need for breaking in now."

    gregg "Lame."

    angus "Nowadays it usually gets used for banquets and whatever other local events need a stage."

    lori "Like the Harfest play!"

    gregg "Yeah, like that thing literally nobody cares about but we still do for some reason."

    "You stand around idly chatting waiting for Mae and Bea to come back."
    "How long does it take to put away a keyboard??"

    show bea neutral at right:
        yalign beaheight
        xalign 1.0
    with moveinright
    show mae sad1 at right:
        yalign maeheight
        xalign .7
    with moveinright

    "Seems Lori was thinking the same thing. When the pair finally return, she makes a quip."

    lori "Did ya get lost along the way?"

    bea "Har har. Come on, we doing this or not?"

    mae "Yeah. Let's go."

    hide gregg
    hide angus
    hide lori
    with dissolve

    "Bea stands between you and Mae as your party advances, footsteps crunching against the snow."
    "While the others joke and converse, you sneak a glance at Mae. You can feel that there's something conflicting her and that she doesn't want to be here."
    "Unfortunately you don't know what you can do about it other than feel bad for her."

    hide bea
    hide mae
    with dissolve

    show mae neutral at right:
        xalign 2.0

    "The diner turns out to only be a few blocks away. It's a repurposed train car with an orange neon sign reading CLIK CLAK DINER."

    show angus neutral left:
        yalign angusheight
        xalign -2.0
    show lori neutral right:
        yalign loriheight
        #xalign 2.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.15
    with dissolve

    gregg "Here we are!"

    "Gregg holds the door open for everyone. Inside, you're met with a cramped, cluttered space, vaguely reminiscent of Art Deco design, covered with photos, paintings, and other artwork on the walls."
    "You're seated at a booth and given a menu that has the typical diner offerings."
    "Pizza, burgers, bacon and eggs, club sandwiches, and even pierogies. You all make your selections and chat while the food is cooked."

    show bea neutral at right with dissolve:
        yalign beaheight
        xalign 1.18

    bea "So [newname], I heard you moved here recently? What are you doing in Possum Springs?"

    player "Eh, just wanted to get away from home, ya know? Move out and be independent and all that stuff."
    player "I have to say, I'm enjoying Possum Springs a lot more than I thought I would."

    bea "Really? Almost everyone I know can't wait to escape from here."

    "A subtle hush falls over the group. Bea quickly changes the topic."

    bea "Anyway, you got a job here yet?"

    player "Nope. Living off of savings at the moment. Why, you know anybody who's hiring?"

    show lori neutral at right:
        yalign loriheight
        xalign .85
    with dissolve

    lori "I could scrounge together something and pay you a little if you help me work on my movie."

    player "You're making a movie?"

    lori "Yup! It's partly a school project but it's also something I just wanna do."
    lori "I'm out in the woods or by the tracks nearly every day if you wanna come and watch or set up equipment or maybe even act in it?"

    player "Sounds spooky. I'll definitely consider it."

    "Lori giggles at your choice of words."

    bea "*Ahem*"
    bea "I could use a hand at the shop if you're interested. Backbreaking work but decent untaxed, under the table pay."

    player "What do I have to do?"

    bea "Lift heavy stuff, maybe direct a customer toward said heavy stuff, and on rare occasion move the heavy stuff to their car."

    player "Noted. I'll consider that as well."

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    with dissolve

    gregg "I could try putting in a good word for you at Ham Panther. I don't think they're hiring right now though."

    angus "I've got my hands full just trying to pay myself at the bakery so..."

    gregg "Maybe Mae could get you something at the arts council if you're into that."

    "All eyes turn toward an unsuspecting Mae. She looks like she wasn't paying much attention to the conversation and was caught off guard."

    show mae panic at right:
        yalign maeheight
        xalign .7
    with dissolve

    mae "Oh uh, yeah. I teach art stuff at the Deep Hollow County Arts Council on Fridays and Saturdays. Painting, clay sculpting, photography..."

    lori "Mae's the one who taught me how to use a camera!"

    show mae sad1

    "Mae shrugs."

    mae "At this point, Lori's more comfortable with cameras than I am. I just know enough to teach the basics."

    player "Gotchya. I'll check it out if I'm feeling artsy."

    show mae neutral

    "Mae flashes you a forced smile. Luckily the awkward moment is interrupted by the waitress coming by with your food."
    "Food has a way of lightening the mood. Mae relaxes and even becomes more talkative as the evening goes on."
    "Even though your meal isn't very good, you still have a pleasant time with your new friends."
    "Towards the end of the night, Bea gets a box for her leftovers and the waitress drops off the meal she ordered for her father."
    "When it comes time to pay the bill, Gregg insists that he cover for you but you politely decline, knowing you can spare the cash more comfortably."
    "Ironically, Angus is the one to put down his debit card for both him and Gregg, though you suspect they share a bank account."
    "Bea pays for her own, and Mae asks the waitress to put hers and Lori's meals on one bill."

    show mae blush

    "Lori wordlessly expresses her gratitude by resting her head on Mae's shoulder and wrapping her arm around Mae's. For the first time this night you see Mae smile in earnest."

    #scene transition

    show mae neutral

    "Once you're outside, you all crowd around under a streetlight and discuss your plans for the rest of the night."

    gregg "This was great. We should do this again."

    lori "Yeah, it was awesome seeing you guys playing as a band again!"

    "Bea lights a cigarette."

    bea "Always a joy. But I think I'm gonna go home, relax and watch some TV with my dad now."

    lori "Hmm, yeah I should get home too before my dad starts worrying where I am so late."

    mae "I'll drive you home so you don't have to walk back in the dark Lori."

    lori "Thanks!"

    gregg "Me and Angus will probably watch some streams then go to sleep."

    player "Yeah, sleep sounds good right about now. It was fun hanging out with you all though."

    bea "Before I forget, you have Chattrbox right? Add me and we can talk more about having you work at the Pickaxe."

    lori "Oh and add me too in case you decide to help me out on my film!"

    "You pull out your phone and get their Chattrbox names."
    "You'll have to wait until you have wifi again before it registers but it's no big deal. You pocket your phone and give them a smile."

    player "Sweet. I'm open to just chatting too if you want."

    bea "Sure."

    lori "Of course!"

    hide lori
    hide gregg
    hide angus
    hide bea
    hide mae
    with dissolve

    "You walk as a group back to the bakery before parting ways. Gregg and Angus go around to the back of the building, while Mae, Bea and Lori go to the parking lot by the Ol' Pickaxe."
    "You hop on your motorcycle and rev her up for the trip home, where you promptly get ready for bed."
    "You add Bea and Lori to your Chattrbox then set your phone to 'Do not disturb' mode and fall asleep with your face buried in your pillow."



    # Day 6, sunday
    $ currentDate = "December 12"

    "Your first week in Possum Springs has come to a close."
    "Really this is only your sixth day here, but it's Sunday so you're counting it as having been a week."
    "Each new day further cements your routine. Wake up, shower, eat breakfast, play around on the internet for a bit, and so on."
    "The excitement of moving into an unfamiliar town has worn off, yet you still seek the thrills you've felt over the past few days."
    "You should get out of this dusty old house and go on an adventure today."

    #scene bg outsidePlayerHouseSnowClearSky
    #door opening sound effect

    "The snowstorm has finally subsided."
    "The skies are bright and clear once again, but the ground is going to be covered with a thick blanket of snow for a while."
    "That shouldn't hinder your ability to get around though."
    "Now then, where shall you go?"

    jump locationMenu

    label locationMenu:

    # if all scenes have been played, jump to end scene
    if beenToChurch == True and beaSelmaPoetry == True and maeLoriSleepoverCompleted == True:
        "end scene"

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Church of the First Coalescence" if beenToChurch == False:
            jump week1Church
        "Ol' Pickaxe" if beaSelmaPoetry == False:
            jump olPickaxeWeek1
        "Wander Around" if maeLoriSleepoverCompleted == False and beenToChurch == True:
            jump wander
        #"Town Center":
            #jump townCenter
        #"Possum Springs General Area":
            #jump psGenArea
        #"Outskirts":
            #jump outskirts

    label townCenter:
    
    menu:
        "{cps=0}Where do you want to go?{/cps}"
        #"Bear Essentials Bakery":
        #    jump bearBakery
        "Church of the First Coalescence":
            jump week1Church
        "Ol' Pickaxe":
            jump olPickaxeWeek1
        #"Trolley Tunnel":
        #    jump tunnel
        "Back":
            jump locationMenu

    label psGenArea:

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        #"Cafe":
        #    jump cafe
        #"Library":
            #jump libraryWeek1
        #"Train Tracks":
        #    jump tracks
        "Wander Around":
            jump wander
        "Back":
            jump locationMenu

    #label outskirts:
    #menu:
    #    "{cps=0}Where do you want to go?{/cps}"
    #    "Arts Council":
    #        jump artsCouncil
    #    "Ham Panther":
    #        jump hamPanther
    #    "Woods":
    #        jump woods

    #label artsCouncil:
    #"arts council"

    #label cafe:
    #"cafe"

    #label bearBakery:
    #"bakery"

    label week1Church:
        #if beenToChurch == False and currentDate == "December 12":
            #jump churchScene1
        #elif beenToChurch == True and currentDate == "December 12":
            #jump churchScene2
        #elif beenToChurch == False and currentDate != "December 12":
            #jump firstChurchNotDec12
        #elif beenToChurch == True and currentDate != "December 12":
            #jump churchNotDec12
        jump churchScene1


    label churchScene1:
        $ beenToChurch = True
        scene bg church_exterior with fade

        "It's quite a climb up the hill to the church but you're rewarded with a pretty view when you reach the peak."
        "You can see for miles from up here."
        "Forests near and far, fields in the distance, all the buildings in town... You think you can make out the top of your house from here too!"
        "The church itself is as impressive as the library. Not surprising, considering the type of folk who live around these parts."
        "Stained glass decorates the front of the classically designed stony architecture and it's one of the few places in Possum Springs lacking graffiti of any kind."
        "Seems that the statue of the fire-breathing pope guy by the welcome sign is doing a good job of guarding the premises."
        "Behind the building, there's a wide hill that hosts a cemetery."
        "Damn, what a way to put a damper on the otherwise pleasant mood the church brings."
        #wind sound effect
        "You shiver. It's pretty windy way up here."
        "You wonder who's idea it was to put a church at the top of such a tall hill."
        "Since you're here, you might as well check out the inside."

        scene bg church_interior with fade
        play music "/music/andalsowithyou_v2loop.mp3" fadein 1.0

        "You push through the doors and find the interior to be almost as bright it is outdoors, thanks to the large windows lining the walls."
        "Much like the outside, the walls are a clean blue and the doors a fresh red, giving it a modern twist on the traditional aesthetic."
        "As you pass by the sanctuary doors, they suddenly open and a procession of churchgoers come pouring out."
        "Some walk right past you, giving you friendly smiles and hellos on their way to the exit, while others hang back and chat among themselves here in the lobby."
        "To your surprise, you spot Mae amid the last to pass through the doors, accompanied by who you can only assume are her parents."
        "Mae impatiently drags them toward the front door until she notices you, whereupon she jumps back in shock."

        show mae freakout at right with dissolve:
            yalign maeheight

        mae "Oh. It's you."

        "You get the feeling she wants to leave as soon as possible so you keep your response short."

        player "Hey Mae. I was just passing through. Guess I'll see you lat-"

        show stan neutral flip:
            xalign .22
        show candy neutral flip:
            xalign -.1
        with dissolve

        stan "Well hello there! I believe we've met before at the Ham Panther. Good seeing you again!"

        if gender == "masculine":
            candy "You all know each other already? I feel so left out! Mae, is this your boyfriend?"
        elif gender == "feminine":
            candy "You all know each other already? I feel so left out! Mae, is this your girlfriend?"
        elif gender == "neutral":
            candy "You all know each other already? I feel so left out! Mae, is this your... er... boyfriend? Girlfriend? I'm sorry, I can't quite tell."

        mae "What? No!"

        "Dammit, Mae's parents aren't going to let you get away that easily."
        "You give them a cordial nod and introduce yourself."

        player "Hi there. I'm [newname]. I just moved in last week."

        candy "Nice to meet you [newname]! I'm Mae's mother, Candy."

        stan "I don't have my name tag on me at the moment but rest assured I'm still Stan."
        stan "Working at the Panther is my just part time job. Raising Mae is my full time one hahaha!"

        "Great, dad jokes. You grin and bear it."
        "Mae is more up front in her distaste for them and tries to pull her parents away."

        show mae grump

        mae "Ugh you're embarrassing me, Dad! Let's go already!"

        candy "Hold on kitten, I promised I'd give Dorothy my recipe for peppermint cake."

        mae "It's literally just vanilla cake mix and crushed peppermint!"

        stan "And I wanted to see what Jacob's been up to lately."

        mae "You see him literally every day at work!!"

        candy "Why don't you show your new friend around, Mae? We won't be long."

        mae "Ugggghhhhhh!!! Why aren't you listening to me!"

        show mae grump flip at offscreenright with move:
            yalign maeheight

        "Mae storms off toward the main entrance."

        mae "I'll be waiting for you outside! Getting frostbite!!"

        candy "Oh dear, she's been so rambunctious lately. What a shame, I thought she'd finally grown out of it..."

        stan "She gets it from your side of the family."

        candy "I'm so sorry, [newname]. Could you go check on her? She's a lot to handle but she's sweet once you get to know her, I promise."

        player "It's ok. I'll go make sure she's alright. It was nice meeting you."

        candy "Oh thank you! We'll catch up later!"

        player "No problem. See you around!"

        stan "See ya!"

        hide stan
        hide candy
        with dissolve

        stop music fadeout 2.0

        scene bg church_exterior with fade

        "You step outside and take a look around, keeping an eye out for Mae."
        "You find her sitting on the corner of the podium the bird statue rests upon, facing away from you as you approach."

        player "Hey."

        show mae sad1 flip at left with dissolve:
            yalign maeheight

        "Mae looks over her shoulder and sighs."

        mae "Hey. Sorry about all that."

        menu:
            mae "{cps=0}Hey. Sorry about all that.{/cps}"
            "It's whatever.":
                $ whateverFine = "whatever"
                $ fineWhatever = "fine"
            "It's fine.":
                $ whateverFine = "fine"
                $ fineWhatever = "whatever"

        player "It's [whateverFine]."

        "Mae doesn't respond."
        "Your brain scrambles to try and think of something else to talk about."
        "Uhhhhhhh..."

        player "I didn't know you go to church."

        mae "Only on Sundays. It makes my parents happy."

        player "Your parents are nice."

        mae "Yeah. I shouldn't make things so hard for them."

        player "You need a ride home?"

        mae "Nah. I could walk home but my family always gets lunch after church."

        jump churchStayAndTalk

        #menu:
            #"Stay and talk more":
                #jump churchStayAndTalk
            #"Leave":
                #player "Alright. Just wanted to check on you. I'll be off now."

                #mae "Cool. See you."

                #"You leave her be and walk back to your bike."

                #"Where to go now?"

                #jump locationMenu



    label churchScene2:
        "You make it up the hill to the church and come up to Mae, who is still sitting by the welcome sign."

        player "You haven't left yet?"

        mae "What's it look like?"

        menu:
            "Stay and talk more":
                jump churchStayAndTalk
            "Leave":
                player "Alright. Just wanted to check on you. I'll be off now."

                mae "Cool. See you."

                "You leave her be and walk back to your bike."

                hide mae with dissolve

                "Where to go now?"

                jump locationMenu

label churchStayAndTalk:

    $ maeAP = maeAP + 1
    $ maeChurch1 = True

    "You brush aside the snow from the top of the steps and sit down, your feet dangling from the edge."
    "Mae seems to forget you're there after a while. She looks over her shoulder at you again."

    mae "You're still here?"

    player "Is that a problem? I'll leave you alone if you want."

    mae "Nah, it's [fineWhatever]."
    mae "...Hey I have a question for you."

    "Mae turns toward you."

    mae "Are you actually religious?"

    menu:
        "Kinda? I don't know.":
            player "Kinda? I don't know."

            mae "That's pretty much how I feel."
            mae "Like, I'm pretty sure there's some supernatural stuff in the universe but maybe it's just in my head."
            mae "And even if it is real, who's to say this religion is correct or if that one is, or more likely it's one that hasn't been invented yet."

            player "That's one way to think about it."
            player "I don't believe we're going to Hell or whatever just cause we didn't happen to worship the right god."
            player "Maybe it doesn't even matter who's running the universe or what happens when we die. What we believe doesn't change reality."
            player "I mean, if we're on a ship that's heading somewhere and we can't control it, it'll arrive at the same place regardless of where we choose to believe it's going, if that makes sense."

            mae "I guess."
            mae "It's just--"
            mae "When you witness something that doesn't make sense, the only way to explain it is to believe there's a higher power controlling things behind the scenes, you know?"

            player "Yeah."

            mae "I dunno, I feel like some things are meant to happen but I can't figure out *why.*"

            player "Hm. I dunno either."
            player "Maybe we're just like ants to some cosmic god and we're not really meant to understand things outside our influence."

            mae "Oh well. Church can be fun sometimes at least. The people are kind. We help the community. And there's food involved. I can't complain."

        "Not really.":
            player "Not really."

            mae "Why'd you come here then?"

            player "I dunno. Even if I don't believe in this stuff I still find it interesting."

            mae "That's fair I guess. I'm not really sure if I believe in it myself."
            mae "I mean, there's stuff that I can't explain without saying God did it or whatever but that doesn't necessarily mean there is actually a God."

            player "That doesn't mean there *isn't* actually a God though."

            mae "I know! And that's what makes it frustrating!"
            mae "Never knowing for sure."

            player "I try not to think about it. It doesn't really impact my life one way or another."

            mae "I envy people who can think like that."
            mae "Oh well. Even if it is all a sham, church can still be fun. The people are kind. We help the community. And there's food involved. I can't complain."

        "Yeah.":
            player "Yeah. I'm not super into it but I do believe there's a God or something like that."

            mae "That's about how Bea feels too."

            player "What about you?"

            mae "I dunno. I change stances like every month and I'm not sure which side I'm rooting for."

            player "I hope you find the answers you're looking for one day."

            mae "That's just it, the lack of answers means it can go either way! How am I supposed to know anything?"

            player "It's not about knowing, it's about believing."

            mae "Now you sound like Pastor Kate."

            player "Well it's true."
            player "Even if I *knew* there wasn't a God I could still believe in one."
            player "It's the principle that matters."

            mae "Mmh, I guess."

            "Mae looks down at the snow on the ground."

            mae "Oh well, even if I don't get it, church can still be fun. The people are kind. We help the community. And there's food involved. I can't complain."


    player "Heh."

    show mae neutral flip

    "Mae finally eases up and cracks a smile."

    if newname.upper() == "AUTUMN":
        mae "Y'know you're pretty weird, Autumn."
        mae "But like, good weird."

        player "Thanks?"


    "A sudden uproarious laughter coming from the church entrance interrupts your conversation."
    "A group comes walking out but Candy and Stan are nowhere to be found."

    mae "You don't have anywhere to be do you? I think I'm gonna be stranded here for a while."

    player "Nope!"

    mae "Good, cause I don't wanna be stuck out here freezing *and* alone!"

    "The two of you chat about philosophical stuff you both barely comprehend for what feels like hours until Mae's parents eventually come out and call for her."

    mae "That's my cue to go. Thanks for coming out and talking with me."
    mae "I was already bored to tears during service and my parents take F O R E V E R getting ready to leave."

    player "Anytime."

    "You give her a wave as she runs past you toward the church."

    mae "See ya around!"

    player "See ya!"

    hide mae with dissolve

    "You stick around for a while enjoying the comfy scenery before deciding to head back home and make some lunch for yourself."

    jump returnHomeDec12



label firstChurchNotDec12:

    $ beenToChurch = True

    "It's quite a climb up the hill to the church but you're rewarded with a pretty view when you reach the peak."
    "You can see for miles from up here."
    "Forests near and far, fields in the distance, all the buildings in town... You think you can make out the top of your house from here too!"
    "The church itself is as impressive as the library. Not surprising, considering the type of folk who live around these parts."
    "Stained glass decorates the front of the classically designed stony architecture and it's one of the few places in Possum Springs lacking graffiti of any kind."
    "Seems that the statue of the fire-breathing pope guy by the welcome sign is doing a good job of guarding the premises."
    "Behind the building, there's a wide hill that hosts a cemetery."
    "Damn, what a way to put a damper on the otherwise pleasant mood the church brings."
    #wind sound effect
    "You shiver. It's pretty windy way up here."
    "You wonder who's idea it was to put a church at the top of such a tall hill."
    
    "placeholder"
    "Nothing noteworthy happens and you leave. (Come here on sunday for mae scene)"





    jump locationMenu

label churchNotDec12:
    
    "placeholder"
    "You go up to the church but nothing noteworthy happens. (Come here on sunday for mae scene)"





    jump locationMenu




    label olPickaxeWeek1:
        # make beaSelmaPoetry available only after the cafe meetup

        scene bg pickaxe with fade

        play music "music/picknaxe_loop.mp3" fadein 1.0

        "You head down to the hardware store and find Bea manning the counter."

        show bea apron at right with dissolve:
            yalign beaheight

        bea "Hey [newname]. Me and Selma are going out to the Arts Council tonight for some poetry. You wanna come?"

        player "Sure!"

        bea "Meet us there at around 7:00, k?"

        player "Sounds good. See you then!"

        stop music fadeout 2.0

        bea "See ya."

        hide bea with dissolve

        jump beaSelmaPoetry


        #menu:
            #"Sure!":

                #player "Sure!"

                #bea "Meet us there at around 7:00, k?"

                #player "Sounds good. See you then!"

                #stop music fadeout 2.0

                #bea "See ya."

                #hide bea with dissolve



                #jump beaSelmaPoetry
            #"Nope.":

                #player "Sorry, I think I'm busy around that time."

                #bea "No big deal. See ya around."

                #stop music fadeout 2.0

                #player "Bye!"

                #hide bea with dissolve

                #jump locationMenu


    #label tunnel:
    #"trolley tunnel"

    label libraryWeek1:
    "library"
    #temp jump to beaselmapoetry scene
    jump beaSelmaPoetry

    #label tracks:
    #"train tracks"

    label wander:
    if firstWander == True:
        "Today feels like a good day to just wander around and familiarize yourself with the area."
        "And who knows, you might find something interesting."
        "Your stroll through town gives you a chance to clear your head and subconsciously memorize street layouts and pathways."
        "You even find a convenient shortcut to town center through a back alley. You'll certainly be taking advantage of that later on."
        "All around though, it's a pretty quiet and uneventful day in Possum Springs."
        $ firstWander = False
    else:
        "You could go for another walk around town. If nothing else, it's calming and there's always a chance you'll find something interesting."

    if maeLoriSleepoverCompleted == False:
        #and date is compatible
        jump maeLoriSleepover
        

    #label hamPanther:
    #"ham panther"

    #label woods:
    #"woods"


label beaSelmaPoetry:
    $ beaSelmaPoetry = True

    scene bg arts_council with fade
    play music "music/Ecitara.mp3" fadein 1.0

    "You pull into the arts center parking lot at 7:00 sharp after killing some time at home."
    "Turning off the engine, you dismount your bike and walk toward the building where Bea and Selma are already standing near the entrance."
    "Bea's got a cigarette between her lips. The tip of it lights up against the darkness, followed by a thick cloud of smoke spewing from her mouth."
    "She nods while Selma talks."
    "As you get closer, you can start to pick up on their conversation."

    show bea neutral flip at left:
        yalign beaheight
    show selma neutral at right:
        yalign selmaheight
    with dissolve

    selma "...and they still haven't read it."

    bea "Uh huh."

    selma "Like I'm not worth their time."

    "Bea scoffs."

    bea "Eff them."

    selma "Yeah..."
    selma "Hey, [newname]."

    "Bea turns and nonchalantly greets you."

    bea "Hey."

    player "Nice night for some poetry, huh?"

    bea "Sure is."

    stop music fadeout 2.0

    bea "Come on, let's go inside. I'm sick of standing out in the cold."

    scene bg arts_council with fade
    play music "music/Distant.mp3" fadein 1.0

    "You hold the door open for the ladies and follow them inside where the receptionist welcomes you all warmly."

    receptionist "Well if it isn't Possum Springs' lovely pair of poets! And I see you brought a guest."

    selma "Evening Marcie."
    selma "And yeah, we're excited to show off to [himherthem]."

    marcie "I'm sure your friend will enjoy your performances!"

    bea "Thanks. You're free to join us if you've got a minute."

    marcie "I'd love to, but sadly I can't abandon my post."

    bea "We understand. Maybe next time?"

    marcie "Maybe!"

    selma "You know where to find us if you change your mind."

    marcie "I sure do. Have fun!"

    "Bea and Selma usher you out of the reception area, through a corridor and into an auditorium."
    "Dim lights illuminate a wooden stage like the kind you'd see for orchestral concerts and plays, complete with velvet red curtains."

    selma "Go ahead and sit wherever, [newname]. I'll be in the control booth messing with the lights and stuff."

    player "Ok!"

    hide selma with dissolve

    "Selmers goes off to take care of that, leaving you and Bea alone as you walk toward the stage."
    
    player "You do this often?"
   
    bea "About as often as we have new poems."

    player "And they just let you use this place whenever?"

    bea "As long as it's not being used for anything else."

    player "That's awful nice of them."

    bea "Yeah it is. The library used to host official monthly poetry meets but that died out."
    bea "Selma was pretty upset about that so I started hanging out with her more, reading poems and lyrics at my place."
    bea "Then we started doing 'em wherever around town."
    bea "Selma likes the acoustics in the old subway tunnels in town but it's cold down there and the arts center has heating."
    bea "And we like the stage. Makes us feel like we're a big deal."

    player "You ever draw an audience?"

    bea "You mean like now? Sometimes."

    hide bea with dissolve

    "Bea climbs the stairs onto the platform and disappears behind the curtains while you pick a seat in the front row."
    "You didn't expect to have such a theatrical setting for the performances tonight. You're filled with anticipation as you wait to hear Bea's poem."
    "Suddenly a voice calls out from the speakers."

    selma "And now for Possum Springs' prime songwriter! Give it up for Beatrice Santello!"

    "Audience cheers and claps come through the speaker from a soundboard. You laugh and join in on the applause as the curtain pulls away."

    show bea neutral flip at center with dissolve:
        yalign beaheight

    "A spotlight turns on, revealing Bea standing in the center behind a microphone."
    "You can tell she's trying not to smile but the moment gets the best of her. She chuckles and shakes her head as the clapping fades away."

    bea "Alright, alright, um this isn't anything special, it's just some scrapped song lyrics I was working on."
    bea "Ok, here goes."

    "She pulls out a crumpled piece of paper and reads from it, tapping her foot to a tempo."

    bea "I drive through the night\nRight after we fight."
    bea "I know you were right\nBut I don't care."
    bea "I'm takin' a flight\nI don't know where."
    bea "I thought I'd share.\nIt's up in the air."
    bea "Wherever I land\nI'm hoping it's bright."
    bea "You'll be gone and\nI'll be alright."
    bea "I'd rather be there\nWith you."
    bea "But life ain't fair.\nWhat else is new?"

    "..."
    "There's a pause followed by the sound of clapping coming from the control booth."

    selma "Damn, girl! You killed it!"

    "You join in on the applause."

    player "Woo! Way to go Bea!"

    "Bea can't even attempt to hide her grin."

    bea "Thank you, thank you! You're too kind!"
    bea "You're up next, Selma!"

    hide bea with dissolve

    "Bea hops down from the stage and swaps places with Selmers. A moment later, Bea's voice comes through the speakers."

    bea "Give it up for our prized poet, Selma Ann Forrester!"

    "More cheering comes from the speakers as you clap."

    show selma neutral at center with dissolve:
        yalign selmaheight

    "Selma takes a half step closer to the microphone and clears her throat."

    selma "*Ahem.* Thanks."
    selma "I've got two poems for you folks today. The first one is called \"Today.\""
    selma "..."
    selma "Today is a snow day"
    selma "So I thought I'd say"
    selma "Hey"
    selma "Wanna come out and play?"

    "..."

    selma "That's it."

    "Bea hits the soundboard applause button again."

    bea "Short and sweet!"

    player "Very nice!"

    selma "I've got another one but I wanted to see if [newname] would like to have a turn on the stage."
    selma "You can borrow one of my poems if you don't have one memorized."

    menu:
        "Recite a poem":
            #+1 Selma AP
            $ audiencepoet = "poet"
            player "Sure! I don't know any poems off the top of my head though."

            selma "Not a problem."

            "Selma pulls out a small notebook while you climb on stage. She flips through a few pages then stops at one and points out one of many poems on the page that she wants you to read."

            selma "Go ahead and read that one."

            player "K."

            hide selma with dissolve

            "You take the notebook from her and she finds a seat to watch from."
            "Wow, being up here in the lights is kinda nerve-wracking. You adjust the mic and look down at the words on the page."

            player "Um, this one is called \"There's Something Strange in Possum Springs.\""
            player "Here in Possum Springs"
            player "Where the phones don't ring"
            player "And the air is spooky"
            player "It sounds kinda kooky"
            player "Our town is full of thrillers"
            player "Talk of ghosts and killers"
            player "Stories shared at Miller's"
            player "As the wind outside gets shriller"
            player "Don't know what it is"
            player "Next time I'll check it out"
            player "Or perhaps it's none of my business"
            player "Don't have the guts, don't have the clout"

            show selma neutral flip at left with dissolve:
                yalign selmaheight

            selma "Nice! You did great!"

            bea "Yeah that was really good, [newname]!"

            "Admittedly you feel a bit silly being in the literal spotlight reading poetry for only two people, but it's also gratifying to be included and appreciated in something like this."
            "You do a quick bow then give the notebook and the stage back to Selmers."

            show selma at center with dissolve:
                yalign selmaheight

            selma "Ok, this one is called \"Morning Stars.\""

        "Don't recite a poem":
            #+1 cynicism
            $ audiencepoet = "audience"
            player "Nah, I'd probably screw it up."

            "Selmers shrugs."
            selma "If you say so. I guess I'll read my next poem then. This one's called \"Morning Stars.\""

    selma "When I really wanted to sleep in."
    selma "One night I was having trouble sleepin'"
    selma "So I rolled out of bed pretty early"
    selma "Already feelin' kinda girly."
    selma "Went upstairs to make hot cocoa"
    selma "Then stared out through the window."
    selma "That's when I saw the twinkling stars"
    selma "Looking down at me from afar."
    selma "I went out and sat on the porch"
    selma "Til the sun rose up like a torch."
    selma "Turning the sky all blue"
    selma "And making the stars just a few."
    selma "After they were done disappearin'"
    selma "Is when I decide to go back in."

    stop music fadeout 2.0

    "..."

    harleyunknown "Yay Selmers!"    

    "A young cat girl with dark brown fur comes running down the aisle and clambers up the stage to give Selmers a hug."

    show selma neutral flip at left with dissolve:
        yalign selmaheight

    selma "Hey kiddo. What are you doing here? You shouldn't be wandering around town so late."

    harley "But it's fun! And I got to hear your poem! You write good poems!"

    selma "Aww, thanks."

    "Selmers picks the girl up in a motherly fashion."

    selma "Oof! You're getting heavy!"

    harleyunknown "Nuh uh!!!"

    "Bea comes down from the control booth while Selmers descends the stairs to the main floor."

    show bea neutral at right:
        yalign beaheight
    with moveinright

    bea "Is that one of the Harley kids?"

    selma "Yup. [newname], this is one of the kids I used to babysit."

    harley "Mom says I don't need a babysitter anymore!"

    selma "True, you're a big girl now. That doesn't mean you can prowl around at night though."
    selma "Come on, let's get you home."

    harley "But I wanna stay and hear more poems..."

    selma "Later, I promise. Your parents are probably worried sick about you."

    "Selmers says she was a babysitter but the way she acts is more like an older sister."
    "She carries her the whole way as you all leave the arts center building and step into the parking lot."

    selma "Well, I guess this is where we part ways, [newname]. Bea and I drove together so we'll take her car to drop off little old Harley here."

    player "Alright, I'll catch you guys later. I had a really fun night with you all!"

    bea "Totally. You were a great [audiencepoet] tonight!"

    selma "Take care!"

    "Selmers waves with her free hand as she opens the back seat door of Bea's car and gently sits the kid down in."

    hide bea
    hide selma
    with dissolve

    harley "Bye, [newname]!"

    "You can see her shouting and waving to you through the window."

    "You smile and give her a wave back before turning to your motorcycle and riding home."

    

    jump returnHomeWeek1

label maeLoriSleepover:
    "As you're about to call it quits and find something else to do, you spot an object half buried in the snow on the sidewalk across the street."
    "It appears to be some sort of zippered pouch."
    "A more thorough investigation reveals the design printed on it, a cat with a knife stuck through their hat."
    "Is this somebody's wallet? Should you pick it up? Nobody is around to witness you."

    label maeLoriSleepover2:
        label maeLoriSleepover3:

    #menu:
        #"Pick it up":
            #+1 mae ap
            #+1 lori ap
            $ maeLoriSleepoverCompleted = True
            "It might have something valuable inside, and you wouldn't want some delinquent making off with it if you can help it."
            "At least, that's what you tell yourself."
            "You stoop down to pick it up and can immediately tell it's full of something by the heft of it."
            "Unzipping it, you see it's full of coins, dollar bills, some personal items, and a few cards stuffed in the slots sewn into the sides."
            "You remove what looks like a driver's license and discover that it belongs to none other than Mae Borowski!"
            "You should return this to her as soon as possible! But... where does she live?"
            "Fortunately the license has her address listed on it. Maple Street, huh?"
            "You recognize that name but you're unsure where exactly Mae's house is on it. It's a pretty long stretch of land after all."
            "Better hurry and find it before it gets too dark out. Mae is probably freaking out over her lost wallet."

            scene bg street with fade

            "Welp, you searched the whole street all the way from town center to the highway."
            "Just as you feared, the sun has gone down and the location of Mae's house has eluded you."
            "All you can do now is go back home and try again tomorrow."
            "Hold on, what's that up ahead?"
            "You can make out the sillhouette of someone across the street. It's too dark to see any distinguishing features but you can tell they're wearing a backpack."
            "Only when the figure crosses underneath a streetlight do you realize it's Lori!"
            "You give her a wave but she must not be able to see you in the darkness. Instead, she turns toward one of the houses and knocks on the door."
            "Shortly after, she's greeted by an amiable Mae, but before you can get their attention they go inside and shut the door."
            "You jog up and double check the address on the mailbox."
            "One of the numbers has fallen off but upon closer inspection you can see the faint mark of where it used to be. Yup, this has to be Mae's house."
            "You approach the door and prepare to knock on it, but something makes you stop and reconsider."
            "Mae isn't exactly expecting you and it might be freaky to have someone you only recently met show up at your doorstep uninvited like this."
            "You briefly think about just leaving the wallet on the doorstep, ringing the bell and running off."
            "However, your curiosity gets the better of you."
            "What's Lori doing at Mae's house this late at night? And what's that delightful smell coming from inside?"
            "Aromas of home cooking waft through the air, tingling your nostrils and filling you with warmth. Lost in the moment, you hardly notice your finger reaching up to the doorbell."
            "*Ding dong*"
            "The pleasant chime echoes throughout the interior. A moment later, a confused Mae opens the door with a sheepish Lori hiding behind her."

            show lori anxious2 flip at left:
                yalign loriheight
                xalign .15
            show mae freakout flip at left:
                yalign maeheight
                xalign 0.0
            with dissolve

            mae "[newname]? What are you doing here? How did you even know I lived here?"

            "You try to ignore the food and bring your attention back to the matter at hand."
            "Play it cool, [newname], you have a perfectly reasonable reason to be here. And besides, you'll only be here for a minute."

            player "Hey sorry to bother you, but I found your wallet lying on the sidewalk. It had your address in it so I came to return it."

            "You hold the wallet out for her. Mae takes it and looks inside, verifying it is in fact hers."

            show mae panic flip

            mae "Wow, I didn't even know I lost this. Thanks, [newname]!"

            show mae happy flip

            "Her demeanor visibly brightens now that she's reunited with her wallet. Lori pokes her head out and waves to you."

            show lori neutral flip:
                yalign loriheight
                xalign .26
            with move
            show mae neutral flip

            lori "Hi [newname]!"

            player "Hey Lori! Having dinner with the Borowskis tonight?"

            lori "Yup!"

            candy "Mae honey, who's at the door?"

            show candy neutral at right with dissolve

            "Mrs. Borowski comes into view as she leans around a corner. Seeing you, she puts on a cheerful face and comes up behind Lori and Mae."

            candy "Why hello again, [newname]! To what do we owe the pleasure?"

            player "Just returning something of Mae's."

            candy "Mae, did you lose your wallet again?"

            show mae angry flip

            mae "Mom!"

            candy "What? I can't count the number of times you've lost that thing. Did you tell [himherthem] thank you?"

            show mae grump flip

            mae "Yes Mom, I'm not five anymore. I know how to talk to people."

            "Lori stifles a giggle. Poor Mae, her mother is too sweet for her own good."

            candy "You know, [newname], if you'd like you're welcome to have dinner with us tonight! I'm just about finished making a big pot of zuppa toscana!"

            "You can see it on Mae's face, she's embarrassed and you *are* kind of interrupting her thing with Lori tonight. You ought to get going and leave them be."

            player "Well I..."

            candy "Oh don't be shy dear! I insist!"

            "Well that settles it, you guess. It's not like you can say no to a kind old lady offering you food."
            "She invites you inside and walks you through the kitchen to the dining area with Lori and Mae in tow."

            mae "..."

            lori "What?"

            mae "Nothing."

            scene bg maekitchen with fade
            play music "music/Stagnant_Tone-down.mp3" fadein 1.0

            "The dining table is small and square shaped with only four chairs. You awkwardly take a seat adjacent to Lori and across from Mae."
            "Mrs. Borowski goes to the stove to stir the pot with a ladle before turning off the burner."

            show candy neutral at right
            show lori neutral flip at left:
                yalign loriheight
                xalign .26
            show mae sad1 flip at left:
                yalign maeheight
                xalign 0.0
            with dissolve

            candy "You all sit tight and I'll have a bowl out for everyone in just a minute!"

            mae "Aren't we gonna wait for Dad to come home?"

            candy "Not tonight, hun. Stan called and said he'd be working a little late and to go ahead and have dinner without him."

            mae "Oh."

            "There's another awkward pause as Mrs. Borowski takes a tray of toasted bread out of the oven. Luckily Lori thinks of something to say to end the silence."

            lori "So whatchya been up to today, [newname]?"

            player "Just exploring town. Getting used to the layout, that sort of thing. That's how I ended up stumbling upon Mae's wallet."

            "Mrs. Borowski steps in to set a steaming bowl of soup in front of you. The spices are enough to make your eyes water."

            candy "And we're very glad you did!"
            candy "Nobody wants to spend a sleepover night worrying about identity theft and cancelling all their credit cards."

            player "A sleepover? Ah, so that's why you're here tonight, Lori."

            lori "Uh huh! Mae and I are gonna watch movies and paint each others nails later."

            player "Sounds like a good time!"

            "Mrs. Borowski finishes setting bowls and silverware for everyone then places a dish full of sliced bread in the center of the table."

            show mae neutral flip

            candy "Go ahead and dig in!"

            lori "Thank you, Mrs. Borowski!"

            player "Yeah, thanks!"

            candy "You're very welcome!"

            "You flash her a grateful smile as you raise your spoon, giving it a quick blow before you take in your first mouthful of kale, bacon, and broth."
            "The spice has a strong kick to it that accentuates the meat, and the soaked kale rounds out the flavor with a touch of earthiness."
            "Unfortunate that it scalds your tongue however, so you're forced to grab a slice of bread and nibble on it while you wait for it to cool. The others seem to have the same idea."
            "Eventually you brave another spoonful, this time scooping up a chunk of potato and a bit of sausage. Both are incredibly soft and easy to chew after brewing in a pot for hours."
            "After a few more spoonfuls, the red pepper loses its edge and you can appreciate the underlying flavors. There's actually a lot of sweetness buried within, not unlike a sweet and sour soup."
            "And there's something in particular that you can't quite identify that makes it unique and truly memorable."

            candy "How are you liking it, [newname]?"

            player "It's amazing! I wish I could cook this well!"

            candy "Heeheehee! The secret's in the ginger root!"

            "You can tell she's got a lot of pride in her cooking by the way she looks at you."
            "And it's clearly deserved, judging by the dish she's graciously provided you tonight."
            "What's more, the way she's treating you feels alien."
            "It's as if she's treating you like you're... family?"
            "As you all finish your dinner, she engages you and Lori and Mae in small talk that she actually seems interested in and to care about."
            "Like you were all her own loving children."
            "Well Mae obviously is, but the way Mrs. Borowski acts, an outsider might think you and Lori were as well."

            candy "...and have you seen the most recent painting Mae has been working on?"

            player "I haven't really seen any of Mae's artwork yet."

            candy "You should! She's improved so much in the past few years, she could be the next Picasso!"

            show mae grump flip

            "Mae groans."

            mae "It's not that good."

            candy "Nonsense! I bet an art collector would pay a high price to have it in their collection!"
            candy "In fact, why don't you go show [newname] your room so they can see your art while I take care of the dishes?"

            mae "...Fine."

            #transition to mae's bedroom
            scene bg maebedroom with dissolve

            "Mae's room is messy and cluttered with all kinds of posters and pictures on the walls. It's certainly got a rebellious vibe to it, similar to how movies like to depict every teenager's bedroom."
            "She's even got a bass in here."
            "Mae walks over to the easel next to the nightstand and gestures to it."

            show mae grump flip at left with dissolve

            mae "It's not finished yet but here it is."

            "An ominous head floating in a dark, starry void with glowing eyes stares back at you."

            menu:
                "I like it.":
                    #+1 Mae AP
                    player "Very nice. I like it a lot."

                    show mae sad1 flip

                    mae "Meh, it's nothing special..."

                    player "Well I think your mother was right, it belongs in a museum!"

                    show mae skeptical flip
                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "\"So do you!\""

                    show mae skeptical flip

                    "You and Lori bust out laughing."
                    "..."

                    show mae laugh flip

                    "Even Mae can't help but smirk at yours and Lori's silly movie references."

                    mae "Heheh."

                    show mae neutral flip

                    mae "Anyway, I'm not very happy with how this one turned out. I'm not sure I'll ever get around to finishing it."

                "It's creepy.":

                    player "It's creepy."

                    show mae angry flip

                    mae "It's supposed to be. That's the whole point."

                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "Creepy is good! I like creepy."

                    player "It kinda disturbs me."

                    show mae sad1 flip

                    mae "Meh, I guess it's not for everyone."
                    mae "I'm not very happy with how it turned out either. I probably won't ever get around to finishing it."

                "What inspired you?":

                    player "Very interesting. What inspired you?"

                    mae "Um, nothing in particular. Just came to me in a dream I guess."

                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "Mae gets a lot of inspiration from her dreams. I'm kinda jealous."

                    player "Do you often have spooky dreams?"

                    mae "Yes. No. Kinda. I dunno."
                    mae "Anyway, I'm not very happy with how this one turned out so I'm probably never gonna finish it."

            show lori sad

            lori "Aww..."

            show mae sad1

            mae "It's not the first time I abandoned a project."

            "Mae stares at her painting for a while, seemingly criticizing it in her head."

            show lori nervous

            "Lori patiently waits at her side, watching her with a contagious smile."

            show mae blush

            "Mae eventually lets up and smiles back."

            "Seeing them like that, a thought pops into your mind. You clear your throat."

            player "So... How long have you two been...?"

            show mae freakout

            mae "Huh?"

            show lori anxious3

            lori "Been what?"

            player "You know, like, together?"

            show mae panic flip

            mae "Together?"

            player "Yeah like... as a couple?"

            "A look of realization forms on both of their faces."

            show lori breath
            show mae freakout flip

            lori "Whaaaaaat? You thought Mae and I were dating???"

            mae "We're not- That doesn't even-"

            "Oh god you effed up."

            player "I mean uh... Oops."

            "There is no way you can salvage this."

            "Mae and Lori exchange a glance at each other then giggle among themselves. You contribute little more than an embarrassed chuckle."

            show lori cheeky
            show mae laugh flip

            lori "Hahahaha does it really seem like we're dating? I had no idea!"

            mae "Hahaha yeah we're just really good friends is all!"

            player "Sorry, my mistake! I shouldn't have assumed!"

            show mae neutral flip

            mae "It's alright. In any case, I think we've all had our fill of my weird art. Let's head back downstairs."

            player "Sure."

            scene bg maelivingroom with dissolve
            stop music fadeout 2.0

            show candy neutral flip at left
            show lori neutral at right:
                yalign loriheight
                xalign .725
            show mae neutral at right:
                yalign maeheight
                xalign 1.05
            with dissolve

            "From the lobby you can see Mrs. Borowski washing the dishes in the kitchen sink. The clock on the wall near her shows it's way later than you thought it was."

            player "Hey Mrs. Borowski! I think I'm gonna head home now. Thanks again for the meal!"

            candy "Going home so soon? Stay safe out there!"

            player "I will! Thanks for having me over!"

            hide candy with dissolve

            "You turn to Mae and Lori."

            player "And sorry, I didn't mean to take up so much of your evening."

            mae "It's cool."

            lori "Yeah, it was a pleasant surprise seeing you tonight, [newname]!"

            player "See you guys later!"

            lori "See ya!"

            mae "Bye, [newname]!"

            hide mae
            hide lori
            with dissolve

            "Mae opens the door for you and you give a last friendly wave as you wander into the night back to your house."

            jump returnHomeWeek1

        #"Leave it alone":
            #set flag so can no longer find wallet
            #"You ultimately decide to steer clear of it."
            #"It's not your problem. It's probably just trash someone neglected to find a bin for. You simply keep walking and forget about it."
            #jump locationMenu


label returnHomeDec12:
    #fade to night time in player's home
    "What an exhausting day! Better get some rest sooner than later, you never know what tomorrow might bring."
    "You hop into bed and close your eyes, eagerly awaiting your next outting."
    jump day7

label returnHomeDec13:
    #fade to night time in player's home
    "What an exhausting day! Better get some rest sooner than later, you never know what tomorrow might bring."
    "You hop into bed and close your eyes, eagerly awaiting your next outting."
    jump day8

label returnHomeDec14:
    #fade to night time in player's home
    scene bg black with fade
    "That concludes the demo! Thanks so much for playing! Stay tuned for more to come!"
    "Credits"
    "Project Management, Programming and Writing: Kodiak"
    "Character Designs and Art: Equestria Prevails"
    "Background Art: Coldiru, Eightbyteowl"
    "Music: Tymime"
    "Special Thanks to the Night in the Woods and Love in the Woods teams"
    "Twitter: https://twitter.com/LiitwDev"
    "Licensing info: The contents of this game are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License	https://creativecommons.org/licenses/by-nc-sa/3.0/us/"
    return

label returnHomeWeek1:
    if currentDay == "December 12":
        jump returnHomeDec12 
    elif currentDay == "December 13":
        jump returnHomeDec13
    elif currentDay == "December 14":
        jump returnHomeDec14


label day7:
    # day 7, monday
    $ currentDay = "December 13"
    scene bg home_bedroom_night with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."
    

    jump locationMenu





label day8:
    # day 8, tuesday
    $ currentDay = "December 14"
    #"Another day, a new adventure awaits." or something to that effect. Opportunity to chat with people on messenger or explore house maybe?

    scene bg home_bedroom_night with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    jump locationMenu
    
    

    return
