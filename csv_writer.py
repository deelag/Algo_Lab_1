import csv
import random

if __name__ == '__main__':

    fastening_types = ['Wall', 'Stand']
    manufacturers = ['Ukraine', 'Bulgaria', 'UK', 'US', 'Japan', 'China', 'Poland']

    with open('projector_screens.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(500):
            writer.writerow([random.randint(0, 500), random.randint(0, 500), random.choice(fastening_types),
                             random.choice(manufacturers)])
