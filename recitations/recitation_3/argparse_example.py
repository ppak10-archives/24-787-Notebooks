import argparse


def main():
    parser = argparse.ArgumentParser(description='Point Cloud Registration')
    parser.add_argument('--exp_name', type=str, required=True,
                        help='name of experiment')
    parser.add_argument('--batch_size', type=int, default=8,
                        help='Size of batch)')
    parser.add_argument('--test_batch_size', type=int, default=2,
                        help='Size of batch)')
    parser.add_argument('--epochs', type=int, default=100,
                        help='number of episode to train ')
    parser.add_argument('--use_sgd', action='store_true', default=False,
                        help='Use SGD')
    parser.add_argument('--lr', type=float, default=0.001, metavar='LR',
                        help='learning rate (default: 0.001, 0.1 if using sgd)')
    parser.add_argument('--momentum', type=float, default=0.9, metavar='M',
                        help='SGD momentum (default: 0.9)')
    args = parser.parse_args()
    print(args)
    ## assign args.variable_name as you require
    # example
    for _ in range(args.epochs):
        continue
    print(f"Looped for {args.epochs} epochs")

if __name__ == '__main__':
    main()

