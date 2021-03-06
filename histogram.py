def create_histogram(file, band_size):
    nums = get_nums_from_file(file)
    bands = get_bands(nums, band_size)
    print_histogram(bands)


def get_nums_from_file(file):
    nums = []
    with open(file) as fh:
        for line in fh.readlines():
            nums.append(float(line.strip()))
    return nums


def get_band_for_value(num, band_size):
    """
    Given a number, find the band that the number will be sorted into.
    """
    return num // band_size * band_size


def get_bands(nums, band_size):
    bands = {}
    min_band = get_band_for_value(min(nums), band_size)
    max_band = get_band_for_value(max(nums), band_size)
    current_band = min_band

    while current_band <= max_band:
        bands[current_band] = 0
        current_band += band_size

    for num in nums:
        band = get_band_for_value(num, band_size)
        bands[band] += 1
    return bands


def print_histogram(bands):
    for band in sorted(bands.keys()):
        print(f"{str(band).rjust(5)} | {'*' * bands[band]}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='Create a histogram')
    parser.add_argument('-b', '--band-size', default=10, type=float)
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)

    if file.is_file():
        create_histogram(file, args.band_size)
    else:
        print(f"{file} does not exist!")
        exit(1)
