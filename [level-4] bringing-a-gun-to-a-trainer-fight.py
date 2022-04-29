# Bringing a Gun to a Trainer Fight
# =================================

# Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

# Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

# Write a function solution(dimensions, your_position, trainer_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, given the maximum distance that the beam can travel.

# The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

# For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).

# =================================



from math import ceil, floor, atan2, hypot


def solution(dimension, y_og_pos, t_og_pos, distance):
    # How does that work :

    # Imagine a virtual space where we have the initial room, and around we have the same room but mirrored.
    # So for exemple to the top we have a room using a symmerty using the top line as a symmetry line,
    #   and at the right we have a room using a symmetry using the right line as a symmetry line.
    # Diagonals use two symmetry, or a central symmetry with the corner (same thing)
    # for two room to the left for exemple we flip the room to the left once, and flip it again.
    # So the first room is the same as two room to the left

    # So every line < distance that goes through a trainer in a mirrored room is a way to shot the trainer,
    #  It act the same way as a bounce in a real room.

    y_og_pos = (y_og_pos[0], y_og_pos[1])  # Your original position
    t_og_pos = (t_og_pos[0], t_og_pos[1])  # Trainer original position

    # Number of room to simulate in the x axis
    room_x = (
        ceil(float(distance - y_og_pos[0]) / dimension[0])
        + ceil(float(distance + y_og_pos[0]) / dimension[0])
        + 1
    )
    # Number of room to simulate in the y axis
    room_y = (
        ceil(float(distance - y_og_pos[1]) / dimension[1])
        + ceil(float(distance + y_og_pos[1]) / dimension[1])
        + 1
    )

    x_lefter_room = -(floor(float(room_x / 2)) * dimension[0])
    y_lower_room = -(floor(float(room_y / 2)) * dimension[1])

    beam_angle = {}

    y_in_same_position = not (y_lower_room / dimension[1] % 2)
    start = int(y_lower_room)
    stop = int(y_lower_room + room_y * dimension[1])
    for _y in range(start, stop, dimension[1]):
        if y_in_same_position:
            your_y = _y + y_og_pos[1]
            trainer_y = _y + t_og_pos[1]
            y_in_same_position = False
        else:
            your_y = _y + (dimension[1] - y_og_pos[1])
            trainer_y = _y + (dimension[1] - t_og_pos[1])
            y_in_same_position = True

        x_in_same_position = not (x_lefter_room / dimension[0] % 2)
        start = int(x_lefter_room)
        stop = int(x_lefter_room + room_x * dimension[0])
        for _x in range(start, stop, dimension[0]):
            if x_in_same_position:
                your_x = _x + y_og_pos[0]
                trainer_x = _x + t_og_pos[0]
                x_in_same_position = False
            else:
                your_x = _x + (dimension[0] - y_og_pos[0])
                trainer_x = _x + (dimension[0] - t_og_pos[0])
                x_in_same_position = True

            if (your_x, your_y) != y_og_pos:
                # distance entre y_og_pos et your_x, your_y
                d = hypot(your_x - y_og_pos[0], your_y - y_og_pos[1])
                if d <= distance:
                    beam = atan2(your_y - y_og_pos[1], your_x - y_og_pos[0])
                    if (beam not in beam_angle) or (d < beam_angle[beam][0]):
                        # (distance, your:False / trainer:True)
                        beam_angle[beam] = (d, False, (your_x, your_y))

            d = hypot(trainer_x - y_og_pos[0], trainer_y - y_og_pos[1])
            if d <= distance:
                beam = atan2(trainer_y - y_og_pos[1], trainer_x - y_og_pos[0])
                if (beam not in beam_angle) or (d < beam_angle[beam][0]):
                    # print(trainer_x, trainer_y, end="), (")
                    beam_angle[beam] = (d, True, (trainer_x, trainer_y))

    # print([v[2] for k, v in beam_angle.items() if v[1]])
    return len([beam for beam in beam_angle.values() if beam[1]])
  
 
print(solution((2, 2), (1, 1), (1, 2), 1)) # 1
print(solution([3, 2], [1, 1], [2, 1], 4)) # 7
print(solution([2, 5], [1, 2], [1, 4], 11)) # 27
print(solution([23, 10], [6, 4], [3, 2], 23)) # 8
print(solution([300, 275], [150, 150], [185, 100], 500)) # 9
print(solution([1250, 1250], [1000, 1000], [500, 400], 10000)) # 196
print(solution([10, 10], [4, 4], [3, 3], 5000)) # 739323
