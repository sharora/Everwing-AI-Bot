from pynput.mouse import Button, Controller
import time
import cv2
import numpy as np
import ImageCapture
import ImageFinder
import random
import os
import neat
import visualize


#Initial Delay Before Memeing Begins
time.sleep(10)


mouse = Controller()
mouse.position = (625, 600)



count=1
goodguys = []
badguys = []
stop = []
firetemp = cv2.imread('/Users/Shreyas/Desktop/GameElements/fireball.png', 0)
greentemp = cv2.imread('/Users/Shreyas/Desktop/GameElements/green.png', 0)
redtemp = cv2.imread('/Users/Shreyas/Desktop/GameElements/orange.png', 0)
okay = cv2.imread('/Users/Shreyas/Desktop/GameElements/okay.png', 0)

#Loop Repeat
def everwingbot(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 120
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        mouse.press(Button.left)
        time.sleep(10)
        lasttime = time.time()
        while True:
            goodguys = []
            badguys = []
            stop = []
            boom = ImageCapture.takeimage()
            ImageFinder.findimage(boom, redtemp)
            l = ImageFinder.l
            if len(l) > 0:
                obj = l[0::4]
                badguys.append(int(obj))
            elif len(l) == 0:
                badguys.append(int(0,0))
            ImageFinder.findimage(boom, okay)
            l = ImageFinder.l
            if len(l) > 0:
                obj = l[0::4]
                stop.append(obj)
                break
            output = net.activate(badguys)
            mouse.move(output,0)

        genome.fitness = lasttime - time.time()
        mouse.release(Button.left)
        lasttime = time.time()
        mouse.position = (720, 640)
        for i in range(3):
            mouse.press(Button.left)
            mouse.release(Button.left)


                
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
    winner = p.run(everwingbot, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)


    node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(everwingbot, 10)


local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-feedforward')
run(config_path)


    
