from block import Platform, Spikes, Ground, Grass, HitBox
from settings import Settings as Stg


def level_reader(level, x ,y, entities, platforms):
    # Level initialisation 
    for row in level:                               # All string in level(level find in levels)
        for col in row:                             # Each symbol
            if col == "g":
                #Creating platforms, filling color and printing
                grass = Grass(x, y)
                entities.add(grass)
                platforms.append(grass)

            if col == "s":
                all_boxes = hb_create(x ,y, 6, [16, 0],
                                    [0, 31], [31, 31],
                                    [7, 16], [16, 31],
                                    [23, 16])
                for i in all_boxes:
                    entities.add(i)
                    platforms.append(i)
                spikes = Spikes(x ,y)
                entities.add(spikes)

            if col == "e":
                ground = Ground(x, y)
                entities.add(ground)
                platforms.append(ground)

            x += Stg.PLATFORM_WIDTH                  # For each block creating platform
        y += Stg.PLATFORM_HEIGHT                     # Same, but HEIGHT
        x = 0


def hb_create(x, y, amount, *args):
    """Function for creating HitBoxes.
    x,y = position for element(ex. spikes)
    amount = amount for HitBoxes
    *args = x, y position for HitBoxes regarding element(ex. [0, 16])
    """
    all_hitboxes = []                                # Here located all hitboxes for 1 element(ex. spike)
    count_args = 0

    for i in range(amount):
        hit_box_x = args[count_args][0]
        hit_box_y = args[count_args][1]

        hit_box = HitBox(x+hit_box_x, y+hit_box_y)
        all_hitboxes.append(hit_box)
        count_args += 1

    return all_hitboxes