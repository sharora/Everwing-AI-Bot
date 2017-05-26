from pynput.mouse import Button, Controller
import time
import cv2
import numpy as np
import ImageCapture
import ImageFinder
import random
import os
import neat


#Initial Delay Before Memeing Begins
time.sleep(10)


mouse = Controller()
mouse.press(Button.left)
mouse.position = (625, 630)


count=1
goodguys = []
badguys = []
stop = []
firetemp = '/Users/Shreyas/Desktop/GameElements/fireball.png'
greentemp = '/Users/Shreyas/Desktop/GameElements/green.png'
redtemp = '/Users/Shreyas/Desktop/GameElements/orange.png'
okay = '/Users/Shreyas/Desktop/GameElements/okay.png'
Templates ={firetemp:badguys, greentemp:goodguys, redtemp:goodguys, okay:stop}



###Loop Repeat
##def everwingbot(genomes, config):
##    for genome_id, genome in genomes:
##        genome.fitness = 120
##        net = neat.nn.FeedForwardNetwork.create(genome, config)
while True:
    goodguys = []
    badguys = []
    stop = []
    ImageCapture.takeimage()
    boom = ImageCapture.boom
    for i,j in Templates.items():
        img = cv2.imread(i, 0)
        ImageFinder.findimage(boom, img)
        l = ImageFinder.l
        if len(l) > 0:
            obj = l[0::4]
            j.append(obj)
            print(j)
        
    
        

        
def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    for xi, xo in zip(xor_inputs, xor_outputs):
        output = winner_net.activate(xi)
        print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

    node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(eval_genomes, 10)





    
