'''
/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */
'''
import random

def plusWithDelay():
    
    n = int(input("First number to process: "))
    m = int(input("Second number to process: "))
    
    processing = [
    "Crunching numbers...",
    "Summoning the spirits of mathematicians past...",
    "Convincing the calculator to cooperate...",
    "Tickling the abacus...",
    "Asking Siri for help...",
    "Consulting the oracle of binary digits...",
    "Waking up the sleeping math genie...",
    "Petitioning the math gods for assistance...",
    "Coaxing the computer out of its daydream...",
    "Tick-tock goes the computational clock...",
    "Persuading the algorithms to play nice...",
    "Hoping the math fairy pays a visit...",
    "Bribing the processor with extra coffee...",
    "Negotiating with the quantum realm...",
    "Feeding the hamster that powers the server...",
    "Sending a distress signal to the math superhero...",
    "Sifting through the data haystack for the math needle...",
    "Mixing a potion of arithmetic excellence...",
    "Stirring the cauldron of computational magic...",
    "Summoning the ancient spirits of algebra...",
    "Battling the demons of computational complexity...",
    "Walking the tightrope of mathematical precision...",
    "Dancing with the algorithms in the digital realm...",
    "Balancing equations on the tightrope of logic...",
    "Polishing the gears of the calculation engine...",
    "Taming the wild numbers of the mathematical jungle...",
    "Calibrating the compass of computational correctness...",
    "Debugging the matrix of mathematical mayhem...",
    "Whispering sweet nothings to the CPU...",
    "Communing with the ghosts in the machine...",
    "Harmonizing the symphony of numerical symmetries...",
    "Channeling the mathematical muse for inspiration...",
    "Unraveling the mysteries of the mathematical universe...",
    "Embarking on an epic quest for numerical nirvana...",
    "Transcending the boundaries of mathematical reality...",
    "Flirting with the fringes of numerical absurdity...",
    "Juggling the digits of destiny...",
    "Deciphering the hieroglyphics of calculus...",
    "Venturing into the labyrinth of mathematical logic...",
    "Navigating the treacherous waters of computational chaos...",
    "Braving the storms of statistical uncertainty...",
    "Harnessing the power of mathematical wizardry...",
    "Solving equations like a math ninja...",
    "Conjuring algorithms with a flick of the wand...",
    "Plotting graphs in the cosmic tapestry of numbers...",
    "Wrestling with the serpents of mathematical paradox...",
    "Diving into the abyss of numerical oblivion...",
    "Wielding the sword of mathematical truth...",
    "Riding the waves of numerical turbulence...",
    "Trekking through the wilderness of mathematical conjecture...",
    "Sailing the seas of numerical adventure...",
    "Scaling the peaks of mathematical Everest...",
    "Seeking the treasure of numerical enlightenment...",
    "Planting the seeds of mathematical innovation...",
    "Navigating the maze of mathematical possibilities...",
    "Weaving the threads of numerical destiny...",
    "Exorcising the demons of computational inefficiency...",
    "Slaying the dragons of numerical uncertainty...",
    "Crafting algorithms with the precision of a watchmaker...",
    "Venturing into the unknown territories of numerical exploration...",
    "Building castles in the clouds of mathematical imagination...",
    "Harnessing the power of mathematical sorcery...",
    "Riding the lightning of numerical revelation...",
    "Climbing the ladder of mathematical abstraction...",
    "Sculpting the marble of numerical elegance...",
    "Embracing the chaos of mathematical creativity...",
    "Taming the wild stallion of numerical chaos...",
    "Chasing the unicorn of numerical perfection...",
    "Brewing a potion of mathematical brilliance...",
    "Transmuting leaden equations into golden solutions...",
    "Gazing into the crystal ball of mathematical prophecy...",
    "Summoning the phoenix of mathematical rebirth...",
    "Harnessing the thunderbolt of numerical enlightenment...",
    "Wielding the scepter of mathematical mastery...",
    "Forging a path through the jungle of mathematical complexity...",
    "Casting a spell of numerical clarity...",
    "Navigating the labyrinth of mathematical intricacy...",
    "Dancing with the fractals in the kaleidoscope of numbers...",
    "Conjuring a whirlwind of mathematical ingenuity...",
    "Climbing the staircase of numerical sophistication...",
    "Painting with the colors of mathematical elegance...",
    "Unleashing the hounds of mathematical analysis...",
    "Charting a course through the constellations of number theory...",
    "Whispering the incantations of mathematical insight...",
    "Harnessing the energy of the mathematical cosmos...",
    "Sailing the ship of mathematical discovery...",
    "Traversing the vast expanse of mathematical possibility...",
    "Taming the ferocious beasts of numerical complexity...",
    "Conducting the orchestra of numerical harmony...",
    "Mastering the art of mathematical wizardry...",
    "Weaving a tapestry of numerical wonder...",
    "Casting a net into the ocean of mathematical truth...",
    "Cracking the code of numerical enigma...",
    "Sculpting the clay of mathematical intuition...",
    "Slaying the hydra of numerical confusion...",
    "Diving into the depths of mathematical profundity...",
    "Planting the seeds of mathematical wisdom...",
    "Climbing the mountain of numerical enlightenment...",
    "Sailing the river of mathematical abstraction...",
    "Exploring the caverns of numerical complexity...",
    "Harnessing the power of mathematical insight...",
    "Embracing the beauty of mathematical elegance...",
    "Riding the comet of numerical discovery...",
    "Wielding the sword of mathematical truth...",
    "Conjuring the phoenix of mathematical rebirth...",
    "Casting a spell of numerical enchantment...",
    "Dancing with the spirits of mathematical creativity...",
    "Taming the dragons of numerical chaos...",
    "Navigating the labyrinth of mathematical possibility...",
    "Conquering the peaks of numerical excellence...",
    "Building the cathedral of mathematical understanding...",
    "Cracking the code of numerical mystery...",
    "Harnessing the energy of the mathematical cosmos...",
    "Solving the riddles of numerical complexity...",
    "Weaving the fabric of numerical reality...",
    "Conducting the symphony of mathematical harmony...",
    "Crafting the tools of numerical analysis...",
    "Unraveling the secrets of numerical nature...",
    "Embracing the chaos of mathematical creativity...",
    "Climbing the tower of mathematical abstraction...",
    "Navigating the maze of numerical uncertainty...",
    "Sailing the ship of mathematical discovery...",
    "Taming the wild beasts of numerical chaos...",
    "Embracing the beauty of mathematical elegance...",
    "Mastering the art of mathematical wizardry...",
    "Conjuring the spirits of numerical wisdom...",
    "Forging a path through the jungle of numerical complexity...",
    "Chasing the dragon of numerical perfection...",
    "Sculpting the clay of mathematical intuition...",
    "Unleashing the power of mathematical insight...",
    "Harnessing the forces of numerical nature...",
    "Embracing the symphony of mathematical harmonies...",
    "Wielding the wand of mathematical transformation...",
    "Dancing with the ghosts of mathematical brilliance...",
    "Conjuring the muses of numerical creativity..."]
    
    resultado = n + m
    response = random.randint(0,len(processing)-1)
    print(processing[response])
    for i in range(99999):
        for i in range(999):
            nothing = 0

    return f"The answer is: {resultado}"

print(plusWithDelay())
            