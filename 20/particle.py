import collections
import operator
import re
import copy

fresh_particles = list()


def add(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1], t1[2]+t2[2]


def get_dist(tuple_):
    return abs(tuple_[0])+abs(tuple_[1])+abs(tuple_[2])


def tick(p):
    p['velocity'] = add(p['velocity'], p['acceleration'])
    p['position'] = add(p['position'], p['velocity'])
    p['dist'] = get_dist(p['position'])
    return p


with open("input1.txt") as f:
    for index, row in enumerate(f):
        p_tuple = tuple([int(x) for x in re.findall('<([^>]+)', row)[0].split(",")])
        v_tuple = tuple([int(x) for x in re.findall('<([^>]+)', row)[1].split(",")])
        a_tuple = tuple([int(x) for x in re.findall('<([^>]+)', row)[2].split(",")])
        fresh_particles.append(dict(id=index, position=p_tuple, velocity=v_tuple, acceleration=a_tuple,
                                    dist=get_dist(p_tuple)))


# part 1
particles = copy.deepcopy(fresh_particles)

for x in range(500):
    for particle in particles:
        particle = tick(particle)

distances = [(x['id'], x['dist']) for x in particles]
print("Particle closest to (0,0,0): ", min(distances, key=operator.itemgetter(1)))

# part 2
particles = copy.deepcopy(fresh_particles)

for x in range(500):
    for particle in particles:
        particle = tick(particle)
    position_list = [x['position'] for x in particles]
    collisions = [t for t, count in collections.Counter(position_list).items() if count > 1]
    particles = [p for p in particles if p['position'] not in collisions]

print("Number of particles surviving particlemageddon: ", len(particles))
