import random
import numpy as np


def find_nearest_excess(positions, excess_value=30):
    min_excess_times = np.full(shape=(positions.shape[0]), fill_value=np.nan)
    for i, walker in enumerate(positions):
        it = np.nditer(walker, flags=['f_index'])
        while not it.finished:
            if abs(it[0]) >= excess_value:
                min_excess_times[i] = it.index
                break
            it.iternext()
        pass
    return min_excess_times[np.logical_not(np.isnan(min_excess_times))].min()


def many_random_walk_ans(walkers_num, steps_num, rand_alg_kind="randint"):
    if rand_alg_kind == "randint":
        steps = np.random.randint(0, 2, size=(walkers_num, steps_num + 1), dtype='int')
        steps = np.where(steps > 0, 1, -1)
    elif rand_alg_kind == "normal":
        steps = np.random.normal(0, 2, size=(walkers_num, steps_num + 1))
        steps = np.where(steps > 0, 1, -1)
    else:
        steps = np.array([[1 if random.randint(0, 1) else -1 for j in range(steps_num + 1)] for i in range(walkers_num)])

    # For initial positions of each walker
    steps[:, 0] = 0

    positions = steps.cumsum(axis=1)

    return positions


def main():
    for rand_alg_kind in ["randint", "normal", "random"]:
        print("Generator '{}':".format(rand_alg_kind))
        positions = many_random_walk_ans(5000, 500, rand_alg_kind=rand_alg_kind)

        print("Min: {}, Max: {}".format(positions.min(), positions.max()))

        print("Nearest value excess time:\n{}\n".format(find_nearest_excess(positions)))

    pass


if __name__ == '__main__':
    main()
