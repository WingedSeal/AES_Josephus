import generate_avalanche_data
import generate_time_data

def main():
    n = 10_000
    generate_avalanche_data.main(n)
    generate_time_data.main(n)

if __name__ == "__main__":
    main()