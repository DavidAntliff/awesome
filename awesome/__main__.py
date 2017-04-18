# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/

from .awesome import do_awesome


def main(args=None):
    if args is None:
        import sys
        args = sys.argv[1:]
    do_awesome(2)


if __name__ == "__main__":
    main()
