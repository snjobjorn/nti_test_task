from utils.cascade_update import cascade_update
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_id', type=int, help='ID источника')
    args = parser.parse_args()
    # Выполнение каскадного изменения
    cascade_update(args.source_id)

